# ADR-0001: Adopt Clean Architecture and inward dependencies

- **Status:** Accepted
- **Date:** 2026-07-26
- **Decision owners:** Founding maintainers
- **Scope:** Future executable software and plugin contracts

## Context

OpenDrone Agent is expected to integrate changing vehicle vendors, transports, operator interfaces,
storage, plugins, and AI providers. Its durable safety and mission policy must remain understandable
and testable without those technologies. Direct coupling would make policy difficult to verify,
encourage AI-to-actuator shortcuts, and allow infrastructure changes to alter safety behavior.

## Decision drivers

- Independently verifiable domain and safety policy
- Vendor and framework portability
- Explicit authority, trust, and failure boundaries
- Simulation and testability without hardware
- Replaceable plugins and adapters with contained failures
- Long-term maintainability despite evolving infrastructure

## Considered options

### 1. Clean Architecture with ports and adapters — chosen

Domain policy sits at the center; application use cases own ports; adapters translate external
systems; drivers and frameworks remain outer details; a composition root wires implementations.

### 2. Framework-centric layered application

This offers fast scaffolding but tends to leak framework models, lifecycle, persistence, and transport
into policy. Replacing vendors and testing failure behavior becomes harder.

### 3. Event-driven services from the outset

Independent services could provide isolation, but premature distribution adds partial failure,
ordering, schema evolution, deployment, and observability risks before boundaries are validated.
Events may later connect proven boundaries without changing the inward dependency rule.

## Decision

Adopt Clean Architecture. Source-level dependencies point from infrastructure and interface adapters
toward application and domain layers. The domain has no framework, vendor, network, persistence, or
AI dependency. Application use cases own the interfaces needed from external systems. Concrete
implementations and configuration meet only in a composition root.

AI hosts and plugins are external actors. They submit requests through the same authenticated,
authorized, validated, safety-governed application boundary as other clients. They never receive
direct actuator or vehicle-driver access.

## Consequences

### Positive

- Core behavior can be tested deterministically without devices or infrastructure.
- Vendor, UI, AI, protocol, and persistence choices remain replaceable.
- Authority and safety decisions have a single reviewable path.
- Plugin conformance and simulation can exercise the same application contracts.

### Negative and trade-offs

- More explicit contracts, translation, and composition are required.
- Poorly chosen abstractions can add ceremony; abstractions need concrete use cases and tests.
- Boundary discipline requires review and automated dependency checks once code exists.
- Some vendor capabilities may need careful modeling rather than direct SDK exposure.

## Compliance and verification

Before executable code is accepted, a follow-up ADR will define source layout and automated boundary
checks. Reviews must reject inward layers importing outer layers, domain types mirroring framework or
vendor models, service locators outside the composition root, and direct plugin/AI access to drivers.
Unit tests must run with no network, hardware, framework boot, or vendor SDK.

## Revisit criteria

Revisit when evidence shows a boundary prevents a required safety property or cannot represent a
validated use case. Convenience alone is insufficient. A superseding ADR must preserve explicit
authority, testability, and safety controls and provide a migration plan.
