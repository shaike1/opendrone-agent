# Port Contract Governance

**Status:** Active freeze policy  
**Effective date:** 2026-07-28  
**Change coordinator:** Shai (`shaike1`)  
**Authority boundary:** This policy does not approve operational implementation.

## Scope and classification

This policy governs `VehiclePort`, `TelemetryPort`, `MissionStore`, `Clock`, and
`EventPublisher` under `backend/app/ports`.

All five protocols are **non-operational contract sketches**. Their existence does not establish
validated requirements, authorization, safety policy, runtime wiring, adapter readiness, or fitness
for flight. In particular, the command-shaped methods on `VehiclePort` grant no authority and must
not be exposed through an API, AI host, plugin, simulator, SDK, or physical vehicle connection.

## Freeze

Until the release conditions below are satisfied:

- do not add a concrete adapter or infrastructure implementation;
- do not connect a port to persistence, telemetry, a simulator, a vehicle SDK, or hardware;
- do not add operational endpoints or a composition root that supplies an implementation;
- do not treat descriptive mission, vehicle, capability, or state data as authorization;
- do not widen, reinterpret, or stabilize a method because a vendor API happens to provide it; and
- do not claim that protocol conformance, static typing, or passing unit tests establishes safety.

Pure in-memory fakes used only for deterministic contract tests are not adapters when they perform no
I/O, expose no external handle, and cannot be selected by an operational runtime.

## Ownership and approvals

Shai (`shaike1`) coordinates proposed contract changes and repository compatibility. Coordination
does not confer specialist authority or permission to accept consequential residual risk.

A change that affects authority, commands, telemetry meaning, time, persistence, events, failure
semantics, privacy, or audit evidence requires named human reviewers for the affected disciplines:

- application/domain ownership for use-case and vocabulary correctness;
- architecture ownership for dependency direction and compatibility;
- safety ownership for hazards, safe-state behavior, and authority changes;
- security ownership for identity, authorization, misuse, and trust boundaries; and
- privacy/legal ownership when data classification, retention, location, identity, or regulation is
  affected.

An agent may prepare evidence and identify gaps. It may not supply a missing specialist approval.

## Change classes

### Clerical

Spelling, links, and wording that do not change signatures or semantics require maintainer review and
evidence that generated/public surfaces are unchanged.

### Compatible contract change

An additive type or method still requires an approved concrete use case, compatibility analysis,
failure semantics, tests, and application plus architecture review. Additive does not mean safe or
authorized.

### Consequential or breaking change

Any changed command, result, timing, freshness, identity, authorization, safety, audit, persistence,
event, cancellation, idempotency, or failure meaning requires:

- a new or superseding ADR;
- traceability to approved requirements, hazards, and threats;
- migration and rollback treatment;
- denial, malformed, stale, replay, timeout, cancellation, and partial-failure evidence as relevant;
- named application, architecture, safety, and security approval; and
- explicit disposition of compatibility and residual risk.

## Adapter release conditions

A concrete adapter remains prohibited until all of the following are recorded and approved:

1. IMP-002 requirements, threat, hazard, data, verification, and acceptance governance exists.
2. The relevant application command/outcome, telemetry/time, event/audit, and invariant contracts are
   accepted from concrete use cases rather than inferred from the current sketches.
3. Reusable adapter-conformance criteria cover capability declaration, failures, timeouts,
   cancellation, cleanup, observability, and safe-state outcomes.
4. A deterministic, no-hardware simulation scope and fault model are separately approved.
5. The change identifies exact owners, verification, rollback, stop conditions, and required human
   acceptance.

Meeting these conditions permits a separately reviewed proposal; it does not automatically authorize
an adapter, hardware connection, HIL activity, flight, or autonomy.

## Required change record

Every proposal must state:

- affected protocol and exact semantic difference;
- approved use case and requirement identifiers;
- callers, implementers, and compatibility impact;
- identity, authorization, safety, temporal, failure, and audit consequences;
- hazards, threats, data classes, mitigations, and residual-risk owner;
- deterministic tests and negative/fault evidence;
- migration, rollback, and stop conditions; and
- named reviewers and their recorded decisions.

## Verification

Current enforcement is limited to protocol import/export tests, strict typing, and the automated
dependency-direction gate. Review the protected packages with:

```bash
cd backend
ruff check app tests
ruff format --check app tests
mypy app tests
pytest tests/ports tests/architecture
pytest
```

These checks enforce code quality and dependency rules only. They are not a safety case.
