# External Feedback Round 2 Correction Audit

Date: 2026-08-26

This audit records the disposition of the second-round review against the source tree. Reviewer suggestions were checked before editing.

1. **GitHub inline math: rejected as incorrect.** GitHub documents `$`-backtick delimiters as supported inline-math syntax. A live render through GitHub's Markdown API recognized all 627 inline expressions and 140 display expressions with no parse-error marker before this correction. The delimiters were preserved.
2. **Undefined field-loss summary: confirmed and corrected.** The loss now binds `\hat e_{\theta,t+1}^H=\hat e_\theta^H(C_t)` and is defined only when both prediction and observation are marked. No-event cases require a declared missing-aware loss.
3. **Physical-bound scope: confirmed and corrected.** The abstract and ontology now limit the physical citations to a limiting thought experiment for physical substrates and require independent compression arguments elsewhere.
4. **Symbol-index gaps: confirmed and corrected.** The coherent summaries and `\mathrm{lift}_H` are indexed.
5. **Stale objective prose: confirmed and corrected.** The introduction distinguishes the oracle population benchmark from certified finite-family operational selection.
6. **Omitted horizon gate: confirmed and corrected.** Reference-procedure and glossary prose now state horizon equality. Exact- and general-cache formulas retain the same gate.
7. **Evaluation-law/sample overload: confirmed and corrected symmetrically.** `P_{\mathrm{obj}}` and `P_{\mathrm{conf}}` denote generating laws; `\mathcal S_{\mathrm{obj}}` and `\mathcal S_{\mathrm{conf}}` denote realized chronological samples or trajectory blocks. Population and empirical risks now use the corresponding types.
8. **Unspecified density and interval arithmetic: confirmed and corrected.** The substrate is called fine-grained without a topological claim. `\tau(e)` is a real-valued temporal anchor, defaulting to interval onset, while the full interval remains in the event frame.

An adjacent cache-contract mismatch was also corrected: exact-cache prose required provenance but the tuple and indicator did not carry it. Exact entries now store `s_{k_t}` and validate it, matching the general cache and the reference procedure.

The self-adjoint representation remains an intentional finite-dimensional representation choice rather than a claimed theorem. A worked finite instantiation now uses diagonal self-adjoint matrices, an explicit no-event Markov kernel, coherent point lifting, a horizon-gate negative control, proper-score arithmetic, and finite operational selection. Its stipulated values are labeled illustrative and are not empirical validation.

The reviewer's corrected observation about the Anti-Pigeon guard is accepted. No formula change was required: contexts sharing an operational key lie within a terminal bucket, so the key-equality pair family is contained in the same-bucket pair family controlled by the active-bucket diameter bound.
