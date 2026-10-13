# Private working records

Use neutral IDs and copy templates into approved restricted storage. Public Git contains only blank schemas and explicitly fictional validation examples. Never commit completed client, employee, billing, incident or access records. CSV date fields use ISO 8601; money includes a currency; deadlines include timezone. Escape untrusted spreadsheet text as text, and keep formulas only in trusted calculation columns.

Finance CSV schemas are under `../finance/templates/`; vendor renewals under `../vendors/templates/`. The operational procedures define required approvals and evidence. A row or checkbox cannot authorize a transaction or legal commitment.
