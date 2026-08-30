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
- Keep the single-file GitHub edition below 540 math nodes, leaving margin below the observed failure boundary.
- Render repeated symbol-only references as exact monospace notation rather than requesting another math render.
- Preserve `build/paper.md` as the canonical fully typeset Markdown assembly and keep the PDF fully typeset.

## Verification

The generated GitHub edition contains 204 display nodes and 330 inline nodes, for 534 total. GitHub's Markdown API recognizes all 534 as math renderers, preserves the protected brace and spacing commands, and reports no server-side malformed-math fallback. Live client verification is required after publication because the renderer ceiling occurs after GitHub's client-side math pass.
