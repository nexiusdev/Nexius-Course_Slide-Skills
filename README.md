# Nexius Course Slide Skills

Reusable AI-agent skills for Nexius course design, training delivery,
management approval, and agentic transformation work.

## What Is a Skill?

A skill is a portable instruction package for a recurring task. Each skill lives
in its own folder and uses a `SKILL.md` file with frontmatter plus task-specific
workflow guidance.

Use these skills with AI coding or knowledge-work agents that can read local
files, such as Codex, Claude Code, or other agentic workspaces.

## Available Skills

### Installed Personal Codex Skills

These mirror the course-related skills installed under
`C:\Users\melve\.codex\skills`.

| Skill | Purpose |
|---|---|
| [`course-slide`](skills/course-slide/SKILL.md) | Main entry point for creating or revising instructor-friendly dark navy PowerPoint course decks. |
| [`course-slide-planner`](skills/course-slide-planner/SKILL.md) | Plan slide counts and slide-by-slide inventory before deck creation. |
| [`course-slide-visual-planner`](skills/course-slide-visual-planner/SKILL.md) | Plan the visual treatment for each slide before PowerPoint creation. |
| [`course-slide-visual-candidates`](skills/course-slide-visual-candidates/SKILL.md) | Generate, compare, score, and select three visual candidates for visual-heavy slides. |
| [`course-learning-experience-designer`](skills/course-learning-experience-designer/SKILL.md) | Design learner journey, outcomes, pacing, activities, assessments, facilitation flow, and cognitive-load plan. |
| [`course-artifact-template-planner`](skills/course-artifact-template-planner/SKILL.md) | Plan handouts, worksheets, templates, rubrics, checklists, canvases, and final course artifacts. |
| [`powerpoint-slide-illustration`](skills/powerpoint-slide-illustration/SKILL.md) | Decide when and how to use diagrams, icons, screenshots, graphics, and generated visuals in course slides. |

### Project-Derived Skills

These were created from the course approval and slide-planning work in this
repository.

| Skill | Purpose |
|---|---|
| [`course-program-design`](skills/course-program-design/SKILL.md) | Design a complete course program from business goals, source material, transformation outcomes, activities, and deliverables. |
| [`course-slide-plan`](skills/course-slide-plan/SKILL.md) | Create build-ready slide-by-slide course deck plans with purpose, visible content, visual treatment, illustration needs, and note direction. |
| [`course-powerpoint-deck-build`](skills/course-powerpoint-deck-build/SKILL.md) | Build editable PowerPoint training decks from slide plans with projection-safe text, visuals, notes, and QA artifacts. |
| [`course-trainer-notes`](skills/course-trainer-notes/SKILL.md) | Expand slide-note directions into trainer-ready speaker notes with script, examples, questions, activities, timing, and transitions. |
| [`course-slide-qa-review`](skills/course-slide-qa-review/SKILL.md) | Review course slide plans or decks for trainer enablement, readability, visuals, notes, and approval readiness. |
| [`course-approval-doc`](skills/course-approval-doc/SKILL.md) | Create management-ready course approval documents, sponsor decision briefs, and training approval papers. |

## Repository Structure

```text
.
├── README.md
├── skill-index.md
└── skills/
    ├── course-approval-doc/
    │   └── SKILL.md
    ├── course-artifact-template-planner/
    │   └── SKILL.md
    ├── course-learning-experience-designer/
    │   └── SKILL.md
    ├── course-powerpoint-deck-build/
    │   └── SKILL.md
    ├── course-program-design/
    │   └── SKILL.md
    ├── course-slide/
    │   ├── SKILL.md
    │   ├── agents/
    │   ├── assets/
    │   └── references/
    ├── course-slide-plan/
    │   └── SKILL.md
    ├── course-slide-planner/
    │   └── SKILL.md
    ├── course-slide-qa-review/
    │   └── SKILL.md
    ├── course-slide-visual-candidates/
    │   └── SKILL.md
    ├── course-slide-visual-planner/
    │   └── SKILL.md
    ├── course-trainer-notes/
    │   └── SKILL.md
    └── powerpoint-slide-illustration/
        ├── SKILL.md
        ├── agents/
        ├── illustration-output/
        ├── references/
        └── scripts/
```

## How to Use

1. Copy the skill folder into your project, agent workspace, or shared skill
   library.
2. Ask your AI agent to read the relevant `SKILL.md` before doing the task.
3. Provide the source material the skill expects, such as course outlines,
   slide plans, management requirements, or governance decisions.
4. Review the output against the verification checklist in the skill.

Example prompt:

```text
Use the course-approval-doc skill to create a management approval brief for this
five-day AI transformation course.
```

## Skill Format

Each skill should include:

- frontmatter with `name`, `description`, and `version`,
- clear trigger phrases,
- required inputs,
- a step-by-step workflow,
- output format guidance,
- verification checks.

## Notes

These skills are designed to preserve useful working patterns from real course
design and AI transformation projects. They should stay practical, specific,
and easy for another agent or trainer to execute.
