# Pain Agent Boundary

The Pain agent is an analysis boundary, not a data-acquisition engine.

## Input

`AgentRequest(stage=PAIN)` with `input.evidence` as a list of verified evidence records.

## Output

Return an `AgentResult` containing:

- `decision`: PASS / FAIL / PIVOT
- `output.pain_cards`: structured pain cards
- `evidence`: supporting source records
- `invalidation_conditions`: measurable conditions for invalidation
- `next_stage`: only when appropriate; the Router remains authoritative

## Canonical pain-card fields

Each pain card should contain, when supported by evidence:

- `consumer`
- `pain`
- `evidence`
- `source`
- `frequency`
- `affected_product`
- `price`
- `confidence`

Missing evidence stays missing. Do not fabricate frequency, price, or confidence.

## Execution boundary

Amazon/browser/BrowserAct/H10 collection happens outside this agent. Providers and acquisition mechanisms are replaceable behind adapters. This package consumes their verified output and converts it into the PAIN-stage contract.
