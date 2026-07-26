# Architecture Principles

These operationalize `PROJECT.md`, `docs/ARCHITECTURE.md`, and ADR-0001. Higher-order sources win.

1. Safety before capability; uncertainty and partial failure converge visibly to a known safe state.
2. Humans retain explicit, continuously available authority for consequential operations.
3. Dependencies point inward; policy does not know frameworks, vendors, transports, storage, or AI.
4. Contracts precede adapters and state units, clocks, identity, errors, freshness, and compatibility.
5. Least authority is deny-by-default, scoped, revocable, observable, and independently enforced.
6. AI and plugins are untrusted external actors; they request application operations, never actuators.
7. Simulation precedes hardware, and evidence gates each increase in real-world authority.
8. Invalid/unsafe states are prevented where practical and validated again at every trust boundary.
9. Consequential intent, decision, state transition, and outcome are correlated and auditable.
10. Prefer small reversible decisions; ADRs document hard-to-reverse choices and supersession.
11. No silent degradation: stale, reordered, denied, timed-out, and partial results remain explicit.
12. Documentation is architecture: implemented, proposed, and absent capabilities must be distinct.
