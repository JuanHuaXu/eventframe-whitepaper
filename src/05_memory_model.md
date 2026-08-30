# 6. Memory, Bayesian Updating, and Drift

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

Here \(r_i\) is not a prior event. It is a correction to a prior pre-residual prediction. The operational use is correction reuse: if the current context resembles a past context where that base law or template missed in a known direction, apply a residual through its typed point operator or law kernel only when every mode-applicable law or template motion certificate still covers the current base.

The conceptual distinction is important. Episodic memory says, "something like this happened before." Residual memory says, "the predictor made this kind of mistake before." A system can have useful episodic recall but poor residual reuse if prior cases are similar but their prediction errors differ. Conversely, a residual may be reusable even when the full episode is not otherwise relevant.

Prediction combines the two memories by priority rather than by collapse. A reference flow is:

1. Nominate the bounded Bayesian frontier, apply the frontier-all cheap update to every evidence-ready member, and use the frozen activation score only to nominate bounded deep review unless a separately validated selective-update policy is in force.
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
5. Preserve at least one traceability frame and the coverage-aware context audit set required by Section 8.
6. Mark low-confidence entries so they cannot dominate future predictions.

Cache pollution is the main risk. If every error becomes a residual, the cache may memorize noise. If keys are too broad, residuals are applied in inappropriate contexts. If keys are too narrow, useful residuals are never reused. The cache should therefore track hit rate, post-correction loss, and whether retrieved residuals improve over the contemporaneous pre-residual base.

Fast-path memory use should be cheap. A practical implementation may use approximate nearest-neighbor lookup, hashed keys, or bounded-size caches. The paper treats constant-time lookup as an approximation, not as a guarantee. Slow-path memory refinement may be more expensive because it runs after the initial prediction, when latency pressure is lower.

Representative preservation is a memory responsibility. A single traceability frame prevents a group from becoming an empty label, but boundary detection requires the context audit set, its associated anchor frames, coverage metadata, and sampling history. If these are discarded, the runtime must mark the group unaudited rather than infer stability from one example.

## Bounded Bayesian Update Frontier

EventFrame may attach a bounded Bayesian belief state to an event bucket, residual family, latent regime, or declared hypothesis family. It does not update every stored belief after every frame. Let \(\mathfrak E_t^B\) be the finite declared universe of event and hypothesis identities eligible for nomination at \(t\). Vector retrieval and graph locality propose a finite update frontier. Let \(\mathcal R_t^{\mathrm{vec}}\) be at most \(k_v\) candidates returned by the frozen vector-retrieval rule. Let \(\mathcal N_t^{\mathrm{sh}}\) be the bounded neighborhood returned by the abstraction compatibility graph. This is a sheaf-inspired neighborhood, not a sheaf-theoretic neighborhood unless the required restriction identity and composition laws have actually been instantiated. Updating all members below always means all evidence-ready members of this bounded frontier, not all records in the corpus.

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

Freeze an update policy \(q_B\in\{q_{\mathrm{FA}},q_{\mathrm{sel}}\}\), where \(q_{\mathrm{FA}}\) is bounded-frontier-update-all and \(q_{\mathrm{sel}}\) is threshold-selective. Define the total update-admission indicator

\[
J_t^{\mathrm{upd},q_B}(e)=
\begin{cases}
J_t^{\mathrm{nom}}(e)J_t^{\mathrm{evid}}(e),
&q_B=q_{\mathrm{FA}},\\
J_t^{\mathrm{act}}(e),&q_B=q_{\mathrm{sel}}.
\end{cases}
\]

