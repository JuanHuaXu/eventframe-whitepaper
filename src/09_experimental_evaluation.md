# 9. Experimental Evaluation

EventFrame's main claims require experiments. The framework should be evaluated on whether compressed event frames preserve intervention-relevant distinctions, whether structured events improve interpretability and prediction, whether residual caches reduce cost or error, whether property fuzzing discovers stable invariants, and whether abstraction preserves target-relevant transition behavior.

A minimal synthetic event world should generate trajectories with known transition rules. Each event should expose the fields:

\[
e_t = (w_t, a_t, \tau_t, \ell_t, m_t, h_t, x_t, c_t).
\]

The generator should include many microscopic variables but control which variables actually influence event timing or downstream state. It should also allow multiple temporal resolutions, such as seconds, milliseconds, and microseconds. This makes it possible to test whether coarse-graining preserves intervention-effective distinctions, whether fuzzing recovers true dependencies, and whether abstraction removes irrelevant detail without damaging prediction.

The first experiment measures temporal prediction accuracy. Compare:

1. A baseline predictor without residual cache.
2. A baseline predictor with episodic retrieval.
3. A baseline predictor with residual cache.
4. A full EventFrame reference predictor.

The primary metric is mean or median \(\mathcal{L}_{time}^{H}\), with confidence intervals over trajectories. Secondary metrics may include actor, action, and location diagnostics. The key question is whether the residual formulation improves temporal prediction without hiding which fields contributed.

The second experiment tests compression and intervention relevance. Define a coarse-graining \(\Gamma_{\Delta_\tau}\) from microscopic variables to event frames and vary \(\Delta_\tau\). A distinction should be treated as intervention-effective only when intervening on it changes the target beyond a declared threshold \(\eta_Y\). This experiment tests the event sparsity hypothesis directly: useful event frames should be sparse relative to the microscopic substrate and candidate-frame set while still preserving target-relevant interventions.

The third experiment measures cache utility. Report cache hit rate, post-hit temporal loss, baseline temporal loss on the same examples, and the fraction of hits that improve prediction. A residual cache is useful only if retrieved residuals improve over the baseline often enough to justify lookup and maintenance. Cache pollution should be measured by tracking entries that repeatedly fail to improve predictions.

The fourth experiment evaluates property fuzzing. For each field \(\phi_i\), perturb it across a declared range and compute:

\[
S_g = \min\left(1, \frac{\Delta_g}{\eta_g}\right).
\]

The experiment should compare discovered stable fields to the known generating rules. If the generator makes location irrelevant to timing, temporal fuzzing should identify location as stable for that target. If the generator makes actor identity relevant, actor perturbation should change temporal predictions beyond threshold.

The fifth experiment evaluates confluence and divergence. Generate event streams that eventually become prediction-equivalent and test whether a merge operator \(\mu_{\delta}\) can replace them with an aggregate event without degrading temporal prediction. Generate separate cases in which small perturbations amplify into target-distinct downstream branches and test whether the system preserves those divergence-effective distinctions rather than merging them away. Each event-frame group must retain at least one representative frame, and the experiment should measure whether those representatives correctly identify split thresholds and merge thresholds.

The sixth experiment evaluates invariant stability over time. Candidate invariants discovered in one trajectory segment should be tested on later segments and under distribution shift. This distinguishes local accidental stability from robust invariance. Report the rate at which candidate invariants remain valid, fail, or become conditional.

The seventh experiment evaluates lumpability and Anti-Pigeon refinement. Define projections \(\pi\) that remove or group selected fields. Compare detailed and abstract predictors using temporal loss and transition-distribution divergence. A merge should be accepted only when loss degradation remains below a declared threshold and at least one representative frame is retained for every event-frame group. Then test the dual split criterion: for each bucket \(B\), estimate \(\max_{e_i,e_j \in B} D_{ij}\). If the maximum future divergence exceeds \(\epsilon_{AP}\), the bucket should split or be marked divergence-sensitive. This experiment directly tests whether surface-similar groupings are rejected when they hide target-distinct futures.

The eighth experiment evaluates runtime tradeoffs. Measure fast-path latency, slow-path cost, cache update cost, and memory growth. Report the conditions under which residual lookup approximates constant-time behavior and the conditions under which it fails.

Ablation studies should remove one component at a time: residual cache, episodic memory, fuzzing, abstraction, and slow-path refinement. The paper should treat negative results as informative. If residual caches fail in a domain, the failure helps characterize when EventFrame is useful. If fuzzing produces unstable invariants, the thresholds or perturbation families may be wrong.

The evaluation plan is deliberately falsifiable. Each claim should be tied to a measurable result. The next section lists open problems that remain even if the initial experiments succeed.
