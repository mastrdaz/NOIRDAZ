# Legal, Security, and Business Checklist

This is a planning checklist, not legal advice.

## Before accepting money

- [ ] Noirdaz Industries legal entity/banking/payment setup is ready, or invoicing structure is otherwise settled.
- [ ] Written statement of work (SOW) defines the exact deliverable.
- [ ] Master/service terms define support, payment, liability, termination, and ownership.
- [ ] Client confirms authorized point of contact.
- [ ] Third-party processing costs/accounts are assigned clearly.
- [ ] Noirdaz insurance needs reviewed (general liability / technology E&O as appropriate).

## Payment-security boundary

Preferred architecture:
- [ ] Wisconsin Surplus owns its merchant/processor account.
- [ ] Buyer enters card data on processor-hosted checkout.
- [ ] Noirdaz does **not** intentionally store raw PAN/card number, CVV, or magnetic-stripe data.
- [ ] Production secrets are in a secrets manager/environment config, never source control.
- [ ] Webhooks are signature-verified.
- [ ] Payment actions are idempotent to avoid duplicate checkout/payment creation.
- [ ] Logs avoid sensitive data.
- [ ] Admin access uses MFA.
- [ ] Access is least-privilege and revocable.

Square's Checkout API provides a pre-built Square-hosted checkout page:
https://developer.squareup.com/reference/square/checkout-api

Do not promise that using hosted checkout eliminates every PCI/business obligation. Confirm the merchant's responsibilities with the processor.

## Auction/invoice data

- [ ] Document exactly what data leaves the auction system.
- [ ] Minimize copied bidder/customer information.
- [ ] Define retention/deletion periods.
- [ ] Encrypt data in transit (HTTPS).
- [ ] Encrypt sensitive stored data where appropriate.
- [ ] Back up only what must be backed up.
- [ ] Define breach/incident notification contacts.
- [ ] Do not use production data in demos.

## Tax-exempt handling

Wisconsin DOR provides the electronic S-211E exemption certificate workflow:
https://www.revenue.wi.gov/Pages/SalesAndUse/ExemptionCertificate.aspx

Questions for Wisconsin Surplus:
- [ ] Are exemption certificates stored in the auction system, accounting system, or manually?
- [ ] Are exemptions transaction-specific or customer-level?
- [ ] Who is authorized to approve/update tax status?
- [ ] Should online checkout pause until staff confirms the revised amount?
- [ ] Who is responsible for retaining exemption documentation?

Noirdaz should not make tax eligibility decisions. Build the workflow around Wisconsin Surplus's policy/accounting determination.

## Surcharges / service fees

Their current email states a 2.5% fee for credit-card and PayPal payments over $25,000.

Before reproducing this:
- [ ] confirm current processor rules
- [ ] confirm card-network rules
- [ ] confirm applicable state/federal rules
- [ ] confirm debit-card treatment
- [ ] confirm disclosure wording/timing

Square currently documents credit-card surcharge configuration with limits tied to cost of acceptance and network rules:
https://squareup.com/help/us/en/article/8596-set-up-and-manage-card-surcharges

Treat this as an accounting/legal/processor decision owned by Wisconsin Surplus, not a Noirdaz assumption.

## Contracts should address

- scope and acceptance
- implementation milestones
- client responsibilities / access
- fees and payment schedule
- third-party services
- uptime/support language
- maintenance/change requests
- confidentiality
- data ownership
- IP/code licensing or ownership
- security responsibilities
- limitation of liability
- indemnification as appropriate
- warranties/disclaimers
- term/termination
- offboarding/data export
- governing law
- incident contacts

Use an attorney-reviewed template before making this a repeatable Noirdaz service.

## Production-readiness checklist

- [ ] demo approved
- [ ] processor account owned by client
- [ ] sandbox tests complete
- [ ] duplicate-payment protection tested
- [ ] success/failure/cancel paths tested
- [ ] tax-exempt exception tested
- [ ] wrong/expired link behavior tested
- [ ] payment webhook verification tested
- [ ] staff notification tested
- [ ] audit trail tested
- [ ] backups/export tested
- [ ] rollback plan documented
- [ ] support contacts exchanged
- [ ] limited pilot authorized in writing
