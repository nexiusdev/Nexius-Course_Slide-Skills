# Course Slide Style Guide

Use this visual system for dark navy instructional training decks.

## Brand Profiles

This skill supports brand profiles. Unless the user supplies another profile,
use `references/brand-profiles/nexius-dark.md` as the default.

When the user asks for a different brand, client style, color palette, sample
deck, or visual identity:

1. Read the requested brand profile if it exists under `references/brand-profiles/`.
2. If no profile exists, infer a temporary profile from the user's brand guide,
   sample deck, colors, fonts, or attached references.
3. Apply that profile consistently across palette, typography, layout rhythm,
   visual style, iconography, and generated-image prompts.
4. Keep large-room readability rules from this style guide unless the user
   explicitly changes them.
5. Do not force `nexius-dark` colors when another brand profile is selected.

To add a reusable brand, copy
`references/brand-profiles/custom-brand-template.md`, rename it to the new
profile id, and fill in the sections.

## Core Style

- Canvas: 16:9 widescreen PowerPoint.
- Background: solid deep navy, close to `#0B1A2A`.
- Accent: bright teal, close to `#05D6A4`, for section labels, borders, divider
  lines, vertical bars, and emphasis.
- Primary text: soft white, close to `#F8FAFC`.
- Body/supporting text: muted blue-gray.
- Secondary colors: amber for caution, red for risk, blue/green/purple for
  secondary categories.
- Typography: large bold sans-serif headings similar to Aptos Display; body in
  clean sans-serif similar to Aptos.
- Mood: serious, modern, instructor-friendly, cybersecurity/workflow governance
  training style.

## Slide Anatomy

- Top-left kicker: small uppercase teal, 13-16 pt, bold.
- Title: large, bold, white, left-aligned. For big-audience course decks,
  default to 48-60 pt for H1/title/header text.
- Subtitle/body: concise and projection-readable. The smallest instructional
  text should be at least 18-24 pt, with 24+ pt preferred for body text, cards,
  diagrams, chart labels, and callouts. Footer/source metadata may be smaller.
- Takeaway and callout statements should generally be 26-32 pt. If text does
  not fit at these sizes, reduce wording or split the slide instead of shrinking
  the text.
- Footer: tiny muted course/source label bottom-left.
- Slide number: bottom-right, two digits.
- Breathing room: leave generous margins and avoid edge-to-edge text.

## Components

- Cards: slightly lighter navy than the background, with thin teal, blue, amber,
  red, green, or purple borders. Use vertical accent bars for status or category.
- Callout bars: full-width rounded rectangle near the bottom, teal outline, left
  label in uppercase teal, cue text in white.
- Flow steps: circles or compact cards connected by simple lines/arrows.
- Comparisons: two large side-by-side cards with clear labels and parallel
  structure.
- Checklists: compact cards or rows with short action labels and risk/impact
  notes.
- Quote/rule slides: centered text inside a bordered box, minimal supporting
  copy.
- Image-led concept slides: large left-aligned headline, one generated or
  sourced explanatory illustration occupying 60-70% of the slide, 2-4 short
  teaching cues, and a bottom callout. Use these for abstract systems,
  workflows, before/after comparisons, governance paths, and course canvases.
- Diagram-led slides: use a large near-full-width diagram when the relationship
  between parts is the lesson. Keep labels sparse and editable. Use this for
  loops, ladders, model routers, workflow maps, approval paths, and
  orchestration diagrams.
- Diagram-plus-text slides: use when a visual alone is too symbolic. Pair a
  large diagram with 1-3 bold teaching statements that explain the business
  meaning. The diagram should carry the structure; the text should explain the
  implication.

## Avoid

- Stock imagery unless necessary.
- Random decorative imagery, glossy corporate visuals, dense icon sets, and
  illustrations that do not explain the slide's teaching point.
- Paragraph-heavy slides.
- Tiny text, crowded grids, and low-contrast body copy.
- Vendor-locked phrasing when the course should be model-agnostic.

## Sample Deck Observations

The bundled sample decks use:

- Dark navy full-slide backgrounds.
- Teal section/kicker labels and occasional vertical teal bars.
- Large white left-aligned headings.
- Simple shape visuals: circles, cards, rows, and bordered message bars.
- Bottom-left course/source footer and bottom-right slide number.
- Minimal photos; most meaning comes from typography and simple editable shapes.

## Generated Illustration Style

When generated illustrations are useful, keep them consistent with the sample
deck rather than photorealistic:

- deep navy background with teal/blue enterprise linework,
- minimal amber/red/green accents for caution, risk, and approval,
- clean vector-like or polished infographic style,
- no logos, no readable text, and no stock-photo composition,
- enough empty space for large headings and editable labels.

Embed generated images as concept illustrations, then keep titles, labels,
captions, and callout text editable in PowerPoint.

## Raw Reference Conversion

When a project has raw reference screenshots or diagrams, inspect them and
convert the useful structure into the deck style. Do not paste low-resolution
screenshots as-is unless the slide is explicitly about showing the original
artifact.

Good conversions:

- raw loop diagram -> large dark navy loop with editable step labels,
- raw maturity ladder -> staged teal/blue ladder with short level names,
- raw workflow screenshot -> cleaned pipeline with generated visual support,
- raw governance graphic -> approval/escalation/evidence path,
- raw operating-system image -> central hub with department or capability nodes.

Use the raw image for composition and meaning, then redraw, generate, or hybrid
compose it so it blends with the course palette and remains readable in a room.
When the source image contains a useful framework, preserve the explanatory
structure with large editable labels instead of reducing it to a simple icon or
metaphor.

After rendering, inspect the slide image. Check that diagram labels do not clip,
hide behind the bottom callout, collide with the title block, or become smaller
than the surrounding support text. Confirm the large-room typography contract is
met: primary headers at 48-60 pt where appropriate, and no instructional text
below the 18-24 pt minimum band.
