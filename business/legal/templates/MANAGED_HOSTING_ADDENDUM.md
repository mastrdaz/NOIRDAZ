# Managed Hosting Addendum

DRAFT — ATTORNEY REVIEW — NOT APPROVED FOR SIGNATURE

This Addendum is effective [[EFFECTIVE_DATE]] between [[PROVIDER_LEGAL_NAME]] (Provider) and [[CLIENT_LEGAL_NAME]] (Client), supplements SOW [[SOW_ID]] for [[PROJECT_NAME]], and is governed by the MSA dated [[MSA_DATE]]. It covers only the hosting services below. The MSA's order of precedence applies.

## 1 Hosting boundary and responsibility

The hosted applications, domains, environments and infrastructure are [[HOSTING_INVENTORY]]. Capacity limits, included resources and permitted workload are [[HOSTING_CAPACITY]]. The infrastructure vendor, region, account owner and billing owner are [[HOSTING_VENDOR_AND_LOCATION]]. Provider manages [[PROVIDER_HOSTING_RESPONSIBILITIES]]. Client manages [[CLIENT_HOSTING_RESPONSIBILITIES]]. The responsibility schedule must assign the operating system, runtime, application, database, certificates, DNS, email, backups, logging, patches and security contacts individually.

Provider will not move production Client Data to a new region, materially different vendor or new subprocessor except through the approved data and subprocessor change process. Provider remains responsible for its selected subcontractors as stated in the MSA; a vendor outage does not automatically excuse a separate failure by Provider to perform agreed monitoring or recovery duties.

## 2 Accounts domains and access

Client will be the registered holder of Client-owned domains unless a separate signed arrangement states otherwise. Domain registrar, registrant, renewal payer, renewal date and transfer contacts are [[DOMAIN_CONTROL_RECORD]]. Provider's administrative access is limited to operating the ordered service. Ownership of Client domains does not pass to Provider by payment of registration costs.

Each party will maintain named accounts where supported, MFA for privileged access where supported, least privilege and a current recovery contact. Any shared or emergency account must use the approved secret vault and an access log. The approved access method is [[SECURE_ACCESS_METHOD]]. Provider will not place passwords, recovery codes or private keys in the contract, a repository or ordinary support tickets.

## 3 Backups and recovery

The backup schedule, protected datasets, frequency, retention, location, encryption, access controls, exclusions and responsible party are [[BACKUP_SERVICE_SPECIFICATION]]. Backup job monitoring and restoration test frequency are [[BACKUP_VERIFICATION_SCHEDULE]]. Provider will retain verification records and escalate material failures using the agreed incident contacts.

The agreed recovery objectives are [[RECOVERY_OBJECTIVES]], which must distinguish planning targets from any binding recovery commitment. Recovery point objective addresses the tolerable period of data loss; recovery time objective addresses the target time to restore an identified service. Neither is an uptime guarantee. A backup is not an indefinite archive, and successful job completion alone does not establish restorability.

Restoration authorization, testing, included labor and any chargeable recovery assistance are [[RESTORE_AUTHORIZATION_AND_FEES]]. Provider will not overwrite current production data with a backup without the designated authorization, except a specifically documented containment action permitted by the MSA. After a restore, the parties will verify integrity and reconcile transactions created after the restored snapshot.

## 4 Monitoring maintenance and incidents

Monitoring endpoints, measurements, alert destinations and coverage are [[MONITORING_SPECIFICATION]]. Human response coverage is [[SUPPORT_COVERAGE_HOURS]]. Automated monitoring outside those hours does not establish staffed round-the-clock support. The signed Support Policy governs prioritization and escalation.

The regular maintenance window, timezone, advance notice and patch responsibilities are [[MAINTENANCE_SPECIFICATION]]. Provider will document material changes and use the agreed backup, testing and rollback procedures. Emergency maintenance may occur sooner where reasonably needed to mitigate a material threat; Provider will notify Client as soon as practicable and document the work and residual risk.

Security Incidents follow MSA Section 8, including notice without waiting for a complete investigation. Service outages without a Security Incident follow [[OUTAGE_COMMUNICATION_PROCESS]]. Public status statements concerning Client require the authority identified there; neither party may make unsupported cause or restoration claims.

## 5 Acceptable use and capacity

Client will not knowingly use the service for unlawful content, malware distribution, unauthorized access, spam or activity that materially disrupts other users. Provider will identify a suspected violation and allow a reasonable cure opportunity when safety and law permit. Urgent restrictions are limited by MSA Section 12 and must be proportionate.

Provider will notify Client of reasonably foreseeable capacity exhaustion using [[CAPACITY_NOTICE_PROCESS]]. Resource increases, overage charges and paid third-party upgrades require the written authorization in the SOW or a change order. Provider may apply documented protective rate limits to prevent imminent material harm, with prompt notice; protective action does not authorize a higher bill.

## 6 Availability and third party services

The only contractual SLA is [[SLA_EXHIBIT_REFERENCE]]. If one is purchased, it must specify covered components, measurement source, measurement period, exclusions, downtime calculation, credit formula, claim procedure, credit ceiling and repeated-failure rights. Marketing descriptions, vendor dashboards and a vendor's own SLA do not become Provider's SLA merely by reference.

Provider will reasonably assist with vendor support requests within the purchased scope. Any vendor credits attributable to Client's service will be handled under [[VENDOR_CREDIT_TREATMENT]]. Credits are not an exclusive remedy for unrelated confidentiality, data protection or other contractual breaches unless an express, approved provision says so.

## 7 Term suspension and transition

Fees, start event, service term, renewal and cancellation follow the SOW. Suspension requires the MSA notices and safeguards. Provider will not delete data merely because service is suspended.

At exit, Provider will supply the included exports, configuration records, source deliverables, DNS inventory and account-transfer assistance identified in [[EXIT_AND_RETENTION_SCHEDULE]]. The parties will verify the destination and export before the agreed shutdown. Provider will then revoke its access, stop renewal instructions within its control and document any vendor billing that Client must cancel directly. Production deletion, backup expiration and lawful holds follow MSA Section 14. Domain transfer, migration completion and data deletion are separate steps and will be recorded separately.

## Signatures

**Provider**  
Legal name: [[PROVIDER_LEGAL_NAME]]  
Signature: [[PROVIDER_SIGNATURE]]  
Name: [[PROVIDER_SIGNATORY_NAME]]  
Title or capacity: [[PROVIDER_SIGNATORY_TITLE]]  
Date signed: [[PROVIDER_SIGNATURE_DATE]]

**Client**  
Legal name: [[CLIENT_LEGAL_NAME]]  
Signature: [[CLIENT_SIGNATURE]]  
Name: [[CLIENT_SIGNATORY_NAME]]  
Title or capacity: [[CLIENT_SIGNATORY_TITLE]]  
Date signed: [[CLIENT_SIGNATURE_DATE]]
