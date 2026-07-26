# ADR-0003: Introduce domain-only application orchestration

- **Status:** Accepted
- **Date:** 2026-07-26
- **Decision owners:** Founding maintainers
- **Scope:** Initial synchronous application services

## Context

The pure domain model describes missions, vehicles, capabilities, and measurements without defining workflows.
Callers nevertheless need one consistent place to coordinate entity creation, associations, and descriptive state updates.
Putting that orchestration in domain entities would mix use-case sequencing with durable business vocabulary, while placing it in FastAPI or another adapter would couple business workflows to delivery technology.

## Decision

Create an application package under `backend/app/application` with focused mission, vehicle, and capability services.
The services depend only on the domain layer, operate synchronously on domain entities in memory, and contain no persistence or execution behavior.
They reject invalid state types and duplicate capability identities through domain validation exceptions.

No ports or DTOs are introduced until a concrete boundary requires them.
An empty DTO package records the intended source location without inventing contracts.

## Considered alternatives

### Put workflows on domain entities

This would make the domain responsible for caller-specific sequencing and obscure the distinction between describing state and orchestrating a use case.

### Put workflows in API handlers

This would duplicate behavior across delivery mechanisms and violate the inward dependency rule by tying workflows to FastAPI or HTTP concepts.

### Add repositories and ports now

The current workflows are deliberately in memory.
Adding external boundaries before a concrete persistence or integration use case would create speculative abstractions outside this increment.

## Consequences

Application workflows are independently testable without mocks, infrastructure, hardware, or network access.
The domain remains free of orchestration concerns, and future adapters can call transport-neutral services.
The services currently mutate the supplied domain entities and provide no durability, concurrency handling, authorization, safety policy, or operational execution.

## Verification

Run Ruff, MyPy, and Pytest against the backend.
Review imports under `backend/app/application` to ensure that they reference only the Python standard library and `app.domain`.

## Revisit criteria

Revisit when a validated use case needs persistence, authorization, safety policy, application-owned DTOs, or an external integration boundary.
Introduce ports only with that concrete requirement and a separately reviewed architectural decision.
