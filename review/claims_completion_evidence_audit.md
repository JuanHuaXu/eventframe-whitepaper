# Claims-Completion Evidence Audit

Date: 2026-08-29

## Patch reasoning

- **Observed mismatch:** the paper still reported v4 group and changepoint
  numbers and labeled most later targets untested, while the daemon repository
  contained a frozen completion protocol and newer generated artifacts.
- **Primary evidence:** machine-readable design and confirmation JSON, paired
  evaluator reports, aggregate chronological reports, and a machine-readable Go
  integration test. The daemon's prose digest was checked against those files.
- **Alternatives rejected:** treating positive average residual gain as a pass
  would ignore the frozen false-reuse ceiling; treating two chronological
  trajectories as confirmation would violate the frozen minimum; treating
  accepted certificate fields as measured coverage would confuse validation
  with estimation.
- **Chosen invariant:** every reported proposition carries the outcome required
  by its frozen criterion, and implementation scaffolding is not described as
  predictive effect when the scored output is invariant.
- **Falsifier:** a mismatch between the paper's counts or intervals and the
  preserved JSON, or a current integration run in which a published snap changes
  the scored recall law under otherwise identical input.
- **Scope:** update empirical status, evidence, open-problem boundaries, and
  conclusion only. The mathematical definitions are unchanged.
- **Hot-path cost:** not relevant; this is a publication update.

## Evidence classifications

- Heterogeneous residual safety: confirmed failure of the frozen safety
  criterion despite positive mean gain.
- Complete compatible/divergent group decision criterion: confirmed failure;
  divergent split behavior remains supported.
- Synthetic changepoint scenario contract: confirmed pass for all six frozen
  scenarios; no production guarantee inferred.
- Structured-frame and priority effects: inconclusive due to two trajectories
  and missing interpretability or clean structure ablations.
- Omitted-influence coverage: inconclusive because the estimator is absent.
- Predictive-snap output improvement: confirmed failure in the current runtime;
  publication and rollback scaffolding remain functional.