The reference policy is \(q_{\mathrm{FA}}\). Under the implemented replacement, \(J_t^{\mathrm{act}}\) nominates bounded deep work such as model comparison, particle refinement, graph expansion, or recalibration while every evidence-ready frontier member still receives the cheap update. A selective cheap-update policy is admitted only as a measured resource-quality tradeoff; it is not presumed superior merely because it performs fewer updates. All nomination, evidence-readiness, scoring, normalization, weighting, threshold, tie-break, policy-selection, and source-dependence rules are part of \(\Lambda_{\mathrm{eval}}\). A score may use a newly arrived frame once that frame is available, but it may not use a later target outcome, posterior audit, or graph revision. Because \(J_t^{\mathrm{upd},q_B}\) is defined on all of \(\mathfrak E_t^B\) and equals zero outside the frontier or before evidence readiness, its model probability includes the complete admission path. A conforming implementation materializes and scores only \(\mathcal N_t^B\); it represents the zero branch outside that frontier sparsely rather than scanning \(\mathfrak E_t^B\). For \(q_{\mathrm{FA}}\), admission is nomination plus evidence readiness; for \(q_{\mathrm{sel}}\), it additionally includes threshold admission. Admission controls expenditure; it does not establish that candidates are safe to pool.

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

The certificate concerns externally evaluated downstream target-law disagreement, not agreement among the candidate model's own posteriors. Its guarantee is empirical and conditional on the declared target-law estimator, audit design, simultaneous coverage procedure, and any continuity bound actually attaining their stated coverage; EventFrame does not prove those premises from its architecture. The fast path checks a materialized certificate; it does not recompute \(D_K^{\mathrm{cert},\star}\). Admitted events in a certified bucket may update one shared posterior. If the certificate fails or is unavailable, each event retains or receives a separate posterior and the case may be routed to slow-path split review. Unrelated events are ignored by the production update except for the audit and changepoint mechanisms below.

A bounded Bayesian comparison may nominate a sharing or splitting review, but it does not certify its own abstraction. In the Bernoulli retrieval-usefulness specialization, retain member-level sufficient statistics \((u_e,v_e)\) even when a current certificate lets members share one operational posterior, where \(u_e\) and \(v_e\) are the design-weighted useful and not-useful counts available in the current evidence epoch. Under a common \(\mathrm{Beta}(a_0,b_0)\) prior, the log marginal evidence for one shared rate and for independent member rates is

\[
\begin{aligned}
\ell_K^{\mathrm{share}}
&=\log\frac{\mathrm B\!\left(a_0+\sum_{e\in K}u_e,
b_0+\sum_{e\in K}v_e\right)}{\mathrm B(a_0,b_0)},\\
\ell_K^{\mathrm{split}}
&=\sum_{e\in K}
\log\frac{\mathrm B(a_0+u_e,b_0+v_e)}{\mathrm B(a_0,b_0)}.
\end{aligned}
\]

For a frozen split prior \(\pi_K^{\mathrm{split}}\in(0,1)\), define

\[
p_K^{\mathrm{split}}
=\mathrm{logistic}\!\left(
\log\frac{\pi_K^{\mathrm{split}}}{1-\pi_K^{\mathrm{split}}}
+\ell_K^{\mathrm{split}}-\ell_K^{\mathrm{share}}
\right).
\]

Exact equality is unnecessarily strict for operational pooling. Freeze a region-of-practical-equivalence width \(\epsilon_{B,\mathrm{eq}}>0\) and a declared posterior calculation, exact or approximation-controlled, for

\[
p_K^{\mathrm{eq}}=
P\!\left(
\max_{e,e'\in K}|\theta_e-\theta_{e'}|
\le\epsilon_{B,\mathrm{eq}}
\,\middle|\,(u_e,v_e)_{e\in K}
\right).
\]

The two probabilities are deliberately not complements. The quantity
\(p_K^{\mathrm{split}}\) is posterior model probability for the independent-member
model against the shared-parameter model, whereas \(p_K^{\mathrm{eq}}\) is posterior
mass inside a declared practical-equivalence region. The marginal-likelihood
comparison therefore has no split margin that must equal
\(\epsilon_{B,\mathrm{eq}}\), and in general
\(p_K^{\mathrm{split}}+p_K^{\mathrm{eq}}\ne1\). The contract freezes the split prior,
practical-equivalence width, and both decision thresholds independently.

