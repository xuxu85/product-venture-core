from __future__ import annotations

from typing import Any

from adapters.amazon_native import AmazonNativeProvider
from adapters.h10_provider import H10ProviderNotConfigured


def select_finder_provider(*, h10_enabled: bool = False) -> tuple[Any, dict[str, Any]]:
    """Select the strongest available provider without silently inventing data."""
    if h10_enabled:
        provider = H10ProviderNotConfigured()
        health = provider.health()
        if health["status"] == "READY":
            return provider, health

    provider = AmazonNativeProvider()
    return provider, {
        **provider.health(),
        "mode": "DEGRADED",
        "fallback_reason": "H10 not activated",
    }
