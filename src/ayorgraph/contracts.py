"""Execution contracts for graph nodes and deterministic orchestration."""
from dataclasses import dataclass
from typing import Any, Protocol

@dataclass(frozen=True)
class NodeResult:
    node: str
    state: dict[str, Any]

class Node(Protocol):
    name: str
    def run(self, state: dict[str, Any]) -> dict[str, Any]: ...

def validate_state(state: dict[str, Any]) -> None:
    if not isinstance(state, dict):
        raise TypeError("state must be a dictionary")
