# ADR-0005: Keep application ports in the top-level `app.ports` package

- **Status:** Accepted
- **Date:** 2026-07-27
- **Decision owners:** Shai (`shaike1`)
- **Scope:** Python package topology and automated dependency enforcement

## Context

[ADR-0004](ADR-0004-ports.md) placed five application-owned protocols under
`backend/app/ports`. The architecture audit identified that this sibling package can make ownership
less visually obvious than nesting ports under `app.application`. Moving the package now would,
however, change the documented import surface without adding safety, authority, or runtime behavior.

Automated enforcement needs an explicit topology decision before it can encode allowed dependency
directions.

## Decision

Keep `app.ports` as a top-level package owned by the application boundary.

Package ownership is architectural rather than determined solely by directory nesting:

- `app.domain` may import only the Python standard library and `app.domain`;
- `app.ports` may import only the Python standard library, `app.domain`, and `app.ports`;
- `app.application` may import the Python standard library, `app.domain`, `app.ports`, and
  `app.application`; and
- outer packages may depend inward, but the three protected packages may not import API, models,
  core/bootstrap, infrastructure, adapters, frameworks, vendor SDKs, or other third-party packages.

A dependency-free AST fitness test enforces these rules in the existing backend Pytest job. It checks
normal imports, relative imports, and literal `__import__` or `importlib.import_module` calls.
Computed dynamic imports remain subject to architecture review because static analysis cannot resolve
arbitrary runtime strings.

## Considered alternatives

### Move ports under `app.application.ports`

Nesting would make ownership visible in the path, but it would create import churn and compatibility
work before a concrete use case requires it. It is deferred rather than prohibited.

### Add a third-party import-boundary tool

A dedicated package could provide richer policy configuration, but adding it before the repository
has an approved dependency-lock and update policy would conflict with IMP-004. The standard-library
AST test is sufficient for the current small package graph.

### Continue with review-only enforcement

Manual review has preserved direction so far, but it does not provide repeatable negative evidence and
will become less reliable as the repository grows.

## Consequences

The existing `app.ports` import surface remains stable and no runtime code moves. CI fails when a
protected layer introduces a forbidden static dependency. Representative negative fixtures prove that
the test detects domain-to-framework, domain-to-application, application-to-outer-layer, and
port-to-adapter violations.

This decision does not authorize adapters, persistence, simulation, AI/plugins, vehicle SDKs, hardware
access, or autonomous behavior. Port protocols remain non-operational sketches governed by ADR-0004.

## Verification

From `backend/` run:

```bash
ruff check app tests
ruff format --check app tests
mypy app tests
pytest tests/architecture
pytest
```

## Revisit criteria

Revisit the package location when an approved application use case requires a compatibility-breaking
port redesign, or when the package graph justifies adopting a reviewed and reproducibly locked
architecture-analysis dependency.
