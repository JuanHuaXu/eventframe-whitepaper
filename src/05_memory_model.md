# 5. Memory Model

EventFrame uses memory for two different purposes: recalling prior events and reusing prior corrections. These purposes should not be collapsed. Episodic memory stores cases. A residual cache stores adjustments to the posterior-predictive base law and template that were actually issued before correction. The fallback baseline is one possible base. Both memories may support prediction, but they answer different questions.

An episodic key-value cache can be written:

\[
\mathcal{C}_E = \{(u_i, v_i, s_i)\}_{i=1}^{M},
\]

where \(u_i\) is a retrieval key, \(v_i\) is an event frame, trajectory segment, or summary, and \(s_i\) is metadata. Given a context \(C_t\), an episodic lookup retrieves prior cases that resemble the current situation. The operational use is case recall: retrieve examples that may inform the baseline model, explain the current state, or provide analogies for review.

A residual cache is different:

\[
\mathcal{C}_R = \{(\kappa_i, r_i, s_i)\}_{i=1}^{N}.
\]

Here \(r_i\) is not a prior event. It is a correction to a prior pre-residual prediction. The operational use is correction reuse: if the current context resembles a past context where that base law or template missed in a known direction, apply a residual through its typed point operator or law kernel only when the posterior-motion certificate still covers the current base.

The conceptual distinction is important. Episodic memory says, "something like this happened before." Residual memory says, "the predictor made this kind of mistake before." A system can have useful episodic recall but poor residual reuse if prior cases are similar but their prediction errors differ. Conversely, a residual may be reusable even when the full episode is not otherwise relevant.

Prediction combines the two memories by priority rather than by collapse. A reference flow is:

1. Nominate and activate the bounded Bayesian frontier, then retrieve or update valid local posteriors.
2. Form the posterior-predictive base \((\mathsf Q_t^0,b_t^0)\), falling back to \((\mathsf Q_B,B)\) when no valid belief bucket exists.
3. Try action-residual lookup in \(\mathcal{C}_A\), including posterior-predictive version and motion checks.
4. If that record is not certified, try general residual lookup in \(\mathcal{C}_R\) under the same base-law compatibility requirement.
5. If residual confidence is still insufficient, retrieve episodic cases from \(\mathcal{C}_E\) to explain uncertainty or schedule slow-path review; any change to the current scored law must pass through a declared predictive map and the same gates.
6. Compose and gate the candidate; after observation, update episodic memory, posterior state, residual confidence, and any cache entry that was used or falsified.

This flow keeps the low-latency path cheap while preserving a fallback to richer case evidence. Residual memory can answer quickly when the current situation matches a known error pattern. Episodic memory becomes more important when the residual cache is missing, low-confidence, stale, or contradicted by recent outcomes.

Similarity lookup requires declared key functions and distances. For episodic memory, the key function may emphasize entities, action types, and temporal neighborhoods. For residual memory, the key should emphasize features that predict pre-residual forecast error and include the base-law certificate identity. These are not necessarily the same. For example, two events may share an action type but differ in timing dynamics; they may be episodically similar while producing different residuals.

Consolidation is the process of updating memory after observation. A conservative consolidation step should:

1. Record the observed event \(e_{t+1}\) with provenance and confidence.
2. Compute proper predictive loss and the event-aware timing diagnostic.
3. Estimate whether the error relative to the recorded \((\mathsf Q_t^0,b_t^0)\) is systematic enough to store as a residual.
4. Update or decay cache entries based on age, confidence, and repeated utility.
5. Preserve at least one traceability frame and the coverage-aware context audit set required by Section 7.
6. Mark low-confidence entries so they cannot dominate future predictions.

Cache pollution is the main risk. If every error becomes a residual, the cache may memorize noise. If keys are too broad, residuals are applied in inappropriate contexts. If keys are too narrow, useful residuals are never reused. The cache should therefore track hit rate, post-correction loss, and whether retrieved residuals improve over the contemporaneous pre-residual base.

Fast-path memory use should be cheap. A practical implementation may use approximate nearest-neighbor lookup, hashed keys, or bounded-size caches. The paper treats constant-time lookup as an approximation, not as a guarantee. Slow-path memory refinement may be more expensive because it runs after the initial prediction, when latency pressure is lower.

