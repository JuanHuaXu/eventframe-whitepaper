# Appendix A. Symbol Index

This index resolves the core symbols used by the formulas. Component spaces for event fields use calligraphic letters without descriptive subscripts; packet component spaces always carry descriptive subscripts.

\(\Omega\): substrate state space. It is never used as a cost function.

\(A_t\), \(\omega_{A_t}\): finite substrate/computational region and its history.

\(\Delta_\tau\), \(\Gamma_{\Delta_\tau}\): temporal resolution and task-relative coarse-graining map.

\(e_t\), \(C_t\), \(\mathfrak C_{\mathrm{adm}}\): event frame, length-\(k\) event context, and declared context domain for conditional laws and suprema.

\(H\), \((\mathcal N,\mathscr A_{\mathcal N})\), \((\mathcal Z_H,\mathscr A_H)\), \(Z_{t+1}\): prediction horizon, measurable mark space, complete measurable marked-time/no-event space, and observed outcome.

\(a(x)\), \(\mathscr F_t^{\mathrm{pred}}\), \(\mathfrak H_t\), \(\mathfrak h_t\), \(c_k\), \(\mathrm{Replay}_\Theta\), \(S_{\Theta,t^-}\): availability time, prediction information, observable-history space and one history, context extractor, candidate replay operator, and reconstructed candidate state.

\(P_{\mathrm{obj}}\), \(P_{\mathrm{conf}}\), \(P_\star\): design-generating law, confirmation-generating law, and externally fixed target law.

\(\mathcal S_{\mathrm{obj}}\), \(\mathcal S_{\mathrm{conf}}\): realized design sample or trajectory block and untouched confirmation sample or block.

\(\nu(e)\), \(\tau(e)\): event-mark extractor and declared scalar temporal anchor; the anchor is a point timestamp or, by default, interval onset.

\(\mathcal E_\varnothing\), \(d_H\): tagged no-event extension of the structured event space and fixed point-decision rule on forecast laws.

\(\hat e_\theta^H(C)\), \(\hat e_t^H(\mathbf r)\), \(\mathrm{lift}_H\): coherent no-event-capable predictor summary, residual-record summary, and map aligning a structured template with a selected marked outcome.

\(\mathsf Q_\theta\), \(\mathcal O_\theta(C)\): predictive distribution over marked event times and the no-event outcome, and the typed bundle pairing that law with a coherent no-event-capable structured summary.

\(\mathcal L_{\mathrm{pred}}\), \(\overline{\mathcal L}_{\mathrm{pred}}\), \(\mathcal L_{\mathrm{event}}^H\): untransformed proper predictive loss, its preregistered bounded system-action transform, and bounded event-aware timing diagnostic.

\(\mathcal R_{\mathrm{pre}}\), \(\mathcal A_{\mathrm{post}}\): pre-observation admission risk and post-observation realized event action.

\(\mathsf Q_B\), \(B\), \(b_t\): fallback forecast law, fallback conditional event-template predictor, and its template. Event buckets use \(K\), never \(B\).

\(\mathcal K_t^{\mathrm{bel}}\), \(q_{K,t}^{\mathrm{eff}}\), \(\mathbb P_{K,\theta}\), \(\mathsf P_{H,K}\), \(\lambda_{K,t}^{\mathrm{bel}}\): valid belief buckets, effective posteriors, coherent joint evidence-and-outcome model family, its declared outcome-predictive kernels, and frozen mixture weights.

\((\mathcal X_K,\mathscr A_{\mathcal X_K})\), \(\nu_K\), \(\mathbb P_{K,\theta}^{\Xi}\), \(\mathbb P_{K,\theta}^{Z}\): measurable bucket evidence space, dominating measure, and the joint model's evidence and outcome marginals.

\(\mathsf Q_t^0\), \(B_H^{\mathrm{bel}}\), \(b_t^0\): posterior-predictive base law, its template map, and aligned pre-residual template. The fallback baseline is used only when the valid belief-bucket set is empty.

