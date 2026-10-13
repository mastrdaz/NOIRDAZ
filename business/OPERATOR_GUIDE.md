# Noirdaz operator guide

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

This guide shows how to use the business system for a small software, website and hosting company. The reusable source checklists and contract drafts carry the details. Start with one client and one workflow; keep actual records in approved private storage.

## 1 Establish the operating facts

Verify the legal business identity, entity/tax treatment, owner authority, work locations and actual insurance. Assign the owner and backup for sales, delivery, support, finance and compliance. Until someone else is named, the owner is accountable. Do not advertise an LLC, a certification, 24/7 coverage or an SLA based on a planning note.

Adopt the working choices in [owner decisions](OWNER_DECISIONS.md). Have counsel review legal templates, the CPA review taxes/payroll/bookkeeping, and the broker review coverage. The public repository holds blank templates and fictional examples only. Store client contracts, contacts, incidents, live costs, payroll and access indexes privately; secrets remain in the approved vault.

## 2 Run a new opportunity

Create a private lead record. Record the actual need, source, contact context, budget band, decision-maker, timing and data/payment risks. Every opportunity has one stage, next action, owner and due date. Review the pipeline weekly. Follow-up guidance is not an automated sending authorization.

Use the discovery template to establish measurable success, required workflows, existing providers/API rights, account ownership, client inputs, support expectations and regulated-data constraints. Escalate unknown integrations and sensitive data before a fixed-price promise. Prepare a proposal describing approach and boundaries, then a costed quote with expiry, taxes for review, setup/recurring split and third-party payer.

The lifecycle is lead, qualification, discovery, proposal, quote, contract/SOW, deposit/payment setup, access/intake, execution, client review, acceptance, launch, recurring service, support, renewal/expansion and offboarding. The client lifecycle table defines the evidence and gate at each handoff.

## 3 Quote from costs

Include discovery, design, build, setup, migration, test, documentation, launch and legal/admin effort. Recurring economics include hosting/storage/bandwidth/database, backups, monitoring, email/domains/licenses, support, maintenance/security, payment fees and administration. Count founder time and allocate shared costs once.

For non-percentage cost C, fixed transaction fees F, target fully loaded margin m and variable revenue fee fraction v, price is (C + F) / (1 − m − v). A 40% margin on $100 cost needs $166.67 before fees, not $140. The workbook also accounts for processing fees on tax where applicable. Its figures are fictional USD examples; replace them with actual assumptions and verify the tax basis.

The target is an economic contribution after allocated costs. Accounting gross margin uses recognized revenue and matching delivery COGS; keep the two labels distinct. Annualize recurring costs once. Check the minimum viable floor before any pilot discount and set a pilot end date/limit. A valid formula is not approval to quote, spend or charge.

## 4 Select and review the contract package

Use the MSA plus SOW, with only relevant hosting, software/integration, payment and support exhibits. The website form is a lighter project order under the MSA. Use the mutual NDA for appropriate pre-contract discovery, change order for approved scope changes, acceptance/launch form for explicit decisions, and offboarding form for transfer/exit.

All are DRAFT ATTORNEY REVIEW and unapproved for signature. Fill exact party facts, attach referenced schedules, resolve commercial choices and the liability/IP/privacy/SLA/renewal/cancellation decisions, and have counsel approve the final version. The privacy questionnaire gathers facts; it is not a DPA or BAA. Productized software such as Sync Coverage may need separate subscription/product terms.

Do not remove unresolved issues to make a packet appear final. Client details, business decisions and professional review are distinct steps. Preserve the signed immutable package and its version privately. A quote, paid invoice or verbal yes is not a substitute for the specified contract and launch approvals.

## 5 Onboard and deliver

After executed scope and any required cleared deposit, create the private client record, verify contacts and authority, collect assets, and obtain least-privilege named access. Confirm domain/merchant ownership, separate test from production, and complete the security/privacy review before production data enters the service.

Create a project plan with deliverables, criteria, milestones, dependencies, time/cost budget, tests, risks, review and rollback. Send approved factual status updates at agreed intervals. Record defects against the signed criteria separately from requested changes. A scope change needs its impact assessed and an approved written change order before additional work/spend.

Acceptance requires evidence tied to a version and authorized client review. Launch is a separate go/no-go: approval, tested backup, rollback, TLS/access, monitoring, data/payment/accessibility requirements, client communications and support readiness. After an authorized launch, verify the important client journey and actual recurring start condition, then close out delivery economics and hand support the runbook.

## 6 Operate hosting and support

Each service needs an owner, inventory, account roles, support entitlement, renewal dates, backup/restoration path and monitoring route. Monitoring is not continuous human coverage. Recovery objectives must be feasible and tested; no generic uptime or data-loss guarantee is implied.

Proposed internal baseline: daily backup-job checks, monthly sample restores, weekly advisory review, monthly routine maintenance and quarterly capacity/access review, adjusted to actual risk, platform, signed scope and approved cost. Assign the checks before claiming they run. A missing alert heartbeat is itself a failure condition.