Representative preservation is a memory responsibility. A single traceability frame prevents a group from becoming an empty label, but boundary detection requires the context audit set, its associated anchor frames, coverage metadata, and sampling history. If these are discarded, the runtime must mark the group unaudited rather than infer stability from one example.

## Selective Bayesian Update Frontier

EventFrame may attach a bounded Bayesian belief state to an event bucket, residual family, latent regime, or declared hypothesis family. It does not update every stored belief after every frame. Let \(\mathfrak E_t^B\) be the finite declared universe of event and hypothesis identities eligible for nomination at \(t\). Vector retrieval and graph locality propose a finite update frontier. Let \(\mathcal R_t^{\mathrm{vec}}\) be at most \(k_v\) candidates returned by the frozen vector-retrieval rule. Let \(\mathcal N_t^{\mathrm{sh}}\) be the bounded neighborhood returned by the abstraction compatibility graph. This is a sheaf-inspired neighborhood, not a sheaf-theoretic neighborhood unless the required restriction identity and composition laws have actually been instantiated.

If an explicit SCM \(\mathfrak M\) exists, let \(v_t^E\) be the graph node associated with the current context and use its declared parents and children. A child here is an outgoing relationship already present in the as-of graph, not a future realized event. Without an identified SCM, the corresponding predictive-dependency neighbors may be used but may not be called causal. The candidate frontier is

\[
\mathcal N_t^B=
\mathcal R_t^{\mathrm{vec}}
\cup\mathcal N_t^{\mathrm{sh}}
\cup
\begin{cases}
\mathrm{Pa}_{\mathfrak M}(v_t^E)\cup
\mathrm{Ch}_{\mathfrak M}(v_t^E),&\mathfrak M\text{ is available},\\
\mathcal N_t^{\mathrm{pred}},&\text{otherwise.}
\end{cases}
\]

Every set is constructed from the as-of snapshot and has a predeclared cardinality or degree cap. For an evidence-bearing event \(e\in\mathcal N_t^B\), define four measurable scores in \([0,1]\): vector relevance \(v_t^B(e)\), sheaf-inspired neighbor compatibility \(n_t^B(e)\), novelty \(u_t^B(e)\), and source independence \(s_t^B(e)\). Freeze non-negative weights satisfying \(\alpha_B+\beta_B+\gamma_B+\delta_B=1\), and set

\[
J_t^{\mathrm{nom}}(e)=\mathbf1\{e\in\mathcal N_t^B\},
\qquad
J_t^{\mathrm{evid}}(e)=
\mathbf1\{\xi_t(e)\text{ exists and }a(\xi_t(e))\le t\},
\qquad e\in\mathfrak E_t^B.
\]

An as-of graph child or declared hypothesis may be nominated while \(J_t^{\mathrm{evid}}(e)=0\). Such a candidate can lower review latency or reserve state, but it cannot activate or update a posterior until evidence is available. Define the activation score on the evidence-ready nominated domain and extend it by zero elsewhere:

\[
A_t^B(e)=
\begin{cases}
\alpha_Bv_t^B(e)+\beta_Bn_t^B(e)
+\gamma_Bu_t^B(e)+\delta_Bs_t^B(e),
&J_t^{\mathrm{nom}}(e)J_t^{\mathrm{evid}}(e)=1,\\
0,&\text{otherwise.}
\end{cases}
\]

Let \(c_t^B(e)\in[0,1]\) be structural criticality available before the downstream target whose performance will be evaluated. For fixed \(0\le\tau_{\min}\le\tau_{\max}\le1\), define the lower threshold for critical neighbors by

\[
\tau_t^B(e)=
\min\!\left(\tau_{\max},
\max\!\left(\tau_{\min},
\tau_0-\lambda_{\mathrm{crit}}c_t^B(e)\right)\right),
\qquad
J_t^{\mathrm{act}}(e)=
J_t^{\mathrm{nom}}(e)J_t^{\mathrm{evid}}(e)
\mathbf1[A_t^B(e)\ge\tau_t^B(e)].
\]

