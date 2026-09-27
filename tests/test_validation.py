import pytest

from ayorgraph.core import Graph, State


def passthrough(state: State) -> State:
    return state


def test_duplicate_node_identifier_has_deterministic_error():
    graph = Graph().node("agent", passthrough)

    with pytest.raises(ValueError, match=r"^duplicate node: agent$"):
        graph.node("agent", passthrough)


@pytest.mark.parametrize("missing", ["missing", "validator", "tool"])
def test_run_rejects_missing_node_reference_deterministically(missing):
    graph = Graph().node("start", passthrough)

    with pytest.raises(KeyError) as first:
        graph.run(State(), ["start", missing])
    with pytest.raises(KeyError) as second:
        graph.run(State(), ["start", missing])

    assert first.value.args == (missing,)
    assert second.value.args == first.value.args


def test_missing_node_stops_execution_at_invalid_step():
    calls = []

    def first(state: State) -> State:
        calls.append("first")
        return state

    def last(state: State) -> State:
        calls.append("last")
        return state

    graph = Graph().node("first", first).node("last", last)

    with pytest.raises(KeyError, match="missing"):
        graph.run(State(), ["first", "missing", "last"])

    assert calls == ["first"]


def test_empty_execution_order_is_valid_and_preserves_state():
    state = State({"value": 1})

    result = Graph().run(state, [])

    assert result is state
