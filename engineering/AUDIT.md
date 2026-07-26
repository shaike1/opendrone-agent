# Bootstrap Engineering Audit

**Audit date:** 2026-07-26
**Scope:** all 90 tracked/non-generated repository files present at bootstrap; no runtime behavior was
changed. This is a static repository audit, not a safety certification or production-readiness claim.

## Strengths

- The charter clearly prioritizes safety, human authority, evidence, least privilege, and inward
  dependencies.
- Four accepted ADRs explain the domain, application, and port decisions and explicitly constrain
  what each increment does not authorize.
- Domain measurements carry units and reject non-finite/out-of-range data; domain tests exercise
  boundaries and immutability.
- Application services remain framework-independent and their tests require no hardware or network.
- CI covers backend linting, strict typing, tests, frontend lint/format/type/build, and both images.
- The current UI and API accurately present themselves as a development status foundation.

## Weaknesses

- Governance artifacts disagree about whether executable code exists and which phase is current.
- Phase 1 hazard, threat, privacy, regulatory-assumption, and verification artifacts are absent even
  though Phase 2-like domain and port contracts exist.
- Operationally consequential port method names exist without explicit authorization, denial,
  timeout, idempotency, freshness, or safe-failure contracts.
- Dependency installs are not locked; security reporting, license, dependency inventory, SBOM, and
  provenance processes are missing.
- The frontend has no behavioral/component tests, and no integration or safety suites exist.

## Architecture observations

- The implemented backend has recognizable domain, application, ports, API/framework, and assembly
  concerns, but the package names do not fully match the conceptual architecture document.
- `app.ports` is adjacent to rather than nested within `app.application`; ADR-0004 explicitly accepts
  this application-owned location.
- `app.core` mixes configuration and logging infrastructure, while `app.main` is the practical
  composition point for the existing HTTP foundation. These should be documented before expansion.
- The empty `app/services` package overlaps semantically with `app/application/services` and may
  confuse future agents.
- There are no external adapters, persistence, simulator, vehicle SDKs, plugins, AI integrations,
  authentication, authorization, safety engine, or mission execution. Planning must not imply them.

## Maintainability observations

- Small modules, explicit types, dataclasses, protocols, and narrow tests make the backend easy to
  navigate.
- Backend docs and root architecture status have drifted as increments landed.
- API types are duplicated manually in Python and TypeScript; this is acceptable at current scale but
  needs a compatibility strategy before the API expands.
- Broad dependency ranges and absent lockfiles weaken build reproducibility.
- No issue/PR templates or ownership configuration are present; this OS supplies review content but
  does not alter GitHub configuration.

## Testing observations

- Backend tests cover domain construction/invariants, core service workflows, protocol exposure, and
  the two happy-path API endpoints.
- Tests do not currently cover app factory/configuration/log formatter behavior, HTTP failures,
  generated schemas, or cross-layer dependency violations.
- Frontend `npm test` is an alias for TypeScript checking; it does not execute UI behavior tests.
- CI has no coverage threshold, dependency vulnerability scan, secret scan, Markdown/link check,
  contract/integration suite, fault injection, or safety verification.
- Docker builds are checked, but Compose startup and end-to-end service interaction are not.

## Documentation observations

- The charter, AI context, contribution guide, domain model, application layer, ports, and ADRs are
  unusually explicit about non-authority and current limitations.
- `docs/ARCHITECTURE.md` is stale: it describes only an intended system and says source directories
  do not exist. `docs/ROADMAP.md` still calls Phase 0 current.
- `backend/README.md` describes only foundation endpoints and omits the domain/application/ports
  packages; the root README describes the application foundation but not the later architecture.
- No explicit owner or acceptance record accompanies roadmap phase gates.

## Recommended priorities

1. Have maintainers reconcile and approve phase status, architecture reality, scope, and owners.
2. Complete Phase 1 requirements, hazard analysis, threat model, privacy/data classification, and
   verification strategy before implementing any external or vehicle-facing adapter.
3. Establish security disclosure, license, dependency locking/inventory/scanning, and release policy.
4. Add architecture dependency tests and close targeted backend/frontend test gaps.
5. Harden application contracts for identity, authorization, safety decisions, failure semantics,
   time/freshness, and auditability before deterministic simulation work.
