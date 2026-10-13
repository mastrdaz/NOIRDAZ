# Demo and Workflow Plan

## What we need before building a useful demo

Minimum discovery answers:

- Current invoice/winner-email source
- Existing payment processor
- Example invoice fields (redacted is fine)
- Example winner email
- Rules for tax exemption/special handling
- How staff currently confirms/records payment
- Whether API/export/import access exists
- Approximate invoice/payment volume
- Branding preference: keep existing Wisconsin Surplus appearance or lightly modernize the payment portal

## Do NOT request for the first demo

- production card data
- real customer passwords
- production payment credentials
- unrestricted auction-database access

Use fake invoice/bidder records and the payment processor sandbox where possible.

## Demo scenario A - simplest viable bridge

**Purpose:** prove customer flow without auction-platform integration.

1. Winner clicks **Pay Invoice Online**.
2. Demo link opens invoice summary using a signed demo token.
3. Customer sees:
   - auction ID
   - invoice number
   - masked bidder reference
   - amount due
4. Customer answers:
   - “Is this purchase tax exempt?”
5. If **No**, continue.
6. If **Yes**, show staff-review path.
7. Eligible customer clicks **Continue to Secure Payment**.
8. Redirect to hosted checkout (Square sandbox for demo).
9. Return to Noirdaz/Wisconsin Surplus confirmation page.
10. Demo staff notification records payment success.

### Demo data model

Store only what is required:
- internal transaction/token ID
- external auction/invoice reference
- amount due
- payment eligibility/status
- Square/payment-link reference
- timestamps
- staff notes if required

Avoid copying bidder profiles or unnecessary personal information.

## Demo scenario B - invoice lookup

Use only if a direct email token is not practical.

Lookup inputs might be:
- bidder ID
- invoice ID or auction ID
- ZIP/email verification

Never expose invoices based on bidder ID alone.

## Demo scenario C - future integrated flow

If the auction platform exposes an API:

1. Signed email link identifies invoice.
2. Portal requests current invoice status/amount from auction system.
3. Portal evaluates eligibility.
4. Portal creates hosted checkout link.
5. Processor handles payment.
6. Webhook/payment confirmation arrives.
7. Portal updates Wisconsin Surplus staff/system.
8. Customer sees paid confirmation.

## Suggested presentation structure

### Slide/page 1 - The current friction
“Most of your process already works. The opportunity is to remove the unnecessary phone step for normal card payments.”

### 2 - Preserve the auction workflow
Show the current system unchanged with a small Express Payment layer beside it.

### 3 - Customer experience
Show the 4-5 screen demo.

### 4 - Staff experience
Show:
- exception review
- successful payment notification
- reconciliation/status

### 5 - Security boundary
Emphasize:
- Wisconsin Surplus owns the processor account.
- Square/current provider handles card entry.
- Noirdaz does not store raw card numbers.
- Auction data remains with the existing system wherever practical.

### 6 - Rollout
- sandbox/demo
- staff review
- limited pilot
- production
- optional deeper integration

### 7 - Pricing/support
Fixed implementation fee + managed monthly service.

## Rollout plan

### Phase 0 - Discovery
1 call + redacted samples.

### Phase 1 - Prototype
Fake/test data and processor sandbox.

### Phase 2 - Technical validation
Confirm integration path with auction software/provider.

### Phase 3 - Pilot
A limited auction/payment population if operationally appropriate.

### Phase 4 - Production
Enable standard payment link/workflow.

### Phase 5 - Enhancements
Only if useful:
- dashboard
- invoice synchronization
- automatic tax-exempt workflow
- ACH
- reporting
- staff roles
