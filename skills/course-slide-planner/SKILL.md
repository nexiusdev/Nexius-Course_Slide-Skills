---
name: course-slide-planner
description: Plan slide counts and slide-by-slide inventory from course requirements before building a training deck. Use when the user asks to estimate how many slides a course, workshop, training program, lesson, day-by-day curriculum, or PowerPoint deck requires; when preventing drift from a course brief; when expanding course content into one-concept-per-slide planning; or when deciding deck splits by day, module, activity, and artifact. This skill does not create the final PPTX.
---

# Course Slide Planner

## Purpose

Use this skill to convert course requirements into a defensible slide count and slide inventory. Keep it separate from deck creation: this skill plans quantity, sequencing, and coverage; a slide-building skill may later handle visual design and PowerPoint production.

## Core Rule

Prefer one main idea, concept, example, activity instruction, canvas, debrief, or takeaway per slide.

Do not compress several teachable concepts into one slide just because they share a section heading. For instructor-led training, a section usually expands into multiple slides:

1. Setup or why it matters.
2. Concept explanation.
3. Worked example or pattern.
4. Participant activity or canvas.
5. Review, debrief, or takeaway.

## Default Density

Use these defaults unless the user gives a different target:

- Full instructor-led training day: 40-50 slides.
- Hands-on lab day: 45-65 slides when multiple artifacts are produced.
- Half-day workshop: 20-30 slides.
- 60-90 minute executive briefing: 12-25 slides.
- Management overview deck before the course: 8-15 slides.
- Activity-heavy course: increase slide count for instructions, canvases, examples, debriefs, and artifact checklists.
- Pure lecture or awareness talk: may be lower, but still keep one concept per slide.

When a course has 5 full training days, expect roughly 200-250 slides before a management overview. If labs produce many templates/artifacts, 250-300 slides can be appropriate.

## Planning Workflow

1. Read the course source: brief, document, outline, outcomes, agenda, learning objectives, or user notes.
2. Identify the course form:
   - executive briefing,
   - short workshop,
   - full-day training,
   - multi-day course,
   - hands-on lab,
   - artifact-producing implementation program.
3. Extract the real teaching units:
   - concepts,
   - frameworks,
   - examples,
   - tools,
   - workflows,
   - risks,
   - decisions,
   - activities,
   - canvases/templates,
   - debriefs,
   - final deliverables.
4. Convert each unit into slide atoms. A slide atom is one explainable thing that deserves its own slide.
5. Estimate slide count by module/day before writing slide titles.
6. Expand into a slide inventory only after the count feels proportionate to duration and learning outcomes.
7. Add explicit rationale when deviating from the default density.

## Slide Atom Patterns

Use these common expansions:

- New topic: divider/opening slide + learning outcomes.
- Concept: definition slide + why it matters + example.
- Framework: overview slide + one slide per major component + application slide.
- Workflow: overview slide + one slide per step + review slide.
- Tool comparison: landscape slide + one slide per tool/category + routing/decision slide.
- Governance topic: risk slide + control slide + decision/escalation slide.
- Activity: setup slide + instructions slide + editable canvas/template slide + debrief slide.
- Artifact: purpose slide + field-by-field explanation + worked example + activity canvas + quality checklist.
- Day close: artifact checklist + debrief + takeaway + bridge to next day.

## Artifact-Producing Course Rule

For courses where participants must produce reusable artifacts, allocate slides for each artifact:

- artifact purpose,
- required fields/components,
- good example,
- common mistakes or quality bar,
- activity instructions,
- blank/editable canvas,
- peer review or debrief.

This often means 5-7 slides per major artifact. Do not hide multiple artifacts in one summary slide if participants need to build them.

## Output Format

When planning, provide:

1. Assumptions: course duration, audience, delivery mode, and slide-density target.
2. Count summary: total slides and slides per day/module.
3. Rationale: why the count is appropriate.
4. Slide inventory: slide number, slide title, teaching job, and optional visual type.
5. Coverage check: map course requirements to slide ranges.
6. Drift warnings: note any missing course requirements, overloaded modules, or places where the brief implies more slides than the current plan.

For large courses, save the full plan to a Markdown file and summarize it in chat.

## Coordination With Deck-Building Skills

Use this skill before any PowerPoint creation when slide volume or coverage matters. After this plan is approved, a deck-building skill can create the actual PowerPoint, speaker notes, visual treatments, and rendered QA.

Do not let design concerns reduce the slide count below the teaching requirement. If a slide is too dense, split it.
