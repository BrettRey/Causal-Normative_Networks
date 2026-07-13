# STATUS.md - Causal-Normative Networks

**Last updated:** 2026-07-13
**Current phase:** REJECTED after review at Journal of Social Ontology (2026-07-13; editor Emma Tieffenbach; two referees; final, no resubmission). Public surfaces reverted to Preprint (PhilArchive REYEWW); reviews saved at `submission/jso/reviews-2026-07-13.md`; verified triage at `reviews/jso-rejection-triage-2026-07-13.md`. The section-numbering bug is root-caused and fixed (pandoc DOCX conversion in `scripts/build_jso_submission.py`, not the LaTeX; fix verified, archived package left as the record). Remaining revision before any retarget: name the forced-choice opponent and target debate on page one, define terms at first use (social cascade, anchoring, life-cycle, causal-normative network), resolve the "profile" polysemy, and settle projection-vs-read-off (Brett's call). Retarget via /venue-selection with a venue decision record.
**GitHub:** https://github.com/BrettRey/Causal-Normative_Networks
**Preprint:** https://philarchive.org/rec/REYEWW
**Working submission title:** Effective without warrant: Causal-normative networks and the social life of status
**Venue:** Journal of Social Ontology, regular article; submitted 2026-05-27

## Overview

Foundational companion to the act-kinds paper. Where the act-kinds paper uses causal-normative networks to explain the projectibility of moral act-kinds, this paper makes *causal-normative network* itself the explanandum.

Working orientation: Khalidi-forward. Khalidi supplies the network-order/projectibility frame; this paper extends that frame from ordinary causal networks to typed causal-normative networks. Boyd is not the scaffold, but his accommodation/projectibility point now supports the compact field-relative projectibility claim in Section 7.

## Current Thesis

Some social and moral explanations need causal production, recognitional representation, and field-grounded status-determination represented in one coupled structure. A causal-normative network has three relation-genera displayed by four graph roles: causal edges, recognitional edges, directed status-transition edges, and non-directed correlative ties. Its key payoff is projectibility across those graph roles plus the assessment vocabulary: social efficacy, institutional field-validity, communal successful conferral, recognitional fit, enforceability/finality, and moral warrant.

Misrecognition and wrongful conferral are diagnostic. A status-assignment can be socially effective, and sometimes field-valid or successfully conferred, without acquiring moral warrant. Discrimination is now treated as wrongful conferral at regime scale, not merely as false belief or local tracking failure.

## What Exists Now

- `main.tex`: current polished draft with all sections written, two TikZ figures, two tables, and review rounds addressed.
- `main.pdf`: current build, 22 pages.
- PhilArchive preprint: `https://philarchive.org/rec/REYEWW` (archival date 2026-05-26).
- `submission/jso/`: blind JSO package generated from `scripts/build_jso_submission.py`, including DOCX, RTF, internal-check PDF, figures, blind source, and submission checks.
- `abstract.md`: synced to the current abstract framing.
- `planning/brief.md`: original design brief, still useful for architecture and title options but partly superseded by the current draft.
- `planning/submitted-vs-current-delta.md`: operational map from the submitted JSO package to the post-submission working draft; use this when reviews arrive.
- `planning/source-map.md`: updated section-by-section source map and local-source inventory.
- `references-standalone.bib`: public-build bibliography extracted from verified central entries, with the added ALI Judgments entry verified against ALI's official publication page.
- `references-local.bib`: scratch file only for future verified additions; current public builds use `references-standalone.bib`.
- `literature/`: local source pack, including moved Downloads sources for Ásta, Weinberger, Epstein, Searle 1995, Fraser/Honneth, and copied Pullum/Scholz. This directory is ignored and not pushed to GitHub.

## Review State

The implementation pass addressed the 2026-05-26 GPT-5.5 xhigh field/validity board saved at `reviews/review-board-2026-05-26-gpt55-xhigh-field-validity.md`. A second post-implementation board is saved at `reviews/review-board-2026-05-26-gpt55-xhigh-post-implementation.md`; its main actionable items have now been implemented and polished.

The current draft incorporates:

- assessment vocabulary: efficacy / field-validity or successful conferral / moral warrant;
- regularized edge inventory: three relation-genera displayed by four graph roles: causal, recognitional, directed status-transition, and non-directed correlative;
- recognition as fit, mis-fit, or no target;
- broader status-transition sources: performances, rules, statuses, and transition events;
- §6 distinction between local misrecognition and wrongful conferral;
- Figure 2 as wrongful conferral, with harm downstream of exclusion/sanction;
- weakened overclaims about projectibility and explanatory reach;
- optional Pullum/Rogers formal analogy;
- Fraser/Honneth guardrail against over-recognition accounts of oppression;
- simplified field account: a field is an ordinary normative practice or domain, not an HPC or a front-door Epstein apparatus;
- Boyd supports field-relative projectibility/accommodation; Messick 1995 is only a limited analogy for validity as interpretation/use-relative;
- network-as-representation language: the graph represents real dependence relations without becoming a further ground or social object;
- a field-indexed projection ledger in §4 and a projectibility-forward conclusion;
- a §6 assessment table separating social efficacy, institutional field-validity, communal successful conferral, recognitional fit, enforceability/finality, and moral warrant;
- judgment as the institutional authorized-recognition case, with cautious ALI Judgments support;
- specified wrongful-conferral machinery: conferring agents, base/ascription, conferred standing, and later recognition over time;
- a direct answer to the strongest rival: grounding/anchoring plus causal mechanisms do useful work, but the network represents the cross-edge projection profile;
- Figure 2 as wrongful communal conferral, not a simple false-recognition diagram;
- polished abstract and table lead-ins, with judgment/legal language softened and source-tethered;
- final submission-prep micro-edits from the May 26 assessment: status-assignments in the abstract, distributive payoff sentence, Table 2 diagnostic-grid lead-in, and conclusion naming the coupled projection routes. The current post-submission working draft supersedes the submitted edge-inventory wording.

Declined for this paper: Lewis, Brandom, Hacking, and Haslanger. They pull toward adjacent projects; Sbisà, Ásta, Epstein, Searle, Weinberger, Kohler-Hausmann, Hu, and Fraser/Honneth are enough for the present argument.

## Open Decisions

- **Title.** Working submission title is "Effective without warrant: Causal-normative networks and the social life of status." Earlier alternatives remain in `planning/brief.md`.
- **Target venue.** Working target is Journal of Social Ontology regular article.
- **Act-kinds bridge sentence.** Applied to the live sister manuscript on 2026-05-25.

## Next Actions

1. Brett decides the projection-vs-read-off question (see `reviews/jso-rejection-triage-2026-07-13.md`, defer item 1): restrict "projection" to defeasible cross-edge inference, or defend the broad notion against Reviewer B's disanalogy charge. This decision shapes the §2 and §4 revisions.
2. Brett decides keep/cut on the uncommitted 2026-07-04 Pearl addition (`main.tex` §5 sentence + `pearl2009` in `references-standalone.bib`; builds cleanly; flagged in the triage memo because it adds another apparatus name of the sort Reviewer B objected to).
3. Revision pass on the working draft: §1 names the forced-choice opponent and the target debate with the payoff in that debate's terms; define social cascade, anchoring (move the Epstein gloss forward from §7), life-cycle, and causal-normative network at first use; reserve "profile" for projection profile only.
4. Retarget via /venue-selection with a venue decision record in `submission/` before any target-specific files. The venue and the debate §1 names must match.
5. Regenerate any future package with `python3 scripts/build_jso_submission.py` (section-numbering fix now included; the JSO-named paths/filenames need retargeting to the new venue first). Do not overwrite `submission/jso/`; it is the archived record of what JSO reviewed.
6. Revision-only literature flag: if reopening the field/practice/stabilisation apparatus, consider Weinberger (2026), `weinberger2026HomeostasisCausalControl`. Use it to prevent drift back toward "field as HPC"; fields should remain practice-relative parameter/regime structures unless a real corrective-control loop is being claimed.
7. Revision-only public-update analogy: if reopening §4, §6, or the projection ledger, consider the narrow analogy to the operator-stratum paper. Promises, judgments, and wrongful conferrals are not grammatical operators, but they are public-update structures with accountability, uptake, and repair/finality consequences. Use only as backstage architecture unless a reviewer asks for cross-domain clarification.

## Session Log

### 2026-06-13
- Integrated the June 13 edge-typing/referee-risk analysis into the canonical working draft. The paper now treats the network as three relation-genera displayed by four graph roles, not four primitive dependence types: causal production, recognitional representation, and status-determination, with status-determination split between directed transitions and non-directed correlatives.
- Repaired the intervention/probe claim: strict Woodwardian intervention is reserved for causal edges; counterfactual probes reveal the projection profile but are not a one-step classifier for every edge. Replaced the deflationary "representational" hedge with modest realism about the represented relations.
- Strengthened the regime case: episode-to-position transition now turns on recursive stabilization by empowered uptake plus new projectible consequences, and partial separability is treated as stage-relative rather than as a failed diagnostic.
- Added explicit field-parameter constraints: the framework misfires without stabilized moves/statuses/standing relations, record or uptake routes, intelligible defeaters, and projectible consequences.
- Created `planning/edge-typing-integrated-revision.md` as the Roughdraft-reviewed revision memo. Rebuilt `main.pdf`; build succeeds. Remaining LaTeX warnings are pre-existing `fancyhdr` headheight warnings and one small overfull vbox.
- Reread the key source set against the post-submission working draft: Jenkins, Ásta, Epstein, Khalidi, Woodward, Weinberger, Hu, and Kohler-Hausmann. Jenkins full text was still not locally available and the Nottingham repository copy is blocked by Cloudflare from this environment, so the Jenkins check rests on publisher abstracts, PhilPapers metadata, and the NDPR review rather than a full chapter/article reread.
- Source check supports the current working-draft fixes: Jenkins is now scoped across wrongful institutional validity and wrongful communal conferral; the division-of-labour reply is framed as projection-profile perspicuity; moral warrant is not treated as field-validity in a moral field; modularity is made field-relative in conferralist cases; the episode/position and entrenchment-threshold contrast is explicit; Hu is correctly treated as forthcoming.
- Follow-up edits after the edge-typing review added the false-recognition/wrongful-conferral exhibit to the division-of-labour reply, gave status-determination a positive mark as determination rather than production, added the Almäng route-map sentence, and added a moral-warrant guardrail against reducing warrant to efficacy or successful conferral.
- Verified the remaining source-status checks: Khalidi (2013) pp. 211--212 support the causal-network/special-science contrast; Bertrand and Mullainathan (2004) pp. 997--998 support the callback-rate figures; Hu's article remains forthcoming in \emph{The Journal of Philosophy} on Hu's official research page and in the PhilArchive draft metadata/text.
- Added `planning/submitted-vs-current-delta.md` to preserve the review-response procedure: answer reviewers against the submitted `submission/jso/` package first, then map already-fixed objections to the canonical working draft.
- Rebuilt `main.pdf`; build succeeds at 22 pages. The only log warnings are pre-existing `fancyhdr`/`microtype` template warnings. Continue to remember that the under-review JSO package predates these working-draft fixes.

### 2026-06-12
- Confirmed the paper is already under consideration at Journal of Social Ontology: submitted 2026-05-27 and still under review, with no manuscript ID recorded locally.
- Completed a post-submission working revision pass in the canonical LaTeX source: added Jenkins on ontic injustice, scoped that category across wrongful institutional validity and wrongful communal conferral, softened the §4 and conclusion division-of-labour reply to a projection-profile/perspicuity claim, added the morality-as-field answer, added the field-relative modularity caveat for conferralist cases, specified the episode/position and entrenchment-threshold contrast, added the Guala-Hindriks footnote, fixed possessive citation phrasing, switched Hu to forthcoming, and added Restatement section references.
- Rebuilt `main.pdf` with the updated source. The submitted `submission/jso/` package was not regenerated in this pass, so the under-review manuscript and current working draft now diverge.
- Created `planning/jenkins-division-labour-draft.md` as a working note for the Jenkins and division-of-labour revisions.

### 2026-05-27
- Submitted "Effective without warrant: Causal-normative networks and the social life of status" to the Journal of Social Ontology as a regular article. Status is now under review; manuscript ID not yet recorded.
- Updated the CV PDF and website publication entry to show "Under review at Journal of Social Ontology"; website commit `d5cd4c1` was pushed to `main`. GitHub raw showed the update immediately; `brettreynolds.ca` was still serving cached HTML on the first checks after push.
- Corrected the title back to sentence case across the canonical LaTeX metadata/title, `STATUS.md`, `DECISIONS.md`, `planning/brief.md`, generated JSO blind sources/checks, CV, website, `PORTFOLIO.md`, and central bibliography entry.
- Regenerated and shipped the sentence-case JSO package. Project commit `b8c4561` (`Use sentence case for submission title`) was pushed to `origin/master`.
- Website publication entry and CV were corrected to sentence case, rebuilt, deployed, and verified live. Website commit `086dc33` (`Use sentence case for effective without warrant`) was pushed to `main`.
- Resolved the open local state by keeping the Khalidi 2013 clarification and targeted Journal of Social Ontology citations, then regenerating the blind JSO DOCX/RTF/PDF package from the canonical draft.

### 2026-05-26
- PhilArchive preprint live as **REYEWW**: "Effective without warrant: Causal-normative networks and the social life of status." Archival date 2026-05-26. URL: https://philarchive.org/rec/REYEWW.
- Updated tracking surfaces to treat the paper as a live preprint with JSO upload still pending.
- Added keywords to the canonical LaTeX, PDF metadata, `abstract.md`, and regenerated blind JSO package.

## Relation to the Act-Kinds Paper

Sister project: `papers/Moral_act-kinds_as_nodes_in_causal-normative_networks/`. The act-kinds paper doesn't require this one; it needs only enough of the network idea to make its argument intelligible. This paper explains why that apparatus is legitimate.
