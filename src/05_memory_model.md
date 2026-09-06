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

## Repetition and Poisoning Gate

Repeated text can crowd a retrieval packet without supplying new evidence. The reference runtime therefore applies two distinct repetition controls: a greedy packing-occupancy gate and an exact-group veto on selected-only Bayesian feedback. The term poisoning gate names these limited controls, not a detector of false statements, malicious intent, or prompt instructions. The threat model permits repeated or slightly edited stored assertions and changing conversation identifiers; it does not assume authenticated provenance, an uncompromised feedback issuer, or guaranteed retrieval of a clean source.

### Claim and recorded-lineage descriptors

For a stored frame \(e\), let \(N_{\mathrm{rep}}\) lowercase text and replace runs of non-letter/non-digit characters by word boundaries. Let \(c_{\mathrm{rep}}(e)\) be the ordered, separator-delimited tuple of normalized who, what, where, why, and how fields. A normalized where value beginning with `session ` is replaced by the empty string. The when field, raw transcript, event identifier, run identifier, and conversation identifier do not enter this claim descriptor. This deliberately prevents recapturing an assertion in a new conversation from creating corroboration, but can also conflate genuinely time-dependent claims.

Let \(\ell_{\mathrm{rep}}(e)\) be the recorded lineage descriptor. A conversation frame uses only its normalized producer; fresh source citations or tool-call identifiers do not create a new conversation lineage. A non-conversation frame uses the producer plus its sorted source-event identifiers when present, otherwise its tool-call identifier when present, otherwise the producer alone. Conversation recognition uses the declared conversation kinds or tags. These are recorded provenance fields, not authenticated origin or a transitive derivation graph.

Let \(o_{\mathrm{rep}}(e)\in\{0,1\}\) be one only for a non-conversation frame explicitly declaring a distinct occurrence with both what and when marked observed. Define \(g_{\mathrm{rep}}(e)\) as a domain-separated SHA-256 digest of the claim and lineage digests, additionally including normalized when only if \(o_{\mathrm{rep}}(e)=1\). Two declared occurrences with identical normalized when still share a key. Hash equality is an operational identity assumption, not a proof of semantic equivalence or independence. Hashes of low-entropy assertions are not anonymization and should not be published as privacy protection.

Let \(V_{\mathrm{rep}}(e)\) be the token set of the normalized claim tuple, retaining tokens with at least two UTF-8 bytes and all numeric tokens. Let \(s_{\mathrm{rep}}(e,f)\) be the cardinality of its intersection divided by the cardinality of its union, defined as zero when either token set is empty. With frozen \(\tau_{\mathrm{rep}}=0.85\), define the symmetric indicator \(R_{\mathrm{rep}}(e,f)\) to be one if the group keys agree, or if the lineages agree, both occurrence flags are zero, and \(s_{\mathrm{rep}}(e,f)\ge\tau_{\mathrm{rep}}\); otherwise it is zero. This Jaccard heuristic is not transitive and does not understand negation, role reversal, or the importance of one changed number.

### Greedy packet occupancy

Let \(E_t^{\mathrm{pack}}(e,f)\) indicate that both frames have different current Anti-Pigeon posterior keys in the reserved certified-key namespace. The runtime checks this namespace and inequality after posterior-key assignment. This is an exemption from repetition suppression, not a certificate of cross-bucket divergence or source independence. Set \(\widetilde R_t^{\mathrm{rep}}(e,f)=R_{\mathrm{rep}}(e,f)(1-E_t^{\mathrm{pack}}(e,f))\).

Given the final candidate order \(e_1,\ldots,e_n\), packing capacity \(p\), token budget \(b\), and non-negative token estimates \(z_i\), start with accepted-index set \(I_0=\varnothing\). Freeze positive integer occupancy limit \(m_{\mathrm{rep}}\), default one. For each candidate in order:

1. Stop when \(|I_{i-1}|=p\). Skip the candidate if its token estimate plus the already accepted token sum exceeds \(b\).
2. Compute \(n_i^{\mathrm{rep}}=\sum_{j\in I_{i-1}}\widetilde R_t^{\mathrm{rep}}(e_i,e_j)\).
3. Accept the candidate exactly when \(n_i^{\mathrm{rep}}<m_{\mathrm{rep}}\), setting \(I_i=I_{i-1}\cup\{i\}\); otherwise retain \(I_i=I_{i-1}\). A token-rejected candidate also leaves the set unchanged.

