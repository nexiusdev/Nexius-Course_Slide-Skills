# Course Slide Patterns

Use these patterns as defaults when turning course content into slides.

## Title Slide

- Big left-aligned headline.
- Short subtitle or audience note.
- One simple right-side visual/callout using circles, cards, or a bordered box.
- Footer source/course label.

## Three-Card Explanation

- Kicker and title at top.
- Three cards in a row or stacked on narrow layouts. Use sparingly; if the
  slide is teaching a system or workflow, prefer an image-led concept slide or
  workflow visual instead of a card grid.
- Each card: label, one sentence, optional "changed/impact/risk" row.
- Use different border colors only when categories differ.

## Workflow or Attack Chain

- Horizontal or vertical sequence of 4-6 steps.
- Each step: number, action verb, short description.
- Add one bottom callout bar with the instructor takeaway.
- Use arrows sparingly and keep them simple.

## Checklist Cards

- 4-6 cards or rows.
- Each item starts with an action verb.
- Use amber/red only for caution or risk.
- Include a bottom cue such as "Use this before deployment" or "Decide before
  you automate."

## Rule or Quote Slide

- Center a large statement inside a thin bordered box.
- Add a short teal label above or inside the box.
- Keep supporting text to one line.

## Image-Led Concept Slide

- Use for abstract or complex concepts that need explanation, such as operating
  models, workflow redesign, human checkpoints, governance loops, and
  before/after transformation.
- Keep the title large and left-aligned.
- Place a generated or sourced illustration as the dominant visual anchor,
  usually on the right or center-right. Make it large: roughly 60-70% of the
  slide canvas unless the slide needs a full-width diagram.
- Add 2-4 short teaching cues beside the image, not paragraphs.
- Keep all readable labels outside the image as editable PowerPoint text.
- Finish with a bottom callout bar that states the instructor takeaway.

## Diagram-Led Explanation Slide

- Use when the slide needs text and diagram structure to explain a concept, not
  only a symbolic illustration.
- Prefer a large central or full-width diagram with 3-6 labeled parts.
- Keep labels editable in PowerPoint and projection-safe, usually 24 pt or
  larger.
- Use generated imagery as the visual base only if needed; overlay clear
  PowerPoint labels, arrows, and callouts.
- Add a short left-side or bottom explanation only when it clarifies the
  business implication of the diagram. Avoid repeating what the labels already
  say.
- Good fits: model router, agent loop, human review path, governance escalation,
  context engineering flow, MCP/tool architecture, maturity ladder, or
  orchestration blueprint.

## Diagram-Plus-Text Teaching Slide

- Use when a slide needs both a framework and a short explanation.
- Make the diagram the dominant object: 60-75% of the usable canvas or
  near-full-width if the title is short.
- Use 1-3 large teaching statements, not bullets, to explain the implication.
- Keep source-inspired labels short enough to read at classroom distance.
- Use this instead of a simple illustration when the source reference contains
  meaningful structure, such as departments around a core, layered operating
  model, feedback loop, approval path, or workflow canvas.

## Raw Reference Redraw Pattern

- Inspect the raw reference image first.
- Identify the reusable teaching structure: loop, ladder, stack, router, map,
  before/after, role split, or governance path.
- Recreate that structure in the course style using editable shapes, generated
  illustration, or a hybrid composition.
- Do not paste the raw image unchanged unless the slide is explicitly about the
  source artifact.
- Preserve explanatory detail when it helps teaching. A raw framework should
  become a readable course diagram with labels, not merely a decorative icon.
- Record the raw image filename in source notes so the visual lineage is
  traceable.
- Render the slide and check for clipped labels, tiny text, and overlap with
  bottom callout bars before delivery.

## Illustration Prompt Pattern

When generating a course illustration, prompt for:

- 16:9 dark navy enterprise training-slide illustration,
- no text, no logos,
- clean vector-like or polished infographic style,
- bright teal main flow, muted blue panels, amber caution, red risk, green
  approval,
- simple composition with enough empty space for a slide title,
- specific concept objects such as AI hub, workflow pipeline, human review
  checkpoint, governance shield, evidence archive, or layered operating model.
- If the output will be used as a diagram background, ask for no text and leave
  space for editable labels. If the diagram itself needs text, ask for very few
  large labels and verify readability in the rendered slide preview.

## Closing Comparison

- Two large side-by-side cards.
- Left: current state, manual workflow, or risk.
- Right: target state, agentic workflow, or governed orchestration.
- Use parallel bullets so the contrast is easy to teach.

## Agentic Course Sequencing

For agentic transformation decks, prefer this learning progression:

1. AI workflow: human-directed task support.
2. Agent: goal, context, tools, memory, action, feedback.
3. Model-agnostic design: separate workflow logic from model choice.
4. Model routing: select model class by task complexity, cost, latency, risk,
   and context size.
5. Token optimization: reduce context waste through retrieval, summarization,
   templates, structured outputs, and handoffs.
6. Agentic orchestration: coordinate specialist agents, tools, state, approvals,
   and governance.
