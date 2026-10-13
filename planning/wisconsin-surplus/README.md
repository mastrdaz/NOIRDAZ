# Wisconsin Surplus - Express Payment / Auction Workflow Lead

**Status:** Discovery / prospective client  
**Owner:** Noirdaz Industries  
**Last updated:** 2026-10-13

## Opportunity

Wisconsin Surplus currently sends winning bidders an invoice/winner email and directs many customers to call the office to pay by credit card, reply if a card is already on file, send PayPal, wire funds, mail guaranteed funds, or pay in person.

The opportunity is **not** to replace their auction platform. The initial Noirdaz proposal is a lightweight, secure **Express Payment bridge** that preserves their existing auction workflow while giving eligible bidders a self-service payment option.

### Core concept

```
Existing auction/invoice system
        |
        | invoice / auction / bidder reference
        v
Wisconsin Surplus Express Payment Portal
        |
        +--> exception / tax-exempt / special handling --> staff review
        |
        +--> eligible invoice
                 |
                 v
        hosted payment checkout
        (Square or their existing processor)
                 |
                 v
              payment
                 |
          +------+------+
          |             |
          v             v
     buyer receipt   Wisconsin Surplus
                     payment confirmation
```

## Design principles

1. **Do not replace what already works.**
2. **Do not collect or store raw card data at Noirdaz.**
3. Prefer a processor-hosted checkout page.
4. Keep auction data with Wisconsin Surplus/their existing platform whenever possible.
5. Make exceptions explicit: tax exemption, wire arrangements, high-dollar review, etc.
6. Give staff an escape hatch and customers a phone option.
7. Start with the smallest useful integration, then deepen only if the client wants it.

## Likely v1

- Add **Pay Online / Express Payment** to the existing winner email.
- Best case: use a unique signed link tied to the invoice.
- Fallback: bidder ID + invoice/auction number + second verification factor.
- Show invoice summary and amount due.
- Ask gating questions such as tax-exempt status.
- Eligible customers continue to a processor-hosted checkout.
- Staff receive payment confirmation by email/dashboard/export/API.
- Customer receives confirmation and pickup instructions.
- Tax-exempt/special cases are routed to staff.

## Important security decision

**Bidder ID alone should not expose an invoice.** Prefer a signed one-time/limited token in the email. If manual lookup is required, use additional verification.

## Processor philosophy

Ask what they use now before proposing a switch.

If the existing processor supports hosted checkout/payment links/API, integrate it.

If not, Square is a reasonable option because its Checkout API creates Square-hosted checkout pages and Square handles the card-entry/payment surface.

Current Square reference:
- Checkout API: https://developer.squareup.com/reference/square/checkout-api
- Create Payment Link: https://developer.squareup.com/reference/square/checkout/create-payment-link
- Current online/API pricing reference: https://developer.squareup.com/us/en/online-payment-apis

## Package contents

- [DISCOVERY_QUESTIONS.md](DISCOVERY_QUESTIONS.md)
- [DEMO_AND_WORKFLOW.md](DEMO_AND_WORKFLOW.md)
- [SALES_CALL_SCRIPT.md](SALES_CALL_SCRIPT.md)
- [PRICING_COSTS_AND_BUSINESS.md](PRICING_COSTS_AND_BUSINESS.md)
- [LEGAL_SECURITY_CHECKLIST.md](LEGAL_SECURITY_CHECKLIST.md)

## Next action

If Wisconsin Surplus calls back:

1. Run the discovery questions.
2. Ask permission to build a non-production demo with fake/test data.
3. Do not request production credentials during the first call.
4. Prepare 2-3 options:
   - simple payment-link workflow
   - integrated invoice lookup/payment bridge
   - deeper platform integration if their auction system supports it
5. Present a fixed setup price plus monthly managed-service price.
6. Only move to production after written scope, payment terms, responsibilities, and data/security boundaries are approved.
