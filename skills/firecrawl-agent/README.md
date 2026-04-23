<div align="center">

<a href="https://theagentmag.com"><img src="https://raw.githubusercontent.com/Agent-mag/.github/main/profile/agentmag-banner-github.png" alt="Agent Mag" width="100%" /></a>

# Firecrawl Agent

**AI-powered autonomous data extraction that navigates complex sites and returns structured JSON. Use this skill when the user wants structured data from websites, needs to extract pricing tiers, product listings, directory entries, or any data as JSON with a schema. Triggers on "extract structured...**

[![Browse Skills](https://img.shields.io/badge/Browse_Skills-theagentmag.com/skills-000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://theagentmag.com/skills)
[![Category](https://img.shields.io/badge/Category-Browsing_%26_Search-000?style=for-the-badge)](https://theagentmag.com/skills)
[![Agent Mag](https://img.shields.io/badge/by-Agent_Mag-000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgMjJoMjBMMTIgMnoiLz48L3N2Zz4=)](https://theagentmag.com)

[Browse Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [Website](https://theagentmag.com)

</div>

---

## What This Skill Is

**Firecrawl Agent** is an installable Agent Mag skill bundle. It gives your coding agent a focused prompt, optional tool definitions, and lightweight configuration so it can perform this job consistently inside your workflow.

## What It Does

AI-powered autonomous data extraction that navigates complex sites and returns structured JSON. Use this skill when the user wants structured data from websites, needs to extract pricing tiers, product listings, directory entries, or any data as JSON with a schema. Triggers on "extract structured...

## Install

```bash
npx agentmag add skill firecrawl-agent
```

## What's Included

| File | Purpose |
|------|---------|
| `manifest.json` | Registry metadata, category, compatibility, and tags |
| `prompt.md` | The core instructions that shape agent behavior |
| `tools.json` | Optional tool definitions the skill expects |
| `config.json` | Optional configuration values and defaults |

## When To Use It

- You need structured data from complex multi-page sites
- Manual scraping would require navigating many pages
- You want the AI to figure out where the data lives
- Always use `--wait` to get results inline. Without it, returns a job ID.
- Use `--schema` for predictable, structured output — otherwise the agent returns freeform data.
- Agent runs consume more credits than simple scrapes. Use `--max-credits` to cap spending.

## Compatibility

- Claude Code
- Cursor
- Windsurf
- Copilot

## Setup Notes

- No required configuration is declared for this skill.
- Install it and review `prompt.md` for any optional adjustments.

## Tooling

- **Bash(firecrawl *)** — Tool: Bash(firecrawl *)
- **Bash(npx firecrawl *)** — Tool: Bash(npx firecrawl *)

## Registry Metadata

- **Category:** Browsing & Search
- **License:** MIT
- **Slug:** `firecrawl-agent`

---

<div align="center">

**Built for the [Agent Mag Skills Registry](https://theagentmag.com/skills)**

[Website](https://theagentmag.com) &nbsp;&middot;&nbsp; [Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [GitHub](https://github.com/Agent-mag)

</div>
