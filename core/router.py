from __future__ import annotations
from .contracts import AgentRequest, AgentResult
from .gates import next_stage

def route(request: AgentRequest, result: AgentResult) -> AgentRequest:
    result.validate()
    expected = next_stage(request.stage, result.decision)
    if result.next_stage is not None and result.next_stage != expected:
        raise ValueError(f"Agent requested {result.next_stage}, but gate policy requires {expected}")
    if result.decision.value != "PASS":
        raise ValueError("route requires a PASS result")
    return AgentRequest(
        task_id=result.task_id or f"{request.task_id}:{expected.value.lower()}",
        agent_id=f"{expected.value.lower()}.input",
        agent_version=result.agent_version or request.agent_version,
        stage=expected,
        input=result.output,
        constraints=request.constraints,
        evidence=result.evidence,
    )
