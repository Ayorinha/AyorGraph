from ayorgraph.core import AgentGraph

def test_graph_runs():
    g = AgentGraph[int](); g.add_node("a", lambda x: x + 1); g.add_node("b", lambda x: x * 2); g.add_edge("a", "b")
    assert g.run("a", 2) == 6

def test_cycle_is_rejected():
    g = AgentGraph[int](); g.add_node("a", lambda x: x); g.add_node("b", lambda x: x); g.add_edge("a", "b")
    try: g.add_edge("b", "a")
    except ValueError: pass
    else: raise AssertionError("cycle was accepted")
