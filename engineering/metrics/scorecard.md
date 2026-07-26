# Engineering Scorecard

**Baseline date:** 2026-07-26. Scores are static audit judgments from repository evidence: `0` absent,
`1` partial/manual, `2` implemented and automated. Safety-critical readiness cannot be averaged.

| Dimension | Score | Evidence/gap |
| --- | ---: | --- |
| Charter and principles | 2 | Charter, AI constraints, contribution rules exist |
| Architecture decisions | 2 | Four accepted ADRs; good constraints |
| Architecture conformance | 1 | Tests/types help; no automated dependency rule |
| Roadmap/gate traceability | 0 | Current phase conflicts with implementation; no acceptance record |
| Backend verification | 2 | Ruff, strict MyPy, pytest in CI |
| Frontend verification | 1 | lint/format/type/build; no behavioral tests |
| Integration/safety verification | 0 | No integration, fault, safety, or simulation suite |
| Security/privacy governance | 0 | Threat/data/disclosure/scanning artifacts absent |
| Dependency reproducibility | 0 | Ranged dependencies and no lockfiles |
| Release governance | 0 | Version exists; license/tag/provenance/rollback process absent |
| Documentation accuracy | 1 | Strong layer docs but canonical status drift |
| Observability | 1 | JSON backend logging; no audit/correlation/operational SLOs |

## Update method

Update only with a dated evidence link and reviewer. Explain changed scores; never improve a score
because work was merely planned. Report critical zeroes independently of any total. The immediate
success condition is closing governance and Phase 1 evidence gaps, not maximizing the sum.
