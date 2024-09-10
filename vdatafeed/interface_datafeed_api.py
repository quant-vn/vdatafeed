""" Interface for Datafeed API """
from abc import ABC, abstractmethod
from .config import Config


class IDatafeedAPI(ABC):
    """
    Interface for a datafeed API.
    This interface defines the methods that a datafeed API should implement.
    """
    def __init__(self, config: Config):
        self.config: Config = config

    @abstractmethod
    def get_token(self) -> str:
        """
        Retrieves the token for authentication.
        Returns:
            str: The authentication token.
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
        Raises:
            NotImplementedError: This method is not implemented yet.
        """
        return NotImplemented

    @abstractmethod
    def get_instrument_details(self, instrument: str = None) -> dict:
        """
        Retrieves the details of a specific instrument.
        Parameters:
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
        Raises:
            NotImplementedError: This method is not implemented and
                                 should be overridden in a subclass.
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
    def get_daily_instruments_info(
        self, instrument: str = None, from_date: str = None, to_date: str = None
    ) -> dict:
        """
        Retrieves daily instruments information.
        Args:
            instrument (str, optional): The instrument to retrieve information for.
                                        Defaults to None.
            from_date (str, optional): The starting date for retrieving information.
                                       Defaults to None.
            to_date (str, optional): The ending date for retrieving information.
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
            exchange (str, optional): The exchange name. Defaults to None.
            from_date (str, optional): The starting date. Defaults to None.
            to_date (str, optional): The ending date. Defaults to None.
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
        a specific exchange within a given date range.
        Parameters:
        - exchange (str): The name of the exchange. (optional)
        - from_date (str): The starting date of the data range. (optional)
        - to_date (str): The ending date of the data range. (optional)
        Returns:
        - dict: A dictionary containing the intraday OHLCV data.
        Note:
        - If any of the parameters are not provided, the function will return NotImplemented.
        """
        return NotImplemented
