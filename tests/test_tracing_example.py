import runpy
from pathlib import Path

import pytest

from ayorgraph.execution import run_traced

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "execution_tracing.py"


def test_tracing_preserves_state_and_records_lifecycle():
    traced_node = runpy.run_path(str(EXAMPLE))["traced_node"]
    ticks = iter([10.0, 10.25, 11.0, 11.5])
    events = []
    nodes = {
        "add": traced_node("add", lambda value: value + 1, events, lambda: next(ticks)),
        "double": traced_node("double", lambda value: value * 2, events, lambda: next(ticks)),
    }
    result = run_traced(nodes, 2, ["add", "double"])
    assert result.state == 6
    assert events == [
        {"node": "add", "event": "started"},
        {"node": "add", "event": "completed", "outcome": "ok", "duration_seconds": 0.25},
        {"node": "double", "event": "started"},
        {"node": "double", "event": "completed", "outcome": "ok", "duration_seconds": 0.5},
    ]


def test_tracing_records_failure_and_reraises_original_exception():
    traced_node = runpy.run_path(str(EXAMPLE))["traced_node"]
    ticks = iter([1.0, 1.125])
    events = []
    error = ValueError("invalid input")

    def fail(value):
        raise error

    nodes = {"fail": traced_node("fail", fail, events, lambda: next(ticks))}
    with pytest.raises(ValueError) as caught:
        run_traced(nodes, 2, ["fail"])
    assert caught.value is error
    assert events == [
        {"node": "fail", "event": "started"},
        {"node": "fail", "event": "completed", "outcome": "error",
         "error_type": "ValueError", "duration_seconds": 0.125},
    ]
