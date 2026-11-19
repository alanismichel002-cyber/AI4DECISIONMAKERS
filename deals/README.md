# deals/

One folder per target: `deals/<target-slug>/` (e.g., `deals/acme-event-tech/`).

Put data-room documents in `deals/<target-slug>/inputs/`. Agents write their outputs here, using these file names:

| File | Agent |
|---|---|
| `00-deal-brief.md` | ges-corp-dev-lead |
| `01-screening.md` | ges-target-screener |
| `02-industry-fit.md` | ges-trade-show-industry-analyst |
| `03-event-tech.md` | ges-event-tech-specialist |
| `04-valuation.md` | ges-valuation-modeler |
| `05-qoe-diligence.md` | ges-qoe-diligence-coordinator |
| `06-labor-venue-contracts.md` | ges-labor-venue-contracts-risk |
| `07-integration-plan.md` | ges-integration-synergy |
| `10-cyber-summary.md` | ges-cyber-diligence-lead |
| `11-privacy-pci.md` | ges-privacy-pci-compliance |
| `12-grc-score.md` | ges-grc-framework-scorer |
| `13-threat-intel.md` | ges-threat-intel-attack-surface |
| `14-compromise-assessment.md` | ges-compromise-assessment |
| `15-appsec.md` | ges-appsec-reviewer |
| `16-iam-integration.md` | ges-iam-integration-security |
| `99-ic-memo.md` | ges-corp-dev-lead (final) |

**Do not commit real confidential deal data to a shared repository.** `deals/*/inputs/` is git-ignored by default.
