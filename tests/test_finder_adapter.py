from adapters.finder_opportunity import normalize_finder_report
from core.state import Decision, Stage
from core.contracts import AgentRequest
from core.router import route


def test_ready_finder_report_normalizes_and_routes():
    report = {
        "category": "Beverage > Water > Electrolyte Water",
        "marketplace": "Amazon.es",
        "date": "2026-09-14",
        "shortlist": [
            {
                "niche": "RTD electrolyte water",
                "score": 72,
                "label": "Strong",
                "metrics": {"searchVolume": 12000, "medRevenue30d": 18000},
                "exampleProducts": [],
            }
        ],
        "runnersUp": [],
        "h10LookupsUsed": 0,
    }
    result = normalize_finder_report(report)
    assert result.decision == Decision.PASS
    assert result.evidence
    request = AgentRequest(
        stage=Stage.MARKET,
        input={"category": report["category"]},
        task_id="finder-cycle-001",
        agent_id="finder",
    )
    next_request = route(request, result)
    assert next_request.stage == Stage.PAIN


def test_empty_shortlist_fails():
    result = normalize_finder_report({"shortlist": []})
    assert result.decision == Decision.FAIL
