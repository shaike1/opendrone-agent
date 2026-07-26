# Backlog Protocol

Backlog items are evidence-bearing decisions, not free-form feature wishes. Use `active.md` for ready
or explicitly blocked near-term work, `icebox.md` for uncommitted ideas, and `completed.md` only after
acceptance evidence and human approval exist.

## Item schema

```markdown
### ENG-000 — Imperative outcome
- State: Ready | In progress | Blocked
- Epic: E0
- Owner: Unassigned
- Rationale:
- Acceptance criteria:
  - [ ] Observable result
- Non-goals:
- Risks/boundaries:
- Dependencies/ADRs:
- Verification:
- Required reviewers:
```

IDs are stable. Moving an item preserves its text and adds completion date, PR/commit, verification,
and approver evidence. Only one agent owns execution. A human owns consequential decisions and risk.

## Ready definition

Outcome and non-goals are unambiguous; scope is phase-authorized; dependencies are met; acceptance is
measurable; risks and reviewers are named; verification and rollback are plausible; no unresolved
instruction conflict exists.
