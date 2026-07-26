# Engineering Health

**Audit date:** 2026-07-26
**Evidence basis:** All tracked source, tests, configuration, documentation, ADRs, and engineering
artifacts; local checks listed below.
**Overall state:** Healthy early-stage code discipline with critical governance, safety, security,
reproducibility, and production-readiness gaps.

## Scorecard

Scores describe repository evidence, not intent: **0 absent**, **1 documented/manual**, **2 partial
implementation**, **3 implemented and automated**. A total is intentionally omitted because critical
safety gaps cannot be averaged away.

| Capability | Score | Evidence-based assessment |
| --- | ---: | --- |
| Project charter and scope control | 3 | Clear stakeholders, exclusions, authority, and success measures |
| Architecture decisions | 2 | Four accepted ADRs; ownership is generic and status has drifted |
| Clean Architecture conformance | 2 | Current imports comply; no automated dependency fitness test |
| Domain design | 2 | Pure types and boundary tests; mutation can bypass invariants |
| Application design | 1 | Independently tested descriptive services; no use-case boundary semantics |
| Ports/adapters | 1 | Five neutral contracts; no adapters or conformance behavior |
| Safety engineering | 1 | Excellent principles/checklists; no hazard-derived executable controls |
| AI engineering | 1 | Clear untrusted-actor rules; no architecture/evaluation implementation |
| Backend test quality | 2 | Unit/API coverage of present behavior; no coverage report or integration suite |
| Frontend test quality | 1 | Types/lint/build only; `npm test` is a typecheck alias |
| CI quality | 2 | Parallel validation and image builds; missing security/docs/architecture gates |
| Dependency/supply chain | 0 | Ranges, `npm install`, no committed locks/SBOM/scanning/provenance |
| Documentation quality | 2 | Broad and thoughtful; canonical contradictions and repeated status data |
| Developer experience | 2 | Compose, Make, examples, formatting; workflows diverge and installs are not reproducible |
| Observability/operations | 1 | JSON process logging; no SLOs, readiness, tracing, audit, runbooks, or alerts |
| Release governance | 0 | No license, security policy, changelog, provenance, release automation, or rollback |
| Production readiness | 0 | Development servers/images and no operational capability or safety case |

## Strengths to preserve

1. **Scope discipline:** the repository repeatedly distinguishes descriptive contracts from authority
   and prohibits hardware or autonomous operation at the current stage.
2. **Pure, typed core:** domain value objects use explicit units, finite/bounds checks, immutable
   measurement values, dedicated exceptions, and strict typing.
3. **Fast baseline feedback:** CI runs backend lint, types, tests; frontend lint, format, types, build;
   and both Docker builds.
4. **Small runtime attack surface:** only health and version endpoints exist; there is no vehicle, AI,
   plugin, database, credential, or operational endpoint.
5. **Evidence-oriented culture:** contribution, AI, review, backlog, and release templates consistently
   demand exact verification and named human authority.

## Testing assessment

### Backend

The domain suite covers happy paths and invalid inputs for entities, enums, and measurements. The
application suite covers creation, mutation, duplicate rejection, and invalid state types. Port tests
primarily establish importability, method shape, and structural conformance. API tests cover the two
successful endpoints and configuration changes.

Missing evidence includes mutation-invariant tests, state-transition rules, property-based boundary
tests, time-zone behavior, logging redaction/shape, configuration failures, negative HTTP behavior,
concurrency, adapter contracts, integration paths, fault injection, safety invariants, and coverage
measurement. These omissions are reasonable for the tiny status runtime but block any authority-bearing
increment.

### Frontend

There is no behavioral test runner. Loading, success, partial success, fetch failure, retry,
unmount/race behavior, error accessibility, and API response validation are untested. TypeScript trusts
`response.json()` through a cast, so malformed responses cross the boundary unchecked. Add tests only
as risk warrants; do not mistake a typecheck script for a test suite.

