""" This module defines the interface for a datafeed HUB. """
from abc import ABC, abstractmethod


class IDatafeedHUB(ABC):
    """
    Interface for a datafeed HUB.
    This interface defines the methods and properties that a datafeed HUB should implement.
    Attributes:
        api (object): The API object used by the datafeed HUB.
        token (str): The token used for authentication.
    Methods:
        listen(args): Abstract method for listening to datafeed events.
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
    async def listen(self, args, on_message):
        """
        Listens for incoming messages from the data feed.
        Args:
            args: The arguments for the listen method.
            on_message: The callback function to be executed when a message is received.
        Returns:
            NotImplemented
        """
        return NotImplemented
