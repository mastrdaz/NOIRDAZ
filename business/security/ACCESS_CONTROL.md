# Access control

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Maintain a private access register: person, employer/role, client/service/environment, privileges, approver, purpose, grant date, expiry, last review and revocation evidence. The owner approves access; technical assignees implement only the approved scope.

- Named accounts only; separate daily and privileged roles where feasible
- Least privilege and time-limited access for vendors/temporary work
- MFA on email, source control, cloud, registrar, password manager and payment admin wherever supported; prefer phishing-resistant methods
- Separate clients and test/production permissions; no shared super-admin for convenience
- Keep the owner and an approved continuity mechanism able to recover critical company accounts; recovery material stays in the vault
- Client remains owner of client domain/merchant accounts unless an expressly approved arrangement says otherwise
- Review privileged access monthly and all access quarterly; remove stale grants promptly
- Revoke immediately for suspected compromise; use the offboarding plan for departures

Before granting, verify identity through a known channel, confirm client authority where needed, record approval and test the intended role without increasing privileges. New persistent credentials/security-sensitive permissions need the required explicit approval. Failed MFA or an unavailable approver is not a reason to bypass controls.


Reference basis, checked 2026-10-13: [NIST small business cybersecurity resources](https://www.nist.gov/itl/smallbusinesscyber), [NIST SP 800-61r3 incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final), and [FTC small business cybersecurity](https://www.ftc.gov/business-guidance/small-businesses/cybersecurity). These inform the proposed controls; following a checklist is not a certification.
