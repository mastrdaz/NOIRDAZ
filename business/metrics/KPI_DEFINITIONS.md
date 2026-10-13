# KPI definitions

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Choose one reporting currency, timezone, period cutoff and source owner. Preserve monthly snapshots and definitions. Report “not available” for missing data or a zero denominator; do not imply zero performance. Use aggregate IDs, not personal data, in exports.

| Metric | Definition and period logic | Source / owner |
|---|---|---|
| Leads | Distinct qualified-to-enter lead records created in period; exclude duplicates/spam | CRM / owner |
| Discovery calls | Completed discovery meetings in period, separately from scheduled | CRM / sales |
| Proposals | Distinct opportunity proposals first sent in period; revisions separately tracked | CRM / sales |
| Wins | Executed opportunities closed-won in period, not verbal yes | Contract register / owner |
| Closed-deal conversion | Won ÷ (won + lost) for opportunities closed in period; N/A if none | CRM / owner |
| Lead cohort conversion | Leads created in one cohort that later win ÷ that cohort's leads; state observation window | CRM / owner |
| Sales cycle | Median days from qualified date to executed win for period wins | CRM / owner |
| MRR | Active committed recurring pre-tax revenue normalized to month; exclude setup, usage and pass-throughs | Service tracker / bookkeeper |
| One-time revenue | Recognized nonrecurring revenue in period under the accounting policy | Books / bookkeeper |
| Gross margin | (Recognized revenue − matching delivery COGS) ÷ recognized revenue | Books / bookkeeper |
| Fully loaded service contribution | Revenue less direct delivery, modeled labor, variable fees and explicitly allocated overhead; label economic vs accounting basis | Cost model / owner |
| Hosting cost | Matching hosting/database/storage/bandwidth/backups/monitoring cost, allocated once | Supplier ledger / service owner |
| Support cost | Logged support time × documented loaded rate plus direct support vendor cost | Time/cost ledger / owner |
| Accounts receivable | Unpaid issued invoice balances less applicable credits as of date; aging by due date | Books / bookkeeper |
| Cash reserve | Unrestricted reconciled cash less identified near-term obligations; separately show tax/client liabilities | Bank/books / owner |
| Active clients | Distinct clients with active contracted service at month end | Client register / owner |
| Client churn | Clients active at start who ended all recurring service during period ÷ start active clients | Service tracker / owner |
| Gross revenue churn | (Contraction + churn MRR) ÷ beginning MRR; exclude expansion from numerator | MRR bridge / owner |
| Average MRR per client | Ending MRR ÷ active recurring clients at the same date | Service tracker / owner |
| Support tickets | New tickets, closed tickets, month-end backlog and overdue updates reported separately | Ticket system / support |
| Client health | Defined score plus reason, risk flags, last evidence and next action | Health review / owner |
| Renewals | Contracts and notice deadlines in next 90 days, with at-risk revenue | Renewal tracker / owner |
| Uptime | (Eligible measured minutes − unplanned unavailable minutes) ÷ eligible measured minutes; state exclusions/gaps | Independent monitor / service owner |
| Backup failures | Failed or missed expected backup jobs; also report clients without recent verified restore | Backup logs / service owner |
| Incidents | Distinct availability/security incidents by severity and duration | Incident log / owner |
| Overdue maintenance | Approved maintenance items past due, with severity and affected service | Maintenance register / service owner |
| Vendor renewals | Count and amount due/notice deadline within 30/60/90 days | Vendor register / owner |

Do not compare sampled uptime to a contractual SLA without matching its measurement/exclusion terms. Do not sum percentages to obtain company margin; calculate from total revenue and matching costs. Small cohorts are volatile; show numerator/denominator and avoid unsupported forecasts.
