""" HUB datafeed for SSI """
import json
from urllib.parse import urlencode

from .constant import HUB_URL, HUB
from ..interface_datafeed_hub import IDatafeedHUB
from ..utils import SocketListener, request_handler


class SSIDatafeedHUB(IDatafeedHUB):
    """
    Datafeed HUB implementation for the SSI datafeed.
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
        listen: Listens for messages from the socket server.
    """
    def __init__(self, api):
        super().__init__(api)
        self.url: str = HUB_URL.replace("wss", "https")
        self.url_hub: str = HUB_URL
        self.headers: dict = {
            "Authorization": self.api.get_token(),
        }
        self.stream_url = self.generate_socket_url()
        self.message_send_to_socket: dict = {
            "H": HUB,
            "M": "SwitchChannels",
            "I": 0,
        }

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
        print(self.connection_data)
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

    async def listen(self, args, on_message):
        """
        Listens for messages from the socket server.
        Args:
            args: The arguments for the listen function.
            on_message: The callback function to handle incoming messages.
        """
        arguments: list = []
        arguments.append(args)
        last_vol: dict = {}
        try:
            socket = SocketListener()
            async with socket.connect_socket_server(self.stream_url, self.headers) as websocket:
                self.message_send_to_socket.update({"A": arguments})
                await websocket.send(json.dumps(self.message_send_to_socket))
                print(f"Subscribed to {self.message_send_to_socket}")
                async for msg in websocket:
                    try:
                        msg = json.loads(msg)
                        if "M" not in msg:
                            continue
                        for i in msg["M"]:
                            if "A" not in i or not i["A"]:
                                continue
                            msg = json.loads(json.loads(i["A"][0]).get("Content"))
                            print(msg)
                            if msg.get("symbol") not in last_vol:
                                last_vol[msg.get("symbol")] = msg.get("LastVol")
                            else:
                                if last_vol[msg.get("symbol")] == msg.get("LastVol"):
                                    continue
                                last_vol[msg.get("symbol")] = msg.get("LastVol")
                            msg = {
                                "datetime":  " ".join([msg.get("TradingDate"), msg.get("Time")]),
                                "symbol": msg.get("Symbol"),
                                "ce": msg.get("Ceiling"),
                                "fl": msg.get("Floor"),
                                "re": msg.get("RefPrice"),
                                "price": msg.get("LastPrice"),
                                "vol": msg.get("LastVol"),
                                "t_vol": msg.get("TotalVol"),
                                "t_val": msg.get("TotalVal"),
                            }
                            on_message(msg)
                    except Exception as e:
                        print(f" Connection error: {e}")
        except Exception as e:
            print(f" Connection error: {e}")
