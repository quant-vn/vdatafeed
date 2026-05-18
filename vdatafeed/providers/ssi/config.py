""" SSI Datafeed Configuration. """
from typing import Optional
from ..._base.config import BaseConfig


class SSIConfig(BaseConfig):
    """
    Configuration for the SSI datafeed provider.

    Attributes:
        consumer_id (Optional[str]): The SSI consumer ID (API key).
        consumer_secret (Optional[str]): The SSI consumer secret.
    """
    consumer_id: Optional[str] = None
    consumer_secret: Optional[str] = None