\(\mathscr H\), \(\mathbb H_d^E\), \(\mathbb H_d^Q\): finite-dimensional Hilbert space and separately tagged point-template and forecast-law copies of its self-adjoint operator representation space.

\(q_E\), \(d_E\), \(\Pi_E\), \(\delta_E\), \(\delta_Q\): event encoder, decoder, admissibility projection, and point/law clipping radii.

\(\oplus_E\): typed event residual composition \(\mathcal E\times\mathbb H_d^E\to\mathcal E\).

\(\mathcal C_{A,t^-}\), \(\mathcal C_{R,t^-}\), \(\mathcal C_E\): as-of exact-key residual, as-of general residual, and episodic caches.

\(\mathcal M_R\), \(\mathcal V_R\), \(\mathbf r\), \(\mathbf0_R\): residual-component mode set, typed record space, residual record, and no-correction record.

\(J_t^A\), \(J_t^R\), \(\mathbf r_t^{\mathrm{use}}\), \(r_{t,H}^{E,\mathrm{obs}}\): cache acceptance indicators, selected record, and point residual defined only for an in-horizon event.

\(\rho_H^Q\), \(r_{t,H}^{Q,\mathrm{obs}}\), \(\mathfrak K_H^Q\), \(\mathfrak F_R\), \(\mathsf Q_t^R\): law-residual estimator, observed law residual, measurable full-outcome kernel map, deterministic complete residual policy, and final scored corrected law.

\(D_{\mathrm{res}}\), \(\mathsf Q_i^{0,\mathrm{ref}}\), \(\epsilon_i^{\mathrm{bel}}\), \(\overline D_{i,t}^{\mathrm{bel}}\), \(\mu_i^{\mathrm{bel}}\): fixed residual-reference law distance, reference base law, allowed law motion, certified upper law-motion bound, and law-component survival margin.

\(D_{\mathrm{tmpl}}\), \(b_i^{0,\mathrm{ref}}\), \(\epsilon_i^{\mathrm{tmpl}}\), \(\overline D_{i,t}^{\mathrm{tmpl}}\), \(\mu_i^{\mathrm{tmpl}}\), \(\upsilon_i^{\mathrm{bel}}\): fixed template distance, reference base template, allowed template motion, certified upper template-motion bound, point-component survival margin, and posterior-predictive certificate version.

\(s_i\), \(s_{k_t}\), \(\mathcal S_{\mathrm{prov}}\): provenance records for general and exact residual-cache entries and their declared space.

\(\Xi_R\), \(\Xi_B\), \(\Xi_A^{(v)}\), \(\Lambda_{\mathrm{eval}}\): residual contract, bounded Bayesian contract, published versioned abstraction-compatibility structure, and the externally frozen evaluation contract.

\(H_i\), \(H_{k_t}\), \(v_{k_t}\), \(v_t\), \(\mu_{k_t}\): cache horizons, cache-entry and active epochs, and materialized compatibility safety margin.

\(\mathfrak E_t^B\), \(\mathcal N_t^B\), \(\mathcal R_t^{\mathrm{vec}}\), \(\mathcal N_t^{\mathrm{sh}}\): bounded Bayesian candidate universe, nominated frontier, and its vector-retrieval and sheaf-inspired components.

\(J_t^{\mathrm{nom}}\), \(J_t^{\mathrm{evid}}\), \(A_t^B\), \(\tau_t^B\), \(J_t^{\mathrm{act}}\): nomination and evidence-readiness indicators, Bayesian activation score, criticality-adjusted threshold, and threshold-selective indicator.

\(q_B\), \(q_{\mathrm{FA}}\), \(q_{\mathrm{sel}}\), \(J_t^{\mathrm{upd},q_B}\): frozen Bayesian policy, bounded-frontier-update-all and threshold-selective policies, and complete policy-indexed update-admission indicator.

