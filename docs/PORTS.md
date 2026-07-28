# Application Ports

## Purpose

Ports are application-owned contracts for capabilities that must ultimately be supplied outside the
application boundary.
They let application code describe what it needs in domain terms without selecting a vehicle SDK,
database, clock source, or event transport.

The initial ports cover vehicle operations, telemetry retrieval, mission persistence, time, and
domain-event publication.
They are contracts only and do not authorize an operation, implement mission execution, or provide a
connection to a physical vehicle.

## Dependency inversion

Dependencies point inward: the application may depend on these ports and the ports may depend only
on the Python standard library and `app.domain`.
Infrastructure does not become an application dependency merely because the application needs an
external capability.
Instead, a future outer-layer implementation will conform structurally to the relevant protocol.

## Ports and adapters

A **port** says what the application requires through a typed, implementation-neutral interface.
An **adapter** translates between that interface and a particular external technology.
For example, `MissionStore` defines mission persistence operations but makes no choice of database,
while a future persistence adapter would make that choice and implement the contract.

No adapters are part of this increment.
Future adapters belong outside the ports package and must depend inward on the contracts rather than
causing the contracts to import infrastructure.

## Why ports contain no logic

Ports contain method signatures, parameter types, and result types only.
Business policy remains in the domain and application services, while integration behavior remains
in adapters.
Keeping logic out of ports prevents an interface from becoming a hidden implementation and allows
contract consumers and implementers to evolve independently.

The protocols intentionally provide no connection handling, storage, telemetry collection, event
bus, dependency injection, or concrete clock.

## Contract status and change control

All five protocols are frozen as **non-operational contract sketches**. Command-shaped methods do not
grant authority, and no concrete adapter, simulator implementation, SDK integration, persistence
implementation, hardware connection, or operational wiring may be merged from these sketches.

The authoritative ownership, review requirements, compatibility evidence, adapter prohibition, and
release conditions are defined in the
[port contract governance policy](../engineering/architecture/port-contract-governance.md).
[ADR-0004](adr/ADR-0004-ports.md) governs the protocol decision and
[ADR-0005](adr/ADR-0005-ports-topology.md) governs package ownership and dependency enforcement.

Changing a signature or semantic meaning requires a concrete approved use case and the review level
specified by that policy. Passing typing, protocol, or architecture tests does not establish safety or
authorize implementation.
