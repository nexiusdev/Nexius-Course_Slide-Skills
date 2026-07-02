# Nexius AI Skills

Reusable AI-agent skills for Nexius course design, training delivery,
management approval, and agentic transformation work.

## What Is a Skill?

A skill is a portable instruction package for a recurring task. Each skill lives
in its own folder and uses a `SKILL.md` file with frontmatter plus task-specific
workflow guidance.

Use these skills with AI coding or knowledge-work agents that can read local
files, such as Codex, Claude Code, or other agentic workspaces.

## Available Skills

| Skill | Purpose |
|---|---|
| [`course-approval-doc`](skills/course-approval-doc/SKILL.md) | Create management-ready course approval documents, sponsor decision briefs, and training approval papers. |

## Repository Structure

```text
.
├── README.md
├── skill-index.md
└── skills/
    └── course-approval-doc/
        └── SKILL.md
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

