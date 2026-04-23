<div align="center">

<a href="https://theagentmag.com"><img src="https://raw.githubusercontent.com/Agent-mag/.github/main/profile/agentmag-banner-github.png" alt="Agent Mag" width="100%" /></a>

# Lark Openapi Explorer

**飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时使用。**

[![Browse Skills](https://img.shields.io/badge/Browse_Skills-theagentmag.com/skills-000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://theagentmag.com/skills)
[![Category](https://img.shields.io/badge/Category-Code_%26_Compute-000?style=for-the-badge)](https://theagentmag.com/skills)
[![Agent Mag](https://img.shields.io/badge/by-Agent_Mag-000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgMjJoMjBMMTIgMnoiLz48L3N2Zz4=)](https://theagentmag.com)

[Browse Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [Website](https://theagentmag.com)

</div>

---

## What This Skill Is

**Lark Openapi Explorer** is an installable Agent Mag skill bundle. It gives your coding agent a focused prompt, optional tool definitions, and lightweight configuration so it can perform this job consistently inside your workflow.

## What It Does

飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时使用。

## Install

```bash
npx agentmag add skill lark-openapi-explorer
```

## What's Included

| File | Purpose |
|------|---------|
| `manifest.json` | Registry metadata, category, compatibility, and tags |
| `prompt.md` | The core instructions that shape agent behavior |
| `tools.json` | Optional tool definitions the skill expects |
| `config.json` | Optional configuration values and defaults |

## When To Use It

- 飞书品牌使用 `open.feishu.cn`
- Lark 品牌使用 `open.larksuite.com`
- 如不确定用户品牌，默认使用飞书
- **写入/删除类 API**（POST/PUT/DELETE）调用前必须确认用户意图
- 建议先用 `--dry-run` 预览请求（如支持）
- 不要猜测 API 路径或参数——必须从文档中获取确认

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
- **Slug:** `lark-openapi-explorer`

---

<div align="center">

**Built for the [Agent Mag Skills Registry](https://theagentmag.com/skills)**

[Website](https://theagentmag.com) &nbsp;&middot;&nbsp; [Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [GitHub](https://github.com/Agent-mag)

</div>
