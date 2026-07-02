---
name: course-powerpoint-deck-build
description: Build an editable PowerPoint course deck from a slide plan using projection-safe text, native diagrams, speaker notes, and QA artifacts. Use when the user asks to create or rebuild a PPTX training deck.
version: 1.0.0
---

# Course PowerPoint Deck Build Skill

## Purpose

Turn a course slide plan into an editable PowerPoint deck that is usable in a
training room. Prioritize teaching clarity, trainer support, projection-safe
text, and editable shapes over decorative complexity.

## Use When

Use this skill when asked to:

- build a PowerPoint course deck,
- recreate slides from a slide plan,
- make a review deck,
- rebuild a course deck with better readability,
- create a trainer-ready PPTX.

## Build Principles

- Build the actual training experience, not a marketing deck.
- Keep slides editable where practical.
- Use native PowerPoint shapes, diagrams, tables, and icons for review builds.
- Use generated or searched imagery only when it genuinely improves teaching.
- Keep detail in speaker notes, not crowded slide text.
- Use consistent visual rhythm across the course.

## Visual Style Defaults

For Nexius AI transformation training decks, default to:

- dark navy instructional background,
- teal and green accents,
- white or near-white title text,
- large left-aligned headings,
- concise labels,
- card grids, matrices, workflows, ladders, dashboards, and diagrams,
- minimal decorative effects.

## Trainer Notes

Every slide must include notes. At minimum:

- teaching point,
- how to explain it,
- example or scenario,
- question to ask,
- activity instruction when relevant,
- transition cue.

## Workflow

1. Read the slide plan and any QA review.
2. Choose a consistent theme and layout system.
3. Build section by section.
4. Keep each slide to one teaching job.
5. Add speaker notes as the deck is built, not afterward.
6. Export or render slide previews if tooling allows.
7. Run text overflow and readability checks.
8. Produce a contact sheet or QA folder for review when practical.

## QA Checks

Verify:

- slide count matches the intended plan or documented revision,
- every slide has notes,
- no text overflow is detected,
- visible text is large enough for projection,
- diagrams are legible,
- activity instructions are clear,
- title and body text do not overlap,
- final file opens and has non-trivial size.

## Output

Save generated decks under `outputs/` with a stable descriptive filename. When
possible, also save:

- rendered previews,
- contact sheet,
- QA notes,
- generation script.

