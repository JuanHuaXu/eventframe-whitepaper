# Notation

This register is normative for the paper. A symbol has one meaning unless an explicit subscript creates a typed variant.

## Symbol Table

| Symbol | Type | Meaning |
|---|---|---|
| \(\Omega\) | set | substrate state space |
| \(A_t\) | finite index region | substrate/computational region available at event index \(t\) |
| \(\omega_{A_t}\) | \(\Omega^{A_t}\) | substrate history over \(A_t\) |
| \(\Delta_\tau\) | positive real | temporal resolution |
| \(\Gamma_{\Delta_\tau}\) | \(\Omega^{A_t}\to\mathcal E_{\Delta_\tau}\) | task-relative coarse-graining |
| \(e_t\) | \(\mathcal E_{\Delta_\tau}\) | event frame |
| \(C_t\) | \(\mathcal E^k\) | length-\(k\) event context |
| \(\mathfrak C_{\mathrm{adm}}\) | subset of \(\mathcal E^k\) | declared context domain for conditional laws and suprema |
| \(H\) | positive real | prediction horizon |
| \((\mathcal N,\mathscr A_{\mathcal N})\) | measurable space | event-mark space |
| \((\mathcal Z_H,\mathscr A_H)\) | measurable tagged union | complete marked-time/no-event outcome space |
| \(\nu(e)\) | event-mark set | event identity/type extractor |
| \(\tau(e)\) | real | declared scalar temporal anchor; timestamp for point events and interval onset by default |
| \(Z_{t+1}\) | \(\mathcal Z_H\) | observed marked time or no-event outcome |
| \(\mathcal Z_H^+\) | subset of \(\mathcal Z_H\) | marked-time branch \(\mathcal Z_H\setminus\{\varnothing\}\) |
| \(\mathcal E_\varnothing\) | tagged union | structured event space extended by the no-event symbol |
| \(d_H\) | \(\mathcal P(\mathcal Z_H)\to\mathcal Z_H\) | fixed point-decision rule with declared loss and tie-break |
| \(\hat e_\theta^H(C)\) | \(\mathcal E_\varnothing\) | structured point summary coherent with \(d_H(\mathsf Q_\theta)\) |
| \(\mathrm{lift}_H\) | \(\mathcal E\times\mathcal Z_H^+\to\mathcal E\) | aligns a structured event template with a selected marked outcome |
| \(a(x)\) | time | availability time of datum or state object \(x\) |
| \(\mathscr F_t^{\mathrm{pred}},S_{t^-}\) | information, state | information and mutable state available immediately before prediction |
| \(\mathfrak H_t,\mathfrak h_t,c_k,\mathrm{Replay}_\Theta\) | space, history, extractor, map | observable-history space and one prediction history, context extraction, and candidate-specific as-of state replay |
| \(P_{\mathrm{obj}},P_{\mathrm{conf}}\) | probability laws | design- and confirmation-generating laws |
| \(\mathcal S_{\mathrm{obj}},\mathcal S_{\mathrm{conf}}\) | finite samples or trajectory blocks | realized design and untouched confirmation data |
| \(P_\star(Y\mid C)\) | conditional law | externally fixed target conditional law |
| \(\mathsf Q_\theta\) | probability kernel | predictive distribution over \(\mathcal Z_H\) |
| \(\mathcal O_\theta(C)\) | \(\mathcal P(\mathcal Z_H)\times\mathcal E_\varnothing\) | typed forecast-law and coherent no-event-capable point-summary bundle |
| \(\mathcal L_{\mathrm{pred}}\) | extended real | untransformed proper post-observation predictive loss |
| \(\overline{\mathcal L}_{\mathrm{pred}}\) | \([0,1]\) | preregistered bounded transformation used inside system action |
| \(\mathcal L_{\mathrm{event}}^H\) | \([0,1]\) | bounded event-aware timing diagnostic |
| \(\mathcal R_{\mathrm{pre}}\) | \([0,1]\) | pre-observation admissibility risk |
| \(\mathcal A_{\mathrm{post}}\) | \([0,1]\) | post-observation realized event action |
| \(\mathsf Q_B\) | \(\mathcal E^k\to\mathcal P(\mathcal Z_H)\) | baseline probability-law predictor |
| \(B\) | \(\mathcal E^k\to\mathcal E\) | baseline conditional event-template predictor |
| \(\mathcal K_t^{\mathrm{bel}}\) | finite set | valid local belief buckets available at prediction time |
| \(\mathsf P_{H,K},\lambda_{K,t}^{\mathrm{bel}}\) | probability kernel, weight | bucket posterior-predictive kernel and frozen context-dependent mixture weight |
| \(\mathbb P_{K,\theta}\) | joint model family | coherent bucket model whose evidence marginal and next-outcome conditional induce the ordinary likelihood and predictive kernel |
| \((\mathcal X_K,\mathscr A_{\mathcal X_K}),\nu_K,\mathbb P_{K,\theta}^{\Xi},\mathbb P_{K,\theta}^{Z}\) | measurable space, measure, marginals | bucket evidence space, dominating measure, and joint-model evidence and outcome marginals |
| \(\mathsf Q_t^0,b_t^0\) | probability law, event template | belief-conditioned posterior-predictive base law and its aligned template before residual correction |
| \(B_H^{\mathrm{bel}}\) | measurable map | converts the effective posterior family and context into the base event template |
| \(\mathscr H\) | finite-dimensional Hilbert space | carrier for operator representation |
| \(\mathbb H_d^E,\mathbb H_d^Q\) | tagged vector spaces | point-template and forecast-law copies of the self-adjoint operators on \(\mathscr H\) |
| \(\mathcal Q_{E,\mathrm{adm}}\) | closed subset of \(\mathbb H_d^E\) | admissible event representations |
| \(q_E,d_E\) | encoder, decoder | event representation maps |
| \(\Pi_E\) | deterministic projection selection | projection to \(\mathcal Q_{E,\mathrm{adm}}\) |
| \(\delta_E,\delta_Q\) | positive reals | point- and law-residual clipping radii |
| \(\oplus_E\) | \(\mathcal E\times\mathbb H_d^E\to\mathcal E\) | event residual composition |
| \(\mathcal C_{R,t^-}\) | finite cache | as-of general residual cache |
| \(\mathcal C_{A,t^-}\) | partial map | as-of exact action-key residual cache |
| \(J_t^R,J_t^A\) | \(\{0,1\}\) | general- and exact-cache acceptance indicators |
| \(\mathcal M_R,\mathcal V_R,\mathbf r\) | mode set, product space, record | typed presence mode and paired point/law residual payload |
| \(\mathbf r_t^{\mathrm{use}}\) | \(\mathcal V_R\) | exact-to-general selected residual record |
| \(r_{t,H}^{E,\mathrm{obs}}\) | \(\mathbb H_d^E\) or undefined | observed point residual only for an event inside the originating horizon |
| \(\rho_H^Q,r_{t,H}^{Q,\mathrm{obs}}\) | estimator, \(\mathbb H_d^Q\) | horizon-specific law-residual estimator and residual defined on both outcome branches |
| \(\mathfrak K_H^Q\) | kernel-valued map | law-residual-induced Markov kernel on \((\mathcal Z_H,\mathscr A_H)\) |
| \(H_i,H_{k_t}\) | positive reals | horizons recorded by general and exact residual-cache entries |
| \(s_i,s_{k_t}\) | \(\mathcal S_{\mathrm{prov}}\) | provenance records for general and exact residual-cache entries |
| \(D_{\mathrm{res}},\mathsf Q_i^{0,\mathrm{ref}},\epsilon_i^{\mathrm{bel}},\overline D_{i,t}^{\mathrm{bel}}\) | distance, law, reals | frozen residual-reference distance, fixed base-law reference, allowed motion, and certified upper motion bound |
| \(D_{\mathrm{tmpl}},b_i^{0,\mathrm{ref}},\epsilon_i^{\mathrm{tmpl}},\overline D_{i,t}^{\mathrm{tmpl}}\) | distance, template, reals | frozen template distance, fixed template reference, allowed motion, and certified upper motion bound |
| \(\upsilon_i^{\mathrm{bel}},\mu_i^{\mathrm{bel}},\mu_i^{\mathrm{tmpl}}\) | version, reals | posterior-predictive certificate version and law/template residual-survival margins |
| \(\mathfrak F_R\) | deterministic policy | complete posterior-aware residual selection, composition, and pre-risk fallback map |
| \(\Xi_R\) | typed contract tuple | complete residual representation, kernel, key, and gate contract |
| \(\mathfrak E_t^B,\mathcal N_t^B\) | finite sets | bounded candidate universe and nominated Bayesian frontier |
| \(J_t^{\mathrm{nom}},J_t^{\mathrm{evid}},A_t^B,\tau_t^B,J_t^{\mathrm{act}}\) | indicators and scores | nomination, evidence-readiness, activation score, threshold, and threshold-selective decision |
| \(q_B,q_{\mathrm{FA}},q_{\mathrm{sel}},J_t^{\mathrm{upd},q_B}\) | policies, indicator | frozen Bayesian policy, frontier-all and selective policies, and complete policy-indexed admission decision |
| \(\kappa_t^B,\mathcal X_{K,t}^{\mathrm{upd},q_B},L_K^{\mathrm{adm},q_B}\) | map, finite set, likelihood | posterior-key assignment, admitted evidence-packet set, and admission-conditioned likelihood |
| \(p_K^{\mathrm{adm},q_B},\underline p_{K,t}^{\mathrm{adm},q_B},p_{\min}^{\mathrm{adm}},\mathfrak H_{K,t}^{\mathrm{adm},q_B}\) | probability, bound, threshold, set | complete admission probability, certified lower bound, positive support floor, and certified admission-support region |
| \(J_{K,t}^{\mathrm{share}}\) | \(\{0,1\}\) | Anti-Pigeon posterior-sharing certificate decision for bucket \(K\) |
| \(q_{K,t^-},q_{K,t}^+,q_{K,t}^{\mathrm{eff}}\) | probability measures | cached prior, candidate update, and valid posterior actually used for prediction |
| \(u_e,v_e,n_e^{\mathrm{eff}},\ell_K^{\mathrm{share}},\ell_K^{\mathrm{split}},p_K^{\mathrm{split}},p_K^{\mathrm{eq}},G_{K,t}^{B},w_{K,t}^{B}\) | counts, reals, decision | member sufficient statistics, shared/split evidence, split and practical-equivalence probabilities, proposal-only group decision, and bounded borrowing weight |
| \(\pi_K^{\mathrm{split}},\tau_{B,\mathrm{cmp}},n_{B,\mathrm{cmp}},K_{\max}\) | constants | frozen split prior, decision threshold, minimum member support, and group-size cap |
| \(\omega_{B,\mathrm{pool}},J_t^{\mathrm{val}},J_{K,t}^{\mathrm{shock}},A_{K,t}^{\mathrm{rev}}\) | weight, indicators, action | pooled-evidence discount, revision-valid evidence, Anti-Pigeon split shock, and fail-closed revision action |
| \(Y_{K,t},m_{K,t}^{s},C_{K,t}^{+},C_{K,t}^{-},\delta_{\mathrm C},h_{\mathrm C},d_{K,t}^{\mathrm{cool}},n_{\mathrm{warm}}\) | outcome, states, constants | observed usefulness, slow reference, cumulative detector, slack, boundary, cooldown, and warm-up |
| \(J_{K,t}^{\mathrm{cp}},J_t^{\mathrm{audit}}\) | \(\{0,1\}\) | changepoint trigger and independent non-admitted-event audit indicator |
| \(D_{\mathrm{omit}},\Delta_{K,t}^{\mathrm{omit}},U_t^{\mathrm{omit}}\) | divergence and reals | normalized Jensen--Shannon forecast divergence, audit-population mean, and simultaneous upper confidence bound |
| \(\mathfrak U_{\mathrm{omit}}^{\mathrm{seq}}\) | confidence procedure | frozen design-weighted simultaneous confidence sequence for omitted influence |
| \(N_{\mathrm{audit}}^{\max}\) | non-negative integer | fixed non-admitted-event audit-reservoir capacity |
| \(B_{\max},N_t^{\mathrm{upd},q_B},M_{\mathrm{hyp}},R_{\mathrm{cp}}\) | non-negative integers | frontier cap, admitted count, bounded hypothesis/statistic dimension, and retained changepoint-state count |
| \(T_{\mathrm{adm}},T_{\mathrm{sel}},T_{\mathrm{Bayes}}^{\mathrm{fast}}\) | costs | policy admission, complete admission-probability, and bounded direct Bayesian work |
| \(\mathcal C_{B,t^-},\Xi_B\) | cache, typed contract | as-of posterior cache and complete bounded Bayesian contract |
| \(c_t^{\mathrm{pack}},r_{i,t}^{\mathrm{corr}},\lambda_{i,t}^{\mathrm{el}},d_{i,t}^{\mathrm{raw}},\Delta_{i,t}^{\mathrm{rank}},s_{i,t}^{\mathrm{final}}\) | reals | packing-boundary certainty, independent correction reliability, elastic scale, raw correction, hard-capped rank delta, and final retrieval score |
| \(\Sigma_t,B_{\mathrm{pub}},B_{\mathrm{inv}},N_{\mathrm{pub}},N_{\mathrm{inv}}\) | state and counts | coupled versioned learning state, per-evidence-epoch publication/invalidation budgets, and realized counts |
| \(X_t\) | \(\mathcal X_{\mathrm{ctx}}\) | compressed runtime context state |
| \(\mathcal Y_{\mathrm{pkt}}\) | product set | runtime packet space |
| \(\mathcal V_Y\) | normed vector space | packet representation/residual space |
| \(B_Y,R_Y\) | typed maps | packet baseline and packet residual |
| \(\oplus_Y\) | \(\mathcal Y_{\mathrm{pkt}}\times\mathcal V_Y\to\mathcal Y_{\mathrm{pkt}}\) | packet residual composition |
| \(\widehat{\mathbf y}_{t+1}\) | \(\mathcal Y_{\mathrm{pkt}}\) | predicted runtime packet |
| \(\mathbf y_{t+1}^{\star}\) | \(\mathcal Y_{\mathrm{pkt}}\) | audited packet target |
| \(G_t=(V_t,R_t)\) | typed directed graph | time-unrolled event graph |
| \(\mathfrak M\) | SCM | structural causal model \((U,V,F,P_U)\) |
| \(\pi\) | \(\mathcal E\to\mathcal S_{\mathrm{abs}}\) | event abstraction map |
| \(h_\pi(C)\) | operational key | abstract context plus declared, costed side information |
| \(K\) | subset of \(\mathcal E\) | abstraction bucket; never the baseline predictor |
| \(\mathfrak K_\pi\) | set of buckets | partition or grouping induced by \(\pi\) |
| \(\mathfrak K_\pi^+\) | set of buckets | active buckets with non-empty admissible context families |
| \(\bar e_K\) | element of \(K\) | concrete traceability frame |
| \(\mathfrak C_K\) | subset of \(\mathcal E^k\) | contexts whose anchor frame lies in \(K\) |
| \(\mathcal R_C(K)\) | subset of \(\mathfrak C_K\) | coverage-aware context audit set |
| \(D_K^\star(\pi)\) | non-negative real | external target-law bucket future-diameter |
| \(D_K^{\mathrm{mdl}}(\Theta_\Gamma)\) | non-negative real | candidate model-forecast diameter; diagnostic only |
| \(D_K^{\mathrm{audit},\star},\widehat D_K^\star\) | non-negative reals | restricted external diameter and its estimate |
| \(D_K^{\mathrm{cert},\star}\) | non-negative real | simultaneous statistical and continuity upper certificate |
| \(\zeta_t\) | \(\mathcal Z_{\mathrm{reg}}\) | observed operating regime; not causal by default |
| \(\mathcal C_{\mathrm{rep}}\) | non-negative function | representation/runtime cost; does not reuse \(\Omega\) |
| \(\Phi\) | real-valued potential | fixed finite-state refinement objective |
| \(\mathcal G_t^A=(V_t^A,E_t^A)\) | undirected graph | abstraction compatibility graph at time \(t\) |
| \(\mathsf Q_i\) | \(\mathcal P(\mathcal Y_i)\) | node-local predictive law |
| \(g_{ie},\mathsf r_{ie}\) | measurable map, pushforward map | node-to-edge comparison map and its distributional restriction |
| \(\delta_e,\Delta_{\mathrm{comp}}\) | non-negative reals | edge defect and maximum upper confidence bound |
| \(\partial_A,L_A\) | linear operators | compatibility boundary and Laplacian under linear assumptions |
| \(\Xi_A^{(v)}\) | typed structure tuple | published versioned compatibility graph, assigned spaces, maps, divergences, and weights |
| \(\mathfrak S_t,\Psi_t\) | finite set, real function | bounded predictive-snap candidate family and its design-block score |
| \(d_{\mathrm{edit}},\mathcal C_{\mathrm{snap}}\) | non-negative functions | graph-churn penalty and measured or hardware-indexed snap cost |
| \(D_t^{\mathrm{design}},D_t^{\mathrm{conf}}\) | chronological data blocks | disjoint as-of blocks used to select and then confirm a predictive-snap candidate |
| \(\mathfrak O_t,U_{\mathrm{obl}}\) | finite obligation set, non-negative function | externally fixed comparison obligations and unresolved-obligation burden |
| \(\lambda_{\mathrm{comp}},\lambda_{\mathrm{edit}},\lambda_{\mathrm{snap}},\lambda_{\mathrm{obl}}\) | non-negative reals | snap-selection weights for defect, churn, revision cost, and unresolved obligations |
| \(\mathcal D_{\Delta,t},\mathfrak K_{\Delta,t},E_{\Delta,t}^{\mathrm{keep}}\) | affected sets | reverse dependency closure and its affected active-bucket and retained/new-edge projections |
| \(A_t^{\mathrm{snap}}\) | \(\{0,1\}\) | joint confirmation and publication indicator for a selected snap |
| \(\Lambda_{\mathrm{eval}}\) | fixed contract tuple | externally frozen domains, metrics, targets, thresholds, weights, validation procedures, and snap-policy rules |
| \(\mathcal U_0,\ldots,\mathcal U_5\) | staged maps | baseline and selectable refinement operators, including predictive sheaf snapping at Stage 3 |
| \(\mathcal B_0,\ldots,\mathcal B_3\) | staged maps | bounded Bayesian update, changepoint, event-pattern, and deep particle/variational ladder |
| \(r_n\) | \(\{1,2,3,4,5\}\) | stage selected at slow-path invocation \(n\) |
| \(d_t(h)\) | \(\{0,\ldots,5\}\) | selected refinement depth on hardware profile \(h\) |
| \(p_t^{\mathrm{pri}}\) | \([0,1]\) | priority assigned from prediction-time information |
| \(w_{\mathrm{pri}}\) | positive function | declared importance weight for priority |
| \(\Delta_{\mathrm{pred}}(d),\widehat\Delta_{\mathrm{pred}}(d)\) | reals | paired proper-risk effect of ablating distinction \(d\) and its confirmation estimate |
| \(s_{\mathrm{eff}}^{\mathrm{pred}},s_{\mathrm{eff}}^{\mathrm{causal}}\) | \([0,1]\) | confidence-classified predictive-ablation and identified-causal sparsity ratios |
| \(\mathfrak F_{AP}^{\Gamma,\star},\mathcal J_\Gamma^{\mathrm{oracle}}\) | family, real value | oracle population-feasible family and its infimal benchmark |
| \(\mathfrak G_\Gamma,\widehat{\mathfrak F}_{AP}^{\Gamma},\widehat\Theta_\Gamma\) | finite families, design | predeclared candidate family, certified empirical family, and selected design |
| \(G_{a\rightarrow b}^{\mathrm{pri}}\) | real | priority-weighted absolute gain between complete policies |
| \(\mathcal R_{\mathrm{pri}}^D\) | non-negative real | normalized priority-weighted post-observation risk under \(D\) |
| \(\mathcal R_{\mathrm{prop}}^D\) | extended real | unweighted strictly proper forecast risk under \(D\) |
| \(D_Y^{\mathrm{law}}\) | law distance | distance between predictive or interventional laws; distinct from packet decoder \(d_Y\) |

