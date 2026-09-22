from dataclasses import dataclass, field
from typing import Any, Callable

@dataclass(frozen=True)
class ExecutionEvent:
    node: str
    status: str

@dataclass
class ExecutionResult:
    state: Any
    events: list[ExecutionEvent] = field(default_factory=list)

def run_traced(nodes: dict[str, Callable[[Any], Any]], state: Any, order: list[str]) -> ExecutionResult:
    current = state
    events: list[ExecutionEvent] = []
    for name in order:
        if name not in nodes:
            raise KeyError(name)
        try:
            current = nodes[name](current)
        except Exception:
            events.append(ExecutionEvent(name, "error"))
            raise
        events.append(ExecutionEvent(name, "ok"))
    return ExecutionResult(current, events)
