# Engineering Health Metrics

Metrics are decision aids, not targets to game and never substitutes for safety evidence.

| Signal | Definition | Source/cadence | Initial state |
| --- | --- | --- | --- |
| CI pass rate | successful required workflow runs / completed runs | GitHub Actions, monthly | Not collected |
| Change lead time | first commit to merge, median and p90 | Git/PR, monthly | Not collected |
| Review latency | ready-for-review to first substantive human review | PR, monthly | Not collected |
| Rework rate | merged PRs needing corrective follow-up within 30 days | PR/issues, monthly | Not collected |
| Flaky checks | checks passing on rerun without relevant change | CI incidents, monthly | Not collected |
| Gate traceability | active items with requirement, evidence, owner, reviewer | backlog audit, sprint | Baseline incomplete |
| Documentation drift | confirmed code/doc contradictions open | audit, sprint | At least 2 |

Record sample window, numerator/denominator, exclusions, and raw evidence link. Prefer trends over
individual performance. Do not rank people or pressure reviewers to trade safety for speed.