## Event Space

An event frame is:

\[
e_t=(w_t,a_t,\tau_t,\ell_t,m_t,h_t,x_t,c_t)
\]

with typed product space:

\[
\mathcal E_{\Delta_\tau}
=\mathcal W\times\mathcal A\times\mathcal T_{\Delta_\tau}
\times\mathcal L\times\mathcal M\times\mathcal H
\times\mathcal X\times\mathcal C.
\]

These component-space symbols are used only for event fields. Runtime packet component spaces carry descriptive subscripts and are not identified with them.

The coarse-graining is:

\[
\Gamma_{\Delta_\tau}:\Omega^{A_t}\rightarrow\mathcal E_{\Delta_\tau},
\qquad
e_t=\Gamma_{\Delta_\tau}(\omega_{A_t}).
\]

The framework does not assert that \(\Omega\) is discrete or sampled at Planck scale.

## Marked Event Forecast

The context is:

\[
C_t=e_{t-k+1:t}\in\mathcal E^k.
\]

All conditional-law suprema range over a declared \(\mathfrak C_{\mathrm{adm}}\) or the support of a named evaluation law; arbitrary zero-probability contexts are excluded unless a conditional-law version is explicitly defined there.

The complete event field may contain a point time or interval. The scalar extractor \(\tau(e)\in\mathbb R\) is the timestamp for a point event and, by default, the onset for an interval event. Another measurable anchor may be declared, but it is frozen before fitting and used consistently in labels, caches, and evaluation. The next outcome over horizon \(H\) is:

