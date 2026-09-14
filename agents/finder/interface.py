from __future__ import annotations

from typing import Any

from core.contracts import AgentRequest
from core.state import Stage


def build_request(
    candidates: list[dict[str, Any]],
    *,
    category: str = "",
    marketplace: str = "",
    constraints: dict[str, Any] | None = None,
    task_id: str = "",
) -> AgentRequest:
    """Normalize Finder inputs into the Product Venture Core contract."""
    if not isinstance(candidates, list):
        raise TypeError("candidates must be a list")
    if not all(isinstance(item, dict) for item in candidates):
        raise TypeError("every candidate must be a dict")

    return AgentRequest(
        stage=Stage.MARKET,
        input={
            "category": category,
            "marketplace": marketplace,
            "candidates": candidates,
        },
        constraints=constraints or {},
        task_id=task_id,
        agent_id="finder",
        agent_version="0.1.0",
    )
