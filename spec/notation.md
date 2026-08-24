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
| \(\nu(e)\) | event-mark set | event identity/type extractor |
| \(\tau(e)\) | temporal set | event-time extractor |
| \(Z_{t+1}\) | \(\mathcal Z_H\) | observed marked time or no-event outcome |
| \(a(x)\) | time | availability time of datum or state object \(x\) |
| \(\mathscr F_t^{\mathrm{pred}},S_{t^-}\) | information, state | information and mutable state available immediately before prediction |
| \(P_{\mathrm{obj}},P_{\mathrm{conf}}\) | laws or samples | design/selection distribution and untouched confirmation distribution |
| \(P_\star(Y\mid C)\) | conditional law | externally fixed target conditional law |
| \(\mathsf Q_\theta\) | probability kernel | predictive distribution over \(\mathcal Z_H\) |
| \(\mathcal O_\theta(C)\) | \(\mathcal P(\mathcal Z_H)\times\mathcal E\) | typed forecast-law and point-summary output bundle |
| \(\mathcal L_{\mathrm{pred}}\) | extended real | untransformed proper post-observation predictive loss |
| \(\overline{\mathcal L}_{\mathrm{pred}}\) | \([0,1]\) | preregistered bounded transformation used inside system action |
| \(\mathcal L_{\mathrm{event}}^H\) | \([0,1]\) | bounded event-aware timing diagnostic |
| \(\mathcal R_{\mathrm{pre}}\) | \([0,1]\) | pre-observation admissibility risk |
| \(\mathcal A_{\mathrm{post}}\) | \([0,1]\) | post-observation realized event action |
| \(\mathsf Q_B\) | \(\mathcal E^k\to\mathcal P(\mathcal Z_H)\) | baseline probability-law predictor |
| \(B\) | \(\mathcal E^k\to\mathcal E\) | baseline point predictor |
| \(\mathscr H\) | finite-dimensional Hilbert space | carrier for operator representation |
| \(\mathbb H_d\) | vector space | self-adjoint operators on \(\mathscr H\) |
| \(\mathcal Q_{E,\mathrm{adm}}\) | closed subset of \(\mathbb H_d\) | admissible event representations |
| \(q_E,d_E\) | encoder, decoder | event representation maps |
| \(\Pi_E\) | deterministic projection selection | projection to \(\mathcal Q_{E,\mathrm{adm}}\) |
| \(\delta_E\) | positive real | event-residual clipping radius |
| \(\oplus_E\) | \(\mathcal E\times\mathbb H_d\to\mathcal E\) | event residual composition |
| \(\mathcal C_{R,t^-}\) | finite cache | as-of general residual cache |
| \(\mathcal C_{A,t^-}\) | partial map | as-of exact action-key residual cache |
| \(J_t^R,J_t^A\) | \(\{0,1\}\) | general- and exact-cache acceptance indicators |
| \(J_t^A\) | \(\{0,1\}\) | exact-cache acceptance indicator |
| \(r_t^{\mathrm{use}}\) | \(\mathbb H_d\) | exact-to-general selected residual |
| \(\mathfrak K_E\) | kernel-valued map | residual-induced Markov kernel on \(\mathcal Z_H\) |
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
| \(\Xi_A\) | typed structure tuple | candidate compatibility graph and comparison maps |
| \(\Lambda_{\mathrm{eval}}\) | fixed contract tuple | externally frozen domains, metrics, targets, thresholds, weights, and validation procedures |
| \(\mathcal U_0,\ldots,\mathcal U_4\) | staged maps | baseline and selectable refinement operators |
| \(r_n\) | \(\{1,2,3,4\}\) | stage selected at slow-path invocation \(n\) |
| \(d_t(h)\) | \(\{0,\ldots,4\}\) | selected refinement depth on hardware profile \(h\) |
| \(p_t^{\mathrm{pri}}\) | \([0,1]\) | priority assigned from prediction-time information |
| \(w_{\mathrm{pri}}\) | positive function | declared importance weight for priority |
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

The next outcome over horizon \(H\) is:

\[
Z_{t+1}=\begin{cases}
(\nu(e_{t+1}),\tau(e_{t+1})-\tau(e_t)), & \text{event within }H,\\
\varnothing, & \text{no event within }H.
\end{cases}
\]

The forecast and primary loss are:

\[
\mathsf Q_\theta(\cdot\mid C_t)\in\mathcal P(\mathcal Z_H),
\qquad
\mathcal O_\theta(C_t)=
(\mathsf Q_\theta(\cdot\mid C_t),\hat e_\theta(C_t)),
\]

