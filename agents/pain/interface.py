from __future__ import annotations

from typing import Any

from core.contracts import AgentRequest
from core.state import Stage


def build_request(
    evidence: list[dict[str, Any]],
    *,
    constraints: dict[str, Any] | None = None,
    task_id: str = "",
) -> AgentRequest:
    """Normalize Finder evidence into the Pain-stage request contract."""
    if not isinstance(evidence, list):
        raise TypeError("evidence must be a list")
    if not all(isinstance(item, dict) for item in evidence):
        raise TypeError("every evidence item must be a dict")
    return AgentRequest(
        stage=Stage.PAIN,
        input={"evidence": evidence},
        constraints=constraints or {},
        evidence=evidence,
        task_id=task_id,
        agent_id="pain",
        agent_version="0.1.0",
    )
