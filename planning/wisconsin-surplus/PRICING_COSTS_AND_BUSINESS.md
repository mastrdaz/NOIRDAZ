# Pricing, Cost Model, and Business Plan

All numbers are planning ranges until discovery confirms scope.

## Recommended commercial model

Charge separately for:

1. **Implementation/build**
2. **Managed hosting/support**
3. Payment processing belongs directly to Wisconsin Surplus/their processor, not Noirdaz.

This prevents custom-development work from being hidden inside a very low monthly hosting fee.

## Suggested client options

### Option A - Express Payment Lite
Best when their existing workflow can supply an invoice/payment link with little integration.

**Possible scope**
- branded payment landing page
- secure invoice token/link
- tax-exempt/special handling branch
- processor-hosted checkout
- success/cancel page
- payment notification
- basic monitoring

**Planning price**
- Setup: **$750-$1,500**
- Managed service: **$99-$149/month**

### Option B - Integrated Payment Bridge
Best when Noirdaz must retrieve/validate invoice state and report payment status back.

**Possible scope**
- everything in Lite
- API/export integration
- current-balance validation
- webhook processing
- staff dashboard or richer notification
- audit/event log

**Planning price**
- Setup: **$1,500-$3,500**
- Managed service: **$149-$249/month**

### Option C - Operational Integration
For deeper auction-platform integration, tax-exempt automation, staff roles, reconciliation tools, etc.

**Planning price**
- Build: **$2,500-$7,500+ after discovery**
- Managed service: **$199-$399+/month**

For an early anchor client, Noirdaz may intentionally quote a discounted pilot rate. Show the discount explicitly rather than making custom development appear to be worth $0.

## What Noirdaz likely pays

### Development
Largest cost is founder time. Track hours even if not billing hourly so Noirdaz knows actual project economics.

Example internal planning:
- discovery/design: 4-8 hours
- basic demo: 8-20 hours
- production Lite: 15-35 hours
- integration: +15-60+ hours depending on auction platform

### Hosting
A lightweight portal can be extremely inexpensive.

Cloudflare Workers:
- Free tier exists.
- Paid Workers plan starts at **$5/month per account** and includes substantial usage.
- Static asset requests are free/unlimited under current Workers pricing.
Source: https://developers.cloudflare.com/workers/platform/pricing/

Cloudflare D1:
- free and paid included usage is large relative to a small auction-payment metadata store.
Source: https://developers.cloudflare.com/d1/platform/pricing/

**Planning infrastructure cost for a small portal:** often **$0-$10/month incremental**, excluding third-party monitoring/email services and unusual traffic.

Do not price the service based only on server cost. Monthly pricing pays for:
- availability/monitoring
- updates
- API compatibility
- security maintenance
- backups/configuration
- support
- incident response
- change requests within an agreed allowance

### Payment processing

If Square is chosen:
- Square APIs/SDKs are currently free for developers.
- Online/API card transactions are currently listed at **2.9% + $0.30** per transaction.
- Higher-volume merchants may qualify for custom pricing.
Sources:
- https://developer.squareup.com/us/en/online-payment-apis
- https://squareup.com/us/en/payments/merchant-services

**Recommended:** Wisconsin Surplus creates/owns the Square account and processing agreement. Processing fees are paid directly by Wisconsin Surplus, not marked up or passed through Noirdaz.

Their current winner email says credit-card/PayPal payments over $25,000 are charged an additional 2.5% service fee. Do not assume that policy can simply be copied into a new processor workflow. Confirm processor/card-network and legal rules before automating a surcharge.

## Sample pilot proposal

**Express Payment Pilot**
- Discovery/workflow review: included
- Prototype with test data: included in implementation
- Production setup: **$1,000 pilot rate**
- Managed hosting/support: **$129/month**
- Payment processing: direct between Wisconsin Surplus and its processor
- Initial term: consider month-to-month after setup, or a short 3-month pilot
- Major feature additions quoted separately

This is only an example anchor-client offer; do not quote until scope is known.

## Payment terms for Noirdaz

Suggested:
- 40-50% implementation deposit after scope approval
- balance due before production launch
- recurring service billed monthly in advance
- third-party costs billed directly to client whenever possible
- define late payment, termination, data export, and transition assistance

## Scope boundaries

Monthly managed service should define:
- included support channel
- response target (not an unrealistic guaranteed resolution SLA)
- included minor changes/month, if any
- what counts as billable enhancement work
- ownership of custom code/configuration
- offboarding/export process
- third-party outages/processor outages exclusions
