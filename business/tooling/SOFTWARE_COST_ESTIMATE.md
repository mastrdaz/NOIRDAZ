# Software cost estimate

Working planning values, checked 2026-10-13. USD before tax. Not a quote, approved budget or purchase authorization. No payroll or other financial product was activated. Assumptions must be replaced with actual headcount, client footprint, required features and current vendor terms.

## Core monthly equivalent

Assumptions: Wave Pro monthly at $19; Bitwarden Teams annual commitment at $4/user/month equivalent; Gusto Simple at $49 + $6/person/month when applicable; owner is not on payroll in the example. Other categories stay within verified free limits. Owner seats count where used. These are scenario assumptions, not conclusions about owner compensation.

| Component | Owner only, no payroll | Owner + one employee | Owner + five employees |
|---|---:|---:|---:|
| Wave Pro accounting and invoicing | $19 | $19 | $19 |
| Bitwarden Teams, 1 / 2 / 6 users | $4 | $8 | $24 |
| Gusto Simple, 0 / 1 / 5 payroll people | $0 | $55 | $79 |
| CRM, tickets, e-sign, uptime/heartbeats, docs/projects and Calc within caps | $0 | $0 | $0 |
| Core monthly equivalent | **$23** | **$82** | **$122** |
| Core 12-month equivalent | **$276** | **$984** | **$1,464** |

Source prices: [Wave](https://www.waveapps.com/pricing), [Bitwarden](https://bitwarden.com/pricing/), [Gusto](https://gusto.com/product/pricing). The last column is viable only if CRM has at most two named users, support at most three, and owner-only e-sign/monitor limits fit. It is not a six-seat free license for every tool.

### Cash timing and alternatives

- Bitwarden’s modeled commitment is $48/$96/$288 per year for 1/2/6 users, generally paid on annual billing; the table spreads it for comparison. Check actual checkout terms and any minimum before approval.
- Wave Pro annual $190 replaces $228 across twelve monthly payments, but creates an up-front commitment. No annual purchase is recommended automatically.
- If the owner legitimately needs payroll, add the applicable paid-person charge, and activate a base payroll subscription if none exists. CPA makes that decision.
- Gusto Plus alternative for multi-state examples: $80 + $12/person/month, or $92 for one payroll person and $140 for five. Recheck supported services and extra charges.
- Wave Starter can reduce subscription cost by $19/month if manual bookkeeping and required access/features are workable; saved labor may justify Pro.
- Healthchecks Business adds $20/month or $192/year when selected, and Dropbox Sign Essentials adds $180/year if it replaces the free e-sign workflow. Neither is included above.

## Operating allowances beyond the core

The following are explicitly unquoted planning allowances, not verified vendor prices. Replace them with a scoped quote before a budget is approved.

| Allowance | Owner only | Owner + one | Owner + five |
|---|---:|---:|---:|
| Business email/private document storage, proposed $6–$15 per user/month | $6–$15 | $12–$30 | $36–$90 |
| Additional monitoring/backup-job capacity and notification reserve | $0–$40 | $0–$40 | $20–$80 |
| Paid CRM/helpdesk/e-sign feature reserve | $0–$30 | $0–$60 | $30–$150 |
| Core plus these allowances, monthly | **$29–$108** | **$94–$212** | **$208–$442** |
| Annualized planning range | **$348–$1,296** | **$1,128–$2,544** | **$2,496–$5,304** |

Do not use the low end until seats, monitoring jobs and actual work are counted. Existing subscriptions may reduce incremental cost; paid export/security requirements may raise it. No contingency range guarantees a vendor can supply the required service at that price.

## Excluded costs

Client hosting, domains, databases, storage/bandwidth, backup storage and retrieval, processor fees, chargebacks, sales taxes, payroll wages/taxes, benefits, workers’ compensation, hardware, endpoint management/security, legal/CPA services, implementation labor, migration, AI credits and paid automation are excluded. Allocate client-specific infrastructure to the relevant service cost model. Heartbeat monitoring does not buy backups.

## Reusable calculation

Monthly equivalent = monthly fixed subscriptions + sum(required seats × per-seat rate) + usage charges + annual commitments / 12 + forecast tax.

Annual cash forecast = actual scheduled monthly charges + actual annual renewals + one-time setup/migration + expected usage and tax. Avoid counting an annual subscription both as twelve monthly equivalents and as an extra renewal.

Private budget fields: [[TOOL_NAME]], [[PLAN_NAME]], [[SEAT_COUNT]], [[MONTHLY_RATE]], [[ANNUAL_COMMITMENT]], [[USAGE_ASSUMPTION]], [[TAX_ESTIMATE]], [[RENEWAL_DATE]], [[CANCELLATION_DEADLINE]], [[BUDGET_OWNER]], [[APPROVAL_REFERENCE]].

## Approval gate

Before any action risking money, credits, assets or financial obligations: discuss the actual counterparty, costs, recurrence, terms and risks; obtain approval in principle; then obtain separate explicit final confirmation immediately before execution. Approval is transaction-specific and changes require reapproval. A planning estimate, free trial or a small/refundable amount does not waive the gate.