All nomination, evidence-readiness, scoring, normalization, weighting, threshold, tie-break, and source-dependence rules are part of \(\Lambda_{\mathrm{eval}}\). A score may use a newly arrived frame once that frame is available, but it may not use a later target outcome, posterior audit, or graph revision. Because \(J_t^{\mathrm{act}}\) is defined on all of \(\mathfrak E_t^B\) and equals zero outside the frontier or before evidence readiness, its model probability includes nomination, evidence readiness, and threshold admission. Activation controls expenditure; it does not establish that candidates are safe to pool.

Anti-Pigeon controls posterior granularity. For a candidate bucket \(K\), let \(v_K^B\) be the abstraction epoch under which its posterior-sharing certificate was produced. Sharing is permitted only when

\[
J_{K,t}^{\mathrm{share}}=
\mathbf1\!\left\{
D_K^{\mathrm{cert},\star}\le\epsilon_{B,\mathrm{share}},\quad
n_K^{\mathrm{eff}}\ge n_{B,\min},\quad
v_K^B=v_t,\quad
H_K=H,\quad
s_K^B\text{ is valid}
\right\}.
\]

The certificate concerns externally evaluated downstream target-law disagreement, not agreement among the candidate model's own posteriors. The fast path checks a materialized certificate; it does not recompute \(D_K^{\mathrm{cert},\star}\). Active events in a certified bucket may update one shared posterior. If the certificate fails or is unavailable, each event retains or receives a separate posterior and the case may be routed to slow-path split review. Unrelated events are ignored by the production update except for the audit and changepoint mechanisms below.

Let \((\Theta_K,\mathscr A_{\Theta_K})\) be a declared parameter space and let \(q_{K,t^-}\in\mathcal P(\Theta_K)\) be the cached prior available before the update. Let \(\xi_t(e)\) be the evidence packet extracted from an available event and its currently available labels. For an activated, sharing-approved evidence-packet set \(\mathcal X_{K,t}^{\mathrm{act}}\), an ordinary Bayesian update is

\[
q_{K,t}^{+}(d\theta)=
\frac{
L_K^{\mathrm{sel}}(\mathcal X_{K,t}^{\mathrm{act}}\mid\theta,\mathfrak h_t)
q_{K,t^-}(d\theta)}
{\int_{\Theta_K}
L_K^{\mathrm{sel}}(\mathcal X_{K,t}^{\mathrm{act}}\mid\vartheta,\mathfrak h_t)
q_{K,t^-}(d\vartheta)},
\]

provided the denominator is finite and strictly positive. Because novelty or compatibility may depend on the arrived event, activation is generally informative. For one evidence packet \(\xi\), the selection-conditioned likelihood is

\[
L_K^{\mathrm{sel}}(\xi\mid\theta,\mathfrak h_t,J^{\mathrm{act}}=1)=
\frac{
P_\theta(J^{\mathrm{act}}=1\mid\xi,\mathfrak h_t)
p_\theta(\xi\mid\mathfrak h_t)}
{P_\theta(J^{\mathrm{act}}=1\mid\mathfrak h_t)},
\]

on the domain where the denominator is positive. For a jointly activated evidence set, the contract must model the joint activation probability; multiplying one-event selection corrections is valid only under a declared conditional factorization. Selection may be ignored only under a stated conditional-ignorability result, for example when activation depends exclusively on already conditioned-on pre-evidence variables. If the selection probability cannot be modeled, the result is called an activation-conditioned working posterior, not a calibrated posterior for the full event stream, and must be tested against the independent audit stream.

Because \(J_t^{\mathrm{act}}\) already contains \(J_t^{\mathrm{nom}}\) and \(J_t^{\mathrm{evid}}\), both the numerator and marginal denominator integrate the complete two-stage nomination-and-activation event. Conditioning only on the threshold comparison while treating frontier membership as fixed is valid only under a separately stated conditional design.

The effective posterior consumed by Section 4 is

\[
q_{K,t}^{\mathrm{eff}}=
\begin{cases}
q_{K,t}^{+},&
\mathcal X_{K,t}^{\mathrm{act}}\neq\varnothing
\text{ and the update is valid},\\
q_{K,t^-},&\text{otherwise, provided the cached prior is valid}.
\end{cases}
\]

