# Dependency Rules

## Current package rules

| Source | May depend on | Must not depend on |
| --- | --- | --- |
| `backend/app/domain` | Python standard library; other domain modules | FastAPI/Pydantic, application, ports, API, core, models, SDKs, I/O |
| `backend/app/application` | standard library; domain | FastAPI/Pydantic, API, core, infrastructure/vendor code |
| `backend/app/ports` | standard library; domain | concrete adapters, FastAPI, persistence/transport/vendor SDKs |
| `backend/app/api`, `models` | application-facing/core contracts and frameworks | vehicle SDKs or policy bypasses |
| `backend/app/main.py` | current HTTP assembly dependencies | business policy or direct vehicle operations |
| `frontend/src` | React/browser and HTTP API contract | backend internals, vehicle connections, secrets |

`backend/app/application/dto` and `backend/app/services` are currently empty. Emptiness is not an
implemented capability. No adapter, simulator, persistence, plugin, AI host, or vehicle integration
exists.

## Boundary rules

- Outer layers translate into inward-owned types; inward layers never import outward implementations.
- Only a composition root selects concrete implementations.
- Every consequential request crosses identity, authorization, deterministic safety policy, and
  audit boundaries. No UI, AI host, plugin, or adapter receives a direct vehicle handle.
- Ports contain contracts rather than implementation logic. New methods require a concrete use case,
  failure semantics, compatibility plan, tests, and architecture review.
- Domain tests run without framework boot, network, storage, clock, simulator, or hardware.

## Enforcement plan

Today enforcement is review plus Ruff/MyPy/Pytest. E2 should select an automated import-boundary
check and negative fixture without adding exceptions that normalize violations. Review imports with:

```sh
rg '^(from|import) ' backend/app/domain backend/app/application backend/app/ports
```