\[
\qquad
\mathcal L_{\mathrm{pred}}(\theta;t)
=S_{\mathrm{prop}}(\mathsf Q_\theta(\cdot\mid C_t),Z_{t+1}).
\]

For a mixed event/no-event logarithmic score, fix a dominating event-branch reference measure \(\mu_H\) and time units. The event branch is a subdensity with respect to \(\mu_H\) whose mass plus \(\mathsf Q_\theta(\{\varnothing\}\mid C_t)\) equals one. The no-event observation is scored by \(-\log\mathsf Q_\theta(\{\varnothing\}\mid C_t)\), not by evaluating an undefined event time. The reference measure and units remain fixed across forecast comparisons.

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

For a candidate bundle \(\widetilde{\mathcal O}=(\widetilde{\mathsf Q},\tilde e)\), before observation:

\[
\mathcal R_{\mathrm{pre}}(\widetilde{\mathcal O}\mid C_t)
=\lambda_a^{\mathrm{pre}}D_{\mathrm{abs}}^{\mathrm{pre}}(\widetilde{\mathcal O},C_t)
+\lambda_c^{\mathrm{pre}}D_{\mathrm{edge}}^{\mathrm{pre}}(\widetilde{\mathcal O},C_t)
+\lambda_u^{\mathrm{pre}}U^{\mathrm{pre}}(\widetilde{\mathcal O}\mid C_t).
\]

The three components lie in \([0,1]\), and their non-negative weights sum to one. Let \(g_{\mathrm{pred}}:\overline{\mathbb R}\to[0,1]\) be preregistered, order-preserving on the declared finite score range, and satisfy \(g_{\mathrm{pred}}(+\infty)=1\). Constant or order-reversing transforms are inadmissible. Define:

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

Every post component lies in \([0,1]\), and the four non-negative post weights sum to one. Thus \(\mathcal A_{\mathrm{post}}\in[0,1]\). The untransformed proper score remains the fitting and forecast-comparison quantity. \(\mathcal A_{\mathrm{post}}\) is undefined before \(Z\) is observed and may not gate the fast path.

## Event Residual Composition

Let \(\mathbb H_d\) be self-adjoint operators with Frobenius norm. Define:

