from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Generic, TypeVar
T = TypeVar("T")
Node = Callable[[T], T]
@dataclass
class AgentGraph(Generic[T]):
    nodes: dict[str, Node[T]] = field(default_factory=dict)
    edges: dict[str, str] = field(default_factory=dict)
    def add_node(self, name: str, fn: Node[T]) -> None:
        if not name.strip() or name in self.nodes: raise ValueError("node name must be unique and non-empty")
        self.nodes[name] = fn
    def add_edge(self, source: str, target: str) -> None:
        if source not in self.nodes or target not in self.nodes: raise KeyError("unknown node")
        self.edges[source] = target
        self._assert_acyclic()
    def run(self, start: str, state: T, *, max_steps: int = 32) -> T:
        if start not in self.nodes: raise KeyError(start)
        if max_steps < 1: raise ValueError("max_steps must be positive")
        current = start
        for _ in range(max_steps):
            state = self.nodes[current](state)
            if current not in self.edges: return state
            current = self.edges[current]
        raise RuntimeError("graph exceeded max_steps")
    def _assert_acyclic(self) -> None:
        visiting: set[str] = set(); visited: set[str] = set()
        def visit(node: str) -> None:
            if node in visiting: raise ValueError("graph contains a cycle")
            if node in visited: return
            visiting.add(node)
            if node in self.edges: visit(self.edges[node])
            visiting.remove(node); visited.add(node)
        for node in self.nodes: visit(node)
