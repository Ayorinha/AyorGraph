import pytest
from ayorgraph.pipeline import compose
def test_pipeline_rejects_non_mapping_state():
    with pytest.raises(TypeError): compose([])([])
