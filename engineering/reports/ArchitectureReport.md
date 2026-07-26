# Architecture Report

**Audit date:** 2026-07-26
**Scope:** Entire tracked repository at `58fb384`
**Verdict:** Sound architectural intent, partially realized boundaries, not ready for an operational adapter or autonomous behavior.

## Executive assessment

OpenDrone Agent has an unusually clear architectural direction for an early repository. `PROJECT.md`,
`docs/ARCHITECTURE.md`, and ADR-0001 consistently require inward dependencies, explicit authority,
simulation before hardware, and separation of AI from actuators. The pure Python domain, synchronous
application services, and Protocol-based ports largely conform to ADRs 0002–0004.

The implementation is nevertheless ahead of its governance baseline. The canonical architecture still
calls the source layout proposed and says no source directories exist, while domain, application, port,
API, and frontend code are present. The roadmap still identifies Phase 0 as current even though Phase 2
contracts have been introduced without repository evidence that the Phase 0 and Phase 1 gates were
accepted. This is a control-plane defect, not merely stale wording: contributors cannot reliably tell
which work is authorized.

The present runtime is a development status application, not a drone agent. There are no adapters,
composition root for operational dependencies, safety-policy implementation, authorization boundary,
AI integration, plugin runtime, persistence, simulator, or vehicle connection. That narrowness is a
strength and must be preserved until prerequisites are approved.

## Repository model

| Area | Current responsibility | Architectural classification | Assessment |
| --- | --- | --- | --- |
| `backend/app/domain` | Missions, vehicles, capabilities, measurements, validation errors | Domain | Pure standard-library Python; strongest boundary |
| `backend/app/application` | In-memory entity creation, association, and descriptive updates | Application | Framework-free, but not yet use-case/transaction boundaries |
| `backend/app/ports` | Vehicle, telemetry, storage, clock, and event contracts | Application-owned ports | Dependency direction is correct; semantics are premature |
| `backend/app/api`, `models`, `core`, `main.py` | Health/version HTTP delivery and process configuration | Interface/framework edge and bootstrap | Appropriately isolated from domain behavior |
| `frontend/src` | Development service-status UI | Driver/UI | Small and separated; its API contract is duplicated manually |
| Docker/Compose/Vite | Development execution and proxying | Infrastructure | Development-oriented, not production deployment |
| `engineering/` and `docs/` | Governance and intended design | Engineering control plane | Strong breadth but canonical drift and duplicated status views |

## Clean Architecture and layering

### What is working

- Domain imports remain within the standard library and `app.domain`; no FastAPI, Pydantic, SDK, I/O,
  or deployment concern leaks inward.
- Application services import only domain objects and errors. They are synchronous and testable without
  frameworks, networks, storage, or hardware.
- Ports use structural protocols and domain vocabulary. No concrete adapter is disguised as a port.
- FastAPI route and response models are outside the domain. The status API does not expose operational
  methods.
- The frontend does not know Python internals and communicates only over two status endpoints.

### Boundary weaknesses

1. **Ports are not located under `app.application`.** Documentation calls them application-owned, but
   `app.ports` is a sibling package. This does not reverse dependencies today, yet package topology
   weakens ownership clarity and allows application services to remain disconnected from their ports.
   Resolve through an ADR before the package becomes a public compatibility surface.
2. **Application services are mutable transaction scripts without boundary inputs or outcomes.** They
   accept live entities, mutate public fields, and return the same object. There is no requester,
   authorization decision, unit of work, concurrency/version contract, durable outcome, or audit event.
   This is acceptable only for the explicitly descriptive increment.
3. **Domain invariants are construction-time rather than mutation-safe.** Mutable dataclasses allow
   callers to assign invalid `id`, `name`, state, capability collections, or observations after
   `__post_init__`. Services validate some state types but not every assignment. Domain purity is good;
   domain integrity is incomplete.
4. **Capability operations are duplicated.** Mission and capability services both attach/detach
   capabilities, creating two policy locations that can diverge.
5. **The empty `app/services` package competes with `app/application/services`.** It introduces a false
   navigation path and unclear ownership.
6. **No automated architecture fitness function exists.** Ruff, MyPy, and unit tests do not prohibit a
   future inward import from FastAPI or infrastructure.

## Dependency direction

