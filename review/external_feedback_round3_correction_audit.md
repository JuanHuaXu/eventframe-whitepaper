# External Feedback Round 3: Correction Audit

Date: 2026-08-28

This audit records how the third external review was resolved. Reviewer statements were treated as evidence and checked against the source, normative notation, claims register, and generated publication formats.

| Finding | Classification | Resolution |
|---|---|---|
| Point and law residuals lacked semantic alignment | Confirmed | Replaced the shared residual with a tagged record containing independently typed point-template and forecast-law components. Component modes, estimators, clips, provenance, and claim limits are explicit. Joint records require forward validation of the complete bundle. |
| Population risks omitted history-dependent state | Confirmed | Defined observable trajectory history, candidate-specific deterministic as-of replay, and design/confirmation laws over history-outcome instances. Risks now integrate over replayed candidate state. |
| Log score could be infinite outside the transform contract | Confirmed | Made the bounded transform total on the attainable extended-real range, supplied explicit endpoint behavior, and specified how infinite empirical proper loss affects certification. A probability floor is valid only as a frozen forecast-family constraint. |
| Outcome and kernel measurability were underspecified | Confirmed | Defined measurable mark, time, marked-event, and tagged no-event spaces. Kernel requirements are stated through jointly measurable evaluation maps and the Markov-kernel property. |
| Reconciliation returned the wrong type and used undefined \(D_i\) | Confirmed | The argmin now returns a forecast tuple over a declared feasible tuple family; each local fidelity divergence is typed and its existence conditions are stated. |
| Estimated continuity bound uncertainty was absent | Confirmed | The certificate now uses an analytic uniform bound or a simultaneous upper confidence bound, jointly covering selected audit pairs and any estimated continuity constant. |
| Evaluation quantities could be tuned after inspection | Confirmed | The evaluation contract now freezes complete diagnostics or finite admissible classes and fitting rules, packet target/loss, priority model, and regime-shift window, repetition criterion, threshold, and action. |
| “Sheaf-compatible” overstated the current construction | Confirmed | Replaced the label with “sheaf-inspired compatibility scaffold” and retained the requirement that identity/composition laws be instantiated before a sheaf-theoretic claim. |
| Backtick-wrapped GitHub inline math should be stripped | Stale / rejected | GitHub’s supported inline math syntax in this repository is `$` followed by a backtick-delimited expression and a closing `$`; prior render checks established that stripping those delimiters breaks formulas containing dollar-sensitive Markdown. The generated GitHub paper retains the supported syntax. |
| Self-adjointness remains unnecessary to a theorem | Recommendation only | Retained with the existing limited-inspiration disclaimer and executable diagonal toy instantiation. No theorem is claimed to require self-adjointness. |
| The work remains a specification, not an empirical result | Confirmed by design | No correction required. The abstract, worked example, claims register, and evaluation section continue to state this limitation explicitly. |

No publication or remote push is part of this correction pass unless separately requested.
