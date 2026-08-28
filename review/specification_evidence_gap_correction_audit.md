# Specification-to-Evidence Gap Correction Audit

Date: 2026-08-28

Scope: reviewer concerns about joint Bayesian coherence, empirical certificate boundaries, selective-support positivity, coupled-update stability, sheaf and causal terminology, and missing implementation evidence.

## Finding Classification

1. **Likelihood/kernel mathematics, confirmed:** prose named one model family but did not display the marginal equalities or the conditional factorization needed when the outcome kernel omits the evidence packet. The paper now defines one joint evidence-and-outcome kernel, a dominating evidence measure, both marginals, the Radon--Nikodym likelihood identity, the context-sufficient outcome-kernel identity, and the required factorization. If the factorization fails, the kernel must retain the evidence or additional history.
2. **Anti-Pigeon evidence boundary, recommendation confirmed:** the prior mathematics already required simultaneous coverage or exhaustive/continuity support, but the limitation was not prominent enough. Claims and conclusion now state that the certificate is empirical and conditional on those premises attaining coverage.
3. **Selective-support boundary, confirmed:** pointwise positive selection probability did not provide a reliable certified region. The paper now requires an analytic or simultaneous lower bound uniformly over the declared parameter family to exceed a frozen positive floor. Histories outside that region receive working-posterior or no-update semantics.
4. **Continuous-learning stability, confirmed as open:** no joint convergence theorem covers posterior, residual, epoch, graph, and abstraction transitions. Finite publication/invalidation budgets, hysteresis, cooldowns, and conflict ordering now bound same-evidence-epoch thrashing, while cross-epoch convergence remains explicitly open.
5. **Sheaf status, already resolved:** the paper consistently calls the construction sheaf-inspired until assigned spaces and identity/composition laws are instantiated.
6. **Causal status, already resolved:** ordinary why/how and predictive-dependency graphs are not causal evidence; causal claims require an explicit SCM and identification contract.
7. **Benchmarks, specification only:** the evaluation plan now explicitly requires activation rate, selection-support coverage, never-nominated high-priority events, false Anti-Pigeon merges, calibration, omitted-influence coverage, tail latency, and update-all and naive-selective baselines. No empirical result is claimed.

## Corrected Invariants

**Joint-model coherence.** For every declared bucket, parameter, and history,

\[
L_K=\frac{d\mathbb P_{K,\theta}^{\Xi}}{d\nu_K},
\qquad
\mathbb P_{K,\theta}^{Z}(A\mid\mathfrak h)
=\mathsf P_{H,K}(A\mid\theta,c_k(\mathfrak h)).
\]

Because the displayed outcome kernel omits \(\xi\), the contract also requires

\[
\mathbb P_{K,\theta}(d\xi,dz\mid\mathfrak h)
=L_K(\xi\mid\theta,\mathfrak h)\nu_K(d\xi)
\mathsf P_{H,K}(dz\mid\theta,c_k(\mathfrak h)).
\]

Failure of any required marginal or factorization identity makes the construction modular rather than posterior predictive; empirical calibration cannot repair the missing identity.

**Selective-support claim.** Full-stream selection correction is claimed only when

\[
\underline p_{K,t}^{\mathrm{sel}}(\mathfrak h)
\ge p_{\min}^{\mathrm{sel}}>0.
\]

Inactive objects inside the candidate universe may enter the independent audit. Objects outside that universe are outside both certificates absent exhaustive or verified envelope coverage.

**Bounded immediate churn.** Within evidence epoch \(j\),

\[
N_{\mathrm{pub}}(j)\le B_{\mathrm{pub}},
\qquad
N_{\mathrm{inv}}(j)\le B_{\mathrm{inv}}.
\]

This is an operational bound, not a convergence theorem for a drifting stream.

## Falsifiers

1. Pairing marginals from different model families must fail the joint-model identity even if held-out calibration looks favorable.
2. Histories whose simultaneous selection lower bound falls below the floor must not receive a full-stream posterior claim.
3. A same-epoch adversarial update cycle must stop or freeze when either publication budget is exhausted.
4. Failed target-law or audit coverage invalidates the Anti-Pigeon certificate rather than being treated as evidence of a safe merge.

## Residual Risk

The paper remains a specification without implementation evidence. It does not establish online convergence, universal nomination coverage, Anti-Pigeon coverage in a concrete domain, or runtime performance. Those claims remain contingent on the stated experiments.