### Test architecture required before simulation

- pure domain property/invariant tests;
- application use-case authorization and denial tests;
- port contract suites shared by every adapter;
- deterministic simulator integration and fault-injection tests;
- architecture dependency tests with negative fixtures;
- API schema/auth/error tests;
- frontend behavior/accessibility tests; and
- traceability from every safety requirement and hazard control to evidence.

## CI/CD and supply chain

The workflow is clear and least-privileged at the repository level. Job timeouts and separate backend,
frontend, and image jobs are positive. However:

- Python and npm dependencies are range-resolved during CI and Docker builds;
- CI uses `npm install` rather than a committed-lockfile `npm ci` workflow;
- action versions are tag-pinned, not immutable commit-pinned;
- no dependency review, vulnerability, secret, license, SAST, container, or IaC scan exists;
- no documentation/link or architecture-boundary check runs;
- no coverage, test-report, artifact checksum, SBOM, signature, or provenance is produced; and
- there is no deployment or release pipeline—which is appropriate until release governance exists.

Do not add deployment merely to improve maturity optics. First select license, disclosure, dependency,
artifact, and release policies, then produce reproducible evidence.

## Developer experience

The root README, service READMEs, Compose file, Makefile, `.env.example`, EditorConfig, Prettier,
pre-commit, and CI provide a usable starting path. Friction and ambiguity remain:

- root instructions use `uv sync`, hooks use `uv run`, CI uses editable `pip install`, Docker uses
  `pip install`, and the backend README uses a venv plus the nonexistent `test` extra;
- Node requirements differ between the frontend README (20+) and CI/Docker (22);
- `make test` says it runs frontend tests, but `npm test` only runs TypeScript;
- Docker images run Uvicorn reload and Vite development servers and should be labeled development-only;
- the two service package paths and multiple overlapping engineering status files increase navigation
  cost; and
- no one-command clean bootstrap verifies tool versions and exact dependency resolution.

## Documentation health

Documentation coverage is broad, but accuracy is uneven. Critical contradictions include:

- `docs/ARCHITECTURE.md` states that no source directories exist;
- `docs/ROADMAP.md` labels Phase 0 current while Phase 2 domain/port work exists;
- `PROJECT.md` lists executable software as not currently in scope despite the status application;
- the root/backend READMEs understate the implemented domain/application/port packages; and
- the backend install command requests `[test]`, while `pyproject.toml` defines `[dev]`.

Treat these as active defects. Designate canonical owners and generate or link secondary views rather
than copying status claims into many files.

## Maintainability and extensibility

The codebase is small, legible, typed, and conventionally organized. Replaceable contracts create a
good extensibility foundation. Risks rise quickly if the present sketches become stable APIs without
requirements: duplicated capability orchestration, mutable entities, unconstrained event objects, and
command-shaped vehicle methods will create compatibility and safety debt. Extension points should be
earned through a concrete use case, a threat/hazard review, contract tests, and an ADR—not through
empty packages or speculative methods.

## Production-readiness decision

**Not production-ready and not operationally deployable.** The application is a development status
surface. The following minimum gates remain open:

- reconciled roadmap phase and named accountable owners;
- license, security policy/private disclosure channel, threat model, data classification, and hazard log;
- authenticated/authorized application boundary and independent safety controls;
- deterministic simulation with fault and conformance evidence;
- reproducible, scanned, inventoried, and provenance-bearing builds;
- production server/static hosting, hardened containers, health/readiness semantics, observability,
  SLOs, backups where applicable, incident response, rollback, and release policy; and
- named human acceptance of residual safety, security, privacy, and operational risks.

## Audit verification record

The auditor inspected all files returned by `git ls-files`, reviewed all four ADRs and all documentation,
examined imports and package topology, and ran the repository's existing quality commands. Command
results belong in the pull request and commit evidence; passing software checks do not alter the
production-readiness verdict.
