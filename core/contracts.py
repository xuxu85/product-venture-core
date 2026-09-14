from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from .state import Decision, Stage

@dataclass(frozen=True)
class AgentRequest:
    stage: Stage
    input: dict[str, Any]
    constraints: dict[str, Any] = field(default_factory=dict)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    task_id: str = ""
    agent_id: str = ""
    agent_version: str = ""

@dataclass(frozen=True)
class AgentResult:
    decision: Decision
    output: dict[str, Any] = field(default_factory=dict)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    invalidation_conditions: list[str] = field(default_factory=list)
    next_stage: Stage | None = None
    task_id: str = ""
    agent_id: str = ""
    agent_version: str = ""
    status: str = "SUCCESS"
    confidence: float | None = None

    def validate(self) -> None:
        if self.status not in {"SUCCESS", "ERROR"}:
            raise ValueError("status must be SUCCESS or ERROR")
        if self.confidence is not None and not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")
        if not self.invalidation_conditions:
            raise ValueError("Every gate result requires an invalidation condition")
