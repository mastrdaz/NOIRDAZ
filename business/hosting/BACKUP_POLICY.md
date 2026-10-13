# Backup and restoration policy

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Proposed internal baseline, subject to client data sensitivity, platform capability, cost approval and signed scope. Backups are only useful when restoration is tested.

## Define per service

Record protected databases, uploads, configuration, source and external dependencies; backup method and consistency; frequency; retention; location/region; encryption/key owner; access roles; failure alert; recovery point/time objectives; restore operator; deletion/legal-hold behavior. Provider snapshots alone may share the production failure domain.

For a typical small site, assess daily backups, 30-day retention and a separate protected copy as a starting proposal. These are not active settings or promises. Transactional systems may need tighter recovery points; static sites may use repository/configuration recovery plus asset copies. Select the design only after testing against client requirements and approved cost.

## Operating checks

- [ ] Daily automated job result, age and size checked where approved monitoring exists; otherwise assign a manual daily check
- [ ] Failure/missed heartbeat reaches a named person; ticket includes last good recovery point
- [ ] Monthly sample restore in isolation verifies application and representative records
- [ ] Full recovery exercise before launch and after material architecture change; measure elapsed time
- [ ] Quarterly review access, encryption, isolation, retention and restore documentation
- [ ] Record restore evidence, failed steps and corrective owner/due date

Never restore over production without authorization and a rollback plan. Use isolated networks and scrubbed data where possible. Preserve evidence during an incident before altering backups. Erase expired copies under an approved schedule, suspend disposal for legal holds, and state any immutable-backup expiry limit honestly.
