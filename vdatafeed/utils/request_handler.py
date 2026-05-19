"""
HTTP Request handler using httpx.
"""
import time
import httpx
from .logger import logger


class RequestHandler:
    """Helper class to perform synchronous GET and POST requests using httpx."""
    def __init__(self) -> None:
        self.__timeout: int = 10

    def get(self, url: str, headers: dict, params: dict, limit: int = 0) -> dict:
        """Perform a synchronous GET request."""
        try:
            logger.info(f"Call ~> GET: {url} params: {params}")
            res = httpx.get(url, headers=headers, params=params, timeout=self.__timeout)
            if limit:
                time.sleep(limit)
            res.raise_for_status()
            return res.json()
        except httpx.HTTPError as e:
            raise e

    def post(self, url: str, headers: dict, data: dict = {}, limit: int = 0) -> dict:
        """Perform a synchronous POST request."""
        try:
            logger.info(f"Call ~> POST: {url} body: {data}")
            if data:
                res = httpx.post(url, headers=headers, json=data, timeout=self.__timeout)
            else:
                res = httpx.post(url, headers=headers, timeout=self.__timeout)
            if limit:
                time.sleep(limit)
            res.raise_for_status()
            return res.json()
        except httpx.HTTPError as e:
            raise e


request_handler = RequestHandler()
