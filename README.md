<div align="center">

<a href="https://theagentmag.com"><img src="https://raw.githubusercontent.com/Agent-mag/.github/main/profile/agentmag-banner-github.png" alt="Agent Mag" width="100%" /></a>

# Agent Skills Registry

**Open registry of installable AI agent skills. Submit yours via PR.**

[![Browse Skills](https://img.shields.io/badge/Browse_Skills-theagentmag.com/skills-000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://theagentmag.com/skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-000?style=for-the-badge)](LICENSE)
[![Agent Mag](https://img.shields.io/badge/by-Agent_Mag-000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgMjJoMjBMMTIgMnoiLz48L3N2Zz4=)](https://theagentmag.com)

[Browse Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [Website](https://theagentmag.com)

</div>

---

## What Is a Skill?

A skill is a **config bundle** — not executable code. It's a folder containing prompts, tool definitions, and metadata that tells an AI agent how to perform a specific task.

```
skills/
  web-scraper/
    manifest.json    # Name, description, category, version, author
    prompt.md        # System prompt / instructions for the agent
    tools.json       # Tool schemas (function definitions)
    config.json      # Optional settings and defaults
```

Because skills are config — not code — you can **audit everything** before it touches your system.

---

## Install a Skill

```bash
npx agentmag add <skill-name>
```

This drops the skill's config bundle into your project. You own it from there — customize the prompt, tweak the tool schemas, make it yours.

---

## Browse Skills

Visit **[theagentmag.com/skills](https://theagentmag.com/skills)** for the full registry with search, categories, and install counts.

### Categories

| Category | Examples |
|----------|---------|
| 🔍 **Browsing & Search** | Web search, site crawling, content extraction |
| 💻 **Code & Compute** | Code execution, sandboxed environments, REPL access |
| 📁 **Data & Files** | File parsing, data transformation, document processing |
| 💬 **Communication** | Email, messaging, notification integrations |
| 🧠 **Memory & Knowledge** | RAG, vector stores, knowledge graph connectors |
| 🎨 **Multimodal** | Vision, audio, image generation, OCR |

---

## Submit a Skill

We welcome community-contributed skills. Here's how:

### 1. Fork this repo

### 2. Create your skill folder

```
skills/
  your-skill-name/
    manifest.json
    prompt.md
    tools.json
    config.json      # optional
```

### 3. Follow the manifest schema

```json
{
  "name": "your-skill-name",
  "version": "1.0.0",
  "description": "One-line description of what this skill does",
  "category": "Browsing & Search",
  "author": {
    "name": "Your Name",
    "github": "your-github-username"
  },
  "tags": ["web", "scraping", "extraction"],
  "license": "MIT"
}
```

**Valid categories:** `Browsing & Search`, `Code & Compute`, `Data & Files`, `Communication`, `Memory & Knowledge`, `Multimodal`

### 4. Write a clear prompt

Your `prompt.md` should be a self-contained system prompt that tells an agent exactly how to use this skill. Be specific, include edge cases, and describe expected behavior.

### 5. Define tool schemas

`tools.json` follows the standard function-calling schema:

```json
[
  {
    "name": "tool_name",
    "description": "What this tool does",
    "inputSchema": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string",
          "description": "The URL to scrape"
        }
      },
      "required": ["url"]
    }
  }
]
```

### 6. Open a PR

Our automated checks will:
- ✅ Validate your manifest schema
- ✅ Scan for security issues (no executable code, no secrets, no suspicious URLs)
- ✅ Preview how it'll appear on the site

Once approved and merged, your skill automatically appears on [theagentmag.com/skills](https://theagentmag.com/skills).

---

## Example Skill

See [`skills/.example/`](skills/.example/) for a complete reference implementation.

---

## Architecture

```
Community PR → This repo (public) → Automated checks → Merge → Webhook → theagentmag.com
```

This repo is the **source of truth** for skill definitions. The Agent Mag platform syncs from this repo on every merge. The platform codebase is private — contributors only interact with this public repo.

---

## Guidelines

- **No executable code.** Skills are config bundles: prompts, tool schemas, and metadata. If your skill requires running code, it belongs in [Agent-mag/tools](https://github.com/Agent-mag/tools) instead.
- **One skill, one job.** Keep skills focused on a single capability.
- **Be specific in prompts.** Vague prompts produce vague results. Include edge cases and expected behavior.
- **MIT license.** All skills in this registry are MIT-licensed.
- **Respect the schema.** PRs that don't match the manifest schema will be auto-rejected.

---

## License

MIT — see [LICENSE](LICENSE) for details.

All skills contributed to this registry are released under the MIT license.

---

<div align="center">

**Built by [Agent Mag](https://theagentmag.com)** — the magazine for AI agent builders.

[Website](https://theagentmag.com) &nbsp;&middot;&nbsp; [Tools](https://theagentmag.com/tools) &nbsp;&middot;&nbsp; [Skills](https://theagentmag.com/skills) &nbsp;&middot;&nbsp; [Newsletter](https://theagentmag.com/newsletter) &nbsp;&middot;&nbsp; [GitHub](https://github.com/Agent-mag)

</div>
