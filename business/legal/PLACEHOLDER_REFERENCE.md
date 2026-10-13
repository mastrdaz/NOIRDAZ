# Placeholder reference

DRAFT — ATTORNEY REVIEW — COMPLETION GUIDE

Prepared 2026-10-13. All fillable tokens use double brackets and uppercase snake case. This reference covers every token in the twelve templates and the optional clause library. It does not supply factual or commercial values.

## Completion rules

1. Create one value register for the actual client package. Reuse the same agreed value wherever a key repeats. A separately signed amendment may change a value only within its stated scope.
2. EFFECTIVE_DATE and signature fields are document-instance values. MSA_DATE always identifies the incorporated MSA, not the date of the current addendum. SOW_ID ties the package to its project order.
3. Replace schedule tokens with actual text or a specifically identified, attached immutable schedule. A link to a changing policy is not enough. Record its title, version and date in CONTRACT_ATTACHMENT_INDEX.
4. Required identity, signature, risk-allocation, scope and price fields cannot be completed with “TBD,” a guessed fact or an unexplained “N/A.” “None” is appropriate only when the absence is deliberate and consistent with the contract.
5. Use ISO dates where possible and include timezone for a clock time or cutoff. Specify business versus calendar days and elapsed versus staffed support hours. Use a consistent currency and verify arithmetic.
6. Keep legal risk selections with owner/counsel; verify service promises with operations/engineering; confirm tax treatment with the CPA and insurance statements with the broker.
7. Never put credentials, account numbers, card data or live sensitive examples into placeholders. Name the approved secure system without copying its contents.
8. In the final client copy, no unresolved double-bracket token may remain. Signature fields become real signing fields. The questionnaire may record an explicit unknown with an owner/date, but processing must stay blocked if that unknown affects readiness.

## Core relationship fields

The base keys are PROVIDER_LEGAL_NAME, PROVIDER_ENTITY_TYPE, PROVIDER_ADDRESS, PROVIDER_NOTICE_EMAIL, CLIENT_LEGAL_NAME, CLIENT_ENTITY_TYPE, CLIENT_ADDRESS, CLIENT_NOTICE_EMAIL, EFFECTIVE_DATE, MSA_DATE, SOW_ID, PROJECT_NAME, GOVERNING_STATE and VENUE_COUNTY_STATE. Do not create competing aliases for these concepts. Provider and Client remain role names even if a future template is used for a different brand.

## Complete alphabetical field index

Each entry gives the expected content and where the token appears. “Clause library” entries are needed only when that optional clause is selected and integrated.

### ACCEPTANCE_CRITERIA

Objective tests, pass conditions, supported environment and evidence for each deliverable.

Used in: Acceptance and launch, Software, SOW, Website.

### ACCEPTANCE_CURE_PROCESS

Correction deadline/method, repeat-testing process and failed-cure threshold.

Used in: MSA.

### ACCEPTANCE_DECISION

Exactly accepted, accepted subject to punch list, or rejected with material nonconformities.

Used in: Acceptance and launch.

### ACCEPTANCE_EVIDENCE

Test results, expected outcomes and evidence references for acceptance.

Used in: Acceptance and launch.

### ACCEPTANCE_INVOICE_EFFECT

Existing milestone triggered by the decision, or None; do not invent a new fee.

Used in: Acceptance and launch.

### ACCEPTANCE_PUNCH_LIST

Remaining items, severity, owner, due dates and retest evidence; or None.

Used in: Acceptance and launch.

### ACCEPTANCE_REVIEW_DAYS

Approved business-day review window after complete delivery.

Used in: MSA.

### ACCESSIBILITY_SPECIFICATION

Technical standard/version/level, test scope, manual checks, exclusions and evidence.

Used in: Website.

### ACCESS_REVOCATION_PLAN

Provider/subcontractor access to remove, timing, remaining transition rights and client rotation duties.

Used in: Offboarding.

### ACCOUNT_AND_DOMAIN_TRANSFER_PLAN

Registrant/account changes, DNS/email/certificate actions, permissions and third-party restrictions.

Used in: Offboarding.

### ACQUIRER_OR_COMPLIANCE_CONTACT

Merchant bank or validation-accepting entity and verified compliance contact.

Used in: Payment.

### ADDITIONAL_EXIT_WORK

Separately ordered migration, conversion, training or transition labor; or None.

Used in: Offboarding, Clause library.

### ADDITIONAL_INDEMNITY_CATEGORIES

Specific additional covered third-party claims, responsible party, exclusions and cap allocation; or approved None.

Used in: MSA.

### AFTER_HOURS_COVERAGE

Exact purchased after-hours staffing/availability or explicit None.

Used in: Support.

### AI_DATA_USE_ASSESSMENT

Proposed AI provider, data, purpose, retention/training behavior and required specific approval.

Used in: Questionnaire.

### API_DEPENDENCY_REGISTER

API vendors/versions, quotas, permissions, licenses, change contacts and known support deadlines.

Used in: Software.

### APPROVED_PUBLICITY_CHANNELS

Specific approved portfolio/marketing channels and scope.

Used in: Clause library.

### APPROVED_PUBLICITY_MATERIALS

Exact client-approved assets and factual description, excluding confidential details.

Used in: Clause library.

### APPROVED_RATE_SCHEDULE

Approved currency, roles, units, rates, minimum increments and applicable hours.

Used in: Change, SOW, Support, Website.

