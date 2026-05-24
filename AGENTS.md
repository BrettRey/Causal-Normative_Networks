# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an academic research paper by Brett Reynolds (provisional title: "Normative Status in Causal Networks"; final title open, see `STATUS.md`). It is the foundational companion to the act-kinds paper (`../Moral_act-kinds_as_nodes_in_causal-normative_networks/`). The act-kinds paper *uses* causal-normative networks to explain why moral act-kinds are projectible; this paper makes *causal-normative network* itself the explanandum.

Role: Editor/Researcher. Deep work welcome (drafting, argument development, sourcing).

Full design lives in `planning/brief.md`. Working state in `STATUS.md`.

## Project-Specific Guidance

- **Animating question:** what kind of explanatory structure contains both causal relations and normative transitions without reducing either to the other?
- **Thesis:** a causal-normative network is a typed, coupled structure (normative statuses alter practical positions; causal mechanisms transmit uptake and response; recognition links connect the two). Neither a causal graph with moral labels nor a normative taxonomy with sociology appended.
- **Keep the four dependence types distinct:** causal, constitutive, normative-transition, recognitional. The whole point is that they compose one network without collapsing into one relation-type. Do not silently reduce normative status to beliefs, sanctions, or dispositions, and do not treat causal talk as mere metaphor for rules.
- **Central opponent:** the forced-choice view (reduce-to-causal or reduce-to-normative), not essentialism. Essentialism is the act-kinds paper's opponent; do not import it here.
- **Four carrying cases:** promise, consent, official judgment or registration, discrimination. Prefer these recurring four over scattering examples.
- **Social efficacy vs moral validity:** a status-assignment can be socially effective while normatively invalid (misrecognition, discrimination). Keep this distinction sharp; it is a main payoff.
- **Relation to the sister paper:** do not conflate the two projects, and do not rewrite the act-kinds paper as this one. A bridge sentence is recommended for the act-kinds paper's Section 3 (see `planning/brief.md`), but applying it needs Brett's go-ahead.
- **Source-grounding (LAW):** legal, speech-act, and deontic claims must come from sources. Verified entries reused from the sister paper live in `references-local.bib`; reuse keys, do not regenerate bibliographic data.

## Build System

This LaTeX project requires **XeLaTeX** (not pdfLaTeX) due to the Charis SIL font requirement.

**Avoid LuaLaTeX** – it tends to run words together in the underlying PDF text layer, breaking copy-paste and accessibility.

### Compilation Commands

```bash
# Full build sequence
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex

# Or use automated build
make              # Full build
make quick        # Single pass
make clean        # Clean artifacts
```

The multiple runs are necessary to resolve all cross-references and citations.

## File Structure

```
Causal-Normative_Networks/
├── main.tex                  # Main document
├── references.bib            # Bibliography
├── .house-style/             # House style snapshot
│   ├── preamble.tex         # LaTeX preamble
│   └── style-rules.yaml     # Style conventions
├── Makefile                  # Build automation
├── CLAUDE.md                 # This file
├── AGENTS.md                 # Synced with this file
└── GEMINI.md                 # Synced with this file
```

## House Style

This project uses Brett Reynolds house style (see `.house-style/style-rules.yaml`).

### Key LaTeX Conventions

**Terms, Mentions, Quotations:**
- Use `\term{}` for terms/concepts (small caps): `\term{definiteness}`
- Use `\mention{}` for mentions/forms (italics): `\mention{the}`
- Use `\olang{}` for object language (italics): `\olang{der Hund}`
- Use `\enquote{}` for quotations: `\enquote{actual quote}`
- Never use raw quotes for mention

**Cross-linguistic Notation:**
- Cross-linguistic: `\textsc{subject}\crossmark`
- Language-specific: `\textsc{subject}\textsubscript{eng}`

**Dashes:**
- Parenthetical: `foo~-- bar~-- baz` (en dash with spaces)
- Ranges: `2001--2025` (en dash, no spaces)
- Compounds: `corpus-based` (hyphen)

**Citations:**
- Parenthetical: `\citep{key}`
- Textual: `\textcite{key}`

**Citations and BibTeX (LAW):**
- Citations and BibTeX entries must NEVER be placeholders
- Citations must NEVER be generated from training data
- LLMs MUST browse the web to find DOIs and verify bibliographic data
- Every citation must be confirmed against an authoritative source
- If you cannot verify a citation, say so. Do not guess. Do not fabricate.

### Writing Style

**Preferred:**
- Use contractions (don't, won't)
- Keep paragraphs ~60 words, max 100
- Direct verbs and short clauses
- Concrete before abstract

**Avoid:**
- Throat-clearers: "It is important to note that..."
- `\paragraph{}` headings (use topic sentences)
- Bold labels in prose
- Hackneyed adverbs: moreover, furthermore

**Document Structure:**
- Use `\section{}` and `\subsection{}` only
- Avoid bullet points for arguments (use prose)
- Use ordinal markers: "first," "second," "third"

**Examples (gb4e):**
```latex
\ea\label{ex:example}
\textit{Example sentence.}
\z
```

## Common Tasks

**Adding References:**
1. Add entry to `references.bib`
2. Protect capitals: `title = {The {Cambridge} Grammar...}`
3. Use `\textcite{key}` or `\citep{key}`

**Building:**
```bash
make              # Full build
make quick        # Fast build
make clean        # Clean up
```

**Git Workflow:**
- Pre-commit hook keeps CLAUDE.md, AGENTS.md, GEMINI.md synced
- Commit often with meaningful messages
- Build before committing to ensure no LaTeX errors

## Multi-Agent Dispatch (MANDATORY)

**Before dispatching multiple agents, ALWAYS ask Brett:**

1. **Which model(s)?** Options: Claude, Codex, Gemini, Copilot
   - Codex is often best for Brett's work
   - Claude and Gemini both have 1M token context windows
   - Different models have different strengths

2. **Redundant outputs?** Should multiple models tackle the same task?
   - Useful for judgment calls (e.g., "Should I add this figure?")
   - Not needed for factual tasks

### CLI Command Patterns

| CLI | Command | Notes |
|-----|---------|-------|
| **Codex** | `codex -p 'prompt' > output.txt &` | Include "Read [PATH] first" in prompt |
| **Gemini** | `cat file.tex \| gemini --yolo -o text 'prompt'` | Must pipe content (file reading broken in YOLO) |
| **Copilot** | `copilot -p 'prompt' > output.txt &` | Fast; add `--allow-all-tools` for file ops |

**Token limits:** Claude 1M = Gemini 1M+ > Codex

See portfolio `CLAUDE.md` or `HPC book/.agent/workflows/multi-agent-review.md` for full patterns.
