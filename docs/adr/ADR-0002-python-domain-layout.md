# ADR-0002: Establish the Python domain source layout

- **Status:** Accepted
- **Date:** 2026-07-26
- **Decision owners:** Founding maintainers
- **Scope:** Initial core domain model

## Context

[ADR-0001](ADR-0001-clean-architecture.md) requires a follow-up decision before executable code is
accepted.
The repository already has a Python 3.11 backend and its quality tooling.
The first Phase 2 increment needs a precise home for pure domain contracts without expanding into
application behavior or infrastructure.

## Decision

Place the initial domain model under `backend/app/domain` and its unit tests under
`backend/tests/domain`.
Use the Python standard library only within the domain package, with dataclasses for entities and
immutable value objects and enums for closed state vocabularies.

Domain modules may depend on other domain modules and the Python standard library.
They must not depend on application, adapter, infrastructure, framework, vendor, transport,
persistence, deployment, or external-service modules.
Automated linting, strict type checking, and isolated unit tests enforce the initial boundary;
dedicated import-boundary analysis may be added when additional architectural layers are introduced.

## Consequences

The domain vocabulary can be imported and tested without starting a framework, network service,
simulator, or hardware integration.
Explicit units and domain exceptions make invalid values visible.
The chosen package path follows the existing backend layout rather than the conceptual `src/domain`
example in the architecture document.

This decision does not approve application services, vehicle control, persistence, APIs, plugins,
AI behavior, or physical vehicle connections.

## Verification

Run Ruff, MyPy, and Pytest against the backend.
Review domain imports whenever a dependency or new architectural layer is proposed.

## Revisit criteria

Revisit the layout if independently versioning the domain becomes necessary or if automated boundary
checks show that the package structure cannot reliably preserve inward dependencies.
