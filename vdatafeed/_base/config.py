""" Base configuration for datafeed providers. """
from ..utils import BaseModel


class BaseConfig(BaseModel):
    """
    Base configuration class for datafeed providers.

    Each provider should subclass this and define its own
    configuration fields (e.g., API keys, secrets, endpoints).
    """
    pass
