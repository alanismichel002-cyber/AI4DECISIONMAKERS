# AI4DECISIONMAKERS: GES M&A Advisory Agents

Fifteen specialist AI agents that support mergers & acquisitions advice for GES (Global Experience Specialists) senior leadership: eight deal-team roles and seven cybersecurity roles (GRC, SOC/blue team, red team/AppSec).

| Where | What |
|---|---|
| `.claude/skills/<name>/SKILL.md` | Each agent's expertise as an [Agent Skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) |
| `.claude/agents/<name>.md` | Claude Code subagent for each role (loads its skill, with scoped tools) |
| `CLAUDE.md` | Roster and the rules every agent follows |
| `docs/ges-context.md` | GES company and events-industry background |
| `docs/demo-prompts.md` | Prompts that show the agents talking to each other |
| `deals/` | One folder per target: outputs plus `handoffs.md`, the agents' message log |

## Use in Claude Code
Open this repository in Claude Code. The skills and subagents load automatically. Try:
```
Use the ges-corp-dev-lead skill to run a full assessment of <Target Company>.
```

## Use in Claude.ai or the API
Run `python3 scripts/package-skills.py`. Then upload any zip from `dist/skills/` in Claude.ai (Settings > Capabilities > Skills) or through the API's Skills endpoint.

## Guardrails
Every claim is either sourced or labelled as an assumption. Legal, tax, and labor outputs are issue-spotting for licensed professionals, not advice. Cyber work is passive-only until the target gives written authorization. Confidential data-room files (`deals/*/inputs/`) are git-ignored.
