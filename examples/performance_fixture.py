"""Small repeatable fixture for graph construction and execution overhead."""

import json
from time import perf_counter

from ayorgraph.core import Graph, State


def build_fixture_graph() -> Graph:
    return Graph().node(
        "increment",
        lambda state: State({**state.values, "counter": state.values["counter"] + 1}),
    )


def measure_graph_overhead(iterations: int = 1000, clock=perf_counter) -> dict[str, float | int]:
    """Measure construction and execution separately without enforcing thresholds."""
    if iterations <= 0:
        raise ValueError("iterations must be positive")

    construction_started = clock()
    graphs = [build_fixture_graph() for _ in range(iterations)]
    execution_started = clock()

    final_state = State({"counter": 0})
    for graph in graphs:
        final_state = graph.run(State({"counter": 0}), ["increment"])

    finished = clock()
    return {
        "iterations": iterations,
        "construction_seconds": execution_started - construction_started,
        "execution_seconds": finished - execution_started,
        "final_counter": final_state.values["counter"],
    }


def main() -> None:
    print(json.dumps(measure_graph_overhead(), indent=2))


if __name__ == "__main__":
    main()
