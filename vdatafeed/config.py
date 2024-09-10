""" Configuration module for the datafeed. """
from typing import Optional

from .utils import BaseModel


class Config(BaseModel):
    """
    Configuration class for the datafeed.

    Attributes:
        ssi_datafeed_id (Optional[str]): The SSI datafeed ID.
        ssi_datafeed_secret (Optional[str]): The SSI datafeed secret.
    """
    # SSI datafeed information
    ssi_datafeed_id: Optional[str] = None
    ssi_datafeed_secret: Optional[str] = None
