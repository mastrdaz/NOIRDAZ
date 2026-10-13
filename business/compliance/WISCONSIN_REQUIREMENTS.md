# Wisconsin requirements and review gates

Status: research and operating checklist, not legal or tax advice or a finding that Noirdaz complies. Sources checked 2026-10-13. Owner: [[COMPLIANCE_OWNER]]. Review with [[CPA_CONTACT]], [[COUNSEL_CONTACT]], and [[INSURANCE_CONTACT]] before implementation. Recheck whenever facts or rules change.

## Establish the facts first

- [ ] Confirm [[PROVIDER_LEGAL_NAME]], [[PROVIDER_ENTITY_TYPE]], [[FORMATION_JURISDICTION]], [[FORMATION_DATE]], [[TAX_CLASSIFICATION]], and actual operating/work locations. “Noirdaz Industries” alone does not establish an LLC or tax election.
- [ ] Record registration evidence and tax-account access in [[PRIVATE_COMPLIANCE_RECORD_LOCATION]]. Keep identifiers, returns, ownership records, employee files, and payment details out of this repository.
- [ ] Owner approves [[COMPLIANCE_CALENDAR_OWNER]] and a backup. Calendar entry means scheduled, not filed; retain agency acceptance and payment evidence separately.
- [ ] Have local city/county officials or counsel check applicable zoning, home-business, licensing, and permit requirements for [[BUSINESS_LOCATION]]. State entity registration does not resolve local requirements.

## Entity and federal ownership reporting

