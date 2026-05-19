""" Base class for Datafeed API providers. """
from abc import ABC, abstractmethod
from .config import BaseConfig


class BaseDatafeedAPI(ABC):
    """
    Abstract base class for a datafeed API.

    All provider API implementations must subclass this and implement
    the abstract methods below.
    """
    def __init__(self, config: BaseConfig):
        self.config: BaseConfig = config

    @abstractmethod
    def get_token(self) -> str:
        """
        Retrieves the token for authentication.
        Returns:
            str: The authentication token.
        """
        return NotImplemented

    @abstractmethod
    def import_session(self, auth_response: dict):
        """
        Directly import a raw auth response dictionary into the session storage.
        """
        return NotImplemented

    @abstractmethod
    def get_instruments(self, exchange: str = None) -> dict:
        """
        Retrieves the instruments from the data feed.
        Args:
            exchange (str, optional): The exchange to filter the instruments. Defaults to None.
        Returns:
            dict: A dictionary containing the instruments.
        """
        return NotImplemented

    @abstractmethod
    def get_instrument_details(self, instrument: str = None) -> dict:
        """
        Retrieves the details of a specific instrument.
        Args:
            instrument (str): The identifier of the instrument.
        Returns:
            dict: A dictionary containing the details of the instrument.
        """
        return NotImplemented

    @abstractmethod
    def get_indices(self, exchange: str = None) -> dict:
        """
        Retrieves the indices from the data feed for a specific exchange.
        Args:
            exchange (str, optional): The exchange for which to retrieve the indices.
                                      Defaults to None.
        Returns:
            dict: A dictionary containing the indices data.
        """
        return NotImplemented

    @abstractmethod
    def get_indices_instruments(self, index: str = None) -> dict:
        """
        Retrieves the instruments for the specified index.
        Args:
            index (str, optional): The index for which to retrieve the instruments.
                                   Defaults to None.
        Returns:
            dict: A dictionary containing the instruments for the specified index.
        """
        return NotImplemented

    @abstractmethod
    def get_daily_instrument_info(
        self, instrument: str, from_date: str = None, to_date: str = None
    ) -> dict:
        """
        Retrieves daily information for a specific instrument.
        Args:
            instrument (str): The identifier of the instrument.
            from_date (str, optional): The starting date (YYYY-MM-DD) for retrieving information.
                                       Defaults to None.
            to_date (str, optional): The ending date (YYYY-MM-DD) for retrieving information.
                                     Defaults to None.
        Returns:
            dict: A dictionary containing the daily instrument information.
        """
        return NotImplemented

    @abstractmethod
    def get_daily_instruments_info(
        self, from_date: str = None, to_date: str = None
    ) -> dict:
        """
        Retrieves daily instruments information.
        Args:
            from_date (str, optional): The starting date (YYYY-MM-DD) for retrieving information.
                                       Defaults to None.
            to_date (str, optional): The ending date (YYYY-MM-DD) for retrieving information.
                                     Defaults to None.
        Returns:
            dict: A dictionary containing the daily instruments information.
        """
        return NotImplemented

    @abstractmethod
    def get_daily_indices_info(
        self, index: str, from_date: str = None, to_date: str = None
    ) -> dict:
        """
        Retrieves daily indices information.
        Args:
            index (str): The index identifier.
            from_date (str, optional): The starting date (YYYY-MM-DD). Defaults to None.
            to_date (str, optional): The ending date (YYYY-MM-DD). Defaults to None.
        Returns:
            dict: A dictionary containing the daily indices information.
        """
        return NotImplemented

    @abstractmethod
    def get_endofday_ohlcv(
        self, instrument: str = None, from_date: str = None, to_date: str = None
    ) -> dict:
        """
        Retrieves the end-of-day OHLCV (Open, High, Low, Close, Volume) data for a
        specific instrument within a given date range.
        Args:
            instrument (str): The instrument symbol for which to retrieve the OHLCV data.
            from_date (str): The starting date of the date range in the format 'YYYY-MM-DD'.
            to_date (str): The ending date of the date range in the format 'YYYY-MM-DD'.
        Returns:
            dict: A dictionary containing the OHLCV data for the specified
                  instrument and date range.
        """
        return NotImplemented

    @abstractmethod
    def get_intraday_ohlcv(
        self, instrument: str = None, from_date: str = None, to_date: str = None
    ) -> dict:
        """
        Retrieves the intraday OHLCV (Open, High, Low, Close, Volume) data for
        a specific instrument within a given date range.
        Args:
            instrument (str): The instrument symbol. (optional)
            from_date (str): The starting date (YYYY-MM-DD) of the data range. (optional)
            to_date (str): The ending date (YYYY-MM-DD) of the data range. (optional)
        Returns:
            dict: A dictionary containing the intraday OHLCV data.
        """
        return NotImplemented
