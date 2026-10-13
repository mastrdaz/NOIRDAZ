# Prompt for Mya - Build Noirdaz Standard Client/Hosting Forms

Work in:

https://github.com/mastrdaz/NOIRDAZ

## Mission

Build a complete first-draft legal/business document set for **Noirdaz Industries**, focused on:
- website builds
- managed website hosting
- maintenance/support
- custom software / workflow integrations
- payment/invoice integrations
- small-business clients

These are **attorney-review drafts**, not final legal advice. The goal is to get them to ~99% structurally complete so a lawyer can review/edit instead of drafting from scratch.

Do not invent Noirdaz legal identifiers, address, EIN, insurance limits, or state registrations. Use clear placeholders.

## Deliverables

Create editable Markdown source under:

`legal/templates/`

and a documentation index explaining when each form is used.

### 1. Master Services Agreement (MSA)
Include:
- parties
- definitions
- service relationship
- statements of work
- fees/invoicing/taxes
- client responsibilities
- third-party services
- access/credentials
- confidentiality
- data/privacy responsibilities
- security responsibilities
- intellectual property
- pre-existing IP
- custom deliverables
- open-source components
- client content
- warranties/disclaimers
- limitation of liability
- indemnification placeholders/alternatives for counsel
- force majeure
- compliance with law
- subcontractors
- term/termination
- suspension
- effect of termination
- data export/deletion/offboarding
- dispute/gov-law placeholders
- notices
- assignment
- entire agreement
- amendment
- severability
- electronic signatures

### 2. Statement of Work (SOW) template
Include fillable sections for:
- client
- project
- objective
- scope
- exclusions
- deliverables
- milestones
- acceptance criteria
- timeline
- dependencies
- client-supplied assets/access
- Noirdaz responsibilities
- client responsibilities
- pricing
- deposit
- recurring charges
- third-party costs
- change requests
- support after launch
- launch authorization
- signatures

### 3. Managed Hosting & Maintenance Addendum
Include:
- hosting scope
- domain/DNS responsibility
- SSL
- backups
- monitoring
- updates
- maintenance windows
- reasonable-use support
- excluded development work
- uptime language that does not overpromise
- security responsibilities
- third-party outages
- malware/incident handling
- restoration limits
- billing
- suspension
- termination
- transfer/offboarding
- data retention/deletion
- credential handoff

### 4. Software / Integration Addendum
For API/workflow/payment integrations.
Include:
- external systems/APIs
- sandbox/testing
- integration assumptions
- API/version changes
- client approvals
- production credentials
- change management
- logging
- data minimization
- webhook/event handling
- third-party failures
- rate limits
- maintenance
- acceptance testing
- incident response responsibilities

### 5. Payment Integration Security Addendum
Designed for cases like Wisconsin Surplus.
Principles:
- client should own merchant account
- processor handles card-entry surface when possible
- Noirdaz does not intentionally store PAN/CVV
- no promises of blanket PCI compliance
- define each party's responsibilities
- credential/secrets rules
- webhook validation
- logs
- refunds/disputes
- tax/surcharge decisions belong to client
- processor terms control processor behavior
- breach/incident contacts

### 6. Website Build Agreement / Small Project SOW
A lighter form for a basic website client who does not need the full custom-software paperwork.

### 7. Change Order Form
Short form with:
- requested change
- reason
- scope effect
- price effect
- timeline effect
- approvals

### 8. Project Acceptance / Launch Authorization
Client signs that:
- reviewed deliverables
- accepts known issues/exceptions
- authorizes production launch
- acknowledges recurring service start date

### 9. Support Request / Maintenance Policy
Client-facing description of:
- how to request help
- normal support
- emergencies
- response targets vs resolution guarantees
- billable enhancement work
- abuse/after-hours boundaries

### 10. Client Offboarding / Transfer Checklist
Include:
- cancellation date
- outstanding invoices
- domain
- DNS
- source/files
- databases
- credentials
- backups
- analytics
- email
- third-party accounts
- client data export
- deletion date
- confirmation/signoff

### 11. Confidentiality / Mutual NDA template
Keep it balanced and suitable for discovery before an MSA.

### 12. Data Processing / Privacy Questionnaire
A practical intake form to establish:
- what data is handled
- where it originates
- sensitive categories
- retention
- third parties
- access roles
- backups
- incident contacts
- state/country concerns

### 13. Client Intake Form
Collect:
- legal/client name
- billing contact
- technical contact
- authorized approvers
- domain ownership
- existing provider
- project goals
- integrations
- access
- payment preference
- tax-exempt status if relevant
- support requirements

### 14. Internal Project Risk Checklist
Before accepting a project:
- regulated data?
- payment data?
- health data?
- minors?
- financial data?
- client-owned credentials?
- unusual uptime requirement?
- custom SLA?
- unknown third-party system?
- production access risk?
- legal review trigger?
- insurance trigger?

## Standardization

Use consistent variables/placeholders, such as:
- {{CLIENT_LEGAL_NAME}}
- {{NOIRDAZ_LEGAL_NAME}}
- {{PROJECT_NAME}}
- {{EFFECTIVE_DATE}}
- {{STATE}}
- {{SETUP_FEE}}
- {{MONTHLY_FEE}}
- {{PAYMENT_TERMS}}

Create:
- `legal/README.md`
- `legal/templates/PLACEHOLDER_REFERENCE.md`
- `legal/templates/ATTORNEY_REVIEW_CHECKLIST.md`

## Attorney review flags

In every template, clearly mark clauses that deserve counsel attention, especially:
- limitation of liability
- indemnification
- governing law
- privacy/data processing
- PCI/payment issues
- SLA/uptime
- IP ownership/license
- warranty language
- auto-renewal
- attorney fees
- consequential damages

Do not pretend these are final or legally approved.

## Other Noirdaz work to start in parallel

### A. Web-hosting service catalog
Create `services/hosting/` with:
- service tiers
- what is included
- what is excluded
- monthly maintenance model
- optional add-ons
- internal estimated cost
- recommended client price
- escalation rules

### B. Standard client onboarding workflow
From lead -> discovery -> quote -> SOW -> deposit -> access -> build -> client review -> launch approval -> recurring billing -> support.

### C. Sales pipeline definitions
Stages:
- Lead
- Contacted
- Discovery Scheduled
- Discovery Complete
- Demo/Proposal
- Negotiation
- Won
- Lost
- Onboarding
- Active Client

### D. Quote / proposal template
Create a reusable Noirdaz proposal template that is professional, concise, and not sales-hype heavy.

### E. Hosting operations checklist
- domain/DNS
- backups
- uptime monitoring
- SSL
- update cycle
- security headers
- dependency updates
- restoration test
- client contacts
- incident procedure
- offboarding

### F. Internal pricing model
Create a spreadsheet-friendly Markdown/CSV framework to calculate:
- founder development time
- third-party services
- hosting
- email
- monitoring
- support hours
- payment costs
- gross margin
- setup price
- recurring price
- pilot discount

## Working rules

- Inspect existing Noirdaz repo first.
- Preserve current planning.
- Do not deploy anything.
- Do not create paid accounts.
- Do not purchase anything.
- Do not make legal claims.
- Prefer complete, practical drafts over vague outlines.
- Use plain English where possible.
- Add comments/notes where counsel should make the final call.
- Commit logically in small groups.
- Finish with a summary of files created, assumptions, open decisions, and attorney-review hotspots.