The packet is the accepted ordered subsequence. With the default limit, no accepted pair has \(\widetilde R_t^{\mathrm{rep}}=1\): the later member would have failed step 3. For larger limits the rule bounds each arrival's correlated predecessors, not every final node degree or a transitive component's size. Exempt bucket pairs remain outside this bound. Suppression frees space for later candidates, so both removals and additions can occur relative to an unguarded packet. No stored frame, abstraction, or provenance is deleted or merged. The gate cannot recover a clean answer excluded from the nominated frontier, and the first accepted repetition need not be true.

### Selected-feedback veto and scored-law boundary

The feedback control uses exact \(g_{\mathrm{rep}}\) equality, not the packing Jaccard rule. In the Bayesian report's decision order, let \(j_i\) be the first earlier decision with the same non-empty group key. Let \(b_i^{\mathrm{rep}}=0\) if no such decision exists; otherwise set \(b_i^{\mathrm{rep}}=1-E_t^{\mathrm{pack}}(e_i,e_{j_i})\). The first representative remains fixed even when a later bucket is exempt. Consequently, this mechanism is not a per-bucket deduplicator: several later records in one bucket may all be exempt relative to that first representative.

For an outcome request let \(J_i^{\mathrm{old}}\) denote the complete pre-existing journal, availability, inclusion, and source-specific acceptance decision. Its new decision is \(J_i^{\mathrm{fb}}=J_i^{\mathrm{old}}(1-b_i^{\mathrm{rep}})\) for the selected-only source class, and \(J_i^{\mathrm{fb}}=J_i^{\mathrm{old}}\) for the full-stream or independent-audit source classes. A zero rejects the request rather than applying its outcome weight. Independent-audit requests still require the journal's audit draw and recorded inclusion probability. A full-stream label is not made trustworthy merely by naming that source class.

This veto does not change \(J_t^{\mathrm{upd},q_B}\), activation, or ordinary cheap frontier updates. Packing alone changes the retrieval packet, not the already computed \(\mathsf Q_t^R\). Rejecting feedback can change future sufficient statistics, \(q_{K,t}^{\mathrm{eff}}\), the Section 5 posterior-predictive base, and subsequently the scored law. Thus the combined gate is not globally law-invariant. It neither bounds cumulative influence across journals nor blocks repeated full-stream or valid audit updates. Usefulness probabilities remain probabilities of usefulness, not probabilities that an assertion is true.

Freeze descriptor rules, ordering, exemptions, occupancy limits, source classes, and policy version under \(\Xi_B\) and \(\Lambda_{\mathrm{eval}}\). The durable suppression decision is distinct from the internal descriptor key; current keys are not serialized in the outcome journal. Reconstructing them requires retained as-of frames and the matching implementation. For any ordinary Bayesian claim about feedback surviving the veto, the admission model must include this additional selection stage and its dependence on other candidates; the earlier single-packet admission formula alone does not establish that correction. The current heuristic supplies no such certificate and supports only working-posterior semantics where it is needed. Authenticated provenance, cross-journal evidence accounting, semantic contradiction protection, and poisoned-answer evaluation remain open requirements.

## Authenticated Outcomes and Reversible Working Beliefs

The preceding limitations describe the original repetition heuristic alone. The optional layer below narrows attribution and same-identity replay gaps, but does not supply complete derivation lineage, a cumulative independence budget, or poisoned-answer validation.

An optional outcome-admission layer distinguishes attributable evidence from factual truth. It operates when usefulness feedback is submitted, not when raw text is stored or an old frame is retrieved. The original repetition gate remains a packet and selected-feedback heuristic; authenticating a producer requires a separate operator-enrolled public-key registry. Unsigned learning remains a compatibility mode. The reversible filter below is opt-in and requires authenticated admission.

### Attribution and one-time observation accounting