With \(n_e^{\mathrm{eff}}=u_e+v_e\), minimum member support \(n_{B,\mathrm{cmp}}>0\), frozen \(\tau_{B,\mathrm{cmp}}\in(1/2,1)\), and frozen equivalence threshold \(\tau_{B,\mathrm{eq}}\in(1/2,1)\), the diagnostic gives split evidence precedence:

\[
G_{K,t}^{B}=\begin{cases}
\mathrm{split},&
\min_{e\in K}n_e^{\mathrm{eff}}\ge n_{B,\mathrm{cmp}}
\text{ and }p_K^{\mathrm{split}}\ge\tau_{B,\mathrm{cmp}},\\
\mathrm{share},&
\min_{e\in K}n_e^{\mathrm{eff}}\ge n_{B,\mathrm{cmp}}
\text{ and }p_K^{\mathrm{eq}}\ge\tau_{B,\mathrm{eq}},\\
\mathrm{uncertain},&\text{otherwise.}
\end{cases}
\]

Both threshold conditions can hold because they summarize different posterior
questions; the displayed order then gives split evidence precedence. The
\(\mathrm{uncertain}\) result is an explicit abstention whenever neither ordered
decision fires, not a geometric middle band between complementary probabilities.

For frozen \(w_{B,\max}\in[0,1]\), an optional proposal-only borrowing weight may be

\[
w_{K,t}^{B}=\begin{cases}
0,&G_{K,t}^{B}=\mathrm{split},\\
p_K^{\mathrm{eq}},&G_{K,t}^{B}=\mathrm{share},\\
w_{B,\max}p_K^{\mathrm{eq}},&G_{K,t}^{B}=\mathrm{uncertain}.
\end{cases}
\]

The asymmetry is intentional. A share proposal that crossed the frozen
equivalence threshold may borrow up to the full unit cap, weighted by
\(p_K^{\mathrm{eq}}\); an uncertain proposal is additionally limited by
\(w_{B,\max}\). Neither weight authorizes posterior sharing.

This is partial-pooling advice, not grouping authority. The comparison includes the shared-versus-independent complexity tradeoff and practical-equivalence evidence, but its conclusion remains model-dependent. Formally, \(G_{K,t}^{B}\) and \(w_{K,t}^{B}\) cannot set \(J_{K,t}^{\mathrm{share}}\), publish \(s_K^B\), or mutate \(\kappa_t^B\). A \(\mathrm{share}\) proposal still requires the external target-law certificate above; a \(\mathrm{split}\) proposal forces zero borrowing and may suspend reuse or request review, but final bucket revision remains an independently validated slow-path transition.

### Anti-Pigeon shock revocation

Positive sharing and revocation are asymmetric. Only a valid external Anti-Pigeon certificate may create a shared key, but sufficiently strong later evidence may invalidate that certificate without certifying any replacement merge. To keep a shared posterior from becoming confident faster than its member-level divergence test, freeze a pooled-evidence factor \(\omega_{B,\mathrm{pool}}\in(0,1]\). For an available Bernoulli outcome \(Y_{e,t}\), inclusion weight \(w_{e,t}\), and active shared bucket \(K\), update the pooled posterior by

\[
(\alpha_{K,t},\beta_{K,t})
=(\alpha_{K,t-1},\beta_{K,t-1})
+\omega_{B,\mathrm{pool}}w_{e,t}(Y_{e,t},1-Y_{e,t}),
\]

while retaining full-strength member statistics

\[
(u_{e,t},v_{e,t})
=(u_{e,t-1},v_{e,t-1})
+w_{e,t}(Y_{e,t},1-Y_{e,t}).
\]

The discount controls pooled confidence; it does not weaken the evidence used to discover that the grouping itself is wrong. Event-local posteriors are not discounted by this rule. Unless the fractional contribution follows from a declared coherent generative model, \(\omega_{B,\mathrm{pool}}<1\) defines a tempered working posterior rather than an ordinary posterior under the common-\(\theta\) model.

