# Glossary

## Event

A structured representation of a change, occurrence, action, observation, or state transition.

## Event Frame

A compressed structured event record containing fields such as who, what, when, where, why, and how, plus optional state vectors, confidence, causal links, and residuals.

## Microscopic Substrate

The physical, simulated, biological, robotic, software, or computational description from which task-relative event frames are coarse-grained. This does not assert a discrete Planck-scale substrate.

## Coarse-Graining

The mapping from a fine-grained substrate history to a lower-dimensional event frame or event trajectory. Fine-grained describes retained detail and does not impose a topology.

## Intervention-Effective Event

A distinction whose effect on a target exceeds a declared threshold under a randomized or otherwise identified intervention. Without identification, the framework reports predictive sensitivity instead.

## Event Sparsity Hypothesis

The hypothesis that predictively effective distinctions form a small held-out ablation fraction of a finite declared candidate set. A separate causal fraction is defined only when intervention effects are identified.

## Temporal Resolution

The chosen precision of the event time field. A model may choose coarse resolution such as seconds or finer resolution such as microseconds, subject to measurement quality and computational budget.

## Candidate Event Frame

An event frame instantiated or considered at a chosen temporal resolution before it is known whether the frame is intervention-effective or worth retaining.

## 5W1H Ontology

An event-frame schema organized around: who, what, when, where, why, and how. In EventFrame, these are not fundamental physical categories; they are typed fields used for compressed prediction and comparison.

## Event State

A representation of the system before, during, or after an event. May include symbolic fields, vector fields, graph links, and latent variables.

## Event Transition

A mapping from one event state to a later event state.

## Event Confluence

A many-to-one process in which multiple event streams or event frames become representable as a single larger event, aggregate, or macro-event.

## Event Divergence

A one-to-many process in which a small event distinction, perturbation, or intervention leads to multiple downstream event branches or materially different predictions.

## Event Stream

A temporally ordered event trajectory or subtrajectory that can merge with other streams or branch into multiple downstream streams.

## Event Frame Group

A set of event frames treated as equivalent or jointly represented under a chosen abstraction, confluence, cache key, or projection.

## Representative Event Frame

A concrete frame retained for traceability. It is not sufficient to establish group stability; a coverage-aware context audit set is required for divergence tests.

## Audit Set

A set of prediction contexts anchored in a group, containing boundary, uncertain, and sampled cases with declared context-space coverage metadata. Outcomes estimate disagreement in the externally fixed target law; the candidate's own forecasts cannot serve as truth. The group separately retains at least one concrete event frame for traceability. The audit set certifies unseen contexts only under exhaustive coverage or a verified continuity bound.

## Prediction

The estimation of a future event frame, event state, or transition from current and prior event context.

## Prediction Context

The finite event history used as input to a prediction step, usually written as \(C_t = e_{t-k+1:t}\) for a context of length \(k\).

## Compressed World/Context State

A runtime state \(X_t\) assembled from the current event context, active memory state, local graph, and control constraints. It is the object used when the system must decide not only what event is next, but what memory, graph edge, retrieval route, response mode, or control branch should be used next.

## Runtime Prediction Packet

A predicted operational packet \(\widehat{\mathbf y}_{t+1}\in\mathcal Y_{\mathrm{pkt}}\) produced by the typed packet operator \(\oplus_Y\). It may include memory nodes, graph edges, retrieval lane, compaction risk, response mode, and an optional control branch.

## Retrieval Lane

The selected retrieval route or source family for the next prediction or response, such as action-residual cache, general residual cache, episodic memory, graph lookup, or slow-path retrieval.

## Compaction Risk

An estimate that compressing context, memory, or event detail will hide distinctions that matter for the current prediction target.

## Response Mode

The selected mode of response or action, such as direct answer, clarification request, defer-to-slow-path, tool use, or control action.

## Robot/Control Branch

An optional runtime output specifying an embodied, robotic, tool, or external-control branch. Implementations without such a system may set this component to null or no-op.

## Particle Set

A weighted set of candidate hypotheses, abstraction choices, retrieval routes, or control branches. Tightening particles means reweighting, pruning, or resampling this set after usefulness feedback.

## Baseline Predictor

A model, rule, or procedure that produces an initial event prediction before residual correction.

## Prediction Horizon

The future interval \(H\) over which marked events or the no-event outcome are forecast.

