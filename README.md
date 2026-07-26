# OpenDrone Agent

OpenDrone Agent is an open, safety-first platform for building auditable agent-assisted drone
operations. The project is in its **governance and architecture phase**: this repository currently
contains documentation only and intentionally provides no flight, vehicle, or agent runtime.

## Vision

Enable people to compose portable drone capabilities without coupling mission policy to a vehicle
vendor, while keeping humans in control and making every consequential decision observable,
explainable, and reversible.

Safety is a system property, not a feature. An AI recommendation must never become an unrestricted
actuator command. Future software will enforce explicit authority boundaries, conservative
defaults, independent safety controls, and a reliable human override.

## Start here

- [Project charter](PROJECT.md) — scope, principles, stakeholders, and success criteria
- [Architecture](docs/ARCHITECTURE.md) — boundaries, dependency rules, and plugin model
- [Roadmap](docs/ROADMAP.md) — gated delivery phases
- [Contributing](docs/CONTRIBUTING.md) — branch, review, and Definition of Done
- [AI context](AI_CONTEXT.md) — mandatory guidance for AI-assisted changes
- [ADR-0001](docs/adr/ADR-0001-clean-architecture.md) — Clean Architecture decision

## Current scope

The current milestone establishes shared language and engineering governance. It does **not** select
a vehicle protocol, implement an API or UI, connect to hardware, or enable autonomous operation.
Those decisions require explicit architecture records and phase-gate approval.

## Repository structure

```text
.
├── README.md                 # Entry point and project status
├── PROJECT.md                # Project charter and engineering principles
├── AI_CONTEXT.md             # Rules for AI-assisted development
└── docs/
    ├── ARCHITECTURE.md       # Target architecture and plugin contracts
    ├── ROADMAP.md            # Safety-gated long-term plan
    ├── CONTRIBUTING.md       # Contribution and review workflow
    └── adr/                  # Immutable architecture decision records
```

Future source layout is described as a proposal in the architecture document; empty implementation
directories are deliberately not created yet.

## License and security

Licensing, disclosure channels, and a security policy will be selected before accepting executable
code. Until then, do not report sensitive operational or vulnerability details in public issues.