Let \(J_t^{\mathrm{val}}(e)=1\) only for a full-stream outcome or an independently selected audit outcome whose inclusion semantics are valid for revision. At time \(t\), the revealing outcome is first incorporated into the pooled and full-strength member statistics displayed above; \(p_K^{\mathrm{split}}\), effective support, and \(J_{K,t}^{\mathrm{shock}}(e)\) are then evaluated from those post-outcome statistics. Define the split-shock indicator

\[
J_{K,t}^{\mathrm{shock}}(e)
=J_{K,t}^{\mathrm{share}}J_t^{\mathrm{val}}(e)
\mathbf1\!\left[
\min_{e'\in K}n_{e'}^{\mathrm{eff}}\ge n_{B,\mathrm{cmp}},
\ p_K^{\mathrm{split}}\ge\tau_{B,\mathrm{cmp}}
\right].
\]

This is called a shock because it authorizes a structural response stronger than an ordinary posterior nudge. Combined with the changepoint indicator, the fail-closed revision action is

\[
A_{K,t}^{\mathrm{rev}}=
\begin{cases}
\mathrm{split\_reset},&J_{K,t}^{\mathrm{shock}}=1, J_{K,t}^{\mathrm{cp}}=1,\\
\mathrm{split},&J_{K,t}^{\mathrm{shock}}=1, J_{K,t}^{\mathrm{cp}}=0,\\
\mathrm{shared\_reset},&J_{K,t}^{\mathrm{share}}=1, J_{K,t}^{\mathrm{cp}}=1,\\
\mathrm{individual\_reset},&J_{K,t}^{\mathrm{share}}=0, J_{K,t}^{\mathrm{cp}}=1,\\
\mathrm{retain},&\text{otherwise.}
\end{cases}
\]

A \(\mathrm{split}\) transition atomically revokes the old sharing certificate, marks its shared posterior and dependent residuals inactive, advances the affected posterior, residual, abstraction, graph, and epoch versions through the dependency-closure mechanism, and materializes event-local posteriors from every member's retained sufficient statistics. A \(\mathrm{split\_reset}\) performs the same transition, but for the triggering member only it discards the pre-revealing sufficient statistics, calibration accumulators, and changepoint state, then initializes that event-local posterior and monitor from the declared prior plus the revealing outcome; all other members retain their sufficient statistics. A \(\mathrm{shared\_reset}\) keeps the certified shared key but resets its pooled posterior, calibration accumulators, member-comparison statistics, and changepoint state to the declared prior plus the revealing outcome. An \(\mathrm{individual\_reset}\) performs the corresponding reset on the triggering event-local posterior and monitor. Thus every reset explicitly sacrifices the named pre-change evidence to prevent it from dominating the new regime, whereas plain \(\mathrm{split}\) does not. Revocation is not positive regrouping: no branch above may publish a replacement Anti-Pigeon certificate. Selected-only evidence may update a working or shared posterior but cannot make this structural decision self-certifying.

Let \(\kappa_t^B(e)\) be the frozen posterior-key assignment after the Anti-Pigeon decision: admitted events share a key only when the corresponding sharing certificate passes; otherwise each receives a separate key. For each key \(K\), define the admitted evidence-packet set

\[
\mathcal X_{K,t}^{\mathrm{upd},q_B}
=\left\{\xi_t(e):
J_t^{\mathrm{upd},q_B}(e)=1,
\ \kappa_t^B(e)=K\right\}.
\]

