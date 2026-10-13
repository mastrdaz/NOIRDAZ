# Payment Integration Addendum

DRAFT — ATTORNEY REVIEW — NOT APPROVED FOR SIGNATURE

This Addendum is effective [[EFFECTIVE_DATE]] between [[PROVIDER_LEGAL_NAME]] (Provider) and [[CLIENT_LEGAL_NAME]] (Client), supplements SOW [[SOW_ID]] for [[PROJECT_NAME]], and incorporates the MSA dated [[MSA_DATE]]. The Software and Integration Addendum applies only if included in the signed attachment index.

## 1 Limited technical service

Provider will configure and test [[PAYMENT_INTEGRATION_SCOPE]] using [[PAYMENT_PROCESSOR]]. The merchant of record is [[MERCHANT_OF_RECORD]]. Client's acquiring or compliance-accepting entity is [[ACQUIRER_OR_COMPLIANCE_CONTACT]]. Processor accounts, payout destinations and merchant agreements remain in the name of the authorized merchant.

Provider supplies technical integration services. This Addendum does not appoint Provider as a bank, payment facilitator, money transmitter, merchant of record, escrow holder or custodian of Client funds. Provider will not receive customer proceeds in its own account or change settlement instructions under this scope. A business model requiring any such role must stop for a separate legal, processor and operational assessment.

Client is responsible for its product or service, customer disclosures, authorization to charge, tax decisions, refund policy, fulfillment and handling of disputes and chargebacks. Provider remains responsible for performing the technical duties expressly assigned to it. Processor failures or merchant responsibilities do not excuse a defect in Provider's agreed implementation.

## 2 Approved card data flow

The payment flow is [[PAYMENT_DATA_FLOW]], identifying each browser element, endpoint, processor-hosted page or iframe, script source, token, webhook, log and storage destination. Raw primary account numbers, card security codes, full magnetic-stripe data and PIN data must not enter Provider-controlled servers, databases, support tickets, analytics, logs or repositories under this scope. No sensitive authentication data may be retained after authorization where prohibited by applicable card requirements.

Only the approved processor collects card credentials through its approved implementation. Provider may receive the minimum approved tokens and transaction metadata listed in [[PAYMENT_METADATA_ALLOWLIST]]. Tokens are treated as confidential and security-sensitive according to their capabilities; tokenization is not an automatic exemption from all obligations.

If the implementation requires direct handling of cardholder data, the parties must stop that work and approve a revised scope, security design, responsibility allocation and qualified compliance review before enabling it. Client must not send actual card credentials to Provider to diagnose a problem.

## 3 PCI responsibilities and verification

The allocation of merchant, Provider and processor responsibilities is [[PCI_RESPONSIBILITY_MATRIX]]. It must identify the applicable validation path, evidence to obtain from service providers, who works with the acquirer, external scan ownership, script protections where applicable, patching, incident reporting and annual or change-triggered review.

Client will confirm the required assessment or validation method with its acquirer or other compliance-accepting entity. Provider will provide accurate technical information and the evidence it has agreed to produce. Neither party will represent that an integration is PCI compliant, eligible for a particular self-assessment questionnaire or outside scope merely because a processor uses a hosted page, iframe or token.

For embedded payment forms, the parties will document the controls or processor confirmation needed to address script-attack eligibility requirements applicable to the selected validation path. For redirect and iframe implementations, they will also determine and assign applicable external vulnerability scanning obligations. Provider will not sign a merchant attestation or certify another party's compliance unless separately authorized and qualified for that exact role.

## 4 Transaction and credential controls

Provider will separate sandbox and live credentials and use the approved secret vault [[SECURE_ACCESS_METHOD]]. The implementation must authenticate webhook origin, check relevant message freshness, enforce idempotency, avoid duplicate charges, validate amount and currency on trusted systems, and log only the approved metadata, as specified in [[PAYMENT_CONTROL_SPECIFICATION]]. A browser success message alone is not proof of settlement.

Permissions for viewing transactions, issuing refunds, canceling subscriptions and managing disputes will be assigned individually in [[PAYMENT_ACTION_AUTHORITY]]. Technical access does not itself authorize Provider to charge, refund, transfer, alter pricing or accept financial obligations. Each real financial action requires the separate authority specified by Client; no blanket authority is created here.

Client will approve customer-facing billing descriptions, pricing, tax settings, refund disclosures, recurring-charge consent and cancellation behavior in [[BILLING_AND_CONSENT_SPECIFICATION]]. Provider will implement those approved choices. The parties will not infer recurring billing permission from a one-time payment. Changes in payment methods or destinations must follow a verified anti-fraud approval process.

## 5 Testing and live activation

Provider will first use processor test tools and synthetic payment data. The test plan [[PAYMENT_TEST_PLAN]] will address successful and declined payments, additional authentication where applicable, abandoned checkout, duplicate webhooks, retries, partial failure, cancellation, refunds, subscription changes, reconciliation and failure alerts.

Any live test involving actual funds requires Client's separate transaction-specific approval of the counterparty, amount, currency, recurrence, terms, fees and refund restrictions, followed by explicit final confirmation immediately before execution. A refundable test can still incur nonrefundable processor fees. Approval of this Addendum, test plan or launch form is not that final confirmation.

Live activation requires [[PAYMENT_LAUNCH_APPROVERS]] to verify the merchant account, intended payout settings, completed tests, required compliance evidence, operational contacts and rollback or disablement method. The exact deployment and reconciliation plan is [[LAUNCH_PLAN]]. Provider will record the live version and configuration without recording secrets.

## 6 Fees disputes incidents and exit

Processor, network, dispute, foreign-exchange and related fees are payable by the party identified in [[THIRD_PARTY_COST_AUTHORIZATION]]. Those fees are distinct from Provider's service fees. Provider does not promise processor approval, settlement timing, fraud elimination or chargeback outcomes. Changes imposed by a processor will be assessed through change control; Provider may not purchase an upgrade without approval.

The parties will reconcile transaction records under [[PAYMENT_RECONCILIATION_PROCESS]], identify the authoritative source and escalate discrepancies. A suspected payment-data compromise must be handled under the MSA incident process and applicable processor/acquirer reporting obligations; contract notice periods do not delay an earlier required report. Containment must preserve relevant evidence and avoid unnecessary disclosure of card data.

On termination, Provider will supply the agreed transaction-metadata exports and configuration documentation, identify pending events and subscriptions, and revoke its access. Customer billing or subscriptions will not be canceled, transferred or re-created without authorized instructions. Token portability depends on processor rules and lawful transfer arrangements; Provider does not promise that tokens can be exported. Ordinary data retention, backup expiration and legal holds follow the MSA. MSA risk allocation applies; this Addendum does not create an unlimited chargeback or fraud indemnity.

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
