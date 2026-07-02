---
name: course-slide
description: Create or revise instructor-friendly PowerPoint course decks using a configurable brand profile. Defaults to the bundled nexius-dark training style, but can use another brand profile, sample deck, or user-supplied palette. Use when the user asks for course slides, training decks, workshop decks, lesson decks, PowerPoint outlines, or slide-generation prompts.
---

# Course Slide

## Overview

Use this skill to create training decks that are projection-readable,
model-agnostic, and visually consistent with the bundled sample PowerPoints.
Default to the `nexius-dark` brand profile: a serious dark navy instructional
style with teal accents, concise text, editable shapes, and clear teaching
hierarchy. If the user provides or requests another brand profile, use that
profile instead of the default palette and layout style.

This skill is the main course-slide preparation entry point. For substantial
course decks, use the preparation pipeline below before building the final
PowerPoint:

1. Use `course-learning-experience-designer` when the course needs a learner
   journey, behavior-change outcomes, activity flow, mastery checks,
   facilitation plan, or cognitive-load pass before slides are planned.
2. Use `course-artifact-template-planner` when the course requires handouts,
   worksheets, templates, rubrics, checklists, canvases, or management-ready
   final artifacts beyond the slide deck.
3. Use `course-slide-planner` when the course requirements exist but the slide
   count or slide inventory is not settled.
4. Use `course-slide-visual-planner` when the slide inventory exists but each
   slide's visual treatment has not been planned.
5. Use `course-slide-visual-candidates` for visual-heavy slides that need three
   candidate visual routes, scoring, regeneration, and final visual selection.
6. Return to this `course-slide` skill to build or revise the actual `.pptx`
   using the approved slide inventory, visual plan, selected visuals, and
   trainer-note requirements.

When a deck needs professional explanatory illustrations rather than simple
icons, cards, or editable schematic diagrams, also use the
`powerpoint-slide-illustration` skill to plan, source, generate, and QA those
visual assets before embedding them in the course deck.

## Required References

Before creating or revising a deck, read:

- `references/style-guide.md` for the visual system and layout rules.
- `references/slide-patterns.md` for reusable slide archetypes.
- `references/brand-profiles/nexius-dark.md` as the default brand profile.
- Any user-selected brand profile under `references/brand-profiles/`.

Use these assets when a PowerPoint template or visual reference is useful:

- `assets/sample-decks/AI_Updates_Since_Jan_2026_Work_Impact_READABLE.pptx.pptx`
- `assets/sample-decks/Using-AI-Safely-Beginners.pptx.pptx`
- `assets/visual-reference/sample-contact-sheet.png`

## Workflow

0. Determine the preparation state:
   - If the learner journey, behavior-change outcomes, activities, assessments,
     facilitation plan, or cognitive-load flow are not settled, run
     `course-learning-experience-designer`.
   - If the course requires participant worksheets, templates, rubrics,
     checklists, canvases, or final management artifacts, run
     `course-artifact-template-planner`.
   - If course requirements exist but the slide count and inventory are not
     settled, run `course-slide-planner` to produce a slide count and
     slide-by-slide inventory.
   - If the slide inventory exists but visual treatment is not planned, run
     `course-slide-visual-planner`.
   - If a slide needs a rich explanatory visual, run
     `course-slide-visual-candidates` for three routes, scoring, regeneration,
     and final selection.
   - If the learning blueprint, artifact register, slide inventory, visual plan,
     and selected visual assets are ready, proceed with this deck-building
     workflow.
1. Inspect the user brief and identify audience, duration, learning outcomes,
   and desired deliverable: outline, slide-by-slide script, or `.pptx`.
2. Read the required references above. Determine the active brand profile:
   - If the user names a brand profile, read and apply that profile.
   - If the user provides a brand guide, sample deck, logo, palette, or style
     instruction, infer a temporary brand profile from it and state the key
     choices before building.
   - Otherwise use `nexius-dark`.
   The active profile controls colors, typography, layout rhythm, visual style,
   icon treatment, and generated-image prompts. Large-room readability remains
   mandatory unless explicitly changed.
3. If creating an actual `.pptx`, inspect the bundled sample decks first and
   reuse their proportions, spacing, footer behavior, and card/callout language
   only when `nexius-dark` or a compatible dark training profile is active. For
   other profiles, inspect the user's brand references or selected profile
   instead. Keep slides 16:9 widescreen.
4. Turn content into a teaching sequence: setup, concept, worked example,
   activity, debrief, and takeaway. Avoid marketing-deck structure unless the
   user explicitly requests it.
5. Before building the actual deck, create a slide-by-slide visual plan. For
   each slide, identify the teaching intent, the trainer explanation job, the
   most suitable visual treatment, the icon or illustration needed, and the
   speaker-note purpose. Use this as an acceptance checklist while building:
   every teaching slide should visibly help the trainer explain the concept,
   not merely decorate the slide.
   The plan must explicitly say when a slide does **not** need an illustration.
   Do not force an image onto every slide. Use illustration only when it improves
   learner understanding, memory, or explanation speed.
