"""
Provider enumerations for vdatafeed.
"""
from .utils import EnumHandler


class Provider(EnumHandler):
    """
    Enum of supported datafeed providers.

    Attributes:
        SSI (str): SSI Securities datafeed.
    """
    SSI = 'ssi'