Observed dependencies point inward for implemented business packages. No current code path connects
the frontend or API to the domain, application services, or vehicle port. That means there is no
present actuator bypass, but also no evidence that the intended application boundary works end to end.

Before any adapter, add an automated import rule with a deliberately failing fixture. Define the
composition root explicitly and prohibit service location, runtime imports, and driver handles outside
it. The API/AI/plugin path should be constrained to:

```text
untrusted request -> edge validation -> authenticated application command
  -> authorization -> deterministic safety decision -> audited port invocation
  -> normalized outcome -> correlated response/event
```

No layer may infer that descriptive mission, vehicle, or capability state grants authority.

## Ports and adapters

The five ports are technology-neutral, but `VehiclePort` currently exposes `arm`, `takeoff`,
`execute_mission`, `return_to_home`, and `emergency_stop` as `None`-returning synchronous methods. It
does not express command identity, requester, authorization, preconditions, deadlines, freshness,
idempotency, acknowledgement versus completion, cancellation, partial failure, loss of link,
retryability, audit correlation, or safe-state outcome. `TelemetryPort` similarly presents observations
without timestamp, source, frame, quality, or staleness. `EventPublisher` accepts `object`, preventing a
versioned event contract. `Clock` returns a potentially naive `datetime`. `MissionStore` has no
concurrency or failure semantics.

These are valid sketches, not safe implementation contracts. Freeze adapter work until concrete
simulation use cases and Phase 1 requirements define the semantics. Prefer command/result and
observation envelopes over widening methods ad hoc. Emergency behavior needs a separately analyzed,
independently available safety path; it must not be treated as an ordinary best-effort SDK call.

## Safety architecture

Safety is well articulated as an intended independent boundary but wholly absent as executable policy.
There is no hazard log, operational envelope, state-transition policy, deny-by-default authorization,
watchdog, override, freshness enforcement, command interlock, fault model, safe-state definition, or
tamper-evident audit schema. Consequently:

- no code may be described as safe for real-world flight;
- vehicle adapters and operational API endpoints remain blocked;
- domain state enums must not be treated as a safety state machine;
- `/health` means only that the web process answers, not operational readiness; and
- a qualified human safety owner must accept each future authority increase.

## AI and plugin architecture

There is no AI or plugin implementation, which is appropriate. The documented design correctly treats
both as untrusted outer actors and prohibits direct vehicle access. Before introducing either, require:

- typed, bounded, versioned request schemas with provenance and uncertainty;
- prompt-injection and tool-confusion threat analysis;
- deterministic validation, authorization, safety policy, and rate limits after model output;
- least-privilege, revocable capabilities and isolated execution;
- complete intent/decision/outcome correlation and retention rules;
- refusal, timeout, malformed, stale, replayed, and partial-failure tests; and
- an explicit statement that AI recommendations never constitute approval.

Model evaluation can support quality evidence but cannot replace deterministic safety tests or named
human approval.

## Required architectural decisions

In priority order, maintainers should record decisions for:

1. current roadmap phase and disposition of unmet earlier gates;
2. authoritative implemented source map and composition-root location;
3. requirements, threat, hazard, and traceability scheme;
4. application command/result, identity, authorization, and audit boundaries;
5. time, telemetry freshness, units, frames, and failure semantics;
6. deterministic simulator and port conformance strategy;
7. plugin/AI isolation only when validated requirements justify them; and
8. production deployment topology only after the application has production scope.

## Architecture verdict

| Dimension | Rating | Rationale |
| --- | --- | --- |
| Clean Architecture intent | Strong | Consistent charter, architecture, and ADRs |
| Current dependency direction | Strong/manual | Imports conform, but CI does not enforce boundaries |
| Domain purity | Strong | Standard-library-only and independently tested |
| Domain integrity | Partial | Public mutation can bypass construction invariants |
| Application boundary | Early | Descriptive services, no request/authority/transaction contract |
| Port quality | Early/high risk | Neutral types but operational semantics are absent |
| Adapter isolation | Not assessable | No adapters exist |
| Safety architecture | Designed only | Principles exist; requirements and controls do not |
| AI/plugin architecture | Designed only | Appropriate prohibition, no implementation or validation |
| Extensibility | Promising | Replaceable boundaries, but contracts must harden before growth |

**Decision:** preserve the current no-hardware/no-autonomy boundary. Architecture is adequate for
requirements work and pure-domain experimentation, not for operational implementation.
