from __future__ import annotations

from typing import Any

from .provider_contracts import FinderProviderRecord


class AmazonNativeProvider:
    """Degraded-mode boundary for browser-collected Amazon evidence.

    The provider accepts only externally captured, verified records. It does
    not scrape, infer revenue, or manufacture missing H10 metrics.
    """

    name = "amazon_native"

    def health(self) -> dict[str, Any]:
        return {
            "provider": self.name,
            "status": "READY_FOR_BROWSER_INPUT",
            "paid_dependency": False,
        }

    def find_products(self, *, marketplace: str, category: str, keyword: str) -> list[FinderProviderRecord]:
        raise NotImplementedError("Feed verified TinyFish/Amazon browser output into this boundary")

    def enrich_keywords(self, *, marketplace: str, keywords: list[str]) -> dict[str, dict[str, Any]]:
        return {keyword: {} for keyword in keywords}
