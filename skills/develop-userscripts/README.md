<div align="center">

<a href="https://theagentmag.com"><img src="https://raw.githubusercontent.com/Agent-mag/.github/main/profile/agentmag-banner-github.png" alt="Agent Mag" width="100%" /></a>

# Develop Userscripts

**Use when building, debugging, packaging, or publishing browser userscripts for Tampermonkey or ScriptCat, including GM APIs, metadata blocks, permission issues, @match/@grant/@connect setup, ScriptCat background or scheduled scripts, UserConfig blocks, or subscription workflows.**

[![Browse Skills](https://img.shields.io/badge/Browse_Skills-theagentmag.com/skills-000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://theagentmag.com/skills)
[![Category](https://img.shields.io/badge/Category-Design_%26_UI-000?style=for-the-badge)](https://theagentmag.com/skills)
[![Agent Mag](https://img.shields.io/badge/by-Agent_Mag-000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgMjJoMjBMMTIgMnoiLz48L3N2Zz4=)](https://theagentmag.com)

[Browse Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [Website](https://theagentmag.com)

</div>

---

## What This Skill Is

**Develop Userscripts** is an installable Agent Mag skill bundle. It gives your coding agent a focused prompt, optional tool definitions, and lightweight configuration so it can perform this job consistently inside your workflow.

## What It Does

Use when building, debugging, packaging, or publishing browser userscripts for Tampermonkey or ScriptCat, including GM APIs, metadata blocks, permission issues, @match/@grant/@connect setup, ScriptCat background or scheduled scripts, UserConfig blocks, or subscription workflows.

## Install

```bash
npx agentmag add skill develop-userscripts
```

## What's Included

| File | Purpose |
|------|---------|
| `manifest.json` | Registry metadata, category, compatibility, and tags |
| `prompt.md` | The core instructions that shape agent behavior |
| `tools.json` | Optional tool definitions the skill expects |
| `config.json` | Optional configuration values and defaults |

## When To Use It

- writing or fixing a Tampermonkey or ScriptCat userscript
- debugging injection timing, missing permissions, CSP workarounds, update checks, or `GM_*` behavior
- deciding between a portable foreground script and ScriptCat-only `@background` or `@crontab`
- adding config UI with `==UserConfig==`
- packaging a ScriptCat `==UserSubscribe==` bundle or preparing a CloudCat-compatible script
- Confirm the manager and browser. On Manifest V3 browsers, ScriptCat may require `Allow User Scripts` or browser developer mode before script

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
- **Slug:** `develop-userscripts`

---

<div align="center">

**Built for the [Agent Mag Skills Registry](https://theagentmag.com/skills)**

[Website](https://theagentmag.com) &nbsp;&middot;&nbsp; [Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [GitHub](https://github.com/Agent-mag)

</div>
