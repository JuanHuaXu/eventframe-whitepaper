# 7. Lumpability and Abstraction

Abstraction is useful only when it preserves the transition behavior required by the declared target. Let:

\[
\pi:\mathcal E\rightarrow\mathcal S_{\mathrm{abs}}
\]

map detailed events to abstract states, and extend it componentwise to contexts as \(\pi^k(C_t)\).

Let \(\mathfrak C_{\mathrm{adm}}\subseteq\mathcal E^k\) be the declared admissible context domain from Section 3. The target \(Y\), target law \(P_\star\), divergence, and admissible context domain are fixed by the evaluation contract before \(\pi\) is selected. An aggregate conditional law is not by itself a lumpability test because it averages over hidden detailed states inside a bucket. Instead, define the external predictive lumpability defect:

\[
\varepsilon_{\mathrm{lump}}^\star(\pi)=
\sup_{C,C'\in\mathfrak C_{\mathrm{adm}}:\,h_\pi(C)=h_\pi(C')}
D\!\left(
P_\star(Y\mid C),
P_\star(Y\mid C')
\right).
\]

The abstraction is \(\epsilon_L\)-predictively lumpable for the target when:

\[
\varepsilon_{\mathrm{lump}}^\star(\pi)\le\epsilon_L.
\]

This pairwise condition prevents an aggregate conditional distribution from hiding incompatible microstate transitions. It adapts classical and near-lumpability to finite-context prediction rather than claiming a new Markov-chain theorem [3,4]. In finite data, the supremum is estimated with confidence bounds over observed or generated context pairs; passing the estimate is evidence, not proof about unseen contexts.

Operationally:

1. Freeze the target, target law, divergence \(D\), tolerance \(\epsilon_L\), and evaluation protocol; then choose \(\pi\).
2. Form detailed context pairs that map to the same operational key \(h_\pi\).
3. Compare their fixed-target future distributions.
4. Report the maximum estimated divergence with uncertainty and minimum bucket support.
5. Accept the abstraction only when held-out predictive degradation and the upper confidence bound remain below threshold.

Confluence applies the same requirement to merged event streams. Divergence rejects a merge when a small valid perturbation produces target-distinct future distributions. These statements concern predictive equivalence unless a separate causal model supports intervention claims.

Every non-empty bucket \(K\subseteq\mathcal E\) retains at least one concrete frame \(\bar e_K\in K\) for traceability, but one frame is not sufficient to characterize a heterogeneous bucket. Let \(\mathrm{anc}(C)=e_t\) denote the terminal or anchor frame of context \(C=e_{t-k+1:t}\), and define the context family represented by \(K\):

\[
\mathfrak C_K=\{C\in\mathfrak C_{\mathrm{adm}}:\mathrm{anc}(C)\in K\}.
\]

When \(\mathfrak C_K\neq\varnothing\), call \(K\) active and maintain a non-empty context audit set \(\mathcal R_C(K)\subseteq\mathfrak C_K\). If no context has yet been assigned to the bucket, retain \(\bar e_K\) for traceability but mark the bucket inactive and unaudited; no future-diameter or admissibility claim is made for it. With a declared context metric \(d_C\), a representational coverage rule for an auditable bucket may be:

\[
\sup_{C\in\mathfrak C_K}\min_{R\in\mathcal R_C(K)}d_C(C,R)\le\delta_K.
\]

The set should include contexts for a medoid or high-confidence anchor, boundary examples, high-uncertainty examples, and a reservoir sample when the bucket is large. Its associated anchor frames preserve concrete traceability. If compression prevents this coverage estimate, the system cannot claim that the bucket has been audited.

Anti-Pigeon is the split-side guard against invalid abstraction and stale predictive habit. The name denotes anti-pigeonholing: events may share a bucket only while their target futures remain sufficiently similar.

