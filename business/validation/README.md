# Validation scope

Prepared 2026-10-13. Checks establish document-package consistency, not legal approval or operational compliance.

## Reproduce source checks

From any directory run Python 3 against business/validation/validate_business.py. Optionally supply the path to Noirdaz-Pricing-and-Trackers.xlsx as its first argument. The script is read-only and uses the Python standard library. It checks relative links, placeholder registration, the 12-template inventory and signature fields, blank public CSV trackers, independent Decimal pricing arithmetic, and exact original-file Git blob hashes. With the workbook it also compares formula text and checks cached errors, macros and external-link components.

The preservation manifest pins main at ba94af23c3cf7092b983f4b85bcf55dfef2240fe and its original tree. Original README/docs/planning files are preserved byte-for-byte, including Wisconsin Surplus planning. Existing website work remains separate. The release is additive under business/.

## Spreadsheet checks performed

The editable workbook was authored/recalculated with the artifact spreadsheet engine. Tests cover the fictional base scenario, annual cost normalization, percentage and fixed fees, processor fees on tax, commissions, invalid denominators, missing versus zero inputs, zero candidate price, below-floor pilot, and the zero-only setup annual-cost field. Expected results are in pricing_expected.json. Independent review recomputed prices using Decimal and compared the exported XLSX with CSV formulas. No formula errors appeared in the final engine scan or exported caches.

Interactive Microsoft Excel and Google Sheets behavior was not tested. After importing CSV, verify that formulas calculate rather than display as text and compare the example results. Locale/import settings can change formula interpretation. The workbook has no macros, external connections or external formula links in the checked export.

## Document and privacy checks

All legal source fields are registered, signatures are present on operative instruments, and decision/research notes are separate. Editable legal Word files contain tagged plain-text fields, not functioning signature requests. The exported files are rendered and visually reviewed before delivery; the package manifest records outputs and checks. Source Markdown remains authoritative for this draft version.

Public files contain blank templates and explicitly fictional economic examples. A bounded scan checks common credential/identity patterns; it is not a complete repository-history secret audit. Completed records must remain in private storage regardless of whether a scanner detects them.

## Review limits

Counsel must determine enforceability, applicability and all final legal terms. CPA/payroll reviewers must determine taxes, reporting, classification and due dates. The broker must verify actual coverage. No client service, backup, alert, account, payroll, DNS change, deployment, transaction or automation was activated by producing this package.
