# New project security review

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Project [[PROJECT_ID]] · Reviewer [[SECURITY_REVIEWER]] · Date [[REVIEW_DATE]]

- [ ] Data categories, source, purpose, volume, subjects and locations mapped
- [ ] Health/minors/financial/employment/biometric/payment or other regulated use identified and specialist gate resolved
- [ ] Privacy questionnaire complete; client responsibilities, notices/consent and processing terms reviewed
- [ ] Account/domain/merchant ownership, approvers and least-privilege roles verified
- [ ] MFA, recovery and client-separated production/test environments planned
- [ ] Secrets have an approved store and rotation owner; no credentials in repository
- [ ] Synthetic/redacted test data and limited logs; sensitive fields excluded
- [ ] Input validation, authorization, dependency and abuse/threat checks planned
- [ ] Hosted/tokenized payment flow, webhook signatures/idempotency and reconciliation assessed when relevant
- [ ] Backups, restore test, monitoring, incident contact and notice duties defined
- [ ] Vendor rights/API terms, subprocessors, locations and exit/export checked
- [ ] Support/recovery/uptime promises match tested capability and staffing
- [ ] Insurance requirements and exclusions reviewed by broker where triggered
- [ ] Residual risks, acceptance owner, mitigation due and no-go criteria recorded

Decision [[SECURITY_GO_NO_GO]]. No-go: unknown authority, unapproved restricted data, unsupported card storage, unavailable recovery, uncontrolled cross-client access or unresolved legal requirement. A signed checklist is evidence of review, not a guarantee that a system is secure.
