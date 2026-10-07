import pytest

from examples.performance_fixture import measure_graph_overhead


def test_performance_fixture_is_deterministic_with_injected_clock():
    readings = iter([10.0, 10.2, 10.5])

    result = measure_graph_overhead(iterations=3, clock=lambda: next(readings))

    assert result == {
        "iterations": 3,
        "construction_seconds": pytest.approx(0.2),
        "execution_seconds": pytest.approx(0.3),
        "final_counter": 1,
    }


def test_performance_fixture_requires_positive_iterations():
    with pytest.raises(ValueError, match="iterations must be positive"):
        measure_graph_overhead(iterations=0)
