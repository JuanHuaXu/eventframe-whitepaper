# 8. Complexity and Runtime Model

EventFrame separates prediction-time computation from post-observation refinement. The fast path may use only \(\mathscr F_t^{\mathrm{pred}}\) and state \(S_{t^-}\); realized loss, residual estimation, and abstraction learning begin only after the next outcome's availability time.

The reference fast path is:

1. Incrementally update \(C_t=e_{t-k+1:t}\).
2. Optionally form \(X_t=\chi(C_t,\mathcal M_t,G_t,\sigma_t)\).
3. Construct the bounded vector, sheaf-inspired, and as-of graph candidate frontier \(\mathcal N_t^B\).
4. Apply the frontier-all cheap update to every evidence-ready frontier member. Use the frozen activation threshold to select bounded deep work, not to suppress the cheap update, unless a separately validated selective-update policy is explicitly in force. Check the certified positive support bound for the complete nomination probability and materialized Anti-Pigeon sharing certificates; retrieve the corresponding cached prior and apply only a bounded Bayesian update. Unsupported admission correction falls back to working-posterior or no-update semantics.
5. Compute the posterior-predictive base law \(\mathsf Q_t^0(\cdot\mid C_t)\) and aligned template \(b_t^0\) from the valid effective posterior family, falling back to \(\mathsf Q_B\) and \(B\) only when that family is empty; independently compute packet baseline \(B_Y(X_t)\) when required.
6. Construct the bounded action key \(k_t=\alpha(C_t)\).
7. Try \(\mathcal C_{A,t^-}(k_t)\), then \(\mathcal C_{R,t^-}\), then episodic support if confidence is insufficient; require the residual's posterior-predictive version, the law-motion margin for every law-bearing record, and the template-motion margin for every point-bearing record to match \((\mathsf Q_t^0,b_t^0)\).
8. Compose a candidate event output bundle or packet using the separately typed clipped point and law residual components.
9. Evaluate \(\mathcal R_{\mathrm{pre}}\), confidence, effective support, age, epoch, margin, provenance, and decoder validity from \(S_{t^-}\).
10. When the output is a bounded retrieval packet, receive the external retrieval scores, compute \(c_t^{\mathrm{pack}}\), apply only reliability-gated elastic deltas, sort by \(s_{i,t}^{\mathrm{final}}\), and then enforce packing-count and token budgets. Anti-Pigeon or epoch invalidation is checked before a cached delta can act.
11. Return the admissible prediction or fall back to the posterior-predictive no-residual bundle \(\mathcal O_t^0\). Do not evaluate realized prediction loss yet.

The packet names memory nodes, graph edges, retrieval lane, compaction risk, response mode, and an optional control branch. It predicts what the runtime should read or do; the event prediction describes what is expected to happen.

```mermaid
flowchart LR
    C["Context C_t"] --> N["Bounded Bayesian frontier"]
    N --> J["Admission and sharing certificates"]
    J --> B["Cached belief update"]
    B --> Q0["Posterior-predictive base"]
    Q0 --> A["Posterior-aware exact residual"]
    A -->|accepted| P["Typed composition"]
    A -->|miss| R["General residual cache"]
    R -->|accepted| P
    R -->|miss| E["Episodic support"]
    E --> P
    P --> Q["Pre-risk and validity gate"]
    Q --> O["Return prediction"]
    O --> Z["Observe outcome"]
    Z --> S["Post-observation slow path"]
    S --> U["Update losses and memories"]
    S --> D["Bayesian audit and changepoint review"]
    S --> F["Sensitivity audit"]
    S --> G["Abstraction and compatibility audit"]
    U --> A
    D --> N
    F --> G
    G --> A
    G --> R
```

Expected constant-time lookup is a conditional implementation property. Let \(T_K\) be key-construction cost, \(T_A\) exact-key lookup, \(T_R(N)\) general residual retrieval, \(T_E(M)\) episodic retrieval, \(T_{\oplus}\) typed composition, \(T_{\mathrm{Bayes}}^{\mathrm{fast}}\) the bounded-frontier Bayesian work, and \(T_{\mathrm{rank}}(N_t)\) the boundary-certainty, delta-application, and bounded sorting cost. Then:

