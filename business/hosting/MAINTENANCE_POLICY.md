# Hosting maintenance procedure

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Maintain a private inventory of runtime/CMS/framework versions, dependencies, licenses and end-of-support dates. The owner approves a client-specific maintenance window and emergency procedure in the agreement.

1. Review vendor/security advisories and identify applicability to the actual environment.
2. Prioritize actively exploited or externally reachable critical flaws for immediate owner assessment; routine updates enter the planned cycle. Document a risk decision and due date rather than pretending every update has the same SLA.
3. Read release notes and compatibility constraints; test on a representative nonproduction environment.
4. Verify a current recoverable backup, rollback path and client communication/approval required by the contract.
5. Apply only authorized changes; record versions, operator, window and affected services.
6. Run essential functional/security/integration smoke tests; monitor errors and resource use.
7. Roll back under the approved criteria or escalate; close with evidence and update the inventory.

Proposed cadence: weekly advisory/dependency review, monthly routine maintenance and quarterly capacity/supportability review. These become operational duties only when assigned and adopted. Major upgrades, end-of-life migrations and client-requested features may need a new SOW/change order; ordinary contracted defect/security obligations remain in scope.
