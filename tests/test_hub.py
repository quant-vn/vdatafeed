""" Test the datafeed module. """
import asyncio
from vdatafeed import Datafeed, Config, EnumDatafeed


datafeed = Datafeed(
    datafeed=EnumDatafeed.SSI.value,
    config=Config(
        ssi_datafeed_id="",
        ssi_datafeed_secret=""
    )
)


def on_trade_message(msg):
    """
    Handle the incoming trade message.
    Args:
        msg (str): The message received.
    Returns:
        None
    """
    print(f"TRADE: {msg}")


def on_quote_message(msg):
    """
    Handle the incoming quote message.
    Args:
        msg (str): The message received.
    Returns:
        None
    """
    print(f"QUOTE: {msg}")


asyncio.run(
    datafeed.hub.listen(
        input("Please select Symbol(SSI)/Index(VNINDEX/VN30) or list(SSI,VCB): "),
        on_trade_message,
        on_quote_message
    )
)
