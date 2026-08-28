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
| \(\mathfrak h_t,c_k,\mathrm{Replay}_\Theta\) | history, extractor, map | observable prediction history, context extraction, and candidate-specific as-of state replay |
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
| \(\Xi_R\) | typed contract tuple | complete residual representation, kernel, key, and gate contract |
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

For the forecast issued at \(t\), the point residual is defined only on an in-horizon event:

\[
r_{t,H}^{E,\mathrm{obs}}=q_E(e_{t+1})-q_E(b_t),
\qquad 0<\tau(e_{t+1})-\tau(e_t)\le H.
\]

It is undefined when \(Z_{t+1}=\varnothing\). A later event cannot retroactively label the expired forecast; no-event observations may instead update the distributional kernel through the proper score.

A distributional residual may be learned on either outcome branch through a declared measurable estimator:

\[
\rho_H^Q:\mathcal P(\mathcal Z_H)\times\mathcal Z_H\to\mathbb H_d^Q,
\qquad
r_{t,H}^{Q,\mathrm{obs}}=\rho_H^Q(\mathsf Q_B(\cdot\mid C_t),Z_{t+1}).
\]

It is defined at \(\varnothing\), and cache provenance distinguishes it from \(r_{t,H}^{E,\mathrm{obs}}\). Let \(\mathcal M_R=\{\varnothing,E,Q,EQ\}\), \(\mathcal V_R=\mathbb H_d^E\times\mathbb H_d^Q\times\mathcal M_R\), and \(\mathbf r=(r^E,r^Q,m)\in\mathcal V_R\). The mode is authoritative about component presence. Point and law components have independent semantics; a joint record requires forward validation of the complete output bundle and does not assert that its components are equal.

## Residual Caches

Both caches are reconstructed as of \(S_{t^-}\); no later entry, outcome, confidence update, epoch, or audit result may be read. The general cache is:

\[
\mathcal C_{R,t^-}=\{(\kappa_i,\mathbf r_i,c_i,n_i,t_i,v_i,\mu_i,H_i,s_i)\}_{i=1}^{N_t},
\quad
\kappa:\mathcal E^k\to\mathcal K_R,
\quad \mathbf r_i\in\mathcal V_R.
\]

For \(N_t>0\), \(j_t\) is the deterministic nearest-key selection. Let \(J_t^R\) indicate that distance, confidence, effective support, age, epoch, horizon equality \(H_i=H\), compatibility margin, and provenance gates all pass; set it to zero when the cache is empty. Then

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
\times\mathcal S_{\mathrm{prov}}.
\]

For \(k_t=\alpha(C_t)\), bind the entry only when it exists, including provenance \(s_{k_t}\). Let \(J_t^A\) indicate that confidence, effective support, age, epoch, horizon equality \(H_{k_t}=H\), compatibility-margin, and provenance checks pass; set it to zero when the key is absent. The exact-to-general selector is:

\[
\mathbf r_t^{\mathrm{use}}=
\begin{cases}
\mathbf r_{k_t},&J_t^A=1,\\
\mathbf r_t^*,&J_t^A=0\text{ and }J_t^R=1,\\
\mathbf 0_R,&\text{otherwise.}
\end{cases}
\]

This indicator distinguishes an accepted zero residual from a cache miss. To obtain a corrected forecast law, declare:

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
\,\mathsf Q_B(dz\mid C_t).
\]

In particular,

\[
\begin{aligned}
\mathsf Q_t^{(\mathbf r)}(\{\varnothing\}\mid C_t)
={}&\mathfrak K_H^Q(\bar r^Q)(\varnothing,\{\varnothing\})
\mathsf Q_B(\{\varnothing\}\mid C_t)\\
&+\int_{\mathcal Z_H^+}\mathfrak K_H^Q(\bar r^Q)(z,\{\varnothing\})
\,\mathsf Q_B(dz\mid C_t).
\end{aligned}
\]

Let \(\mathrm{lift}_H:\mathcal E\times\mathcal Z_H^+\to\mathcal E\) align a corrected event template with the marked decision. Set \(\hat e_t^H(\mathbf r)=\varnothing\) when \(d_H(\mathsf Q_t^{(\mathbf r)})=\varnothing\), and otherwise set \(\hat e_t^H(\mathbf r)=\mathrm{lift}_H(b_t\oplus_E\bar r^E,d_H(\mathsf Q_t^{(\mathbf r)}))\). Then \(\mathcal O_t(\mathbf r)=(\mathsf Q_t^{(\mathbf r)},\hat e_t^H(\mathbf r))\). The typed pair keeps law and auxiliary-template semantics separate; \(d_H\) and \(\mathrm{lift}_H\) enforce mark/time coherence only. The selected candidate is returned only if its pre-observation gate passes from \(S_{t^-}\); otherwise \(\mathcal O_t(\mathbf 0_R)\) is returned. Point-only records cannot support a proper-score claim; law-only records cannot claim auxiliary-field correction. Confidence updates include only outcomes already available, use clustered or effective support for overlapping contexts, and use sequentially valid inference when monitored repeatedly.

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

Priority-normalized evaluation weights are:

\[
\widetilde w_t=
\frac{w_{\mathrm{pri}}(p_t^{\mathrm{pri}})}
{\sum_{u=1}^{T}w_{\mathrm{pri}}(p_u^{\mathrm{pri}})},
\qquad
G_{a\rightarrow b}^{\mathrm{pri}}=\sum_t\widetilde w_t(L_t^{[q_a]}-L_t^{[q_b]}).
\]

## Governing Objective

At fixed \(\Gamma_{\Delta_\tau}\), let \(\Theta_\Gamma=(\mathsf Q_\theta,B,\pi,\mathcal C_A,\mathcal C_R,\mathcal C_E,\Xi_R,\Xi_A^{(v)})\). The frozen \(\Lambda_{\mathrm{eval}}\) includes generating laws \(P_{\mathrm{obj}},P_{\mathrm{conf}}\), realized blocks \(\mathcal S_{\mathrm{obj}},\mathcal S_{\mathrm{conf}}\), \(P_\star\), domains, metrics, complete diagnostics or finite admissible classes and fitting rules, targets, thresholds, weights, \(g_{\mathrm{pred}}\), packet target/loss, priority model, regime-shift rule, \(\lambda_{\mathrm{rep}}\ge0\), cost definition, confidence rules, map-validity tests, and snap candidate, obligation, and publication rules. Let \(\mathfrak h_t\in\mathfrak H_t\) be the observable prediction history excluding the next outcome, \(c_k(\mathfrak h_t)=C_t\), and \(S_{\Theta,t^-}=\mathrm{Replay}_\Theta(\mathfrak h_t)\). The laws \(P_{\mathrm{obj}}\) and \(P_{\mathrm{conf}}\) are over \((\mathfrak h_t,Z_{t+1})\), so candidate-specific cache, epoch, and confidence state is reconstructed from the same raw history. Define \(h_\pi(C)=(\pi^k(C),s_\pi(C))\). The predictor, baseline, and cache keys must factor through \(h_\pi\), and the side information is charged to \(\mathcal C_{\mathrm{rep}}\):

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
