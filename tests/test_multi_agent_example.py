from examples.multi_agent import run_example


def test_two_agents_cooperate_through_graph_state():
    result = run_example("AyorGraph")

    assert result.values == {
        "topic": "AyorGraph",
        "facts": [
            "AyorGraph models work as explicit graph nodes.",
            "Each node receives and returns State.",
        ],
        "response": (
            "AyorGraph models work as explicit graph nodes. "
            "Each node receives and returns State."
        ),
    }
