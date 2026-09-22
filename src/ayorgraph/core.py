from dataclasses import dataclass, field
from typing import Any, Callable

@dataclass
class State:
    values: dict[str, Any] = field(default_factory=dict)

class Graph:
    def __init__(self): self._nodes: dict[str, Callable[[State], State]] = {}
    def node(self, name: str, fn: Callable[[State], State]):
        if name in self._nodes: raise ValueError(f"duplicate node: {name}")
        self._nodes[name]=fn; return self
    def run(self, state: State, order: list[str]) -> State:
        for name in order:
            if name not in self._nodes: raise KeyError(name)
            state=self._nodes[name](state)
        return state