Let \((\Theta_K,\mathscr A_{\Theta_K})\) be a declared parameter space and let \(q_{K,t^-}\in\mathcal P(\Theta_K)\) be the cached prior available before the update. Let \(\xi_t(e)\) be the evidence packet extracted from an available event and its currently available labels. The ordinary Bayesian interpretation requires the single model family \(\{\mathbb P_{K,\theta}\}\) declared in Section 5: \(L_K\) is exactly its dominated evidence marginal and \(\mathsf P_{H,K}\) is exactly its outcome marginal under the displayed context-sufficiency identity. A modular update and forecast that do not share that family remain modular even after favorable forward validation and may not use ordinary posterior-predictive language.

For a non-empty \(\mathcal X_{K,t}^{\mathrm{upd},q_B}\), an ordinary Bayesian update is

\[
q_{K,t}^{+}(d\theta)=
\frac{
L_K^{\mathrm{adm},q_B}(\mathcal X_{K,t}^{\mathrm{upd},q_B}\mid\theta,\mathfrak h_t)
q_{K,t^-}(d\theta)}
{\int_{\Theta_K}
L_K^{\mathrm{adm},q_B}(\mathcal X_{K,t}^{\mathrm{upd},q_B}\mid\vartheta,\mathfrak h_t)
q_{K,t^-}(d\vartheta)},
\]

provided the denominator is finite and strictly positive. Nomination, evidence readiness, novelty, or compatibility may depend on the arrived event, so admission is generally informative under either policy. For one evidence packet \(\xi\), the admission-conditioned likelihood is

\[
L_K^{\mathrm{adm},q_B}(\xi\mid\theta,\mathfrak h_t,J^{\mathrm{upd},q_B}=1)=
\frac{
P_\theta(J^{\mathrm{upd},q_B}=1\mid\xi,\mathfrak h_t)
L_K(\xi\mid\theta,\mathfrak h_t)}
{P_\theta(J^{\mathrm{upd},q_B}=1\mid\mathfrak h_t)},
\]

on the domain where the denominator is positive. Reliable correction requires more than pointwise positivity. Let

\[
p_K^{\mathrm{adm},q_B}(\theta,\mathfrak h)
=P_\theta(J^{\mathrm{upd},q_B}=1\mid\mathfrak h),
\]

let \(\underline p_{K,t}^{\mathrm{adm},q_B}(\mathfrak h)\) be either an analytic lower bound or a simultaneously valid lower confidence bound for \(\inf_{\theta\in\Theta_K}p_K^{\mathrm{adm},q_B}(\theta,\mathfrak h)\), and freeze \(p_{\min}^{\mathrm{adm}}>0\). The certified admission-support region is

\[
\mathfrak H_{K,t}^{\mathrm{adm},q_B}
=\left\{\mathfrak h:
\underline p_{K,t}^{\mathrm{adm},q_B}(\mathfrak h)
\ge p_{\min}^{\mathrm{adm}}\right\}.
\]

An admission-corrected full-stream posterior claim is permitted only on this region. Under \(q_{\mathrm{FA}}\), threshold selection disappears but nomination and evidence readiness remain part of admission and may still require correction. Outside the certified region, including a structurally never-nominated case, the update is labeled a working posterior or is withheld. A non-admitted event inside the declared candidate universe may still enter the independent audit population; an event outside \(\mathfrak E_t^B\) is outside both the production admission certificate and that audit unless a separate exhaustive or envelope argument covers it.

For a jointly admitted evidence set, the contract must model the joint admission probability; multiplying one-event admission corrections is valid only under a declared conditional factorization. Admission may be ignored only under a stated conditional-ignorability result, for example when the complete admission process depends exclusively on already conditioned-on pre-evidence variables. If the admission probability cannot be modeled with the required support bound, the result is called an admission-conditioned working posterior, not a calibrated posterior for the full event stream, and must be tested against the independent audit stream.

Because \(J_t^{\mathrm{upd},q_B}\) contains nomination and evidence readiness under both policies, both the numerator and marginal denominator integrate the complete admission event. Conditioning only on the selective threshold while treating frontier membership as fixed is valid only under a separately stated conditional design.

The effective posterior consumed by Section 5 is

