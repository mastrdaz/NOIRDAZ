# Hosting onboarding

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Before accepting responsibility for an existing or new service:

- [ ] Verify signed scope, supported stack, service period, billing and client authority
- [ ] Confirm client owns its domain and merchant account; document any exception
- [ ] Inventory current provider, licenses, architecture, data, DNS, email and exit constraints
- [ ] Complete new-project security review and approve data locations/subprocessors
- [ ] Provision only approved environments/accounts; use named roles and MFA
- [ ] Configure TLS, supported dependencies and least-privilege network/application access
- [ ] Establish encrypted backups with separate credentials and retention
- [ ] Perform and time a restore into an isolated environment; verify essential data/journey
- [ ] Configure external uptime/TLS/backup-age/usage checks and test alert receipt
- [ ] Document maintenance window, rollback, support boundaries and emergency contacts
- [ ] Confirm capacity and recovery objectives against actual testing
- [ ] Follow project launch authorization before cutover or DNS changes
- [ ] Record inventory, runbook, proof of handover and exact responsibility start time

Gate owner [[SERVICE_OWNER]] · Client [[CLIENT_APPROVER]] · Date [[SERVICE_START_DATE]] · Evidence [[HOSTING_READINESS_EVIDENCE]]. If the owner cannot provide the requested coverage, quote a smaller service or obtain approved third-party coverage; do not imply a 24/7 team.