Let \(\mathsf E\) denote a bounded outcome envelope containing tenant, issuer, key identifier, observation identifier, target event and query journal, resolved usefulness, original feedback signals, observed and available times, source class, inclusion probability, optional parent references, and signature. Freeze its encoding and source scopes in \(\Xi_B\). Let \(\zeta^{\mathrm{auth}}\) be the enrolled public-key registry fingerprint. The indicator \(J^{\mathrm{auth}}(\mathsf E;\zeta^{\mathrm{auth}})\) is one only when the signature verifies under a currently valid, non-revoked key enrolled for that tenant and feedback class, the observation time lies in its key-validity interval, availability is not in the future, and no declared parent makes it derived evidence. Existing journal, temporal, selection, and source-specific gates still apply. Authority to sign a full-stream label does not prove exhaustive sampling.

The reference encoding binds resolved usefulness and every original signal field, so the normalized durable request remains verifiable. It also binds the target journal and inclusion probability, but excludes transport retry identifiers. The implementation uses Ed25519, a versioned JSON-array encoding, and domain-separated SHA-256 digests; these are implementation choices, not new cryptographic constructions. A bounded successful-verification cache never bypasses current key-validity or admission checks. The registry is immutable during a run and replaced through controlled restart.

Define \(\iota^{\mathrm{obs}}(\mathsf E)\) as the domain-separated digest of tenant, issuer, and observation identifier, deliberately excluding key identifier and journal. Let \(\mathcal D^{\mathrm{obs}}\) be the durable partial map from this identity to the committed payload digest. First-consumption indicator \(\nu^{\mathrm{obs}}(\mathsf E)\) is obtained inside the transaction that mutates posterior, residual, and version state. Only an otherwise admitted envelope with an absent identity may commit a new update. An admission-eligible exact retry is a duplicate; a changed payload, re-signed key, or new journal for a consumed identity conflicts instead of learning again. Failed admission does not consume an identity. Unsigned callers cannot preoccupy the reserved ledger namespace.

Subject to unforgeability, collision resistance, stable issuer/observation identifiers, and an intact transactional ledger, one identity cannot count twice across concurrent requests, journals, and restart. This is not a global influence budget: an enrolled observer can lie, invent identifiers, or omit derivations, and different issuers can repeat one underlying source. Parent-bearing claims are withheld from independent outcome admission, not recursively resolved. There is no new autonomous provenance-investigation worker. Deleting or rolling back the ledger removes its replay history.

Authenticated posteriors carry \(\zeta^{\mathrm{auth}}\). Registry replacement prevents old-trust member and parent beliefs from serving or supplying group-comparison evidence; fresh outcomes start new-trust statistics, and children retain the applicable fingerprint. This is conservative invalidation, not issuer-specific historical subtraction. Existing policy versions also govern audit and residual reuse. Removing the registry deliberately returns to weaker unsigned semantics.

### A bounded, revisable usefulness model

For bucket \(K\), let \(n\) index newly committed admissible observations for its current working state. Rejected and duplicate requests neither advance \(n\) nor decay the state. Let \(x_n^{\mathrm{wrk}}\in\{0,1\}\) denote resolved usefulness, not factual truth. Declare Bernoulli hypotheses \(\theta_{\mathrm{lo}},\theta_{\mathrm{hi}}\) with \(0<p_{\mathrm{lo}}<p_{\mathrm{hi}}<1\) and likelihood \(L_{\mathrm{wrk}}(x\mid\theta_j)=p_j^x(1-p_j)^{1-x}\), for \(j\in\{\mathrm{lo},\mathrm{hi}\}\). The same family describes next-outcome usefulness before filtering approximations, aligning evidence and predictive semantics.

Freeze retention \(0\le\lambda_{\mathrm{wrk}}\le1\), log-odds bound \(L_{\mathrm{wrk}}^{\max}>0\), factor bound \(c_{\mathrm{wrk}}>0\), and equal prior odds. Define \(\mathrm{clip}_{a}(z)=\max(-a,\min(a,z))\) for \(a>0\). If \(w_n^{\mathrm{wrk}}>0\) is the outcome weight after any pooled-evidence discount, set \(\bar w_n^{\mathrm{wrk}}=\min(1,w_n^{\mathrm{wrk}})\). The bounded log factor is

