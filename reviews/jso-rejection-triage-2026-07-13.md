# JSO Rejection Triage — 2026-07-13
<!-- SUMMARY: Verified triage of the two JSO referee reports + PM comment; build bug root-caused and fixed; revision punch list set · status: revision pending Brett · updated: 2026-07-13 -->

Reports: `submission/jso/reviews-2026-07-13.md`. Compared against the submitted package (`submission/jso/`), per `planning/submitted-vs-current-delta.md`, not against the diverged working draft.

## Bottom line

Substantive rejection, and the PM's diagnosis holds up under verification. All three complaints are real and locatable in the submitted package. The revision is mostly surfacing what `planning/brief.md` already says, with one genuine philosophical decision (projection vs read-off, below). Nothing in either report argues against the thesis itself; both referees engaged with the paper they could see, and what they could see hid the argument.

## Verified findings

**1. Section-numbering bug: confirmed, root-caused, fixed.**
Not `\section*`. `main.tex` numbers sections normally and the internal blind PDF had numbers (in the margin, via the house `\llap` title format). The bug is in `scripts/build_jso_submission.py`: pandoc resolves `Section~\ref{}` to literal numbers in the body text ("Section 6") but emits the DOCX/RTF headings unnumbered. JSO worked from the DOCX, so referees saw eight unnumbered headings and seven numbered cross-references. Fixed: `number_sections()` now numbers every body heading in the generated markdown; verified against the archived submitted markdown (headings 1–8; every in-text reference, Sections 4–7, resolves to the right heading). The archived `submission/jso/` package is left untouched as the record of what JSO saw.

**2. Undefined terms: confirmed, with locations.**
- *social cascade*: two uses (§4 well-formedness condition, conclusion), never defined.
- *anchoring*: used from §4 ("grounding and anchoring"), glossed only in §7 via Epstein. The gloss exists; it arrives three sections late.
- *life-cycle*: introduced in §1, never defined (though nearly self-glossing in context).
- *profile*: the worst offender. Twelve occurrences in at least four senses: the paper's own notion (projection profile), deontic bundles (permission/obligation/remedial profile), the §6 failure profiles, and bare "the profile" in §1 and the conclusion. A reader cannot tell whether "profile" names one thing.
- *causal-normative network*: the title concept never gets a canonical one-sentence definition at first use; it is assembled across §1 and §4.
- *projection/projectibility*: glossed properly in §2 (Khalidi, gold vs dirt) but used in the abstract and §1 before that gloss.

**3. The debate and the opponent never reach page one: confirmed.**
The intro does stage a problem (Pickwick; effective-without-warrant) and does define the four dependence types, so Reviewer A overstates. What is genuinely missing is dialectical placement: no named opponent, no named debate, no statement of what existing positions get wrong. The clean symptom: "the forced choice" first appears in §5 with a definite article, presupposing an introduction that never happened. The paper's named opponent (the forced-choice view, per the brief and DECISIONS) is nowhere in §1; §2–§3 run the two reductions without telling the reader that this pair is the paper's target.

**4. Khalidi motivation (Reviewer B): the deep one, partly unfair, core is real.**
Unfair as stated: §2 defines projectibility, argues the extension through the release and consent cases, and flags the extension as narrow. Real underneath: the projection ledger mixes defeasible empirical inference (breach → demand, repair, trust revision) with constitutive entailment (duty → correlative claim, a "read-off"). Khalidi's projectibility is inductive and defeasible; an entailment is not a projection in that sense, so calling both "projection" invites exactly B's charge that the term is a label. The revision must either (a) restrict "projection" to defeasible cross-edge inference and rename the read-offs, or (b) explicitly defend the broader notion against the disanalogy. This is the /check-hpc "trivial projection" failure mode applied to our own draft, as the PM noted.

## Classification

**Adopt, done this session:**
- Build fix in `scripts/build_jso_submission.py` (above). Takes effect on the next package build.
- Bib housekeeping: reverted the 2026-07-04 additions to `references-local.bib` (all three entries already exist in the central bib and in `references-standalone.bib`; the local Woodward copy also carried year 2014 where this project's 2026-05-26 audit established 2015). Clean rebuild verified: 22 pp, no undefined references.

**Adopt, revision pass (pending retarget decision):**
- Rewrite §1 to name the forced-choice view as the opponent on page one, place the paper in the social-ontology debate the target venue's readers own (conferralism/Ásta, grounding-anchoring/Epstein, rules-vs-equilibria/Guala-Hindriks are the live candidates already cited), and state the payoff in that debate's terms.
- Define at first use: causal-normative network (one sentence), social cascade, anchoring (move or duplicate the Epstein gloss forward), life-cycle.
- Resolve the *profile* polysemy. Recommendation: reserve "profile" for *projection profile* only; use "deontic position/bundle" for permission/obligation/remedial cases and "failure patterns" or keep the small-caps names for §6.
- Motivate the Khalidi transfer head-on: one paragraph in §2 conceding the disanalogy question and answering it (see the defer item).

**Adapt:**
- Reviewer A's "the problem is not identified": don't add a new problem; the problem is there. Fix the placement of debate and opponent. Salience in the brief is not salience on the page.

**Reject:**
- Nothing wholesale. Neither report contains a factual error about the text beyond the two overstatements noted, and both overstatements point at real weaknesses.

**Defer to Brett:**
1. *Projection vs read-off* (the one real philosophical choice): restrict "projection" to defeasible inference, or defend the broad notion. Restriction is cheaper and blunts B's strongest point; defense is more ambitious and closer to the paper's current text.
2. *Retarget venue.* JSO is final. Run /venue-selection with a venue decision record before building any target-specific files. Candidates should be weighed against which debate §1 will name (the venue and the named debate must match).
3. *The uncommitted 2026-07-04 Pearl work* in `main.tex` + `references-standalone.bib` (one sentence on Pearl's causal hierarchy in §5, entry `pearl2009`, verified against the central bib; builds cleanly). Left uncommitted. Note it adds another apparatus name ("Pearl's causal hierarchy") of exactly the sort Reviewer B flagged, and uses "profile" mid-§5. Keep, cut, or fold into the revision.
4. *Central-bib discrepancy*, portfolio-level: central `references.bib` dates `woodward2014MethodologyOntology` 2014 (online-first); the Synthese issue (192(11)) is 2015, as this project's audit found. Central edits don't happen from paper repos; flag for a central-bib pass.

## On the PM's AI-drafting hypothesis

Partially supported by this paper's evidence, and worth acting on. The submitted intro is not empty: the puzzle, the cases, and the four definitions are all there. What it lacks is dialectic: four small-caps definitions installed in sequence, apparatus before opponent, no stakes paragraph, every sentence locally polished. Two independent referees read the result as terminology without analysis. The upstream fix is procedural, and it is already in the venue-outcomes standing lessons: before any submission, page one must name the debate, the problem, and the payoff in the target field's terms. Treat that as a hard gate in /submission-gate, not a style preference.
