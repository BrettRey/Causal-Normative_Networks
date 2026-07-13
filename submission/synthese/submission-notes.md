# Synthese Submission Notes
<!-- SUMMARY: Package state and upload checklist for the Synthese submission · status: package ready, awaiting Brett's upload · updated: 2026-07-13 -->

## Gate results (2026-07-13)

- **Legibility gate A (cold read): PASS.** Three cross-model hostile readers (Claude subagent, Codex, Copilot) on the extracted opening: 0/3 MISSING on problem, debate, gap, and contribution; 2/3 advance; convergent problem statements. Scored with `coldread.py score`. Gemini CLI is dead (free tier discontinued, "migrate to Antigravity"), so Copilot substituted for Brett's approved Gemini slot. Copilot's lone reject demanded demonstrated payoff within the opening itself; that demand is answered by §4's division-of-labour and discrimination-gain passages, not page one. Codex's advance note ("must prove the graph vocabulary explains rather than redescribes") is the residual Reviewer-B pressure the §2 projectibility passage and the read-off restriction now answer.
- **Legibility gate B (terminology): PASS**, exit 0 against `planning/terms.md` (Synthese free/earned split; free rows are either reader-owned or glossed-with-detector-artifact, each with an auditable location).
- **Correctness:** clean build (22 pp), no undefined references, biber error-free, all 32 cited keys present with no unused entries, one trivial 5.6pt overfull vbox, style linter shows only false-positive "false range" heuristics on literal path descriptions.
- **Anonymity:** `submission-checks.md` all CLEAN (tex, PDF text, PDF metadata, source bundle); PDF author field absent.
- **Known intentional deviation:** this repo uses `references-standalone.bib` (public-build design, DECISIONS 2026-05-25), so the gate smoke-test's "missing references.bib" is expected.

## Package contents (`submission/synthese/`)

- `synthese-anon.pdf` — anonymized manuscript, 22 pp.
- `main.anon.tex` + `anon-bundle/` — scrubbed LaTeX source (tex, scrubbed preamble, bib) for the source upload.
- `title-page.pdf` / `title-page.tex` — author block, ORCID, contact, acknowledgements (AI disclosure with model names: Claude Opus 4.8 & Fable 5; ChatGPT GPT-5.6), declarations, preprint pointer.
- `cover-letter.md` — to paste into Editorial Manager.
- `submission-checks.md` — anonymity scan output.
- Regenerate everything with `python3 scripts/build_synthese_submission.py`.

## Before upload (human steps)

1. Confirm the live Synthese submission guidelines in a browser (Springer cookie-walled agent access on 2026-07-13; parameters used here came from search snapshots: no fixed length limit, LaTeX source + PDF, anonymized review, acknowledgements on title page). Include the current Springer Nature AI-policy text in the same check: the title-page disclosure follows the disclosure model (documented use, no AI authorship, full human responsibility), and as last verified no section-by-section attribution is required, but these policies change fast (GLM-5.2 review, 2026-07-13, flagged the same).
2. Submit via Editorial Manager: https://www.editorialmanager.com/synt
3. Record the manuscript ID here, in `STATUS.md`, and in `PORTFOLIO.md`; update the CV/website surfaces via /status-surface-update.

## Watch items carried from the venue record

- A referee may want deeper natural-kinds coverage (Boyd beyond 1999, Millikan, Franklin-Hall); prepared position: the Khalidi-forward scaffold is deliberate and defended in §2.
- Copilot's cold-read note suggests a possible one-sentence §1 forward-pointer that the division-of-labour rival is answered in §4; optional, Brett's call.
- Anticipated referee question (GLM-5.2 review, 2026-07-13): how does the field parameter differ from Epstein's frame principles or Searle's Background beyond parameterizing the graph? Prepared position: §7 argues the field parameterizes the network rather than sitting in it as a node (the Hindriks node-vs-parameter point), with Epstein's frame/anchor machinery explicitly backstage; the field adds the practice-relative projection repertoire, not a rival metaphysics. Triage of the same review found Figure 1's legend already maps one-to-one onto the four graph roles, so no manuscript change was made.