\(\kappa_t^B\), \(\mathcal X_{K,t}^{\mathrm{upd},q_B}\), \(L_K^{\mathrm{adm},q_B}\): Anti-Pigeon-governed posterior-key assignment, admitted evidence-packet set for key \(K\), and complete admission-conditioned likelihood.

\(p_K^{\mathrm{adm},q_B}\), \(\underline p_{K,t}^{\mathrm{adm},q_B}\), \(p_{\min}^{\mathrm{adm}}\), \(\mathfrak H_{K,t}^{\mathrm{adm},q_B}\): complete admission probability, certified uniform lower bound, positive support floor, and certified admission-support region.

\(J_{K,t}^{\mathrm{share}}\), \(q_{K,t^-}\), \(q_{K,t}^+\), \(\mathcal C_{B,t^-}\): Anti-Pigeon posterior-sharing decision, cached prior, updated posterior, and as-of posterior cache.

\(u_e\), \(v_e\), \(n_e^{\mathrm{eff}}\), \(\ell_K^{\mathrm{share}}\), \(\ell_K^{\mathrm{split}}\), \(p_K^{\mathrm{split}}\), \(p_K^{\mathrm{eq}}\), \(G_{K,t}^{B}\), \(w_{K,t}^{B}\): member useful/not-useful statistics, effective support, shared/split log marginal evidence, posterior split and practical-equivalence probabilities, proposal-only group decision, and bounded borrowing weight.

\(\pi_K^{\mathrm{split}}\), \(\epsilon_{B,\mathrm{eq}}\), \(\tau_{B,\mathrm{cmp}}\), \(\tau_{B,\mathrm{eq}}\), \(n_{B,\mathrm{cmp}}\), \(w_{B,\max}\), \(K_{\max}\): frozen split prior, practical-equivalence width, split and equivalence decision thresholds, minimum member support, uncertain-branch borrowing cap, and group-size cap.

\(\omega_{B,\mathrm{pool}}\), \(J_t^{\mathrm{val}}(e)\), \(J_{K,t}^{\mathrm{shock}}\), \(A_{K,t}^{\mathrm{rev}}\): shared-posterior evidence discount, structural-revision evidence eligibility, validated Anti-Pigeon split-shock indicator, and fail-closed retain/reset/split action.

\(Y_{K,t}\), \(m_{K,t}^{s}\), \(\eta_s\), \(C_{K,t}^{+}\), \(C_{K,t}^{-}\), \(\delta_{\mathrm C}\), \(h_{\mathrm C}\), \(d_{K,t}^{\mathrm{cool}}\), \(n_{\mathrm{warm}}\): observed usefulness, slow reference mean and its update rate, two-sided cumulative statistics, cumulative slack and boundary, cooldown counter, and warm-up length.

\(\gamma_{\mathrm{cp}}\), \(J_{K,t}^{\mathrm{cp}}\), \(\pi_{\mathrm{audit}}\), \(J_t^{\mathrm{audit}}\), \(N_{\mathrm{audit}}^{\max}\): changepoint run-length threshold, combined changepoint trigger, frozen inactive-event audit probability, independent audit indicator, and fixed audit-reservoir capacity.

\(\mathsf Q_t^{\mathrm{local}}\), \(\mathsf Q_t^{\mathrm{expanded}}(e)\), \(D_{\mathrm{omit}}\), \(\Delta_{K,t}^{\mathrm{omit}}\), \(\mathfrak U_{\mathrm{omit}}^{\mathrm{seq}}\), \(U_t^{\mathrm{omit}}\), \(\epsilon_{B,\mathrm{omit}}\): complete scored local and shadow-expanded laws, normalized Jensen--Shannon divergence, audit-population omission risk, frozen simultaneous confidence sequence, maximum certified omission bound, and its predeclared acceptance threshold.

