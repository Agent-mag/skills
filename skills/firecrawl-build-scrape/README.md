<div align="center">

<a href="https://theagentmag.com"><img src="https://raw.githubusercontent.com/Agent-mag/.github/main/profile/agentmag-banner-github.png" alt="Agent Mag" width="100%" /></a>

# Firecrawl Build Scrape

**Integrate Firecrawl `/scrape` into product code for single-page extraction. Use when an app already has a URL and needs markdown, HTML, links, screenshots, metadata, or structured page output. Prefer this skill over broader crawl patterns when the feature is page-level.**

[![Browse Skills](https://img.shields.io/badge/Browse_Skills-theagentmag.com/skills-000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://theagentmag.com/skills)
[![Category](https://img.shields.io/badge/Category-Memory_%26_Knowledge-000?style=for-the-badge)](https://theagentmag.com/skills)
[![Agent Mag](https://img.shields.io/badge/by-Agent_Mag-000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgMjJoMjBMMTIgMnoiLz48L3N2Zz4=)](https://theagentmag.com)

[Browse Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [Website](https://theagentmag.com)

</div>

---

## What This Skill Is

**Firecrawl Build Scrape** is an installable Agent Mag skill bundle. It gives your coding agent a focused prompt, optional tool definitions, and lightweight configuration so it can perform this job consistently inside your workflow.

## What It Does

Integrate Firecrawl `/scrape` into product code for single-page extraction. Use when an app already has a URL and needs markdown, HTML, links, screenshots, metadata, or structured page output. Prefer this skill over broader crawl patterns when the feature is page-level.

## Install

```bash
npx agentmag add skill firecrawl-build-scrape
```

## What's Included

| File | Purpose |
|------|---------|
| `manifest.json` | Registry metadata, category, compatibility, and tags |
| `prompt.md` | The core instructions that shape agent behavior |
| `tools.json` | Optional tool definitions the skill expects |
| `config.json` | Optional configuration values and defaults |

## When To Use It

- the feature starts from a known URL
- you need page content for retrieval, summarization, enrichment, or monitoring
- you want the default extraction primitive before considering `/interact`
- Return `markdown` unless the feature truly needs another format.
- Use `onlyMainContent` for article-like pages where nav and chrome add noise.
- Add waits or other rendering options only when the page needs them.

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

- **Category:** Memory & Knowledge
- **License:** ISC
- **Slug:** `firecrawl-build-scrape`

---

<div align="center">

**Built for the [Agent Mag Skills Registry](https://theagentmag.com/skills)**

[Website](https://theagentmag.com) &nbsp;&middot;&nbsp; [Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [GitHub](https://github.com/Agent-mag)

</div>
