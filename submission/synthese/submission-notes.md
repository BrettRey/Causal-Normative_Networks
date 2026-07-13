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

## Guidelines confirm (DONE 2026-07-13)

Brett pasted the live guidelines page during registration; four deltas found against the package and all fixed same day:

- **Abstract 150–250 words:** was 126; now 185 (concrete projections restored; interventionist-typing/misrecognition sentence added).
- **Keywords 4–6:** cut ten to six (social ontology, social kinds, projectibility, causal-normative networks, recognition, discrimination); pdfkeywords and abstract.md synced.
- **Title page:** affiliations now carry city/country; "Statements and Declarations" heading with competing interests, funding, and preprint statements (guidelines: submissions without declarations "will be returned as incomplete").
- **LLM documentation in the manuscript itself:** the anonymized manuscript now ends with a non-identifying "Statements and declarations" section documenting LLM use beyond AI-assisted copy editing; full model names stay on the title page. This tracks Springer's rule that LLM use be documented in the manuscript (no Methods section, so a declarations block), while the copy-editing exemption language mirrors their own.

Also verified: double-anonymized review with reviewer-editor interaction only; no resubmission of rejected papers (n/a); third-person self-citation rule (n/a: no self-citations); footnotes not endnotes (ok); ≤3 heading levels (ok); anon-bundle compiles standalone with XeLaTeX (tested in a clean directory, 22 pp; needs the Charis SIL font, so if Editorial Manager's build system lacks it, the uploaded compiled PDF covers review — upload tex/bib/style files as type "manuscript" per the guidelines note).

Deferred to the accept-but-incomplete stage (per the guidelines' own workflow): de-anonymization, and reference-list conversion toward APA 7 with full DOI links (house biblatex is already author-date; cosmetic conversion is a production-stage task).

## Upload steps (human)

1. Submit via Editorial Manager: https://www.editorialmanager.com/synt (registration in progress 2026-07-13).
2. Record the manuscript ID here, in `STATUS.md`, and in `PORTFOLIO.md`; update the CV/website surfaces via /status-surface-update.

## Watch items carried from the venue record

- A referee may want deeper natural-kinds coverage (Boyd beyond 1999, Millikan, Franklin-Hall); prepared position: the Khalidi-forward scaffold is deliberate and defended in §2.
- Copilot's cold-read note suggests a possible one-sentence §1 forward-pointer that the division-of-labour rival is answered in §4; optional, Brett's call.
- Anticipated referee question (GLM-5.2 review, 2026-07-13): how does the field parameter differ from Epstein's frame principles or Searle's Background beyond parameterizing the graph? Prepared position: §7 argues the field parameterizes the network rather than sitting in it as a node (the Hindriks node-vs-parameter point), with Epstein's frame/anchor machinery explicitly backstage; the field adds the practice-relative projection repertoire, not a rival metaphysics. Triage of the same review found Figure 1's legend already maps one-to-one onto the four graph roles, so no manuscript change was made.
