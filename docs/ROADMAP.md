# Roadmap

The roadmap is outcome-based, not date-based. A phase advances only when its exit evidence is
reviewed and accepted. Work may move backward when new hazards or invalid assumptions emerge.

## Phase 0 — Governance and shared language (current)

**Outcomes:** project charter, architecture principles, contribution rules, AI workflow, initial ADR,
and safety-gated roadmap.

**Exit gate:** maintainers approve the documents; unresolved terms and decision owners are recorded;
there is no executable drone or agent code.

## Phase 1 — Requirements, threat model, and hazard analysis

Define actors, operational scenarios, non-goals, data classification, trust boundaries, misuse cases,
hazards, legal/regulatory assumptions, and measurable safety requirements. Select implementation
languages and repository tooling through ADRs only after requirements are understood.

**Exit gate:** traceable requirements, reviewed threat model, preliminary hazard log, acceptance
authority, verification strategy, and an approved implementation-foundation ADR.

## Phase 2 — Contract-first simulation foundation

Create pure domain types, application ports, plugin manifest contracts, audit schemas, and a
deterministic simulator adapter. Build continuous quality, security, dependency, and documentation
checks. No physical vehicle connection is permitted.

**Exit gate:** conformance suites, safety invariant tests, reproducible builds, dependency inventory,
and fault-injection evidence satisfy Phase 1 requirements.

## Phase 3 — Operator workflow in simulation

Implement authenticated operator intent, planning, approval, cancellation, emergency-stop semantics,
telemetry visibility, and replay against simulation. AI output remains advisory and is evaluated for
unsafe, ambiguous, and adversarial input.

**Exit gate:** end-to-end simulated scenarios, usability review, audit completeness, recovery drills,
and documented model limitations pass independent safety and security review.

## Phase 4 — Hardware-in-the-loop

Introduce one tightly scoped vehicle adapter behind established ports in a controlled test rig.
Validate timing, degraded connectivity, sensor faults, command rejection, physical interlocks, and
manual override without free flight.

**Exit gate:** approved test plan, trained operators, incident procedure, hardware evidence, rollback
plan, and explicit residual-risk acceptance.

## Phase 5 — Staged supervised flight

Progress from tethered or contained tests to bounded supervised scenarios. Every expansion has an
operational envelope, go/no-go checklist, observer, abort criteria, and post-flight review.

**Exit gate:** the accountable safety authority approves each envelope. Passing one envelope does not
authorize another.

## Phase 6 — Ecosystem and carefully bounded agency

Stabilize SDK/plugin contracts, provenance and distribution, multi-vendor adapters, and controlled AI
assistance. Any increase in authority is independently justified and remains revocable.

**Ongoing gates:** backward compatibility, supply-chain controls, field telemetry review, incident
learning, red-team exercises, and periodic re-authorization of safety assumptions.

## Explicit non-commitments

The roadmap does not promise unattended flight, general autonomy, support for a particular vendor,
or a release date. Such commitments require evidence, governance approval, and updated ADRs.
