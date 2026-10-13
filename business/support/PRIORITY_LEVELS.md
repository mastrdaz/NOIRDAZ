# Support priorities

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Proposed internal triage model. Fill actual response/update targets and covered hours in the reviewed client exhibit; blanks are not promises. Measure from receipt through the supported route during the defined coverage window unless the contract says otherwise.

| Level | Typical impact | Internal action | Contract fields to complete |
|---|---|---|---|
| P1 critical | Broad production outage, active compromise, likely data loss or payment integrity failure | Notify owner immediately when seen; activate incident response; establish frequent factual updates | [[P1_RESPONSE_TARGET]], [[P1_UPDATE_TARGET]] |
| P2 high | Major workflow unavailable, important users blocked, no practical workaround | Owner assesses business impact and recovery plan during agreed coverage | [[P2_RESPONSE_TARGET]], [[P2_UPDATE_TARGET]] |
| P3 normal | Limited defect, partial degradation or usable workaround | Queue and schedule diagnosis; communicate next step | [[P3_RESPONSE_TARGET]], [[P3_UPDATE_TARGET]] |
| P4 request | How-to, minor cosmetic issue, new feature or planned change | Clarify, estimate and schedule; changes need approval | [[P4_RESPONSE_TARGET]], [[P4_UPDATE_TARGET]] |

A reporter's chosen label is input, not the final classification. Record impact and any priority change with reason; never downgrade to conceal a missed commitment. Security/legal notification triggers can override normal ticket priority. After-hours response exists only if expressly contracted and staffed. Critical alerts without a contracted on-call responder must still have an owner contingency plan.