\[
T_{\mathrm{fast}}
=T_C+T_{\mathrm{Bayes}}^{\mathrm{fast}}+T_B(k)+T_K+T_A
+I_R T_R(N)+I_E T_E(M)+T_{\oplus}+T_{\mathrm{pre}}
+T_{\mathrm{rank}}(N_t),
\]

where \(I_R,I_E\in\{0,1\}\) indicate fallbacks. Let

\[
N_t^{\mathrm{upd},q_B}
=\left|\left\{e\in\mathfrak E_t^B:
J_t^{\mathrm{upd},q_B}(e)=1\right\}\right|
\le |\mathcal N_t^B|\le B_{\max},
\]

For a frontier cap \(N_t\le B_{\max}\), certainty and delta application are \(O(N_t)\), and comparison sorting is \(O(N_t\log N_t)\) unless the retrieval contract already supplies a compatible bounded order and a selection algorithm is used. Thus the elastic arithmetic is constant per candidate and independent of corpus size, but the complete ranking stage is not called \(O(1)\). Rank-delta cache lookup remains expected \(O(1)\) only under the same bounded-key and bounded-table assumptions as the residual cache.

where \(B_{\max}\) is the predeclared frontier cap. Let \(M_{\mathrm{hyp}}\) bound the updated sufficient-statistic or discrete-hypothesis dimension, and let \(R_{\mathrm{cp}}\) bound retained changepoint run-length states. Let \(T_{\mathrm{adm}}(|\mathcal N_t^B|;q_B)\) evaluate readiness and any policy-specific threshold over the materialized frontier; nomination cost is already charged to vector retrieval and bounded expansion. Let \(T_{\mathrm{sel}}(N_t^{\mathrm{upd},q_B},M_{\mathrm{hyp}};q_B)\) evaluate or approximate the complete admission probability, including nomination, required by the admission-conditioned likelihood without a separate corpus scan. For a conjugate, finite-hypothesis, or otherwise bounded primitive,

\[
\begin{aligned}
T_{\mathrm{Bayes}}^{\mathrm{fast}}
={}&T_{\mathrm{vec}}(k_v)+T_{\mathrm{expand}}(d_{\mathrm{sh}},d_G)
+T_{\mathrm{adm}}(|\mathcal N_t^B|;q_B)\\
&+T_{\mathrm{sel}}(N_t^{\mathrm{upd},q_B},M_{\mathrm{hyp}};q_B)
+O(N_t^{\mathrm{upd},q_B}M_{\mathrm{hyp}}R_{\mathrm{cp}})
+T_{\mathrm{cert}}.
\end{aligned}
\]

This is history-independent only when \(k_v\), sheaf-inspired degree \(d_{\mathrm{sh}}\), as-of graph degree \(d_G\), \(B_{\max}\), \(M_{\mathrm{hyp}}\), and \(R_{\mathrm{cp}}\) are bounded, when the vector-index query itself has a declared bound, and when \(T_{\mathrm{sel}}\) uses a bounded exact computation or a predeclared bounded approximation. Under \(q_{\mathrm{FA}}\), \(N_t^{\mathrm{upd},q_B}\) is the evidence-ready frontier size; under \(q_{\mathrm{sel}}\), it is no larger. Thus frontier-all changes the bounded multiplicative constant, not the dependence on corpus size. Corpus size may still affect \(T_{\mathrm{vec}}\), index construction, cache maintenance, and storage I/O. Constant time per sample in a cited streaming algorithm means constant with respect to accumulated stream length under that algorithm's fixed resources; it does not mean zero dependence on frontier width, particle count, parameter dimension, optimization iterations, graph degree, selection-probability evaluation, or hardware. Sliding-window maintenance gives \(T_C=O(1)\). A bounded, already-constructed key and bounded hash table give expected \(T_A=O(1)\). The claim fails if key construction scans unbounded context, frontier or graph degree grows, the posterior or run-length support expands without cap, the table is unbounded, or lookup falls back to unrestricted nearest-neighbor search. Concurrency, hashing, collision handling, every term in \(T_{\mathrm{sel}}\), and eviction costs must be measured rather than hidden inside the constant.