### ASSIGNED_DELIVERABLES

Precisely identified custom items assigned after their allocated payment.

Used in: SOW, Website.

### ASSURANCE_REQUIREMENTS

Required audits, certifications, insurance or questionnaires and whose actual status they describe.

Used in: Questionnaire.

### AUTHORIZED_LAUNCH_ACTIONS

Exact permitted production changes; exclude unrelated DNS, charges and communications.

Used in: Acceptance and launch.

### AUTHORIZED_SUPPORT_CONTACTS

Named requesters, their permitted requests and identity-verification basis.

Used in: Support.

### AUTHORIZED_TRANSFER_RECIPIENTS

Verified receiving organization/people and exactly what each may receive.

Used in: Offboarding.

### BACKGROUND_MATERIALS

Provider-owned reusable/pre-existing items, versions and embedded use.

Used in: SOW, Website.

### BACKUP_EXPIRATION_SCHEDULE

Actual backup retention/rotation and latest ordinary expiration, with legal-hold treatment.

Used in: Offboarding, Clause library.

### BACKUP_SERVICE_SPECIFICATION

Datasets, frequency, retention, location, encryption, access, exclusions and responsible party.

Used in: Hosting.

### BACKUP_VERIFICATION_SCHEDULE

Job verification and restore-test frequency, evidence, failure escalation and owners.

Used in: Hosting.

### BILLING_AND_CONSENT_SPECIFICATION

Approved customer pricing, descriptors, taxes, recurring consent, notices, refunds and cancellation behavior.

Used in: Payment.

### BREACH_CURE_DAYS

Approved calendar days after material-breach notice to cure.

Used in: MSA.

### CANCELLATION_METHOD

Clear permitted channel and recipient plus receipt evidence and any mandatory-law requirements.

Used in: Clause library.

### CAPACITY_NOTICE_PROCESS

Forecast/threshold notices, responsible contact and action before exhaustion.

Used in: Hosting.

### CHANGED_CONTRACT_SECTIONS

Exact provisions/attachments changed, with replacement version references.

Used in: Change, Offboarding.

### CHANGED_REQUIREMENT

Complete replacement/additional requirement.

Used in: Change.

### CHANGE_ACCEPTANCE_CRITERIA

New/replacement tests and preserved tests for changed work.

Used in: Change.

### CHANGE_BUDGET_LIMIT

Additional not-to-exceed time/expense authority for this change.

Used in: Change.

### CHANGE_DATA_AND_SECURITY_IMPACT

Changed data, access, vendors, locations, retention and required approvals.

Used in: Change.

### CHANGE_DELIVERABLES

Added/changed outputs, owner and boundaries.

Used in: Change.

### CHANGE_DELIVERY_FORMAT

Files, repository, interface or other delivery format.

Used in: Change.

### CHANGE_DEPENDENCIES

New or changed inputs/approvals with owners and dates.

Used in: Change.

### CHANGE_FEE_DELTA

Signed positive/negative fee effect of this change; specify currency.

Used in: Change.

### CHANGE_INVOICE_SCHEDULE

New invoice/credit amounts, events and deadlines.

Used in: Change.

### CHANGE_IP_ALLOCATION

Ownership classification and fee allocation for added/changed deliverables.

Used in: Change.

### CHANGE_OPERATIONAL_IMPACT

Hosting, support, backup, monitoring and recurring-service effects.

Used in: Change.

### CHANGE_ORDER_ID

Unique sequential change ID tied to the SOW.

Used in: Change.

### CHANGE_PAUSE_SCOPE

Affected work that pauses pending approval and the restart condition.

Used in: Change.

### CHANGE_REASON

Business or technical reason for the change without adding unapproved scope.

Used in: Change.

### CLAIM_AGGREGATION_RULE

How related events and multiple claims aggregate; include post-termination and multiple-SOW treatment.

Used in: MSA, Clause library.

### CLIENT_ADDRESS

Client's verified legal notice address.

Used in: MSA, NDA.

### CLIENT_DEPENDENCIES

Client inputs, access, licenses and approvals, each with owner and due date.

Used in: Software, SOW, Website.

### CLIENT_ENTITY_TYPE

Verified client legal form and relevant jurisdiction.

Used in: MSA, NDA.

### CLIENT_HOSTING_RESPONSIBILITIES

Component-level client ownership, coordination and dependencies.

Used in: Hosting.

### CLIENT_LEGAL_NAME

Exact client entity or individual's legal name; distinguish affiliates and DBAs.

Used in: Acceptance and launch, Change, Hosting, MSA, NDA, Offboarding, Payment, Questionnaire, Software, SOW, Support, Website.

### CLIENT_NOTICE_EMAIL

Client's authorized monitored formal-notice address.

Used in: MSA, NDA.

### CLIENT_PRIVACY_AND_SECURITY_CONTACTS

Named client privacy/security/commercial owners and verified business channels.

Used in: Questionnaire.

### CLIENT_PROJECT_CONTACT

Named day-to-day client contact and business channel.

Used in: SOW, Website.

### CLIENT_RELEASE_APPROVER

Named client individual authorized for this release decision.

Used in: Acceptance and launch.

### CLIENT_REVIEW_REPRESENTATIVE

Name and authority of the client reviewer.

Used in: Acceptance and launch.

### CLIENT_SECURITY_CONTACT

Verified incident recipient and backup contact with secure contact details.

