# Nexius Course Slide Skills

Reusable course-related Codex plugin for course design, slide planning, visual
planning, artifact planning, and PowerPoint illustration. The current default
course deck style follows the Nexius Labs Day 2 Company Second Brain template:
dark navy canvas, official Nexius Labs logo, teal section language, icons,
explanatory illustrations, workbook/activity slides, bottom message bars, and
trainer notes.

These folders mirror the installed personal Codex skills from:

```text
C:\Users\melve\.codex\skills
```

## Plugin Package

This repository is packaged as a Codex plugin:

```text
.codex-plugin/plugin.json
```

Plugin name:

```text
nexius-course-slide-skills
```

See [INSTALL.md](INSTALL.md) for install notes.

## Available Skills

| Skill | Purpose |
|---|---|
| [`course-slide`](skills/course-slide/SKILL.md) | Main entry point for creating or revising instructor-friendly dark navy PowerPoint course decks. |
| [`course-slide-planner`](skills/course-slide-planner/SKILL.md) | Plan slide counts and slide-by-slide inventory before deck creation. |
| [`course-slide-visual-planner`](skills/course-slide-visual-planner/SKILL.md) | Plan the visual treatment for each slide before PowerPoint creation. |
| [`course-slide-visual-candidates`](skills/course-slide-visual-candidates/SKILL.md) | Generate, compare, score, and select three visual candidates for visual-heavy slides. |
| [`course-learning-experience-designer`](skills/course-learning-experience-designer/SKILL.md) | Design learner journey, outcomes, pacing, activities, assessments, facilitation flow, and cognitive-load plan. |
| [`course-artifact-template-planner`](skills/course-artifact-template-planner/SKILL.md) | Plan handouts, worksheets, templates, rubrics, checklists, canvases, and final course artifacts. |
| [`powerpoint-slide-illustration`](skills/powerpoint-slide-illustration/SKILL.md) | Plan, source, generate, and QA professional explanatory illustrations for PowerPoint training decks. |

## Canonical Course Template

The plugin defaults to the Day 2 Company Second Brain course template.

Canonical template assets:

```text
skills/course-slide/assets/sample-decks/Day_2_Company_Second_Brain_Template.pptx
skills/course-slide/assets/visual-reference/day2-company-second-brain-contact-sheet.png
skills/course-slide/references/nexius-course-template.md
```

Key acceptance checks:

- Use the official Nexius Labs logo image at top-right on normal content slides.
- Use icons in cards, flows, matrices, and status concepts where they improve
  scanning.
- Use real explanatory illustrations on concept-heavy or system-heavy slides.
- Add trainer notes to every instructional slide.
- Render and inspect the contact sheet before delivery.

Example prompt:

```text
Use $course-slide to build this as a Nexius course deck.
```

Or:

```text
Use $course-slide with this attached final course template. Follow its logo,
icons, illustration style, footer, message bars, and trainer-note requirements.
```

## Repository Structure

```text
.
├── .codex-plugin/
│   └── plugin.json
├── README.md
├── skill-index.md
└── skills/
    ├── course-artifact-template-planner/
    │   ├── SKILL.md
    │   └── agents/
    ├── course-learning-experience-designer/
    │   ├── SKILL.md
    │   └── agents/
    ├── course-slide/
    │   ├── SKILL.md
    │   ├── agents/
    │   ├── assets/
    │   └── references/
    │       └── brand-profiles/
    ├── course-slide-planner/
    │   ├── SKILL.md
    │   └── agents/
    ├── course-slide-visual-candidates/
    │   ├── SKILL.md
    │   └── agents/
    ├── course-slide-visual-planner/
    │   ├── SKILL.md
    │   └── agents/
    └── powerpoint-slide-illustration/
        ├── SKILL.md
        ├── agents/
        ├── illustration-output/
        ├── references/
        └── scripts/
```

## How to Use

### As a Codex Plugin

Clone or download this repository, then install it through your Codex plugin
workflow. The plugin manifest is at:

```text
.codex-plugin/plugin.json
```

After installation, start a new Codex thread so the plugin skills are loaded.

### As Individual Skills

1. Copy the needed skill folder into a Codex skills directory or another agent
   workspace that supports `SKILL.md`-style instructions.
2. Ask the agent to use the relevant skill by name, such as
   `$course-slide-planner` or `$course-slide`.
3. Provide the course brief, outline, slide inventory, source material, or
   visual requirements the skill expects.
4. Review outputs against the skill's own quality bar and verification notes.

## Notes

The `course-slide` and `powerpoint-slide-illustration` skills include reference
files and sample assets used by the skill instructions. Keep those folders
together when copying the skills elsewhere.

To add a reusable client style, copy `custom-brand-template.md`, rename it to a
stable profile id, fill in the palette/layout/visual rules, and ask Codex to use
that profile by name.
