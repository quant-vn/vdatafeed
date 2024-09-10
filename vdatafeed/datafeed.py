""" Datafeed module for datafeed API and HUB. """
from .config import Config

from .enum_datafeed import EnumDatafeed
from .interface_datafeed_api import IDatafeedAPI
from .interface_datafeed_hub import IDatafeedHUB

from .ssi import SSIDatafeedAPI, SSIDatafeedHUB


class Datafeed:
    """
    Represents a datafeed object that provides access to a specific datafeed API and datafeed HUB.
    Args:
        datafeed (EnumDatafeed): The type of datafeed to use.
        config (Config): The configuration for the datafeed.
    Attributes:
        api (IDatafeedAPI): The datafeed API object.
        hub (IDatafeedHUB): The datafeed HUB object.
    """
    def __init__(self, datafeed: EnumDatafeed, config: Config) -> None:
        if datafeed == EnumDatafeed.SSI.value:
            self.__api: IDatafeedAPI = SSIDatafeedAPI(config)
            self.__hub: IDatafeedHUB = SSIDatafeedHUB(self.__api)

    @property
    def api(self) -> IDatafeedAPI:
        """
        Returns the IDatafeedAPI object associated with this datafeed.
        Returns:
            IDatafeedAPI: The IDatafeedAPI object associated with this datafeed.
        """
        return self.__api

    @property
    def hub(self) -> IDatafeedHUB:
        """
        Returns the IDatafeedHUB object associated with this datafeed.
        Returns:
            IDatafeedHUB: The IDatafeedHUB object associated with this datafeed.
        """
        return self.__hub