\[
Z_{t+1}=\begin{cases}
(\nu(e_{t+1}),\tau(e_{t+1})-\tau(e_t)), & \text{event within }H,\\
\varnothing, & \text{no event within }H.
\end{cases}
\]

The measurable mark space is \((\mathcal N,\mathscr A_{\mathcal N})\). With \(\mathscr B_H=\mathscr B((0,H])\), define \((\mathcal Z_H^+,\mathscr A_H^+)=(\mathcal N\times(0,H],\mathscr A_{\mathcal N}\otimes\mathscr B_H)\) and \((\mathcal Z_H,\mathscr A_H)=(\mathcal Z_H^+\sqcup\{\varnothing\},\mathscr A_H^+\oplus2^{\{\varnothing\}})\). Thus \(\mathcal P(\mathcal Z_H)\) always refers to probability measures on this declared measurable space, equipped with the evaluation sigma-algebra generated by \(Q\mapsto Q(A)\), \(A\in\mathscr A_H\).

Let \(\mathcal E_\varnothing=\mathcal E\sqcup\{\varnothing\}\), and fix \(d_H:\mathcal P(\mathcal Z_H)\to\mathcal Z_H\) with a declared point loss and deterministic tie-break. The structured summary \(\hat e_\theta^H(C_t)\in\mathcal E_\varnothing\) equals \(\varnothing\) exactly when \(d_H(\mathsf Q_\theta)=\varnothing\); otherwise its mark and time agree with the selected marked time. The forecast and primary probabilistic-fidelity loss are:

\[
\mathsf Q_\theta(\cdot\mid C_t)\in\mathcal P(\mathcal Z_H),
\qquad
\mathcal O_\theta(C_t)=
(\mathsf Q_\theta(\cdot\mid C_t),\hat e_\theta^H(C_t)),
\]

\[
\qquad
\mathcal L_{\mathrm{pred}}(\theta;t)
=S_{\mathrm{prop}}(\mathsf Q_\theta(\cdot\mid C_t),Z_{t+1}).
\]

