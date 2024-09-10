""" Test the datafeed module. """
import asyncio
from vdatafeed import Datafeed, Config


datafeed = Datafeed(
    datafeed='ssi',
    config=Config(
        ssi_datafeed_id="",
        ssi_datafeed_secret=""
    )
)

def on_message(msg):
    """
    Handle the incoming message.
    Args:
        msg (str): The message received.
    Returns:
        None
    """
    print(msg)


asyncio.run(datafeed.hub.listen(input("Please select channel: "), on_message))
print("Listening...")
