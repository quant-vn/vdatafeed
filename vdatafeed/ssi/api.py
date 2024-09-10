""" SSI Datafeed API """
from ..interface_datafeed_api import IDatafeedAPI

from ..config import Config
from ..utils import jwt_handler, request_handler

from .constant import (
    API_URL,
    ENDPOINT_AUTH,
    ENDPOINT_SECURITIES,
    ENDPOINT_SECURITIES_DETAIL,
    ENDPOINT_INTRADAY_OHLC,
    ENDPOINT_ENDOFDAY_OHLC,
    ENDPOINT_DAILY_STOCK_PRICE,
    ENDPOINT_DAILY_INDEX,
    ENDPOINT_INDEX_COMPONENT,
    ENDPOINT_INDEX_LIST
)
from .model import (
    SecuritiesInfo,
    IndexInfo,
    InstrumentInfo,
    IndicesInfo,
    EndOfDayOHLC,
    IntradayOHLC
)


class SSIDatafeedAPI(IDatafeedAPI):
    """
    This class represents the API for accessing data from the SSIDatafeed service.
    Args:
        config (Config): The configuration object for the datafeed.
    Attributes:
        url_auth (str): The URL for authentication.
        url_securities (str): The URL for retrieving securities information.
        url_securities_detail (str): The URL for retrieving detailed securities information.
        url_intraday_ohlc (str): The URL for retrieving intraday OHLC data.
        url_endofday_ohlc (str): The URL for retrieving end-of-day OHLC data.
        url_index_list (str): The URL for retrieving the list of indices.
        url_index_component (str): The URL for retrieving the components of an index.
        url_daily_stock_price (str): The URL for retrieving daily stock price data.
        __headers (dict): The headers for the API requests.
        __token (str): The access token for authentication.
        wait (int): The wait time in seconds before sending a request.
        exchange (list): The list of exchanges.
    Methods:
        get_token: Retrieves the access token for authentication.
        get_instruments: Retrieves the list of instruments.
        get_instrument_details: Retrieves the details of a specific instrument.
        get_indices: Retrieves the list of indices.
        get_indices_instruments: Retrieves the list of instruments for a specific index.
        get_daily_instruments_info: Retrieves the daily information for a specific instrument.
    """
    def __init__(self, config: Config):
        super().__init__(config)
        self.url_auth: str = "/".join([API_URL, ENDPOINT_AUTH])
        self.url_securities: str = "/".join([API_URL, ENDPOINT_SECURITIES])
        self.url_securities_detail: str = "/".join([API_URL, ENDPOINT_SECURITIES_DETAIL])
        self.url_intraday_ohlc: str = "/".join([API_URL, ENDPOINT_INTRADAY_OHLC])
        self.url_endofday_ohlc: str = "/".join([API_URL, ENDPOINT_ENDOFDAY_OHLC])
        self.url_index_list: str = "/".join([API_URL, ENDPOINT_INDEX_LIST])
        self.url_index_component: str = "/".join([API_URL, ENDPOINT_INDEX_COMPONENT])
        self.url_daily_stock_price: str = "/".join([API_URL, ENDPOINT_DAILY_STOCK_PRICE])
        self.url_daily_index: str = "/".join([API_URL, ENDPOINT_DAILY_INDEX])
        self.__headers: dict = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.__token: str = None
        self.wait: int = 1  # wait 1 second before sending request
        self.exchange: list = ["HOSE", "HNX", "UPCOM"]

    def get_token(self) -> str:
        """
        Retrieves the access token for authentication.
        Returns:
            str: The access token.
        """
        if jwt_handler.is_expired(bearer_token=self.__token):
            data: dict = {}
            data.update(
                consumerID=self.config.ssi_datafeed_id,
                consumerSecret=self.config.ssi_datafeed_secret
            )
            res = request_handler.post(
                url=self.url_auth, headers=self.__headers, data=data, limit=self.wait
            )
            if res.get("status") == 200:
                access_token = " ".join(["Bearer", res.get("data").get("accessToken")])
            else:
                access_token = None
            self.__token = access_token
        return self.__token

    def get_instruments(self, exchange: str = None) -> dict:
        """
        Retrieves the list of instruments.
        Args:
            exchange (str, optional): The exchange to filter the instruments. Defaults to None.
        Returns:
            dict: The list of instruments.
        """
        exchange = [exchange] or self.exchange
        self.__headers.update({"Authorization": self.get_token()})
        data: list = []
        for e in exchange:
            total_element: int = 0
            params: dict = {
                "Market": e,
                "PageIndex": 1,
                "PageSize": 1000
            }
            while True:
                res = request_handler.get(
                    url=self.url_securities_detail, headers=self.__headers,
                    params=params, limit=self.wait
                )
                if res.get("data"):
                    data += res.get("data")[0].get("RepeatedInfo")
                    total_element += len(res.get("data")[0].get("RepeatedInfo"))
                params.update(PageIndex=params.get("PageIndex") + 1)
                if total_element == res.get("totalRecord"):
                    break
        return [SecuritiesInfo(**i) for i in data]

    def get_instrument_details(self, instrument: str = None) -> dict:
        """
        Retrieves the details of a specific instrument.
        Args:
            instrument (str, optional): The instrument symbol. Defaults to None.
        Returns:
            dict: The details of the instrument.
        """
        self.__headers.update({"Authorization": self.get_token()})
        params: dict = {
            "Symbol": instrument
        }
        res = request_handler.get(
            url=self.url_securities_detail, headers=self.__headers, params=params, limit=self.wait
        )
        if res.get("data"):
            return SecuritiesInfo(**res.get("data")[0].get("RepeatedInfo")[0])
        return None

    def get_indices(self, exchange: str = None) -> list:
        """
        Retrieves the list of indices.
        Args:
            exchange (str, optional): The exchange to filter the indices. Defaults to None.
        Returns:
            dict: The list of indices.
        """
        # ENDPOINT_INDEX
        self.__headers.update({"Authorization": self.get_token()})
        exchange = [exchange] or self.exchange
        list_index: list = []
        for e in exchange:
            params: dict = {
                "Exchange": e,
                "PageIndex": 1,
                "PageSize": 1000
            }
            res = request_handler.get(
                url=self.url_index_list, headers=self.__headers, params=params, limit=self.wait
            )
            if res.get("data"):
                list_index += res.get("data")
        return [IndexInfo(**i) for i in list_index] or None

    def get_indices_instruments(self, index: str = None) -> list:
        """
        Retrieves the list of instruments for a specific index.
        Args:
            index (str, optional): The index code. Defaults to None.
        Returns:
            dict: The list of instruments.
        """
        self.__headers.update({"Authorization": self.get_token()})
        instruments: list = []
        params: dict = {
            "indexCode": index,
            "pageIndex": 1,
            "pageSize": 1000
        }
        res = request_handler.get(
            url=self.url_index_component, headers=self.__headers, params=params, limit=self.wait
        )
        if res.get("data"):
            instruments = [i.get("Isin") for i in res.get("data")[0].get("IndexComponent")]
            return instruments
        return None

    def get_daily_instruments_info(
        self, instrument: str = None, from_date: str = None, to_date: str = None
    ) -> dict:
        """
        Retrieves the daily information for a specific instrument.
        Args:
            instrument (str, optional): The instrument symbol. Defaults to None.
            from_date (str, optional): The start date. Defaults to None.
            to_date (str, optional): The end date. Defaults to None.
        Returns:
            dict: The daily information.
        """
        self.__headers.update({"Authorization": self.get_token()})
        params: dict = {
            "fromDate": from_date,
            "toDate": to_date,
            "pageSize": 1000,
            "pageIndex": 1
        }
        data: list = []
        if instrument:
            total_element: int = 0
            params.update(symbol=instrument)
            while True:
                print(params)
                res = request_handler.get(
                    url=self.url_daily_stock_price, headers=self.__headers,
                    params=params, limit=self.wait
                )
                if res.get("data"):
                    data += res.get("data")
                    total_element += len(res.get("data"))
                params.update(pageIndex=params.get("pageIndex") + 1)
                if total_element == res.get("totalRecord"):
                    break
        else:
            for exchange in self.exchange:
                total_element: int = 0
                params.update(
                    pageIndex=1,
                    market=exchange
                )
                while True:
                    print(params)
                    res = request_handler.get(
                        url=self.url_daily_stock_price, headers=self.__headers,
                        params=params, limit=self.wait
                    )
                    if res.get("data"):
                        data += res.get("data")
                        total_element += len(res.get("data"))
                    params.update(pageIndex=params.get("pageIndex") + 1)
                    if total_element == res.get("totalRecord"):
                        break
        return [InstrumentInfo(**i) for i in data] or None

    def get_daily_indices_info(
        self, index: str, from_date: str = None, to_date: str = None
    ) -> list:
        """
        Retrieves the daily information for a specific index.
        Args:
            exchange (str, optional): The exchange name. Defaults to None.
            from_date (str, optional): The start date. Defaults to None.
            to_date (str, optional): The end date. Defaults to None.
        Returns:
            dict: The daily information.
        """
        self.__headers.update({"Authorization": self.get_token()})
        params: dict = {
            "IndexId": index,
            "fromDate": from_date,
            "toDate": to_date,
            "pageSize": 1000,
            "pageIndex": 1
        }
        data: list = []
        total_element: int = 0
        while True:
            res = request_handler.get(
                url=self.url_daily_index, headers=self.__headers,
                params=params, limit=self.wait
            )
            if res.get("data"):
                data += res.get("data")
                total_element += len(res.get("data"))
            params.update(pageIndex=params.get("pageIndex") + 1)
            if total_element == res.get("totalRecord"):
                break
        return [IndicesInfo(**i) for i in data] or None

    def get_endofday_ohlcv(
        self, instrument: str = None, from_date: str = None, to_date: str = None
    ) -> list:
        """
        Retrieves the end-of-day OHLC data.
        Args:
            instrument (str, optional): The instrument symbol. Defaults to None.
            from_date (str, optional): The start date. Defaults to None.
            to_date (str, optional): The end date. Defaults to None.
        Returns:
            dict: The end-of-day OHLC data.
        """
        self.__headers.update({"Authorization": self.get_token()})
        params: dict = {
            "Symbol": instrument,
            "FromDate": from_date,
            "ToDate": to_date,
            "PageSize": 1000,
            "PageIndex": 1
        }
        res = request_handler.get(
            url=self.url_endofday_ohlc, headers=self.__headers, params=params, limit=self.wait
        )
        data: list = []
        if res.get("data"):
            data = res.get("data")
        return [EndOfDayOHLC(**i) for i in data] or None

    def get_intraday_ohlcv(
        self, instrument: str = None, from_date: str = None, to_date: str = None
    ) -> list:
        """
        Retrieves the intraday OHLC data.
        Args:
            exchange (str, optional): The exchange name. Defaults to None.
            from_date (str, optional): The start date. Defaults to None.
            to_date (str, optional): The end date. Defaults to None.
        Returns:
            dict: The intraday OHLC data.
        """
        self.__headers.update({"Authorization": self.get_token()})
        params: dict = {
            "Symbol": instrument,
            "FromDate": from_date,
            "ToDate": to_date,
            "PageSize": 1000,
            "PageIndex": 1
        }
        res = request_handler.get(
            url=self.url_intraday_ohlc, headers=self.__headers, params=params, limit=self.wait
        )
        data: list = []
        if res.get("data"):
            data = res.get("data")
        return [IntradayOHLC(**i) for i in data] or None
