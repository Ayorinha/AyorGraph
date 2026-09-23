# Architecture

## Purpose
Stateful agent orchestration.

## Boundaries

```
Input / Adapter
     ↓
Domain Contracts
     ↓
Deterministic Core
     ↓
Validation / Safety
     ↓
Result + Observability
     ↓
External Integration (optional)
```

The domain layer must not require network access, credentials or a specific model/provider for its core tests.

## Reliability principles

- Validate inputs at boundaries.
- Prefer immutable contracts for decisions and evidence.
- Keep provider adapters outside the deterministic core.
- Make failures explicit rather than silently recovering.
- Preserve provenance and auditability where the domain requires it.
- Keep test fixtures synthetic and reproducible.

## CI contract

Every pull request must pass compilation, static checks and tests before merge.
