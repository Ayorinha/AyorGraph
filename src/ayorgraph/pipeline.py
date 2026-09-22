"""Composable execution pipeline for AYORAI components."""
from collections.abc import Callable
from typing import Any

def compose(stages: list[Callable[[dict[str, Any]], dict[str, Any]]]) -> Callable[[dict[str, Any]], dict[str, Any]]:
    if any(not callable(stage) for stage in stages):
        raise TypeError("all stages must be callable")
    def run(state: dict[str, Any]) -> dict[str, Any]:
        current = dict(state)
        for stage in stages:
            current = stage(current)
            if not isinstance(current, dict):
                raise TypeError("pipeline stages must return dictionaries")
        return current
    return run