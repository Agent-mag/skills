HEADER = """\
<div align="center">
  <img src="https://raw.githubusercontent.com/Agent-mag/.github/main/profile/agentmag-banner-github.png" alt="Agent Mag" width="600" />
  <p><strong>Open registry of installable AI agent skills</strong> &middot; <a href="https://theagentmag.com/skills">theagentmag.com/skills</a></p>
</div>

---

"""

FOOTER = """

---

<sub>Release notes polished by Azure OpenAI &middot; <a href="https://theagentmag.com">theagentmag.com</a></sub>
"""

with open("/tmp/polished-changelog.md") as f:
    changelog = f.read()

with open("/tmp/release-body.md", "w") as f:
    f.write(HEADER + changelog + FOOTER)
