---
name: course-slide-visual-planner
description: Plan the visual treatment for each slide in an instructor-led course deck before PowerPoint creation. Use when the user asks to decide slide visuals, illustration needs, diagram types, icon/image usage, visual routes, raw-reference conversion, or per-slide visual planning for a course, workshop, training deck, lesson deck, or slide inventory. This skill does not estimate slide counts and does not create the final PPTX.
---

# Course Slide Visual Planner

## Purpose

Use this skill after a course slide inventory exists and before building the actual PowerPoint. Its job is to decide how each slide should be visually taught: native diagram, activity canvas, comparison, checklist, chart, rule slide, generated illustration, sourced/redrawn visual, or no illustration.

Do not use this skill to decide how many slides the course needs. Do not build the PPTX here. Produce a visual plan that a deck-building skill can use as an acceptance checklist.

## Required Input

Start from one of:

- a slide-by-slide inventory,
- a course outline with slide titles,
- a lesson plan,
- a workshop agenda,
- an existing deck requiring visual redesign.

If the slide count is not settled, use a slide-count planning skill first. If the user asks for a `.pptx`, finish this visual plan first, then pass it into the deck-building workflow.

## Core Output

For each slide, identify:

- slide number and title,
- teaching intent,
- trainer explanation job,
- recommended visual treatment,
- whether an illustration is needed,
- icon/diagram/image/canvas needs,
- speaker-note purpose,
- rationale for the visual choice,
- QA risks such as crowding, tiny labels, clipping, or overdecorating.

Explicitly say when a slide does not need an illustration. Do not force images onto every slide.

## Visual Decision Rules

Use the lightest visual that helps the trainer teach the point.

- Use typography/rule slides for core principles, cautions, and memorable takeaways.
- Use editable native diagrams for relationships, sequences, workflows, gates, systems, routers, loops, ladders, matrices, and governance paths.
- Use checklists or rows for action criteria, review rubrics, safety checks, and operating rules.
- Use comparison slides for current vs target state, weak vs strong examples, and risk vs control.
- Use activity/canvas slides for participant work, templates, artifact-building, and debrief prompts.
- Use charts only when comparison or evidence is the lesson.
- Use icons only as category cues, not as the main teaching object.
- Use generated or sourced illustrations only when they improve learner understanding, memory, or explanation speed.

Prefer diagram-plus-text for concepts with relationships, sequence, or governance logic. The visual should show the structure; 1-3 large text cues should explain why it matters.

## Illustration Rules

Use richer explanatory illustrations for:

- operating models and AI operating systems,
- productivity bottlenecks and fragmented workflows,
- before/after workflow redesigns,
- human-in-the-loop checkpoints,
- governance, audit, approval, and escalation paths,
- layered frameworks and maturity journeys,
- workshop canvases and capstone artifacts,
- major memory-anchor slides.

Do not treat a plain box-and-line schematic, decorative icon, or letter badge as a finished illustration when the slide needs a true explanatory visual. A strong illustration should be large enough to teach from the back of the room.

For image-led concept slides, plan the illustration as roughly 60-70% of the slide canvas unless a full-width diagram is clearer.

## Visual Route Comparison

When an illustration-heavy slide has multiple plausible routes, compare at least these options before choosing:

1. Generated dark-course visual.
2. Editable/native PowerPoint diagram or adapted in-project reference.
3. Licensed third-party/vector/marketplace candidate, only when license and attribution are safe.

Score or briefly note each route against:

- relevance to the slide concept,
- explanatory power for the trainer,
- visual quality and projection readability,
- editability of teaching labels,
- license safety.

Choose the route that best explains the slide, not the prettiest route. If a third-party asset has a useful structure but unclear license, use it only as reference and redraw or regenerate an original version.

## Course Visual Style Contract

Plan visuals for a serious dark navy instructional training style:

- dark navy background,
- bright teal for emphasis, dividers, borders, and flow lines,
- soft white primary text,
- muted blue-gray support text,
- amber for caution,
- red for risk or rejection,
- green for approval or success,
- simple editable PowerPoint geometry where possible,
- no stock-photo feel,
- no decorative imagery that does not explain the lesson,
- no glossy corporate styling.

All teaching words must remain editable PowerPoint text whenever possible. Generated images should contain no important text, no logos, and no small unreadable labels. Put titles, labels, callouts, captions, process names, chart labels, and explanation text outside the image as editable slide elements.

## Raw Reference Conversion

When raw source images, screenshots, or reference diagrams exist:

1. Inspect the raw image directly.
2. Extract the teachable structure: flow, layers, roles, checkpoints, before/after contrast, maturity level, feedback loop, model router, workflow map, or governance path.
3. Decide whether to recreate it as editable PowerPoint shapes, a generated illustration, or a hybrid.
4. Restyle it into the course visual system.
5. Keep source notes or raw filenames for provenance.
6. Plan a QA check for labels near the footer, title block, slide edges, and bottom callouts.

Do not paste raw screenshots unchanged unless the slide is explicitly about showing the original artifact.

## Projection and QA Rules

Plan every visual for large-room readability:

- main slide titles usually need 48-60 pt when built,
- major teaching statements usually need 44-56 pt,
- instructional text should not go below 18-24 pt,
- body/card/diagram labels should usually be 24-32 pt,
- callouts should usually be 26-32 pt,
- never solve crowding by shrinking text below the minimum.

If a planned visual would become crowded, split it, simplify it, or move detail into notes. Flag slides likely to suffer from tiny labels, cramped cards, repeated visual patterns, or too many diagram parts.

## Output Format

For small decks, return a Markdown table:

| Slide | Title | Teaching Intent | Trainer Job | Visual Treatment | Illustration? | Notes Purpose | QA Risk |
|---:|---|---|---|---|---|---|---|

For large course decks, write the full visual plan to a Markdown file and summarize:

- total slides planned,
- visual mix by type,
- generated illustration candidates,
- slides with no illustration,
- slides needing raw-reference conversion,
- high-risk slides for crowding or visual QA.

## Handoff to Deck Building

The visual plan should be specific enough for a deck builder to create slides without re-deciding the visual strategy. Include enough detail to describe layout type and teaching object, but do not write dense slide copy here unless needed to clarify the visual.

Before final deck delivery, the deck builder must render contact sheets and inspect text overflow, label clipping, repeated visual rhythm, and whether each visual actually helps the trainer explain the concept.