Used in: MSA.

### CLIENT_SIGNATORY_NAME

Full name of the verified authorized client representative.

Used in: Acceptance and launch, Change, Hosting, MSA, NDA, Offboarding, Payment, Software, SOW, Support, Website.

### CLIENT_SIGNATORY_TITLE

Verified title or signing capacity for the client party.

Used in: Acceptance and launch, Change, Hosting, MSA, NDA, Offboarding, Payment, Software, SOW, Support, Website.

### CLIENT_SIGNATURE

Actual authorized signature or e-signature field; never prefill a signature.

Used in: Acceptance and launch, Change, Hosting, MSA, NDA, Offboarding, Payment, Software, SOW, Support, Website.

### CLIENT_SIGNATURE_DATE

Date the client representative actually signs this document.

Used in: Acceptance and launch, Change, Hosting, MSA, NDA, Offboarding, Payment, Software, SOW, Support, Website.

### COMMERCIAL_APPROVERS

Named authorized scope/fee approvers for both parties and any limits on their authority.

Used in: SOW, Website.

### CONFIDENTIALITY_YEARS

Approved survival years, with the separate trade-secret and retained-data rules preserved.

Used in: MSA, NDA.

### CONSEQUENTIAL_ACTION_CONTROLS

Human authorization, spending/action limits, exception handling and audit evidence for consequential workflows.

Used in: Software.

### CONTINUING_SERVICES

Specific retained services, term and authorized charges; or None.

Used in: Offboarding.

### CONTRACT_ATTACHMENT_INDEX

All incorporated schedules/exhibits with immutable titles, versions, dates and locations.

Used in: SOW, Website.

### CONVENIENCE_TERMINATION_TERMS

Which party may terminate without cause, notice, fees, mitigation and refund rules; or expressly unavailable.

Used in: MSA, SOW, Website.

### CURRENCY

ISO currency code for the order; apply consistently to fees, limits and reconciliation.

Used in: Change, Offboarding, SOW, Website.

### CURRENT_REQUIREMENT

Exact current requirement being replaced or supplemented.

Used in: Change.

### DAMAGES_EXCLUSION_EXCEPTIONS

Preserved claim/loss categories and treatment of direct restoration, incident costs, third-party awards and fees.

Used in: MSA, Clause library.

### DATA_ASSISTANCE_AND_REVIEW_PROCESS

Rights-request and regulator assistance, evidence/audit boundaries, frequency, notice and approved cost allocation.

Used in: MSA.

### DATA_BUSINESS_CONTEXT

Industry, service, purpose and categories of affected people.

Used in: Questionnaire.

### DATA_INVENTORY

Dataset/category, source, subjects, purpose, fields, volume, sensitivity, owner, recipients and retention.

Used in: Questionnaire.

### DATA_LOCATION_MAP

People, business, hosting, backup and support/admin access locations; unresolved restrictions.

Used in: Questionnaire.

### DATA_MAPPING_AND_SYNC_RULES

Field maps, direction, frequency, system of record, conflicts, expected volume and tolerable delay.

Used in: Software.

### DATA_OPEN_ISSUES

Unresolved facts/risks, owner, due date and processing block if applicable.

Used in: Questionnaire.

### DATA_PROCESSING_SCHEDULE

Attached verified purpose, categories, subjects, operations, locations, vendors, safeguards and retention instructions.

Used in: MSA, Software, SOW, Website.

### DATA_READINESS_APPROVALS

Specific prerequisites and named approvers; no new processing authorization implied.

Used in: Questionnaire.

### DATA_READINESS_DECISION

Ready for stated data only, ready subject to listed prerequisites, or not ready.

Used in: Questionnaire.

### DATA_REQUEST_WORKFLOW

Owners and steps for access/correction/deletion/portability/legal-hold/regulator requests.

Used in: Questionnaire.

### DATA_REQUIREMENT_REGISTER

Known legal/sector/contract requirements, source, applicability reviewer and status.

Used in: Questionnaire.

### DATA_RETENTION_SCHEDULE

Record categories, purposes, legal bases, production/backup periods, deletion and hold review.

Used in: Questionnaire.

### DATA_ROLE_ASSESSMENT

Facts supporting controller/processor or other roles; identify counsel-verification needs.

Used in: Questionnaire.

### DEFENSE_COST_CAP_TREATMENT

Whether defense expenses count toward each cap and when cap exhaustion ends or affects defense.

Used in: MSA, Clause library.

### DELETION_CONFIRMATION_METHOD

Who verifies which deletions, evidence and statement distinguishing future backup expiry.

Used in: Offboarding.

### DELIVERABLE_SCHEDULE

Item IDs, descriptions, formats, owner, milestone, acceptance tests and allocated fees.

Used in: SOW, Website.

### DELIVERY_DESTINATION

Verified repository, account or secure destination for deliverables, with recipient access.

Used in: SOW, Website.

### DEPOSIT_TERMS

Amount, due event, application to fees and approved refund/cancellation treatment.

Used in: SOW, Website.

### DESIGN_APPROVAL_SCHEDULE

Design checkpoints, deliverables, reviewer and due dates.

Used in: Website.

### DESIGN_REVIEW_ALLOWANCE

Included concepts and revision rounds; distinguish defect correction from new design requests.

Used in: Website.

### DISPUTE_ESCALATION_DAYS

Approved calendar days for commercial escalation without impairing urgent relief or deadlines.

