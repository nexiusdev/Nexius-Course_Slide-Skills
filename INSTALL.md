# Install

This repository is a Codex plugin package named:

```text
nexius-course-slide-skills
```

## Option 1: Clone And Install As A Local Plugin

Clone the repository:

```bash
git clone https://github.com/nexiusdev/Nexius-Course_Slide-Skills.git
```

Then install it using your Codex plugin workflow. The plugin manifest is:

```text
Nexius-Course_Slide-Skills/.codex-plugin/plugin.json
```

After installing, start a new Codex thread so the plugin skills are loaded.

## Option 2: Copy Skills Manually

If plugin installation is not available, copy the folders under `skills/` into
your Codex skills folder:

```text
C:\Users\<your-user>\.codex\skills
```

Then start a new Codex thread.

## Included Skills

- `course-slide`
- `course-slide-planner`
- `course-slide-visual-planner`
- `course-slide-visual-candidates`
- `course-learning-experience-designer`
- `course-artifact-template-planner`
- `powerpoint-slide-illustration`

## Brand Profiles

The default deck style is `nexius-dark`.

Brand profiles live here:

```text
skills/course-slide/references/brand-profiles/
```

To create a new reusable brand profile:

1. Copy `custom-brand-template.md`.
2. Rename it, for example `client-acme-light.md`.
3. Fill in colors, fonts, layout rhythm, visual language, and sample references.
4. Start a new Codex thread and ask:

```text
Use $course-slide with the client-acme-light brand profile.
```

Users can also attach a brand guide or sample deck and ask Codex to infer a
temporary brand profile for that course.
