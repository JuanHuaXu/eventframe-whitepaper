# Revision 2 Review Response

## Source

Reviewed `/Users/clawdius/Downloads/EventFrame_Whitepaper_Review_v2.md`.

## Finding Classification

- Confirmed: The assembled paper had a claim map but no body-level claims section. Action: add an explicit `Claims Register` section after the introduction.
- Confirmed: The action-residual fast path was under-specified. Action: add action-key lookup, validity conditions, confidence update, and expected `O(1)` caveat.
- Confirmed: The paper separated episodic and residual memory but did not describe their combined prediction flow. Action: add residual-first and episodic-fallback flow to the memory section.
- Confirmed: Fuzzing did not yet explain 5W1H ontology self-organization. Action: add field influence scores and retain/migrate/split/uncertain update rules.
- Confirmed: The runtime architecture needed an explicit flow. Action: add a Mermaid architecture diagram and update the fast/slow path steps.
- Confirmed: CFS-inspired language benefits from a concrete surrogate action. Action: add \(\mathcal{A}_{event}\) as a measurable runtime surrogate, while explicitly stating it is not a physical CFS action.
- Recommendation only: Full BibTeX replacement, robotics and skill-transfer chapter, and counterfactual graph-learning chapter are publication-stage additions. They should be planned separately instead of rushed into this patch.

## Patch Decision

Integrate the core runtime additions that complete the EventFrame architecture while preserving conservative claims. Defer domain-specific robotics expansion, full reference conversion, and counterfactual graph-learning as future chapters or open-problem work.
