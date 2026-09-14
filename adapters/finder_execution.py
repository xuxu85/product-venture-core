from __future__ import annotations

from typing import Any

from .h10_provider import H10ProviderNotConfigured


QUANTITATIVE_H10_REQUIREMENTS = {
    "black_box": ["revenue30d", "units30d", "bsr"],
    "magnet": ["searchVolume", "iqScore", "cpr", "resultsNumber"],
}


def h10_dependency_report(*, required_metrics: list[str] | None = None) -> dict[str, Any]:
    """Return the exact H10 dependency without claiming unavailable metrics."""
    required = required_metrics or [
        *QUANTITATIVE_H10_REQUIREMENTS["black_box"],
        *QUANTITATIVE_H10_REQUIREMENTS["magnet"],
    ]
    return {
        "provider": "h10",
        "status": H10ProviderNotConfigured().health()["status"],
        "required_metrics": required,
        "capital_required": True,
        "action_when_needed": "Activate H10 MCP/account, authenticate, then run the existing provider adapter; do not change Finder core.",
    }
