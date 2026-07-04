---
name: powerpoint-slide-illustration
description: Create professional explanatory illustrations for PowerPoint decks. Use when Codex needs to plan, source, generate, adapt, or embed polished slide visuals such as infographic diagrams, dark-neon technology illustrations, hub-and-spoke visuals, process diagrams, role models, governance paths, concept maps, and training-slide imagery; especially when simple icons, card grids, or plain box-and-line diagrams are not enough.
---

# PowerPoint Slide Illustration

## Overview

Use this skill to turn slide content into professional teaching illustrations:
polished image-led or diagram-led visuals that help a presenter explain a
concept. Prefer this skill when the user asks for "illustrations" in slides,
when a deck looks too text/card-heavy, or when a concept needs a visual object
the trainer can point to.

For Nexius Labs/HARPS course decks, match the Day 2 Company Second Brain
template: dark navy classroom canvas, teal section language, structured
card/diagram bodies, bottom message bars, and selective dark technology
illustrations. The visual must support the trainer's explanation, not replace
the deck's editable teaching structure.

For those decks, actual illustration assets are required on concept-heavy or
system-heavy slides. Do not treat text-only cards, plain boxes, or simple lines
as the full illustration requirement. Use the official logo image from the
course template; do not recreate the logo as text.

## Core Rule

An illustration is not a small icon, a letter badge, or a plain schematic.
For this skill, an illustration means one of:

- a professional bitmap infographic or conceptual image,
- a polished PowerPoint-ready diagram with depth, lighting, and coherent
  iconography,
- an adapted licensed marketplace illustration,
- a generated visual asset that explains the slide's concept.

Keep slide titles, labels, and callouts editable. Use bitmap illustrations as
visual anchors, not as a place to hide tiny unreadable text. If a generated or
sourced illustration contains words, recreate those words as editable PowerPoint
elements and use a clean/no-text version of the image whenever possible. For
big-audience course decks, keep H1/title/header text in the 48-60 pt range and
keep instructional labels at least 18-24 pt, with 24+ pt preferred.

## Required Workflow

1. Review every slide's teaching intent before building visuals.
2. Create a visual plan with: slide number, concept, trainer explanation job,
   chosen visual type, icon/illustration need, and speaker-note purpose.
   Include a "no illustration needed" option where the clearest teaching object
   is a quote, discussion prompt, chart, table, canvas, or simple editable
   framework.
3. Choose the visual strategy:
   - **Source** a licensed/free marketplace illustration when it already fits.
   - **Adapt** a raw/reference image by redrawing its structure into the deck
     style.
   - **Generate** a new bitmap illustration when the concept is bespoke.
   - **Draw** an editable PowerPoint diagram only when it can look polished.
4. For visual-heavy course slides, compare three candidate routes before
   embedding: generated course-style illustration, editable/native PowerPoint
   diagram or adapted in-project reference, and licensed third-party/vector
   marketplace candidate.
5. Check licensing before downloading or embedding external assets.
6. Select based on relevance, explanatory power, visual quality, editability,
   and license safety. If a sourced asset explains the idea well but licensing
   is unclear, use it only as reference and redraw or regenerate an original
   version.
7. Build illustrations large enough to teach from the back of a room, usually
   55-75% of the slide canvas.
8. Embed illustrations as PNG for Canva compatibility unless editable vector
   fidelity is explicitly more important, but do not flatten slide labels,
   headings, chart labels, or explanation text into the PNG.
9. Add trainer notes explaining how to teach from the visual.
10. Render previews and inspect the contact sheet plus key slides full-size.

## Visual Types

Use `references/illustration-patterns.md` when deciding which visual type fits a
slide. Use `references/deck-review-principles.md` when a deck risks becoming
visually repetitive or when the user asks for stronger presentation-template
thinking. Common types include:

- hub-and-spoke concept system,
- circular loop or feedback cycle,
- before/after transformation,
- workflow bridge,
- layered architecture stack,
- decision gate,
- permission or governance model,
- evidence trail,
- canvas or worksheet preview,
- role/accountability split.
- bar chart or simple data comparison,
- table or decision matrix,
- quote/rule slide,
- discussion prompt with minimal visual support.

Do not use the same type repeatedly just because it is available. Visual variety
is part of instructional design: different concepts deserve different visual
forms.

## Sourcing Rules

Use external marketplaces only when the asset can be legally used.

- Slidesgo: useful for illustrated template styles and PowerPoint/Canva-ready
  inspiration. Check whether the template is free or premium.
- IconScout: useful for free/premium illustration packs in PNG/SVG/EPS/AI/JPG.
  Confirm free/premium status and licensing before download.
- Envato Elements: use as paid template reference unless the user has access and
  asks to use licensed downloads.
- SlideModel: useful for editable PowerPoint illustration/infographic patterns
  and visual metaphor examples.
- Vecteezy: useful as a third-party vector candidate source when the user asks
  to compare marketplace visuals. Treat preview art as reference until license
  status, attribution requirements, and permitted use are clear.

Do not copy preview images from marketplaces as final assets. If access or
license is unclear, use the site only as visual reference and generate or draw a
new original illustration.

## Generation

For dark technology training decks, use prompts or scripts that target:

- dark navy gradient background,
- teal glow lines and nodes,
- blue/purple/amber/red/green category accents,
- coherent pictograms,
- circular hub systems, process loops, or layered frameworks,
- no logos, no provider names, no tiny text.

Use `scripts/generate_dark_neon_illustrations.py` as a starting point for
repeatable PNG assets when a bespoke professional diagram is needed.

## PowerPoint Embedding

- Use PNG for Canva-safe imports.
- Keep labels outside the image as editable PowerPoint text. This applies to
  titles, section labels, pill labels, process names, chart labels, captions,
  and explanatory callouts. Use large-room readable sizing: 48-60 pt for main
  headers where appropriate, and generally 24+ pt for instructional labels.
- Only place text inside the image when it is decorative, not instructional, or
  when the user explicitly requests a flattened visual.
- Do not let the illustration compete with the title or bottom callout.
- In the Nexius course template, preserve the slide anatomy around the visual:
  section tag, large concept title, structured editable labels, bottom message
  bar, footer, and slide number.
- Do not use small decorative images merely to satisfy an "image per slide"
  requirement.

## QA Checklist

Before delivery:

- Each concept slide has a clear visual explanation strategy.
- Nexius/HARPS course decks use the official Nexius Labs logo image, not a text
  substitute.
- Concept-heavy decks include actual raster, sourced, generated, or adapted
  illustration assets where the template calls for them.
- Icons appear in card grids, flows, and status concepts where they improve
  scanning.
- The visual form changes with the teaching job; the deck is not a sequence of
  near-identical illustration panels.
- Slides that do not need an illustration are allowed to be clean text, chart,
  discussion, or editable framework slides.
- All teaching words are editable PowerPoint elements, not trapped in a bitmap.
- The illustration is large enough to teach, not just decorate.
- H1/title/header text is large enough for the room, normally 48-60 pt in
  course decks.
- No instructional labels, body text, chart labels, or diagram text fall below
  the 18-24 pt minimum band; prefer 24+ pt wherever possible.
- Crowding is solved by simplifying, splitting, or moving detail to notes, not
  by shrinking teaching text below the minimum.
- The visual style is consistent across slides.
- External assets have acceptable license status or are replaced with original
  generated/adapted visuals.
- For slides with three visual candidates, the selected route is documented by
  teaching relevance and explanatory power, not only by visual polish.
- The PPTX renders correctly and key slides have been visually inspected.