## Residual Prediction

A prediction strategy that stores a horizon-indexed typed record with independently interpreted point-template and forecast-law correction components. A post-horizon event cannot retroactively become the point residual of an expired forecast.

## Residual Composition

The typed point-template operation \(\oplus_E\) encodes the posterior-aware base template, norm-clips a point residual, projects into an admissible operator set, and decodes the result. A separately tagged law residual drives a declared full-outcome Markov kernel after the posterior-predictive base law; its no-event transitions are explicit. The components are not semantically interchangeable; a fixed decision rule aligns mark and time, while joint forward tests validate the complete bundle.

## Temporal Loss

A bounded event-aware diagnostic that assigns maximum error to a wrong event mark or incorrect no-event decision and otherwise measures normalized timing error. It is not the primary training objective.

## Proper Predictive Score

A score for a full predictive distribution that is minimized in expectation by reporting the forecaster's true distribution. EventFrame uses it as the primary probabilistic-fidelity metric for marked event time and censoring; the complete system-design objective is composite.

## Pre-Observation Risk

An admission score computed only from information available before the next event. It gates fast-path corrections.

## Post-Observation Event Action

A bounded realized system score computed after the next outcome. It combines a preregistered bounded transformation of predictive loss with declared abstraction, edge, and uncertainty diagnostics. The untransformed proper score remains the forecast-comparison quantity.

## Threshold Clamp

A bounded decision rule that maps an error magnitude to a fixed interval, usually \([0, 1]\), so that invariance and cache-reuse tests are not dominated by outliers.

## Residual Cache

A memory structure storing reusable transition corrections. At prediction time only the as-of snapshot may be read, and reuse requires declared distance, confidence, effective-support, age, epoch, forecast-horizon equality, compatibility-margin, and provenance gates.

## Residual Lookup

The process of retrieving a cached residual correction whose key is sufficiently similar to the current prediction context.

## Action-Residual Cache

A low-latency residual cache keyed by a compact action signature. It stores a residual correction with confidence, support count, and age metadata so the fast path can reuse correction patterns when validity checks pass.

## KV Episodic Cache

A key-value memory structure storing prior event episodes. Keys represent retrieval conditions; values represent event frames, trajectories, or summaries.

## Bounded Bayesian Frontier

A bounded as-of nominated set formed from vector retrieval, sheaf-inspired compatibility neighbors, and incoming or outgoing relationships already present in the event graph. It lies inside a declared finite candidate universe. The frontier-all reference policy cheaply updates every evidence-ready member; an activation threshold selects bounded deep review without suppressing that update. Neither operation updates the entire corpus. Graph children may be nominated, but they cannot update a posterior until evidence is available and do not reveal future child outcomes.

## Bayesian Activation Score

A frozen weighted score combining vector relevance, neighbor compatibility, novelty, and source independence. Structurally critical candidates may receive a lower clamped threshold. It is used only by the threshold-selective policy. The complete admission probability still covers nomination and evidence readiness under both policies.

## Posterior-Predictive Base

The complete marked-time/no-event law obtained by integrating each declared predictive kernel against its valid effective posterior and combining the bucket laws with frozen weights. It is the base law corrected by the residual kernel and scored by the proper loss; the original baseline is used only when no valid belief bucket is available.

## Bayesian Model Coherence

For an ordinary posterior-predictive claim, one declared joint kernel over evidence and next outcome has an evidence marginal dominated by a declared measure and an outcome marginal satisfying the displayed context-sufficiency identity. Because the scored outcome kernel does not separately consume the evidence packet, the joint kernel also factorizes into that evidence density and outcome kernel conditional on the declared parameter and context. If this fails, the predictive kernel must retain the evidence or additional history. Separately modeled components remain modular belief-conditioned forecasts; favorable calibration does not create a missing joint-model identity.

## Certified Admission Support

The histories on which an analytic or simultaneously valid lower bound for the complete policy-indexed admission probability exceeds a frozen positive floor uniformly over the declared parameter family. Admission-corrected full-stream claims are limited to this region. Under frontier-all, admission includes nomination and evidence readiness; under selective admission it also includes the threshold. Never-nominated histories and objects outside the candidate universe are uncertified unless an independent exhaustive or envelope argument covers them.

## Residual Motion Certificate

