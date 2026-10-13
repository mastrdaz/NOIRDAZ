# Project Acceptance and Launch Authorization

DRAFT — ATTORNEY REVIEW — NOT APPROVED FOR SIGNATURE

This record is effective [[EFFECTIVE_DATE]] between [[PROVIDER_LEGAL_NAME]] (Provider) and [[CLIENT_LEGAL_NAME]] (Client) for SOW [[SOW_ID]], [[PROJECT_NAME]], under the MSA dated [[MSA_DATE]]. It records two separate decisions. Neither acceptance nor launch authority may be inferred from an incomplete field.

## 1 Release being reviewed

The deliverables and exact version, release tag or immutable artifact are [[RELEASE_IDENTIFICATION]]. The review location is [[REVIEW_LOCATION]]. The applicable acceptance criteria are [[ACCEPTANCE_CRITERIA]], and the test evidence is [[ACCEPTANCE_EVIDENCE]]. Client reviewed the deliverables through [[CLIENT_REVIEW_REPRESENTATIVE]] on [[REVIEW_DATE]].

Known unresolved items, severity, owner, correction date and retest evidence are [[ACCEPTANCE_PUNCH_LIST]]. The record must say “None” if there are no known items. A general statement that everything is satisfactory does not erase a specifically listed obligation.

## 2 Acceptance decision

Client's decision is [[ACCEPTANCE_DECISION]], completed as one of: accepted; accepted subject to the attached punch list; or rejected with the specified material nonconformities. The decision applies only to the listed deliverables and version. If rejected, the MSA correction and retest process continues and this record gives no launch authority.

Acceptance acknowledges conformity to the stated criteria, subject to listed items. It does not waive latent defects, express warranties, confidentiality or data-protection duties, intellectual property rights, pending corrections or other rights that survive acceptance under the MSA. The related invoicing milestone is [[ACCEPTANCE_INVOICE_EFFECT]]; this record does not independently alter the price.

## 3 Launch readiness

The readiness record is [[LAUNCH_READINESS_EVIDENCE]]. Before release, Provider will confirm the checks assigned to it, and Client will confirm its approvals, including:

- Correct production destination and approved change window with timezone
- Authorized domain and DNS control, certificate, least-privilege access and recovery contact
- Backup or export and a verified restoration or rollback method
- Required privacy text, consent configuration, accessibility review and approved public content
- Production secrets handled securely and test data removed where required
- Monitoring, incident contacts, support coverage and post-launch checks
- Payment integration approval and required compliance evidence, if applicable

An incomplete check must be identified in [[LAUNCH_EXCEPTIONS]] with its operational effect and responsible approver. An exception cannot waive a mandatory legal requirement or authorize handling data outside the agreed scope.

## 4 Separate launch decision

Client's launch decision is [[LAUNCH_DECISION]], completed as “Authorized” or “Not authorized.” If authorized, the permission is limited to the exact release and actions in [[AUTHORIZED_LAUNCH_ACTIONS]], at [[LAUNCH_DESTINATION]], during [[LAUNCH_WINDOW]]. Provider's release approver is [[PROVIDER_RELEASE_APPROVER]], and Client's is [[CLIENT_RELEASE_APPROVER]].

The rollback triggers, decision authority and method are [[ROLLBACK_PLAN]]. If a material new defect, security issue or deviation is discovered before launch, Provider will pause and obtain a revised decision rather than relying on approval for different conditions. Only the expressly listed production changes are authorized.

Live charges, refunds, fund movements, new subscriptions, paid upgrades and other financial actions require separate transaction-specific approval and final confirmation immediately before execution. This form is not that final confirmation. Any customer announcement requires its own authorized recipient and content.

## 5 After launch

Post-launch checks, owners and review time are [[POST_LAUNCH_CHECKS]]. The recurring service start event remains [[RECURRING_SERVICE_START_EVENT]] under the SOW; this form does not add recurring charges. Outstanding items will remain tracked until their specified completion or an authorized change. The MSA remains controlling.

## Signatures

**Provider readiness acknowledgment**  
Legal name: [[PROVIDER_LEGAL_NAME]]  
Signature: [[PROVIDER_SIGNATURE]]  
Name: [[PROVIDER_SIGNATORY_NAME]]  
Title or capacity: [[PROVIDER_SIGNATORY_TITLE]]  
Date signed: [[PROVIDER_SIGNATURE_DATE]]

**Client acceptance and separate launch decision**  
Legal name: [[CLIENT_LEGAL_NAME]]  
Signature: [[CLIENT_SIGNATURE]]  
Name: [[CLIENT_SIGNATORY_NAME]]  
Title or capacity: [[CLIENT_SIGNATORY_TITLE]]  
Date signed: [[CLIENT_SIGNATURE_DATE]]