\[
q_{K,t}^{\mathrm{eff}}=
\begin{cases}
q_{K,t}^{+},&
\mathcal X_{K,t}^{\mathrm{upd},q_B}\neq\varnothing
\text{ and the update is valid},\\
q_{K,t^-},&\text{otherwise, provided the cached prior is valid}.
\end{cases}
\]

Buckets without either valid branch are excluded from \(\mathcal K_t^{\mathrm{bel}}\). Section 5 maps the resulting finite posterior family into \(\mathsf Q_t^0\), applies only residuals certified against that base law, and scores the final \(\mathsf Q_t^R\).

### Bayesian elastic rank delta

Probability prediction and retrieval ordering are related but different contracts. Let a bounded external retrieval contract return \(N_t\) candidates in initial order with finite scores \(s_{(1),t}^{\mathrm{ret}},\ldots,s_{(N_t),t}^{\mathrm{ret}}\), and let \(P_t\le N_t\) be the packing-count boundary before token-budget truncation. Define rank-domain answer certainty by

\[
c_t^{\mathrm{pack}}=
\begin{cases}
1,&P_t=N_t,\\
\mathrm{clip}_{[0,1]}\!\left(
\dfrac{s_{(P_t),t}^{\mathrm{ret}}-s_{(P_t+1),t}^{\mathrm{ret}}}
{\max\{|s_{(P_t),t}^{\mathrm{ret}}|,
|s_{(P_t+1),t}^{\mathrm{ret}}|,\varepsilon_s\}}
\right),&P_t<N_t,
\end{cases}
\]

for a fixed \(\varepsilon_s>0\). A small boundary gap means the current top packet is unsettled; a large gap means the boundary is comparatively stable. This number is not the posterior probability that an answer is true or useful.

For candidate \(i\), let \(d_{i,t}^{\mathrm{raw}}\) be the bounded EventFrame correction relative to its frozen local scoring baseline, and let \(r_{i,t}^{\mathrm{corr}}\in[0,1]\) be an independently declared correction-reliability value. A conforming implementation sets \(r_{i,t}^{\mathrm{corr}}=0\) unless an accepted Bayesian posterior, certified residual, or versioned graph-compatibility path actually generated the correction. With frozen \(0\le\lambda_{\min}\le\lambda_{\max}\), define

\[
\lambda_{i,t}^{\mathrm{el}}
=r_{i,t}^{\mathrm{corr}}
\left[\lambda_{\min}
+(\lambda_{\max}-\lambda_{\min})(1-c_t^{\mathrm{pack}})\right],
\]

and apply

\[
\Delta_{i,t}^{\mathrm{rank}}
=\mathrm{clip}_{[-\Delta_{\max},\Delta_{\max}]}
\left(\lambda_{i,t}^{\mathrm{el}}d_{i,t}^{\mathrm{raw}}\right),
\qquad
s_{i,t}^{\mathrm{final}}
=\mathrm{clip}_{[0,1]}
\left(s_{i,t}^{\mathrm{ret}}+\Delta_{i,t}^{\mathrm{rank}}\right).
\]

The same rule handles promotion and demotion. An uncertain boundary permits a larger authorized move; a clear boundary suppresses it. Reliability remains a mandatory gate even when certainty modulation is disabled, in which case \(\lambda_{i,t}^{\mathrm{el}}=r_{i,t}^{\mathrm{corr}}\). Anti-Pigeon shock revocation can invalidate the shared posterior or residual that supplied \(d_{i,t}^{\mathrm{raw}}\); version checks then force the delta to zero or regeneration. Elasticity cannot create a correction and cannot bypass \(\Delta_{\max}\).

This ranking operator runs after the retrieval contract and before packing. It does not alter \(\mathsf Q_t^R\), its proper score, or its calibration. A monotone probability-calibration map is separately fitted on chronological design data and must bind the complete nomination and gating fingerprint. If that fingerprint changes, the map is stale and must fail closed or return to shadow evaluation. Calibrated usefulness was an unsuitable plasticity signal because it coupled a probability claim to a rank-boundary control; \(c_t^{\mathrm{pack}}\) and \(r_{i,t}^{\mathrm{corr}}\) make those roles explicit.