Used in: MSA.

### DOMAIN_CONTROL_RECORD

Registrant, registrar, domain, payer, renewal date, admin/recovery owner and transfer contacts; no secrets.

Used in: Hosting, Website.

### DOWNSTREAM_SCHEDULE_EFFECTS

Specific effects on otherwise unchanged deliveries, or None.

Used in: Change.

### EFFECTIVE_DATE

Effective date of this particular document, not automatically the signature date.

Used in: Acceptance and launch, Change, Hosting, MSA, NDA, Offboarding, Payment, Questionnaire, Software, SOW, Support, Website.

### ELEVATED_LIABILITY_CAPS

Each elevated claim category and its exact cap; or an explicit approved None.

Used in: MSA, Clause library.

### EMERGENCY_SUPPORT_CHANNEL

Purchased emergency channel or explicit None; do not imply coverage.

Used in: Support.

### END_OF_SUPPORT_NOTICE

Minimum advance notice, channel, supported-version end date and transition options.

Used in: Software, Support.

### EXCLUDED_SERVICES

Explicit exclusions such as unpurchased hosting, ongoing updates or extra integrations.

Used in: SOW, Website.

### EXIT_AND_RETENTION_SCHEDULE

Included export, formats, window, migration responsibilities, fees, production deletion, backup expiry and legal holds.

Used in: Hosting, MSA, Software, SOW, Website, Clause library.

### EXIT_DELIVERABLES

Detailed export/configuration/source/domain/license/data handoff inventory.

Used in: Offboarding.

### EXIT_WORK_FEES

Approved incremental price or ceiling, currency, units and invoice terms; or None.

Used in: Offboarding, Clause library.

### EXPORT_WINDOW_END

Final agreed export-availability date/time with timezone.

Used in: Offboarding.

### FINAL_ACCOUNT_RECONCILIATION

Earned fees, approved commitments, paid amounts, deposits, credits/refunds and separated disputes.

Used in: Offboarding.

### FINAL_PAYMENT_AND_REFUND_DATES

Definite due dates and methods for final undisputed payment/refund.

Used in: Offboarding.

### FORCE_MAJEURE_TERMINATION_DAYS

Approved duration of qualifying disruption allowing affected-service termination.

Used in: MSA.

### GENERAL_LIABILITY_CAP

Complete amount/formula, currency, fee base, measurement period and SOW aggregation scope.

Used in: MSA, Clause library.

### GOVERNING_STATE

Counsel-approved state/jurisdiction; also used to define business holidays in the MSA.

Used in: MSA, NDA.

### HANDOVER_DELIVERABLES

Specific source, files, build/deploy instructions, exports, documentation and training included.

Used in: Software, SOW, Website.

### HOSTING_CAPACITY

Compute, storage, traffic, database and other resource limits and measurement.

Used in: Hosting.

### HOSTING_INVENTORY

Applications, domains, tenant/environment identifiers and included infrastructure.

Used in: Hosting.

### HOSTING_VENDOR_AND_LOCATION

Vendor, service, region, legal/account owner and billing owner.

Used in: Hosting, Website.

### INCIDENT_NOTIFICATION_ASSESSMENT

All relevant notice recipients/deadlines, triggers, escalation and counsel review.

Used in: Questionnaire.

### INCIDENT_NOTIFICATION_DEADLINE

Outside provider-to-client reporting deadline measured from awareness, with earlier mandatory law preserved.

Used in: MSA.

### INCLUDED_EXIT_EXPORT

Ordinary export already included in agreed fees, with formats and boundary.

Used in: Offboarding, Clause library.

### INCORPORATED_ADDENDA

Exact titles, dates and versions of the service addenda actually included.

Used in: SOW, Website.

### INSURANCE_REQUIREMENTS

Agreed policies, types, limits, duration, endorsements and evidence supported by actual coverage.

Used in: MSA.

### INTEGRATION_ARCHITECTURE

Connected systems, authoritative sources, accounts, environments, data flow and supported versions.

Used in: Software.

### INTEGRATION_CONTROL_SPECIFICATION

Validation, authorization, idempotency, retry, queue, reconciliation, logging and failure controls.

Used in: Software.

### INTEGRATION_SPECIFICATION

Endpoints/functions, operations, mappings and explicit integration boundary.

Used in: Software.

### INTEGRATION_TEST_PLAN

Normal/failure cases, synthetic data, expected results, evidence and accountable tester.

Used in: Software.

### INVOICE_DISPUTE_DAYS

Approved number of calendar days after invoice receipt for identifying a dispute.

Used in: MSA.

### INVOICE_SCHEDULE

Milestones, amounts, dates/events, delivery recipient and payment due periods.

Used in: SOW, Website.

### IP_TERMINATION_REFUND_FORMULA

Refund calculation for discontinued infringing items, fee base and retained-use treatment.

Used in: MSA.

### LABOR_BUDGET_LIMIT

Authorized not-to-exceed amount and period for time-based labor; exclude unapproved expansion.

Used in: SOW.

### LATE_CHARGE_TERMS

Counsel-approved rate, calculation, grace period and costs/surcharges, or None; never a guessed legal maximum.

Used in: MSA.

### LAUNCH_DECISION

Exactly Authorized or Not authorized, separately from acceptance.

Used in: Acceptance and launch.

### LAUNCH_DESTINATION

Verified production environment/domain/account.

Used in: Acceptance and launch.

