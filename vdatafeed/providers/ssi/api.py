""" SSI Datafeed API. """
import os
from datetime import datetime

from ..._base.api import BaseDatafeedAPI
from .config import SSIConfig
from ...utils import jwt_handler, request_handler, session_handler, logger, log_execution_time

from .constants import (
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
from .models import (
    SecuritiesInfo,
    IndexInfo,
    InstrumentInfo,
    IndicesInfo,
    EndOfDayOHLC,
    IntradayOHLC,
    IndexComponentInfo
)


class SSIDatafeedAPI(BaseDatafeedAPI):
    """
    API implementation for the SSI datafeed provider.

    Args:
        config (SSIConfig): The SSI-specific configuration.
    """
    def __init__(self, config: SSIConfig):
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
        account_key = self.config.consumer_id
        if not self.__token:
            sess = session_handler.get_session("ssi", account_key)
            self.__token = sess.get("token")

        if jwt_handler.is_expired(bearer_token=self.__token):
            data: dict = {}
            data.update(
                consumerID=self.config.consumer_id,
                consumerSecret=self.config.consumer_secret
            )
            res = request_handler.post(
                url=self.url_auth, headers=self.__headers, data=data, limit=self.wait
            )
            if res.get("status") == 200:
                access_token = " ".join(["Bearer", res.get("data").get("accessToken")])
                logger.info(f"Access Token: {access_token}")
                session_handler.save_session(
                    provider="ssi",
                    account_key=account_key,
                    token=access_token,
                    auth_response=res
                )
            else:
                access_token = None
                logger.error(f"Failed to get access token: {res}")
            self.__token = access_token
        return self.__token

    def import_session(self, auth_response: dict):
        """
        Directly import a raw auth response dictionary, extracting the accessToken,
        and saving the entire response data to the active multi-account session file.
        """
        if not auth_response or not auth_response.get("data"):
            raise ValueError("Invalid auth response: missing 'data' field")
        
        access_token = " ".join(["Bearer", auth_response.get("data").get("accessToken")])
        self.__token = access_token
        session_handler.save_session(
            provider="ssi",
            account_key=self.config.consumer_id,
            token=access_token,
            auth_response=auth_response
        )
        logger.info(f"Successfully imported auth response for account: {self.config.consumer_id}")

    @log_execution_time
    def get_instruments(self, exchange: str = None) -> dict:
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

    @log_execution_time
    def get_instrument_details(self, instrument: str = None) -> dict:
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

    @log_execution_time
    def get_indices(self, exchange: str = None) -> list:
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

    @log_execution_time
    def get_indices_instruments(self, index: str = None) -> IndexComponentInfo:
        self.__headers.update({"Authorization": self.get_token()})
        params: dict = {
            "indexCode": index,
            "pageIndex": 1,
            "pageSize": 1000
        }
        res = request_handler.get(
            url=self.url_index_component, headers=self.__headers, params=params, limit=self.wait
        )
        if res.get("data"):
            return IndexComponentInfo(**res.get("data")[0])
        return None

    @log_execution_time
    def get_daily_instrument_info(
        self, instrument: str, from_date: str = None, to_date: str = None
    ) -> list:
        if from_date:
            from_date = datetime.strptime(from_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        if to_date:
            to_date = datetime.strptime(to_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        self.__headers.update({"Authorization": self.get_token()})
        params: dict = {
            "symbol": instrument,
            "fromDate": from_date,
            "toDate": to_date,
            "pageSize": 1000,
            "pageIndex": 1
        }
        data: list = []
        total_element: int = 0
        while True:
            logger.info(f"Querying daily stock price for {instrument} with params: {params}")
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

    @log_execution_time
    def get_daily_instruments_info(
        self, from_date: str = None, to_date: str = None
    ) -> list:
        if from_date:
            from_date = datetime.strptime(from_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        if to_date:
            to_date = datetime.strptime(to_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        self.__headers.update({"Authorization": self.get_token()})
        params: dict = {
            "fromDate": from_date,
            "toDate": to_date,
            "pageSize": 1000,
            "pageIndex": 1
        }
        data: list = []
        for exc in self.exchange:
            total_element: int = 0
            params.update(
                pageIndex=1,
                market=exc
            )
            while True:
                logger.info(f"Querying daily stock price for market {exc} with params: {params}")
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

    @log_execution_time
    def get_daily_indices_info(
        self, index: str, from_date: str = None, to_date: str = None
    ) -> list:
        if from_date:
            from_date = datetime.strptime(from_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        if to_date:
            to_date = datetime.strptime(to_date, "%Y-%m-%d").strftime("%d/%m/%Y")
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

    @log_execution_time
    def get_endofday_ohlcv(
        self, instrument: str = None, from_date: str = None, to_date: str = None
    ) -> list:
        if from_date:
            from_date = datetime.strptime(from_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        if to_date:
            to_date = datetime.strptime(to_date, "%Y-%m-%d").strftime("%d/%m/%Y")
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

    @log_execution_time
    def get_intraday_ohlcv(
        self, instrument: str = None, from_date: str = None, to_date: str = None
    ) -> list:
        if from_date:
            from_date = datetime.strptime(from_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        if to_date:
            to_date = datetime.strptime(to_date, "%Y-%m-%d").strftime("%d/%m/%Y")
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
