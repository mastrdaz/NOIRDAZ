# Launch checklist

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Project [[PROJECT_ID]] · Release [[DELIVERABLE_VERSION]] · Window [[LAUNCH_WINDOW]] · Timezone [[TIMEZONE]]

## Go or no go

- [ ] Signed acceptance and separate production launch authorization verified
- [ ] Known issues and business risks accepted by authorized client
- [ ] Production account/domain/DNS ownership and change authority verified
- [ ] Tested backup/export and rollback plan available; responsible operator assigned
- [ ] TLS, access/MFA, secrets, permissions, monitoring and alert route checked
- [ ] Dependencies, configuration, data migration and integration endpoints verified
- [ ] Required privacy notices, consent, accessibility and payment review resolved
- [ ] Support coverage, emergency contact and client communications confirmed
- [ ] Billing service-start condition and exact recurring date agreed
- [ ] Change window, expected disruption, rollback trigger and decision owner recorded

## Execute only with authorization

Capture current configuration and recovery point; make the approved change; run smoke tests for the essential client journey, login/roles, forms/integrations and read/write data paths. Record result/time. If rollback criteria are met, follow the pre-approved rollback plan; escalate ambiguity immediately. Do not test a live payment by risking funds without transaction-specific approval.

## Verify and hand over

- [ ] Monitoring healthy and test alert acknowledged
- [ ] Client verifies essential workflow; no unresolved launch-blocking defect
- [ ] Runbook, credentials references and service inventory current
- [ ] Observation window and next check assigned
- [ ] Actual launch/start times, release hash and evidence recorded
- [ ] Owner confirms close or rollback; support and finance informed

Go/no-go [[LAUNCH_DECISION]] by [[LAUNCH_APPROVER]] at [[DECISION_TIME]]. Rollback trigger [[ROLLBACK_TRIGGER]]. Evidence [[LAUNCH_EVIDENCE]].
