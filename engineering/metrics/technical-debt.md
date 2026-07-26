# Technical Debt Register

| ID | Debt | Impact | Priority | Owner | Exit evidence |
| --- | --- | --- | --- | --- | --- |
| TD-001 | Architecture/roadmap status drift | Agents may plan from false phase assumptions | Critical | Unassigned | ENG-001 approved |
| TD-002 | Missing Phase 1 safety/security evidence | Controls and contracts lack traceable hazards/threats | Critical | Unassigned | E1 human approval |
| TD-003 | Unspecified vehicle-port failure/authority semantics | Future adapters could encode unsafe assumptions | High | Unassigned | Requirements + ADR + contract tests |
| TD-004 | No dependency locks/inventory/scanning | Builds are less reproducible; supply-chain risk opaque | High | Unassigned | ENG-003 evidence |
| TD-005 | No automated layer boundary check | Architectural erosion may evade unit tests | Medium | Unassigned | CI negative boundary test |
| TD-006 | Frontend has typecheck but no behavior tests | Loading/error/retry/accessibility regressions may escape | Medium | Unassigned | Risk-based UI suite |
| TD-007 | Empty duplicate `app/services` namespace | Navigation and ownership ambiguity | Low | Unassigned | Documented disposition |
| TD-008 | Release/license/security-channel gaps | Distribution and reporting are not governed | High | Unassigned | Approved policies and rehearsal |

At sprint close, review priority and evidence. Debt is closed only by demonstrated removal or an
explicit human-owned acceptance with revisit date; deleting an entry is not remediation.
