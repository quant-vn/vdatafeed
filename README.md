
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

## Supported Providers

| Provider | Status |
|----------|--------|
| SSI      | ✅ Supported |
| VPS      | 🔜 Coming soon |
| TCBS     | 🔜 Coming soon |

## Usage

### Financial data

```python
from vdatafeed import Datafeed, Provider, SSIConfig


datafeed = Datafeed(
    provider=Provider.SSI.value,
    config=SSIConfig(
        consumer_id="<SSI_CONSUMER_ID>",
        consumer_secret="<SSI_CONSUMER_SECRET>"
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
# Get daily instrument info
datafeed.api.get_daily_instrument_info(instrument="SSI", from_date="2024-09-01", to_date="2024-09-10")
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
from vdatafeed import Datafeed, Provider, SSIConfig


datafeed = Datafeed(
    provider=Provider.SSI.value,
    config=SSIConfig(
        consumer_id="<SSI_CONSUMER_ID>",
        consumer_secret="<SSI_CONSUMER_SECRET>"
    )
)


def on_trade_message(msg):
    print(f"TRADE: {msg}")


def on_quote_message(msg):
    print(f"QUOTE: {msg}")


asyncio.run(
    datafeed.hub.listen(
        input("Please select Symbol(SSI)/Index(VNINDEX/VN30) or list(SSI,VCB): "),
        on_trade_message,
        on_quote_message
    )
)
```

### List available providers

```python
from vdatafeed import list_providers

print(list_providers())  # ['ssi']
```

## Adding a New Provider

To add a new provider (e.g., VPS), create a module under `vdatafeed/providers/vps/`:

```
vdatafeed/providers/vps/
├── __init__.py      # register_provider("vps", VPSConfig, VPSDatafeedAPI, VPSDatafeedHUB)
├── config.py        # VPSConfig(BaseConfig)
├── api.py           # VPSDatafeedAPI(BaseDatafeedAPI)
├── hub.py           # VPSDatafeedHUB(BaseDatafeedHUB)
├── constants.py
└── models.py
```

Then import the provider in `vdatafeed/providers/__init__.py` or `vdatafeed/__init__.py`.