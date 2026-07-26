# Epics

| ID | Epic | Outcome | Dependencies | State |
| --- | --- | --- | --- | --- |
| E0 | Governance truth reconciliation | Canonical documents match code and phase acceptance is explicit | Human maintainers | Proposed |
| E1 | Safety/security requirements baseline | Traceable threats, hazards, data rules, and acceptance authority | E0 | Blocked by E0 |
| E2 | Verification and supply-chain baseline | Reproducible dependencies and layered quality/security evidence | E0; E1 informs scope | Proposed |
| E3 | Contract hardening for simulation | Safe, typed semantics support deterministic simulation | E1, E2, approved Phase 2 scope | Blocked |
| E4 | Deterministic simulator foundation | Conforming simulator and fault evidence, no hardware | E3 and separate implementation approval | Icebox |

## Epic acceptance pattern

Each epic must define: accountable owner; stakeholders and non-users; in/out of scope; linked
requirements and ADRs; safety/security/privacy effects; measurable acceptance criteria; verification
commands and artifacts; compatibility; rollback; residual risks; and required human approvals.

Epic state is planning metadata, not a roadmap phase decision. Product implementation remains outside
this Engineering OS bootstrap.