Likewise, a product of conditionally independent likelihoods is ordinary Bayes only when the declared source model justifies that factorization. Tempering correlated-source contributions,

\[
q_{K,t}^{+}(d\theta)\propto
q_{K,t^-}(d\theta)
\prod_{e\in\mathcal X_{K,t}^{\mathrm{upd},q_B}}
L_K(\xi_t(e)\mid\theta,\mathfrak h_t)^{\omega_t(e)},
\qquad 0\le\omega_t(e)\le1,
\]

defines a generalized or power posterior unless it is derived from a joint generative model. Source-independence scoring therefore cannot by itself justify multiplying evidence as if it were independent.

For cheap regime monitoring, a bucket may maintain a bounded approximation to a Bayesian online changepoint run-length posterior [17,18]. Let \(R_{K,t}\in\mathbb N_0\) be run length. The simplest trigger uses only posterior mass at run length zero, but noisy changes can spread mass over several recent run lengths and gradual changes need not produce a sharp reset. A bounded Bernoulli specialization therefore combines the run-length statistic with a two-sided cumulative detector.

Let \(Y_{K,t}\in\{0,1\}\) be the currently available usefulness outcome. During a frozen warm-up of \(n_{\mathrm{warm}}\) outcomes, estimate the reference mean by the ordinary running mean and hold both cumulative statistics at zero. After warm-up, update the slow reference with \(0<\eta_s<1\),

\[
m_{K,t}^{s}=(1-\eta_s)m_{K,t-1}^{s}+\eta_sY_{K,t},
\]

and, using the pre-update reference in the residual, define

\[
\begin{aligned}
C_{K,t}^{+}&=\max\!\left(0,
C_{K,t-1}^{+}+Y_{K,t}-m_{K,t-1}^{s}-\delta_{\mathrm C}\right),\\
C_{K,t}^{-}&=\min\!\left(0,
C_{K,t-1}^{-}+Y_{K,t}-m_{K,t-1}^{s}+\delta_{\mathrm C}\right),
\end{aligned}
\]

where \(\delta_{\mathrm C}>0\) absorbs small fluctuations. With run-length threshold \(\gamma_{\mathrm{cp}}\), cumulative boundary \(h_{\mathrm C}>0\), and cooldown counter \(d_{K,t}^{\mathrm{cool}}\), define

\[
J_{K,t}^{\mathrm{cp}}=
\mathbf1\!\left[
 d_{K,t}^{\mathrm{cool}}=0
\text{ and }
\left(
P(R_{K,t}=0\mid\mathfrak h_t)\ge\gamma_{\mathrm{cp}}
\text{ or }C_{K,t}^{+}\ge h_{\mathrm C}
\text{ or }-C_{K,t}^{-}\ge h_{\mathrm C}
\right)
\right].
\]

When this indicator fires, the runtime resets the affected posterior and monitor onto the triggering outcome, starts a fixed cooldown during which state may update but no new trigger may fire, and applies the dependency-closure bump \(\mathsf B_{\mathcal D}\) and stale-marking operator \(\mathsf I_{\mathcal D}\) from Section 8 to the affected posterior, residual, and graph-version region before expanding the review frontier and routing recalibration to the slow path. The warm-up, cap, thresholds, cooldown, and repeated-trigger scoring rule are frozen before confirmation. A monitor fed only admitted evidence detects changes in the admission-conditioned process. Under frontier-all this still excludes non-nominated and not-yet-ready evidence; under selective admission it also excludes threshold-rejected evidence. The monitor supports a full-stream regime claim only when its transition and observation model includes the complete admission mechanism or when the independent audit stream is incorporated with its sampling design. Exact classical run-length support can grow with the stream; a constant-memory or constant-time claim therefore requires a declared cap, pruning rule, or finite sufficient-statistic approximation and must report its approximation error. The CUSUM state is constant-size; the capped run-length update remains linear in the retained run-length support.

