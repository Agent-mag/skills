# Contributing a Skill

Thanks for contributing to the Agent Mag skills registry.

## Quick Start

1. Fork this repo
2. Create `skills/your-skill-name/` with the required files
3. Open a PR
4. Automated checks run — fix any issues
5. We review and merge
6. Your skill goes live on [theagentmag.com/skills](https://theagentmag.com/skills)

## Required Files

| File | Purpose |
|------|---------|
| `manifest.json` | Name, description, category, version, author |
| `prompt.md` | System prompt for the agent |
| `tools.json` | Tool schemas (function definitions) |
| `config.json` | Optional — default settings |

See [`skills/.example/`](skills/.example/) for a complete reference.

## Rules

- **No executable code.** Skills are config bundles only.
- **One skill, one job.** Keep it focused.
- **MIT license.** All contributions are MIT-licensed.
- **Follow the schema.** Check `skills/.example/manifest.json` for the format.

## Questions?

Open an issue or reach out at [hello@theagentmag.com](mailto:hello@theagentmag.com).
