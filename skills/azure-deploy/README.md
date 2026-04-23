# azure-deploy

> Execute Azure deployments for ALREADY-PREPARED applications that have existing .azure/deployment-plan.md and infrastructure files. DO NOT use this skill when the user asks to CREATE a new application — use azure-prepare instead. This skill runs azd up, azd deploy, terraform apply, and az deployment commands with built-in error recovery. Requires .azure/deployment-plan.md from azure-prepare and validated status from azure-validate. WHEN: "run azd up", "run azd deploy", "execute deployment", "push to production", "push to cloud", "go live", "ship it", "bicep deploy", "terraform apply", "publish to Azure", "launch on Azure". DO NOT USE WHEN: "create and deploy", "build and deploy", "create a new app", "set up infrastructure", "create and deploy to Azure using Terraform" — use azure-prepare for these.

**Category:** Code & Compute · **License:** MIT

## Install

```bash
npx agentmag add skill azure-deploy
```

## What This Skill Does

This skill provides a reusable prompt configuration for AI coding agents. When installed, it adds structured instructions that guide your agent's behavior for **azure-deploy** tasks.

## Compatibility

- Claude Code
- Cursor
- Windsurf
- Copilot


## Author

**microsoft**

---

Part of the [Agent Mag Skills Registry](https://theagentmag.com/skills) — the open catalog of AI agent skills.
