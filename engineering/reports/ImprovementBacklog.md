# Improvement Backlog

**Audit date:** 2026-07-26
**Purpose:** Prioritized engineering-quality work only. This backlog does not authorize product
features, operational behavior, adapters, AI, plugins, or hardware access.

## Ordering principles

1. Correct authority and source-of-truth defects before expanding code.
2. Establish hazards, threats, data rules, and acceptance authority before designing controls.
3. Make builds and architecture checks trustworthy before multiplying adapters.
4. Harden contracts through deterministic simulation, never through direct hardware experimentation.
5. Add production machinery only when an approved release has an actual consumer and owner.

## Priority 0 — stop-the-line governance

### IMP-001 — Reconcile canonical project reality

**Outcome:** A maintainer-approved statement identifies the current roadmap phase, implemented scope,
unmet earlier gates, and explicitly blocked work.
**Why first:** Every other priority relies on valid authority.
**Scope:** `PROJECT.md`, `docs/ARCHITECTURE.md`, `docs/ROADMAP.md`, READMEs, and linked Engineering OS
views; documentation only.
**Acceptance:**

- canonical documents accurately describe the status runtime, domain, application services, ports,
  tests, and absence of adapters/safety/AI/plugins/hardware;
- each unmet Phase 0/1 gate has an owner and disposition without retroactive implied approval;
- accepted ADRs are linked, not rewritten; and
- named maintainer and architecture reviewers approve the reconciliation.

**Verification:** link check, contradiction review, `git diff --check`.
**Dependencies:** None.
**Non-goals:** advancing a phase or implementing runtime behavior.

### IMP-002 — Establish safety/security requirements governance

**Outcome:** Reviewed formats and owners exist for actors/scenarios, requirements, preliminary hazards,
threats/misuse cases, data classification, legal assumptions, verification, and residual-risk acceptance.
**Acceptance:** Stable identifiers trace one sample scenario through hazard/threat, requirement, control,
test evidence, and human decision; stop conditions and review cadence are explicit.
**Dependencies:** IMP-001.
**Required reviewers:** Named domain, safety, security, privacy, and maintainer owners.
**Non-goals:** claiming completeness without qualified analysis or implementing controls.

### IMP-003 — Freeze and classify consequential port contracts

**Outcome:** Current vehicle/telemetry/event/store/clock protocols are explicitly classified as
non-operational sketches, with change control and adapter prohibition.
**Acceptance:** No concrete adapter can be merged until IMP-002 and contract acceptance; ownership and
compatibility rules are documented.
**Dependencies:** IMP-001.
**Non-goals:** redesigning commands before requirements.

## Priority 1 — trustworthy foundation

### IMP-004 — Make dependency resolution reproducible

**Outcome:** Maintainers select committed Python/npm lock strategy, controlled update cadence, license
and vulnerability policy, and exception ownership.
**Acceptance:** Two clean environments resolve identical inputs; CI uses frozen installs; dependency
inventory and scanner outputs are reviewable.
**Dependencies:** IMP-001 and named security/release ownership.
**Non-goals:** unreviewed bulk upgrades or auto-merging security updates.

### IMP-005 — Automate dependency direction

**Outcome:** CI enforces the package rules in `engineering/architecture/dependency-rules.md`.
**Acceptance:** Valid imports pass; checked negative fixtures fail for domain-to-framework,
domain-to-application, application-to-API/infrastructure, and port-to-adapter imports; exceptions require
architecture review.
**Dependencies:** IMP-001 and topology decision for `app.ports`.
**Non-goals:** a brittle filename-only check that can be bypassed through dynamic imports.

### IMP-006 — Repair contributor workflow drift

**Outcome:** One documented clean-checkout workflow matches CI, hooks, Make, Docker, extras, and supported
Python/Node versions.
**Acceptance:** Backend README uses an existing extra; Node versions agree; commands accurately label
typechecks versus behavioral tests; development images are clearly marked; onboarding is exercised in
a clean environment.
**Dependencies:** IMP-004 decision for final frozen commands.

### IMP-007 — Establish legal and disclosure baseline

**Outcome:** Approved license, contribution/IP expectations, SECURITY policy, private reporting channel,
triage owner, response expectations, and safe disclosure guidance.
**Acceptance:** Policies are discoverable from the root README and the channel is tested without placing
sensitive details in public artifacts.
**Dependencies:** Human maintainer/legal/security decisions.

### IMP-008 — Define layered verification strategy

**Outcome:** A risk-based test taxonomy maps domain, application, contract, adapter, integration,
safety, API, UI, and end-to-end evidence to CI stages.
**Acceptance:** Ownership, determinism, fixtures, coverage interpretation, flake handling, reports, and
traceability rules are explicit; no arbitrary percentage substitutes for hazard coverage.
**Dependencies:** IMP-002 and IMP-005.

## Priority 2 — harden the contract-first simulation boundary

These items remain **blocked** until Priority 0 has human approval.