### LAUNCH_EXCEPTIONS

Specific unresolved readiness issues, effect and named approval; or None.

Used in: Acceptance and launch.

### LAUNCH_PLAN

Version, environment, prerequisites, change window, approvers, backup, rollback and verification.

Used in: Change, Payment, Software, SOW, Website.

### LAUNCH_READINESS_EVIDENCE

Completed prerequisite checks and links/references without secrets.

Used in: Acceptance and launch.

### LAUNCH_WINDOW

Approved start/end date and time, with timezone.

Used in: Acceptance and launch.

### MAINTENANCE_SPECIFICATION

Window/timezone, notice, patch priorities, owners and emergency procedure.

Used in: Hosting.

### MERCHANT_OF_RECORD

Exact legal party selling to customers and responsible for merchant obligations.

Used in: Payment.

### MONITORING_SPECIFICATION

Endpoints, metrics, intervals, thresholds, alerts and monitoring owner.

Used in: Hosting.

### MONTHLY_CANCELLATION_NOTICE_DAYS

Counsel-approved calendar-day notice for the optional monthly model.

Used in: Clause library.

### MONTHLY_END_DATE_RULE

Exact method for determining cutoff after notice, without hidden extra periods.

Used in: Clause library.

### MONTHLY_PRORATION_RULE

Approved partial-period fee/refund calculation.

Used in: Clause library.

### MSA_DATE

Effective date of the exact executed MSA incorporated by this order.

Used in: Acceptance and launch, Change, Hosting, Offboarding, Payment, Software, SOW, Support, Website.

### MSA_SPECIFIC_AMENDMENTS

Exact MSA section, express override and full changed text; or None.

Used in: SOW, Website.

### MSA_TERMINATION_NOTICE_DAYS

Approved calendar days to terminate the MSA when no SOW is active.

Used in: MSA.

### NDA_BACKUP_EXPIRATION

Actual backup rotation/expiration process and timing for NDA copies.

Used in: NDA.

### NDA_DISCLOSURE_END_DATE

End of permitted disclosure period, separate from survival of protection.

Used in: NDA.

### NDA_DISCUSSION_CONFIDENTIALITY

Whether existence/status of discussions are protected; identify precise scope or None.

Used in: NDA.

### NDA_PRIOR_DISCLOSURES

Specifically described earlier disclosures and dates, or None.

Used in: NDA.

### NDA_PURPOSE

Specific evaluation/discussion purpose for allowed confidential-information use.

Used in: NDA.

### NDA_RETURN_DAYS

Approved calendar days after request to return/delete, subject to stated retained-record rules.

Used in: NDA.

### NDA_RISK_ALLOCATION

Complete independent NDA cap/exclusion/remedy allocation; expressly identify any incorporated MSA terms.

Used in: NDA.

### NONPORTABLE_ITEMS

Licenses/tokens/accounts that cannot transfer and approved replacement path; or None.

Used in: Offboarding.

### NONRENEWAL_DEADLINE_RULE

Clear deadline formula/date to prevent automatic renewal, reviewed for applicable law.

Used in: Clause library.

### NOTICE_AND_CONSENT_RESPONSIBILITIES

Owner and evidence for privacy notices, lawful collection, cookies, consent and rights channels.

Used in: Questionnaire.

### ORIGINAL_AUTHORIZED_TOTAL

Initial approved project total before changes, in the order currency.

Used in: Change.

### ORIGINAL_MILESTONE

Original affected milestone identifier and date.

Used in: Change.

### ORIGINAL_RECURRING_FEE

Recurring amount/frequency immediately before this change.

Used in: Change.

### OUTAGE_COMMUNICATION_PROCESS

Recipient/channel, cadence, sender authority, updates and customer/public-statement approval.

Used in: Hosting, Support.

### OVERLAPPING_CAP_RULE

Which cap applies to overlapping categories and whether any caps stack.

Used in: MSA, Clause library.

### PAYMENT_ACTION_AUTHORITY

Who may view, charge, refund, cancel or change settings; per-action approvals and scope limits.

Used in: Payment.

### PAYMENT_CONTROL_SPECIFICATION

Webhook verification, idempotency, amount/currency validation, safe logs and transaction controls.

Used in: Payment.

### PAYMENT_CURE_DAYS

Approved calendar-day notice period before suspension for undisputed nonpayment.

Used in: MSA.

### PAYMENT_DATA_FLOW

Browser/scripts/iframes/redirects, endpoints, tokens, webhooks, logs and storage mapped end to end.

Used in: Payment.

### PAYMENT_INTEGRATION_SCOPE

Specific checkout/invoice/subscription/refund integration features being developed, not financial-action authority.

Used in: Payment.

### PAYMENT_LAUNCH_APPROVERS

Named client/provider approvers for payment configuration and live activation.

Used in: Payment.

### PAYMENT_METADATA_ALLOWLIST

Minimum non-credential transaction/token fields permitted in the service and logs.

Used in: Payment.

### PAYMENT_PROCESSOR

Verified processor and merchant-account reference without secrets.

Used in: Payment.

### PAYMENT_RECONCILIATION_PROCESS

Authoritative transaction source, cadence, matching, exception ownership and dispute escalation.

Used in: Payment.

### PAYMENT_TEST_PLAN

Synthetic test cases, evidence and separate live-test approval requirements.

Used in: Payment.

### PCI_RESPONSIBILITY_MATRIX