A fixed-reference certificate that determines whether a residual remains valid after its posterior-predictive base moves. Law-bearing records require a non-negative certified law-motion margin, point-bearing records require a non-negative certified template-motion margin, and joint records require both. Each bound includes statistical uncertainty and posterior-approximation error propagated through the predictive kernel, fusion rule, and applicable template map; a plug-in distance alone is not a certificate.

## Admission-Conditioned Working Posterior

The result of updating only on admitted evidence without proving conditional ignorability or using a valid admission-conditioned likelihood. It may be useful operationally, but it is not claimed to be calibrated for the full event stream.

## Anti-Pigeon Posterior Sharing

The rule that events may share one cached posterior only while an external target-law divergence certificate, effective-support, horizon, epoch, and provenance checks pass. Its guarantee is empirical and conditional on the target-law estimator, audit coverage, simultaneous uncertainty procedure, and any continuity bound attaining their stated coverage. Divergent or uncertified events receive separate posterior keys.

## Bayesian Group Comparison

A bounded practical-equivalence diagnostic over member-level sufficient statistics. It may propose share, split, uncertain, and a bounded borrowing weight, but cannot publish an Anti-Pigeon certificate or mutate posterior keys. Positive sharing still requires independent external target-law evidence.

## Practical Equivalence

A declared tolerance-based relation used when exact equality is too strict for operational pooling. In the Bayesian group diagnostic, its probability is the posterior mass for which every member parameter lies within a frozen maximum pairwise width. This probability is not the complement of the shared-versus-split model probability, and crossing its threshold proposes sharing without authorizing it.

## Anti-Pigeon Shock Revocation

A fail-closed transition that removes an already active sharing certificate when full-stream or independently audited member evidence crosses the frozen split threshold, optionally together with a changepoint. It materializes separate posteriors and invalidates shared residual state but cannot certify a replacement merge. Shared pooled evidence may be discounted while member-level divergence statistics retain full weight.

## Bayesian Elastic Rank Delta

A hard-capped correction applied after bounded external retrieval and before packing. Packing-boundary score separation controls plasticity, while an independent accepted-path reliability value authorizes the move. Rank certainty is not a posterior probability and the operator does not alter the proper-scored forecast law.

## Packing-Boundary Certainty

The clipped normalized score gap between the last initially packed candidate and the first initially excluded candidate. It measures how settled the rank boundary is under the returned retrieval scores, not whether an answer is true.

## Correction Reliability

A separately declared value in \([0,1]\) that is zero unless an accepted Bayesian posterior, certified residual, or versioned graph-compatibility path generated the raw rank correction. It gates the correction even when certainty modulation is disabled.

## Bounded Changepoint Monitor

A capped Bayesian run-length monitor combined with a frozen-warm-up, two-sided cumulative detector and cooldown. It can invalidate dependent local state and nominate recalibration, but its claims are limited to the admitted or independently audited stream that feeds it.

## Coupled Learning State

The versioned posterior, residual, epoch, abstraction, and graph state published atomically to prediction readers. Finite publication and invalidation budgets, hysteresis, cooldowns, and deterministic conflict ordering bound same-evidence-epoch thrashing; they do not prove convergence across an unbounded drifting stream.

## Omitted-Influence Audit

An independent, design-weighted shadow sample of inactive candidates used to compare the complete scored local forecast with the forecast after one audited expansion. The declared metric is normalized Jensen--Shannon divergence, and a simultaneous sequential upper confidence procedure covers buckets, expansions, and repeated decisions. A plug-in disagreement is not a certificate.

## Bayesian Update Ladder

Four resource-aware stages: bounded cached updating, bounded changepoint monitoring, optional event-pattern refinement, and deep particle, variational, or unrestricted model-comparison inference. The bounded proposal-only group comparator is a slow-path diagnostic with a declared group cap. Only stages with declared deterministic caps belong on a hard-latency fast path.

## Property Fuzzing

A validity-constrained method for testing predictor sensitivity to selected event properties. It is not causal evidence by itself.

## Background Fuzz Incubation

A bounded proposal queue nominated after a successful low-certainty recall. Nomination reuses the already retrieved semantic frontier and does not execute perturbation analysis inline. An idle-gated worker later rejects stale snapshots, runs bounded validity-constrained fuzzing, and emits review proposals only. Queue-selected results do not represent the unselected population without an independent coverage design.

## Invariant

A property or relation that remains stable under a defined class of event perturbations.

