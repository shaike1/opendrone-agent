# Technical Debt

**Audit date:** 2026-07-26
**Policy:** Debt records a present gap with a cost and exit test. It is not permission to implement a
feature, and safety risk cannot be silently accepted as ordinary refactoring debt.

## Prioritization model

- **Critical:** blocks trustworthy governance or any increase in operational authority.
- **High:** likely to create unsafe, insecure, irreproducible, or expensive foundations.
- **Medium:** material maintainability or verification weakness before repository growth.
- **Low:** localized clarity or consistency cost.

## Register

| ID | Priority | Debt and evidence | Consequence | Recommended disposition | Exit evidence |
| --- | --- | --- | --- | --- | --- |
| TD-101 | Critical | Canonical architecture says no source exists; roadmap remains Phase 0 while Phase 2 contracts exist | Work can proceed under false authority and reviewers cannot identify the actual gate | Human-owned truth reconciliation; do not rewrite ADR history | Approved phase decision and consistent canonical docs |
| TD-102 | Critical | No Phase 1 requirements, threat model, hazard log, data classification, or acceptance authorities | Port/control decisions lack traceable safety and security basis | Keep adapters, AI, plugins, and hardware blocked | Reviewed artifacts with requirement-control-test traceability |
| TD-103 | Critical | `VehiclePort` exposes consequential commands without identity, authorization, safety, failure, freshness, idempotency, or outcome semantics | A future adapter could turn an unsafe sketch into an operational API | Freeze implementation; redesign from approved simulation use cases | ADR, typed contracts, denial/fault tests, named safety/security approval |
| TD-104 | High | No dependency locks, inventory, vulnerability/license scanning, SBOM, or build provenance | Builds drift and supply-chain exposure is opaque | Adopt ecosystem-specific lock/update and exception policy | Clean reproducible install, scans, inventory, SBOM/provenance evidence |
| TD-105 | High | No automated dependency-boundary enforcement | Framework/vendor imports can erode the core while normal tests pass | Add CI architecture fitness test and negative fixture | CI fails on representative forbidden imports |
| TD-106 | High | Mutable entities validate mainly during construction | Callers can assign invalid identities, collections, states, and observations after creation | Decide aggregate mutation policy before persistence/concurrency | Domain ADR plus invariant/property tests for every mutation path |
| TD-107 | High | No license or private security disclosure policy | Legal use/distribution and responsible vulnerability handling are undefined | Maintainers/legal counsel choose policies before release | Root license and SECURITY policy with owned channel/SLAs |
| TD-108 | High | Development Dockerfiles use reload/dev servers, root users, unpinned resolution, and no healthcheck/hardening | Images may be mistaken for production artifacts | Label as dev-only now; design production packaging only when authorized | Deployment ADR, hardened scanned images, runtime/runbook evidence |
| TD-109 | High | `/health` always returns healthy if handler runs | Orchestrators/users may confuse liveness with readiness or operational safety | Define liveness/readiness/dependency semantics before production | Endpoint contract, degraded cases, probes, tests, docs |
| TD-110 | High | Telemetry values carry no observation timestamp, source, quality, frame metadata, or freshness | Stale/ambiguous data could appear current and safe | Define observation envelope from hazard requirements | Contract ADR and stale/reordered/future-time tests |
| TD-111 | High | Event publisher accepts arbitrary `object`; no audit-event contract exists | Events cannot provide stable schema, privacy controls, compatibility, or traceability | Separate domain events from security/audit evidence | Versioned schema, redaction/retention policy, conformance tests |
| TD-112 | Medium | Application services mutate shared entities without transaction/version/concurrency semantics | Lost updates and ambiguous outcomes when persistence arrives | Keep in-memory scope explicit; define unit-of-work semantics with first store use case | Concurrent/conflict tests and documented outcome contract |
| TD-113 | Medium | Capability attach/detach behavior exists in two services | Policy and error behavior can diverge | Assign one application use-case owner | One canonical path and regression tests |
| TD-114 | Medium | `app/ports` is described as application-owned but is top-level; `app/services` is an empty duplicate namespace | Boundary ownership and navigation become ambiguous | Decide topology through ADR before public growth | Package map updated; obsolete placeholder removed/migrated safely |
| TD-115 | Medium | Frontend has no behavior/accessibility tests and trusts JSON casts | Loading, retry, malformed data, and accessibility regressions escape | Add risk-based component/boundary tests | Automated success/error/race/accessibility cases in CI |
| TD-116 | Medium | Backend tests lack coverage reporting, properties, integration, mutation-invariant, and negative API cases | Blind spots grow without a risk-based verification map | Define layered strategy; avoid arbitrary percentage alone | Traceable test taxonomy and CI reports |
| TD-117 | Medium | CI omits docs links, secrets, dependencies, containers, SAST, and architecture checks | Important regressions remain manual | Stage checks after policy/ownership decisions | Required checks with triage and exception owners |
| TD-118 | Medium | GitHub Actions use mutable major tags | A third-party action change can alter trusted CI execution | Pin reviewed commits and adopt update policy | Immutable pins plus automated reviewed updates |
| TD-119 | Medium | API/frontend duplicate response contracts without runtime validation | Drift or malformed JSON fails late and opaquely | Select schema generation or runtime validation when API grows | Contract compatibility test and malformed-response handling |
| TD-120 | Medium | No SLOs, correlation, tracing, metrics, audit sink, incident/rollback/runbooks | Production failures cannot be detected, diagnosed, or governed | Defer deployment; define operability requirements first | Exercised alerts, dashboards, incident and rollback evidence |
| TD-121 | Medium | No release version ownership, changelog, tags, checksums, signing, support, or compatibility window | `0.1.0` can be mistaken for a supported release | Establish release governance before distribution | Rehearsed release and rollback with provenance |
| TD-122 | Low | Backend README installs `[test]`, which is not declared; Node/tooling versions and install workflows disagree | New contributors encounter avoidable setup failures and non-equivalent checks | Reconcile docs around one supported bootstrap path | Clean-checkout onboarding verification |
| TD-123 | Low | Documentation status is duplicated across canonical docs and many engineering views | Drift recurs and audit cost grows | Define owner/cadence and link rather than restate | Documentation map and zero known contradictions |
| TD-124 | Low | No repository-wide Markdown/link/spelling check | Broken internal references and presentation drift are manual | Add a lightweight docs check after conventions are agreed | CI documentation check with explicit exclusions |

## Debt dependencies

```text
TD-101 governance truth
  -> TD-102 requirements / hazards / threats
     -> TD-103, TD-106, TD-109, TD-110, TD-111 contract hardening
        -> simulation and adapter evidence

TD-104 supply chain + TD-107 legal/security governance
  -> TD-108 production packaging + TD-117 CI security gates
     -> TD-121 release governance
```

Dependency order matters. Implementing scanners before defining ownership produces ignored findings;
hardening vehicle methods before hazards and use cases produces confident but arbitrary contracts.

## Debt controls

- Assign a named human owner and target gate, not an invented deadline.
- Link every closure to a merged revision, exact verification, and required approval.
- Preserve rejected alternatives and compatibility consequences in ADRs.
- Never close safety debt solely through documentation wording, a passing unit test, or AI evaluation.
- Reassess priority after architecture, security, safety, or incident evidence changes.
- Keep accepted residual risk visible with owner, rationale, expiry/review date, and compensating controls.
