
# event (v1)

> **前置条件：** 先阅读 [`../lark-shared/SKILL.md`](../lark-shared/SKILL.md) 了解认证、权限处理和安全规则。

## Shortcuts（推荐优先使用）

Shortcut 是对常用操作的高级封装（`lark-cli event +<verb> [flags]`）。有 Shortcut 的操作优先使用。

| Shortcut | 说明 |
|----------|------|
| [`+subscribe`](references/lark-event-subscribe.md) | Subscribe to Lark events via WebSocket long connection (read-only, NDJSON output); bot-only; supports compact agent-friendly format, regex routing, file output |

