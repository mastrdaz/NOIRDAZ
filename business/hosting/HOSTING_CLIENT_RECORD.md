# Hosting client record

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

PRIVATE record for [[CLIENT_ID]] · Service [[SERVICE_ID]] · Owner [[SERVICE_OWNER]] · Verified [[LAST_VERIFIED_DATE]]

- Executed hosting/SOW/support exhibits and service dates: [[HOSTING_AGREEMENTS]]
- Domain, registrar, registrant, renewal payer and expiry: [[DOMAIN_INVENTORY]]
- DNS provider, zone export location, TTL baseline and change approvers: [[DNS_RECORD]]
- Host/account owner, region, plan, environment URLs, architecture and dependencies: [[HOSTING_INVENTORY]]
- Separate test/production, data classification and data-location approval: [[ENVIRONMENT_RECORD]]
- TLS issuer/renewal method/expiry alert: [[TLS_RECORD]]
- Admin accounts, MFA/recovery owner, vault reference and roles: [[ACCESS_INVENTORY]]
- Backups: scope, cadence, encryption, retention, location, owner and failure alert: [[BACKUP_RECORD]]
- Recovery point objective/recovery time objective and last measured restoration: [[RECOVERY_OBJECTIVES]] / [[RESTORE_TEST_RECORD]]
- Monitoring endpoints, checks, thresholds, on-call route and last alert test: [[MONITORING_RECORD]]
- Maintenance window/timezone, supported versions and pending updates: [[MAINTENANCE_RECORD]]
- Contracted support window, priority targets and emergency contacts: [[SUPPORT_ENTITLEMENT]]
- Monthly budget/usage thresholds, client/vendor payer and renewal notice: [[HOSTING_ECONOMICS]]
- Incident log, known limitations, accepted risks and open actions: [[OPERATING_RISKS]]
- Export procedure, transfer constraints, termination/deletion plan: [[HOSTING_EXIT_PLAN]]

Do not claim backup or monitoring coverage unless an actual successful check and alert route are recorded. Recovery objectives are design goals unless expressly made contractual commitments in reviewed signed terms.