\(k_v\), \(d_{\mathrm{sh}}\), \(d_G\), \(B_{\max}\), \(N_t^{\mathrm{upd},q_B}\), \(M_{\mathrm{hyp}}\), \(R_{\mathrm{cp}}\): vector width, sheaf-inspired and graph degree caps, frontier cap, admitted update count, bounded hypothesis or statistic dimension, and retained changepoint-state cap.

\(T_{\mathrm{adm}}\), \(T_{\mathrm{sel}}\), \(T_{\mathrm{Bayes}}^{\mathrm{fast}}\): policy-indexed admission evaluation, complete admission-probability evaluation, and bounded direct Bayesian cost. \(T_B(k)\) remains the fallback baseline-predictor cost.

\(s_{(j),t}^{\mathrm{ret}}\), \(P_t\), \(N_t\), \(\varepsilon_s\), \(c_t^{\mathrm{pack}}\): external retrieval score at initial rank \(j\), packing-count boundary, returned frontier size, score normalization floor, and rank-domain packing-boundary certainty.

\(d_{i,t}^{\mathrm{raw}}\), \(r_{i,t}^{\mathrm{corr}}\), \(\lambda_{\min}\), \(\lambda_{\max}\), \(\lambda_{i,t}^{\mathrm{el}}\): raw EventFrame rank correction, independently accepted correction reliability, frozen certainty-modulation bounds, and resulting elastic multiplier.

\(\Delta_{\max}\), \(\Delta_{i,t}^{\mathrm{rank}}\), \(s_{i,t}^{\mathrm{final}}\), \(T_{\mathrm{rank}}(N_t)\): absolute rank-correction cap, applied elastic rank delta, final pre-packing score, and bounded ranking-stage cost.

\(\Sigma_t\), \(B_{\mathrm{pub}}\), \(B_{\mathrm{inv}}\), \(N_{\mathrm{pub}}(j)\), \(N_{\mathrm{inv}}(j)\): coupled versioned learning state, finite per-evidence-epoch publication and invalidation budgets, and realized counts.

\(X_t\), \(\mathcal X_{\mathrm{ctx}}\): compressed runtime state and its domain. This domain is distinct from the auxiliary event-field space \(\mathcal X\).

\(\mathcal Y_{\mathrm{pkt}}\), \(\mathcal V_Y\): runtime packet space and packet residual representation space.

\(B_Y\), \(R_Y\), \(\oplus_Y\): packet baseline, packet residual, and typed packet composition.

\(\widehat{\mathbf y}_{t+1}\), \(\mathbf y_{t+1}^{\star}\): predicted and audited runtime packets.

\(G_t=(V_t,R_t)\): time-unrolled typed event graph. Predictive-dependency and causal edges remain distinct.

\(\mathfrak M=(U,V,F,P_U)\): structural causal model required for \(do\)-intervention notation.

\(E_A^{(b)},E_B^{(b)},m_{\mathrm{ch}}\): equal-length baseline/revealed trajectories in two aligned domains and their stage count; \(b=0\) is baseline and \(b=1\) is revealed.

\(\phi_{A,j},\phi_{B,j},T_j,J_j^{\mathrm{loc}},J_j^{\mathrm{map}}\): declared stage-coordinate projections, frozen cross-domain correspondence, unchanged-coordinate locality-and-map indicator, and mapped-change propagation indicator.

\(J_{\mathrm{prop}},J_{\mathrm{erase}},J_{\mathrm{pred}}\): complete-chain propagation, terminal-erasure, and predictive-law eligibility indicators.

\(p_A^{(b)},p_B^{(b)},\delta_{A,j},\delta_{B,j}\): normalized stage-nomination laws and their signed baseline-to-revealed effects.

\(M_A,M_B,D_{\mathrm{tr}},\eta_{\mathrm{inv}},\eta_{\mathrm{tr}},\mathcal C_{\mathrm{chain}}\): domain-wise predictor movement, cross-domain signed-effect defect, frozen invariant and translation thresholds, and invariant/translation/divergence classifier.

