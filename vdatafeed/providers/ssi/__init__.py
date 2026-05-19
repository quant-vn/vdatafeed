""" SSI Datafeed Provider. """
from .config import SSIConfig
from .api import SSIDatafeedAPI
from .hub import SSIDatafeedHUB

from ..._registry import register_provider

# Auto-register SSI provider when this module is imported
register_provider("ssi", SSIConfig, SSIDatafeedAPI, SSIDatafeedHUB)

__all__ = ["SSIConfig", "SSIDatafeedAPI", "SSIDatafeedHUB"]
