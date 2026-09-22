from ayorgraph.contracts import validate_state

def test_validate_state_accepts_mapping():
    validate_state({"input": 1})

def test_validate_state_rejects_non_mapping():
    try: validate_state([])
    except TypeError: return
    raise AssertionError("expected TypeError")