For a mixed event/no-event logarithmic score, fix a dominating event-branch reference measure \(\mu_H\) and time units. The event branch is a subdensity with respect to \(\mu_H\) whose mass plus \(\mathsf Q_\theta(\{\varnothing\}\mid C_t)\) equals one. The no-event observation is scored by \(-\log\mathsf Q_\theta(\{\varnothing\}\mid C_t)\), not by evaluating an undefined event time. If \(d\mu_H'=h\,d\mu_H\), marked-event loss changes by \(\log h(Z)\), which is outcome-dependent unless \(h\) is constant. The reference measure and units remain fixed for absolute reporting.

The event-aware diagnostic is:

\[
\mathcal L_{\mathrm{event}}^H(\hat Z,Z)=
\begin{cases}
0, & \hat Z=Z=\varnothing,\\
1, & \text{one is null or their marks differ},\\
\min(1,|\widehat{\Delta t}-\Delta t|/H), & \text{marks agree.}
\end{cases}
\]

## Lifecycle Scores

For a candidate bundle \(\widetilde{\mathcal O}=(\widetilde{\mathsf Q},\tilde e^H)\), before observation:

\[
\mathcal R_{\mathrm{pre}}(\widetilde{\mathcal O}\mid C_t)
=\lambda_a^{\mathrm{pre}}D_{\mathrm{abs}}^{\mathrm{pre}}(\widetilde{\mathcal O},C_t)
+\lambda_c^{\mathrm{pre}}D_{\mathrm{edge}}^{\mathrm{pre}}(\widetilde{\mathcal O},C_t)
+\lambda_u^{\mathrm{pre}}U^{\mathrm{pre}}(\widetilde{\mathcal O}\mid C_t).
\]

The three components lie in \([0,1]\), and their non-negative weights sum to one. The log score is \(+\infty\) at zero realized mass or density. Let \(g_{\mathrm{pred}}:\overline{\mathbb R}\to[0,1]\) be a preregistered measurable non-decreasing map on the entire attainable extended-real score range, with every attainable endpoint defined. For non-negative log loss, \(g_{\mathrm{pred}}(\ell)=1-e^{-\ell/\kappa}\), \(\kappa>0\), with \(g_{\mathrm{pred}}(+\infty)=1\), is one admissible example. Constant or order-reversing transforms are inadmissible. Define:

\[
\overline{\mathcal L}_{\mathrm{pred}}(\widetilde{\mathsf Q},Z)
=g_{\mathrm{pred}}(S_{\mathrm{prop}}(\widetilde{\mathsf Q},Z)).
\]

Unless \(g_{\mathrm{pred}}\) is positive affine on the score range, the transformed loss is not asserted to remain proper. After observation:

\[
\begin{aligned}
\mathcal A_{\mathrm{post}}(\widetilde{\mathcal O},Z)
={}&\lambda_p^{\mathrm{post}}\overline{\mathcal L}_{\mathrm{pred}}(\widetilde{\mathsf Q},Z)
+\lambda_a^{\mathrm{post}}D_{\mathrm{abs}}^{\mathrm{post}}(\widetilde{\mathcal O},Z)\\
&+\lambda_c^{\mathrm{post}}D_{\mathrm{edge}}^{\mathrm{post}}(\widetilde{\mathcal O},Z)
+\lambda_u^{\mathrm{post}}U^{\mathrm{post}}(\widetilde{\mathcal O},Z).
\end{aligned}
\]

Every post component lies in \([0,1]\), and the four non-negative post weights sum to one. Thus \(\mathcal A_{\mathrm{post}}\in[0,1]\). The untransformed proper score remains the fitting and forecast-comparison quantity. Empirical \(+\infty\) proper loss gives an infinite proper-risk guard unless a frozen probability-floor forecast family was declared in advance. \(\mathcal A_{\mathrm{post}}\) is undefined before \(Z\) is observed and may not gate the fast path. Every diagnostic, target, normalization, missing-value rule, admissible class, fitting rule, deterministic tie-break, packet target/loss, priority model, and regime-shift rule is frozen by \(\Lambda_{\mathrm{eval}}\) before confirmation; candidate-specific or confirmation-driven retuning is invalid.

## Event Residual Composition

Let \(\mathbb H_d^E\) and \(\mathbb H_d^Q\) be separately tagged copies of the self-adjoint operators with Frobenius norm. Define:

\[
q_E:\mathcal E\to\mathbb H_d^E,
\qquad
d_E:\mathcal Q_{E,\mathrm{adm}}\to\mathcal E.
\]

Clipping is:

\[
\mathrm{clip}_{\delta_E}(r)=
\begin{cases}
0,&r=0,\\
r\min(1,\delta_E/\|r\|_F),&r\ne0.
\end{cases}
\]

Projection is a deterministic selection:

\[
\Pi_E(v)\in\arg\min_{u\in\mathcal Q_{E,\mathrm{adm}}}\|u-v\|_F.
\]

Composition is:

\[
b\oplus_Er=
\begin{cases}
b,&r=0,\\
d_E(\Pi_E(q_E(b)+\mathrm{clip}_{\delta_E}(r))),&r\neq0.
\end{cases}
\]

The zero branch makes no correction an exact identity. The decoder is not written as an inverse because the encoder may be lossy.

For the forecast issued at \(t\), let \(\mathcal K_t^{\mathrm{bel}}\) be the finite set of valid local belief buckets. For each bucket, let \(q_{K,t}^{\mathrm{eff}}\) be the valid updated posterior when one was accepted and the valid cached prior otherwise. Let \((\mathcal X_K,\mathscr A_{\mathcal X_K})\) be its evidence space and \(\nu_K\) a sigma-finite dominating measure. Ordinary posterior-predictive semantics require a measurable joint kernel

\[
\mathbb P_{K,\theta}:
\mathfrak H_t\to\mathcal P(\mathcal X_K\times\mathcal Z_H),
\qquad
\mathbb P_{K,\theta}(d\xi,dz\mid\mathfrak h),
\quad \theta\in\Theta_K.
\]

The scored outcome kernel has type

\[
\mathsf P_{H,K}:\Theta_K\times\mathcal E^k
\to\mathcal P(\mathcal Z_H).
\]

Define its marginals by

\[
\mathbb P_{K,\theta}^{\Xi}(D\mid\mathfrak h)
=\mathbb P_{K,\theta}(D\times\mathcal Z_H\mid\mathfrak h),
\qquad
\mathbb P_{K,\theta}^{Z}(A\mid\mathfrak h)
=\mathbb P_{K,\theta}(\mathcal X_K\times A\mid\mathfrak h).
\]

The normative coherence identities are

\[
L_K(\xi\mid\theta,\mathfrak h)
=\frac{d\mathbb P_{K,\theta}^{\Xi}(\cdot\mid\mathfrak h)}{d\nu_K}(\xi),
\qquad
\mathbb P_{K,\theta}^{Z}(A\mid\mathfrak h)
=\mathsf P_{H,K}(A\mid\theta,c_k(\mathfrak h)).
\]

The domination condition \(\mathbb P_{K,\theta}^{\Xi}(\cdot\mid\mathfrak h)\ll\nu_K\) holds for every declared \((\theta,\mathfrak h)\). Because the displayed outcome kernel does not consume \(\xi\), require

\[
\mathbb P_{K,\theta}(d\xi,dz\mid\mathfrak h)
=L_K(\xi\mid\theta,\mathfrak h)\,\nu_K(d\xi)\,
\mathsf P_{H,K}(dz\mid\theta,c_k(\mathfrak h)).
\]

Thus evidence and next outcome are conditionally independent given the declared parameter and context. If this factorization fails, the predictive kernel and the posterior-predictive integral retain \(\xi\) or the additional history. Separately modeled likelihood and forecast components remain modular belief-conditioned forecasts even after favorable proper-score or calibration validation; such validation does not establish a joint-model identity.

With frozen non-negative weights \(\lambda_{K,t}^{\mathrm{bel}}(C_t)\) summing to one, define the pre-residual base law

\[
\mathsf Q_t^0(A\mid C_t)=
\begin{cases}
\displaystyle\sum_{K\in\mathcal K_t^{\mathrm{bel}}}
\lambda_{K,t}^{\mathrm{bel}}(C_t)
\int_{\Theta_K}\mathsf P_{H,K}(A\mid\theta,C_t)q_{K,t}^{\mathrm{eff}}(d\theta),
&\mathcal K_t^{\mathrm{bel}}\ne\varnothing,\\
\mathsf Q_B(A\mid C_t),&\mathcal K_t^{\mathrm{bel}}=\varnothing.
\end{cases}
\]

A plug-in posterior predictive is allowed only when its decision rule is declared and its output is labeled as plug-in. The aligned base template is

\[
b_t^0=
\begin{cases}
B_H^{\mathrm{bel}}\!\left(C_t,
(q_{K,t}^{\mathrm{eff}})_{K\in\mathcal K_t^{\mathrm{bel}}},
(\lambda_{K,t}^{\mathrm{bel}})_{K\in\mathcal K_t^{\mathrm{bel}}}\right),
&\mathcal K_t^{\mathrm{bel}}\ne\varnothing,\\
B(C_t),&\mathcal K_t^{\mathrm{bel}}=\varnothing,
\end{cases}
\]

with \(b_t^0=B(C_t)\) on the empty-belief fallback. Thus the canonical scored order is posterior update, posterior-predictive base law, posterior-aware residual selection, then residual-kernel composition.

The point residual is defined only on an in-horizon event and against the base template actually forecast:

\[
r_{t,H}^{E,\mathrm{obs}}=q_E(e_{t+1})-q_E(b_t^0),
\qquad 0<\tau(e_{t+1})-\tau(e_t)\le H.
\]

It is undefined when \(Z_{t+1}=\varnothing\). A later event cannot retroactively label the expired forecast; no-event observations may instead update the distributional kernel through the proper score.

A distributional residual may be learned on either outcome branch through a declared measurable estimator:

\[
\rho_H^Q:\mathcal P(\mathcal Z_H)\times\mathcal Z_H\to\mathbb H_d^Q,
\qquad
r_{t,H}^{Q,\mathrm{obs}}=\rho_H^Q(\mathsf Q_t^0(\cdot\mid C_t),Z_{t+1}).
\]

It is defined at \(\varnothing\), and cache provenance distinguishes it from \(r_{t,H}^{E,\mathrm{obs}}\). Let \(\mathcal M_R=\{\varnothing,E,Q,EQ\}\), \(\mathcal V_R=\mathbb H_d^E\times\mathbb H_d^Q\times\mathcal M_R\), and \(\mathbf r=(r^E,r^Q,m)\in\mathcal V_R\). The mode is authoritative about component presence. Point and law components have independent semantics; a joint record requires forward validation of the complete output bundle and does not assert that its components are equal.

## Residual Caches

Both caches are reconstructed as of \(S_{t^-}\); no later entry, outcome, confidence update, epoch, or audit result may be read. The general cache is:

\[
\mathcal C_{R,t^-}=\{(\kappa_i,\mathbf r_i,c_i,n_i,t_i,v_i,\mu_i,H_i,
\upsilon_i^{\mathrm{bel}},\mu_i^{\mathrm{bel}},\mu_i^{\mathrm{tmpl}},s_i)\}_{i=1}^{N_t},
\quad
\kappa:\mathcal E^k\to\mathcal K_R,
\quad \mathbf r_i\in\mathcal V_R.
\]

For \(N_t>0\), \(j_t\) is the deterministic nearest-key selection. Let \(J_t^R\) indicate that distance, confidence, effective support, age, epoch, horizon equality \(H_i=H\), compatibility margin, provenance, posterior-predictive version \(\upsilon_i^{\mathrm{bel}}=\upsilon_t^{\mathrm{bel}}\), law margin for a law-bearing mode, and template margin for a point-bearing mode all pass; set it to zero when the cache is empty. Then

\[
\mathbf r_t^*=\begin{cases}
\mathbf r_{j_t},&J_t^R=1,\\
\mathbf 0_R,&\text{otherwise.}
\end{cases}
\]

The action cache is typed as:

\[
\mathcal C_{A,t^-}:\mathcal K_A\rightharpoonup
\mathcal V_R\times[0,1]\times\mathbb N_0\times\mathcal T
\times\mathbb N_0\times\mathbb R\times\mathbb R_{>0}
\times\mathbb N_0\times\mathbb R\times\mathbb R\times\mathcal S_{\mathrm{prov}}.
\]

For \(k_t=\alpha(C_t)\), bind the entry only when it exists, including provenance \(s_{k_t}\), posterior-predictive version \(\upsilon_{k_t}^{\mathrm{bel}}\), law-motion margin \(\mu_{k_t}^{\mathrm{bel}}\), and template-motion margin \(\mu_{k_t}^{\mathrm{tmpl}}\). Let \(J_t^A\) indicate that confidence, effective support, age, epoch, horizon equality \(H_{k_t}=H\), compatibility margin, provenance, posterior-predictive version equality, and every mode-applicable motion margin pass; set it to zero when the key is absent. The exact-to-general selector is:

\[
\mathbf r_t^{\mathrm{use}}=
\begin{cases}
\mathbf r_{k_t},&J_t^A=1,\\
\mathbf r_t^*,&J_t^A=0\text{ and }J_t^R=1,\\
\mathbf 0_R,&\text{otherwise.}
\end{cases}
\]

This indicator distinguishes an accepted zero residual from a cache miss. Before declaring the corrected forecast law, define its fixed-reference motion certificates.

Each residual certificate is calibrated against fixed posterior-predictive references. Freeze a bounded law distance \(D_{\mathrm{res}}\), law reference \(\mathsf Q_i^{0,\mathrm{ref}}\), and tolerance \(\epsilon_i^{\mathrm{bel}}\). For a point-bearing mode, additionally freeze a bounded template distance \(D_{\mathrm{tmpl}}\), template reference \(b_i^{0,\mathrm{ref}}\), and tolerance \(\epsilon_i^{\mathrm{tmpl}}\). Let \(\overline D_{i,t}^{\mathrm{bel}}\) and \(\overline D_{i,t}^{\mathrm{tmpl}}\) be analytic or simultaneously valid upper bounds for

\[
D_{\mathrm{res}}(\mathsf Q_t^0,\mathsf Q_i^{0,\mathrm{ref}}),
\qquad
D_{\mathrm{tmpl}}(b_t^0,b_i^{0,\mathrm{ref}}),
\]

and define

\[
\mu_i^{\mathrm{bel}}=\epsilon_i^{\mathrm{bel}}-\overline D_{i,t}^{\mathrm{bel}},
\qquad
\mu_i^{\mathrm{tmpl}}=\epsilon_i^{\mathrm{tmpl}}-\overline D_{i,t}^{\mathrm{tmpl}}.
\]

The bounds include posterior-approximation error propagated through \(\mathsf P_{H,K}\), mixture fusion, and, for the point path, \(B_H^{\mathrm{bel}}\), in addition to statistical uncertainty. A plug-in distance or approximation estimate without uncertainty coverage is not a certificate. A law-bearing record requires \(\mu_i^{\mathrm{bel}}\ge0\); a point-bearing record requires \(\mu_i^{\mathrm{tmpl}}\ge0\); a joint record requires both. An ordinary posterior update may retain \(\upsilon_t^{\mathrm{bel}}\) only while every applicable fixed-reference margin remains non-negative. Otherwise the dependency-closure operators \(\mathsf B_{\mathcal D}\) and \(\mathsf I_{\mathcal D}\) in Section 8 bump the posterior-predictive, residual, and graph versions and stale the affected entries.

The law-residual kernel is then declared by:

\[
\mathfrak K_H^Q:\mathbb H_d^Q\to\mathrm{Ker}(\mathcal Z_H),
\qquad
\mathfrak K_H^Q(0_Q)(z,A)=\mathbf 1_A(z),
\]

for every \(z\in\mathcal Z_H\), including \(\varnothing\). For each \(A\in\mathscr A_H\), \((r^Q,z)\mapsto\mathfrak K_H^Q(r^Q)(z,A)\) is jointly measurable, and each fixed residual induces a Markov kernel. With \(\mathcal Z_H^+=\mathcal Z_H\setminus\{\varnothing\}\), the implementation declares the no-event transitions for every nonzero effective law residual; no atom-preservation default is assumed.

For \(\mathbf r=(r^E,r^Q,m)\), let \(\bar r^E\) and \(\bar r^Q\) be the corresponding component clips at radii \(\delta_E\) and \(\delta_Q\), with an absent component replaced by its tagged zero. Define, for \(A\in\mathscr A_H\):

\[
\mathsf Q_t^{(\mathbf r)}(A\mid C_t)=
\int_{\mathcal Z_H}\mathfrak K_H^Q(\bar r^Q)(z,A)
\,\mathsf Q_t^0(dz\mid C_t).
\]

In particular,

\[
\begin{aligned}
\mathsf Q_t^{(\mathbf r)}(\{\varnothing\}\mid C_t)
={}&\mathfrak K_H^Q(\bar r^Q)(\varnothing,\{\varnothing\})
\mathsf Q_t^0(\{\varnothing\}\mid C_t)\\
&+\int_{\mathcal Z_H^+}\mathfrak K_H^Q(\bar r^Q)(z,\{\varnothing\})
\,\mathsf Q_t^0(dz\mid C_t).
\end{aligned}
\]

Let \(\mathrm{lift}_H:\mathcal E\times\mathcal Z_H^+\to\mathcal E\) align a corrected event template with the marked decision. Set \(\hat e_t^H(\mathbf r)=\varnothing\) when \(d_H(\mathsf Q_t^{(\mathbf r)})=\varnothing\), and otherwise set \(\hat e_t^H(\mathbf r)=\mathrm{lift}_H(b_t^0\oplus_E\bar r^E,d_H(\mathsf Q_t^{(\mathbf r)}))\). Then \(\mathcal O_t(\mathbf r)=(\mathsf Q_t^{(\mathbf r)},\hat e_t^H(\mathbf r))\), with \(\mathcal O_t^0=\mathcal O_t(\mathbf0_R)\). The typed pair keeps law and auxiliary-template semantics separate; \(d_H\) and \(\mathrm{lift}_H\) enforce mark/time coherence only. The selected candidate is returned only if its pre-observation gate passes from \(S_{t^-}\); otherwise \(\mathcal O_t^0\) is returned. Define the deterministic complete-law policy \(\mathfrak F_R(\mathsf Q_t^0,b_t^0,C_t;S_{t^-})=\mathsf Q_t^R\), where \(\mathsf Q_t^R\) is the law component actually returned after residual selection and pre-risk gating. Point-only records cannot support a proper-score claim; law-only records cannot claim auxiliary-field correction. Confidence updates include only outcomes already available, use clustered or effective support for overlapping contexts, and use sequentially valid inference when monitored repeatedly.

## Bounded Bayesian Updating

Let \(\mathfrak E_t^B\) be the bounded as-of candidate universe and let the nominated frontier be

\[
\mathcal N_t^B=
\mathcal R_t^{\mathrm{vec}}\cup\mathcal N_t^{\mathrm{sh}}\cup
\begin{cases}
\mathrm{Pa}_{\mathfrak M}(v_t^E)\cup\mathrm{Ch}_{\mathfrak M}(v_t^E),
&\mathfrak M\text{ and its identification contract are available},\\
\mathcal N_t^{\mathrm{pred}},&\text{otherwise}.
\end{cases}
\]

Here \(\mathcal R_t^{\mathrm{vec}}\) is bounded vector retrieval, \(\mathcal N_t^{\mathrm{sh}}\) is a bounded sheaf-inspired compatibility neighborhood, and the final two sets are bounded incoming and outgoing relationships already present in the as-of graph. They scope candidate updates only: an outgoing edge is not evidence about an unrealized child outcome. The graph terms are called causal only when an explicit SCM and identification contract justify that label; otherwise they are predictive-dependency neighbors.

Define \(J_t^{\mathrm{nom}}(e)=\mathbf1\{e\in\mathcal N_t^B\}\) and \(J_t^{\mathrm{evid}}(e)=\mathbf1\{\xi_t(e)\text{ exists and }a(\xi_t(e))\le t\}\) on all \(e\in\mathfrak E_t^B\). A declared graph child or other hypothesis without an available frame may be nominated but is not activatable. Let \(v_t^B(e),n_t^B(e),u_t^B(e),s_t^B(e),c_t^B(e)\in[0,1]\) be frozen vector relevance, neighbor compatibility, novelty, source-independence, and structural-criticality scores when evidence is ready. With non-negative weights summing to one, define

\[
A_t^B(e)=
\begin{cases}
\alpha_Bv_t^B(e)+\beta_Bn_t^B(e)+\gamma_Bu_t^B(e)+\delta_Bs_t^B(e),
&J_t^{\mathrm{nom}}(e)J_t^{\mathrm{evid}}(e)=1,\\
0,&\text{otherwise},
\end{cases}
\]

\[
\tau_t^B(e)=\min\!\left(\tau_{\max},
\max\!\left(\tau_{\min},\tau_0-\lambda_{\mathrm{crit}}c_t^B(e)\right)\right),
\qquad
J_t^{\mathrm{act}}(e)=J_t^{\mathrm{nom}}(e)J_t^{\mathrm{evid}}(e)
\mathbf1\{A_t^B(e)\ge\tau_t^B(e)\}.
\]

Freeze \(q_B\in\{q_{\mathrm{FA}},q_{\mathrm{sel}}\}\) and define

\[
J_t^{\mathrm{upd},q_B}(e)=
\begin{cases}
J_t^{\mathrm{nom}}(e)J_t^{\mathrm{evid}}(e),&q_B=q_{\mathrm{FA}},\\
J_t^{\mathrm{act}}(e),&q_B=q_{\mathrm{sel}}.
\end{cases}
\]

Here \(q_{\mathrm{FA}}\) is the reference bounded-frontier-update-all policy and \(q_{\mathrm{sel}}\) is the optional threshold-selective policy. Updating all means all evidence-ready nominated members, never the entire corpus. Every score is computed from information available when the update decision is made and before any target whose performance will be claimed. Because \(J_t^{\mathrm{upd},q_B}\) is total on \(\mathfrak E_t^B\), its model probability includes nomination and evidence readiness under both policies and threshold admission under \(q_{\mathrm{sel}}\). Implementations materialize and score only \(\mathcal N_t^B\), representing the zero branch outside it sparsely. The scoring maps, caps, weights, thresholds, tie-breaks, policy, and provenance rules are components of \(\Xi_B\) and are frozen under \(\Lambda_{\mathrm{eval}}\).

Let \((\Theta_K,\mathscr A_{\Theta_K})\) be a measurable parameter space and \(q_{K,t^-}\in\mathcal P(\Theta_K)\) the cached prior for bucket \(K\). Anti-Pigeon controls posterior granularity through

\[
J_{K,t}^{\mathrm{share}}=\mathbf1\!\left\{
D_K^{\mathrm{cert},\star}\le\epsilon_{B,\mathrm{share}},\quad
n_{K,t}^{\mathrm{eff}}\ge n_{B,\min},\quad
v_{K,t}=v_t,\quad H_K=H,\quad s_K\text{ is valid}
\right\}.
\]

The certificate uses the external downstream target law, not agreement inside the posterior. Its guarantee is empirical and conditional on valid target-law estimation, audit design, simultaneous coverage, and any declared continuity bound; the framework does not prove those premises. Compatible events may share a bucket posterior; a failed or absent certificate creates a separate posterior key and nominates a slow-path split audit. The fast path reads a materialized certificate and never recomputes the diameter.

For a Bernoulli retrieval-usefulness specialization, retain member statistics \((u_e,v_e)\) and define

\[
\begin{aligned}
\ell_K^{\mathrm{share}}
&=\log\frac{\mathrm B\!\left(a_0+\sum_{e\in K}u_e,b_0+\sum_{e\in K}v_e\right)}{\mathrm B(a_0,b_0)},\\
\ell_K^{\mathrm{split}}
&=\sum_{e\in K}\log\frac{\mathrm B(a_0+u_e,b_0+v_e)}{\mathrm B(a_0,b_0)},\\
p_K^{\mathrm{split}}
&=\mathrm{logistic}\!\left(\log\frac{\pi_K^{\mathrm{split}}}{1-\pi_K^{\mathrm{split}}}+\ell_K^{\mathrm{split}}-\ell_K^{\mathrm{share}}\right).
\end{aligned}
\]

Freeze a practical-equivalence width \(\epsilon_{B,\mathrm{eq}}>0\) and define

\[
p_K^{\mathrm{eq}}=
P\!\left(\max_{e,e'\in K}|\theta_e-\theta_{e'}|
\le\epsilon_{B,\mathrm{eq}}\,\middle|\,(u_e,v_e)_{e\in K}\right).
\]

With \(n_e^{\mathrm{eff}}=u_e+v_e\), minimum support \(n_{B,\mathrm{cmp}}\), split threshold \(\tau_{B,\mathrm{cmp}}>1/2\), and equivalence threshold \(\tau_{B,\mathrm{eq}}>1/2\), \(G_{K,t}^{B}\) proposes split when the support and split-threshold conditions hold, otherwise share when the support and equivalence-threshold conditions hold, and uncertain otherwise. The quantities \(p_K^{\mathrm{split}}\) and \(p_K^{\mathrm{eq}}\) are not complements: the first compares structural models and the second measures posterior mass inside the separately frozen equivalence region. Both conditions may hold, in which case split has precedence; uncertain is abstention, not a geometric band between complementary probabilities. For \(w_{B,\max}\in[0,1]\), the proposal-only borrowing weight is zero for split, \(p_K^{\mathrm{eq}}\) for share, and \(w_{B,\max}p_K^{\mathrm{eq}}\) for uncertain. The lower uncertain cap is intentionally conservative. The group cap is \(|K|\le K_{\max}\). This comparison is model-dependent and cannot create sharing: it cannot set \(J_{K,t}^{\mathrm{share}}\), publish a certificate, or positively merge posterior keys. A share proposal still requires the external target-law certificate.

For an already certified shared bucket, freeze \(\omega_{B,\mathrm{pool}}\in(0,1]\). The pooled Beta posterior receives \(\omega_{B,\mathrm{pool}}w_{e,t}\) per outcome while member statistics \((u_e,v_e)\) retain the full inclusion weight \(w_{e,t}\). Unless that fractional contribution is derived from a declared coherent generative model, \(\omega_{B,\mathrm{pool}}<1\) produces a tempered working posterior, not an ordinary common-parameter posterior. Let \(J_t^{\mathrm{val}}(e)\) identify full-stream or independent-audit evidence eligible to revoke sharing. The revealing outcome is incorporated into both pooled and member statistics before support, \(p_K^{\mathrm{split}}\), and the following shock indicator are evaluated:

\[
J_{K,t}^{\mathrm{shock}}(e)=
J_{K,t}^{\mathrm{share}}J_t^{\mathrm{val}}(e)
\mathbf1\!\left[\min_{e'\in K}n_{e'}^{\mathrm{eff}}\ge n_{B,\mathrm{cmp}},
p_K^{\mathrm{split}}\ge\tau_{B,\mathrm{cmp}}\right].
\]

The revision action \(A_{K,t}^{\mathrm{rev}}\) is split-reset when both split shock and changepoint fire, split for split shock alone, shared-reset for a changepoint in a shared bucket, individual-reset for a changepoint outside sharing, and retain otherwise. Split atomically revokes the old certificate, disables the shared posterior and residual, advances the dependency versions, and materializes event-local posteriors from retained member statistics. Split-reset additionally discards only the triggering member's pre-revealing sufficient statistics, calibration accumulators, and monitor state, then initializes that member from the declared prior plus the revealing outcome. Shared-reset retains the certified key while resetting its pooled posterior, calibration accumulators, member-comparison statistics, and monitor; individual-reset applies the analogous reset to the triggering event-local posterior. Each reset initializes from the prior plus the revealing outcome. Split never certifies a replacement group, and selected-only evidence is ineligible for this revocation transition.

Let \(\kappa_t^B(e)\) be the frozen posterior-key assignment after this decision and define

\[
\mathcal X_{K,t}^{\mathrm{upd},q_B}
=\{\xi_t(e):J_t^{\mathrm{upd},q_B}(e)=1,\ \kappa_t^B(e)=K\}.
\]

For admitted evidence \(\xi_t\) with history \(h_t^B\), an ordinary Bayesian update is valid only for the normalized likelihood \(L_K\) induced by the displayed joint-model marginal identity and with a positive finite normalizer. Separately modeled components remain modular forecasts:

\[
q_{K,t}^+(d\theta)=
\frac{L_K(\xi_t\mid\theta,h_t^B)q_{K,t^-}(d\theta)}
{\int_{\Theta_K}L_K(\xi_t\mid\vartheta,h_t^B)q_{K,t^-}(d\vartheta)}.
\]

If admission is informative, the update instead declares the admission-conditioned likelihood

\[
L_K^{\mathrm{adm},q_B}(\xi\mid\theta,h,J^{\mathrm{upd},q_B}=1)=
\frac{P_\theta(J^{\mathrm{upd},q_B}=1\mid\xi,h)L_K(\xi\mid\theta,h)}
{P_\theta(J^{\mathrm{upd},q_B}=1\mid h)},
\]

where both probabilities refer to the complete policy-indexed admission process. Define

\[
p_K^{\mathrm{adm},q_B}(\theta,h)=P_\theta(J^{\mathrm{upd},q_B}=1\mid h),
\qquad
\mathfrak H_{K,t}^{\mathrm{adm},q_B}
=\{h:\underline p_{K,t}^{\mathrm{adm},q_B}(h)\ge p_{\min}^{\mathrm{adm}}\},
\]

where \(p_{\min}^{\mathrm{adm}}>0\) is frozen and \(\underline p_{K,t}^{\mathrm{adm},q_B}(h)\) is an analytic or simultaneously valid lower bound for \(\inf_{\theta\in\Theta_K}p_K^{\mathrm{adm},q_B}(\theta,h)\). An admission-corrected full-stream claim is permitted only on \(\mathfrak H_{K,t}^{\mathrm{adm},q_B}\). Under \(q_{\mathrm{FA}}\), threshold selection disappears but nomination and evidence readiness remain part of admission. A never-nominated or otherwise unsupported history yields a working posterior or no update. Non-admitted candidates inside \(\mathfrak E_t^B\) may enter the independent audit; objects outside that universe are outside both certificates unless exhaustive coverage or a verified envelope bound extends them.

Conditioning only on the threshold comparison while treating nomination as fixed requires a separately stated conditional-design result. For a jointly admitted evidence set, the contract supplies its joint admission probability; products of one-event corrections are valid only under a declared conditional factorization. Admission may be ignored only under a stated conditional-ignorability result. Without either condition and the support bound, the result is called an admission-conditioned working posterior and no full-stream calibration claim is made. Tempered or source-weighted likelihoods are called generalized Bayesian updates unless derived from a coherent joint source model. The effective posterior \(q_{K,t}^{\mathrm{eff}}\) equals the valid accepted update when one exists and the valid prior otherwise; an invalid bucket is excluded from \(\mathcal K_t^{\mathrm{bel}}\).

For bounded retrieval ranking, let \(s_{(j),t}^{\mathrm{ret}}\) be the external contract score at initial rank \(j\), \(P_t\) the pack boundary, and \(\varepsilon_s>0\). Define

\[
c_t^{\mathrm{pack}}=
\begin{cases}
1,&P_t=N_t,\\
\mathrm{clip}_{[0,1]}\!\left(
\dfrac{s_{(P_t),t}^{\mathrm{ret}}-s_{(P_t+1),t}^{\mathrm{ret}}}
{\max\{|s_{(P_t),t}^{\mathrm{ret}}|,|s_{(P_t+1),t}^{\mathrm{ret}}|,\varepsilon_s\}}
\right),&P_t<N_t.
\end{cases}
\]

For raw correction \(d_{i,t}^{\mathrm{raw}}\), independent reliability \(r_{i,t}^{\mathrm{corr}}\in[0,1]\), and frozen scales \(0\le\lambda_{\min}\le\lambda_{\max}\),

\[
\lambda_{i,t}^{\mathrm{el}}=r_{i,t}^{\mathrm{corr}}\,
[\lambda_{\min}+(\lambda_{\max}-\lambda_{\min})(1-c_t^{\mathrm{pack}})],
\quad
\Delta_{i,t}^{\mathrm{rank}}=
\mathrm{clip}_{[-\Delta_{\max},\Delta_{\max}]}
(\lambda_{i,t}^{\mathrm{el}}d_{i,t}^{\mathrm{raw}}),
\]

and \(s_{i,t}^{\mathrm{final}}=\mathrm{clip}_{[0,1]}(s_{i,t}^{\mathrm{ret}}+\Delta_{i,t}^{\mathrm{rank}})\). Reliability is zero unless an accepted Bayesian, residual, or versioned graph path generated the correction. It remains mandatory when certainty modulation is disabled. The rank operator is after external retrieval and before packing; it does not alter the scored law or its calibration. Any probability-calibration map binds the complete nomination and gating fingerprint under which it was fitted.

Let \(R_{K,t}\) be a declared changepoint run-length state and \(Y_{K,t}\in\{0,1\}\) the currently available usefulness outcome. During a frozen warm-up of \(n_{\mathrm{warm}}\) outcomes, estimate \(m_{K,t}^{s}\) by the ordinary running mean and hold cumulative state at zero. Thereafter, with \(0<\eta_s<1\), update the slow reference and two-sided cumulative state by

\[
\begin{aligned}
m_{K,t}^{s}&=(1-\eta_s)m_{K,t-1}^{s}+\eta_sY_{K,t},\\
C_{K,t}^{+}&=\max\!\left(0,C_{K,t-1}^{+}+Y_{K,t}-m_{K,t-1}^{s}-\delta_{\mathrm C}\right),\\
C_{K,t}^{-}&=\min\!\left(0,C_{K,t-1}^{-}+Y_{K,t}-m_{K,t-1}^{s}+\delta_{\mathrm C}\right).
\end{aligned}
\]

The combined trigger is

\[
J_{K,t}^{\mathrm{cp}}=\mathbf1\!\left[
d_{K,t}^{\mathrm{cool}}=0\ \text{and}\
\left(P(R_{K,t}=0\mid\mathfrak h_t)\ge\gamma_{\mathrm{cp}}
\ \text{or}\ C_{K,t}^{+}\ge h_{\mathrm C}
\ \text{or}\ -C_{K,t}^{-}\ge h_{\mathrm C}\right)
\right].
\]

A trigger resets the affected posterior and monitor onto the triggering outcome, starts a frozen cooldown, and invokes the Section 8 dependency closure and its \(\mathsf B_{\mathcal D}\) and \(\mathsf I_{\mathcal D}\) operators, invalidating affected posterior and residual certificates and incrementing posterior-predictive, residual, and graph versions together. It also expands the bounded frontier and queues slow recalibration. A monitor updated only by admitted evidence detects changepoints in that admission-conditioned process; under frontier-all it still excludes non-nominated and unavailable evidence. It supports a full-stream regime claim only when the complete admission model or independent audit stream is incorporated. Exact run-length support grows with history; a fixed-resource implementation must declare truncation, pruning, or a finite-state approximation and report its approximation error. The cumulative state is constant-size; the capped run-length update is linear in retained support.

Conditional on the inactive candidate set, candidates enter a shadow audit independently of their activation scores with \(J_t^{\mathrm{audit}}(e)\sim\mathrm{Bernoulli}(\pi_{\mathrm{audit}})\) under a frozen schedule. If accepted candidates exceed the capacity \(N_{\mathrm{audit}}^{\max}\), a frozen uniform reservoir subsamples them and records each final inclusion probability; audit estimators use the corresponding design weights.

Let \(\mathsf Q_t^{\mathrm{local}}\) be the complete scored law obtained by applying \(\mathfrak F_R\) to the posterior-predictive base from ordinary frontier updates. For audited inactive candidate \(e\), let \(\mathsf Q_t^{\mathrm{expanded}}(e)\) be the complete scored law obtained after adding that candidate's as-of evidence in the shadow state and then rerunning the same posterior-predictive and residual policy. Define normalized Jensen--Shannon divergence, with natural logarithms,

\[
D_{\mathrm{omit}}(P,Q)=
\frac{\mathrm{KL}(P\|M)+\mathrm{KL}(Q\|M)}{2\log 2},
\qquad M=\tfrac12(P+Q),
\]

which lies in \([0,1]\) for probability laws on \((\mathcal Z_H,\mathscr A_H)\). Under the frozen audit design law \(P_{\mathrm{audit},K,t}\), let

\[
\Delta_{K,t}^{\mathrm{omit}}
=\mathbb E_{e\sim P_{\mathrm{audit},K,t}}
\!\left[D_{\mathrm{omit}}(\mathsf Q_t^{\mathrm{local}},\mathsf Q_t^{\mathrm{expanded}}(e))\right].
\]

The predeclared design-weighted procedure \(\mathfrak U_{\mathrm{omit}}^{\mathrm{seq}}(\alpha_{\mathrm{omit}})\) provides simultaneous sequential coverage over audited buckets, candidate expansions, and repeated audit decisions. If \(\mathfrak K_t^{\mathrm{audit}}\) is the set of buckets with effective audit support, define

\[
U_t^{\mathrm{omit}}=
\max_{K\in\mathfrak K_t^{\mathrm{audit}}}
\mathfrak U_{\mathrm{omit}}^{\mathrm{seq}}(\alpha_{\mathrm{omit}})
[\Delta_{K,t}^{\mathrm{omit}}].
\]

If that set is empty, no certificate is reported. Selective locality is certified only for the declared audit population while \(U_t^{\mathrm{omit}}\le\epsilon_{B,\mathrm{omit}}\); a universal claim additionally requires exhaustive audit coverage or a verified continuity or envelope bound. A plug-in divergence, unweighted capped sample, or pointwise interval is not a certificate. Activation, nomination, evidence readiness, sharing, audit inclusion probability, provenance, horizon, posterior version, and changepoint state are logged. Publication checks the fixed-reference residual-motion certificate, then atomically replaces the posterior, posterior key, dependent residual state, graph version, and epoch; readers observe either the old complete version or the new complete version. Posterior storage has a declared capacity and eviction rule; eviction removes reuse eligibility but does not erase immutable audit provenance.

## Runtime Packet

The compressed runtime state is:

\[
X_t=\chi(C_t,\mathcal M_t,G_t,\sigma_t)\in\mathcal X_{\mathrm{ctx}}.
\]

The packet space is:

\[
\mathcal Y_{\mathrm{pkt}}
=\mathcal N_{\mathrm{mem}}
\times\mathcal E_{\mathrm{graph}}
\times\mathcal L_{\mathrm{lane}}
\times\mathcal C_{\mathrm{compact}}
\times\mathcal M_{\mathrm{mode}}
\times\mathcal U_{\mathrm{control}}.
\]

With separately declared \(q_Y,d_Y,\Pi_Y\), and clipping in \(\mathcal V_Y\):

\[
y\oplus_Yr=
\begin{cases}
y,&r=0,\\
d_Y(\Pi_Y(q_Y(y)+\mathrm{clip}_{\delta_Y}(r))),&r\neq0.
\end{cases}
\]

The maps and prediction are type-compatible:

\[
B_Y:\mathcal X_{\mathrm{ctx}}\to\mathcal Y_{\mathrm{pkt}},
\quad
R_Y:\mathcal X_{\mathrm{ctx}}\to\mathcal V_Y,
\quad
\widehat{\mathbf y}_{t+1}=B_Y(X_t)\oplus_YR_Y(X_t).
\]

## Sensitivity and Causality

Model fuzzing uses the partial map:

\[
\mathcal F_{i,\epsilon}^{(r)}:\mathcal E^k\rightharpoonup\mathcal E^k
\]

and measures:

\[
\Delta_g^{\mathrm{model}}=
d_g(g(\mathcal O_\theta(C_t)),g(\mathcal O_\theta(\mathcal F_{i,\epsilon}^{(r)}(C_t)))).
\]

The validation law is supported only where the partial perturbation is defined.

This is model sensitivity. Causal effects use a separate SCM \(\mathfrak M=(U,V,F,P_U)\):

\[
\Delta_Y^{\mathrm{causal}}(v';P_{\mathrm{ref}})=
D_Y^{\mathrm{law}}(P_{\mathfrak M}(Y\mid do(V_j=v')),P_{\mathrm{ref}}(Y)).
\]

The reference law is declared. This is an effect magnitude, not a signed effect. The symbol \(do\) is never applied directly to a graph perturbation.

For a finite non-empty distinction set \(\mathcal D_t\), let \(\Theta_\Gamma^{-d}\) be the predeclared ablation of distinction \(d\), fitted on design data under the same protocol. Define the paired proper-risk effect under the confirmation-generating law and, after freezing every design, its estimate:

\[
\Delta_{\mathrm{pred}}(d)=
\mathcal R_{\mathrm{prop}}^{P_{\mathrm{conf}}}(\Theta_\Gamma^{-d})
-\mathcal R_{\mathrm{prop}}^{P_{\mathrm{conf}}}(\Theta_\Gamma),
\qquad
\widehat\Delta_{\mathrm{pred}}(d)=
\widehat{\mathcal R}_{\mathrm{prop}}^{\mathcal S_{\mathrm{conf}}}(\Theta_\Gamma^{-d})
-\widehat{\mathcal R}_{\mathrm{prop}}^{\mathcal S_{\mathrm{conf}}}(\Theta_\Gamma),
\]

\[
s_{\mathrm{eff}}^{\mathrm{pred}}=
\frac{|\{d:\mathrm{LCB}_{\mathrm{sim}}[\Delta_{\mathrm{pred}}(d)]
>\eta_{\mathrm{pred}}\}|}{|\mathcal D_t|}.
\]

The simultaneous bounds cover the declared family. Confirmation outcomes classify but do not refit or regenerate distinctions. This ratio is predictive, not causal. If \(\mathcal I_{\mathrm{eff}}^{\mathrm{causal}}(Y,\eta_Y)\) is identified by randomized or otherwise valid interventions, define separately

\[
s_{\mathrm{eff}}^{\mathrm{causal}}=
\frac{|\mathcal I_{\mathrm{eff}}^{\mathrm{causal}}(Y,\eta_Y)|}{|\mathcal D_t|}.
\]

## Lumpability and Anti-Pigeon

For \(\pi:\mathcal E\to\mathcal S_{\mathrm{abs}}\):

\[
\varepsilon_{\mathrm{lump}}^\star(\pi)=
\sup_{C,C'\in\mathfrak C_{\mathrm{adm}}:h_\pi(C)=h_\pi(C')}
D(P_\star(Y\mid C),P_\star(Y\mid C')).
\]

A non-empty bucket \(K\) retains a concrete traceability frame \(\bar e_K\in K\). Let \(\mathrm{anc}(C)\) be the terminal anchor frame of context \(C\) and define:

\[
\mathfrak C_K=\{C\in\mathfrak C_{\mathrm{adm}}:\mathrm{anc}(C)\in K\}.
\]

When \(\mathfrak C_K\neq\varnothing\), maintain \(\varnothing\neq\mathcal R_C(K)\subseteq\mathfrak C_K\). The context-conditional future-diameter, true restricted audit diameter, and estimator are:

\[
D_K^\star(\pi)=\sup_{C,C'\in\mathfrak C_K}
D(P_\star(Y\mid C),P_\star(Y\mid C')),
\qquad
D_K^{\mathrm{audit},\star}=
\max_{R,R'\in\mathcal R_C(K)}D_{R,R'}^{K,\star},
\]

\[
\widehat D_K^\star=
\max_{R,R'\in\mathcal R_C(K)}
\widehat D_{R,R'}^{K,\star}.
\]

With a context metric, an audit may satisfy:

\[
\sup_{C\in\mathfrak C_K}\min_{R\in\mathcal R_C(K)}d_C(C,R)\le\delta_K.
\]

Coverage alone does not certify unseen futures. If \(D\) obeys the triangle inequality and \(\overline L_K^{\mathrm{cert}}\) is either an analytic uniform bound or a simultaneous upper confidence bound satisfying

\[
D(P_\star(Y\mid C),P_\star(Y\mid R))
\le\overline L_K^{\mathrm{cert}}d_C(C,R),
\]

then a simultaneous certificate is:

\[
D_K^{\mathrm{cert},\star}=
\max_{R,R'\in\mathcal R_C(K)}
\mathrm{UCB}_{\mathrm{sim}}[D_{R,R'}^{K,\star}]
+2\overline L_K^{\mathrm{cert}}\delta_K.
\]

The deterministic inequality is \(D_K^\star\le D_K^{\mathrm{audit},\star}+2\overline L_K^{\mathrm{cert}}\delta_K\). The simultaneous procedure jointly covers every selected audit pair and any estimated continuity bound; an uncertainty-free plug-in estimate cannot certify. The model diameter \(D_K^{\mathrm{mdl}}(\Theta_\Gamma)\) is reported separately and cannot certify the abstraction. Without exhaustive coverage or a verified continuity bound, a small \(\widehat D_K^\star\) supports only an observed-sample claim. If \(\mathfrak C_K=\varnothing\), the bucket is unaudited and has no certificate.

Observed regime divergence uses \(\zeta\), not \(\rho\):

\[
D_{i,a,b}^{\mathrm{reg}}=
D(P_\star(Y\mid C_i,\zeta_a),P_\star(Y\mid C_i,\zeta_b)).
\]

This is evaluated only on common context support across regimes; otherwise a declared overlap and transport model is required. It is predictive evidence unless \(\zeta\) is causally identified.

## Abstraction Compatibility

For \(\mathcal G_t^A=(V_t^A,E_t^A)\), node \(i\) has \(\mathsf Q_i\in\mathcal P(\mathcal Y_i)\). For edge \(e=\{i,j\}\), measurable maps into \(\mathcal Y_e\) induce pushforwards:

\[
\mathsf r_{ie}\mathsf Q_i=(g_{ie})_*\mathsf Q_i,
\qquad
\delta_e(\mathsf Q)=D_e(\mathsf r_{ie}\mathsf Q_i,\mathsf r_{je}\mathsf Q_j).
\]

The network statistic is:

\[
\Delta_{\mathrm{comp}}(\mathsf Q)=
\begin{cases}
0,&E_t^A=\varnothing,\\
\max_{e\in E_t^A}\mathrm{UCB}_{\mathrm{sim}}[\delta_e(\mathsf Q)],&E_t^A\neq\varnothing.
\end{cases}
\]

The confidence procedure covers the inspected or adaptively selected edge family. Changes to a dependent map, edge set, threshold, or simultaneous bound increment the affected cache epoch.

This is a sheaf-inspired compatibility scaffold, not a sheaf-theoretic construction unless the assigned spaces and comparison maps instantiate the required identity and composition laws. A local reconciliation returns a forecast tuple:

\[
(\overline{\mathsf Q}_i)_{i\in\mathcal N}
\in\arg\min_{(\widetilde{\mathsf Q}_i)_{i\in\mathcal N}\in\mathfrak Q_{\mathcal N}}
\left[
\sum_{i\in\mathcal N}a_iD_i(\widetilde{\mathsf Q}_i,\mathsf Q_i)
+\lambda_A\sum_{e\in E^+(\mathcal N)}w_e\delta_e(\widetilde{\mathsf Q})
\right].
\]

Here \(\mathfrak Q_{\mathcal N}\subseteq\prod_{i\in\mathcal N}\mathcal P(\mathcal Y_i)\) is declared, and each \(D_i:\mathcal P(\mathcal Y_i)^2\to[0,+\infty]\) is a frozen fidelity divergence with \(D_i(Q,Q)=0\). Exact attainment requires compact feasibility and lower semicontinuity or another stated existence theorem; otherwise the contract returns an approximate tuple and optimality gap.

A predictive sheaf snap selects from a finite predeclared local family:

\[
\Xi_A^{\mathrm{cand}}
\in\arg\min_{\Xi'\in\mathfrak S_t(\Xi_A^{(v)};\mathcal N)}
\Psi_t(\Xi';\Xi_A^{(v)}).
\]

The score includes design-block priority risk, candidate-induced compatibility defect, edit distance, snap cost, and unresolved comparison-obligation burden. Every term is finite and normalized to a common utility scale or converted to it by its coefficient. The externally fixed \(\mathfrak O_t\) prevents edge deletion from making an obligated comparison disappear. Here \(\Theta_\Gamma[\Xi']\) is the complete induced candidate, including any required local change to \(\pi\), node laws, keys, and certificates, all fitted on \(D_t^{\mathrm{design}}\). On disjoint \(D_t^{\mathrm{conf}}\), \(A_t^{\mathrm{snap}}=1\) exactly when the joint confidence procedure establishes gain net of resource cost, proper-score non-inferiority, affected-bucket Anti-Pigeon bounds, affected retained/new-edge compatibility bounds, and bounded unresolved burden. Maxima over empty affected sets are zero. Accepted structures atomically publish graph, abstraction map, bumped epochs, and targeted memory invalidation; rejected candidates leave all four unchanged. This is predictive graph revision, not causal-edge promotion.

Under finite-dimensional embeddings and linear restrictions only:

\[
(\partial_Ax)_e=R_{ie}x_i-R_{je}x_j,
\qquad L_A=\partial_A^*\partial_A.
\]

Then \(\ker L_A=\ker\partial_A\). If \(\lambda_{\max}(L_A)>0\), fixed-step refinement converges to the orthogonal projection onto that kernel when \(0<\eta<2/\lambda_{\max}(L_A)\); if \(L_A=0\), no update is required.

## Staged Refinement and Priority

Starting with certified reuse, repeated or reordered slow-path stages are represented by:

\[
S_t^{(0)}=\mathcal U_0(S_{t^-}),
\qquad
S_t^{(n)}=\mathcal U_{r_n}(S_t^{(n-1)}),
\quad r_n\in\{1,2,3,4,5\}.
\]

Every invocation has a strictly positive conservative cost bound and every repeat is charged. A strict deadline additionally requires interruptibility and a worst-case reserve or deterministic stop. The reported depth is the maximum stage index reached; the complete sequence, actual cumulative cost, overruns, and stopping reason are also reported.

The coupled learning state visible to readers is

\[
\Sigma_t=(\mathcal C_{B,t^-},\mathcal C_{R,t^-},\mathbf v_t,\Xi_A^{(v)},G_t).
\]

Within each evidence epoch \(j\), the frozen stability contract enforces

\[
N_{\mathrm{pub}}(j)\le B_{\mathrm{pub}},
\qquad
N_{\mathrm{inv}}(j)\le B_{\mathrm{inv}},
\]

with finite budgets, hysteresis, cooldowns, and deterministic conflict ordering. Budget exhaustion freezes further dependent publication and routes the region to slow audit. This bounds same-epoch thrashing but is not a convergence result across a drifting stream.

Priority-normalized evaluation weights are:

\[
\widetilde w_t=
\frac{w_{\mathrm{pri}}(p_t^{\mathrm{pri}})}
{\sum_{u=1}^{T}w_{\mathrm{pri}}(p_u^{\mathrm{pri}})},
\qquad
G_{a\rightarrow b}^{\mathrm{pri}}=\sum_t\widetilde w_t(L_t^{[q_a]}-L_t^{[q_b]}).
\]

## Governing Objective

At fixed \(\Gamma_{\Delta_\tau}\), let \(\Theta_\Gamma=(\mathsf Q_\theta,B,\pi,\mathcal C_A,\mathcal C_R,\mathcal C_E,\mathcal C_B,\Xi_R,\Xi_B,\Xi_A^{(v)})\). The frozen \(\Lambda_{\mathrm{eval}}\) includes generating laws \(P_{\mathrm{obj}},P_{\mathrm{conf}}\), realized blocks \(\mathcal S_{\mathrm{obj}},\mathcal S_{\mathrm{conf}}\), \(P_\star\), domains, metrics, complete diagnostics or finite admissible classes and fitting rules, targets, thresholds, weights, \(g_{\mathrm{pred}}\), packet target/loss, priority model, regime-shift rule, \(\lambda_{\mathrm{rep}}\ge0\), cost definition, confidence rules, map-validity tests, snap candidate, obligation, and publication rules. It also freezes Bayesian candidate-universe and frontier caps, the frontier-all or selective policy, nomination and evidence-readiness rules, activation maps and thresholds, the joint evidence-and-outcome family and its displayed marginal identities, source and complete admission models, admission-support floor and simultaneous lower-bound procedure, posterior-predictive kernels, mixture weights and template map, posterior-sharing certificates, proposal-only group-comparison split prior, practical-equivalence width, support, split and equivalence thresholds, statistics, borrowing cap, and group cap, audit design law and reservoir, \(D_{\mathrm{omit}}\), \(\mathfrak U_{\mathrm{omit}}^{\mathrm{seq}}\), changepoint run-length cap, warm-up, cumulative-detector parameters, cooldown and reset rule, component-sensitive law and template motion certificates with propagated approximation-error budgets, dependency-closure versioning, atomic publication, and coupled-state publication/invalidation budgets. Let \(\mathfrak h_t\in\mathfrak H_t\) be the observable prediction history excluding the next outcome, \(c_k(\mathfrak h_t)=C_t\), and \(S_{\Theta,t^-}=\mathrm{Replay}_\Theta(\mathfrak h_t)\). The laws \(P_{\mathrm{obj}}\) and \(P_{\mathrm{conf}}\) are over \((\mathfrak h_t,Z_{t+1})\), so candidate-specific cache, posterior, epoch, changepoint, and confidence state is reconstructed from the same raw history. For EventFrame, the final scored output is the Section 5 bundle

\[
\mathcal O_{\Theta_\Gamma}(C_t;S_{\Theta_\Gamma,t^-})=\mathcal O_t^R,
\qquad
\mathsf Q_{\Theta_\Gamma}(\cdot\mid C_t;S_{\Theta_\Gamma,t^-})=\mathsf Q_t^R(\cdot\mid C_t),
\]

where Section 6 first supplies the effective posterior family, Section 5 constructs \((\mathsf Q_t^0,b_t^0)\), and the residual policy acts after that base. The frozen Bayesian contract also declares the pooled-evidence discount, revision-valid evidence classes, shock and changepoint action table, and atomic invalidation rule; these belief controls can change the posterior-predictive base and therefore the proper-scored law. Separately, the elastic rank scales and cap, independent correction-reliability rule, and complete calibration fingerprint are search-order controls outside \(\mathcal O_{\Theta_\Gamma}\); they cannot change the proper-scored law. Define \(h_\pi(C)=(\pi^k(C),s_\pi(C))\). The predictor, baseline, posterior-predictive maps, and cache keys must factor through \(h_\pi\), and the side information is charged to \(\mathcal C_{\mathrm{rep}}\):

\[
\mathcal R_{\mathrm{pri}}^D(\Theta_\Gamma)=
\frac{\mathbb E_{(\mathfrak h_t,Z)\sim D}
[w_{\mathrm{pri}}(p^{\mathrm{pri}}(c_k(\mathfrak h_t);S_{\Theta_\Gamma,t^-}))\mathcal A_{\mathrm{post}}(\mathcal O_{\Theta_\Gamma}(c_k(\mathfrak h_t);S_{\Theta_\Gamma,t^-}),Z)]}
{\mathbb E_{\mathfrak h_t\sim D}[w_{\mathrm{pri}}(p^{\mathrm{pri}}(c_k(\mathfrak h_t);S_{\Theta_\Gamma,t^-}))]},
\quad D\in\{P_{\mathrm{obj}},P_{\mathrm{conf}}\}.
\]

The corresponding history-aware unweighted proper risk is

\[
\mathcal R_{\mathrm{prop}}^D(\Theta_\Gamma)
=\mathbb E_{(\mathfrak h_t,Z)\sim D}
\left[S_{\mathrm{prop}}\!\left(
\mathsf Q_{\Theta_\Gamma}(\cdot\mid c_k(\mathfrak h_t);S_{\Theta_\Gamma,t^-}),Z
\right)\right].
\]

Displayed population risks are restricted to designs for which the required expectations are finite. An infinite empirical proper loss gives an infinite guard statistic and is not certifiable unless a probability floor was part of the frozen forecast family and its effect on propriety was stated.

\[
\mathfrak F_{AP}^{\Gamma,\star}=\lbrace\Theta_\Gamma:
D_K^\star(\pi)\le\epsilon_{AP}\ \forall K\in\mathfrak K_\pi^+,\quad
h_\pi\text{ factorization holds},\quad
\mathcal R_{\mathrm{prop}}^{P_{\mathrm{obj}}}(\Theta_\Gamma)
\le\mathcal R_{\mathrm{prop}}^{P_{\mathrm{obj}}}(\Theta_{\Gamma,0})+\epsilon_{\mathrm{prop}}\rbrace,
\]

\[
\mathcal J_\Gamma^{\mathrm{oracle}}=
\inf_{\Theta_\Gamma\in\mathfrak F_{AP}^{\Gamma,\star}}
[\mathcal R_{\mathrm{pri}}^{P_{\mathrm{obj}}}(\Theta_\Gamma)+\lambda_{\mathrm{rep}}\mathcal C_{\mathrm{rep}}(\Theta_\Gamma)].
\]

This is an oracle population benchmark. Operational selection uses a finite predeclared \(\mathfrak G_\Gamma(\mathcal S_{\mathrm{obj}})\). Candidates lacking exhaustive audit coverage or the verified continuity certificate are not certifiable. Define

\[
\widehat{\mathfrak F}_{AP}^{\Gamma}=\left\{\Theta_\Gamma\in\mathfrak G_\Gamma(\mathcal S_{\mathrm{obj}}):
\begin{array}{l}
D_K^{\mathrm{cert},\star}(\pi)\le\epsilon_{AP}\ \forall K\in\mathfrak K_\pi^+,\\
h_\pi\text{ factorization holds},\\
\mathrm{UCB}[\widehat{\mathcal R}_{\mathrm{prop}}^{\mathcal S_{\mathrm{obj}}}(\Theta_\Gamma)
-\widehat{\mathcal R}_{\mathrm{prop}}^{\mathcal S_{\mathrm{obj}}}(\Theta_{\Gamma,0})]
\le\epsilon_{\mathrm{prop}}
\end{array}\right\}.
\]

If this family is non-empty, \(\widehat\Theta_\Gamma\) is the deterministic finite argmin of \(\widehat{\mathcal R}_{\mathrm{pri}}^{\mathcal S_{\mathrm{obj}}}+\lambda_{\mathrm{rep}}\mathcal C_{\mathrm{rep}}\) over it. Otherwise the procedure reports no certified design or uses a separately declared conservative fallback. Candidate selection uses only \(\mathcal S_{\mathrm{obj}}\); final frozen claims use untouched \(\mathcal S_{\mathrm{conf}}\). The samples are generated under \(P_{\mathrm{obj}}\) and \(P_{\mathrm{conf}}\) and use grouped rolling-origin evaluation, an overlap/horizon/label-delay embargo, and as-of replay. Cross-resolution comparisons use common raw histories and the same external target. Empirical certification does not imply oracle attainment beyond the certificate's assumptions.

The pre-outcome priority rule and all preprocessing are fitted before each evaluated block and frozen independently of candidates. Setting \(w_{\mathrm{pri}}\equiv1\) recovers the unweighted objective. Finite-sample constraints use preregistered one-sided confidence procedures, clustered inference for overlapping contexts, and sequentially valid methods under repeated monitoring.

## Finite-State Descent

For a finite candidate set \(\mathfrak S\), fixed evaluation distribution, and potential:

\[
\Phi(s)=\sum_{t=1}^{T}\widetilde w_t\mathcal A_{\mathrm{post},t}^s
+\lambda_{\mathrm{rep}}\mathcal C_{\mathrm{rep}}(s),
\]

accept only moves satisfying:

\[
\Phi(s')\le\Phi(s)-\delta,\qquad\delta>0.
\]

Then no state is revisited and at most \(|\mathfrak S|-1\) moves are accepted. This statement does not apply under drift or changing candidate states.
