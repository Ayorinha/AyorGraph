from ayorgraph.pipeline import compose

def test_pipeline_is_deterministic():
    run=compose([lambda s:{**s,"a":1},lambda s:{**s,"b":2}])
    assert run({}) == {"a":1,"b":2}