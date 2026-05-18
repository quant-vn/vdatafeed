""" Base class for Datafeed HUB (streaming) providers. """
from abc import ABC, abstractmethod


class BaseDatafeedHUB(ABC):
    """
    Abstract base class for a datafeed HUB (streaming).

    All provider HUB implementations must subclass this and implement
    the abstract methods below.

    Attributes:
        api: The API object used by the datafeed HUB.
        token (str): The token used for authentication.
    """
    def __init__(self, api):
        self.api = api
        self.__token: str = None

    @property
    def token(self) -> str:
        """
        Returns the token used for authentication.
        Returns:
            str: The authentication token.
        """
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value

    @abstractmethod
    async def listen(self, args, on_trade_message, on_quote_message):
        """
        Listens for incoming messages from the datafeed.
        Args:
            args: The arguments for the listen method.
            on_trade_message: The callback function to be executed when a trade message is received.
            on_quote_message: The callback function to be executed when a quote message is received.
        Returns:
            NotImplemented
        """
        return NotImplemented
