# Shared placeholder reference

All source fields use [[UPPER_SNAKE_CASE]]. Fill working copies privately. The same field name means the same kind of information throughout; its value belongs to a specific client/project/document instance. Never perform an unscoped global replacement across unrelated clients.

Editable legal DOCX files use tagged plain-text Word content controls whose visible labels match these source fields. Repeated controls are not automatically synchronized by Word; update every occurrence and run the final placeholder search. Content controls are editing aids, not electronic signatures or validation. Do not insert actual signature images or execute agreements through the draft pack.

Every field is required for a complete execution copy unless its drafting instruction allows an explicit “None” or “Not applicable.” A blank liability, term, service-level or price choice must not be treated as zero or a harmless default. Resolve terms through the owner/counsel decisions register; attach referenced schedules in immutable agreed versions.

## Canonical cross-document fields

| Field | Meaning and completion rule |
|---|---|
| PROVIDER_LEGAL_NAME | Exact verified contracting person/entity. Do not assume Noirdaz is an LLC. |
| PROVIDER_ENTITY_TYPE | Verified legal form; counsel confirms signing capacity. |
| PROVIDER_ADDRESS | Provider notice/business address approved for the contract. |
| PROVIDER_NOTICE_EMAIL | Verified contractual notice route, distinct from billing/support. |
| CLIENT_LEGAL_NAME | Exact verified client legal party, not only a trading name. |
| CLIENT_ENTITY_TYPE | Verified client form and authority. |
| CLIENT_ADDRESS | Client contractual address; billing address can differ and is recorded separately. |
| CLIENT_NOTICE_EMAIL | Verified contractual notice route. |
| CLIENT_SIGNATORY_NAME | Authorized human signer; verify capacity. |
| EFFECTIVE_DATE | Date agreed in the particular instrument; not necessarily signature or launch date. |
| MSA_DATE | Date identifying the executed master agreement adopted by the order. |
| SOW_ID | Stable order identifier; match every addendum/change/acceptance. |
| PROJECT_NAME | Human-readable project name used consistently across one engagement. |
| CURRENCY | ISO currency code; avoid mixing currencies in totals. |
| SUPPORT_COVERAGE_HOURS | Actual staffed coverage and timezone; not monitoring interval. |
| SLA_EXHIBIT_REFERENCE | Exact executed SLA version or explicit None; no default uptime guarantee. |
| GOVERNING_STATE | Counsel-approved governing law choice; Wisconsin-first does not fill it. |
| VENUE_COUNTY_STATE | Counsel-approved dispute venue. |
| CLIENT_ID | Neutral private client identifier; never a tax or government identifier. |
| PROJECT_ID | Stable private project identifier. |
| VAULT_REFERENCE | Private password-manager item reference only; never a secret value. |

## Complete references

The legal suite's [placeholder reference](legal/PLACEHOLDER_REFERENCE.md) defines the contract fields and owners. The generated [field catalog](validation/field_catalog.json) lists every field and exact source occurrence across business documents. It is a navigation/validation aid, not a repository for filled values.

Dates use YYYY-MM-DD unless a contract requires another format; incident/deadline timestamps include timezone. Amounts include currency and tax treatment. Percentages state their denominator. Use plain text for short fields and a titled attached schedule for long scope, price, security or retention fields. Do not shrink large schedules into a line of contract text.

Before use: verify identity/authority; reconcile repeated fields; remove unused alternatives only after decision; attach all referenced schedules; search for remaining double brackets plus obsolete aliases; confirm numbers/dates/notice deadlines; confirm approved draft version; obtain the appropriate review and execution approvals.
