# Nexius Course Slide Skills

Reusable course-related Codex skills for course design, slide planning, visual
planning, artifact planning, and PowerPoint illustration.

These folders mirror the installed personal Codex skills from:

```text
C:\Users\melve\.codex\skills
```

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

## Repository Structure

```text
.
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