Log tickets with impact, priority, evidence, owner and next update. P1 covers broad outage, active compromise, likely data loss or payment integrity failure; P2 major blocked workflows; P3 limited defects; P4 requests. Actual response/update targets remain fillable until staffing and contracts support them. Separate normal support from enhancement scope. Never claim a response target is a resolution guarantee.

For an outage, establish facts, record a timeline, notify the owner, use authorized runbooks, communicate the next update, verify recovery and assign corrective actions. Suspected compromise invokes the security incident plan and counsel/insurer notice review. Do not guess cause, breach scope or restoration time.

## 7 Protect accounts and data

Use a password manager, MFA and least privilege. Keep named access separate across clients and environments. Vault references belong in private records; actual secrets never belong in Git, documents, tickets or logs. Use synthetic/redacted test data and minimize production data, logging and external disclosure.

Before a vendor sees client data, review its purpose, permissions, subprocessors/locations, terms, incident route and exit plan. Before any new persistent access or credential, obtain required approval. Rotate/revoke exposed secrets; deleting the visible file does not invalidate leaked credentials.

Maintain private incident contacts and a retention schedule by category. Legal holds override deletion. Verify offboarding access removal, sessions/OAuth/keys and shared-secret rotation. Permanent deletion and other consequential actions retain their separate approval requirements.

## 8 Close the financial month

Reconcile bank/card/processor/payroll statements. Match gross collections, fees, refunds, disputes and net settlements. Reconcile invoices, credits, deposits, active recurring services and receivables aging. Categorize costs, attach receipts and resolve allocations. Have the bookkeeper/CPA handle accounting method, deferred revenue, tax treatment, assets and reporting.

Review the MRR bridge, recognized revenue, delivery gross margin, fully loaded contribution, support burden, unrestricted cash, tax/client liabilities and next 90 days of commitments. MRR excludes setup, taxes, uncommitted usage and pass-throughs. Quote pipeline, invoiced sales, recognized revenue and cash are separate measures.

Before refunds, payroll, vendor payments or any action risking money/credits/assets/obligations, discuss the counterparty, total cost, recurrence, terms and risks; obtain approval in principle and separate explicit final confirmation immediately before execution. A planning allowance, urgent incident or small/refundable amount does not waive that requirement.

## 9 Hire and expand carefully

Before the first employee, verify role/duties, work location, classification, wage/overtime and commission plan; payroll/withholding/UI registration; workers' compensation; I-9/new-hire timing; posters; access/equipment/training; and confidentiality/IP documentation. Keep completed employee and tax records in restricted storage.

Wisconsin UI and workers' compensation have different triggers and rules. Do not reuse a generic percentage or presume a sales title/commission structure creates an exemption. The current compliance files link official sources and identify fact-dependent gates. Every new employee work state and material new client/data jurisdiction triggers a fresh review before expansion.

On departure, coordinate lawful final pay and records with payroll/counsel, transfer responsibilities, revoke access at the approved time, preserve holds and verify equipment/account recovery. Do not withhold lawful final pay because equipment is missing.

## 10 Review renewals and client health

Track contract notice deadlines, domain expiry, insurance and vendor commitments by working backward from the cancellation deadline. Review client value, margin, unresolved incidents and support burden before renewal. Change pricing or scope only under the agreement and with the required approval.

Use the monthly business review to make a few concrete decisions. Show source, period and numerator/denominator for metrics; mark missing data unavailable. A client health score is a prioritization aid with evidence and owner judgment, not an automatic cancellation or pricing rule.

For offboarding, agree termination timing, secure exports, account/domain transfer, source/database/configuration handover, final billing and retention. Verify receipt and continuity before ending old services where agreed. Revoke Noirdaz access, record deletion/backup-expiry limits and preserve required records. A disputed bill does not create a blanket right to hold client-owned data or domains.

## 11 Keep the system lean

The tooling comparison covers CRM, invoicing, accounting, payroll, tickets, passwords, documents, signatures, uptime, backup-job monitoring, projects and analytics. Check real seat/usage/security/export needs before choosing a free tier. Budget estimates exclude infrastructure, wages/taxes, insurance, professional review and other stated costs. No accounts or purchases have been made.

Automation opportunities are designs only. Start with safe drafts, checks and owner tasks, and test idempotency, replay, missing events, cancellation and cross-client isolation. Do not enable unattended financial actions or send messages without approved bounded authority. Keep a human owner and a shutdown path.

## 12 First ten actions

1. Verify exact legal/tax identity and authorized signer facts.
2. Choose private record storage and password manager; approve access separately.
3. Select one realistic starter service and supported stack.
4. Fill a real cost model and approve provisional pricing/floor.
5. Resolve the contract decision register and send the polished drafts to chosen counsel when authorized.
6. Ask CPA/bookkeeper to map taxability, accounting, payroll and filing calendar.
7. Ask broker to confirm coverage and client contract fit.
8. Assign support/recovery targets only after staffing and restoration tests.
9. Walk one fictional client through lead, quote, contract, launch and exit to find friction.
10. Adopt reviewed versions, assign the monthly review and return to the system after each material change.

Source details and current qualifications are in the [compliance source register](compliance/OFFICIAL_SOURCE_REGISTER.md), legal research notes and each relevant policy. The source check date is 2026-10-13; verify rules, vendor terms and client facts again before acting.
