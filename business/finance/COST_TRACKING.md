# Cost tracking

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Keep one private cost ledger keyed by client/project/service and supplier invoice ID. Record estimates separately from actuals; never overwrite the original estimate to make variance disappear.

## Weekly delivery update

- [ ] Enter time by phase: discovery, design, development, setup, migration, testing, documentation, launch and legal/admin
- [ ] Add approved vendor costs, receipt link, payer, currency and tax treatment
- [ ] Normalize recurring costs to month; preserve original billing cadence and renewal date
- [ ] Allocate shared infrastructure by a documented driver such as measured storage or client count; allocations must sum to the supplier total
- [ ] Record support/maintenance hours and incidents that exceed allowance
- [ ] Update remaining work and expected final cost; flag variance before it consumes margin
- [ ] Distinguish pass-through reimbursables, client-paid costs, COGS and operating overhead with the bookkeeper

Actual margin uses actual recognized revenue and matching costs for the same period. Cash received, invoiced sales and revenue recognized are not interchangeable. The CPA/bookkeeper determines the accounting method and principal/agent treatment for resold services.

CSV fields are in `templates/cost_ledger.csv`; the header is an import schema, not permission to put completed data in Git. Duplicate supplier invoice/line IDs are blocked or investigated in the private ledger. Store original-currency amount and conversion basis when billing is not USD. Quarterly, compare modeled support hours, usage and provider renewals to actuals and adjust new quotes or contract-authorized renewal pricing.
