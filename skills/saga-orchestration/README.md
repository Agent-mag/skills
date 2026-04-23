# saga-orchestration

Implement saga patterns for distributed transactions and cross-aggregate workflows. Use this skill when implementing distributed transactions across microservices where 2PC is unavailable, designing compensating actions for failed order workflows that span inventory, payment, and shipping services, building event-driven saga coordinators for travel booking systems that must roll back hotel, flight, and car rental reservations atomically, or debugging stuck saga states in production where compensation steps never complete.

## Install

```bash
npx agentmag add skill saga-orchestration
```

## Author

**wshobson**

## Source

- [skills.sh](https://skills.sh/wshobson/agents/saga-orchestration)
- [GitHub](https://github.com/wshobson/agents)

## License

See source repo

---

*Part of the [Agent Mag Skills Registry](https://theagentmag.com/skills). Synced from the skills.sh ecosystem.*
