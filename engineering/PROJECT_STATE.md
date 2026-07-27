# Project State

**Snapshot:** 2026-07-27
**Application version:** `0.1.0` (backend package, frontend package, and default runtime setting)
**Roadmap interpretation:** Phase 0 is the only authorized phase. Early Phase 2-like foundation
exists. PR #12 reconciled that inventory, but Phase 0 and Phase 1 exit-gate acceptance are not
recorded; implementation does not approve either gate retroactively.

## Implemented architecture

- A local two-service development stack: FastAPI/Python 3.11 backend and React 19/TypeScript/Vite
  frontend, orchestrated by Docker Compose.
- Backend HTTP interface exposes only `/health` and `/version`; the dashboard consumes both.
- Pure domain package with mission, vehicle, and capability entities; closed state enums; explicit,
  immutable measurement value objects; and validation exceptions.
- Synchronous, in-memory application services coordinate entity creation and descriptive mutation.
  They provide no authorization, durability, safety policy, or execution.
- Application-owned structural protocols define clock, event publication, mission storage, telemetry,
  and vehicle-operation boundaries. No adapters or composition root implement them.
- Accepted ADRs establish Clean Architecture, the Python domain layout, application orchestration,
  ports, and the decision to retain the application-owned `app.ports` topology.
- Dependency-free AST tests enforce inward imports for domain, application, and ports, including
  representative negative fixtures.

## Existing modules

| Area | Reality today | Verification |
| --- | --- | --- |
| `backend/app/domain` | Entities, enums, exceptions, value objects | Isolated pytest coverage |
| `backend/app/application` | Mission, vehicle, capability services; empty DTO namespace | Unit tests, Ruff, MyPy |
| `backend/app/ports` | Five `Protocol` contracts only | Import/export and architecture-boundary tests |
| `backend/app/api`, `models` | FastAPI system routes and Pydantic responses | API tests |
| `backend/app/core`, `main.py` | Environment settings, JSON logging, app assembly | API tests; limited direct tests |
| `frontend/src` | Service-status dashboard, validated fetch client, status hook | Boundary tests; lint, format, typecheck, build |
| CI/tooling | Backend lint/type/test; frontend lint/format/type/build; Docker builds | GitHub Actions workflow |

## Gate and authorization record

The durable roadmap requires Phase 0 approval before Phase 1 and Phase 2 gates. Repository history
contains Phase 2-like contracts and domain code, but no recorded Phase 0 gate acceptance, Phase 1
requirements package, threat model, hazard log, safety requirements, data classification, or
verification strategy. Treat phase status as **Phase 0 only**, not as permission to extend the
existing executable foundation.

PR #12 completed the canonical reconciliation with Shai (`shaike1`) recorded in both maintainer and
architecture-review roles. That was a documented dual-role approval rather than an independent review
and did not accept the Phase 0 exit gate. Phase 1 remains blocked and has no assigned domain, safety,
security, privacy/legal, or verification owners; specialist evidence and independent approvals cannot
be supplied by maintainer designation alone.

The operating roadmap in [`roadmap/roadmap.md`](roadmap/roadmap.md) therefore prioritizes baseline
reconciliation and safety/security requirements before additional executable capability.

## Current risks

1. **Governance concentration:** IMP-001 has a recorded dual-role maintainer/architecture approval,
   not an independent architecture review; Phase 0 exit evidence and specialist ownership remain open.
2. **Gate traceability:** no durable record proves that Phase 0 or Phase 1 exit criteria were accepted.
3. **Premature authority surface:** `VehiclePort` names arm, takeoff, mission execution, return, and
   emergency operations before authorization, failure, freshness, or safety semantics are specified.
   It is a contract only, but future implementation must remain blocked by governance.
4. **Security governance:** no security policy/private disclosure channel, threat model, dependency
   lockfiles, automated dependency scanning, or data classification is present.
5. **Test depth:** backend unit/API tests and focused frontend HTTP-boundary tests are useful, but
   frontend component/accessibility tests, integration tests, coverage policy, and negative backend API
   tests are absent. Architecture dependency tests now cover the protected backend layers.
6. **Release readiness:** no license, changelog/release notes process, version ownership rule,
   artifact provenance, SBOM, release automation, or rollback runbook exists.

## Technical debt

- Define explicit port failure/result semantics, async/streaming expectations, freshness, identity,
  and authorization before any adapter.
- Resolve duplicate service namespace (`app/application/services` and empty `app/services`).
- Establish reproducible dependency resolution; current Dockerfiles and CI install from ranges with
  `pip install`/`npm install` and no committed lockfiles.
- Extend architecture-boundary checks when approved outer packages or new import mechanisms appear.
- Test backend configuration/logging and frontend loading, partial failure, retry, race/unmount, and
  accessibility paths beyond the existing HTTP-boundary tests.
- Make health semantics meaningful before they are used for operational readiness.

## Recommended next epics

1. **E0 — Governance truth reconciliation:** approve the actual phase, correct architecture/status
   documentation, identify decision owners, and close Phase 0 evidence gaps.
2. **E1 — Safety and security requirements baseline:** actors, misuse cases, data classification,
   threat model, preliminary hazard log, traceable requirements, and acceptance authorities.
3. **E2 — Verification and supply-chain baseline:** architecture tests, dependency policy and locks,
   coverage approach, security scanning, license decision, and reproducible evidence.
4. **E3 — Contract hardening for simulation:** only after E0/E1 approval, define safety-governed
   application operations and port semantics before a deterministic simulator adapter.

See [`AUDIT.md`](AUDIT.md) for the complete bootstrap audit.
