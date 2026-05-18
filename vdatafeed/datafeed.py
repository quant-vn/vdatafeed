""" Datafeed factory — creates provider-specific API and HUB instances. """
from ._base import BaseConfig, BaseDatafeedAPI, BaseDatafeedHUB
from ._registry import get_provider


class Datafeed:
    """
    Factory class that creates the correct API and HUB instances
    based on the selected provider.

    Args:
        provider (str): The provider identifier (e.g., 'ssi', 'vps').
        config (BaseConfig): The provider-specific configuration object.

    Attributes:
        api (BaseDatafeedAPI): The datafeed API object.
        hub (BaseDatafeedHUB): The datafeed HUB (streaming) object.

    Example:
        >>> from vdatafeed import Datafeed, Provider
        >>> from vdatafeed.providers.ssi import SSIConfig
        >>> df = Datafeed(
        ...     provider=Provider.SSI.value,
        ...     config=SSIConfig(consumer_id="...", consumer_secret="...")
        ... )
        >>> df.api.get_instruments()
    """
    def __init__(self, provider: str, config: BaseConfig, show_logs: bool = False) -> None:
        from .utils.logger import configure_logger
        configure_logger(show_logs)
        config_cls, api_cls, hub_cls = get_provider(provider)
        if not isinstance(config, config_cls):
            raise TypeError(
                f"Provider '{provider}' expects config type '{config_cls.__name__}', "
                f"got '{type(config).__name__}'"
            )
        self.__api: BaseDatafeedAPI = api_cls(config)
        self.__api.provider_name = provider
        self.__hub: BaseDatafeedHUB = hub_cls(self.__api)
        self.__hub.provider_name = provider

    @property
    def api(self) -> BaseDatafeedAPI:
        """
        Returns the API object associated with this datafeed.
        Returns:
            BaseDatafeedAPI: The datafeed API object.
        """
        return self.__api

    @property
    def hub(self) -> BaseDatafeedHUB:
        """
        Returns the HUB (streaming) object associated with this datafeed.
        Returns:
            BaseDatafeedHUB: The datafeed HUB object.
        """
        return self.__hub