Continuous publication couples posterior, residual, epoch, graph, and abstraction state. Let

\[
\Sigma_t=
(\mathcal C_{B,t^-},\mathcal C_{R,t^-},\mathbf v_t,\Xi_A^{(v)},G_t)
\]

be the versioned learning state visible to prediction readers. Index evidence epochs by \(j\), where one epoch contains only publications triggered before the next newly available external evidence item. Freeze finite budgets \(B_{\mathrm{pub}},B_{\mathrm{inv}}\in\mathbb N_0\), hysteresis thresholds, cooldowns, and deterministic conflict ordering. A conforming runtime enforces

\[
N_{\mathrm{pub}}(j)\le B_{\mathrm{pub}},
\qquad
N_{\mathrm{inv}}(j)\le B_{\mathrm{inv}}.
\]

Exhausting either budget freezes further dependent publication in that region, retains or republishes the last complete valid snapshot, and routes the case to slow audit. These bounds prevent unbounded same-evidence-epoch update and invalidation loops; atomic publication prevents mixed versions. They do not prove convergence across an unbounded or drifting evidence stream. A stronger claim requires a joint state metric or Lyapunov argument covering posterior updates, residual recertification, epoch changes, and abstraction edits together.

The slow path starts after \(Z_{t+1}\) or the audited packet target exists:

1. Evaluate \(\mathcal L_{\mathrm{pred}}\), \(\mathcal L_{\mathrm{event}}^H\), and \(\mathcal A_{\mathrm{post}}\).
2. Evaluate packet component loss when a packet was used.
3. Estimate observed residuals and update support/confidence.
4. Consolidate episodic and residual memory.
5. Evaluate inactive audit samples, omitted influence, posterior calibration, and changepoint triggers.
6. Run bounded practical-equivalence split/share comparisons and calculate proposal-only borrowing weights. Only external Anti-Pigeon evidence may create sharing; validated full-stream or independent-audit shock evidence may revoke an existing certificate, split the bucket, and invalidate dependent residuals without certifying a replacement merge.
7. Refit or expand Bayesian posteriors with particle, variational, or unrestricted model-comparison methods when required.
8. Run validity-constrained sensitivity tests.
9. Run causal analysis only when an explicit SCM and identification strategy exist.
10. Audit bucket coverage and future-diameter estimates.
11. Accept split, merge, posterior-sharing, or ontology changes only on independent held-out evidence.

A cost decomposition is:

\[
T_{\mathrm{base}}
=T_{\mathrm{score}}+T_{\mathrm{residual}}+T_{\mathrm{consolidate}}
+T_{\mathrm{Bayes},\mathrm{audit}}+T_{\mathrm{cp}}
+\sum_{q=1}^{M_f}T_{\mathrm{predict}}^{(q)}+T_{\mathrm{audit}}
\]

\[
T_{\mathrm{upgrade}}
=T_{\mathrm{comp}}+T_{\mathrm{reconcile}}
+T_{\mathrm{snap}}+T_{\mathrm{spectral}}+T_{\mathrm{mixture}}
+T_{\mathrm{Bayes},\mathrm{deep}},
\]

\[
T_{\mathrm{slow}}=T_{\mathrm{base}}+T_{\mathrm{upgrade}}
+\sum_{q=1}^{M_c}T_{\mathrm{causal}}^{(q)},
\]

where \(M_f,M_c\in\mathbb N_0\) are the numbers of fuzzing-prediction and causal-analysis invocations. Set \(M_c=0\) when no causal model is available. Slow work must be budgeted, deferred, or batched so it does not silently migrate into the latency-critical path.

For the Beta-Bernoulli group comparison in Section 5, retrieving already materialized member sufficient statistics and evaluating both marginal evidences costs \(O(|K|)\) time and \(O(1)\) additional accumulator space, subject to a declared group-size cap \(|K|\le K_{\max}\). This cost is independent of accumulated history only because each member retains bounded sufficient statistics. It is not placed on ordinary recall, and it excludes the external audit and confirmation work required to issue an Anti-Pigeon certificate.

