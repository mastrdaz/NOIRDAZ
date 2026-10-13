# Hosting outage response

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Use this for availability/performance failures. If compromise, data loss, unauthorized access or payment-page tampering is suspected, invoke [security incident response](../security/INCIDENT_RESPONSE.md) as well and preserve evidence.

1. Open incident ID; record UTC/local timezone, detection, affected service, symptoms, scope and last known good state.
2. Check independent monitoring and provider status; confirm whether the client journey is actually affected. Avoid exposing customer data while testing.
3. Assign incident lead and communication owner (initially owner). Classify priority using support definitions and signed coverage.
4. Acknowledge facts, impact, workaround and next update time. Do not guess cause or restoration time.
5. Use the approved runbook: safe diagnostics, containment/failover/restart/restore only within existing authority. New spend, DNS changes, expanded access or destructive steps require appropriate approval.
6. Preserve configuration/logs; record each action/time/result. Test rollback or restoration in isolation where possible.
7. Verify essential client workflows and sustained healthy checks; ask the client to confirm recovery where appropriate.
8. Send closure summary, duration, known data impact or investigation status and remaining actions.
9. Within a proposed 3 business days, review cause, detection, recovery, communication and prevention. Assign corrective owners/dates and update the runbook.

Incident record: [[INCIDENT_ID]], [[INCIDENT_LEAD]], [[AFFECTED_SERVICES]], [[TIMELINE]], [[CLIENT_UPDATES]], [[RECOVERY_EVIDENCE]], [[CORRECTIVE_ACTIONS]]. Contractual/legal notice obligations can run faster than this internal cadence.
