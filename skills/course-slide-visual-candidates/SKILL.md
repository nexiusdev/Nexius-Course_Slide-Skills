---
name: course-slide-visual-candidates
description: Generate, compare, score, and select three visual candidates for course slides based on a visual plan. Use after course-slide-visual-planner when the user wants three visual routes per slide, generated visual assets, native/editable diagram candidates, sourced or reference-derived candidates, scoring by relevance and explanatory power, and a final selected visual for a course, workshop, lesson, training deck, or PowerPoint build. This skill does not estimate slide counts and does not build the full PPTX.
---

# Course Slide Visual Candidates

## Purpose

Use this skill after a slide inventory and visual plan exist. Its job is to create or identify three visual candidates for each selected slide, score them, and choose the candidate that best helps the trainer explain the slide concept.

Do not use this skill to decide slide count. Do not build the full course deck here. Produce visual candidates, selection notes, and final visual recommendations that can be handed to a deck-building workflow.

## Required Inputs

Start from:

- slide number and title,
- slide teaching intent,
- trainer explanation job,
- visual treatment from `course-slide-visual-planner`,
- course visual style requirements,
- any raw reference images or source materials,
- desired output folder when actual visual assets should be generated.

If the visual treatment has not been planned yet, use `course-slide-visual-planner` first.

## Three Candidate Sources

For every visual-heavy slide, produce or identify exactly three routes unless the user explicitly narrows the task:

1. Generated course-style illustration.
   - Use AI image generation for a polished dark navy / teal explanatory visual.
   - Prompt for no text, no logos, 16:9 composition, and enough empty space for editable PowerPoint labels.
   - Use when the slide needs a memory anchor, abstract operating model, human-in-loop scene, governance path, or concept illustration.

2. Editable/native PowerPoint diagram.
   - Design an editable visual route using shapes, cards, lines, arrows, matrices, loops, ladders, timelines, or canvases.
   - This may be represented as a rendered mockup, SVG/PNG preview, or detailed build spec, but the final deck should keep labels editable.
   - Use when the concept depends on relationships, sequence, gates, controls, workflows, or participant activity templates.

3. Sourced, licensed, or reference-derived visual.
   - Search for or inspect a third-party/vector/marketplace/reference structure only when it can add explanatory value.
   - Check license and attribution before recommending embedding.
   - If license is unclear or attribution is not approved, use the candidate only as structural reference and recommend redrawing or regenerating an original version.
   - Raw project images can count as this route when they provide a useful teachable structure.

If a slide does not deserve a rich visual, state that this skill should not generate three candidates for it; recommend a simple rule, checklist, or native slide instead.

## Generation Rules

For generated bitmap candidates:

- create visuals in the dark navy / teal course style,
- avoid embedded words,
- avoid logos,
- avoid stock-photo composition,
- use teal for main flows, muted blue panels, amber caution, red risk, and green approval,
- leave space for slide title and editable labels,
- save candidate files in a clear folder such as `visual-candidates/slide-###/`.

For native diagram candidates:

- keep the structure editable in PowerPoint,
- use large-room readable labels,
- avoid tiny boxes, dense grids, and too many parts,
- prefer 3-6 major parts unless the slide is explicitly a canvas or matrix,
- include a concise build spec if no preview file is created.

For sourced/reference candidates:

- record the source URL or raw filename,
- summarize the useful structure,
- record license status,
- do not embed unsafe preview art,
- recommend redraw/regenerate when license is unclear.

## Scoring Rubric

Score each candidate from 1-10 on:

- Relevance: how directly the visual matches the slide concept.
- Explanatory power: how much it helps the trainer explain the concept quickly.
- Visual quality: hierarchy, polish, projection readability, and style fit.
- Editability: whether teaching labels and slide-specific wording remain editable.
- License safety: whether it can be used without unresolved attribution or rights issues.

Weight the final decision:

- Relevance: 30%.
- Explanatory power: 35%.
- Visual quality: 15%.
- Editability: 10%.
- License safety: 10%.

The best visual is not automatically the prettiest visual. Select the candidate that most improves learner understanding and trainer explanation.

## Regeneration Loop

Use a loop engineering process for visual quality. Do not accept a final selected visual unless its weighted score is at least 9/10.

For each slide:

1. Generate or identify the three candidate routes.
2. Score all candidates with the weighted rubric.
3. Select the highest-scoring candidate.
4. If the selected candidate scores 9/10 or higher, mark it as accepted.
5. If the selected candidate scores below 9/10, diagnose the weakness:
   - weak relevance,
   - low explanatory power,
   - cluttered or low-quality visual hierarchy,
   - poor editability,
   - unsafe or unclear license.
6. Regenerate or redesign only the weak route(s), preserving what worked.
7. Rescore the replacement candidates.
8. Continue until one candidate reaches at least 9/10 or until three regeneration rounds fail.

After three failed regeneration rounds, do not silently accept the best weak candidate. Report the best score reached, explain the blocker, and recommend one of:

- change the visual route,
- simplify the slide concept,
- split the slide,
- use a native editable diagram instead of a generated/sourced visual,
- ask the user for a better reference or constraint.

Record regeneration attempts in the selection report so the final visual choice is auditable.

## Selection Rules

Choose the winner only after comparing all three candidates.

Prefer native/editable diagrams when:

- the slide teaches a sequence, matrix, workflow, gate, router, loop, or architecture,
- editable labels are essential,
- visual precision matters more than atmosphere.

Prefer generated illustrations when:

- the slide is a memory-anchor concept,
- the idea is abstract or human/business-scenario based,
- a richer image will help learners remember the concept,
- labels can remain editable outside the image.

Prefer sourced/reference-derived visuals only when:

- the structure is clearly superior,
- license and attribution are safe,
- or the source is used only as reference for an original redraw.

Reject or revise candidates that contain unreadable text, visual clutter, weak relation to the concept, unsafe licensing, or decorative imagery that does not teach.

## Output Format

For each processed slide, provide:

| Slide | Candidate | Source Route | Asset/Reference | Relevance | Explanatory Power | Visual Quality | Editability | License Safety | Weighted Score | Notes |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|

Then include:

- selected candidate,
- why it won,
- whether it met the 9/10 acceptance threshold,
- regeneration attempts and what changed,
- how to use it on the slide,
- editable labels needed in PowerPoint,
- any redraw or regeneration instructions,
- QA risks before final deck delivery.

For large batches, write a Markdown selection report and keep generated/source assets in per-slide folders.

## QA Before Handoff

Before handing visual choices to a deck builder:

- check every generated candidate for embedded text or logo artifacts,
- inspect generated images visually when possible,
- confirm native diagrams can fit large labels,
- confirm sourced candidates have safe license notes or are marked reference-only,
- ensure the chosen visual supports the slide’s teaching intent,
- ensure the visual does not crowd the title, footer, callout, or slide labels.

## Handoff

The deck builder should receive:

- selected visual route,
- selected asset path or native diagram build spec,
- editable label list,
- placement guidance,
- selection rationale,
- QA warnings.

Keep candidate files and source notes so the selection remains auditable.
