from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(frozen=True)
class MetricValue:
    """A measured value with explicit provenance; unavailable is represented by None."""

    value: Any = None
    provider: str = ""
    metric: str = ""
    marketplace: str = ""
    period: str = ""
    method: str = ""
    verified: bool = False


H10_METRICS = (
    "revenue30d",
    "units30d",
    "bsr",
    "searchVolume",
    "iqScore",
    "cpr",
    "resultsNumber",
)


@dataclass(frozen=True)
class FinderProviderRecord:
    """Provider-neutral record consumed by Finder scoring/orchestration."""

    asin: str
    title: str = ""
    price: MetricValue = field(default_factory=MetricValue)
    revenue30d: MetricValue = field(default_factory=MetricValue)
    units30d: MetricValue = field(default_factory=MetricValue)
    bsr: MetricValue = field(default_factory=MetricValue)
    review_count: MetricValue = field(default_factory=MetricValue)
    rating: MetricValue = field(default_factory=MetricValue)
    weight: MetricValue = field(default_factory=MetricValue)
    search_volume: MetricValue = field(default_factory=MetricValue)
    iq_score: MetricValue = field(default_factory=MetricValue)
    cpr: MetricValue = field(default_factory=MetricValue)
    results_number: MetricValue = field(default_factory=MetricValue)


class FinderProvider(Protocol):
    """Provider contract. Implementations may be Amazon-native or H10."""

    name: str

    def find_products(self, *, marketplace: str, category: str, keyword: str) -> list[FinderProviderRecord]:
        ...

    def enrich_keywords(self, *, marketplace: str, keywords: list[str]) -> dict[str, dict[str, MetricValue]]:
        ...

    def health(self) -> dict[str, Any]:
        ...


class H10Provider(FinderProvider, Protocol):
    """Future H10 implementation boundary; no credentials or paid dependency here."""

    name: str


class AmazonNativeProvider(FinderProvider, Protocol):
    """Amazon/TinyFish implementation boundary for degraded Finder mode."""

    name: str