\(f_n^{\mathrm{wrk}}=\mathrm{clip}_{c_{\mathrm{wrk}}}\bigl(\log L_{\mathrm{wrk}}(x_n^{\mathrm{wrk}}\mid\theta_{\mathrm{hi}})-\log L_{\mathrm{wrk}}(x_n^{\mathrm{wrk}}\mid\theta_{\mathrm{lo}})\bigr)\).

Starting at \(\ell_{K,0}^{\mathrm{wrk}}=0\), the committed update is

\(\ell_{K,n+1}^{\mathrm{wrk}}=\mathrm{clip}_{L_{\mathrm{wrk}}^{\max}}\bigl(\lambda_{\mathrm{wrk}}\ell_{K,n}^{\mathrm{wrk}}+\bar w_n^{\mathrm{wrk}}f_n^{\mathrm{wrk}}\bigr)\).

The weight cap prevents an inverse-selection weight from manufacturing multiple observations. Retention is per admitted observation, not wall-clock decay. Clipping, discounting, and omitted selection normalization make this a generalized working filter, not an exact posterior, unbiased importance-weighted estimator, or calibrated full-stream probability. Authentication does not remove nomination bias. Ordinary posterior claims elsewhere retain their stronger joint-model and admission requirements.

Define \(\sigma_{\mathrm{wrk}}(z)=1/(1+\exp(-z))\). The hypothesis belief mass is \(\sigma_{\mathrm{wrk}}(\ell_{K,n}^{\mathrm{wrk}})\), whereas the probability of useful next output is

\(p_{K,n}^{\mathrm{wrk}}=p_{\mathrm{lo}}+(p_{\mathrm{hi}}-p_{\mathrm{lo}})\sigma_{\mathrm{wrk}}(\ell_{K,n}^{\mathrm{wrk}})\).

These probabilities are not interchangeable. When existing selection, omission, and state-validity gates permit application, the implementation inserts \(p_{K,n}^{\mathrm{wrk}}\) into the belief-conditioned scoring path before residual correction and proper-score evaluation. For the non-contextual, non-hierarchical configuration, let \(s_i^{\mathrm{base}}\) be candidate \(i\)'s baseline score, \(\omega_{\mathrm{score}}\in[0,0.25]\) its frozen belief weight, and \(F_{\mathrm{cal}}\) the declared probability-calibration map. Its pre-residual useful probability is \(F_{\mathrm{cal}}((1-\omega_{\mathrm{score}})s_i^{\mathrm{base}}+\omega_{\mathrm{score}}p_{K,n}^{\mathrm{wrk}})\); without an admitted belief it uses the calibrated baseline. The working probability is also recorded as the belief law. Contextual scoring uses its separately frozen feature map; simultaneous working-filter and hierarchical-posterior modes are rejected. This is a modular Bernoulli-usefulness instantiation of Section 5's composition order, not implementation of the complete marked-time/no-event law.

Defaults are \(p_{\mathrm{lo}}=0.2\), \(p_{\mathrm{hi}}=0.8\), \(\lambda_{\mathrm{wrk}}=0.98\), \(L_{\mathrm{wrk}}^{\max}=6\), \(c_{\mathrm{wrk}}=2\), and \(\omega_{\mathrm{score}}=0.10\). They are design choices, not fitted optima. In the deterministic fixture, five new negative outcomes reverse a filter saturated by 10,000 positive outcomes without a detector reset. This demonstrates revisability, not the correctness of either set of outcomes.

Raw Beta/member evidence remains separate for Anti-Pigeon and monitoring. An authorized reset starts at equal odds and includes the revealing outcome once. Plain splits retain member statistics but start child working filters at prior instead of inheriting pooled certainty; split-reset initializes the triggering child from its revealing outcome. Missing or policy-mismatched working state starts at prior. Authentication cannot bypass Anti-Pigeon, certify replacement sharing, or exempt moved laws and templates from residual checks.

### Fixed-share grid alternative

The two-hypothesis predictive range is limited to approximately 0.201484-0.798516 at its defaults. This is a raw belief limitation, not a bound on every calibrated or residual-corrected output. Authentication and repeated evidence cannot remove model misspecification. A separately versioned, opt-in alternative uses fixed-share prediction [21,22], not a new inference algorithm or the complete run-length detector in [17].

