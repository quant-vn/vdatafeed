# vdatafeed
vDatafeed: A Python wrapper for Viet Nam Datafeed API

## Installation
```bash
pip install vdatafeed
```

## Usage
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
datafeed.api.get_daily_instruments_info(instrument="SSI", from_date="01/09/2024", to_date="10/09/2024")  # noqa  # pylint: disable=all
# Get daily all instruments info
datafeed.api.get_daily_instruments_info(from_date="10/09/2024", to_date="10/09/2024")
# Get daily indices info
datafeed.api.get_daily_indices_info(index="VN30", from_date="01/09/2024", to_date="10/09/2024")  # noqa # pylint: disable=all
# Get end of day OHLCV
datafeed.api.get_endofday_ohlcv(instrument="SSI", from_date="01/09/2024", to_date="10/09/2024")  # noqa # pylint: disable=all
# Get intraday OHLCV
datafeed.api.get_intraday_ohlcv(instrument="SSI", from_date="01/09/2024", to_date="10/09/2024")  # noqa # pylint: disable=all