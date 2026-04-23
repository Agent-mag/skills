<div align="center">

<a href="https://theagentmag.com"><img src="https://raw.githubusercontent.com/Agent-mag/.github/main/profile/agentmag-banner-github.png" alt="Agent Mag" width="100%" /></a>

# Running Claude Code Via Litellm Copilot

**Use when routing Claude Code through a local LiteLLM proxy to GitHub Copilot, reducing direct Anthropic spend, configuring ANTHROPIC_BASE_URL or ANTHROPIC_MODEL overrides, or troubleshooting Copilot proxy setup failures such as model-not-found, no localhost traffic, or GitHub 401/403 auth errors.**

[![Browse Skills](https://img.shields.io/badge/Browse_Skills-theagentmag.com/skills-000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://theagentmag.com/skills)
[![Category](https://img.shields.io/badge/Category-Code_%26_Compute-000?style=for-the-badge)](https://theagentmag.com/skills)
[![Agent Mag](https://img.shields.io/badge/by-Agent_Mag-000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgMjJoMjBMMTIgMnoiLz48L3N2Zz4=)](https://theagentmag.com)

[Browse Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [Website](https://theagentmag.com)

</div>

---

## What This Skill Is

**Running Claude Code Via Litellm Copilot** is an installable Agent Mag skill bundle. It gives your coding agent a focused prompt, optional tool definitions, and lightweight configuration so it can perform this job consistently inside your workflow.

## What It Does

Use when routing Claude Code through a local LiteLLM proxy to GitHub Copilot, reducing direct Anthropic spend, configuring ANTHROPIC_BASE_URL or ANTHROPIC_MODEL overrides, or troubleshooting Copilot proxy setup failures such as model-not-found, no localhost traffic, or GitHub 401/403 auth errors.

## Install

```bash
npx agentmag add skill running-claude-code-via-litellm-copilot
```

## What's Included

| File | Purpose |
|------|---------|
| `manifest.json` | Registry metadata, category, compatibility, and tags |
| `prompt.md` | The core instructions that shape agent behavior |
| `tools.json` | Optional tool definitions the skill expects |
| `config.json` | Optional configuration values and defaults |

## When To Use It

- If the user wants explanation only, provide the smallest correct set of files, commands, and checks.
- If the user wants real setup work on the current machine, inspect first and adapt commands to the active shell and OS.
- Pause before persistent edits such as `~/.claude/settings.json` or shell profile files.
- Claude Code to run against GitHub Copilot through LiteLLM
- lower direct Anthropic API spending while keeping the Claude Code workflow
- a local `config.yaml` for LiteLLM's GitHub Copilot provider

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
- **Slug:** `running-claude-code-via-litellm-copilot`

---

<div align="center">

**Built for the [Agent Mag Skills Registry](https://theagentmag.com/skills)**

[Website](https://theagentmag.com) &nbsp;&middot;&nbsp; [Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [GitHub](https://github.com/Agent-mag)

</div>