Merchant/provider/processor owners for applicable validation, evidence, scanning, script controls and incidents.

Used in: Payment.

### PERMITTED_ASSIGNMENT_TERMS

Approved assignment exceptions, conditions and responsibility of successors, or None.

Used in: MSA.

### POST_LAUNCH_CHECKS

Checks, evidence, owners and timing after deployment, including payment reconciliation if applicable.

Used in: Acceptance and launch, Website.

### PREAUTHORIZED_SUPPORT_ACTIONS

Specific routine tasks allowed within purchased scope; destructive/financial exceptions remain excluded.

Used in: Support.

### PRICING_BASIS

Fixed fee, time and materials, milestone or explicitly defined combination.

Used in: SOW.

### PRIOR_APPROVED_CHANGES_TOTAL

Net signed changes before this order, not unsigned requests.

Used in: Change.

### PRIVACY_QUESTIONNAIRE_REFERENCE

Completed questionnaire identifier, version, date and responsible reviewer.

Used in: SOW.

### PRODUCTION_DELETION_DATE

Scheduled production deletion date, with any category-specific exceptions identified.

Used in: Offboarding.

### PRODUCT_LICENSE_ATTACHMENT

Exact executed product/license attachment and version, or None if no licensed product is included.

Used in: SOW, Clause library.

### PROJECT_ASSUMPTIONS

Facts on which scope, price and schedule depend and how they will be verified.

Used in: SOW.

### PROJECT_COMMUNICATION_CHANNELS

Approved routine instruction channels; keep formal-notice rules distinct.

Used in: SOW.

### PROJECT_FEES

Approved project/setup amounts and deliverable-level allocations; separate taxes and external expenses.

Used in: SOW, Website.

### PROJECT_MILESTONES

Deliverable dates, dependencies and whether each deadline is binding or estimated.

Used in: SOW, Website.

### PROJECT_NAME

Human-readable project name matching the approved order.

Used in: Acceptance and launch, Change, Hosting, Offboarding, Payment, Questionnaire, Software, SOW, Support, Website.

### PROJECT_PURPOSE

Business objective used to interpret scope, without creating an outcome guarantee.

Used in: SOW.

### PROJECT_START_DATE

Agreed start date, qualified by explicitly identified start conditions.

Used in: SOW, Website.

### PROVIDER_ADDRESS

Verified legal notice street address, locality, region and postal code.

Used in: MSA, NDA.

### PROVIDER_DEPENDENCIES

Provider inputs and readiness tasks, each with owner and due date.

Used in: SOW.

### PROVIDER_ENTITY_TYPE

Verified legal form and formation jurisdiction; do not assume LLC status.

Used in: MSA, NDA.

### PROVIDER_HOSTING_RESPONSIBILITIES

Component-level provider ownership of management, patches, certificates, backups and monitoring.

Used in: Hosting.

### PROVIDER_LEGAL_NAME

Exact legal contracting party; verify records, not branding.

Used in: Acceptance and launch, Change, Hosting, MSA, NDA, Offboarding, Payment, Questionnaire, Software, SOW, Support, Website.

### PROVIDER_NOTICE_EMAIL

Monitored address authorized to receive formal notices.

Used in: MSA, NDA.

### PROVIDER_PRIVACY_AND_SECURITY_CONTACTS

Named provider privacy/security/commercial owners and escalation channels.

Used in: Questionnaire.

### PROVIDER_PROJECT_CONTACT

Named day-to-day provider contact and business channel.

Used in: SOW.

### PROVIDER_RELEASE_APPROVER

Named provider individual authorized for this release decision.

Used in: Acceptance and launch.

### PROVIDER_SIGNATORY_NAME

Full name of the verified authorized provider representative.

Used in: Acceptance and launch, Change, Hosting, MSA, NDA, Offboarding, Payment, Software, SOW, Support, Website.

### PROVIDER_SIGNATORY_TITLE

Verified title or signing capacity for the provider party.

Used in: Acceptance and launch, Change, Hosting, MSA, NDA, Offboarding, Payment, Software, SOW, Support, Website.

### PROVIDER_SIGNATURE

Actual authorized signature or e-signature field; never prefill a signature.

Used in: Acceptance and launch, Change, Hosting, MSA, NDA, Offboarding, Payment, Software, SOW, Support, Website.

### PROVIDER_SIGNATURE_DATE

Date the provider representative actually signs this document.

Used in: Acceptance and launch, Change, Hosting, MSA, NDA, Offboarding, Payment, Software, SOW, Support, Website.

### PUBLICITY_REMOVAL_DAYS

Approved calendar-day removal period after withdrawal for controlled channels.

Used in: Clause library.

### PUBLICITY_START_DATE

Earliest approved publication date.

Used in: Clause library.

### QUESTIONNAIRE_PREPARED_DATE

Actual completion date for factual answers.

Used in: Questionnaire.

### QUESTIONNAIRE_PREPARER_NAME

Actual preparer's full name.

Used in: Questionnaire.

### QUESTIONNAIRE_PREPARER_ROLE

Actual preparer's role and organization.

Used in: Questionnaire.

### QUESTIONNAIRE_REVIEWER_NAME

Named factual/security/legal reviewer with role specified if relevant.

Used in: Questionnaire.

### QUESTIONNAIRE_REVIEW_DATE

Actual review date; not a certification date unless separately justified.

Used in: Questionnaire.