6. When multiple illustration routes are plausible, compare them before
   embedding: generated brand-profile visuals, editable/native diagrams, and
   third-party vector/marketplace candidates. Select one visual route per slide
   based on teaching value, style fit, editability, and license safety. Do not
   embed third-party preview art or "free vector" assets unless the license is
   clear and required attribution can be included in the deck or notes.
   For each visual-heavy slide, aim to create or identify three candidate
   visuals from distinct routes, such as:
   - generated course-style illustration,
   - editable/native PowerPoint diagram or adapted in-project reference,
   - licensed third-party/vector marketplace candidate.
   Compare the three candidates against the slide's teaching intent before
   selecting one. Score or briefly note:
   - relevance: how directly it matches the concept,
   - explanatory power: whether a trainer can teach from it quickly,
   - visual quality: hierarchy, polish, style fit, and projection readability,
   - editability: whether teaching labels remain editable PowerPoint text,
   - license safety: whether it can be embedded without unresolved attribution
     or usage issues.
   Choose the candidate that best explains the slide, not merely the prettiest
   one. If a third-party asset has the best structure but unclear license,
   redraw or regenerate an original version inspired by the structure.
7. Keep every slide concise and projection-safe. Prefer one main idea per slide,
   a large teaching statement, and 1-3 short support points over dense card
   grids or paragraphs.
8. Use model-agnostic wording unless the course is explicitly about a named
   model or tool. For AI/agentic courses, separate workflow logic, agent design,
   model routing, token optimization, governance, and orchestration.
9. For concept-heavy slides, create or source a strong explanatory illustration
   when it materially helps the instructor explain the point. In this course,
   "illustration" means a professionally designed explanatory diagram or image:
   a polished composition matching the active brand profile, glow/lighting or
   depth when useful, coherent iconography, and a clear conceptual structure. Do not treat
   a plain box-and-line schematic or letter badge as a finished illustration.
   Treat the visual as a teaching object, not a decoration: it should be large
   enough to explain the concept from the back of a room. Use generated bitmap
   illustrations when the concept needs a richer visual than editable shapes can
   provide, but keep all teaching words separate from the image whenever
   possible. Titles, labels, callouts, captions, process names, chart labels,
   and explanation text must be editable PowerPoint elements. If a sourced or
   generated illustration contains words, recreate those words as PowerPoint
   text and use a clean/no-text version of the image where possible.
10. Add trainer notes to the PowerPoint notes section for every instructional
   slide. Notes should explain how to teach from the visual, what question to
   ask, what transition to make, or what activity instruction to give. Do not
   put trainer-only guidance on the visible slide.
11. If the project includes raw reference images, inspect them for reusable
   structures such as loops, maturity ladders, operating-model stacks,
   governance paths, workflow maps, or before/after diagrams. Recreate the
   useful structure in the active brand profile instead of pasting the raw image
   unchanged. Convert the reference into a profile-matched blended diagram,
   generated illustration, or editable PowerPoint visual with clear labels. If
   the raw reference contains a useful framework, redraw it as an explanatory
   diagram with short text labels, not just a symbolic illustration.
12. Verify the result: check slide count, large-room readable font sizes,
   footer/slide numbers, consistent colors, and no text overflow, overlap, or
   clipping. Render a contact sheet and inspect whether labels sit comfortably
   inside cards, callouts, and compact boxes. If text feels pinched even when no
   overflow is detected, increase padding/box size, reduce wording, or move
   detail into notes.

## Deck Rules

- Apply the active brand profile. If no profile is supplied, use
  `nexius-dark`:
  - dark navy `#0B1A2A` as the default background,
  - bright teal `#05D6A4` for section labels, dividers, borders, and emphasis,
  - soft white `#F8FAFC` for headings and primary text,
  - muted blue-gray for body/supporting text,
  - amber for caution, red for risk, and blue/green/purple for secondary
    categories.
- When another brand profile is active, replace the default palette,
  typography, layout rhythm, and generated-image style with that profile while
  preserving instructional clarity and readability.
- Use the large-room typography contract by default for course decks: H1,
  title, and main header text should be 48-60 pt. Section titles and major
  teaching statements should usually sit in the 44-56 pt range.
- The smallest instructional text on a slide should be at least 18-24 pt.
  Prefer 24+ pt for body text, card text, chart labels, diagram labels, and
  callouts. Footer/source metadata and slide numbers may be smaller.
- Body/card/diagram labels should generally be 24-32 pt; takeaway and callout
  statements should generally be 26-32 pt.
- Never solve crowding by shrinking instructional text below the minimum.
  Shorten wording, split the slide, simplify the visual, or move detail into
  speaker notes.
- For compact cards and short label boxes, use adaptive sizing and padding:
  smaller cards need shorter copy, slightly smaller but still readable body
  text, and more internal breathing room. Text should look seated inside the
  box, not merely non-overflowing.
