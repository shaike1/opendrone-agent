# Release Governance

## Current release state

The repository reports version `0.1.0`, but no tag, changelog, artifact publication, license, release
automation, support window, or provenance policy is evidenced in the repository. Treat it as the
application's configured development version, not proof of a production release.

## Release classes

- **Documentation-only:** no application behavior; still requires review and link/content checks.
- **Development snapshot:** internal evidence only; never implies operational fitness.
- **Versioned release:** semantic-version tag from `main` after every applicable release gate passes.

## Versioned release gate

- Scope and compatibility are documented; phase permits every included capability.
- CI commit is green and source revision is immutable.
- Architecture, security, performance, and release templates have evidence and approvals.
- Dependency inventory, licenses, vulnerabilities, build provenance, and artifacts are reviewed.
- Migration, rollback, known limitations, support owner, and incident channel are documented.
- Safety-affecting claims are approved by named human authorities; no certification is implied.

Use [`../reviews/release.md`](../reviews/release.md) for the reusable checklist. Releases are proposed;
an agent may prepare evidence but may not tag, approve, publish, or accept risk without authorization.