The Bayesian upgrade has an orthogonal cumulative ladder that does not renumber the abstraction-refinement stages:

\[
\begin{aligned}
\mathcal B_0&=\text{bounded activation, certificate lookup, and cached update},\\
\mathcal B_1&=\text{bounded robust changepoint monitoring},\\
\mathcal B_2&=\text{declared event-pattern forecast refinement},\\
\mathcal B_3&=\text{particle, variational SMC, unrestricted comparison, and model recalibration}.
\end{aligned}
\]

Only \(\mathcal B_0\), and \(\mathcal B_1\) when its run-length state is explicitly bounded, may be admitted to the direct fast path. \(\mathcal B_2\) is fast only for a bounded precompiled pattern family and state space. \(\mathcal B_3\) is slow-path work. A changepoint, high omitted-influence certificate, missing prior, invalid sharing certificate, high-priority case, or exhausted approximation budget escalates to a predeclared deeper Bayesian stage.

The full upgrade is defined as a staged family rather than one indivisible algorithm. Let \(S_t\) contain the current forecasts, caches, abstraction graph, audit state, and hardware profile \(h\). Define refinement operators:

\[
\mathcal U_0=\text{certified baseline/residual reuse},
\qquad
\mathcal U_1=\text{edge compatibility audit},
\]

\[
\mathcal U_2=\text{local reconciliation},
\qquad
\mathcal U_3=\text{bounded predictive sheaf snap},
\]

\[
\mathcal U_4=\text{component or spectral refinement},
\qquad
\mathcal U_5=\text{regime-mixture and map refinement}.
\]

Starting from \(S_t^{(0)}=\mathcal U_0(S_{t^-})\), let \(r_n\in\{1,2,3,4,5\}\) be the stage selected for slow-path invocation \(n\), subject to its prerequisites. The step-integration recurrence is:

\[
S_t^{(n)}=\mathcal U_{r_n}(S_t^{(n-1)}),
\qquad n=1,\ldots,N_t.
\]

Let every conservative invocation-cost bound be strictly positive, \(c_r^{U}(h,S)>0\), and charge repeated stages separately:

\[
C_t^{U}(n;h)=
\sum_{q=1}^{n}c_{r_q}^{U}(h,S_t^{(q-1)}).
\]

Invocation \(n\) is permitted only if:

\[
C_t^{U}(n;h)\le\mathcal B(p_t^{\mathrm{pri}}),
\]

and all prerequisite evidence and safety gates pass. The run stops at the first failed budget or prerequisite check, a declared convergence condition, or a finite iteration cap. Its reported refinement depth is:

\[
d_t(h)=\max\left(\{0\}\cup\{r_1,\ldots,r_{N_t}\}\right).
\]

Here \(p_t^{\mathrm{pri}}\in[0,1]\) is priority declared from prediction-time information, \(\mathcal B\) is a priority-dependent resource budget, and \(c_r^U(h,S)\) is a preregistered upper confidence bound or deterministic worst-case bound on hardware profile \(h\). The runtime also accumulates actual cost and reports overruns. Predicted admission alone is not a hard budget guarantee; a strict deadline additionally requires interruptible stages and a reserved worst-case completion margin or a deterministic stop. Stage 5 may revise mixtures or comparison maps, after which Stages 1--4 may be selected again; every rerun appears again in \(C_t^U\). The architecture targets certified reuse plus all five refinement stages; \(d_t(h)\) records the deepest stage reached, while the complete invocation sequence \((r_1,\ldots,r_{N_t})\), actual cost, and stopping reason are also reported.

This definition separates semantic interfaces from hardware policy. Faster processors, larger memory, improved accelerators, or cheaper distributional solvers reduce measured costs and their conservative bounds and can increase \(d_t(h)\) without changing event, residual, compatibility, or causality definitions. A conforming implementation must therefore record both the output stage and the hardware/cost profile used to select it.

For a changed edge set \(E_{\Delta}\), compatibility work is approximately:

\[
T_{\mathrm{comp}}=O\!\left(\sum_{e\in E_{\Delta}}C_{D_e}\right),
\]

