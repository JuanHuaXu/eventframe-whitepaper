# Bayesian Grouping and Changepoint Evidence Correction Audit

Date: 2026-08-28

- **Confirmed stale formulation:** the paper's changepoint specialization triggers only on posterior mass at run length zero, while the implemented v4 monitor also uses a bounded warm-started two-sided CUSUM and a post-reset cooldown.
- **Confirmed stale implementation claim:** the conclusion lists Bayesian model comparison as unimplemented deep work. The reference daemon now implements a bounded slow-path Beta-Bernoulli shared-versus-split comparison.
- **Authority invariant:** Bayesian comparison is diagnostic and proposal-only. It cannot assign a shared posterior key or certify its own grouping. Only a current external Anti-Pigeon certificate may authorize sharing.
- **Evidence classification:** the new residual, Anti-Pigeon, grouping, and changepoint results are synthetic mechanism evidence. They are not real-world validation and do not establish certificate coverage or universal calibration.
- **Rejected iterations:** two frozen changepoint confirmation attempts failed false-alarm targets and remain part of the evidence record. The paper must not report only the final iteration.
- **Hot-path cost:** capped run-length updating remains bounded by retained support and CUSUM updating is constant time. Group comparison is an explicit slow-path operation linear in the declared group size after sufficient statistics are retrieved.
- **Falsifiers:** false sharing without an external certificate violates authority; stable-stream alarm rates, recurring misses, or gradual delay beyond frozen targets falsify detector readiness; wrong split/share rates on untouched data falsify comparison reliability.
- **Scope:** update the Bayesian memory mathematics, claims, runtime description, evidence section, open problems, conclusion, notation, assembled Markdown, and PDF. Do not claim empirical Anti-Pigeon certificate validity from oracle group labels.

## Resolution

- Added the Beta-Bernoulli shared-versus-split marginal-evidence equations, minimum support, threshold, and group cap. The decision is explicitly proposal-only and cannot set the Anti-Pigeon sharing indicator, certificate, or key.
- Replaced the run-length-zero-only specialization with the implemented warm-up, slow reference, two-sided cumulative detector, cooldown, reset, and dependency-closure behavior while retaining the capped run-length branch.
- Recomputed every headline percentage from the untouched v4 JSON. Residual reduction is 29.812249%, oracle-granularity reduction is 29.412955%, and noisy abrupt, recurring, and gradual detection rates are 87.5%, 77.34375%, and 93.75%.
- Preserved the initial, rejected v2/v3, and final v4 machine-readable reports under `evidence/bayesian-upgrade/`. Corrected the human digest to distinguish the group-comparison and changepoint confirmation seed bases; raw reports were not edited.
- Synchronized canonical source, claims, notation, glossary, outline, project brief, conclusion, symbol index, assembled Markdown, and both PDF copies.
- Verification found no remaining P1 or P2 inconsistency in the added formulation. The result remains synthetic mechanism evidence; certificate coverage, independent replication, complete marked-time/no-event evaluation, and real-world transport remain open.
