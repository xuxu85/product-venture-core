from __future__ import annotations
from .state import Decision, Stage

_NEXT = {
    Stage.IDEA: Stage.MARKET,
    Stage.MARKET: Stage.PAIN,
    Stage.PAIN: Stage.OPPORTUNITY,
    Stage.OPPORTUNITY: Stage.PRODUCT_THESIS,
    Stage.PRODUCT_THESIS: Stage.DEMAND_VALIDATION,
    Stage.DEMAND_VALIDATION: Stage.PRODUCT_SPEC,
    Stage.PRODUCT_SPEC: Stage.FORMULA,
    Stage.FORMULA: Stage.ECONOMICS,
    Stage.ECONOMICS: Stage.MANUFACTURING,
    Stage.MANUFACTURING: Stage.PILOT,
    Stage.PILOT: Stage.SALES,
    Stage.SALES: Stage.REPEAT,
    Stage.REPEAT: Stage.SCALE,
}

def next_stage(stage: Stage, decision: Decision) -> Stage:
    if decision == Decision.PASS:
        return _NEXT.get(stage, Stage.STOP)
    return Stage.STOP
