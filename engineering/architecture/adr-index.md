# ADR Index

| ADR | Status | Decision | Current observation |
| --- | --- | --- | --- |
| [0001](../../docs/adr/ADR-0001-clean-architecture.md) | Accepted | Clean Architecture and inward dependencies | Protected backend layers have automated AST checks |
| [0002](../../docs/adr/ADR-0002-python-domain-layout.md) | Accepted | Pure Python domain under `backend/app/domain` | Implemented with entities, enums, value objects, exceptions, tests |
| [0003](../../docs/adr/ADR-0003-application-layer.md) | Accepted | Synchronous domain-only application services | Implemented; in-memory and non-operational |
| [0004](../../docs/adr/ADR-0004-ports.md) | Accepted | Five Protocol-based application ports | Contracts implemented; no adapters |
| [0005](../../docs/adr/ADR-0005-ports-topology.md) | Accepted | Keep application-owned ports at `app.ports` and automate dependency checks | Topology preserved; AST gate implemented |

## Governance

Create an ADR for languages/frameworks, source layout changes, public contracts, persistence,
protocols, trust boundaries, plugin isolation, safety invariants, or reversal of an accepted decision.
Use the next unused four-digit number. Include status, date, owners, scope, context, drivers, options,
decision, consequences, compliance/verification, migration/rollback when applicable, and revisit
criteria. Accepted ADRs are immutable except clerical corrections; superseding ADRs link both ways.

## Reconciliation status

PR #12 reconciled the canonical architecture and recorded Shai (`shaike1`) in both maintainer and
architecture-review roles. That dual-role approval closed IMP-001 but was not an independent review,
did not accept the Phase 0 exit gate, and did not authorize operational implementation.
