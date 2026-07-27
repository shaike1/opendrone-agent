# Active Backlog

No product implementation is authorized by this file.

### ENG-001 / IMP-001 — Reconcile canonical architecture and phase status
- State: Reconciliation drafted; pending Shai's maintainer approval and named architecture review
- Epic: E0
- Owner: Shai (maintainer decision); architecture reviewer to be named by Shai
- Rationale: canonical documents describe Phase 0/no source while domain, application, and port code exists.
- Acceptance criteria:
  - [ ] Maintainers record current phase and disposition every unmet prior gate.
  - [x] Canonical architecture and READMEs accurately describe existing modules and limitations.
  - [x] The reconciliation links rather than rewrites accepted ADR history.
  - [ ] Shai approves or corrects the phase/gate record and names an architecture reviewer.
  - [ ] The named architecture reviewer approves the reconciliation.
- Non-goals: new runtime behavior, adapters, vehicle access, or claims of safety.
- Risks/boundaries: misleading phase advancement; required maintainer and architecture review.
- Verification: link check, documentation review, `git diff --check`.

### ENG-002 — Establish Phase 1 evidence plan
- State: Blocked by Phase 0 gate acceptance and ENG-001 human approvals
- Epic: E1
- Owner: Unassigned
- Acceptance criteria:
  - [ ] Owners and formats exist for requirements, threat model, hazard log, data classification, and verification strategy.
  - [ ] Acceptance authority and traceability identifiers are explicit.
- Non-goals: completing analysis without qualified humans; implementing controls.
- Risks/boundaries: safety, security, privacy, legal assumptions; named specialist review required.
- Verification: cross-artifact traceability sample and review record.

### ENG-003 — Define reproducible dependency and security baseline
- State: Proposed
- Epic: E2
- Owner: Unassigned
- Acceptance criteria:
  - [ ] Maintainers choose lock/update policy for Python and npm.
  - [ ] Dependency, license, vulnerability, and secret scanning policy is documented.
  - [ ] CI evidence and exception ownership are defined.
- Non-goals: silently changing dependency versions or waiving findings.
- Risks/boundaries: supply chain and build reproducibility; security review required.
- Verification: clean checkout install/build procedure and scanner evidence.

### ENG-004 — Specify layered test and architecture gates
- State: Proposed
- Epic: E2
- Owner: Unassigned
- Acceptance criteria:
  - [ ] Test taxonomy maps to current and planned layers.
  - [ ] Dependency rules have automated enforcement criteria.
  - [ ] Frontend behavior and end-to-end priorities are risk-ranked.
- Non-goals: arbitrary coverage targets or hardware tests.
- Verification: CI design review against `engineering/architecture/dependency-rules.md`.