Let \(m_{\mathrm{grid}}=21\), \(j\in\{0,\ldots,20\}\), \(\vartheta_j=\max(0.01,\min(0.99,j/20))\), \(\pi_j^{\mathrm{grid}}=1/21\), and \(h_{\mathrm{grid}}=0.02\). The finite latent state has transition \(T_{ij}^{\mathrm{grid}}=(1-h_{\mathrm{grid}})\mathbf 1[i=j]+h_{\mathrm{grid}}\pi_j^{\mathrm{grid}}\). Given latent state \(j\), the observed usefulness and predictive outcome use the same Bernoulli family with parameter \(\vartheta_j\). The transition represents a reset opportunity per admitted observation, not an assertion that a real-world regime changed.

Let \(q_{K,n,j}^{\mathrm{grid}}\) be the stored latent-state posterior after \(n\) committed observations, initially \(\pi_j^{\mathrm{grid}}\). Before observing outcome \(x_{n+1}^{\mathrm{wrk}}\), form

\(a_{K,n+1,j}^{\mathrm{grid}}=(1-h_{\mathrm{grid}})q_{K,n,j}^{\mathrm{grid}}+h_{\mathrm{grid}}\pi_j^{\mathrm{grid}}\).

The next-admitted-outcome useful probability is \(p_{K,n}^{\mathrm{grid}}=\sum_{j=0}^{20}a_{K,n+1,j}^{\mathrm{grid}}\vartheta_j\). This replaces \(p_{K,n}^{\mathrm{wrk}}\) in the same pre-residual scoring map above; it is not an additional score multiplier. After admission and one-time ledger consumption, with effective weight \(\bar w_{n+1}^{\mathrm{wrk}}\in[0,1]\), define the powered likelihood \(\ell_{n+1,j}^{\mathrm{grid}}=[\vartheta_j^{x_{n+1}^{\mathrm{wrk}}}(1-\vartheta_j)^{1-x_{n+1}^{\mathrm{wrk}}}]^{\bar w_{n+1}^{\mathrm{wrk}}}\) and update

\(q_{K,n+1,j}^{\mathrm{grid}}=a_{K,n+1,j}^{\mathrm{grid}}\ell_{n+1,j}^{\mathrm{grid}}/(\sum_{k=0}^{20}a_{K,n+1,k}^{\mathrm{grid}}\ell_{n+1,k}^{\mathrm{grid}})\).

The denominator is positive. The predictive lies within \([(1-h_{\mathrm{grid}})0.01+h_{\mathrm{grid}}/2,(1-h_{\mathrm{grid}})0.99+h_{\mathrm{grid}}/2]=[0.0198,0.9802]\); thus finite model bias remains. At unit weight this is Bayesian filtering for the declared finite reset model. Fractional weights define generalized Bayes. Neither interpretation establishes selection ignorability, source independence, calibration under the external law, or factual truth.

Serving derives the next-step prior without mutating stored weights. Repeated reads and duplicate or rejected outcomes do not compound the transition. A reset or incompatible working-state policy starts from the uniform prior; split-reset includes the revealing outcome once, and siblings retain their separate member evidence. The existing authentication, Anti-Pigeon, audit, and residual-motion gates still apply. Computation and working-state memory are \(O(m_{\mathrm{grid}})\), with no historical scan; ledger storage and complete request costs are separate.

The frozen synthetic comparison in Section 11 supports removing the narrow two-hypothesis bias in some regimes, not replacing every filter with the grid. Stable rates matching the old hypotheses favored the old model. A better raw belief also worsened the composed proper score in one drift scenario. Promotion must therefore evaluate the actual composed forecast, not the detached belief alone. The following separately tested rescue changes that composition contract.

### Complete-forecast mixture rescue

For a fixed bucket, let \(p_{j,n}^{\mathrm{mix}}\), \(j\in\{0,1,2,3\}\), be four complete useful probabilities committed before the next outcome: calibrated baseline, calibrated grid blend, direct grid predictive, and direct Beta mean. Clip each to \([10^{-6},1-10^{-6}]\). The direct experts are modular forecasts, not guaranteed calibrated probabilities under the external law. They allow prediction outside the narrow fixed-blend envelope without pretending the raw usefulness estimate should compensate for shrinkage.

