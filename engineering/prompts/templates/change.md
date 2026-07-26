# Change Prompt

You are acting as the `<role>` for backlog item `<ID>`. Read the project charter, AI context,
architecture, applicable ADRs, Engineering OS state, and every file in scope before editing.

## Outcome
`<measurable result>`

## Constraints
- In scope: `<files/behaviors>`
- Non-goals: `<explicit exclusions>`
- Phase/gate authority: `<evidence>`
- Trust/safety/privacy boundaries: `<boundaries>`
- Required human reviewers: `<roles/names>`

## Acceptance and verification
- `<criterion with evidence>`
- Exact checks: `<commands>`
- Failure/adversarial cases: `<cases>`
- Compatibility and rollback: `<plan>`

Inspect first. State assumptions and stop on conflicting authority. Make the smallest reversible
change. Do not invent APIs, results, approvals, or modules. Do not weaken controls. Return changed
files, exact check outcomes, residual risks, and work requiring human verification.