### IMP-009 — Define application command and outcome contracts

Include requester/subject identity, authorization context, correlation, idempotency, preconditions,
deadlines, acknowledgement/completion, structured failures, retryability, cancellation, and audit
effects. Derive every field from an approved use case or requirement.
**Acceptance:** ADR, compatibility strategy, success/denial/malformed/replay/timeout/partial-failure tests,
and named application/safety/security approval.

### IMP-010 — Define trustworthy telemetry and time

Specify aware monotonic/wall-clock use, observation time, receipt time, source, coordinate frame,
units, uncertainty/quality, freshness, ordering, gaps, and loss behavior.
**Acceptance:** Stale, future, reordered, duplicate, invalid, missing, and clock-discontinuity cases have
deterministic outcomes and traceability to hazards.

### IMP-011 — Protect domain invariants across mutation

Decide whether aggregates own transitions, services replace immutable snapshots, or validated mutation
is retained. Consolidate duplicated capability association policy and define concurrency/version
semantics before persistence.
**Acceptance:** No supported mutation can bypass identity, type, collection, and transition invariants;
property and regression tests demonstrate this.

### IMP-012 — Specify event and audit evidence contracts

Separate business events from security/audit records; version schemas; define identity, intent, policy
decision, outcome, correlation/causation, ordering, tamper considerations, redaction, retention, access,
and failure behavior.
**Acceptance:** Schema compatibility, privacy review, redaction, failure, and integrity evidence.

### IMP-013 — Build adapter conformance criteria

Define a reusable suite for every future port implementation, including capability declaration,
timeouts, cancellation, partial failure, resource cleanup, observability, and safe-state behavior.
**Acceptance:** A deliberately nonconforming fake fails each mandatory behavior.
**Non-goals:** selecting a vehicle vendor.

### IMP-014 — Approve a deterministic simulator design

Only after IMP-002 and IMP-009–013, decide simulation time, seeded determinism, fault model, scenario
format, oracle, reproducibility, and evidence retention through an ADR.
**Acceptance:** Simulator scope explicitly excludes physical connectivity; fault scenarios trace to
requirements and hazards.
**Note:** Implementation belongs in a separate feature-authorized change, not this audit backlog.

## Priority 3 — quality depth for the existing status application

### IMP-015 — Add risk-based frontend boundary tests

Test loading, success, total/partial failure, retry, malformed response, race/unmount behavior, and
accessible error/status presentation. Add runtime response validation or schema-derived contracts when
the API expands.

### IMP-016 — Strengthen backend edge tests

Test invalid configuration, logging structure/redaction, negative HTTP behavior, schema stability, and
meaningful liveness/readiness. Report coverage as diagnostic evidence rather than a safety claim.

### IMP-017 — Reduce namespace and documentation ambiguity

Decide the disposition of empty `app/services` and `application/dto`; document the authoritative package
map; assign documentation owners/cadence; reduce duplicated state claims; automate Markdown links and
basic formatting.

## Priority 4 — production and release readiness

These items are deliberately deferred until there is an approved release scope and named operators.

### IMP-018 — Define production deployment architecture

Cover process/server topology, non-root read-only images, secret/config delivery, network policy,
resource limits, TLS/ingress, liveness/readiness, scaling, state, backups, retention, and rollback.

### IMP-019 — Establish observability and incident operations

Define SLOs and error budgets, metrics/logs/traces/audit correlation, alert ownership, runbooks,
escalation, privacy, safe shutdown, incident review, and exercised recovery.

### IMP-020 — Establish release and provenance pipeline

Define version ownership, changelog, compatibility/support windows, immutable artifacts, checksums,
signing, SBOM, build provenance, vulnerability disposition, promotion, rollback, and post-release
verification. No agent may publish or accept residual risk.

### IMP-021 — Threat-model AI and plugins before implementation

Only when separately authorized, define untrusted-input boundaries, capability grants, isolation,
resource/network/device access, provenance/signing, revocation, prompt/tool injection defenses, model
evaluation limits, human approval, and deterministic enforcement. AI/plugins must never receive a
vehicle handle.

## Suggested delivery sequence

| Increment | Items | Exit decision |
| --- | --- | --- |
| A — truthful baseline | IMP-001–003 | Maintainers confirm authorized scope and stop conditions |
| B — trustworthy engineering system | IMP-004–008 | Builds/checks/policies have owners and reproducible evidence |
| C — safe simulation contracts | IMP-009–014 | Qualified reviewers approve contract and simulator evidence |
| D — current-app quality | IMP-015–017 | Existing behavior has proportionate automated evidence |
| E — release readiness | IMP-018–021 | Humans approve an actual release scope; no flight claim implied |

## Backlog governance

Before promotion, every item needs a named owner, approved phase, issue, measurable acceptance, risks,
dependencies, exact verification, rollback, and required human reviewers. Close an item only with a
merged revision and evidence. Reprioritize after new hazards, threats, incidents, or scope decisions;
never reorder solely for feature velocity.
