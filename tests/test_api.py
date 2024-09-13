""" Test the datafeed module. """

from vdatafeed import Datafeed, Config

datafeed = Datafeed(
    datafeed='ssi',
    config=Config(
        ssi_datafeed_id="",
        ssi_datafeed_secret=""
    )
)

print(datafeed.api.get_token())
print(datafeed.api.get_instruments())
print(datafeed.api.get_instrument_details("SSI"))

print(datafeed.api.get_indices())
print(datafeed.api.get_indices_instruments("VN30"))

print(datafeed.api.get_daily_instruments_info(instrument="SSI", from_date="2024-09-01", to_date="2024-09-09"))  # noqa  # pylint: disable=all
print(datafeed.api.get_daily_instruments_info(from_date="2024-09-09", to_date="2024-09-09"))
print(datafeed.api.get_daily_indices_info(index="VN30", from_date="2024-09-01", to_date="2024-09-09"))  # noqa # pylint: disable=all

print(datafeed.api.get_endofday_ohlcv(instrument="SSI", from_date="2024-09-01", to_date="2024-09-09"))  # noqa # pylint: disable=all
print(datafeed.api.get_intraday_ohlcv(instrument="SSI", from_date="2024-09-01", to_date="2024-09-09"))  # noqa # pylint: disable=all