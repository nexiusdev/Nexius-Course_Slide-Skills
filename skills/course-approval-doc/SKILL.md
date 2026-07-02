---
name: course-approval-doc
description: Create a management-ready course approval document for an AI, agentic, technical, or transformation course. Use when the user asks for an approval paper, management brief, sponsor proposal, course sign-off document, business case, or executive approval doc for a course.
version: 1.0.0
---

# Course Approval Document Skill

## Purpose

Create a concise, management-ready course approval document that helps decision
makers approve, fund, govern, or sponsor a course. The document should read as
an executive decision brief, not a lesson plan and not a marketing brochure.

This skill is especially suited to AI transformation, agentic workflow,
Frontier Firm, Agent Boss, Codex, company second-brain, technical training, and
hands-on capability-building courses.

## Trigger Phrases

Use this skill when the user asks for:

- a course approval document,
- a management approval brief,
- a training proposal for approval,
- a sponsor sign-off document,
- an executive course business case,
- a course approval paper,
- a decision document for a training program.

## Required Inputs

Gather these from the workspace, wiki, existing course notes, or the user:

- Course title and audience.
- Duration and delivery format.
- Business problem or strategic reason.
- Course objectives.
- Day-by-day or module-by-module architecture.
- Major participant outputs and management deliverables.
- Tooling or platform decisions.
- Governance, risk, data, privacy, and security constraints.
- Post-course implementation path.
- Exact decision being requested.

If some inputs are missing, proceed with clearly labeled assumptions when the
risk is low. Ask the user only when the missing detail changes the approval ask,
budget, sponsor, audience, governance stance, or delivery commitment.

## Source Workflow

1. Read the project instructions, especially `AGENTS.md`.
2. Read `wiki/index.md` to locate relevant course pages.
3. Search the wiki and workspace for the course name, course outline, slide
   plan, approval notes, and governance decisions.
4. Prefer filed wiki synthesis over raw notes unless the answer depends on a
   detail not captured in the wiki.
5. Reuse durable decisions already made in the workspace, such as:
   - Codex Desktop is the main coding-agent lab tool.
   - OpenClaw and Hermes are governance-gated pilot candidates, not default
     live-system tools.
   - AI fluency, company second brain, agent-ready specs, and governed
     developer swarms are strategic course outcomes when relevant.
6. If the approval document creates reusable synthesis, file or update a wiki
   question page and append a log entry.

## Document Structure

Create the approval document in this order unless the user requests a different
format:

1. Title block
   - Document type.
   - Course title.
   - Prepared for.
   - Prepared by or owner.
   - Date.
   - Status, such as "Approval requested".

2. Approval ask
   - One clear decision requested from management.
   - One paragraph explaining what approval enables.

3. Executive summary
   - What the course is.
   - Why it matters now.
   - What participants will produce.
   - What management gets at the end.

4. Decision snapshot
   - Use a table with columns:
     `Decision Area`, `Recommendation`, `Management Benefit`.
   - Include course approval, target outcome, audience, primary tools,
     governance stance, and post-course path.

5. Strategic rationale
   - Tie the course to business capability, productivity, operating-model
     change, governance, and measurable delivery.
   - Avoid generic claims such as "AI is the future" unless backed by source
     material.

6. Program architecture
   - Summarize the days or modules in a table.
   - Columns should normally be:
     `Day/Module`, `Theme`, `Core Content`, `Output`.
   - Make clear which parts are concept foundation and which parts are hands-on
     implementation.

7. Detailed course program
   - One section per day or module.
   - Include purpose, topics, activities, participant outputs, and trainer
     support needs.
   - Keep this readable for management; move excessive lesson detail to an
     appendix.

8. Final deliverables for management
   - Use a table with:
     `Deliverable`, `Description`, `Management Value`.
   - Include training assets, templates, governance artifacts, implementation
     roadmap, metrics, ownership model, or pilot backlog when relevant.

9. Governance and risk controls
   - Use a table with:
     `Risk Area`, `Control Designed Into Course`, `Approval Confidence`.
   - Cover data exposure, inaccurate AI output, uncontrolled automation,
     coding-agent activity, tool access, lack of ownership, and adoption risk
     when relevant.

10. 30/60/90-day implementation path
    - Use a table with:
      `Phase`, `Focus`, `Expected Management Decision`.
    - The path should turn course outputs into pilots, ownership, governance
      cadence, metrics, and next investment decisions.

11. Approval requested
    - Restate the decision.
    - List the scope of approval.
    - Include conditions or constraints.
    - Add a signature or sign-off table if producing a formal document.

12. Appendix
    - Add a management scan guide, detailed program notes, slide QA checklist,
      source list, or assumptions log as needed.

## Course Quality Checks

Before finalizing, check the approval document answers these management
questions:

- What exactly are we approving?
- Who is the course for?
- What business problem does it solve?
- What will exist after the course that does not exist now?
- How does the course avoid becoming generic awareness training?
- What risks are controlled by course design?
- What decisions remain after the course?
- Who owns implementation after training?
- What should happen in the first 30, 60, and 90 days?

## Slide and Trainer Approval Checks

If the course includes a slide deck or proposed slide plan, include a short
approval-readiness section covering:

- Trainer enablement: whether slide purpose and trainer notes are sufficient.
- Readability: whether visible text is short enough for large-room delivery.
- Visual support: whether concepts use diagrams, icons, graphics, dashboards,
  matrices, or illustrations instead of dense text.
- Notes quality: whether PPT notes include script, example, participant
  question, activity instruction, timing cue, and transition.
- One-concept-per-slide discipline.
- Summary or overview slides after multi-slide concept sequences.

Use the following rating language:

- `Pass`: sufficient for approval or production.
- `Partial pass`: usable but needs build-time correction or more detail.
- `Needs work`: not yet suitable for management approval.

## Writing Style

- Write for senior management, sponsors, and training owners.
- Be clear, practical, and approval-oriented.
- Use direct headings and tables.
- Keep claims tied to course outputs, governance, and implementation.
- Prefer "Approval requested" language over vague recommendations.
- Avoid hype, generic AI marketing, and unnecessary technical depth.
- Make governance visible without making the document defensive.

## Output Formats

Default to a Markdown approval brief unless the user asks for another format.
When asked for a formal document, create a `.docx` in `outputs/` and, if useful,
also save the generation script for reproducibility.

Suggested filenames:

- `outputs/course-management-approval-[slug].docx`
- `outputs/course-management-approval-[slug].md`
- `outputs/build_course_management_approval_[slug].py`

## Verification

Before handing over the result:

- Check the file exists and has non-trivial size.
- If producing `.docx`, inspect headings or document text where practical.
- Confirm the approval ask is explicit.
- Confirm governance controls are included.
- Confirm final deliverables and implementation path are included.
- Confirm the document does not read like a generic brochure.

