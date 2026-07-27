# Operating Roadmap

This view translates `docs/ROADMAP.md` into near-term engineering outcomes based on repository
reality. It does not supersede phase gates or authorize implementation.

## Now — reconcile the baseline

Phase 0 is the only currently authorized phase. The documentation reconciliation is drafted, but
completion requires Shai's explicit maintainer approval/correction and approval from an architecture
reviewer named by Shai. No placement of code or acceptance of an ADR closes an earlier roadmap gate.

- Approve or correct the current phase and capture named gate acceptance.
- Update canonical architecture and developer documentation to describe implemented layers.
- Confirm safety, security, domain, and release decision owners.
- Establish requirements identifiers and traceability format.

**Exit evidence:** approved state statement; documentation-drift PR; owner list; Phase 0 checklist
with explicit accepted, open, and blocked items.

## Next — Phase 1 evidence

- Define actors, operational scenarios, explicit non-goals, and regulatory assumptions.
- Produce data classification, trust boundaries, threat/misuse model, preliminary hazard log, and
  measurable safety/security requirements.
- Approve verification strategy and residual-risk acceptance authority.

**Exit evidence:** all durable Phase 1 artifacts reviewed by named human domain, safety, and security
owners with traceability among hazards, controls, and verification.

## Then — strengthen the contract-first simulation foundation

- Specify application operation semantics before adapter work.
- Add automated dependency/conformance checks and reproducible dependency management.
- Define audit schemas and plugin manifest contracts only from validated requirements.
- Implement a deterministic simulator only in a separately approved product change.

**Exit evidence:** the Phase 2 gate in `docs/ROADMAP.md`; no physical vehicle connection.

## Later

Phases 3–6 remain governed solely by `docs/ROADMAP.md`. Do not schedule operator execution,
hardware-in-the-loop, flight, plugin distribution, or increased AI authority until every preceding
gate has independently accepted evidence.
