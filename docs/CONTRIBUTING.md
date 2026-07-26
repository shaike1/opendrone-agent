# Contributing

OpenDrone Agent welcomes reviewable, evidence-driven contributions. During Phase 0, contributions are
limited to governance, requirements, architecture exploration, and documentation unless maintainers
explicitly approve a roadmap transition.

## Before opening a change

1. Search issues, pull requests, and ADRs for prior decisions.
2. Open an issue for behavior, public contracts, dependencies, trust boundaries, or safety impact.
3. Agree on acceptance criteria and identify required domain, safety, or security reviewers.
4. Use an ADR proposal for consequential or difficult-to-reverse architecture decisions.

## Branch strategy

The project uses trunk-based development:

- `main` is protected, always reviewable, and never receives direct pushes.
- Create a short-lived branch from current `main`, named `docs/<topic>`, `feat/<topic>`,
  `fix/<topic>`, `test/<topic>`, or `chore/<topic>`.
- Keep one coherent outcome per branch; rebase or update it before merge.
- Merge reviewed pull requests using squash merge unless preserving a deliberate commit series is
  approved. Delete the branch afterward.
- Releases use annotated semantic-version tags from `main`; no long-lived release or environment
  branches. Urgent fixes follow the same review path and are never committed directly to a tag.

## Coding and documentation standards

Language-specific tooling will be chosen by ADR before executable code is accepted. Durable standards
already apply:

- use explicit types and stable contracts; avoid implicit units, time bases, coordinate frames, and
  error semantics;
- keep domain policy independent of frameworks, I/O, global state, and vendor SDKs;
- make unsafe and invalid states unrepresentable where practical, then validate again at boundaries;
- use structured errors and logs without secrets or unnecessary personal/location data;
- document public contracts, invariants, failure behavior, compatibility, and migration;
- write deterministic tests at the lowest appropriate layer, including denial and failure paths;
- pin and review dependencies, minimize their privilege, and record provenance/licenses;
- use concise Markdown headings, relative repository links, one sentence per line when practical, and
  inclusive, precise language;
- never commit generated artifacts, credentials, local environment state, or unlicensed content.

## Commit rules

Make small logical commits that build toward one outcome. Use an imperative Conventional Commit-style
subject such as `docs: define plugin trust model`. Explain *why* in the body when the reason is not
obvious. Do not mix formatting, refactoring, and behavior. Signed commits may become required once
the maintainer and release-key policy is established.

## Pull Request rules

Every PR must:

- link its issue or explain why no issue is needed;
- describe problem, scope, non-goals, approach, alternatives, and user/operational impact;
- identify safety, security, privacy, compatibility, and plugin-boundary effects;
- list exact verification commands and distinguish passed, failed, and not-run checks;
- include or update tests, documentation, ADRs, migration, and rollback as applicable;
- disclose AI assistance according to `AI_CONTEXT.md`;
- contain no unrelated changes and resolve all review conversations;
- receive at least one maintainer approval, plus safety/security/domain owners when relevant;
- pass required checks and remain unmodified after final approval (other than an approved rebase).

Authors cannot approve their own PR. Draft PRs are encouraged for early design review. Reviews focus
on correctness and risk; approval is not granted merely because automation passes.

### Suggested PR description

```markdown
## Problem and scope
## Approach and alternatives
## Safety / security / privacy impact
## Verification evidence
## Rollback and compatibility
## AI assistance
## Checklist
```

## Definition of Done

A change is done only when all applicable items are true:

- [ ] Acceptance criteria and non-goals are satisfied without scope creep.
- [ ] Architecture dependency rules and accepted ADRs are preserved or explicitly superseded.
- [ ] Hazards, threats, privacy, permissions, failure states, and rollback were assessed.
- [ ] Public behavior is typed, documented, versioned, and compatible or has a migration plan.
- [ ] Tests cover success, denial, boundary, malformed input, and relevant failure paths.
- [ ] Required formatting, linting, typing, tests, security, and documentation checks pass reproducibly.
- [ ] No secrets, sensitive data, unsupported claims, or unexplained dependencies are introduced.
- [ ] Operational observability and support/runbook changes are included when relevant.
- [ ] AI use and any unverified work are disclosed accurately.
- [ ] Required human reviewers approve and every review conversation is resolved.
- [ ] The branch is current, commits/PR are understandable, and rollback is possible.

If a check cannot run, the PR stays draft unless an authorized maintainer documents the limitation,
alternative evidence, risk, and follow-up. Safety gates cannot be waived for schedule convenience.

## Reporting concerns

Use an issue for ordinary documentation concerns. Do not publish exploitable vulnerabilities,
credentials, sensitive locations, or dangerous operational details. Until a private security channel
is established, contact a maintainer privately and share the minimum information necessary.
