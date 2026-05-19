"""
Provider registry for datafeed providers.

Each provider registers itself via `register_provider()` when its module is imported.
The `Datafeed` factory uses `get_provider()` to look up the correct classes.
"""

_PROVIDERS: dict = {}  # {name: (config_cls, api_cls, hub_cls)}


def register_provider(name: str, config_cls, api_cls, hub_cls):
    """
    Register a datafeed provider.

    Args:
        name (str): The provider identifier (e.g., 'ssi', 'vps').
        config_cls: The provider-specific config class (subclass of BaseConfig).
        api_cls: The provider-specific API class (subclass of BaseDatafeedAPI).
        hub_cls: The provider-specific HUB class (subclass of BaseDatafeedHUB).
    """
    _PROVIDERS[name] = (config_cls, api_cls, hub_cls)


def get_provider(name: str):
    """
    Retrieve a registered provider by name.

    Args:
        name (str): The provider identifier.

    Returns:
        tuple: (config_cls, api_cls, hub_cls)

    Raises:
        ValueError: If the provider is not registered.
    """
    if name not in _PROVIDERS:
        available = list(_PROVIDERS.keys())
        raise ValueError(
            f"Unknown provider: '{name}'. Available providers: {available}"
        )
    return _PROVIDERS[name]


def list_providers() -> list:
    """
    List all registered provider names.

    Returns:
        list: List of registered provider name strings.
    """
    return list(_PROVIDERS.keys())
