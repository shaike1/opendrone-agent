# Project Charter

## Mission

OpenDrone Agent will provide an open foundation for safe, portable, and observable agent-assisted
drone operations. It separates human intent and domain policy from AI planners, vehicle vendors, and
deployment technology.

## Problem

Drone integrations are frequently vendor-coupled, difficult to inspect, and unsafe to expose directly
to probabilistic systems. Teams need stable contracts and evidence-driven safety gates so that
planning, simulation, operator workflows, and hardware can evolve without granting accidental
authority or rewriting core policy.

## Stakeholders

- Operators accountable for an operation and its abort decisions
- Safety and security reviewers accountable for risk evidence
- Maintainers accountable for architecture, releases, and community health
- Plugin and adapter authors accountable for contract conformance
- Researchers and users who need reproducible simulations and transparent limitations
- People, property, airspace participants, and communities affected by operation

Affected non-users are stakeholders even when they cannot participate directly in design.

## Scope

### Intended, subject to phase gates

- Vendor-neutral domain and application contracts
- Simulation-first mission and telemetry workflows
- Independently enforceable safety policy and human override
- Capability-based, isolated plugins and adapters
- Auditable AI-assisted planning through constrained application operations
- Observable, reproducible developer and operator environments

### Not currently in scope

- Executable software, vehicle connectivity, or flight control
- Unattended or unrestricted autonomy
- Circumvention of aviation rules, geofencing, authorization, or operator responsibility
- Weapons, harmful payloads, surveillance-by-default, or covert operation
- A claim of regulatory approval or fitness for real-world flight

## Engineering principles

1. **Safety before capability.** Prefer refusal and a known safe state to uncertain execution.
2. **Humans retain authority.** Approval, cancellation, and override are explicit system concepts.
3. **Evidence over confidence.** Decisions cite requirements, tests, analysis, and known limitations.
4. **Dependencies point inward.** Domain policy is insulated from frameworks and vendors.
5. **Least authority.** Components, users, plugins, and AI receive the minimum revocable capability.
6. **Contracts before implementations.** Types, units, failure semantics, and compatibility come first.
7. **Observable by default.** Intent, decisions, state transitions, and outcomes are correlated.
8. **Secure and private by design.** Minimize collection and exposure; never rely on secrecy alone.
9. **Small reversible changes.** Favor reviewable increments, migration paths, and rollback.
10. **No silent degradation.** Uncertainty, stale data, and partial failure are visible and actionable.

## Decision ownership

Maintainers steward project scope and architecture. Domain experts review specialized claims. A named
safety reviewer must approve safety-affecting changes; a named security reviewer approves trust or
privilege changes. Review does not transfer accountability away from the change author. When roles
are unfilled, affected work remains blocked rather than self-approved.

## Measures of success

- Requirements trace to implementation, verification, and operational evidence.
- Domain and safety tests run without vendor SDKs or network services.
- Every external integration conforms to versioned ports and declared capabilities.
- Consequential operations identify requester, authorization, policy result, and outcome.
- Faults converge to documented safe states and recovery procedures are exercised.
- Contributors can reproduce supported builds and checks from documented commands.

Feature count, AI benchmark score, and flight time alone are not success measures.

## Governance artifacts

- `PROJECT.md` defines why the project exists and its durable principles.
- `docs/ARCHITECTURE.md` defines dependency and trust boundaries.
- ADRs capture consequential technical decisions.
- `docs/ROADMAP.md` defines outcome and safety gates.
- `docs/CONTRIBUTING.md` defines how a change is proposed and accepted.
- `AI_CONTEXT.md` constrains AI-assisted work.

Conflicts are resolved in that order unless a later accepted ADR explicitly and transparently
supersedes a specific architectural decision. Safety and applicable law always take precedence.
