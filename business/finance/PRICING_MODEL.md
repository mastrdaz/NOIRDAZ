# Pricing model

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Cost each engagement before quoting. Values in the example workbook are fictional planning assumptions in USD; they do not establish approved rates, processor pricing, wages or permanent service prices. Record the estimate date, owner and supplier evidence privately.

## Cost basis

Setup cost S = sum of discovery, design, development, setup/configuration, migration, testing, documentation, launch-support and legal/admin hours × the relevant loaded hourly rate + approved one-time vendor/setup costs + explicit risk contingency. Loaded labor should include compensation, employer burden and reasonable nonbillable capacity; do not add the same overhead twice.

Monthly non-percentage cost C = hosting + storage + bandwidth + database + backups + monitoring + email + annual domain/license cost ÷ 12 + monthly licenses + support hours × loaded support rate + maintenance/security hours × loaded technical rate + allocated administration/overhead + other recurring costs. Normalize annual charges; do not book them again as monthly expenses in the model. Count founder delivery time even when no salary is paid, to expose sustainable economic cost.

Keep delivery COGS separate from general operating overhead in the accounts. The model's target is a fully loaded contribution margin after explicitly allocated costs; it is not automatically the financial-statement gross margin defined in the KPI guide.

## Price equations

Let m be target margin as a fraction of pre-tax client revenue, r the processor percentage, t the expected sales-tax fraction charged through that processor, c a commission or other variable revenue-based rate, f fixed transaction fee, and n expected charges per period. Let v = r × (1 + t) + c. This simple tax gross-up assumes fees apply to revenue plus tax and commissions apply to revenue excluding tax; use a custom model when the actual agreement differs.

Recommended monthly price P = (C + f × n) ÷ (1 − m − v).
Recommended setup price = (S + f_setup × n_setup) ÷ (1 − m_setup − v_setup).
Internal monthly economic cost at P = C + f × n + v × P.
Internal annual economic cost = 12 × monthly economic cost, for a full 12-month service period.
Realized fully loaded margin = (P − C − f × n − v × P) ÷ P.
Minimum viable price = (C + f × n) ÷ (1 − minimum_margin − v).
Pilot price = approved standard price × (1 − pilot_discount_fraction).

A margin of 40% is not a 40% markup. Markup uses cost as denominator; margin uses revenue. If C=100, fixed fees=0 and v=0, 40% margin requires 166.67, not 140. Percentage fees belong in the denominator when solving price.

## Approval gates

- [ ] All applicable costs and nonbillable work included; missing values remain missing
- [ ] Currency, tax basis, fee basis, billing count and period documented
- [ ] All costs/hours nonnegative; 0 ≤ margin, discount and fee fractions < 1
- [ ] Denominator 1 − m − v is positive; otherwise INVALID, never a zero price
- [ ] Minimum margin ≤ target margin; pilot price ≥ minimum viable floor
- [ ] Pilot has scope, start/end, capped hours and approved post-pilot price
- [ ] Usage/volume/FX/renewal risks and cancellation costs reviewed
- [ ] Capacity and support obligation feasible at the price
- [ ] Owner approves exact quote; client tax classification reviewed before billing

A discount that falls below the floor is blocked in the workbook. An owner may fund a separately documented capped research/pilot budget after discussing its economics, but the template does not approve that spending. Requote when scope or vendor economics materially change.

Use `templates/pricing_calculator.csv` for spreadsheet imports and the editable workbook for formulas. Formula cells must calculate rather than display as text. The CSV is a single-sheet template with no external links/macros. Check the example result against `validation/pricing_expected.json` after import. Do not paste untrusted text beginning with =, +, -, @ into calculation cells; import client text as text to prevent spreadsheet formula injection.
