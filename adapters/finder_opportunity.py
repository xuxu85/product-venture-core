from __future__ import annotations

from typing import Any

from core.contracts import AgentResult
from core.state import Decision


REQUIRED_OPPORTUNITY_KEYS = {"niche", "score", "label", "metrics"}


def normalize_finder_report(report: dict[str, Any]) -> AgentResult:
    """Convert a ready-made Finder report into the Core gate contract.

    This adapter does not execute Amazon, H10, Chrome, or the Skill. It only
    normalizes already-produced Finder output. Missing evidence cannot PASS.
    """
    shortlist = report.get("shortlist")
    if not isinstance(shortlist, list):
        raise ValueError("Finder report must contain shortlist[]")

    valid = [x for x in shortlist if isinstance(x, dict) and REQUIRED_OPPORTUNITY_KEYS <= x.keys()]
    evidence = report.get("evidence", [])
    if not isinstance(evidence, list):
        evidence = []

    invalidation = report.get("invalidation_conditions", [])
    if not isinstance(invalidation, list):
        invalidation = []
    if not invalidation:
        invalidation = [
            "Opportunity fails if real marketplace demand/competition evidence cannot be reproduced or the shortlisted niche does not meet the agreed demand gate."
        ]

    decision = Decision.PASS if valid and evidence else Decision.FAIL
    return AgentResult(
        decision=decision,
        output={
            "category": report.get("category"),
            "date": report.get("date"),
            "totals": report.get("totals", {}),
            "shortlist": valid,
            "runnersUp": report.get("runnersUp", []),
            "h10LookupsUsed": report.get("h10LookupsUsed", 0),
        },
        evidence=evidence,
        invalidation_conditions=invalidation,
        task_id=str(report.get("task_id", "")),
        agent_id="product-opportunity-finder-skill",
        agent_version=str(report.get("agent_version", "unknown")),
        confidence=1.0 if decision == Decision.PASS else 0.0,
    )