- Use the profile's kicker/section label style. For `nexius-dark`, use
  uppercase teal kicker labels at top-left, typically 13-16 pt.
- Use tiny muted footer text bottom-left and two-digit slide number bottom-right.
- Build simple visuals from editable PowerPoint shapes: cards, circles, rows,
  bars, simple flows, and comparison columns.
- Use icons, diagrams, charts, tables, or illustrations only when they help the
  trainer teach the point. Not every slide needs an illustration. Icons are good
  for quick category cues; editable diagrams are better for relationships,
  sequences, gates, and systems; charts are better for comparisons and evidence;
  sourced or generated illustrations are better for human/business scenarios,
  abstract operating models, and memory anchors.
- Avoid repeating the same visual type across the deck. A good teaching deck
  should deliberately vary between image-led concept slides, diagram-led slides,
  chart/data slides, comparison slides, canvas/activity slides, quote/rule
  slides, and discussion slides.
- Make explanatory illustrations large enough to do real teaching work. On
  image-led concept slides, the illustration should usually occupy 60-70% of
  the slide canvas, or become a near-full-width diagram with short editable
  labels layered around it. If the illustration is smaller than the title block,
  it is probably too small.
- Prefer diagram-plus-text slides for concepts with relationships, sequence, or
  governance logic. Use the visual to show the structure and 1-3 large text cues
  to explain why it matters.
- Do not let icon/card grids become the whole visual language. Match the active
  profile's rhythm. For `nexius-dark`, use the sample decks' rhythm: big
  left-aligned teaching headline, one clear visual anchor, short support
  points, and a bottom callout when useful.
- Keep image and words as separate elements. Bitmap/raster images may provide
  the scene, metaphor, or background, but editable PowerPoint text should carry
  the teaching labels. Do not export a full slide section as one flattened image
  if the user may need to edit the words later.
- Treat speaker notes as part of the deliverable for instructor decks. Every
  slide should include concise notes for the trainer's explanation, discussion
  prompt, activity cue, transition, or debrief guidance.
- Avoid stock photos, gradients, shadows, complex illustrations, decorative
  icons, and glossy corporate styling.

## Illustration Guidance

Use generated illustrations when the user asks for richer visuals, when the
concept is hard to explain with cards alone, or when the deck risks becoming
text-heavy. Good generated illustration targets include:

- operating models and AI operating systems,
- productivity bottlenecks and fragmented workflows,
- before/after workflow redesigns,
- human-in-the-loop checkpoints,
- governance, audit, approval, and escalation paths,
- layered frameworks and maturity journeys,
- workshop canvases and capstone artifacts.

Generated images should match the active brand profile. For `nexius-dark`, use
deep navy background, bright teal flow lines or highlights, muted blue panels,
amber for caution/escalation, red only for risk/rejection, and green for
approval or success. For other profiles, use that profile's palette,
composition, mood, and "avoid" rules. Avoid trapping important text inside generated images. Prefer diagrams
with no embedded words plus editable PowerPoint labels. If the slide needs text
inside the diagram, make the text large, sparse, and verify it visually in the
rendered preview.

When sourcing from vector marketplaces such as Vecteezy, Slidesgo, IconScout,
Envato, or SlideModel, check the exact asset license before embedding. Free
assets may require attribution, may prohibit some uses, or may differ from Pro
licenses. If attribution is required and the user has not approved it, use the
asset only as visual reference and generate or redraw an original course-style
visual instead. Keep a short source/selection note for each third-party route
considered.

## Raw Reference Conversion

When raw source images are available, use them as visual intelligence, not as
decorations:

1. Inspect the raw image directly.
2. Extract the teachable structure: flow, layers, roles, checkpoints,
   before/after contrast, maturity level, feedback loop, or governance path.
3. Decide whether to recreate it as editable PowerPoint shapes, a generated
   illustration, or a hybrid: generated background/scene plus editable labels.
4. Restyle it into the active brand profile with simple geometry,
   projection-safe labels, and a clear takeaway.
5. Keep the raw-source file names or source notes in a short provenance note.
6. Verify the rendered slide preview for clipping, especially labels near the
   footer callout, title area, or slide edges.

Use raw references especially for agent loops, AI operating-system diagrams,
model routers, human-in-the-loop governance, context engineering flows, MCP/tool
integration, workflow canvases, maturity ladders, and orchestration diagrams.

When using generated images, save or copy selected assets into the project
output/assets folder, keep a short source-notes file, and render a contact sheet
so the visual treatment can be inspected at deck level.

## Common Output Modes

- **Course outline**: provide day/session/module structure, objectives,
  activities, and outcomes.
- **Slide outline**: provide slide number, title, purpose, layout type, and
  concise bullets.
- **PowerPoint deck**: create a `.pptx` using the style guide and sample decks
  as visual references.
- **Prompt for another agent**: include the full style contract from
  `references/style-guide.md` and any content constraints from the user.
