# Recommended lean software stack

Research checked 2026-10-13. Recommendation for one owner and zero to five employees; no product was purchased, installed, connected or configured. USD prices below exclude taxes and transaction fees. Existing tools that already work should be kept unless a specific gap justifies migration.

## Start with a small set of systems

Use one accounting/invoicing ledger, one sales pipeline, one support queue, one password vault and one project board. Reuse tools across categories. Keep this public repository limited to blank templates, policies and fictional examples. Live contracts, client records, employee files, credentials, financial exports and incident evidence belong in approved private systems.

| Category | Initial recommendation | Verified limits or price | Why and upgrade trigger |
|---|---|---|---|
| CRM | HubSpot Free, limited to owner and sales lead | Two users, 1,000 contacts; [vendor](https://www.hubspot.com/pricing/crm) | Simple shared pipeline. Re-evaluate before a third user, contact-cap pressure or automation requirement; do not share logins. |
| Invoicing | Wave, same account as bookkeeping | Starter has unlimited estimates/invoices; payment processing costs extra; [vendor](https://www.waveapps.com/pricing) | Avoid duplicate invoice ledgers. Use approved invoice/tax configuration and export reconciled records. |
| Accounting | Wave Pro after CPA fit check; Starter if manual workflow is acceptable | Pro $19/month or $190/year; Starter $0. Pro includes bank import and receipt capture; [vendor](https://www.waveapps.com/pricing) | Small-service-business candidate. Accountant access, reporting, recurring billing and tax workflows must be tested before selection. |
| Payroll | Gusto Simple only when payroll is needed and eligible | $49/month + $6/person/month; single-state starting option; Plus $80 + $12/person includes multi-state; [vendor](https://gusto.com/product/pricing) | Assign employer/provider responsibilities. Owner payroll depends on tax treatment; zero employees does not automatically mean no payroll. |
| Ticketing | Zoho Desk Free | Up to three users; [vendor](https://www.zoho.com/desk/pricing.html) | Dedicated support history. Review before fourth agent or advanced SLA/automation needs; a software feature is not a contractual SLA. |
| Password management | Bitwarden Teams | $4/user/month billed annually; [vendor](https://bitwarden.com/pricing/) | Company-owned shared collections and audit history. Prefer business administration for client access; free personal vaults are not the team operating model. |
| Documentation | Markdown in GitHub for non-sensitive procedures; approved private document store for records | GitHub Free permits unlimited public/private repos and collaborators with plan limitations; [vendor](https://docs.github.com/en/get-started/learning-about-github/githubs-plans) | Keep portable source files. Do not place private records in this public repo or assume private branch contents are private in a public repo. |
| Contracts and e-signature | Zoho Sign Free for owner-only sending | One user and five envelopes/month, audit trail; [vendor](https://www.zoho.com/sign/pricing.html) | Export executed PDFs and audit evidence privately. Review above cap or for multiple senders, templates or integrations; paid price needs a current quote. |
| Uptime monitoring | Better Stack free monitoring within capacity | Ten monitors, ten heartbeats, status page, three-minute checks; [vendor](https://betterstack.com/uptime) | Covers a small starting footprint. More checks/faster detection/on-call requirements need a priced plan before promising them. |
| Backup monitoring | Reuse Better Stack heartbeats; Healthchecks.io if more independent job checks are needed | Better Stack capacity above; Healthchecks free 20 checks; [vendor](https://healthchecks.io/pricing/) | Send completion only after backup validation. A heartbeat is not backup storage, integrity verification or a successful restore test. |
| Project management | GitHub Issues/Projects for technical delivery | Use existing Free plan; [vendor](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories) | Link work to code and checklists. Private client details require an approved private project/repository. Keep the public business repo generic. |
| Business analytics | CSV exports plus LibreOffice Calc | No license fee for business use; [vendor](https://business.libreoffice.org/faq/) | Monthly KPI review is enough initially. Keep real revenue/payroll/client data private; add a BI platform only when repeated analysis justifies upkeep. |

Paid plans are proposals, not approvals. [Alternatives](ALTERNATIVES.md) compares each category; [Cost estimate](SOFTWARE_COST_ESTIMATE.md) separates selected software from operating costs.

## Fit and portability test before adopting

Owner: [[TOOLING_OWNER]]. Use fictional data until vendor/privacy review and authorized setup are complete.

- [ ] Check current price, billing period, minimum seats, trial conversion, renewal, cancellation, refunds and usage overages.
- [ ] Confirm business ownership, MFA/recovery, scoped access and offboarding. Do not use employee personal accounts as sole owners.
- [ ] Confirm data region, subprocessors, retention/deletion, breach terms and any needed DPA/customer permission. Vendor compliance marketing does not certify Noirdaz.
- [ ] Export sample contacts/deals, invoices/ledger, tickets, signed documents/audit trails, tasks and monitor configurations. Test that records, attachments, IDs and dates survive; do not assume all exports are available on a free tier.
- [ ] Define [[SYSTEM_OF_RECORD]] for each object and [[PRIVATE_EXPORT_LOCATION]]. Proposed cadence: monthly exports plus pre-migration export; verify restore/readability quarterly.
- [ ] Check notification limits and ownership; create an owner backup route independent of the failing service.
- [ ] Disable unneeded paid/AI/credit features and set available spending limits before approved use. No automatic trial conversion or migration is authorized by this document.
- [ ] Obtain transaction-specific discussion and approval in principle, then separate explicit final confirmation immediately before any spending/financial commitment. Reapprove changes.

## Order of adoption

1. Inventory existing tools, data owners, costs and renewal dates.
2. Approve private records storage and company-owned vault.
3. CPA chooses the accounting system; validate one complete invoice-to-reconciliation cycle.
4. Add CRM/support/project workflows using manual handoffs first.
5. Validate monitoring and backup/restore evidence against actual service promises.
6. Implement payroll before the first relevant pay date, after professional and owner approvals.
7. Automate only a stable, reversible workflow with its own approval and spending controls.