\(\kappa,s_{\mathrm{cache}},s_{\mathrm{fresh}}\): exact snapshot-bound nomination-score cache identity, cached raw score, and freshly computed raw score.

\(T_{\mathrm{chain}},T_{\mathrm{struct}},T_{\mathrm{law}},d\): complete chain-audit cost, structural-validation cost, predictive-law cost, and embedding dimension.

\(K_{A,j},K_{B,j}\): optional explicit stage-transition maps used only by the stronger kernel-level commuting condition.

\(\pi:\mathcal E\to\mathcal S_{\mathrm{abs}}\), \(h_\pi\), \(K\), \(\mathfrak K_\pi\), \(\mathfrak K_\pi^+\): abstraction map, operational abstraction key including costed side information, one event bucket, all induced buckets, and active buckets with admissible contexts.

\(\bar e_K\), \(\mathfrak C_K\), \(\mathcal R_C(K)\): concrete traceability frame, contexts anchored in a bucket, and coverage-aware context audit set.

\(D_K^\star\), \(D_K^{\mathrm{mdl}}\), \(D_K^{\mathrm{audit},\star}\), \(\widehat D_K^\star\), \(D_K^{\mathrm{cert},\star}\): external target-law future-diameter, model-only diagnostic diameter, restricted external diameter, its estimator, and simultaneous statistical-plus-continuity certificate.

\(\overline L_K^{\mathrm{cert}}\): analytic uniform continuity bound or simultaneous upper confidence bound included in the bucket certificate.

\(D_Y^{\mathrm{law}}\): distance between probability laws. It is distinct from packet decoder \(d_Y\).

\(\mathcal G_t^A=(V_t^A,E_t^A)\): abstraction compatibility graph.

\(\mathsf Q_i\), \(\mathcal Y_i\): node-local predictive law and its outcome space.

\(g_{ie}\), \(\mathsf r_{ie}\): measurable node-to-edge comparison map and its pushforward restriction on predictive laws.

\(\delta_e\), \(\Delta_{\mathrm{comp}}\): edge compatibility defect and maximum defect upper confidence bound.

\(\mathfrak Q_{\mathcal N}\), \(D_i\), \((\overline{\mathsf Q}_i)_{i\in\mathcal N}\): reconciliation feasible tuple family, local fidelity divergences, and returned reconciled forecast tuple.

\(\partial_A\), \(L_A\): compatibility boundary and Laplacian, defined only for the stated finite-dimensional linear representation.

