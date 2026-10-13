# Recurring revenue tracker

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Maintain `templates/recurring_revenue.csv` privately, one row per client service/subscription. Required fields: neutral client ID, service ID, executed agreement, currency, billing cadence, pre-tax recurring contract value, monthly equivalent, actual service start/end, next billing, renewal, cancellation notice deadline, status, direct cost, owner and last verification.

Monthly equivalent: monthly amount; quarterly amount ÷ 3; annual amount ÷ 12. Exclude setup, taxes, one-time projects, uncommitted usage and pass-through receipts from MRR. Convert currencies using a stated consistent reporting policy; do not add mixed currencies. Pending quotes and signed-but-not-started subscriptions stay separately labeled.

MRR bridge = beginning MRR + new + expansion + reactivation − contraction − churn. Ending MRR must equal the service-level active total under the same period cutoff. Record cancellation effective date rather than deleting the row. Separate contract MRR from invoiced recurring revenue, recognized revenue and cash collection.

Monthly check: match active services to hosting inventory and billing; investigate a running unbilled service or billed terminated service; review 90/60/30-day renewal/notice horizon; verify credits and promotional expiry; confirm one owner for every renewal. Retain an immutable period snapshot.
