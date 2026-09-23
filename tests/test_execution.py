from ayorgraph.execution import run_traced

def test_run_traced_records_success():
    result = run_traced({"a": lambda x: x + 1, "b": lambda x: x * 2}, 2, ["a", "b"])
    assert result.state == 6
    assert [e.status for e in result.events] == ["ok", "ok"]

def test_run_traced_records_failure():
    try:
        run_traced({"a": lambda x: 1 / 0}, 0, ["a"])
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("expected failure")


def test_run_traced_rejects_unknown_node():
    import pytest

    with pytest.raises(KeyError):
        run_traced({"a": lambda x: x + 1}, 1, ["missing"])


def test_run_traced_stops_after_error():
    calls = []

    def fail(value):
        calls.append("fail")
        raise RuntimeError("boom")

    def should_not_run(value):
        calls.append("unexpected")
        return value

    try:
        run_traced({"fail": fail, "after": should_not_run}, 0, ["fail", "after"])
    except RuntimeError:
        pass
    else:
        raise AssertionError("expected failure")

    assert calls == ["fail"]
