# STATUS.md - Causal-Normative Networks

**Last updated:** 2026-05-26
**Current phase:** JSO blind submission package regenerated after final micro-edits; ready for human upload/review
**GitHub:** https://github.com/BrettRey/Causal-Normative_Networks
**Working submission title:** Effective without Warrant: Causal-Normative Networks and the Social Life of Status
**Working venue:** Journal of Social Ontology, regular article

## Overview

Foundational companion to the act-kinds paper. Where the act-kinds paper uses causal-normative networks to explain the projectibility of moral act-kinds, this paper makes *causal-normative network* itself the explanandum.

Working orientation: Khalidi-forward. Khalidi supplies the network-order/projectibility frame; this paper extends that frame from ordinary causal networks to typed causal-normative networks. Boyd is not the scaffold, but his accommodation/projectibility point now supports the compact field-relative projectibility claim in Section 7.

## Current Thesis

Some social and moral explanations need causal relations and normative transitions represented in one coupled structure. A causal-normative network has three directed edge types (causal, normative-transition, recognitional) plus a non-directed constitutive tie. Its key payoff is projectibility across typed edges plus the assessment vocabulary: social efficacy, institutional field-validity, communal successful conferral, recognitional fit, enforceability/finality, and moral warrant.

Misrecognition and wrongful conferral are diagnostic. A status-assignment can be socially effective, and sometimes field-valid or successfully conferred, without acquiring moral warrant. Discrimination is now treated as wrongful conferral at regime scale, not merely as false belief or local tracking failure.

## What Exists Now

- `main.tex`: current polished draft with all sections written, two TikZ figures, two tables, and review rounds addressed.
- `main.pdf`: current build, 18 pages.
- `submission/jso/`: blind JSO package generated from `scripts/build_jso_submission.py`, including DOCX, RTF, internal-check PDF, figures, blind source, and submission checks.
- `abstract.md`: synced to the current abstract framing.
- `planning/brief.md`: original design brief, still useful for architecture and title options but partly superseded by the current draft.
- `planning/source-map.md`: updated section-by-section source map and local-source inventory.
- `references-standalone.bib`: public-build bibliography extracted from verified central entries, with the added ALI Judgments entry verified against ALI's official publication page.
- `references-local.bib`: scratch file only for future verified additions; current public builds use `references-standalone.bib`.
- `literature/`: local source pack, including moved Downloads sources for Ásta, Weinberger, Epstein, Searle 1995, Fraser/Honneth, and copied Pullum/Scholz. This directory is ignored and not pushed to GitHub.

## Review State

The implementation pass addressed the 2026-05-26 GPT-5.5 xhigh field/validity board saved at `reviews/review-board-2026-05-26-gpt55-xhigh-field-validity.md`. A second post-implementation board is saved at `reviews/review-board-2026-05-26-gpt55-xhigh-post-implementation.md`; its main actionable items have now been implemented and polished.

The current draft incorporates:

- assessment vocabulary: efficacy / field-validity or successful conferral / moral warrant;
- regularized edge inventory: three directed edges plus a constitutive tie;
- recognition as fit, mis-fit, or no target;
- broader normative-transition sources: performances, rules, statuses, and transition events;
- §6 distinction between local misrecognition and wrongful conferral;
- Figure 2 as wrongful conferral, with harm downstream of exclusion/sanction;
- weakened overclaims about projectibility and explanatory reach;
- optional Pullum/Rogers formal analogy;
- Fraser/Honneth guardrail against over-recognition accounts of oppression;
- simplified field account: a field is an ordinary normative practice or domain, not an HPC or a front-door Epstein apparatus;
- Boyd supports field-relative projectibility/accommodation; Messick 1995 is only a limited analogy for validity as interpretation/use-relative;
- network-as-representation language: grounding and anchoring are not replaced by the graph;
- a field-indexed projection ledger in §4 and a projectibility-forward conclusion;
- a §6 assessment table separating social efficacy, institutional field-validity, communal successful conferral, recognitional fit, enforceability/finality, and moral warrant;
- judgment as the institutional authorized-recognition case, with cautious ALI Judgments support;
- specified wrongful-conferral machinery: conferring agents, base/ascription, conferred standing, and later recognition over time;
- a direct answer to the strongest rival: grounding/anchoring plus causal mechanisms do useful work, but the network represents the cross-edge projection profile;
- Figure 2 as wrongful communal conferral, not a simple false-recognition diagram;
- polished abstract and table lead-ins, with judgment/legal language softened and source-tethered;
- final submission-prep micro-edits from the May 26 assessment: status-assignments in the abstract, distributive payoff sentence, Table 2 diagnostic-grid lead-in, and conclusion naming causal uptake, normative transition, recognition, and constitutive ties.

Declined for this paper: Lewis, Brandom, Hacking, and Haslanger. They pull toward adjacent projects; Sbisà, Ásta, Epstein, Searle, Weinberger, Kohler-Hausmann, Hu, and Fraser/Honneth are enough for the present argument.

## Open Decisions

- **Title.** Working submission title is "Effective without Warrant: Causal-Normative Networks and the Social Life of Status." Earlier alternatives remain in `planning/brief.md`.
- **Target venue.** Working target is Journal of Social Ontology regular article.
- **Act-kinds bridge sentence.** Applied to the live sister manuscript on 2026-05-25.

## Next Actions

1. Open and spot-check `submission/jso/effective-without-warrant-jso-blind.docx` in Word/LibreOffice before upload; local render-to-PNG QA is blocked here because `soffice` is not installed.
2. Upload the blind DOCX to JSO if the title/venue still look right.
3. Keep the LaTeX canonical draft as the source of truth; regenerate the package with `python3 scripts/build_jso_submission.py` after any further manuscript edits.

## Relation to the Act-Kinds Paper

Sister project: `papers/Moral_act-kinds_as_nodes_in_causal-normative_networks/`. The act-kinds paper doesn't require this one; it needs only enough of the network idea to make its argument intelligible. This paper explains why that apparatus is legitimate.