\(D_t^{\mathrm{design}}\), \(D_t^{\mathrm{conf}}\), \(\mathfrak S_t(\Xi_A^{(v)};\mathcal N)\), \(\Psi_t\), \(d_{\mathrm{edit}}\), \(\mathcal C_{\mathrm{snap}}\): disjoint chronological snap-design and confirmation blocks, finite local candidate family, design-block score, structural-churn penalty, and revision cost. \(\Theta_\Gamma[\Xi']\) is the complete candidate induced by an edit, including dependent local abstraction, model, key, and certificate revisions.

\(\mathfrak O_t\), \(U_{\mathrm{obl}}\): externally fixed comparison-obligation set and weighted unresolved burden.

\(\lambda_{\mathrm{comp}}\), \(\lambda_{\mathrm{edit}}\), \(\lambda_{\mathrm{snap}}\), \(\lambda_{\mathrm{obl}}\): non-negative snap-selection weights for compatibility defect, structural churn, revision cost, and unresolved obligations; the final weight is strictly positive unless unresolved obligations are forbidden.

\(\mathcal D_{\Delta,t}(\Xi')\), \(\mathfrak K_{\Delta,t}(\Xi')\), \(E_{\Delta,t}^{\mathrm{keep}}(\Xi')\): reverse dependency closure of a snap candidate and its affected active-bucket and retained/new-edge projections.

\(\Delta\mathcal R_{\mathrm{prop},t}^{\mathrm{snap}}\), \(G_{v\rightarrow\mathrm{cand},t}^{\mathrm{pri}}\), \(C_{v\rightarrow\mathrm{cand},t}(h)\), \(A_t^{\mathrm{snap}}\): empirical confirmation proper-risk change, paired priority gain, utility-normalized resource cost, and joint snap-acceptance indicator.

\(T_{\mathrm{generate}}\), \(T_{\mathrm{obl}}\), \(T_{\mathrm{confirm}}\), \(T_{\mathrm{publish}}\): bounded snap-candidate generation, comparison-obligation validation, confirmation scoring, and atomic publication costs.

\(\delta_{\mathrm{snap}}>0\), \(\epsilon_{\mathrm{obl}}\ge0\), \(\epsilon_{\mathrm{acc}}^{\mathrm{comp}}\in[0,\epsilon_{\mathrm{split}}^{\mathrm{comp}}]\): predeclared net-gain safety margin, unresolved-obligation limit, and compatibility threshold for affected retained or newly added edges.

\(\mathbf v^{(v)}\), \(\mathcal C_{\mathrm{mem}}^{(v)}\), \(\mathsf B_{\mathcal D}\), \(\mathsf I_{\mathcal D}\): local epoch map, versioned memory tuple, monotone epoch-bump map, and targeted stale-marking operator for a dependency closure.

\(\mathcal U_0,\ldots,\mathcal U_5\), \(r_n\), \(d_t(h)\): baseline/refinement operators, selected stage at invocation \(n\), and deepest reached stage under hardware profile \(h\); \(\mathcal U_3\) is bounded predictive sheaf snapping.

\(\mathcal B_0,\ldots,\mathcal B_3\): bounded cached Bayesian update, bounded changepoint monitor, event-pattern refinement, and deep particle, variational, or unrestricted-comparison stages.

\(p_t^{\mathrm{pri}}\), \(w_{\mathrm{pri}}\), \(\widetilde w_t\), \(L_t^{[q]}\): pre-outcome priority, its declared importance function, normalized evaluation weight, and bounded per-case system loss under complete policy \(q\).

\(\mathcal R_{\mathrm{pri}}^D\), \(\mathcal R_{\mathrm{prop}}^D\), \(G_{a\rightarrow b}^{\mathrm{pri}}\), \(G_{a\rightarrow b,\mathrm{rel}}^{\mathrm{pri}}\): normalized weighted risk, unweighted proper risk, and absolute and relative priority-weighted gains from complete policy \(q_a\) to \(q_b\).

\(C_{a\rightarrow b}(h)\), \(T_{\mathrm{budget}}\), \(\delta_{\mathrm{safety}}\): normalized resource cost of changing policies on hardware profile \(h\), declared latency budget used in that cost, and promotion safety margin.

\(\Delta_{\mathrm{pred}}(d)\), \(\widehat\Delta_{\mathrm{pred}}(d)\), \(s_{\mathrm{eff}}^{\mathrm{pred}}\), \(s_{\mathrm{eff}}^{\mathrm{causal}}\): paired proper-risk effect of ablating distinction \(d\), its confirmation estimate, the simultaneous-confidence-classified predictive sparsity ratio, and the separately identified causal sparsity ratio.

\(\zeta_t\), \(\mathcal Z_{\mathrm{reg}}\): observed operating regime and its space. A regime is not causal by default.

\(\mathcal C_{\mathrm{rep}}\), \(\Phi\): representation/runtime cost and finite-state descent potential.

\(\mathfrak F_{AP}^{\Gamma,\star}\), \(\mathcal J_\Gamma^{\mathrm{oracle}}\): population Anti-Pigeon-feasible design family and its oracle infimal benchmark.

\(\mathfrak G_\Gamma\), \(\widehat{\mathfrak F}_{AP}^{\Gamma}\), \(\widehat\Theta_\Gamma\): finite predeclared design family, empirically certified feasible family, and operationally selected design.
