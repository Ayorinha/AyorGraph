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
