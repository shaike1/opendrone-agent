# Risk Register

**Audit date:** 2026-07-26
**Scope:** Engineering and product risks evidenced by the current repository.
**Important:** This register is preliminary and is not a hazard analysis, threat model, legal review,
flight-safety case, or acceptance of residual risk. Only named qualified humans may accept consequential
risk.

## Scale

- Likelihood: **1 rare** to **5 likely**.
- Impact: **1 minor** to **5 catastrophic/mission-ending**.
- Exposure is likelihood × impact before the proposed treatment.
- **Stop** means the listed work must not proceed until the condition is resolved.

## Active risks

| ID | Risk event | L | I | Exposure | Existing controls | Required treatment / stop condition | Owner |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| R-001 | Contributors interpret stale phase/status documentation as approval for executable scope | 4 | 5 | 20 | Charter, roadmap, AI constraints, engineering audit | Record authoritative phase and unmet-gate disposition. **Stop:** adapters, AI/plugins, operational endpoints, hardware | Unassigned maintainers |
| R-002 | Consequential `VehiclePort` methods are implemented without an authorization and safety boundary | 3 | 5 | 15 | Contract-only status; explicit warnings; no adapter | Derive contracts from threat/hazard requirements; require named safety/security review. **Stop:** any concrete vehicle adapter | Unassigned safety owner |
| R-003 | Stale, reordered, ambiguous, or low-quality telemetry is treated as current truth | 3 | 5 | 15 | Explicit value units and bounds | Add timestamps, clocks, source/frame/quality, freshness and failure semantics with adversarial tests | Unassigned domain/safety owners |
| R-004 | Mutable domain objects enter invalid states after construction | 3 | 4 | 12 | Constructors and some service checks; strict typing | Choose controlled mutation/aggregate policy and test invariant preservation | Unassigned domain owner |
| R-005 | Dependency drift or compromise changes build behavior unnoticed | 4 | 4 | 16 | Version ranges, CI builds, minimal runtime dependencies | Lock, inventory, scan, pin CI actions, define update/exception ownership | Unassigned security/release owners |
| R-006 | Public vulnerability reports expose sensitive details because no private channel exists | 3 | 4 | 12 | Contributor warning to contact a maintainer privately | Publish owned SECURITY policy and tested private channel before public distribution | Unassigned security owner |
| R-007 | Development containers are deployed as production services | 3 | 4 | 12 | READMEs call stack developmental | Explicitly label artifacts; do not publish; later build hardened non-root immutable images | Unassigned release owner |
| R-008 | `/health` is interpreted as full readiness or operational safety | 4 | 3 | 12 | Endpoint doc says API process health | Separate liveness/readiness and state dependencies/limitations before orchestration | Unassigned operations owner |
| R-009 | Architecture erodes through accidental outward imports | 3 | 3 | 9 | ADRs, review rules, MyPy/Ruff | Automate import constraints with a negative CI fixture | Unassigned architect |
| R-010 | Frontend silently mishandles malformed/partial backend responses or races | 3 | 2 | 6 | Error UI and strict TypeScript | Runtime-validate responses; test partial failure, retry, race/unmount, accessibility | Unassigned frontend owner |
| R-011 | AI output later bypasses deterministic controls through prompt/tool confusion | 3 | 5 | 15 | AI_CONTEXT prohibition; no AI implementation | Threat model, capability sandbox, typed requests, policy enforcement, adversarial evaluation. **Stop:** AI tools with vehicle authority | Unassigned AI/security owners |
| R-012 | A plugin later escapes intended least authority or acquires a vehicle handle | 3 | 5 | 15 | Documented isolation model; no runtime | Isolation ADR, signed provenance, resource/network/device bounds, revocation and conformance. **Stop:** plugin loading | Unassigned security owner |
| R-013 | Audit events leak precise location, identity, secrets, or model inputs | 3 | 4 | 12 | Documentation requires minimization/redaction | Data classification, field-level policy, retention/access/deletion rules, redaction tests | Unassigned privacy/security owners |
| R-014 | Passing unit/CI checks are mistaken for a flight-safety case | 4 | 5 | 20 | Repeated explicit disclaimers and phase gates | Trace hazards to independent evidence; named residual-risk authority. **Stop:** any real-world fitness claim | Unassigned safety owner |
| R-015 | No explicit emergency/override architecture remains available during component or link failure | 2 | 5 | 10 | Architectural intent only | Analyze independent override, watchdogs, safe states, failure containment and drills before operational work | Unassigned safety owner |
| R-016 | Synchronous contracts conceal latency, timeout, cancellation, acknowledgement, and partial completion | 4 | 4 | 16 | Ports have no implementation | Specify temporal/result semantics through simulator fault cases before adapters | Unassigned architect/domain owner |
| R-017 | Concurrent persistence produces lost updates or duplicate execution | 3 | 4 | 12 | No persistence exists | Define identity, versioning, idempotency, transaction/outbox behavior before a store adapter | Unassigned application owner |
| R-018 | License absence makes use, contribution, or distribution legally ambiguous | 4 | 3 | 12 | README acknowledges gap | Maintainers/legal counsel choose license and contribution policy before release | Unassigned maintainers |
| R-019 | Documentation duplication causes recurring architecture and workflow contradictions | 5 | 3 | 15 | Source-of-truth hierarchy and manual audits | Assign owners/cadence, reconcile current contradictions, automate links and reduce copies | Unassigned documentation owner |
| R-020 | Project cannot diagnose, contain, or roll back a production incident | 3 | 5 | 15 | Release checklist only; no deployment | Define SLOs, observability, incident authority, recovery and rehearsed rollback before release | Unassigned operations/release owners |

## Risk themes and controls

### Governance risk

The immediate dominant risk is ambiguity of authority. Repository quality mechanisms cannot compensate
for an unapproved roadmap transition. Resolve R-001 and R-019 first; all later planning depends on a
truthful baseline.

### Safety risk

R-002, R-003, R-014, R-015, R-016, and R-017 form a connected control problem. They require a formal
preliminary hazard analysis with operational scenarios, severity/likelihood rationale, controls,
verification, residual risk, and qualified acceptance. This document must not be used as that analysis.

### Security and privacy risk

R-005, R-006, R-011, R-012, and R-013 require actors, assets, trust boundaries, abuse cases, data flows,
least privilege, revocation, monitoring, incident response, and supply-chain provenance. AI and plugins
must stay outside the trusted computing base wherever possible.

### Delivery and operations risk

R-007, R-008, R-018, and R-020 mean the repository should not publish production artifacts. A local
development image successfully building is not evidence of secure deployment or support readiness.

## Review protocol

Review this register at each roadmap gate and after any architecture, dependency, trust-boundary,
incident, or operational-scope change. Each update must include evidence, named owner, treatment state,
residual score/rationale, next review trigger, and named human acceptance when applicable. Agents may
identify and propose treatment; they may not accept residual risk.
