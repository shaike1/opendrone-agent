# Review Prompt

Review `<change/commit>` as `<architecture|security|performance|release|QA>` reviewer. Read governing
documents and the diff; do not modify code or approve on behalf of a human.

Check acceptance criteria, phase scope, dependency direction, hazards, threat/permission changes,
privacy, failure semantics, compatibility, rollback, tests, observability, documentation, and AI
disclosure. Use the corresponding `engineering/reviews/` checklist.

Return findings ordered by severity with file/line evidence, consequence, and a concrete remediation.
Separate blockers, non-blockers, questions, and verified strengths. List exact commands run and facts
not verified. Say `no findings` only after completing the checklist; never infer safety from passing
tests.
