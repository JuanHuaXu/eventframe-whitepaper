# 2. EventFrame in Plain Language

EventFrame is a memory and prediction layer for systems that must retrieve useful prior experience without treating an entire transcript as one undifferentiated block. It converts experience into compact internal records, uses those records to find a bounded set of relevant candidates, and hydrates full text only after ranking and packing are complete. The 5W1H representation is internal to EventFrame; an agent or chatbot can continue to send and receive ordinary text through its existing memory contract.

## What an event frame represents

An event frame is not necessarily one chat turn. It is one complete, task-relevant episodic segment at the chosen temporal resolution. A short exchange may yield one frame, several turns may combine into one frame, and one dense turn may contain several frames. Each frame records who participated, what happened, when and where it happened, why it may have happened, how it happened, and what uncertainty or provenance accompanies those fields.

The frame is a compressed representation rather than a claim about fundamental reality. EventFrame keeps distinctions that may matter for prediction, intervention, retrieval, or later review. Details that do not currently matter can be compressed, while uncertainty remains explicit rather than being promoted to fact.

## The normal prediction path

The fast path follows one bounded sequence:

1. Convert the current situation into one or more internal event frames.
2. Ask the vector store for a bounded candidate frontier, ordinarily tens or hundreds of frames rather than the whole corpus.
3. Expand that frontier with bounded graph neighbors, including prior and next explanatory or causal candidates that are available as of the query time.
4. Use current Anti-Pigeon certificates to assign shared or separate posterior keys before updating beliefs. Similar-looking events without a valid sharing certificate remain separate.
5. Apply the cheap update to every evidence-ready member of that frontier under its assigned key. Expensive analysis remains selective; mark exact repeated claim/lineage decisions for the separate selected-feedback veto.
6. Build a baseline forecast from the accepted beliefs, then apply only residual corrections whose provenance, age, horizon, confidence, and version checks still hold.
7. For memory retrieval, apply a bounded rank correction after external retrieval, then pack under repetition-occupancy and token budgets. Hydrate the selected records' full text only after this semantic work is finished.
8. Return the forecast or packed memory context immediately.

This ordering matters. The answer must survive retrieval into the candidate frontier before EventFrame can rerank it. A packer that truncates to ten items before a fifty-candidate reranker runs has already discarded forty candidates and cannot recover them.

After a successful low-certainty recall, an implementation may also place a bounded fuzz nomination on an incubation queue. Nomination reuses the already retrieved frontier and does not run perturbation analysis before the response. A background worker may later test the proposal while the serving path is idle; any resulting invariant or translation remains a review proposal rather than an automatic memory or ontology edit.

## Learning after the outcome

Learning happens after the relevant outcome becomes available. EventFrame records whether the forecast or retrieved memory was useful, updates the corresponding belief and residual confidence, and checks whether the current abstraction remains valid. It does not use future outcomes while making the earlier prediction.

Most updates are small and local. The slow path handles cases where evidence conflicts, uncertainty is high, a regime appears to have changed, or a shared abstraction may be hiding important differences. That path can audit omitted candidates, compare shared and split models, recalibrate probabilities, test perturbations, revise graph structure, or invalidate stale cache entries without blocking the current response.

## Anti-Pigeon and changing categories

Anti-Pigeon is short for resisting pigeonholing: the framework should not keep using a convenient historical category after the variables that made it useful have changed. Candidate retrieval proposes which events appear related. Bayesian comparison can suggest sharing, splitting, or uncertainty. Anti-Pigeon retains final authority over sharing because it tests whether members of a proposed group still have compatible downstream behavior under external evidence.

This supports both directions of revision. Events that repeatedly behave alike may share evidence and eventually join into one predictive group. Events that once looked alike may split after a changepoint or a revealing outcome. Event streams can therefore merge like tributaries or diverge when a small distinction becomes consequential.

Every group retains at least one concrete traceability frame and a broader audit set. The concrete frame makes the abstraction inspectable; the audit set tests whether the group is hiding divergent boundary cases. One representative alone is never treated as proof that the whole group is stable.

## Repetition is not corroboration

Repetition protection is separate from Anti-Pigeon. Ten recaptures of one assertion should not automatically fill ten memory slots or count as ten independent confirmations. The implemented gate limits similar same-lineage records inside the packet and rejects exact-group duplicates on the selected-feedback route, subject to the separate-bucket exemption defined in Section 6. It preserves stored records and ordinary frontier updates. It does not decide which assertion is true, authenticate a source, or prevent repetition across every future feedback request.

## Invariance and domain translation

Fuzzing one variable can reveal two different structures. If the variable changes upstream but the final result and prediction remain effectively unchanged, EventFrame treats that distinction as a candidate for a higher-order abstraction. If the corresponding variable changes at every aligned stage of another domain, while all unrelated variables remain fixed, EventFrame treats the pair as a predictive translation candidate. A temperature chain written in Celsius and the same chain written in kelvins is a simple declared-map example: the raw values differ, but the frozen conversion explains how they correspond.

Translation must hold through the chain, not only at its endpoint. If an intermediate stage changes an unrelated variable, endpoint agreement does not rescue the mapping. Anti-Pigeon keeps the chains separate until external evidence supports the proposed correspondence. The ordinary runtime calls this predictive chain translation. It uses the stronger causal label only when intervention evidence and a structural causal model justify it.

## Fast path and slow path

The fast path is designed for bounded local work: retrieve a capped frontier, update cached sufficient statistics, reuse valid corrections, rerank a bounded packet, optionally enqueue a bounded audit nomination, and respond. The slow path performs particle methods, broad model comparison, fuzz and abstraction audits, changepoint review, compatibility analysis, and recalibration asynchronously or under explicit resource budgets.

Future hardware may permit more slow-path stages to run more often, but it does not change their meaning or remove their evidence requirements. A faster machine cannot turn model sensitivity into causality, make a stale residual valid, or allow a proposed group to certify itself.

## A compact example

Suppose an agent must recall how a deployment failure was fixed. The vector store returns fifty compressed event frames. The correct repair is initially ranked outside the ten-item packet. EventFrame sees that the top ten have weak boundary certainty, finds that the lower-ranked repair matches the current mechanism and graph neighborhood, and applies a bounded positive rank correction. The repair enters the packed context, and only then is its full transcript text loaded for the agent.

Later, explicit feedback says whether that repair was useful. Repeated useful outcomes strengthen the local belief and correction. Strong contradictory evidence can rapidly revoke a previously shared group, demote stale confident knowledge, and preserve separate posteriors until new evidence justifies another merge.

The remainder of the paper turns this lifecycle into typed objects, measurable claims, and falsifiable experiments.
