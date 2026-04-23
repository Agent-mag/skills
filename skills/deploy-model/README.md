<div align="center">

<a href="https://theagentmag.com"><img src="https://raw.githubusercontent.com/Agent-mag/.github/main/profile/agentmag-banner-github.png" alt="Agent Mag" width="100%" /></a>

# Deploy Model

**Unified Azure OpenAI model deployment skill with intelligent intent-based routing. Handles quick preset deployments, fully customized deployments (version/SKU/capacity/RAI policy), and capacity discovery across regions and projects. USE FOR: deploy model, deploy gpt, create deployment, model depl...**

[![Browse Skills](https://img.shields.io/badge/Browse_Skills-theagentmag.com/skills-000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://theagentmag.com/skills)
[![Category](https://img.shields.io/badge/Category-Code_%26_Compute-000?style=for-the-badge)](https://theagentmag.com/skills)
[![Agent Mag](https://img.shields.io/badge/by-Agent_Mag-000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgMjJoMjBMMTIgMnoiLz48L3N2Zz4=)](https://theagentmag.com)

[Browse Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [Website](https://theagentmag.com)

</div>

---

## What This Skill Is

**Deploy Model** is an installable Agent Mag skill bundle. It gives your coding agent a focused prompt, optional tool definitions, and lightweight configuration so it can perform this job consistently inside your workflow.

## What It Does

Unified Azure OpenAI model deployment skill with intelligent intent-based routing. Handles quick preset deployments, fully customized deployments (version/SKU/capacity/RAI policy), and capacity discovery across regions and projects. USE FOR: deploy model, deploy gpt, create deployment, model depl...

## Install

```bash
npx agentmag add skill deploy-model
```

## What's Included

| File | Purpose |
|------|---------|
| `manifest.json` | Registry metadata, category, compatibility, and tags |
| `prompt.md` | The core instructions that shape agent behavior |
| `tools.json` | Optional tool definitions the skill expects |
| `config.json` | Optional configuration values and defaults |

## When To Use It

- Azure CLI installed and authenticated (`az login`)
- Active Azure subscription with deployment permissions
- Azure AI Foundry project resource ID (or agent will help discover it via `PROJECT_RESOURCE_ID` env var)
- **[preset/SKILL.md](preset/SKILL.md)** — Quick deployment to optimal region with sensible defaults
- **[customize/SKILL.md](customize/SKILL.md)** — Interactive guided flow with full configuration control
- **[capacity/SKILL.md](capacity/SKILL.md)** — Discover available capacity across regions and projects

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
- **Slug:** `deploy-model`

---

<div align="center">

**Built for the [Agent Mag Skills Registry](https://theagentmag.com/skills)**

[Website](https://theagentmag.com) &nbsp;&middot;&nbsp; [Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [GitHub](https://github.com/Agent-mag)

</div>