| Topic | Verified general rule or trigger | Action and evidence |
|---|---|---|
| Wisconsin DFI annual report | For covered domestic entities, report in each year after registration during the registration-anniversary quarter; due March 31, June 30, September 30, or December 31. Foreign entities registered in Wisconsin generally report in Q1 of subsequent years. | Confirm entity type and DFI record, registered agent/address, actual due date, filing method and fee. Save receipt. Do not assume every business is an LLC. [DFI FAQ](https://dfi.wi.gov/Pages/BusinessServices/BusinessEntities/FAQ.aspx) |
| FinCEN BOI | Current FinCEN guidance exempts entities created in the United States and their beneficial owners. Certain foreign-country-created entities registered in the U.S. remain within reporting rules unless exempt. | Counsel confirms place of creation and current rule. A company formed in another U.S. state is not foreign-country-created merely because Wisconsin calls it foreign. Do not put an automatic BOI filing on every LLC calendar. [FinCEN](https://www.fincen.gov/boi) |
| Tax identity and returns | Legal form and federal/state tax treatment can differ. | CPA determines EIN requirements, returns, fiscal year, owner compensation treatment, estimated payments and reserves. No tax election, payroll treatment or percentage is selected here. |

## Before the first employee

| Topic | Verified general rule or trigger | Required review |
|---|---|---|
| Wisconsin withholding | An employer required to withhold Wisconsin income tax must register for a Wisconsin withholding account. Employee work location/residence and exceptions matter. | CPA/payroll provider determines account registration, WT-4/W-4 forms, reciprocity evidence, assigned filing frequency, WT-6 and WT-7 obligations. [DOR withholding](https://www.revenue.wi.gov/Pages/FAQS/pcs-with.aspx) |
| Unemployment insurance | Commercial-employer triggers include at least $1,500 wages in a calendar quarter, or employment during some part of a day in at least 20 weeks in a calendar year, including part-time work. FUTA liability, acquisition and voluntary coverage can create other triggers. Coverage generally reaches back to January 1 of the year a liability condition is met. | Assess before hiring, register when required, and preserve payroll from the start. Account-specific rate comes from DWD; no generic rate is assumed. [DWD coverage](https://dwd.wisconsin.gov/ui201/t1201.htm) |
| Workers’ compensation | General Wisconsin triggers: three full- or part-time employees, with coverage that day; or $500 combined gross wages in a calendar quarter for Wisconsin work, with coverage by the 10th day of the next quarter’s first month. | Insurer confirms counting/exceptions, owner treatment, prior coverage and actual effective date. Once subject, ongoing/restarted employment can require coverage immediately. Verify Wisconsin appears in policy section 3-A. [DWD insurance](https://dwd.wi.gov/dwd/publications/wc/wkc-13328-p.htm) |
| Worker classification | Wisconsin UI and workers’ compensation use their own tests; federal employment-tax treatment is separate. A contract, LLC, commission-only label or Form 1099 is not a determination. | Document actual control, duties, equipment, business independence and relationship; CPA/counsel reviews all applicable tests. [DWD classification](https://dwd.wisconsin.gov/worker-classification/classification-determination.htm), [IRS](https://www.irs.gov/taxtopics/tc762) |
| Employment eligibility and new hires | See the timed checklist in [Employee onboarding](../employees/EMPLOYEE_ONBOARDING.md). | Assign I-9 reviewer and new-hire reporting owner before start; retain restricted evidence. |
| Wage and employment policies | Minimum wage, overtime, work-time recording, wage statements, final pay, discrimination protections and applicable posters require review even for a small team. | Counsel approves classification, pay/commission/PTO policies, notices, accommodation/reporting path and any benefits duties. Do not presume salary, software work, or sales work creates an overtime exemption. [DWD overtime](https://www.dwd.wisconsin.gov/er/laborstandards/overtime.htm), [posters](https://www.dwd.wisconsin.gov/dwd/workplace-posters/) |

Use [Payroll setup](../employees/PAYROLL_SETUP_CHECKLIST.md) before any payroll is activated. Budgeted wages or software are not authorization to debit funds.

## Service tax review before quoting

Wisconsin treatment turns on the actual transaction. Have the CPA map every SKU, bundle, implementation charge and renewal to a written determination. The following is a screening summary of [DOR’s computer and cloud guidance](https://www.revenue.wi.gov/Pages/FAQS/pcs-computerc.aspx):

- Prewritten software sold, licensed or downloaded is generally taxable; calling a product “custom” does not decide its treatment.
- Writing non-prewritten software and qualifying separately stated purchaser-specific modifications have different treatment.
- Pure website hosting, domain registration, and maintenance can be nontaxable when no taxable property, digital good or taxable service is supplied.
- Hosted software/data-processing access can be nontaxable under DOR’s conditions; downloaded software, customer control of equipment, taxable outputs/services and bundles can change the result.

For Basic Website, Managed Website, Managed Hosting, custom applications, Sync Coverage, automation and payment integrations, record:

| Field | Entry |
|---|---|
| Service and deliverable | [[SERVICE_SKU]] / [[DELIVERABLE_DESCRIPTION]] |
| Rights and delivery | [[SOFTWARE_RIGHTS_AND_DELIVERY_METHOD]] |
| Customer and use locations | [[CUSTOMER_USE_JURISDICTIONS]] |
| Components and separate charges | [[BUNDLE_AND_LINE_ITEM_ANALYSIS]] |
| Written CPA conclusion and authority | [[TAX_REVIEW_REFERENCE]] |
| Seller permit, rate sourcing, exemption and use-tax handling | [[TAX_CONFIGURATION_DECISION]] |
| Effective date and next review | [[TAX_DECISION_DATE]] / [[NEXT_REVIEW_DATE]] |

Check seller-permit requirements before taxable sales, exemption evidence before applying an exemption, and use tax on purchases. Do not hard-code one statewide tax rate. [DOR sales and use tax tools](https://www.revenue.wi.gov/Pages/SalesAndUse/Home.aspx).

## Records and recurring review

- IRS employment-tax records: generally retain at least four years after tax becomes due or is paid, whichever is later. Certain credits require longer. [IRS retention](https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records)
- FLSA guidance generally specifies three years for payroll records and two for wage-calculation records; apply any longer state, contract, tax or litigation requirement. [DOL recordkeeping](https://www.dol.gov/agencies/whd/fact-sheets/21-flsa-recordkeeping)
- I-9s: retain while employed and until the later of three years after hire or one year after termination. Restricted storage, separate from ordinary personnel files, is the operating choice. [USCIS retention guidance](https://www.uscis.gov/sites/default/files/document/guides/E3en.pdf)
- CPA/counsel assigns [[RETENTION_SCHEDULE_REFERENCE]]. Suspend deletion for a claim, audit, investigation or legal hold. Never use one blanket retention period for all files.
- Federal 1099-NEC thresholds changed for 2026 payments; CPA checks current federal rules, payment-channel exceptions, backup withholding and Wisconsin requirements separately. [IRS information returns](https://www.irs.gov/businesses/small-businesses-self-employed/am-i-required-to-file-a-form-1099-or-other-information-return)
- Insurance review covers workers’ compensation, technology E&O, cyber, general liability, equipment and any client-required endorsements. No coverage, policy limit or insurability is assumed.

## Release gate

Owner records unresolved items, responsible reviewer and due date in the private compliance log. Hiring, a new state, taxable product launch or contract promise waits for the relevant review. Research completion is not professional approval. See [source register](OFFICIAL_SOURCE_REGISTER.md).
