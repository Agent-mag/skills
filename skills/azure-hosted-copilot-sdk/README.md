# azure-hosted-copilot-sdk

Build, deploy, modify GitHub Copilot SDK apps on Azure. MANDATORY when codebase contains @github/copilot-sdk or CopilotClient — use this skill instead of azure-prepare. PREFER OVER azure-prepare when codebase contains copilot-sdk markers. WHEN: copilot SDK, @github/copilot-sdk, copilot-powered app, deploy copilot app, add feature, modify copilot app, BYOM, bring your own model, CopilotClient, createSession, sendAndWait, azd init copilot. DO NOT USE FOR: general web apps without copilot SDK (use azure-prepare), Copilot Extensions, Foundry agents (use microsoft-foundry).

## Install

```bash
npx agentmag add skill azure-hosted-copilot-sdk
```

## Author

**microsoft**

## Source

- [skills.sh](https://skills.sh/microsoft/azure-skills/azure-hosted-copilot-sdk)
- [GitHub](https://github.com/microsoft/azure-skills)

## License

MIT

---

*Part of the [Agent Mag Skills Registry](https://theagentmag.com/skills). Synced from the skills.sh ecosystem.*