where \(C_{D_e}\) is the cost of mapping and comparing the two incident forecasts. With bounded local degree this is local in the changed neighborhood. Spectral work depends on component size, representation dimension, sparsity, solver, and requested tolerance. Mixture refinement additionally depends on component counts and optimization restarts and is expected to remain the most expensive stage. No fixed millisecond or slowdown claim is made without an implementation and hardware profile.

For a finite predictive-snap family \(\mathfrak S_t\), the design-block computation is bounded by the work charged for every inspected candidate:

\[
T_{\mathrm{snap}}
\le
T_{\mathrm{generate}}
+
\sum_{\Xi'\in\mathfrak S_t}
\left[
T_{\mathrm{refit}}(\Xi')
+\sum_{e\in E_\Delta(\Xi')}C_{D_e}
+T_{\mathrm{obl}}(\Xi')
+T_{\mathrm{score}}(\Xi')
\right]
+T_{\mathrm{confirm}}+T_{\mathrm{publish}}.
\]

Here \(T_{\mathrm{generate}}\) includes bounded neighborhood and candidate construction, \(T_{\mathrm{obl}}\) validates direct or composed comparison obligations, and \(T_{\mathrm{confirm}}\) is confirmation scoring cost rather than the wall-clock wait for future outcomes. \(T_{\mathrm{score}}\) includes candidate risk, affected-bucket Anti-Pigeon evaluation, and affected-edge compatibility evaluation not already charged in the explicit edge sum; an implementation must partition these measurements so no operation is omitted or counted twice. The ordinary \(T_{\mathrm{comp}}\) term audits the published graph, whereas the inner edge sum charges incremental candidate comparisons. The untouched confirmation block may delay publication but is not placed on the current prediction path. Candidate count, neighborhood radius, reverse dependency closure, refit budget, comparison-obligation set, and map class must be bounded before the review begins; unrestricted graph-structure search is not a conforming snapping implementation. The candidate graph, induced local abstraction mapping, and dependent keys are built in shadow state, and publication is an atomic graph-key-epoch swap. Consequently snapping requires only the existing version-consistent epoch check on the direct fast path. The indirect cost is a temporary rise in baseline or certified-fallback use while affected residual entries are recertified.

The integration roadmap is cumulative:

1. Specify typed Bayesian evidence, parameter spaces, activation maps, source model, selection semantics, bounded sufficient statistics, and deterministic fallbacks.
2. Add shadow-only activation, independent audit sampling, and omitted-influence measurement before allowing production posterior updates.
3. Materialize Anti-Pigeon posterior-sharing certificates and enable bounded cached updates with atomic posterior-key-epoch publication.
4. Add bounded robust changepoint monitoring, warm-up, cooldown, and targeted invalidation; keep particle or unbounded run-length methods asynchronous.
5. Add proposal-only bounded practical-equivalence comparison and partial-pooling advice while retaining Anti-Pigeon as the sole posterior-sharing authority.
6. Add read-only compatibility auditing and materialize epoch/margin certificates for the unchanged residual fast path.
7. Enable local reconciliation only on held-out evidence that it improves priority-weighted utility without unacceptable harm.
8. Add bounded predictive sheaf snapping with shadow construction, targeted invalidation, atomic publication, and rollback.
9. Add component-level spectral diagnostics and refinement where linearization assumptions are validated.
10. Add predictive regime mixtures and deep Bayesian state-space refinement; promote causal interpretations only with explicit SCMs and identification assumptions.
11. Rebenchmark every stage on each hardware generation and widen activation budgets without weakening validation, selection, or Anti-Pigeon gates.

The runtime reports prediction score, event-aware timing error, pre-risk calibration, cache hit and fallback rates, residual improvement, activation and audit rates, selected and unselected posterior calibration, omitted influence, effective support, changepoint delay and false alarms, Bayesian frontier size, posterior-update cost, decoder failures, slow-path delay, selected Bayesian and abstraction refinement depths, hardware profile, edge defects, bucket audit coverage, snap attempts and acceptances, rollback, cache recertification delay, and split/merge churn. Without these measurements, the claimed fast/slow tradeoff remains an architectural proposal rather than an established result.
