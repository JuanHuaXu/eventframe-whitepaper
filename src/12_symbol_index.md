# Appendix A. Symbol Index

This index resolves the core symbols used by the formulas. Component spaces for event fields use calligraphic letters without descriptive subscripts; packet component spaces always carry descriptive subscripts.

\(\Omega\): substrate state space. It is never used as a cost function.

\(A_t\), \(\omega_{A_t}\): finite substrate/computational region and its history.

\(\Delta_\tau\), \(\Gamma_{\Delta_\tau}\): temporal resolution and task-relative coarse-graining map.

\(e_t\), \(C_t\), \(\mathfrak C_{\mathrm{adm}}\): event frame, length-\(k\) event context, and declared context domain for conditional laws and suprema.

\(H\), \(Z_{t+1}\): prediction horizon and observed marked-time or no-event outcome.

\(a(x)\), \(\mathscr F_t^{\mathrm{pred}}\), \(S_{t^-}\): availability time, prediction-time information, and mutable state reconstructed immediately before prediction.

\(P_{\mathrm{obj}}\), \(P_{\mathrm{conf}}\), \(P_\star\): design/selection law, untouched confirmation law, and externally fixed target law.

\(\nu(e)\), \(\tau(e)\): event-mark and event-time extractors.

\(\mathsf Q_\theta\), \(\mathcal O_\theta(C)\): predictive distribution over marked event times and the no-event outcome, and the typed bundle pairing that law with a structured point summary.

\(\mathcal L_{\mathrm{pred}}\), \(\overline{\mathcal L}_{\mathrm{pred}}\), \(\mathcal L_{\mathrm{event}}^H\): untransformed proper predictive loss, its preregistered bounded system-action transform, and bounded event-aware timing diagnostic.

\(\mathcal R_{\mathrm{pre}}\), \(\mathcal A_{\mathrm{post}}\): pre-observation admission risk and post-observation realized event action.

\(\mathsf Q_B\), \(B\), \(b_t\): baseline forecast law, baseline point predictor, and its point prediction. Event buckets use \(K\), never \(B\).

\(\mathscr H\), \(\mathbb H_d\): finite-dimensional Hilbert space and its self-adjoint operator representation space.

\(q_E\), \(d_E\), \(\Pi_E\), \(\delta_E\): event encoder, decoder, admissibility projection, and clipping radius.

\(\oplus_E\): typed event residual composition \(\mathcal E\times\mathbb H_d\to\mathcal E\).

\(\mathcal C_{A,t^-}\), \(\mathcal C_{R,t^-}\), \(\mathcal C_E\): as-of exact-key residual, as-of general residual, and episodic caches.

\(J_t^A\), \(J_t^R\), \(r_t^{\mathrm{use}}\), \(\mathfrak K_E\), \(\mathsf Q_t^R\): exact- and general-cache acceptance indicators, selected residual, residual Markov-kernel map, and corrected forecast law.

\(\Xi_R\), \(\Xi_A\), \(\Lambda_{\mathrm{eval}}\): residual contract, candidate abstraction-compatibility structure, and the externally frozen evaluation contract.

\(v_{k_t}\), \(v_t\), \(m_{k_t}\): cache-entry epoch, active local abstraction epoch, and materialized compatibility safety margin.

\(X_t\), \(\mathcal X_{\mathrm{ctx}}\): compressed runtime state and its domain. This domain is distinct from the auxiliary event-field space \(\mathcal X\).

\(\mathcal Y_{\mathrm{pkt}}\), \(\mathcal V_Y\): runtime packet space and packet residual representation space.

\(B_Y\), \(R_Y\), \(\oplus_Y\): packet baseline, packet residual, and typed packet composition.

\(\widehat{\mathbf y}_{t+1}\), \(\mathbf y_{t+1}^{\star}\): predicted and audited runtime packets.

\(G_t=(V_t,R_t)\): time-unrolled typed event graph. Predictive-dependency and causal edges remain distinct.

\(\mathfrak M=(U,V,F,P_U)\): structural causal model required for \(do\)-intervention notation.

\(\pi:\mathcal E\to\mathcal S_{\mathrm{abs}}\), \(h_\pi\), \(K\), \(\mathfrak K_\pi\), \(\mathfrak K_\pi^+\): abstraction map, operational abstraction key including costed side information, one event bucket, all induced buckets, and active buckets with admissible contexts.

\(\bar e_K\), \(\mathfrak C_K\), \(\mathcal R_C(K)\): concrete traceability frame, contexts anchored in a bucket, and coverage-aware context audit set.

\(D_K^\star\), \(D_K^{\mathrm{mdl}}\), \(D_K^{\mathrm{audit},\star}\), \(\widehat D_K^\star\), \(D_K^{\mathrm{cert},\star}\): external target-law future-diameter, model-only diagnostic diameter, restricted external diameter, its estimator, and simultaneous statistical-plus-continuity certificate.

\(D_Y^{\mathrm{law}}\): distance between probability laws. It is distinct from packet decoder \(d_Y\).

\(\mathcal G_t^A=(V_t^A,E_t^A)\): abstraction compatibility graph.

\(\mathsf Q_i\), \(\mathcal Y_i\): node-local predictive law and its outcome space.

\(g_{ie}\), \(\mathsf r_{ie}\): measurable node-to-edge comparison map and its pushforward restriction on predictive laws.

\(\delta_e\), \(\Delta_{\mathrm{comp}}\): edge compatibility defect and maximum defect upper confidence bound.

\(\partial_A\), \(L_A\): compatibility boundary and Laplacian, defined only for the stated finite-dimensional linear representation.

\(\mathcal U_0,\ldots,\mathcal U_4\), \(r_n\), \(d_t(h)\): baseline/refinement operators, selected stage at invocation \(n\), and deepest reached stage under hardware profile \(h\).

\(p_t^{\mathrm{pri}}\), \(w_{\mathrm{pri}}\), \(\mathcal R_{\mathrm{pri}}^D\), \(\mathcal R_{\mathrm{prop}}^D\), \(G_{a\rightarrow b}^{\mathrm{pri}}\): pre-outcome priority, its declared importance function, normalized weighted risk, unweighted proper risk, and gain between complete policies.

\(\zeta_t\), \(\mathcal Z_{\mathrm{reg}}\): observed operating regime and its space. A regime is not causal by default.

\(\mathcal C_{\mathrm{rep}}\), \(\Phi\): representation/runtime cost and finite-state descent potential.

\(\mathfrak F_{AP}^{\Gamma}\), \(\mathcal J_\Gamma^*\): fixed-resolution Anti-Pigeon-feasible design family and infimal governing objective value.