Bounded retrieval and optional selective admission can become self-confirming by never revisiting what they have learned to ignore. EventFrame therefore reserves a predeclared audit probability \(\pi_{\mathrm{audit}}>0\). Conditional on the non-admitted candidate set and independently of activation-score magnitude, draw

\[
J_t^{\mathrm{audit}}(e)\sim\mathrm{Bernoulli}(\pi_{\mathrm{audit}}).
\]

If the accepted audit sample exceeds a fixed capacity \(N_{\mathrm{audit}}^{\max}\), a frozen uniform reservoir subsamples it and records every final inclusion probability. Audit estimators use the corresponding design weights; an unweighted capped convenience sample cannot support the omission certificate.

For one audited non-admitted evidence packet \(e\), let \((q_{K,t}^{\mathrm{loc}})_K\) be the effective posterior family produced by the ordinary frontier policy and let \((q_{K,t}^{\mathrm{exp}}(e))_K\) be the shadow family after admitting that packet through the same admission-aware update. Section 5 maps these to posterior-predictive bases \((\mathsf Q_t^{0,\mathrm{loc}},b_t^{0,\mathrm{loc}})\) and \((\mathsf Q_t^{0,\mathrm{exp}}(e),b_t^{0,\mathrm{exp}}(e))\). Replay the complete residual policy in each state:

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
(q_B,J_t^{\mathrm{nom}},J_t^{\mathrm{evid}},A_t^B,\tau_t^B,
J_t^{\mathrm{act}},J_t^{\mathrm{upd},q_B},J_{K,t}^{\mathrm{share}},J_t^{\mathrm{audit}},
v_t,\upsilon_t^{\mathrm{bel}},H,s_t^{\mathrm{prov}}),
\]

together with audit inclusion probability, so calibration can be reconstructed under as-of replay.

Before an ordinary posterior update publishes in place, its posterior-predictive law and template are compared with the fixed references for \(\upsilon_t^{\mathrm{bel}}\) using the analytic or simultaneous bounds declared in Section 5. Those bounds include propagated posterior-approximation error. The update retains that version only while every affected law-bearing residual has non-negative law margin and every point-bearing residual has non-negative template margin. Otherwise \(\mathsf B_{\mathcal D}\) bumps the dependency closure and \(\mathsf I_{\mathcal D}\) invalidates affected residuals. Posterior, posterior key, dependent residual certificate, graph version, and epoch then publish atomically. Prediction readers observe one complete old or new version, never a mixed state. Posterior storage has a declared capacity and deterministic eviction rule. Eviction removes fast-path reuse eligibility but preserves immutable provenance required by later audits.

Streaming variational Bayes motivates incremental and asynchronous posterior approximation [14]. Streaming variational Monte Carlo and online variational sequential Monte Carlo provide richer state-space and particle-based alternatives [15,16], but their constant-per-sample or online properties do not make their particle count, parameter dimension, optimization, or hardware cost free. Pattern Markov Chains are relevant only for declared event-pattern completion forecasts, not as a universal next-event Bayesian model [19]. Work on out-of-distribution sequential event prediction motivates latent-context and shift-aware evaluation [20], but EventFrame does not inherit its causal interpretation without the corresponding identification assumptions.

The memory model supports the overall EventFrame loop. Episodic memory helps interpret and compare cases. Residual memory corrects recurring transition errors. The bounded Bayesian frontier updates cached beliefs under a frontier-all reference policy or an explicitly evaluated selective policy, while Anti-Pigeon decides which evidence may share one posterior. Slow-path consolidation, changepoint review, and independent audits keep all three memories from turning into overconfident filtered history. The next section uses perturbation rather than recall to discover which event properties are stable under prediction.
