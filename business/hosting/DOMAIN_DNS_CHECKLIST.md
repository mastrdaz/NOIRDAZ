# Domain and DNS change checklist

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

A record is preparation; no domain transfer, purchase or DNS change is authorized by this checklist.

## Before an approved change

- [ ] Verify registrant/account owner and requester authority independently
- [ ] Record registrar, DNS provider, expiry, auto-renew/payment owner and lock status
- [ ] Export the existing zone privately and identify web, MX/email, SPF, DKIM, DMARC, verification and subdomain dependencies
- [ ] Record present values and TTLs; plan propagation and cached-client behavior
- [ ] Agree exact records, change window, expected disruption and rollback values
- [ ] Confirm destination server/TLS readiness before switching traffic
- [ ] Protect transfer authorization codes as credentials; use secure handoff
- [ ] Owner and client approve exact change; vendor renewal/transfer charges separately approved

## After execution by an authorized operator

- [ ] Check authoritative and independent recursive resolution
- [ ] Verify website/TLS, mail delivery and required verification records
- [ ] Record start/end, results, operator and any propagation issues
- [ ] Restore normal TTL when planned and verify monitoring
- [ ] Retain zone/version history privately; update renewal calendar and account owner

A domain transfer and a DNS change are different actions. Do not move registration just to point a site, and do not remove mail records during a website cutover.
