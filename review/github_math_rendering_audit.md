# GitHub Math Rendering Audit

Date: 2026-08-29

## Symptom

The live GitHub page displayed four specific parse errors and then hundreds of generic "Unable to render expression" boxes, including for trivial expressions.

## Classification

| Finding | Classification | Evidence |
|---|---|---|
| Four malformed display expressions | Confirmed | GitHub's ordinary `$$` Markdown path consumed escaped punctuation before math rendering, changing `\left\{` to `\left{` and `\!` to `!`. |
| Hundreds of later formulas are mathematically invalid | Stale | The failure suffix included valid expressions such as `i` and `N_t`. |
| Single-page renderer exhaustion | Confirmed | The live page contained 1,275 math nodes. GitHub rendered 564 successfully, reported four real parse failures, and returned a generic failure for every node after index 567. Waiting did not retry them. |
| Canonical source or PDF mathematics must be reduced | Rejected | The fully typeset `build/paper.md` and PDF remain valid; the fault is specific to GitHub's single-page rendering path. |

## Patch Invariant

- Preserve every display equation and its exact mathematical source.
- Protect display equations with GitHub's fenced `math` syntax so Markdown cannot consume TeX punctuation.
- Protect retained inline expressions with GitHub's documented backtick-delimited inline-math syntax.
- Keep the single-file GitHub edition below 360 math nodes, leaving margin below the stricter live-client failure boundary observed after fenced display math was introduced.
- Render repeated symbol-only references as exact monospace notation rather than requesting another math render.
- Preserve `build/paper.md` as the canonical fully typeset Markdown assembly and keep the PDF fully typeset.

## Verification

The first generated edition contained 204 display nodes and 330 inline nodes. GitHub's Markdown API recognized all 534, but the live client exposed one fenced `cases` row-break defect and then entered generic failure. A `\cr` substitution was tested and rejected because GitHub still reported the same missing-end error. The corrected GitHub edition expresses that one piecewise rule as two equivalent conditional equalities, while the canonical assembly retains the `cases` form. It contains 204 display nodes plus 150 selected inline nodes, for 354 total. Repeated audit reloads produced progressively earlier generic-failure suffixes, consistent with transient renderer rate limiting; final acceptance therefore distinguishes specific parse errors from generic exhaustion and requires a clean fresh-session or post-cooldown pass.
