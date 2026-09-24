"""Local node lifecycle tracing; run from the repository root after pip install -e ."""

import json
from time import perf_counter

from ayorgraph.execution import run_traced


def traced_node(name, function, events, clock=perf_counter):
    """Wrap a node without changing its result or swallowing its exception."""
    def run(state):
        started = clock()
        events.append({"node": name, "event": "started"})
        try:
            result = function(state)
        except Exception as error:
            events.append({
                "node": name,
                "event": "completed",
                "outcome": "error",
                "error_type": type(error).__name__,
                "duration_seconds": clock() - started,
            })
            raise
        events.append({
            "node": name,
            "event": "completed",
            "outcome": "ok",
            "duration_seconds": clock() - started,
        })
        return result
    return run


def main():
    events = []
    nodes = {
        "normalize": traced_node("normalize", lambda text: text.strip().lower(), events),
        "count_words": traced_node("count_words", lambda text: len(text.split()), events),
    }
    result = run_traced(nodes, "  Hello from AyorGraph  ", ["normalize", "count_words"])
    print(json.dumps({"state": result.state, "events": events}, indent=2))


if __name__ == "__main__":
    main()
