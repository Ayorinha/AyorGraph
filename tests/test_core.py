from ayorgraph.core import Graph, State

def test_graph_runs_typed_state_pipeline():
    g=Graph().node("a",lambda s: State({**s.values,"x":1})).node("b",lambda s: State({**s.values,"y":2}))
    assert g.run(State(),["a","b"]).values=={"x":1,"y":2}

def test_duplicate_node_rejected():
    g=Graph().node("a",lambda s:s)
    try: g.node("a",lambda s:s)
    except ValueError: return
    assert False
