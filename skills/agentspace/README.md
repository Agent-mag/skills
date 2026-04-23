<div align="center">

<a href="https://theagentmag.com"><img src="https://raw.githubusercontent.com/Agent-mag/.github/main/profile/agentmag-banner-github.png" alt="Agent Mag" width="100%" /></a>

# Agentspace

**Use when the user wants to share a local folder, file, generated artifacts, logs, screenshots, or a project workspace with a human or another agent via a link. Trigger on requests like "share this folder", "upload these files", "send me the artifacts", "give me a link", or "handoff this workspace...**

[![Browse Skills](https://img.shields.io/badge/Browse_Skills-theagentmag.com/skills-000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://theagentmag.com/skills)
[![Category](https://img.shields.io/badge/Category-Code_%26_Compute-000?style=for-the-badge)](https://theagentmag.com/skills)
[![Agent Mag](https://img.shields.io/badge/by-Agent_Mag-000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgMjJoMjBMMTIgMnoiLz48L3N2Zz4=)](https://theagentmag.com)

[Browse Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [Website](https://theagentmag.com)

</div>

---

## What This Skill Is

**Agentspace** is an installable Agent Mag skill bundle. It gives your coding agent a focused prompt, optional tool definitions, and lightweight configuration so it can perform this job consistently inside your workflow.

## What It Does

Use when the user wants to share a local folder, file, generated artifacts, logs, screenshots, or a project workspace with a human or another agent via a link. Trigger on requests like "share this folder", "upload these files", "send me the artifacts", "give me a link", or "handoff this workspace...

## Install

```bash
npx agentmag add skill agentspace
```

## What's Included

| File | Purpose |
|------|---------|
| `manifest.json` | Registry metadata, category, compatibility, and tags |
| `prompt.md` | The core instructions that shape agent behavior |
| `tools.json` | Optional tool definitions the skill expects |
| `config.json` | Optional configuration values and defaults |

## When To Use It

- Only the path the user explicitly names is uploaded. Do not default to uploading the current working directory unless the user clearly says
- All network traffic goes to `agentspace.so` only. The skill does not call any other endpoint.
- The skill does not read environment variables, shell history, or files outside the path the user specifies.
- Ask the user which folder or file to share if they have not named one explicitly. Do not assume `.`.
- Run `ascli share <path> --permission edit` with the user-specified path.
- If the user asks for view-only access, use `--permission view`.

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

- **Category:** Code & Compute
- **License:** MIT
- **Slug:** `agentspace`

---

<div align="center">

**Built for the [Agent Mag Skills Registry](https://theagentmag.com/skills)**

[Website](https://theagentmag.com) &nbsp;&middot;&nbsp; [Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [GitHub](https://github.com/Agent-mag)

</div>
