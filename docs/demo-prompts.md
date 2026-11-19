# Demo prompts: watching the agents talk to each other

The agents talk through `deals/<target-slug>/handoffs.md`, a numbered message log of FINDINGs, QUESTIONs, CHALLENGEs, ANSWERs, and DECISIONs. Open that file while a prompt runs (or ask Claude to show it at the end) to watch the conversation.

> **Tip:** to avoid exposing real deal interest, start with a **public company you're curious about**, or a clearly **hypothetical** target (prompt 6). For a hypothetical target, the agents must label every invented fact `[HYPOTHETICAL]`.

---

### 1. The full deal: everyone talks
```
Use the ges-corp-dev-lead skill to run a full assessment of <Target Company>.
Run at least two message rounds in handoffs.md. When done, show me the
handoffs.md conversation and the IC memo bottom line.
```
**What you'll see:** 15 agents posting findings, the orchestrator re-routing open questions, and an IC memo section called "How the agents disagreed".

### 2. Price fight: valuation vs. the risk agents
```
For <Target Company>: have ges-valuation-modeler propose an offer price first.
Then have ges-labor-venue-contracts-risk and ges-cyber-diligence-lead each post
a CHALLENGE in handoffs.md arguing what should come off the price or move into
escrow/indemnity. Let ges-valuation-modeler respond to each challenge, then
have ges-corp-dev-lead post a DECISION. Show me the full exchange.
```

### 3. Cyber chain reaction (SOC → IAM → integration)
```
For <Target Company>: run ges-threat-intel-attack-surface (passive only).
Have it post its top findings to ges-compromise-assessment. Compromise
assessment decides whether they raise breach likelihood and posts gate
criteria to ges-iam-integration-security, which then tells
ges-integration-synergy whether the Day-1 plan or synergy timing must change.
Show me each handoff in order.
```

### 4. Cross-sell vs. privacy (event tech vs. GRC)
```
For <Event Tech Target>: have ges-event-tech-specialist build the cross-sell
case for using the target's attendee and lead data across GES shows. Then have
ges-privacy-pci-compliance CHALLENGE whether that data can legally transfer and be
reused under GDPR/CCPA. Let them go back and forth up to 3 times, then have
ges-corp-dev-lead decide how much of the revenue synergy survives.
```

### 5. Screening debate
```
Use ges-target-screener to build a short list of 5 event-technology or AV
acquisition targets for GES in North America. Then have
ges-trade-show-industry-analyst and ges-threat-intel-attack-surface each post a
CHALLENGE to the ranking (strategic fit vs. outside-in cyber exposure).
Screener responds and re-ranks. Show the before/after ranking and the debate.
```

### 6. Tabletop crisis (hypothetical, safe to demo live to leadership)
```
Hypothetical tabletop. Target: "Northwind Event Systems" (fictional
registration & lead-retrieval company, ~$40M revenue, label all facts
[HYPOTHETICAL]). Scenario: two weeks before closing, ges-threat-intel-attack-surface
finds the target named on a ransomware leak site. Run the response: each
affected agent (compromise assessment, privacy/PCI, labor/contracts,
valuation, integration, corp dev) posts in handoffs.md what it needs and
what it recommends. End with the corp dev DECISION: delay, re-price, add
conditions, or walk away.
```

### 7. Ask a single agent a question
```
Ask ges-labor-venue-contracts-risk: what are the top 5 labor risks when GES
buys a unionized AV company in Las Vegas, and what should it ask
ges-qoe-diligence-coordinator to request?
```