Freeze \(\pi^{\mathrm{mix}}=(0.7,0.1,0.1,0.1)\) and \(h_{\mathrm{mix}}=0.002\). With normalized stored weights \(v_{j,n}^{\mathrm{mix}}\), initially \(\pi_j^{\mathrm{mix}}\), form \(a_{j,n}^{\mathrm{mix}}=(1-h_{\mathrm{mix}})v_{j,n}^{\mathrm{mix}}+h_{\mathrm{mix}}\pi_j^{\mathrm{mix}}\). The final useful probability is \(p_n^{\mathrm{mix}}=\sum_{j=0}^3 a_{j,n}^{\mathrm{mix}}p_{j,n}^{\mathrm{mix}}\). No second calibration or fixed belief blend is applied to this mixture. The old belief-weight cap constrains only the blend expert, not this new complete-law composition.

After an eligible outcome \(x_{n+1}^{\mathrm{wrk}}\) arrives, define \(L_{j,n}^{\mathrm{mix}}=(p_{j,n}^{\mathrm{mix}})^{x_{n+1}^{\mathrm{wrk}}}(1-p_{j,n}^{\mathrm{mix}})^{1-x_{n+1}^{\mathrm{wrk}}}\), using the journaled probabilities rather than predictions reconstructed with the revealing outcome. Update \(v_{j,n+1}^{\mathrm{mix}}=a_{j,n}^{\mathrm{mix}}(L_{j,n}^{\mathrm{mix}})^{\bar w_{n+1}^{\mathrm{wrk}}}/(\sum_{k=0}^3 a_{k,n}^{\mathrm{mix}}(L_{k,n}^{\mathrm{mix}})^{\bar w_{n+1}^{\mathrm{wrk}}})\). The denominator is positive, weights remain normalized, and the mixture defines both Bernoulli branches. Unit-weight immediate feedback is log-loss expert aggregation; fractional weights are generalized updates. Delayed feedback uses original forecasts but updates current weights in arrival order, without claiming the immediate-feedback posterior for the original chronology.

This reference mode requires authenticated grid inference, non-contextual and non-hierarchical scoring, and disabled residual application, so the optimized mixture is the final scored law. It does not redefine ranking deltas. Existing admission and Anti-Pigeon gates remain mandatory. The selector's state and each journal commitment carry policy/version information; stale-policy or stale-epoch feedback cannot train it. Reads do not mutate weights. Observation replay accounting and selector updates share the existing transaction. A policy change discards incompatible selector weights; resets and split children start from the selector prior rather than pooled performance. Old-regime forecasts do not initialize selector weights after a revealing reset.

State and update work are \(O(4)\) beyond the constituent forecasts. This is an implemented rescue for the tested composed-law failures, not a cure for the grid's raw estimation noise. Synthetic confirmation supports the three targeted repairs and a predeclared small mean-harm ceiling across varied baselines. Small regressions remain when the baseline is already correct. Active-residual coexistence, independently calibrated experts, delayed-feedback accuracy, retrieval improvement, and real-world utility remain unvalidated.

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

The discount controls pooled confidence; it does not weaken the evidence used to discover that the grouping itself is wrong. Event-local posteriors are not discounted by this rule. Relative to undiscounted pooling of the same observations and prior, the resulting shared predictive law is deliberately less concentrated, while full-strength member statistics let divergence evidence overturn sharing sooner. Unless the fractional contribution follows from a declared coherent generative model, \(\omega_{B,\mathrm{pool}}<1\) defines a tempered working posterior rather than an ordinary posterior under the common-\(\theta\) model.

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
\mathrm{shared\_reset},&J_{K,t}^{\mathrm{shock}}=0, J_{K,t}^{\mathrm{share}}=1, J_{K,t}^{\mathrm{cp}}=1,\\
\mathrm{individual\_reset},&J_{K,t}^{\mathrm{shock}}=0, J_{K,t}^{\mathrm{share}}=0, J_{K,t}^{\mathrm{cp}}=1,\\
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
