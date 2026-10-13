# Monitoring policy

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Monitoring detects conditions; it does not itself provide human response or guarantee uptime. Contractual coverage must match the staffed support window and approved escalation route.

For each service define endpoint/journey, expected result, check interval, timeout, failure threshold, notification route, deduplication, maintenance handling and owner. Prefer an external check independent of the hosting failure domain. Monitor TLS/domain expiry, HTTP/service health, resource limits, backup freshness, scheduled-job heartbeat and application errors appropriate to the service.

Proposed starting design: 5-minute uptime checks, consecutive-failure confirmation, TLS/domain reminders at 30/14/7 days, backup alert after the expected window plus documented tolerance. Validate vendor capabilities and costs before adoption; do not claim these checks are already running.

- [ ] Send a test alert before launch and monthly thereafter
- [ ] Verify a human acknowledges and can access the runbook
- [ ] Separate warning, outage and suspected security incident routes
- [ ] Avoid private data, credentials and payment details in alerts/logs
- [ ] Track false positives and missing detections; tune thresholds with evidence
- [ ] Reconcile maintenance exclusions to the executed SLA, if one exists
- [ ] Store monitoring exports and outage intervals for the monthly review

If coverage fails or the only responder is unavailable, tell the owner and arrange approved coverage or reduce the promise. Do not silently substitute vendor uptime statistics for the client's measured service availability.