\[
q_E:\mathcal E\to\mathbb H_d,
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

## Residual Caches

Both caches are reconstructed as of \(S_{t^-}\); no later entry, outcome, confidence update, epoch, or audit result may be read. The general cache is:

\[
\mathcal C_{R,t^-}=\{(\kappa_i,r_i,c_i,n_i,t_i,v_i,m_i,s_i)\}_{i=1}^{N_t},
\quad
\kappa:\mathcal E^k\to\mathcal K_R,
\quad r_i\in\mathbb H_d.
\]

For \(N_t>0\), \(j_t\) is the deterministic nearest-key selection. Let \(J_t^R\) indicate that distance, confidence, effective support, age, epoch, compatibility margin, and provenance gates all pass; set it to zero when the cache is empty. Then

\[
r_t^*=\begin{cases}
r_{j_t},&J_t^R=1,\\
0_{\mathbb H_d},&\text{otherwise.}
\end{cases}
\]

The action cache is typed as:

\[
\mathcal C_{A,t^-}:\mathcal K_A\rightharpoonup
\mathbb H_d\times[0,1]\times\mathbb N_0\times\mathcal T
\times\mathbb N_0\times\mathbb R.
\]

For \(k_t=\alpha(C_t)\), bind the entry only when it exists. Let \(J_t^A\) indicate that confidence, effective support, age, epoch, and compatibility-margin checks pass; set it to zero when the key is absent. The exact-to-general selector is:

\[
r_t^{\mathrm{use}}=
\begin{cases}
r_{k_t},&J_t^A=1,\\
r_t^*,&J_t^A=0\text{ and }J_t^R=1,\\
0,&\text{otherwise.}
\end{cases}
\]

This indicator distinguishes an accepted zero residual from a cache miss. To obtain a corrected forecast law, declare:

\[
\mathfrak K_E:\mathbb H_d\to\mathrm{Ker}(\mathcal Z_H),
\qquad
\mathfrak K_E(0)(z,A)=\mathbf 1_A(z),
\]

and define, for measurable \(A\subseteq\mathcal Z_H\) and candidate \(r\in\mathbb H_d\), with \(\bar r=\mathrm{clip}_{\delta_E}(r)\):

\[
\mathsf Q_t^{(r)}(A\mid C_t)=
\int_{\mathcal Z_H}\mathfrak K_E(\bar r)(z,A)
\,\mathsf Q_B(dz\mid C_t).
\]

Let \(\mathcal O_t(r)=(\mathsf Q_t^{(r)},b_t\oplus_E\bar r)\). The same clipped residual controls both components. The selected candidate is returned only if its pre-observation gate passes from \(S_{t^-}\); otherwise the exact baseline \(\mathcal O_t(0)\) is returned. A point-only implementation cannot claim improvement on a proper forecast score. Confidence updates include only outcomes already available, use clustered or effective support for overlapping contexts, and use sequentially valid inference when monitored repeatedly.

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

Coverage alone does not certify unseen futures. If \(D\) obeys the triangle inequality and a verified \(\overline L_K\) satisfies

\[
D(P_\star(Y\mid C),P_\star(Y\mid R))
\le\overline L_Kd_C(C,R),
\]

then a simultaneous certificate is:

\[
D_K^{\mathrm{cert},\star}=
\max_{R,R'\in\mathcal R_C(K)}
\mathrm{UCB}_{\mathrm{sim}}[D_{R,R'}^{K,\star}]
+2\overline L_K\delta_K.
\]

The deterministic inequality is \(D_K^\star\le D_K^{\mathrm{audit},\star}+2\overline L_K\delta_K\), while the simultaneous UCB handles estimation error. The model diameter \(D_K^{\mathrm{mdl}}(\Theta_\Gamma)\) is reported separately and cannot certify the abstraction. Without exhaustive coverage or a verified continuity bound, a small \(\widehat D_K^\star\) supports only an observed-sample claim. If \(\mathfrak C_K=\varnothing\), the bucket is unaudited and has no certificate.

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
\quad r_n\in\{1,2,3,4\}.
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

At fixed \(\Gamma_{\Delta_\tau}\), let \(\Theta_\Gamma=(\mathsf Q_\theta,B,\pi,\mathcal C_A,\mathcal C_R,\mathcal C_E,\Xi_R,\Xi_A)\). The frozen \(\Lambda_{\mathrm{eval}}\) includes \(P_{\mathrm{obj}},P_{\mathrm{conf}},P_\star\), domains, metrics, targets, thresholds, weights, \(\lambda_{\mathrm{rep}}\ge0\), cost definition, confidence rules, and map-validity tests. Define \(h_\pi(C)=(\pi^k(C),s_\pi(C))\). The predictor, baseline, and cache keys must factor through \(h_\pi\), and the side information is charged to \(\mathcal C_{\mathrm{rep}}\):

\[
\mathcal R_{\mathrm{pri}}^D(\Theta_\Gamma)=
\frac{\mathbb E_{(C,Z)\sim D}
[w_{\mathrm{pri}}(p^{\mathrm{pri}}(C;S_{t^-}))\mathcal A_{\mathrm{post}}(\mathcal O_{\Theta_\Gamma}(C;S_{t^-}),Z)]}
{\mathbb E_{C\sim D}[w_{\mathrm{pri}}(p^{\mathrm{pri}}(C;S_{t^-}))]},
\quad D\in\{P_{\mathrm{obj}},P_{\mathrm{conf}}\}.
\]

\[
\mathfrak F_{AP}^\Gamma=\lbrace\Theta_\Gamma:
D_K^\star(\pi)\le\epsilon_{AP}\ \forall K\in\mathfrak K_\pi^+,\quad
h_\pi\text{ factorization holds},\quad
\mathcal R_{\mathrm{prop}}^{P_{\mathrm{obj}}}(\Theta_\Gamma)
\le\mathcal R_{\mathrm{prop}}^{P_{\mathrm{obj}}}(\Theta_{\Gamma,0})+\epsilon_{\mathrm{prop}}\rbrace,
\]

\[
\mathcal J_\Gamma^*=\inf_{\Theta_\Gamma\in\mathfrak F_{AP}^\Gamma}
[\mathcal R_{\mathrm{pri}}^{P_{\mathrm{obj}}}(\Theta_\Gamma)+\lambda_{\mathrm{rep}}\mathcal C_{\mathrm{rep}}(\Theta_\Gamma)].
\]

Only when the feasible infimum is attained may the paper write an argmin. Candidate selection uses only \(P_{\mathrm{obj}}\); final frozen claims use untouched \(P_{\mathrm{conf}}\). Both use grouped rolling-origin evaluation, an overlap/horizon/label-delay embargo, and as-of replay. Cross-resolution comparisons use common raw histories and the same external target.

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