Buckets without either valid branch are excluded from \(\mathcal K_t^{\mathrm{bel}}\). Section 4 maps the resulting finite posterior family into \(\mathsf Q_t^0\), applies only residuals certified against that base law, and scores the final \(\mathsf Q_t^R\).

Likewise, a product of conditionally independent likelihoods is ordinary Bayes only when the declared source model justifies that factorization. Tempering correlated-source contributions,

\[
q_{K,t}^{+}(d\theta)\propto
q_{K,t^-}(d\theta)
\prod_{e\in\mathcal X_{K,t}^{\mathrm{act}}}
p_\theta(\xi_t(e)\mid\mathfrak h_t)^{\omega_t(e)},
\qquad 0\le\omega_t(e)\le1,
\]

defines a generalized or power posterior unless it is derived from a joint generative model. Source-independence scoring therefore cannot by itself justify multiplying evidence as if it were independent.

For cheap regime monitoring, a bucket may maintain a bounded approximation to a Bayesian online changepoint run-length posterior [17,18]. Let \(R_{K,t}\in\mathbb N_0\) be run length and define

\[
J_{K,t}^{\mathrm{cp}}=
\mathbf1\!\left[
P(R_{K,t}=0\mid\mathfrak h_t)\ge\gamma_{\mathrm{cp}}
\right].
\]

When this indicator fires, the runtime applies the dependency-closure bump \(\mathsf B_{\mathcal D}\) and stale-marking operator \(\mathsf I_{\mathcal D}\) from Section 7 to the affected posterior, residual, and graph-version region before expanding the review frontier and routing recalibration to the slow path. A monitor fed only activated evidence detects changes in the selected process. It supports a full-stream regime claim only when its transition and observation model includes the selection mechanism or when the independent audit stream is incorporated with its sampling design. Exact classical run-length support can grow with the stream; a constant-memory or constant-time claim therefore requires a declared cap, pruning rule, or finite sufficient-statistic approximation and must report its approximation error.

Selective retrieval can become self-confirming by never revisiting what it has learned to ignore. EventFrame therefore reserves a predeclared audit probability \(\pi_{\mathrm{audit}}>0\). Conditional on the inactive candidate set and independently of activation-score magnitude, draw

\[
J_t^{\mathrm{audit}}(e)\sim\mathrm{Bernoulli}(\pi_{\mathrm{audit}}).
\]

If the accepted audit sample exceeds a fixed capacity \(N_{\mathrm{audit}}^{\max}\), a frozen uniform reservoir subsamples it and records every final inclusion probability. Audit estimators use the corresponding design weights; an unweighted capped convenience sample cannot support the omission certificate.

For one audited inactive evidence packet \(e\), let \((q_{K,t}^{\mathrm{loc}})_K\) be the effective posterior family produced by the ordinary frontier and let \((q_{K,t}^{\mathrm{exp}}(e))_K\) be the shadow family after admitting that packet through the same selection-aware update. Section 4 maps these to posterior-predictive bases \((\mathsf Q_t^{0,\mathrm{loc}},b_t^{0,\mathrm{loc}})\) and \((\mathsf Q_t^{0,\mathrm{exp}}(e),b_t^{0,\mathrm{exp}}(e))\). Replay the complete residual policy in each state:

\[
\mathsf Q_t^{\mathrm{local}}=
\mathfrak F_R(\mathsf Q_t^{0,\mathrm{loc}},b_t^{0,\mathrm{loc}},C_t;S_{t^-}^{\mathrm{loc}}),
\qquad
\mathsf Q_t^{\mathrm{expanded}}(e)=
\mathfrak F_R(\mathsf Q_t^{0,\mathrm{exp}}(e),b_t^{0,\mathrm{exp}}(e),C_t;S_{t^-}^{\mathrm{exp}}(e)).
\]

Thus both laws include posterior prediction, posterior-aware residual selection, residual composition, and pre-risk fallback. Define the normalized Jensen--Shannon divergence on \(\mathcal P(\mathcal Z_H)\):

\[
D_{\mathrm{omit}}(P,Q)=
\frac{\mathrm{KL}(P\Vert M)+\mathrm{KL}(Q\Vert M)}
{2\log 2},
\qquad M=\frac{P+Q}{2}.
\]

