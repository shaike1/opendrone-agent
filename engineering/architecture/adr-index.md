# ADR Index

| ADR | Status | Decision | Current observation |
| --- | --- | --- | --- |
| [0001](../../docs/adr/ADR-0001-clean-architecture.md) | Accepted | Clean Architecture and inward dependencies | Governs all executable layers; automated boundary checks pending |
| [0002](../../docs/adr/ADR-0002-python-domain-layout.md) | Accepted | Pure Python domain under `backend/app/domain` | Implemented with entities, enums, value objects, exceptions, tests |
| [0003](../../docs/adr/ADR-0003-application-layer.md) | Accepted | Synchronous domain-only application services | Implemented; in-memory and non-operational |
| [0004](../../docs/adr/ADR-0004-ports.md) | Accepted | Five Protocol-based application ports | Contracts implemented; no adapters |

## Governance

Create an ADR for languages/frameworks, source layout changes, public contracts, persistence,
protocols, trust boundaries, plugin isolation, safety invariants, or reversal of an accepted decision.
Use the next unused four-digit number. Include status, date, owners, scope, context, drivers, options,
decision, consequences, compliance/verification, migration/rollback when applicable, and revisit
criteria. Accepted ADRs are immutable except clerical corrections; superseding ADRs link both ways.

## Known reconciliation

`docs/ARCHITECTURE.md` predates the implemented layout and still says no source directories exist.
Correcting that descriptive drift does not itself supersede ADRs, but requires maintainer review.
