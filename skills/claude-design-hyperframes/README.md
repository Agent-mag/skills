<div align="center">

<a href="https://theagentmag.com"><img src="https://raw.githubusercontent.com/Agent-mag/.github/main/profile/agentmag-banner-github.png" alt="Agent Mag" width="100%" /></a>

# Claude Design Hyperframes

**Claude Design entry point for HyperFrames. Produce renderable HyperFrames videos in Claude Design with a working in-pane preview. Use for any request to create a video, animation, launch teaser, editorial explainer, product tour, social reel, or motion deliverable.**

[![Browse Skills](https://img.shields.io/badge/Browse_Skills-theagentmag.com/skills-000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://theagentmag.com/skills)
[![Category](https://img.shields.io/badge/Category-Design_%26_UI-000?style=for-the-badge)](https://theagentmag.com/skills)
[![Agent Mag](https://img.shields.io/badge/by-Agent_Mag-000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgMjJoMjBMMTIgMnoiLz48L3N2Zz4=)](https://theagentmag.com)

[Browse Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [Website](https://theagentmag.com)

</div>

---

## What This Skill Is

**Claude Design Hyperframes** is an installable Agent Mag skill bundle. It gives your coding agent a focused prompt, optional tool definitions, and lightweight configuration so it can perform this job consistently inside your workflow.

## What It Does

Claude Design entry point for HyperFrames. Produce renderable HyperFrames videos in Claude Design with a working in-pane preview. Use for any request to create a video, animation, launch teaser, editorial explainer, product tour, social reel, or motion deliverable.

## Install

```bash
npx agentmag add skill claude-design-hyperframes
```

## What's Included

| File | Purpose |
|------|---------|
| `manifest.json` | Registry metadata, category, compatibility, and tags |
| `prompt.md` | The core instructions that shape agent behavior |
| `tools.json` | Optional tool definitions the skill expects |
| `config.json` | Optional configuration values and defaults |

## When To Use It

- Do **NOT** call `copy_starter_component` with `kind: "animations.jsx"`. The animations.jsx starter is the wrong format here — HyperFrames us
- Do **NOT** invoke the built-in "Animated video" skill. HyperFrames replaces it for this project.
- Do **NOT** use React, Babel, or `<script type="text/babel">`. Compositions are plain HTML; animation state lives on a paused GSAP timeline r
- Do **NOT** hand-roll a 1920×1080 scale-to-fit stage wrapper. `<hyperframes-player>` (loaded in `preview.html`) handles viewport scaling and
- A file attachment
- A pasted hex code or named typeface

## Compatibility

- Claude Code
- Cursor
- Windsurf
- Copilot

## Setup Notes

- No required configuration is declared for this skill.
- Install it and review `prompt.md` for any optional adjustments.

## Tooling

- No explicit tool definitions are bundled with this skill.

## Registry Metadata

- **Category:** Design & UI
- **License:** MIT
- **Slug:** `claude-design-hyperframes`

---

<div align="center">

**Built for the [Agent Mag Skills Registry](https://theagentmag.com/skills)**

[Website](https://theagentmag.com) &nbsp;&middot;&nbsp; [Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [GitHub](https://github.com/Agent-mag)

</div>
