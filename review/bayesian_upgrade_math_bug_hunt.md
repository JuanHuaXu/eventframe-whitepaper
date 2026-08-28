# Bayesian Upgrade Math Bug Hunt

Date: 2026-08-28

Scope: the selective Bayesian frontier, activation rule, Anti-Pigeon posterior sharing, selection-aware inference, changepoint monitoring, inactive-event audits, runtime bounds, staged integration, and their interaction with the pre-existing residual, abstraction, and evaluation contracts.

## Severity Result

- P1 open: none.
- P2 open: none after the corrections below.
- P3 or empirical limitations: retained explicitly as open problems and experimental requirements.

## Confirmed And Corrected

1. **P2: normative frontier semantics diverged from the body.** The first notation draft used graph parents and children unconditionally. It now uses SCM adjacency only when the SCM and identification contract exist, and otherwise uses predictive-dependency neighbors.
2. **P2: outgoing graph edges could be misread as future evidence.** The contract now states that as-of outgoing relationships nominate candidates only; an unrealized child outcome supplies no evidence.
3. **P2: selective updates could claim full-stream Bayesian calibration.** Informative activation now requires a normalized selection-conditioned likelihood with positive denominator. Without that model or a conditional-ignorability result, the object is named an activation-conditioned working posterior.
4. **P2: joint activation dependence was omitted.** A jointly activated set now requires a joint selection probability. Products of one-event corrections require a declared conditional factorization.
5. **P2: correlated sources could be counted as independent evidence.** Source-weighted or tempered products are explicitly generalized Bayesian updates unless a coherent joint source model derives them.
6. **P2: Anti-Pigeon sharing could become self-certifying.** Posterior sharing now uses the externally evaluated target-law diameter certificate, plus support, horizon, epoch, and provenance gates. Posterior agreement alone cannot certify sharing.
7. **P2: changepoint semantics were too broad.** A monitor fed only activated evidence is now stated to detect changes in the selected process. Full-stream regime claims require the selection model or design-aware independent audits.
8. **P2: bounded audit sampling lacked post-cap inclusion probabilities.** A frozen uniform reservoir now records final inclusion probabilities and uses design-weighted estimators. An unweighted capped convenience sample cannot certify omitted influence.
9. **P2: posterior publication and growth were underspecified.** Posterior, key, dependent residual certificate, and epoch now publish atomically. Posterior storage has a declared capacity and deterministic eviction rule while immutable audit provenance is retained.
10. **P2: fixed-resource language could hide growing state.** Fast-path claims now require bounds on retrieval size, graph degree, activated candidates, hypothesis or sufficient-statistic dimension, changepoint states, audit reservoir, and vector-query work. Deep particle and variational methods remain slow-path work by default.
11. **P2: GitHub rejects the operator-name macro used by earlier and new formulas.** All remaining instances were replaced by equivalent roman math labels before release generation.
12. **P2: the introduction retained the old procedure count.** The prose now states seven steps, matching the seven numbered operations after Bayesian activation was inserted.
13. **P1 rendering: a standalone equals-sign line broke GitHub display math.** The selection-likelihood equality now keeps the equals sign on the formula's first line, preventing Markdown from interpreting the preceding line as a Setext heading.

## Cross-Contract Checks

- **Time and leakage:** activation may use an arrived frame only after its availability time and cannot use a later evaluation target, audit result, or graph revision.
- **Risk integration:** candidate replay reconstructs posterior, cache, changepoint, confidence, and epoch state from the same raw as-of history.
- **No-event and horizon semantics:** the Bayesian layer does not alter the residual model's distinct point and law components or permit post-horizon point residuals.
- **Causality:** vector or graph locality is predictive unless an explicit SCM and identification strategy support causal language.
- **Proper scoring:** evaluation remains on the complete chronological outcome stream; selected-only scores are reported only as strata.
- **Anti-Pigeon:** failed or missing sharing certificates split posterior keys and nominate review; they do not silently pool evidence.
- **Resource claims:** constant-per-sample means independence from accumulated history under fixed caps, not independence from model dimension, particles, iterations, graph degree, or hardware.
- **Publication consistency:** readers observe one complete old or new posterior-key-residual-epoch version.

## Required Empirical Falsifiers

The dedicated Bayesian experiment compares update-all, naive selective, selection-conditioned selective, separate-posterior, Anti-Pigeon-sharing, and simulation-oracle variants. It reports full-stream proper score and calibration, activated-stratum calibration, omitted-influence coverage, false posterior merges, missed high-priority evidence, changepoint delay and false alarms, approximation error, audit design weights, memory, and tail latency.

The upgrade remains a mathematical and architectural specification. Passing this audit establishes internal contract consistency, not empirical speed, calibration, or predictive benefit.
