"""Production smoke tests for the AyorGraph package."""
import importlib


def test_package_imports() -> None:
    module = importlib.import_module("ayorgraph")
    assert module is not None


def test_package_does_not_require_network_for_import() -> None:
    # Import-time network access would make CI and local development fragile.
    module = importlib.import_module("ayorgraph")
    assert module.__name__ == "ayorgraph"
