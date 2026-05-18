"""
vdatafeed: A Python wrapper for Viet Nam Datafeed API.

Supports multiple datafeed providers (SSI, VPS, TCBS, etc.)
via a unified interface.
"""
from .enums import Provider  # noqa: F401
from .datafeed import Datafeed  # noqa: F401
from ._base.config import BaseConfig  # noqa: F401
from ._registry import list_providers  # noqa: F401

# Auto-load all built-in providers
from .providers import ssi  # noqa: F401

# Re-export provider configs for convenience
from .providers.ssi.config import SSIConfig  # noqa: F401