For each bucket \(K\) and contexts \(C,C'\in\mathfrak C_K\), define the external target-law disagreement:

\[
D_{C,C'}^{K,\star}=
D\!\left(
P_\star(Y\mid C),
P_\star(Y\mid C')
\right),
\]

and the theoretical future-diameter:

\[
D_K^\star(\pi)=\sup_{C,C'\in\mathfrak C_K}D_{C,C'}^{K,\star}.
\]

The bucket is admissible only when:

\[
D_K^\star(\pi)\le\epsilon_{AP}.
\]

Separately define the model-forecast diameter

\[
D_K^{\mathrm{mdl}}(\Theta_\Gamma)=
\sup_{C,C'\in\mathfrak C_K}
D\!\left(
\mathsf Q_{\Theta_\Gamma}^{Y}(\cdot\mid C;S_{t^-}),
\mathsf Q_{\Theta_\Gamma}^{Y}(\cdot\mid C';S_{t^-})
\right).
\]

This model diameter detects internal inconsistency and drift, but it cannot certify the abstraction: a predictor that emits the same wrong law everywhere has zero model diameter while the external future-diameter may be large.

Define the true restricted audit diameter and its estimator by:

\[
D_K^{\mathrm{audit},\star}=
\max_{R,R'\in\mathcal R_C(K)}D_{R,R'}^{K,\star},
\qquad
\widehat D_K^\star=
\max_{R,R'\in\mathcal R_C(K)}\widehat D_{R,R'}^{K,\star}
\]

where \(\widehat D_{R,R'}^{K,\star}\) estimates target-law disagreement from observed outcomes without using the candidate forecast as ground truth. The audit reports \(\widehat D_K^\star\), coverage, and statistical uncertainty. The deterministic relation is \(D_K^{\mathrm{audit},\star}\le D_K^\star\); no sample-wise ordering between \(\widehat D_K^\star\) and \(D_K^\star\) is asserted. A statistically significant large pairwise divergence is evidence to split or mark the bucket. Representational coverage alone does not make a small estimate a certificate of unseen future behavior.

To obtain a certified upper bound from a non-exhaustive audit, require that \(D\) obey the triangle inequality and verify a continuity bound for the forecast map on \(\mathfrak C_K\). Let \(\overline L_K^{\mathrm{cert}}\) be either a deterministic uniform bound established analytically or a simultaneous upper confidence bound produced by a predeclared procedure. It must satisfy, at the certificate's stated confidence level:

\[
D\!\left(P_\star(Y\mid C),P_\star(Y\mid R)\right)
\le\overline L_K^{\mathrm{cert}}d_C(C,R)
\qquad\text{for all }C,R\in\mathfrak C_K,
\]

then the coverage rule implies:

\[
D_K^\star(\pi)\le D_K^{\mathrm{audit},\star}+2\overline L_K^{\mathrm{cert}}\delta_K.
\]

With statistical estimation, a simultaneous upper confidence certificate is:

\[
D_K^{\mathrm{cert},\star}=
\max_{R,R'\in\mathcal R_C(K)}
\mathrm{UCB}_{\mathrm{sim}}[D_{R,R'}^{K,\star}]
+2\overline L_K^{\mathrm{cert}}\delta_K.
\]

The confidence procedure must jointly cover all adaptively selected audit pairs used by the maximum and any data-estimated continuity bound. A plug-in estimate of \(\overline L_K\) without uncertainty coverage is not a certificate. If the audit is exhaustive, the coverage term vanishes. If neither exhaustive coverage nor a verified continuity bound is available, the audit supports only an observed-sample claim and cannot certify \(D_K^\star\le\epsilon_{AP}\).

Observed operating regimes use a distinct symbol \(\zeta_t\in\mathcal Z_{\mathrm{reg}}\). On the common-support domain \(\mathfrak C_{a,b}=\mathrm{supp}(C\mid\zeta_a)\cap\mathrm{supp}(C\mid\zeta_b)\), regime-conditioned predictive divergence is:

\[
D_{i,a,b}^{\mathrm{reg}}=
D\!\left(
P_\star(Y\mid C_i,\zeta_a),
P_\star(Y\mid C_i,\zeta_b)
\right).
\]

This quantity is evaluated only for \(C_i\in\mathfrak C_{a,b}\). Outside common support it requires a declared overlap and transport model; otherwise it is unidentified and no comparison is reported. The evaluation contract freezes a held-out review window \(W_{\mathrm{reg}}\), the minimum number \(m_{\mathrm{reg}}\) of multiplicity-adjusted exceedances of \(\epsilon_{AP}^{\mathrm{reg}}\), and the resulting action before candidate inspection. Meeting that rule is evidence that a shared predictive bucket is stale; the predeclared action may split by regime, condition the cache key on \(\zeta\), decay the residual, or mark the abstraction as divergence-sensitive. Post hoc changes to the window, repetition count, threshold, or action invalidate the claim. This adaptation problem is related to concept-drift detection and response [12]. The conditional difference supports predictive adaptation; it is not evidence that \(\zeta\) is causal unless intervention or identification assumptions establish that fact.

A split operator returns \(\{K_1,\ldots,K_m\}\) such that every non-empty active child has sufficient effective support and either exhaustive verification or \(D_{K_j}^{\mathrm{cert},\star}\le\epsilon_{AP}\). Singleton buckets always satisfy an empirical pairwise bound, so representation cost, minimum support, untouched confirmation performance, and coverage of future contexts are required to prevent trivial memorization.

Merge and split thresholds should use hysteresis, for example \(\epsilon_{\mathrm{merge}}<\epsilon_{AP}\), and changes should be accepted only after a minimum held-out improvement. Abstraction quality reports memory and latency gains alongside predictive degradation, subgroup errors, audit coverage, and split/merge churn.

EventFrame can extend this bucket-local test to a network of heterogeneous abstractions. Let:

\[
\mathcal G_t^A=(V_t^A,E_t^A)
\]

be an abstraction compatibility graph. A node may represent an event group, temporal resolution, sensor, local predictor, or agent. Node \(i\) produces a predictive law:

\[
\mathsf Q_i(\cdot\mid C_t)\in\mathcal P(\mathcal Y_i).
\]

For an edge \(e=\{i,j\}\), choose a common measurable comparison space \(\mathcal Y_e\) and measurable maps \(g_{ie}:\mathcal Y_i\to\mathcal Y_e\) and \(g_{je}:\mathcal Y_j\to\mathcal Y_e\). Their pushforward restrictions are:

\[
\mathsf r_{ie}\mathsf Q_i=(g_{ie})_*\mathsf Q_i,
\qquad
\mathsf r_{je}\mathsf Q_j=(g_{je})_*\mathsf Q_j.
\]

Given a declared divergence \(D_e\), the edge compatibility defect is:

\[
\delta_e(\mathsf Q)=
D_e\!\left(\mathsf r_{ie}\mathsf Q_i,\mathsf r_{je}\mathsf Q_j\right),
\qquad
\Delta_{\mathrm{comp}}(\mathsf Q)=
\begin{cases}
0, & E_t^A=\varnothing,\\
\max_{e\in E_t^A}\mathrm{UCB}_{\mathrm{sim}}[\delta_e(\mathsf Q)],
& E_t^A\neq\varnothing.
\end{cases}
\]

Here the simultaneous confidence procedure must cover the family of inspected or adaptively selected edges. A zero defect on every edge defines a compatible assignment for the declared comparison maps. A small defect is only approximate predictive compatibility. It is not causal compatibility unless the node laws are interventional or counterfactual distributions from explicit SCMs and the maps preserve their declared causal semantics.

The closest mathematical prior work for this extension is D'Acunto, Di Lorenzo, and Barbarossa's *Networks of Causal Abstractions: A Sheaf-theoretic Framework* [13]. Their causal abstraction network coordinates heterogeneous causal models using network sheaves and cosheaves, restriction maps, a connection Laplacian, global sections, and mixture causal models. EventFrame adapts the local-to-global compatibility pattern to event-centered predictive laws, then combines it with within-bucket Anti-Pigeon tests, residual-cache certification, and priority-aware staged execution. It does not inherit their causal semantics, consistency results, convergence results, or mixture-learning guarantees.

Accordingly, the EventFrame construction is described only as a sheaf-inspired compatibility scaffold. It should be called a sheaf only after its assigned spaces and restriction maps satisfy the required identity and composition laws. EventFrame does not assume those laws merely because local forecasts are connected by a graph.

EventFrame calls a validated local revision of this scaffold a **predictive sheaf snap**. This is paper-specific terminology, not a standard sheaf-theoretic operation. Write the published compatibility structure at version \(v\) as:

\[
\Xi_A^{(v)}=
\left(
\mathcal G^{A,(v)},
\{\mathcal Y_i\}_{i\in V^{A,(v)}},
\{\mathcal Y_e,D_e,w_e,\{g_{ie}:i\in e\}\}_{e\in E^{A,(v)}}
\right).
\]

For an affected neighborhood \(\mathcal N\), let \(D_t^{\mathrm{design}}\) and \(D_t^{\mathrm{conf}}\) be disjoint chronological design and confirmation blocks satisfying the paper's embargo and as-of rules. Let \(\mathfrak S_t(\Xi_A^{(v)};\mathcal N)\) be a finite, predeclared family of candidate structures constructed only from information available by the slow-path review time, with the unchanged structure \(\Xi_A^{(v)}\) included as the no-snap candidate. An edit may split, merge, or duplicate predictive nodes; add or remove predictive-compatibility edges; or select a comparison map from a prevalidated candidate class. The family has bounded neighborhood radius, candidate count, and map complexity. It may not relabel a predictive edge as causal. The notation \(\Theta_\Gamma[\Xi']\) means the complete candidate design induced by \(\Xi'\), including any required local revision \(\pi'\) of the operational abstraction map, refitted node laws, keys, and certificates. Those dependent components are fitted only on \(D_t^{\mathrm{design}}\); a graph edit is never scored while retaining keys or forecasts that are inconsistent with it.

Fix a task-defined comparison-obligation set \(\mathfrak O_t\) before candidate inspection. Each obligation names local predictions that must remain comparable. A candidate discharges an obligation through a valid direct edge or a composition-valid comparison path; otherwise it must retain the obligation explicitly as unresolved. Let \(U_{\mathrm{obl}}(\Xi';\mathfrak O_t)\ge0\) be the predeclared weighted unresolved burden. This prevents a candidate from obtaining zero defect merely by deleting difficult edges; in particular, an empty graph is not automatically a successful snap when \(\mathfrak O_t\neq\varnothing\).

Let \(\mathcal D_{\Delta,t}(\Xi')\) be the reverse dependency closure of the proposed edit, including every bucket, node law, comparison map, key, certificate, cache entry, or edge whose value or validity can change, not only objects edited syntactically. Let \(\mathfrak K_{\Delta,t}(\Xi')\) and \(E_{\Delta,t}^{\mathrm{keep}}(\Xi')\) be its affected active-bucket and retained-or-new-edge projections.

On a chronological design block \(D_t^{\mathrm{design}}\), score a candidate by:

\[
\begin{aligned}
\Psi_t(\Xi';\Xi_A^{(v)})={}&
\widehat{\mathcal R}_{\mathrm{pri}}^{D_t^{\mathrm{design}}}(\Theta_\Gamma[\Xi'])
+\lambda_{\mathrm{comp}}\widehat\Delta_{\mathrm{comp}}^{D_t^{\mathrm{design}}}
(\Theta_\Gamma[\Xi'];\Xi')\\
&+\lambda_{\mathrm{edit}}d_{\mathrm{edit}}(\Xi',\Xi_A^{(v)})
+\lambda_{\mathrm{snap}}\mathcal C_{\mathrm{snap}}(\Xi')
+\lambda_{\mathrm{obl}}U_{\mathrm{obl}}(\Xi';\mathfrak O_t),
\end{aligned}
\]

where the hatted quantities are design-block estimates computed under the predeclared candidate-selection procedure. The compatibility estimate uses the candidate-induced laws and the maps in \(\Xi'\). Every term is finite and normalized to a declared common utility scale, or its coefficient carries the conversion needed to produce that scale. All coefficients are non-negative: \(\lambda_{\mathrm{comp}}\) weights compatibility defect, \(\lambda_{\mathrm{edit}}\) weights structural churn, and \(\lambda_{\mathrm{snap}}\) weights measured or hardware-indexed revision cost. The unresolved-obligation coefficient \(\lambda_{\mathrm{obl}}\) is strictly positive unless the candidate family itself requires \(U_{\mathrm{obl}}=0\). Because the candidate family is finite and non-empty, a deterministic tie-breaking rule selects:

\[
\Xi_A^{\mathrm{cand}}
\in\arg\min_{\Xi'\in\mathfrak S_t(\Xi_A^{(v)};\mathcal N)}
\Psi_t(\Xi';\Xi_A^{(v)}).
\]

Candidate generation and selection do not authorize publication. On \(D_t^{\mathrm{conf}}\), define the proper-risk change:

\[
\Delta\mathcal R_{\mathrm{prop},t}^{\mathrm{snap}}=
\widehat{\mathcal R}_{\mathrm{prop}}^{D_t^{\mathrm{conf}}}(\Theta_\Gamma[\Xi_A^{\mathrm{cand}}])
-\widehat{\mathcal R}_{\mathrm{prop}}^{D_t^{\mathrm{conf}}}(\Theta_\Gamma[\Xi_A^{(v)}]).
\]

Let \(G_{v\rightarrow\mathrm{cand},t}^{\mathrm{pri}}\) be the paired priority-weighted gain defined as in Section 9, and let \(C_{v\rightarrow\mathrm{cand},t}(h)\) be its resource cost on the same declared utility scale. Declare \(\delta_{\mathrm{snap}}>0\), \(\epsilon_{\mathrm{obl}}\ge0\), and \(0\le\epsilon_{\mathrm{acc}}^{\mathrm{comp}}\le\epsilon_{\mathrm{split}}^{\mathrm{comp}}\) before candidate inspection. With \(\max\varnothing=0\), the joint snap-acceptance indicator is:

\[
\begin{aligned}
A_t^{\mathrm{snap}}=1\quad\Longleftrightarrow\quad&
\mathrm{LCB}\!\left[G_{v\rightarrow\mathrm{cand},t}^{\mathrm{pri}}\right]
-\mathrm{UCB}\!\left[C_{v\rightarrow\mathrm{cand},t}(h)\right]
{}>\delta_{\mathrm{snap}},\\
&\mathrm{UCB}\!\left[\Delta\mathcal R_{\mathrm{prop},t}^{\mathrm{snap}}\right]
\le\epsilon_{\mathrm{prop}},\\
&\max_{K\in\mathfrak K_{\Delta,t}(\Xi_A^{\mathrm{cand}})}
D_K^{\mathrm{cert},\star}\le\epsilon_{AP},\\
&\max_{e\in E_{\Delta,t}^{\mathrm{keep}}(\Xi_A^{\mathrm{cand}})}
\mathrm{UCB}_{\mathrm{sim}}[\delta_e]\le\epsilon_{\mathrm{acc}}^{\mathrm{comp}},\\
&U_{\mathrm{obl}}(\Xi_A^{\mathrm{cand}};\mathfrak O_t)
\le\epsilon_{\mathrm{obl}}.
\end{aligned}
\]

Set \(A_t^{\mathrm{snap}}=0\) otherwise. Every outcome-dependent quantity in the indicator is computed exclusively from as-of predictions on \(D_t^{\mathrm{conf}}\); no confirmation outcome may refit the candidate. The predeclared joint confidence procedure covers every displayed stochastic gate after candidate selection. Repeated reviews use fresh blocks or a sequentially valid procedure. On acceptance, relabel the confirmed candidate as version \(v+1\) and write \(\mathcal D_{\Delta,t}=\mathcal D_{\Delta,t}(\Xi_A^{\mathrm{cand}})\). Let \(\mathbf v^{(v)}\) be the local epoch map, let \(\mathcal C_{\mathrm{mem}}^{(v)}=(\mathcal C_A^{(v)},\mathcal C_R^{(v)},\mathcal C_E^{(v)})\), let \(\mathsf B_{\mathcal D}\) monotonically increment epochs in dependency closure \(\mathcal D\), and let \(\mathsf I_{\mathcal D}\) mark every dependent memory entry stale. The publish-or-retain transition is:

\[
\left(\Xi_A^{\mathrm{new}},\pi^{\mathrm{new}},
\mathbf v^{\mathrm{new}},\mathcal C_{\mathrm{mem}}^{\mathrm{new}}\right)=
\begin{cases}
\left(\Xi_A^{(v+1)},\pi',
\mathsf B_{\mathcal D_{\Delta,t}}(\mathbf v^{(v)}),
\mathsf I_{\mathcal D_{\Delta,t}}(\mathcal C_{\mathrm{mem}}^{(v)})\right),
& A_t^{\mathrm{snap}}=1,\\
\left(\Xi_A^{(v)},\pi,\mathbf v^{(v)},\mathcal C_{\mathrm{mem}}^{(v)}\right),
& A_t^{\mathrm{snap}}=0.
\end{cases}
\]

The accepted tuple publishes atomically, and the previous complete version remains available for rollback. The invalidation operator preserves unaffected entries and marks affected ones unusable until recertified; it does not silently assign them certificates under the new version. When \(A_t^{\mathrm{snap}}=0\), no candidate component is published. This operation revises predictive organization only. It may nominate a causal hypothesis, but changing an SCM edge additionally requires the paper's intervention and identification conditions; compatibility improvement alone is insufficient.

When an explicit SCM exists, an accepted predictive snap may nominate a separate finite family of local SCM edits, such as adding or removing an edge, reversing a direction not fixed by temporal order, or introducing a measured mediator or regime variable. Every causal candidate must specify the resulting structural equations, obey declared temporal and domain constraints, and identify the intervention law under which it will be tested. Candidate generation may use predictive defect, but causal selection and confirmation require independent randomized or otherwise identified intervention evidence with correction for the inspected edit family. Observational fit, lower compatibility defect, or successful predictive gluing cannot by themselves orient or promote a causal edge. Until those tests pass, the published causal graph remains unchanged.

The network defect complements rather than replaces Anti-Pigeon. \(D_K^\star\) tests hidden external future disagreement inside a bucket; \(\delta_e\) tests disagreement between representations after both are mapped into a common comparison space. A proposed merge is accepted only when both its external bucket future-diameter and affected edge-defect upper bounds are below their merge thresholds. A bucket or edge is split, invalidated, or routed to deeper review when a lower confidence bound exceeds its split threshold. Separate thresholds \(\epsilon_{\mathrm{merge}}^{\mathrm{comp}}<\epsilon_{\mathrm{split}}^{\mathrm{comp}}\) provide hysteresis.

When simple rejection would discard useful local information, a local reconciliation stage may solve:

\[
(\overline{\mathsf Q}_i)_{i\in\mathcal N}
\in\arg\min_{(\widetilde{\mathsf Q}_i)_{i\in\mathcal N}\in\mathfrak Q_{\mathcal N}}
\left[
\sum_{i\in\mathcal N}a_iD_i(\widetilde{\mathsf Q}_i,\mathsf Q_i)
+\lambda_A\sum_{e\in E^{+}(\mathcal N)}w_e\delta_e(\widetilde{\mathsf Q})
\right],
\]

where \(\mathcal N\subseteq V_t^A\) is an affected neighborhood, \(\mathfrak Q_{\mathcal N}\subseteq\prod_{i\in\mathcal N}\mathcal P(\mathcal Y_i)\) is the declared feasible forecast-tuple family, and \(E^{+}(\mathcal N)=\{e\in E_t^A:e\cap\mathcal N\neq\varnothing\}\) includes both internal and boundary edges. Forecasts outside \(\mathcal N\) remain fixed and \(a_i,w_e\ge0\). Each \(D_i:\mathcal P(\mathcal Y_i)\times\mathcal P(\mathcal Y_i)\to[0,+\infty]\) is a declared fidelity divergence with \(D_i(Q,Q)=0\); every divergence and tie-breaking rule is frozen by the evaluation contract. The first term preserves each local forecast; the second penalizes incompatibility without hiding damage at the neighborhood boundary. A minimizer is asserted only when \(\mathfrak Q_{\mathcal N}\) is compact and the objective is lower semicontinuous, or under another stated existence theorem; otherwise the algorithm must return a declared approximate tuple with an optimality gap. Reconciliation is not unqualified averaging, and the unreconciled forecasts and defects remain available for audit.

For a fixed graph with finite-dimensional embeddings \(x_i=\phi_i(\mathsf Q_i)\) and linear restrictions \(R_{ie}\), define the boundary operator on edge \(e=\{i,j\}\) by:

\[
(\partial_Ax)_e=R_{ie}x_i-R_{je}x_j,
\qquad
L_A=\partial_A^{*}\partial_A.
\]

Then \(\|\partial_Ax\|^2=\langle x,L_Ax\rangle\) and \(\ker L_A=\ker\partial_A\), the linearly compatible assignments. If \(\lambda_{\max}(L_A)>0\), the fixed-step refinement

\[
x^{(n+1)}=x^{(n)}-\eta L_Ax^{(n)},
\qquad
0<\eta<\frac{2}{\lambda_{\max}(L_A)},
\]

converges in finite dimensions to the orthogonal projection of \(x^{(0)}\) onto \(\ker L_A\). If \(L_A=0\), the assignment is already linearly compatible and no update is required. These statements require a fixed graph, fixed linear restrictions, and the stated inner products. Nonlinear distribution-valued forecasts do not inherit this spectral guarantee automatically.

Finally, a node may represent a predictive regime mixture:

\[
\mathsf Q_i(\cdot\mid C_t)
=\sum_{s=1}^{S_i}\lambda_{is}(C_t)\mathsf Q_{is}(\cdot\mid C_t),
\qquad
\lambda_{is}\ge0,
\quad
\sum_{s=1}^{S_i}\lambda_{is}=1.
\]

This mixture can preserve multiple currently plausible mechanisms instead of collapsing them into one habitual prediction. It remains a predictive mixture unless each component has an explicit SCM and the data and assumptions identify causal interpretation. Mixture learning is the final, most expensive refinement stage; it may revise node laws or comparison maps and then rerun compatibility and reconciliation.
