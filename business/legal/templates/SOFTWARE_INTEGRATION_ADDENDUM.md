# Software and Integration Addendum

DRAFT — ATTORNEY REVIEW — NOT APPROVED FOR SIGNATURE

This Addendum is effective [[EFFECTIVE_DATE]] between [[PROVIDER_LEGAL_NAME]] (Provider) and [[CLIENT_LEGAL_NAME]] (Client), supplements SOW [[SOW_ID]] for [[PROJECT_NAME]], and incorporates the MSA dated [[MSA_DATE]]. It applies to the custom software, workflow automation and integrations expressly ordered in the SOW.

## 1 Architecture and boundary

The approved architecture, systems of record, data flow, environments, connected accounts and supported versions are [[INTEGRATION_ARCHITECTURE]]. Provider will implement the functions and interfaces described in [[INTEGRATION_SPECIFICATION]]. Interfaces or data fields not identified in that specification are outside scope.

The parties will identify which system is authoritative for each data category, conflict-resolution rules, synchronization direction, frequency, expected volume and tolerable delay in [[DATA_MAPPING_AND_SYNC_RULES]]. An integration is not presumed to replace Client's accounting, operational review or legal-record responsibilities.

## 2 Access and external dependencies

Client will obtain the required vendor permissions, subscriptions and authorized test accounts assigned to it in [[CLIENT_DEPENDENCIES]]. Provider will use the least privileges reasonably needed and separate production credentials from test credentials. Secrets will be stored and transferred through [[SECURE_ACCESS_METHOD]] and excluded from source files, logs and documentation.

The vendor API versions, quotas, rate limits, license terms and change-notice contacts are [[API_DEPENDENCY_REGISTER]]. Provider will disclose known material dependencies and any end-of-support dates identified during the work. Unless included in the ordered maintenance scope, future vendor changes are subject to a change order. Provider remains responsible for correcting its own implementation that did not meet the agreed supported specification when delivered.

Provider will not materially broaden OAuth scopes, create additional persistent access or connect a new account without Client's specific approval. Client may revoke access; the parties will document the resulting functionality or schedule impact.

## 3 Reliability and test controls

Provider will implement the agreed validation, authentication, authorization, retry, idempotency, duplicate handling, exception queue, reconciliation and logging controls in [[INTEGRATION_CONTROL_SPECIFICATION]]. Retries that can create duplicate records, invoices, messages or other consequential actions must be bounded and tested. A transport acknowledgement alone is not proof that the intended business result occurred.

Testing will use synthetic or approved minimized data in a separate environment wherever practicable. Client will not supply production-sensitive data for convenience without the approved processing basis and safeguards. The test plan [[INTEGRATION_TEST_PLAN]] must cover normal cases, permission failures, rate limits, interrupted connections, malformed input, replayed events, partial completion, rollback and recovery. Provider will deliver results and known limitations with the release candidate.

Any workflow that can move money, create orders, send external communications, modify legal records or make high-impact decisions must include the human authorization and exception-handling controls in [[CONSEQUENTIAL_ACTION_CONTROLS]]. Development or access approval does not authorize Provider to perform real transactions on Client's behalf.

## 4 Release acceptance and change control

Acceptance criteria are [[ACCEPTANCE_CRITERIA]] and the MSA acceptance process applies. Client will test the business rules and sample reconciliations assigned to it; Provider remains responsible for its technical tests. Unresolved issues and approved workarounds must be recorded with an owner and due date, not hidden in a general acceptance statement.

The production cutover, data freeze if any, backup, reconciliation, rollback thresholds and approvers are [[LAUNCH_PLAN]]. Provider will not deploy or activate a consequential workflow without the authorized release approval. New mappings, connectors, user roles, transaction types or material volume increases require a change order and renewed security review where relevant.

## 5 Rights documentation and maintenance

Assigned Deliverables, Background Materials and third-party components are identified in the SOW. Provider will deliver the component/license inventory, agreed source, build instructions, environment requirements, deployment instructions and operational runbook in [[HANDOVER_DELIVERABLES]]. The MSA's assignment and embedded-material license apply. A subscription product remains licensed only as described in its executed product terms; a customization fee does not silently transfer ownership of that product.

The maintenance boundary, supported versions, dependency updates and end-of-support process are [[SOFTWARE_MAINTENANCE_SCOPE]]. Warranty corrections follow the MSA; enhancements, business-rule changes and third-party API adaptations are included only if that scope says so. Provider will give the agreed end-of-support notice [[END_OF_SUPPORT_NOTICE]] and propose a transition before discontinuing a supported version under its control.

## 6 Data exit and operational responsibility

Processing and retention follow [[DATA_PROCESSING_SCHEDULE]] and [[EXIT_AND_RETENTION_SCHEDULE]]. The exit package must identify export formats, schemas, transformation rules, pending transactions, failed jobs and reconciliation status. The parties will decide whether queued jobs are completed, canceled or handed over before disabling the integration. No replay of pending jobs is permitted without review where it could duplicate a consequential action.

Provider will revoke access and return Client-controlled repositories and accounts as agreed. Client will rotate secrets and arrange replacement operations. The parties will retain only records justified by the retention schedule or a documented legal hold. This Addendum does not change MSA liability limits or create a separate indemnity.

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