### RECOVERY_OBJECTIVES

RPO/RTO, covered systems and explicit target versus binding-commitment status.

Used in: Hosting.

### RECURRING_FEES

Amount, interval, included usage, taxes and the separate authorized start event.

Used in: SOW.

### RECURRING_FEE_CHANGE_DATE

Approved effective date/event for a recurring price change.

Used in: Change.

### RECURRING_SERVICE_START_EVENT

Objective signed event/date that starts purchased recurring service and billing.

Used in: Acceptance and launch, SOW, Website, Clause library.

### REFUND_AND_CREDIT_TIMING

Definite deadline, method and invoice-credit versus cash-refund treatment.

Used in: MSA.

### RELEASE_IDENTIFICATION

Immutable artifact/release tag and deliverables presented for acceptance.

Used in: Acceptance and launch.

### REMOVED_SCOPE

Specific canceled work and effect on prior deliverables; or None.

Used in: Change.

### RENEWAL_NOTICE_PROCESS

Statutory/contract reminder timing, content, delivery method and evidence.

Used in: Clause library.

### RENEWAL_PERIOD

Exact additional term and any restrictions, with required disclosures.

Used in: Clause library.

### RENEWAL_PRICE_CHANGE_PROCESS

Notice, effective date, cancellation opportunity and authorization required for new prices.

Used in: Clause library.

### RENEWAL_PRICE_TERMS

Renewal amount/formula and permitted changes, not an unrestricted future list price.

Used in: Clause library.

### RENEWAL_TERMS

Selected term model, renewal/cancellation mechanism, dates, prices and required notices; no inference from invoicing.

Used in: SOW.

### REQUIRED_DATA_AGREEMENTS

Needed DPA/BAA/transfer/sector instruments, owner, signature status and processing gate.

Used in: Questionnaire.

### RESPONSE_TARGET_SCHEDULE

Priority targets, business/elapsed clocks, start/pause/stop rules; distinct from resolution promises.

Used in: Support.

### RESTORE_AUTHORIZATION_AND_FEES

Approver, restoration tests, included effort, cost ceiling and destructive-change authorization.

Used in: Hosting.

### RESTRICTED_DATA_SCREENING

Yes/no/unknown answers by sensitive category, limits and required specialist review.

Used in: Questionnaire.

### RETAINED_RECORD_EXCEPTIONS

Necessary record categories, legal basis, custodian, scope, review and eventual deletion.

Used in: Offboarding.

### REVIEW_DATE

Actual date of the identified client review.

Used in: Acceptance and launch.

### REVIEW_ESCALATION_DAYS

Business days after a final acceptance reminder before commercial escalation.

Used in: Clause library.

### REVIEW_LOCATION

Verified test/review environment accessible to the authorized reviewer.

Used in: Acceptance and launch.

### REVISED_AUTHORIZED_TOTAL

Original total plus prior changes plus this delta, verified arithmetically.

Used in: Change.

### REVISED_MILESTONES

Replacement milestone dates and dependencies.

Used in: Change.

### REVISED_RECURRING_FEE

New authorized amount/frequency, or unchanged/no recurring fee.

Used in: Change.

### ROLLBACK_PLAN

Triggers, authority, artifacts, recovery procedure and decision/communication timing.

Used in: Acceptance and launch.

### SECURE_ACCESS_METHOD

Approved vault or secure transfer system and access process; reference only, never actual credentials.

Used in: Hosting, Payment, Software.

### SECURITY_CONTROL_ASSESSMENT

Implemented/planned/not-applicable/unknown status, owner, dates and evidence for each requested control.

Used in: Questionnaire.

### SECURITY_GAP_REGISTER

Known gap, risk, mitigation, owner, date and authorized readiness decision.

Used in: Questionnaire.

### SECURITY_REPORTING_CHANNEL

Actual secure incident intake channel and escalation fallback.

Used in: Support.

### SERVICE_BOUNDARIES

Permitted environments, users, locations, workloads, quantities and use cases.

Used in: SOW.

### SERVICE_DESCRIPTION

Specific services ordered, sufficient to distinguish included work from exclusions.

Used in: SOW.

### SERVICE_END_DATE

Definite expiration date or precisely defined ending event consistent with renewal terms.

Used in: SOW, Clause library.

### SERVICE_TERMINATION_DATE_AND_TIME

Actual agreed cutoff date/time/timezone for the identified service.

Used in: Offboarding.

### SLA_CREDIT_CEILING

Maximum approved credit per period and currency/percentage basis.

Used in: Clause library.

### SLA_CREDIT_FORMULA

Covered-service fee base, measured failure bands and credit calculation.

Used in: Clause library.

### SLA_EXHIBIT_REFERENCE

Exact signed SLA and version; or None for no purchased contractual SLA.

Used in: Hosting, SOW, Support, Clause library.

### SLA_REPEATED_FAILURE_REMEDY

Defined repeated-failure trigger, termination opportunity and financial adjustment.

Used in: Clause library.

### SOFTWARE_MAINTENANCE_SCOPE

Versions, dependencies, patch work, warranty boundary and explicitly included adaptation work.

Used in: Software.

### SOW_ID

Unique order identifier shared across its addenda and later forms.

Used in: Acceptance and launch, Change, Hosting, Offboarding, Payment, Questionnaire, Software, SOW, Support, Website.

### START_CONDITIONS

Executed documents, authorized payment setup/deposit and specific readiness conditions.

