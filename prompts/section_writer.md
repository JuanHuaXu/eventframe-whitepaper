# Prompt: Section Writer

Use the repository files as the complete source of truth. Draft the requested white paper section.

Constraints:

- Do not mention any private project, chatbot, product, or agent name.
- Use `spec/project_brief.md`, `spec/glossary.md`, `spec/notation.md`, `spec/claims.md`, `spec/references.md`, and `spec/outline.md`.
- Maintain a conservative academic tone.
- Define terms before using them.
- Include equations only when they carry real explanatory load.
- For every equation, define variables and interpretation.
- Pair formal math with a conceptual explanation of why the math is used.
- When a section introduces a computational construct, explain how it would be run during prediction.
- Mark uncertain claims as hypotheses or proposed methods.
- End the section with a short transition to the next section.

Output:

- Write the section to the appropriate `src/NN_section_name.md` file.
- Add newly introduced terms to `spec/glossary.md` only if necessary.
- Add newly introduced claims to `spec/claims.md` only if necessary.