Using natural logarithms, this measurable divergence lies in \([0,1]\). Let \(\mathbb P_{\mathrm{audit},K,t}\) be the frozen design distribution over audit-eligible inactive packets in bucket \(K\), including the recorded reservoir inclusion probabilities, and define the audit-population omission risk

\[
\Delta_{K,t}^{\mathrm{omit}}=
\mathbb E_{e\sim\mathbb P_{\mathrm{audit},K,t}}
\left[
D_{\mathrm{omit}}\!\left(
\mathsf Q_t^{\mathrm{local}},
\mathsf Q_t^{\mathrm{expanded}}(e)
\right)
\right].
\]

The predeclared procedure \(\mathfrak U_{\mathrm{omit}}^{\mathrm{seq}}(\alpha_{\mathrm{omit}})\) is a design-weighted simultaneous upper confidence sequence covering every named bucket, inspected expansion, and repeated audit time. Let \(\mathfrak K_t^{\mathrm{audit}}\) be the buckets with positive effective audit support after reservoir sampling and valid design weights. Set

\[
U_t^{\mathrm{omit}}=
\max_{K\in\mathfrak K_t^{\mathrm{audit}}}
\mathfrak U_{\mathrm{omit}}^{\mathrm{seq}}(\alpha_{\mathrm{omit}})
\left[\Delta_{K,t}^{\mathrm{omit}}\right].
\]

If \(\mathfrak K_t^{\mathrm{audit}}=\varnothing\), the system reports no omission certificate rather than substituting zero. Local updating is certified only in the declared audit-population sense while \(U_t^{\mathrm{omit}}\le\epsilon_{B,\mathrm{omit}}\). A universal omitted-event claim additionally requires exhaustive audit coverage or a verified continuity or envelope bound. A plug-in divergence, unweighted capped sample, or pointwise interval without simultaneous sequential coverage is not a certificate.

Every production or shadow decision records

\[
(J_t^{\mathrm{nom}},J_t^{\mathrm{evid}},A_t^B,\tau_t^B,
J_t^{\mathrm{act}},J_{K,t}^{\mathrm{share}},J_t^{\mathrm{audit}},
v_t,\upsilon_t^{\mathrm{bel}},H,s_t^{\mathrm{prov}}),
\]

together with audit inclusion probability, so calibration can be reconstructed under as-of replay.

Before an ordinary posterior update publishes in place, its posterior-predictive base is compared with the fixed reference for \(\upsilon_t^{\mathrm{bel}}\) using the analytic or simultaneous bound declared in Section 4. It retains that version only while every affected materialized motion margin remains non-negative. Otherwise \(\mathsf B_{\mathcal D}\) bumps the dependency closure and \(\mathsf I_{\mathcal D}\) invalidates affected residuals. Posterior, posterior key, dependent residual certificate, graph version, and epoch then publish atomically. Prediction readers observe one complete old or new version, never a mixed state. Posterior storage has a declared capacity and deterministic eviction rule. Eviction removes fast-path reuse eligibility but preserves immutable provenance required by later audits.

Streaming variational Bayes motivates incremental and asynchronous posterior approximation [14]. Streaming variational Monte Carlo and online variational sequential Monte Carlo provide richer state-space and particle-based alternatives [15,16], but their constant-per-sample or online properties do not make their particle count, parameter dimension, optimization, or hardware cost free. Pattern Markov Chains are relevant only for declared event-pattern completion forecasts, not as a universal next-event Bayesian model [19]. Work on out-of-distribution sequential event prediction motivates latent-context and shift-aware evaluation [20], but EventFrame does not inherit its causal interpretation without the corresponding identification assumptions.

The memory model supports the overall EventFrame loop. Episodic memory helps interpret and compare cases. Residual memory corrects recurring transition errors. The selective Bayesian frontier updates bounded cached beliefs, while Anti-Pigeon decides which evidence may share one posterior. Slow-path consolidation, changepoint review, and independent audits keep all three memories from turning into overconfident filtered history. The next section uses perturbation rather than recall to discover which event properties are stable under prediction.
