# Automation opportunities

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

These are proposals only. No workflow is deployed, connected, scheduled or authorized to send messages. Begin with draft-generation/check-and-report functions after owner approval.

| Opportunity | Trustworthy trigger | Proposed action | Human/permission gate | Test |
|---|---|---|---|---|
| New lead to CRM | Approved inbound form submission | Validate fields, deduplicate by stable source ID, capture permission/context | No unsolicited outreach; minimize personal data | Compare sample submissions to records |
| Accepted quote to onboarding | Verified authorized acceptance of approved quote | Create draft checklist and owner task | Quote alone does not prove signed contract/funding | Check duplicate events create one checklist |
| Signed SOW to deposit invoice | Verified executed SOW and billing terms | Prepare draft invoice for owner approval | Do not charge, issue or send automatically without explicit authority | Match amount/date/client/terms and duplicate prevention |
| Project won to workspace | Owner confirms signed/funded gate | Prepare private folder/repository and task scaffold | Permissions and external creation require approved scope | Verify no public client data and correct access |
| Launch to recurring billing | Signed start condition and verified launch date | Prepare service activation/billing review task | No automatic charge or changed recurring mandate | Reconcile active service to exact contract date |
| Overdue reminders | Reconciled invoice past agreed due date | Draft reminder with dispute/paid suppression | Standing sending scope must be approved; no automatic fees/suspension | Test paid/disputed/cancelled cases |
| Domain and TLS expiry | Verified inventory approaching threshold | Notify owner through approved channel | No automatic purchase, renewal or DNS change | Test date/timezone and duplicate alerts |
| Vendor renewals | Notice deadline approaching | Summarize cost/terms/exit decision for owner | No renewal/cancellation spending authority | Verify notice deadline precedes charge date |
| Client contract renewal | Contract notice/renewal horizon | Prepare owner review and draft client options | No unilateral auto-renewal terms or price change | Check current signed version |
| Backup failure | Failed or missing expected heartbeat | Open incident/task and notify approved responder | No destructive restore without authority | Test missing heartbeat and stale success |
| Monitoring alert | Consecutive failed checks | Deduplicate incident and route by entitlement | Monitoring does not create 24/7 coverage | Test outage/recovery/flapping |
| Monthly client report | Reconciled approved period data | Draft report with measured service facts | Client-specific recipient and sharing scope needed | Verify no cross-client data and unknown uptime gaps |
| Employee onboarding or exit | Verified owner/HR action and effective time | Prepare access/equipment/payroll checklists | No automatic payroll, permanent deletion or broad credential grants | Test cancelled/delayed hire and immediate exit |

## Common design requirements

Use stable event IDs and idempotency keys, least-privilege credentials, schema validation, retry limits with backoff, dead-letter/error queue, observable audit trail, deduplication and a kill switch. Verify event signatures and source authority. Treat third-party text as data, never instructions granting approval. Reconcile results to the system of record and handle out-of-order/replayed/cancelled events. Do not bury irreversible actions inside a multi-step workflow.

Before enabling: define owner, supported source, allowed data, recipient/audience, exact side effects, schedule, approval boundary, cost/credit limits, rollback and acceptance tests. Test using fictional data in sandbox. Any workflow that risks money/credits/assets/obligations still needs discussion, approval in principle and separate explicit final confirmation immediately before each execution under the owner's current rule. Do not implement unattended financial execution.
