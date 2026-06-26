# Codex Master Prompt

Use this repository as the complete source of truth. Do not assume access to prior chats. Do not mention any named agent system, chatbot, product, or private project.

Goal: develop this repository into a self-contained white paper titled:

EventFrame: A Mathematical Framework for Event-Centric Prediction

Process:

1. Read all files under `spec/`.
2. Create `src/` section files according to `spec/outline.md`.
3. Draft one section at a time.
4. After drafting each section, run a math review and red-team review.
5. Patch the section based on review files.
6. Keep glossary, notation, claims, and reference placeholders synchronized.
7. Assemble a final `build/paper.md`.

Do not generate PDF until the Markdown paper is internally consistent.

Hard requirements:

- Self-contained.
- Conservative claims.
- No dependency on prior conversation.
- No product lock-in.
- Equations must be explained.
- Experiments must be falsifiable.
