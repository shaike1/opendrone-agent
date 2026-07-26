# Engineering OS

This directory is the coordination layer for future OpenDrone Agent development. It records what is
true now, what may be worked next, how work is reviewed, and which evidence is required. It does not
grant operational authority or replace the project charter, accepted ADRs, or human approval.

## Source of truth order

1. `PROJECT.md` — mission, scope, and durable principles.
2. `docs/ARCHITECTURE.md` and accepted files in `docs/adr/` — architectural decisions.
3. `docs/ROADMAP.md` — phase gates.
4. `docs/CONTRIBUTING.md` and `AI_CONTEXT.md` — contribution and AI constraints.
5. This workspace — current planning, evidence links, and reusable workflows.

If this workspace conflicts with a higher source, stop, record the conflict, and ask a maintainer to
resolve it. Backlog priority never overrides a safety gate.

## Operating loop

1. **Orient:** read [project state](PROJECT_STATE.md), the governing ADRs, and the current sprint.
2. **Select:** pull a ready item from [active backlog](backlog/active.md); do not infer authority from
   an icebox idea.
3. **Frame:** use a [prompt template](prompts/README.md) to state outcome, non-goals, risks,
   acceptance criteria, verification, and rollback.
4. **Deliver:** keep one reviewable outcome per change and preserve inward dependencies.
5. **Verify:** run the relevant automated checks and the applicable architecture, security,
   performance, and release reviews.
6. **Close:** attach evidence, obtain required human approvals, move the item to completed, update
   metrics, and archive the sprint. Agents never approve their own work.

## Workspace map

- `roadmap/`: repository-grounded outcomes, epics, and release gates.
- `backlog/`: ready, completed, and deliberately deferred work.
- `sprints/`: a time-box-neutral current commitment and archive instructions.
- `prompts/`: safe, reusable task, review, and audit prompts.
- `reviews/`: evidence-oriented review checklists.
- `architecture/`: principles, enforceable dependency rules, and ADR inventory.
- `metrics/`: definitions and manually maintained baseline scorecard.
- `agents/`: bounded roles; all consequential decisions remain human-owned.
- [`AUDIT.md`](AUDIT.md): bootstrap engineering audit and next priorities.

## Update rules

- Every status claim links to repository evidence, a PR, an issue, or a command result.
- Use ISO dates (`YYYY-MM-DD`) and identify an accountable owner; use `Unassigned` rather than
  inventing one.
- Never store secrets, personal data, precise sensitive locations, or operational telemetry here.
- Mark estimates and proposals explicitly. Do not describe planned adapters, simulators, safety
  policy, or AI behavior as implemented.
- A sprint item is complete only when its acceptance evidence and required human review exist.
