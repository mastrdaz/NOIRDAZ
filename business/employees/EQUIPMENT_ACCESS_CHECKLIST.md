# Equipment and access checklist

Draft operating control. Owner: [[ACCESS_OWNER]]. Employee reference: [[EMPLOYEE_ID]]. Record lifecycle: provision / change / revoke. Store completed inventories privately; no passwords, secret keys, recovery codes or device identifiers in this repository.

## Request and approval

- [ ] Confirm role, manager, start/end date and approved client/project scope.
- [ ] Grant individual accounts, least privilege and separate production/test access.
- [ ] Owner approves each privileged, financial or client-system role; client permission is verified where needed.
- [ ] Record MFA, recovery ownership, access expiration and business backup owner.

| System or asset | Private record reference | Role or condition | Approver | Granted/returned | Revoke/test evidence |
|---|---|---|---|---|---|
| Laptop and accessories | [[DEVICE_RECORD_REFERENCE]] | [[DEVICE_CONDITION]] | [[APPROVER]] | [[ASSET_DATE]] | [[RETURN_REFERENCE]] |
| Business identity and email | [[IDENTITY_REFERENCE]] | [[IDENTITY_ROLE]] | [[APPROVER]] | [[ACCESS_DATE]] | [[REVOKE_REFERENCE]] |
| Password vault | [[VAULT_REFERENCE]] | [[VAULT_COLLECTION_SCOPE]] | [[APPROVER]] | [[ACCESS_DATE]] | [[REVOKE_REFERENCE]] |
| Repositories and projects | [[REPOSITORY_ACCESS_REFERENCE]] | [[REPOSITORY_ROLE]] | [[APPROVER]] | [[ACCESS_DATE]] | [[REVOKE_REFERENCE]] |
| Hosting, cloud, DNS and registrar | [[INFRASTRUCTURE_REFERENCE]] | [[INFRASTRUCTURE_ROLE]] | [[APPROVER]] | [[ACCESS_DATE]] | [[REVOKE_REFERENCE]] |
| CRM, support and documents | [[BUSINESS_APP_REFERENCE]] | [[BUSINESS_APP_ROLE]] | [[APPROVER]] | [[ACCESS_DATE]] | [[REVOKE_REFERENCE]] |
| Payroll, banking and billing | [[FINANCE_ACCESS_REFERENCE]] | [[FINANCE_ROLE_OR_NONE]] | [[APPROVER]] | [[ACCESS_DATE]] | [[REVOKE_REFERENCE]] |
| Client apps and integrations | [[CLIENT_ACCESS_REFERENCE]] | [[CLIENT_SCOPE]] | [[APPROVER]] | [[ACCESS_DATE]] | [[REVOKE_REFERENCE]] |

## Device and account readiness

- [ ] Approved OS, security updates, encryption, screen lock and endpoint protection verified.
- [ ] Company owns recovery path; employee has no need to share a password.
- [ ] Backups, loss/theft reporting and permitted use explained.
- [ ] No production/client data on personal devices or unapproved storage; exceptions require documented review.
- [ ] Verify login and actual permissions; record successful test without capturing secrets.

## Role change or departure

- [ ] Remove old privileges before adding new ones where practical; update inventory.
- [ ] Revoke active sessions, tokens, SSH keys, OAuth grants, vault shares and recovery methods.
- [ ] Transfer business/service ownership; rotate shared secrets safely; verify scheduled jobs survive.
- [ ] Confirm returned equipment, preservation holds and authorized disposition.
- [ ] Independently verify revocation and close every row; list any blocker with owner and deadline.

Review cadence proposal: at start, role change, separation and quarterly. An access checklist does not authorize payment, credential disclosure or public sharing.