Used in: SOW, Website.

### SUBPROCESSOR_CHANGE_PROCESS

Notice/approval model, objection grounds/window, alternatives, urgent changes and affected-service exit.

Used in: MSA.

### SUBPROCESSOR_NOTICE_DAYS

Approved advance notice for a new subprocessor; reconcile upstream change capability.

Used in: Clause library.

### SUBPROCESSOR_OBJECTION_DAYS

Approved objection period and when it starts, with required-law protections.

Used in: Clause library.

### SUBPROCESSOR_REGISTER

Vendor legal name, role, data, locations, account owner, contract, deletion and security evidence.

Used in: Questionnaire.

### SUBSCRIPTION_PRODUCTS

Product names and versions remaining licensed/hosted services rather than assigned work.

Used in: SOW, Clause library.

### SUPPORTED_ENVIRONMENTS

Browsers/devices/platforms, versions, configuration and applicable test boundaries.

Used in: SOW, Website.

### SUPPORT_ALLOWANCE

Units, quantity, billing period, measurement and rollover/expiration treatment.

Used in: Support.

### SUPPORT_COVERAGE_HOURS

Staffed days/hours, timezone and excluded holidays; distinguish automated checks.

Used in: Hosting, Support.

### SUPPORT_ESCALATION_SCHEDULE

Roles/contacts and impact/time thresholds for escalation.

Used in: Support.

### SUPPORT_EXCLUSIONS

Specific systems/tasks/version ranges not purchased.

Used in: Support.

### SUPPORT_EXHIBIT_REFERENCE

Exact signed or incorporated support exhibit and version; or None.

Used in: SOW.

### SUPPORT_INTAKE_CHANNEL

Actual maintained ticket/email channel for routine requests.

Used in: Support.

### SUPPORT_OVERAGE_AUTHORIZATION

Approved additional support rates/ceiling and required approval process.

Used in: Support.

### SUPPORT_RECORD_RETENTION

Ticket/log categories, duration, access, deletion and hold review.

Used in: Support.

### SUPPORT_SCOPE

Purchased tasks, systems, supported versions and operational boundary.

Used in: SOW, Support.

### SUPPORT_TERM

Start/end dates or clear duration for the purchased support service.

Used in: SOW, Support.

### TERMINATING_SERVICES

Exact services/environments/orders ending; distinguish continuing items.

Used in: Offboarding.

### TERMINATION_NOTICE_REFERENCE

Original notice, sender/recipient, date and contract basis.

Used in: Offboarding.

### THIRD_PARTY_COMPONENTS

Vendor/open-source components, versions, licenses, notices and ongoing obligations; or None.

Used in: Change, SOW, Website.

### THIRD_PARTY_COST_AUTHORIZATION

Vendor/service, account owner, payer, amount/ceiling, recurrence, term, restrictions and disclosed markup; or None.

Used in: Change, Payment, SOW, Website.

### THIRD_PARTY_DATA_AUTHORITY

Source/account-holder permission and restrictions on receiving and using third-party records.

Used in: Questionnaire.

### TICKET_INACTIVITY_PROCESS

Reminder, client-response opportunity, administrative closure and reopening process.

Used in: Support.

### TRACKING_AND_FORM_INVENTORY

Approved form fields, analytics, cookies, pixels and consent configuration; or None.

Used in: Website.

### TRANSFER_CHECKLIST_RECORD

Each checklist item's status, owner, completion date, evidence and exception.

Used in: Offboarding.

### TRANSFER_COMPLETION_ACKNOWLEDGMENT

Limited acknowledgment of verified completed handoff tasks and outstanding exceptions.

Used in: Offboarding.

### TRANSFER_METHOD

Approved secure destination/channel, encryption and integrity-verification process; no secrets.

Used in: Offboarding.

### TRANSFER_SCHEDULE

Milestones, owners, cutoff, verification window and contingency.

Used in: Offboarding.

### TRANSITION_CONTACTS

Named provider/client owners and escalation details.

Used in: Offboarding.

### UNCAPPED_CLAIM_CATEGORIES

Precisely identified categories excluded from contractual caps, or approved None subject to mandatory law.

Used in: MSA, Clause library.

### USAGE_AND_OVERAGE_TERMS

Measured units, included capacity, notification thresholds, price and required approval before excess costs.

Used in: SOW.

### VENDOR_CANCELLATION_PLAN

Account owner, specifically authorized stop/cancellation action, date and evidence.

Used in: Offboarding.

### VENDOR_CREDIT_TREATMENT

How attributable upstream credits are passed through, applied or retained as expressly agreed.

Used in: Hosting.

### VENUE_COUNTY_STATE

Counsel-approved county and state or other precise judicial location.

Used in: MSA, NDA.

### WARRANTY_CURE_PROCESS

Correction timing, process and escalation for a reported covered warranty failure.

Used in: MSA.

### WARRANTY_FAILURE_REMEDY

Approved remedy following unsuccessful cure, including refund basis and any exclusivity.

Used in: MSA.

### WARRANTY_PERIOD

Definite duration measured from acceptance of each covered deliverable.

Used in: MSA.

### WEBSITE_SPECIFICATION

Pages/templates, counts, CMS, navigation, languages, forms, migration and specific features.

Used in: Website.

## Validation count

This revision contains 279 unique tokens across the templates and optional clause library. Every token has an entry above. This count is a structural check, not legal review.
