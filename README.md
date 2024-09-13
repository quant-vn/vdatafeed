
# vDatafeed
vDatafeed: A Python wrapper for Viet Nam Datafeed API

![PyPI - Version](https://img.shields.io/pypi/v/vdatafeed)
![Python Version](https://img.shields.io/pypi/pyversions/vdatafeed)
![PyPI - Downloads](https://img.shields.io/pypi/dm/vdatafeed)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## Installation
```bash
pip install vdatafeed
```

## Usage

### Financial data

```python
from vdatafeed import Datafeed, Config


datafeed = Datafeed(
    datafeed='ssi',
    config=Config(
        ssi_datafeed_id="<SSI_DATAFEED_ID>",
        ssi_datafeed_secret="<SSI_DATAFEED_SECRET>"
    )
)

# Get list of instruments
datafeed.api.get_instruments()
# Get instrument details
datafeed.api.get_instrument_details("SSI")
# Get list of indices
datafeed.api.get_indices()
# Get list of instruments in an index
datafeed.api.get_indices_instruments("VN30")
# Get daily instruments info
datafeed.api.get_daily_instruments_info(instrument="SSI", from_date="2024-09-01", to_date="2024-09-10")
# Get daily all instruments info
datafeed.api.get_daily_instruments_info(from_date="2024-09-10", to_date="2024-09-10")
# Get daily indices info
datafeed.api.get_daily_indices_info(index="VN30", from_date="2024-09-01", to_date="2024-09-10")
# Get end of day OHLCV
datafeed.api.get_endofday_ohlcv(instrument="SSI", from_date="2024-09-01", to_date="2024-09-10")
# Get intraday OHLCV
datafeed.api.get_intraday_ohlcv(instrument="SSI", from_date="2024-09-01", to_date="2024-09-10")
```

### Streaming data

```python
import asyncio
from vdatafeed import Datafeed, Config


datafeed = Datafeed(
    datafeed='ssi',
    config=Config(
        ssi_datafeed_id="<SSI_DATAFEED_ID>",
        ssi_datafeed_secret="<SSI_DATAFEED_SECRET>"
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

```