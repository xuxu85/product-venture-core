from __future__ import annotations

from typing import Any

from .provider_contracts import FinderProviderRecord, MetricValue


class H10ProviderNotConfigured:
    """Explicit placeholder until the H10 account/MCP is activated.

    This is intentionally not a fake H10 client. It preserves the execution
    boundary and returns an auditable unavailable state instead of guessed data.
    """

    name = "h10"

    def health(self) -> dict[str, Any]:
        return {
            "provider": self.name,
            "status": "NOT_CONFIGURED",
            "paid_dependency": True,
            "credentials_present": False,
        }

    def find_products(self, *, marketplace: str, category: str, keyword: str) -> list[FinderProviderRecord]:
        return []

    def enrich_keywords(self, *, marketplace: str, keywords: list[str]) -> dict[str, dict[str, MetricValue]]:
        return {
            keyword: {
                metric: MetricValue(
                    value=None,
                    provider=self.name,
                    metric=metric,
                    marketplace=marketplace,
                    method="h10_mcp",
                    verified=False,
                )
                for metric in ("searchVolume", "iqScore", "cpr", "resultsNumber")
            }
            for keyword in keywords
        }
