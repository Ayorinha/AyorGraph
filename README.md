# AyorGraph

> **Graph-based orchestration for reliable, testable, and observable AI agents.**

[![CI](https://github.com/Ayorinha/AyorGraph/actions/workflows/ci.yml/badge.svg)](https://github.com/Ayorinha/AyorGraph/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**AyorGraph** is an open-source engineering project for building AI agent workflows as explicit graphs. Agents, tools, validation steps, and execution paths can be represented as connected components rather than hidden inside a single opaque chain.

The project is developed under **AYORAI · Applied Intelligence**, with a focus on reliable agentic systems, testing, traceability, and controlled execution.

## Why AyorGraph?

As agentic applications become more complex, a workflow can involve multiple agents, tools, decisions, retries, and validation stages. Making those relationships explicit helps developers reason about the system and evolve it safely.

AyorGraph explores a practical foundation for:

- **Agent orchestration** — compose multiple execution components into a graph.
- **Explicit workflows** — make relationships and execution paths visible.
- **Validation** — detect invalid graph definitions before runtime surprises.
- **Testing** — keep core behavior deterministic and regression-tested.
- **Tracing** — make execution behavior easier to inspect and understand.
- **Extensibility** — provide a foundation for agents, tools, integrations, and execution strategies.
- **AI safety** — support controlled, observable execution as the architecture evolves.

## Architecture

A typical workflow can be represented conceptually:

```text
Input → Agent A → Agent B / Tool → Validation → Output
```

The architecture is intentionally explicit: the graph is a first-class representation of the workflow.

## Current Engineering Focus

AyorGraph is actively evolving. Current contribution areas include:

| Area | Examples |
|---|---|
| Graph validation | Invalid definitions, duplicate identifiers, missing connections |
| Multi-agent workflows | Small, deterministic agent compositions |
| Execution tracing | Node lifecycle, duration, outcome |
| Testing | Regression coverage and deterministic fixtures |
| Documentation | Getting started, examples, architecture |
| Performance | Repeatable execution and regression fixtures |
| Security | Controlled execution and safe contribution practices |

See the repository Issues for concrete tasks that can be picked up by contributors.

## Local tracing example

```bash
pip install -e .
python examples/execution_tracing.py
```

This deterministic text pipeline normalizes a fixed input and counts its three
words. Each node emits `started` and `completed` events to an in-memory list,
including its outcome and elapsed seconds measured with `time.perf_counter`.
Durations vary between runs; the node order and final state do not. No model,
credentials or telemetry provider is needed.

The wrapper also records the exception type and duration when a node fails, then
re-raises the original exception. Keep the event list to inspect failed runs.
The example supplements `run_traced` locally; it does not change the library's
event schema or provide a production telemetry backend. Tests inject a clock to
check exact durations without sleeps.

## Contributing

**You don't need to build the whole framework to contribute.**

Good contributions can be small and focused:

- add a test;
- improve documentation;
- create an example;
- fix a bug;
- improve validation;
- add an integration;
- improve observability;
- investigate performance;
- propose an architectural improvement.

Recommended workflow:

```text
Issue → Fork → Branch → Implement → Test → Pull Request → CI → Review → Merge
```

Start with [CONTRIBUTING.md](CONTRIBUTING.md) and look for an open Issue that matches your interests.

## Quality & Security

AyorGraph treats automated validation as part of the development workflow. Changes are expected to include appropriate tests and documentation, and CI provides an automated quality gate for submitted changes.

Security concerns should **not** be disclosed through public Issues. Please follow [SECURITY.md](SECURITY.md).

## Roadmap

The project is evolving toward a broader foundation for agentic systems, including:

- richer graph validation;
- multi-agent coordination;
- execution tracing and observability;
- evaluation and benchmarking;
- tool and integration support;
- stronger security controls;
- production-oriented engineering practices.

The detailed implementation plan is available in [docs/roadmap.md](docs/roadmap.md).

## Project Philosophy

AyorGraph is built around a simple idea:

> **Make agentic systems easier to understand, test, trace, and evolve.**

The project favors explicit contracts, reproducible behavior, automated testing, security-conscious engineering, and incremental development over opaque complexity.

## License

AyorGraph is released under the [MIT License](LICENSE).

---

## Current Status

The repository is maintained as a focused engineering foundation for explicit agent orchestration, validation, tracing and safe execution. CI is configured for pushes to `main` and pull requests targeting `main`.

**AyorGraph · AYORAI · Applied Intelligence**

Built by **Anderson Leon Ayora**
