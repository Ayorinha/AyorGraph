from ayorgraph.core import AgentGraph

def test_graph():
    graph = AgentGraph()
    graph.add_node("a", lambda x: x + 1)
    graph.add_node("b", lambda x: x * 2)
    graph.add_edge("a", "b")
    assert graph.run("a", 2) == 6
