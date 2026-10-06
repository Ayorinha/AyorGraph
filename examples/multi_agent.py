"""Deterministic two-agent workflow; run after `pip install -e .`."""

import json

from ayorgraph.core import Graph, State


def research_agent(state: State) -> State:
    """Add deterministic facts for the requested topic."""
    topic = str(state.values["topic"])
    facts = [
        f"{topic} models work as explicit graph nodes.",
        "Each node receives and returns State.",
    ]
    return State({**state.values, "facts": facts})


def writer_agent(state: State) -> State:
    """Turn the first agent's facts into a stable response."""
    facts = state.values["facts"]
    response = " ".join(facts)
    return State({**state.values, "response": response})


def build_graph() -> Graph:
    return Graph().node("research_agent", research_agent).node("writer_agent", writer_agent)


def run_example(topic: str = "AyorGraph") -> State:
    return build_graph().run(State({"topic": topic}), ["research_agent", "writer_agent"])


def main() -> None:
    print(json.dumps(run_example().values, indent=2))


if __name__ == "__main__":
    main()
