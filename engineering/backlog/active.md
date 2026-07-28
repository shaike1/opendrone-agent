# Active Backlog

No product implementation is authorized by this file.

### ENG-001 / IMP-001 — Reconcile canonical architecture and phase status
- State: Completed by PR #12
- Epic: E0
- Owner: Shai (`shaike1`) in maintainer and architecture-review roles
- Approval note: dual-role approval was recorded; it was not an independent architecture review.
- Acceptance criteria:
  - [x] Maintainer recorded the current authorized phase and disposition of unmet gates.
  - [x] Canonical architecture and READMEs describe existing modules and limitations.
  - [x] The reconciliation links rather than rewrites accepted ADR history.
  - [x] Maintainer and architecture-review approval are recorded.
- Non-goals: no phase-exit acceptance, runtime expansion, adapters, vehicle access, or safety claim.
- Verification: PR #12 review record and passing CI run #29.

### ENG-005 / IMP-003 — Freeze and classify consequential port contracts
- State: Completed by PR #15
- Epic: E0
- Owner: Shai (`shaike1`) as change coordinator; specialist acceptance remains unassigned
- Acceptance criteria:
  - [x] All five protocols are classified as non-operational sketches.
  - [x] Concrete adapters and operational wiring are explicitly prohibited.
  - [x] Ownership, review disciplines, compatibility evidence, and change classes are documented.
  - [x] Release conditions require IMP-002 and accepted contract/conformance/simulation evidence.
- Non-goals: no contract redesign, adapter, simulator implementation, SDK, hardware, or autonomy.
- Verification: policy/link review and PR #15 CI.
- Residual condition: no adapter proposal may proceed until named specialist owners approve the
  prerequisite requirements and contract evidence.

### ENG-002 — Establish Phase 1 evidence plan
- State: Blocked by Phase 0 gate acceptance and named specialist owners
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
- State: In progress; IMP-005 implemented, broader verification strategy remains open
- Epic: E2
- Owner: Shai (`shaike1`) for architecture enforcement; verification owner unassigned
- Acceptance criteria:
  - [ ] Test taxonomy maps to current and planned layers.
  - [x] Dependency rules are enforced by AST tests with representative negative fixtures.
  - [ ] Frontend behavior and end-to-end priorities are risk-ranked.
- Non-goals: arbitrary coverage targets or hardware tests.
- Verification: CI design review against `engineering/architecture/dependency-rules.md`.
