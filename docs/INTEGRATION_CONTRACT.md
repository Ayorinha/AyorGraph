# AYORAI Integration Contract

## Purpose
This repository is one component of the AYORAI Applied Intelligence ecosystem. Cross-repository integrations must remain deterministic, auditable, testable, and safe by default.

## Integration rules
1. No component trusts model output as an authorization decision.
2. Tool execution is mediated by MCP-Sentinel.
3. Consequential actions can require FlowPilot approval.
4. Retrieval evidence must preserve provenance before generation.
5. TraceMind receives execution metadata without secrets or raw credentials.
6. External services are optional adapters; core tests use deterministic fakes.
7. Every integration boundary has an explicit contract and failure mode.
8. Security failures fail closed.
9. Performance regressions are measured rather than assumed.
10. Production deployment requires readiness evidence.

## Reference flow

AyorGraph → OrbisAgents → MCP-Sentinel → Indexa/Vectoris/PgMind → TraceMind → Ayoris → EdgeMesh

Specialized paths:
- DocuVision → Indexa
- LocalForge → inference/runtime consumers
- InferFlow → performance validation
- DataPulse → data quality and benchmark evidence
- FlowPilot → consequential-action approval

## Definition of integration complete
An integration is complete only when it has:
- a typed boundary;
- deterministic unit tests;
- an integration test with a fake adapter;
- explicit error handling;
- security validation;
- observability hooks;
- documentation;
- CI evidence.
