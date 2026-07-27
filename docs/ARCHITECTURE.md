# Architecture

## Status

This document distinguishes the implemented development foundation from the intended architecture.
It does not authorize additional implementation or establish that roadmap gates have passed.
Significant changes must be recorded in an Architecture Decision Record (ADR).
[ADR-0001](adr/ADR-0001-clean-architecture.md) establishes the dependency model.

## Quality attributes, in priority order

1. **Safety:** loss of connectivity, invalid input, component failure, or AI uncertainty leads to a
   known safe state.
2. **Security and privacy:** least privilege, authenticated control, minimized data, and auditable
   access are default properties.
3. **Correctness and observability:** behavior is deterministic where possible, contracts are typed,
   and consequential actions are traceable.
4. **Portability:** domain policy is independent of drone vendors, transports, UI frameworks, and AI
   providers.
5. **Operability:** upgrades, rollback, diagnosis, and manual intervention are designed in.

Convenience, feature velocity, and autonomy never outrank these attributes.

## Clean Architecture

Dependencies point inward:

```text
Drivers / UI / AI hosts
          │
          ▼
Interface adapters ──► Application use cases ──► Domain policy
          ▲                       │
          └──── implementations ◄─┘ ports owned inward
```

- **Domain:** entities, value objects, invariants, safety policy, and domain events. It imports no
  framework, vendor SDK, transport, database, or AI library.
- **Application:** typed use cases and ports. It coordinates domain policy and authorization but has
  no infrastructure details.
- **Interface adapters:** translate external representations into application contracts. Validation
  at this edge does not replace domain invariants.
- **Drivers/infrastructure:** vehicle SDKs, persistence, message transports, web frameworks, AI/MCP
  hosts, and deployment-specific code.
- **Composition root:** the only location that selects concrete implementations and connects them.

Cross-layer shortcuts are prohibited. In particular, AI and plugin interfaces cannot call vehicle
drivers directly; all actions pass through authenticated application use cases and safety policy.

## Implemented source structure

The current repository implements this narrower topology:

```text
backend/app/
├── domain/             # Pure entities, enums, exceptions, and measurement value objects
├── application/        # Synchronous in-memory orchestration services; empty DTO namespace
├── ports/              # Five application-owned Protocol contracts; no implementations
├── api/ and models/    # FastAPI status routes and response schemas
├── core/               # Runtime configuration and JSON logging
├── main.py             # Assembly for the status-only FastAPI application
└── services/           # Empty legacy namespace
frontend/src/           # React status dashboard for /health and /version
```

The HTTP interface and dashboard are a development status application. The domain model describes
missions, vehicles, capabilities, and measurements, while application services only construct and
mutate those objects in memory. The ports name clock, events, mission storage, telemetry, and vehicle
operations, but are non-operational sketches: no adapter or composition wiring implements them.

There is no persistence, simulator, authentication/authorization, independent safety engine,
mission execution, vehicle SDK or connection, hardware access, AI integration, or plugin runtime.
Backend unit and API tests cover the implemented foundation; frontend validation is static
lint/format/type/build checking rather than behavioral testing. The development Docker images are
not a production deployment architecture.

## Governing accepted decisions

- [ADR-0001](adr/ADR-0001-clean-architecture.md): Clean Architecture and inward dependencies.
- [ADR-0002](adr/ADR-0002-python-domain-layout.md): pure Python domain layout.
- [ADR-0003](adr/ADR-0003-application-layer.md): synchronous, domain-only application services.
- [ADR-0004](adr/ADR-0004-ports.md): five Protocol-based application ports without adapters.

These accepted records govern the existing code and remain unchanged. Their acceptance does not
record approval of the Phase 0 or Phase 1 exit gates and does not authorize later-phase work.

## Safety architecture

The safety boundary is independent of planning and AI components. Future designs must provide:

- explicit operational envelopes and deny-by-default permissions;
- command validation, freshness, idempotency, rate and geospatial limits;
- a human-authorized arming transition and continuously available override;
- watchdogs, fail-safe states, and behavior defined for partial failure;
- separation between advisory output, planned action, approved action, and actuator command;
- tamper-evident audit events with identity, intent, policy decision, and outcome;
- simulation, fault injection, hardware-in-the-loop, and staged flight evidence;
- no claim of safety based solely on tests, AI evaluation, or an LLM assertion.

A hazard analysis identifies what may go wrong, the owner of each mitigation, its verification
method, residual risk, and the authority accepting that risk. A safety-affecting change requires a
named safety reviewer.

## Plugin architecture

Plugins extend capabilities across stable, typed ports; they do not weaken boundaries.

### Contract

Each future plugin must declare an immutable identifier, semantic version, compatible host contract,
requested capabilities, configuration schema, health semantics, and provenance. Contracts are
versioned independently from implementations and verified by a shared conformance suite.

### Lifecycle

Discovery is explicit—never arbitrary filesystem execution. The host validates signature/provenance,
compatibility, configuration, and granted capabilities before activation. Lifecycle states are
`discovered`, `validated`, `inactive`, `active`, `degraded`, and `stopped`. Activation and shutdown
must be bounded, observable, idempotent, and safe after interruption.

### Isolation and trust

- Plugins receive only explicitly granted capabilities and scoped data.
- Untrusted plugins run out of process or in an equivalent sandbox with bounded CPU, memory, time,
  network, filesystem, and device access.
- A plugin cannot obtain a vehicle handle. It may request an application operation, which remains
  subject to identity, authorization, safety policy, and audit.
- Failure is contained; the host can revoke, quarantine, and roll back a plugin without compromising
  the safety controller.
- Secrets are supplied at runtime and are never included in manifests, logs, or plugin artifacts.

## Data and observability

Schemas are explicit, versioned, and backward-compatible within a documented window. Units, clocks,
coordinate frames, precision, provenance, and retention are part of the contract. Structured events
carry correlation and causation identifiers. Sensitive fields are classified and redacted by design.
Telemetry loss or reordering must not silently imply a safe or successful action.

## Architecture governance

An ADR is required for languages/frameworks, public contracts, trust boundaries, persistence,
protocols, plugin isolation, safety invariants, or a reversal of an accepted decision. ADRs record
context, options, decision, consequences, and verification. Accepted ADRs are not rewritten except
for clerical corrections; superseding decisions link both records.
