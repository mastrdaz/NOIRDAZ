# Security incident response

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Use for suspected compromise, unauthorized disclosure, ransomware, lost devices, exposed credentials, data corruption or payment tampering. Treat uncertainty seriously without claiming an unverified breach.

## Prepare

Private contact register: owner/incident lead [[INCIDENT_LEAD]], backup [[BACKUP_OWNER]], client security contact [[CLIENT_SECURITY_CONTACT]], counsel [[COUNSEL_CONTACT]], insurer/broker [[INSURANCE_CONTACT]], hosting/vendor escalation [[VENDOR_INCIDENT_CONTACT]]. Record contract notice obligations and insurance notice/consent terms before incidents occur. Test the route quarterly.

## Detect and contain

1. Open incident ID; record discovery time, source, systems/data potentially affected and known facts. Restrict access to the incident record.
2. Preserve relevant logs, snapshots and evidence with timestamp, source, hash and custodian where feasible. Do not delete or overwrite evidence during hurried cleanup.
3. Notify owner promptly through a verified channel. Assess ongoing exposure, credential compromise, client impact and whether an attacker controls normal communications.
4. Take only authorized containment steps from the runbook, such as isolating an affected workload or revoking a known compromised credential under the approved response authority. Escalate any new permission, destructive step or spending approval. Emergency status does not authorize financial risk.
5. Engage counsel/insurer/specialist when appropriate and authorized; determine applicable contractual and jurisdictional notification duties from the actual facts. Do not use a generic 72-hour rule or delay a required notice while waiting for full certainty.

## Investigate and recover

Establish timeline, entry path, affected accounts/data, persistence and scope. Use clean recovery sources; patch the cause, rotate affected credentials through secure flows, verify isolation and restore in stages. Test client workflows, data integrity and monitoring before declaring recovery. Preserve evidence and legal holds.

## Communicate and improve

Only the designated owner communicates externally after verifying recipients, content and required approvals. Provide factual impact, actions, next update and uncertainty; do not admit liability, speculate attribution or promise compensation. Counsel guides legal notices; insurer conditions may govern vendor engagement. Document decisions, notifications, recovery evidence and corrective owners/dates. Review lessons promptly and test the revised control.

Incident fields: [[INCIDENT_ID]], [[DISCOVERED_AT]], [[FACTS_AND_UNCERTAINTIES]], [[AFFECTED_DATA]], [[EVIDENCE_REGISTER]], [[CONTAINMENT_APPROVALS]], [[NOTICE_DECISIONS]], [[RECOVERY_EVIDENCE]], [[CORRECTIVE_ACTIONS]].


Reference basis, checked 2026-10-13: [NIST small business cybersecurity resources](https://www.nist.gov/itl/smallbusinesscyber), [NIST SP 800-61r3 incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final), and [FTC small business cybersecurity](https://www.ftc.gov/business-guidance/small-businesses/cybersecurity). These inform the proposed controls; following a checklist is not a certification.
