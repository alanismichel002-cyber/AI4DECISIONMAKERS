# AI4DECISIONMAKERS — GES M&A Advisory Agents

This project supports an advisory engagement with **GES (Global Experience Specialists, ges.com)** senior leadership on mergers & acquisitions. The goal is expertise for decision makers, plus a small M&A application, not a large software build.

Read `docs/ges-context.md` before doing any deal work. It holds the company and industry background every agent relies on.

## Agent roster (15)
Each agent is a **skill** (`.claude/skills/<name>/SKILL.md`, the expertise) with a matching **subagent** (`.claude/agents/<name>.md`, which delegates to it).

**Deal team (business)**
1. `ges-corp-dev-lead`: orchestrator. Runs the deal workflow and writes the IC memo.
2. `ges-target-screener`: builds the target list and screens it.
3. `ges-trade-show-industry-analyst`: market, competitors, trends.
4. `ges-event-tech-specialist`: evaluates event technology targets.
5. `ges-valuation-modeler`: valuation, comparables, returns.
6. `ges-qoe-diligence-coordinator`: quality of earnings and the diligence request list.
7. `ges-labor-venue-contracts-risk`: unions, venue exclusives, change-of-control clauses.
8. `ges-integration-synergy`: 100-day plan and synergies.

**Cyber team**
9. `ges-cyber-diligence-lead`: cyber orchestrator. Produces the cyber risk rating.
10. `ges-privacy-pci-compliance`: GDPR, CCPA, PCI-DSS, attendee data.
11. `ges-grc-framework-scorer`: NIST CSF 2.0 / CIS gap scoring.
12. `ges-threat-intel-attack-surface`: passive OSINT and attack-surface mapping.
13. `ges-compromise-assessment`: "are we buying a breach?"
14. `ges-appsec-reviewer`: registration, lead retrieval, and API security.
15. `ges-iam-integration-security`: identity, access, and the Day-1 connection plan.

## How to run a deal
Tell Claude: *"Use the ges-corp-dev-lead skill to run a full assessment of <Target Name>."*
The orchestrator delegates to the specialist subagents, and each writes its output into `deals/<target-slug>/`. Subagents cannot spawn other subagents, so always run the orchestrators (`ges-corp-dev-lead`, `ges-cyber-diligence-lead`) from the main conversation.

## How the agents talk to each other
Every deal folder has `handoffs.md`, an append-only message log. Agents post `FINDING`, `QUESTION`, `REQUEST`, `CHALLENGE`, and `ANSWER` messages addressed to each other. The orchestrators re-run any agent with OPEN messages (up to 3 rounds) and post `DECISION`s on challenges. See `docs/demo-prompts.md`.

## Rules every agent follows
- **Source every claim.** Facts get a source (URL, document name, or page). Anything else is labelled `[ASSUMPTION]` or `[ESTIMATE]`. Never invent financials, customers, or contacts.
- **Not professional advice.** Legal, tax, labor-law, and audit outputs prepare issues for licensed professionals to review. They are not opinions.
- **Confidentiality.** Data-room material (financials, contracts, employee data) never goes into web searches or external tools. Public research on a target's name is fine.
- **Cyber rules of engagement.** Before a signed NDA *and* written authorization from the target, only passive, public-source research is allowed: no scanning, no probing, no login attempts. Active testing requires that authorization and a human tester under contract.
- **Write for executives.** Every output starts with a 3-to-5 bullet "Bottom line" and a clear rating, then the detail.
