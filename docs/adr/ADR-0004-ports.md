# ADR-0004: Define application ports with Python protocols

- **Status:** Accepted
- **Date:** 2026-07-26
- **Decision owners:** Founding maintainers
- **Scope:** Initial application-owned external capability contracts

## Context

[ADR-0001](ADR-0001-clean-architecture.md) requires application-owned interfaces between use cases
and external systems.
[ADR-0003](ADR-0003-application-layer.md) deferred those interfaces until a separately reviewed
increment established a concrete boundary.
The contract-first Phase 2 work now needs named boundaries for vehicle operations, telemetry, mission
persistence, time, and event publication before any adapters are selected.

## Decision

Define `VehiclePort`, `TelemetryPort`, `MissionStore`, `Clock`, and `EventPublisher` under
`backend/app/ports` as Python `typing.Protocol` classes.
Their signatures use only standard-library and domain types.
They contain no implementation, runtime wiring, infrastructure imports, or authorization policy.

Protocols were selected because structural typing lets future adapters satisfy an application-owned
contract without inheriting from an application base class.
This keeps conformance explicit to static type checking while avoiding implementation coupling and
the runtime ceremony of abstract base classes.

Infrastructure is hidden because vendor SDKs, transports, databases, and clocks are replaceable outer
details.
Adapters implement the protocols and translate domain-facing operations at the boundary.
Application code must not call SDKs directly: doing so would reverse the inward dependency direction,
couple workflows to a vendor, and bypass the single boundary where future safety and authorization
requirements must be applied.

## Considered alternatives

### Abstract base classes

Nominal inheritance could enforce method implementation at instantiation time, but would require
adapters to inherit from application classes and add runtime machinery that these contracts do not
need.

### Direct SDK and infrastructure calls

This would initially require fewer interfaces, but would make application tests depend on external
technology and prevent integrations from being replaced without changing application code.

### Delay every port until its adapter exists

Deferral would avoid unused contracts, but would allow adapter APIs to dictate application needs.
Defining the required boundary first preserves contract-first design without approving any adapter.

## Consequences

Application code can type against stable, infrastructure-neutral operations, and future adapters can
be checked structurally.
The contracts add no runtime behavior and cannot demonstrate that an adapter is operationally safe.
Method evolution is a public compatibility concern and requires tests and documentation updates.

This decision revisits only ADR-0003's deferral of ports.
Its limits on persistence implementations, execution behavior, and infrastructure remain in force.

## Verification

Run Ruff, MyPy, and Pytest against the backend.
Tests verify that every protocol is importable and that the package export list remains stable.
Review imports under `backend/app/ports` to ensure they reference only the standard library and
`app.domain`.

## Revisit criteria

Revisit when real application use cases establish failure, freshness, asynchronous, or streaming
semantics that the initial contracts cannot express.
Any change must preserve inward dependencies and provide a compatibility plan.
