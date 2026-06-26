# External Critique Response

## Source

Reviewed `/Users/clawdius/Downloads/EventFrame_Review_and_AntiPigeon_Critique.md`.

## Finding Classification

- Confirmed: Anti-Pigeon was mostly philosophical in the paper draft. Action: add a future-divergence split criterion and split operator to the notation spec and abstraction section.
- Confirmed: Lumpability should be presented as the merge-side dual of Anti-Pigeon. Action: state the merge/split duality explicitly and include hysteresis-style threshold guidance.
- Confirmed: The experimental plan should test Anti-Pigeon directly. Action: revise the lumpability experiment to estimate intra-bucket future divergence and require split or divergence-sensitive marking when the threshold is crossed.
- Partially confirmed: The critique says the claims register is missing. The project already has `spec/claims.md` and the assembled paper has a claim map, but Claim 6 needed to reflect the stronger Anti-Pigeon criterion. Action: update Claim 6.
- Partially confirmed: The critique asks for fast-path versus audit-path/runtime architecture and combined memory. The current paper already has fast/slow path runtime and complementary episodic/residual memory sections, so no broad rewrite is needed.
- Partially confirmed: The critique asks for residual mathematics and O(1) residual cache math. The current paper has constrained residual composition and lookup-cost caveats; publication-grade guarantees remain an open problem rather than a safe claim.
- Needs investigation: Multi-field fuzzing and synergy are not yet fully formalized. This should be considered in a future fuzzing expansion rather than patched as a quick equation.

## Patch Decision

Integrate only the confirmed Anti-Pigeon formalization and directly related claim, glossary, notation, and experiment updates. Do not broaden residual-runtime claims or present constant-time lookup as guaranteed.