## Predictive Chain Translation

A proposal-only relation between two declared, aligned baseline/revealed trajectories. The mapped distinction must propagate through every stage, all non-target 5W1H coordinates must remain unchanged, and the signed predictor-effect defect must stay below a frozen threshold. Terminal erasure with small movement is classified as a higher-order invariant instead. A failed intermediate square is divergence even when endpoints agree. The observed-path relation does not discover its own maps or establish causality.

## Causal Chain Translation

The stronger claim that identified intervention transition operators commute under declared cross-domain maps and transport assumptions. Ordinary explanatory or predictive graphs do not satisfy this definition merely because their observed paths align.

## Lumpability

A condition under which many detailed states can be aggregated into a coarser state without losing relevant predictive behavior.

## Anti-Pigeon Principle

The repetition gate is a separate source-dependence heuristic and does not redefine the principle below.

A split-side criterion against invalid pigeonholing. A bucket is unsafe when its external target-law future-diameter exceeds threshold. Agreement among a candidate model's own forecasts is diagnostic and cannot certify the bucket. Regime-conditioned divergence requires common support or transport assumptions; causal attribution requires separate evidence.

## Causal Regime

An observed operating condition under which a prediction pattern is evaluated. It is called causal only when intervention or identification assumptions support that interpretation.

## Repetition and Poisoning Gate

A bounded packing-occupancy rule plus an exact-group selected-feedback veto. The reference implementation detects normalized same-lineage repetition, preserves different certified-key namespaces as separate packet candidates, and rejects flagged selected-only outcomes. It preserves stored records and ordinary frontier updates. It is not a truth classifier, authenticated provenance system, global evidence budget, or complete prompt-injection defense.

## Recorded Evidence Lineage

An operational producer/source descriptor, not proof of independent origin. Conversation lineage ignores fresh session, run, citation, and tool-call identifiers. Source authentication and transitive derivation tracking are separate unresolved requirements.

## Fast Path

A low-latency prediction route using only state available immediately before prediction, including certified cached residuals, bounded cached posterior updates, episodic retrieval, or learned approximations. It may perform bounded nonblocking audit nomination after constructing a response, but it does not execute fuzz analysis inline.

## Slow Path

A higher-cost route using deeper computation, search, simulation, external tools, or background refinement.

## Background Refinement

Asynchronous or deferred computation used to improve future predictions, update caches, or test invariants after an initial response.

## Ontology Self-Organization

The slow-path process of revising, splitting, duplicating, or marking 5W1H field assignments when held-out sensitivity and predictive evidence show that the initial ontology is incomplete or misleading.

## Abstraction Compatibility Graph

A graph whose nodes hold predictive laws at possibly different event groups, resolutions, sensors, local models, or agents, and whose edges declare common comparison spaces and maps into them.

## Edge Compatibility Defect

A declared divergence between two node forecasts after both are pushed into the comparison space of their shared edge. It measures predictive agreement unless explicit SCM semantics make a causal comparison valid.

## Sheaf-Inspired Compatibility Scaffold

An abstraction compatibility graph inspired by local-to-global sheaf reasoning and designed so restriction-map identity and composition laws can later be stated and tested. It is not called a sheaf-theoretic construction until those laws and the required assigned structures actually hold.

## Predictive Sheaf Snap

EventFrame terminology for a bounded, slow-path revision of a local predictive compatibility structure. Candidate node, edge, or comparison-map edits are selected on chronological design data, accepted only after later untouched confirmation, and published as an atomic graph-key-epoch version. Externally fixed comparison obligations prevent a candidate from appearing coherent merely by deleting difficult edges. A predictive snap does not establish or promote causal edges.

When an explicit SCM exists, a predictive snap may nominate a separate bounded causal-edit family. Causal publication still requires specified structural equations and independent randomized or otherwise identified intervention evidence; predictive gluing cannot orient an edge.

## Local Reconciliation

A slow-path optimization that trades fidelity to unreconciled local forecasts against declared edge compatibility penalties within an affected neighborhood.

## Refinement Depth

The deepest completed stage in the cumulative upgrade architecture for one case. It is selected from priority, prerequisite gates, and measured cost on a named hardware profile.

## Priority-Weighted Gain

The reduction in predictive loss after weighting cases by a priority assigned before their outcomes are observed. It must be reported with unweighted and priority-stratified results.
