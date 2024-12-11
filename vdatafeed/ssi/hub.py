""" HUB datafeed for SSI with Reconnection """
import json
import asyncio
import random
from urllib.parse import urlencode

from .constant import HUB_URL, HUB
from .model import TradeTick, QuoteTick
from ..interface_datafeed_hub import IDatafeedHUB
from ..utils import SocketListener, request_handler


class SSIDatafeedHUB(IDatafeedHUB):
    """
    Datafeed HUB implementation for the SSI datafeed with improved reconnection.
    Args:
        api: An instance of the API class.
    Attributes:
        url (str): The URL for the datafeed HUB.
        url_hub (str): The URL for the HUB.
        headers (dict): The headers for the API request.
        stream_url (str): The URL for the socket connection.
        message_send_to_socket (dict): The message to send to the socket.
    Methods:
        generate_socket_url: Generates the socket URL for the connection.
        listen: Listens for messages from the socket server with reconnection support.
    """
    def __init__(self, api):
        super().__init__(api)
        self.url: str = HUB_URL.replace("wss", "https")
        self.url_hub: str = HUB_URL
        self.headers: dict = {
            "Authorization": self.api.get_token(),
        }
        self.stream_url = None
        self.message_send_to_socket: dict = {
            "H": HUB,
            "M": "SwitchChannels",
            "I": 0,
        }
        # Reconnection settings
        self.max_reconnect_attempts = 5
        self.base_delay = 1  # Base delay in seconds
        self.max_delay = 60  # Maximum delay between reconnection attempts

    def generate_socket_url(self):
        """
        Generates the socket URL for the connection.
        Returns:
            str: The socket URL.
        """
        self.connection_data: dict = {
            "connectionData": '[{"name": "' + HUB + '"}]',
            "clientProtocol": '1.5',
        }
        self.negotiate_query = urlencode(self.connection_data)
        self.url_negotiate = f"{self.url}/negotiate?{self.negotiate_query}"
        response = request_handler.post(self.url_negotiate, headers=self.headers)
        query = urlencode({
            "transport": "webSockets",
            "connectionToken": response["ConnectionToken"],
            "connectionData": '[{"name": "' + HUB + '"}]',
            "clientProtocol": response["ProtocolVersion"],
        })
        socket_url = f"{self.url_hub}/connect?{query}"
        return socket_url

    def calculate_backoff_delay(self, attempt):
        """
        Calculate exponential backoff delay with jitter.
        Args:
            attempt (int): Current reconnection attempt number.
        Returns:
            float: Delay in seconds before next reconnection attempt.
        """
        # Exponential backoff with full jitter
        delay = min(self.max_delay, self.base_delay * (2 ** attempt))
        jitter = random.uniform(0, delay)
        return jitter

    async def listen(self, args, on_trade_message, on_quote_message):
        """
        Listens for messages from the socket server with automatic reconnection.
        Args:
            args: Comma-separated list of symbols to subscribe to.
            on_trade_message: Callback for trade tick messages.
            on_quote_message: Callback for quote tick messages.
        """
        symbol_list: str = args.split(",")
        arguments: list = []
        arguments.append("X:" + "-".join(symbol_list))
        last_vol: dict = {}
        # Regenerate stream URL for each connection attempt
        for attempt in range(self.max_reconnect_attempts):
            try:
                # Generate a fresh socket URL for each attempt
                self.stream_url = self.generate_socket_url()
                socket = SocketListener()
                async with socket.connect_socket_server(self.stream_url, self.headers) as websocket:
                    print(f"[vDatafeed] WebSocket connected (Attempt {attempt + 1})")
                    # Prepare and send subscription message
                    self.message_send_to_socket.update({"A": arguments})
                    await websocket.send(json.dumps(self.message_send_to_socket))
                    print(f"[vDatafeed] Subscribed to {self.message_send_to_socket}")
                    # Create keepalive task
                    async for msg in websocket:
                        try:
                            msg = json.loads(msg)
                            if "M" not in msg:
                                continue
                            for i in msg["M"]:
                                if "A" not in i or not i["A"]:
                                    continue
                                msg = json.loads(json.loads(i["A"][0]).get("Content"))
                                if msg.get("symbol") not in last_vol:
                                    last_vol[msg.get("symbol")] = msg.get("TotalVol")
                                else:
                                    if last_vol[msg.get("symbol")] == msg.get("TotalVol"):
                                        on_quote_message(QuoteTick(**msg))
                                        continue
                                    last_vol[msg.get("symbol")] = msg.get("TotalVol")
                                on_trade_message(TradeTick(**msg))
                            attempt = 0
                        except Exception as e:
                            print(f"[vDatafeed] Message processing error: {e}")
            except Exception as e:
                print(f"[vDatafeed] Connection error: {e}")
                # If this was the last attempt, raise the exception
                if attempt == self.max_reconnect_attempts - 1:
                    raise
                # Calculate backoff delay
                delay = self.calculate_backoff_delay(attempt)
                print(f"[vDatafeed] Reconnecting in {delay:.2f} seconds...")
                # Wait before trying to reconnect
                await asyncio.sleep(delay)
        print("[vDatafeed] Maximum reconnection attempts reached")
