# Passwords and secrets

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Use an approved password manager for unique generated passwords, recovery codes and shared organizational credentials. Access is role-based; share a vault item/invitation rather than plaintext. Never store secrets in Git, Markdown, spreadsheets, tickets, email, screenshots, build logs or chat.

Application credentials live in the authorized runtime secret store. Use narrowly scoped, client/environment-specific credentials with expiry where supported. Do not create or upload persistent credentials without the required approval. Keep credential references and owners in the private inventory; never the values.

Rotate on suspected exposure, access departure involving shared secrets, vendor-required expiry or a documented security need. Avoid unsupported blanket password-reset schedules that encourage weak choices. Test replacements safely, revoke the old credential and record evidence without values. A leaked secret must be revoked/rotated and incident-reviewed; deleting a Git file does not remove history or invalidate the secret.

Enable MFA and safe recovery, restrict exports, lock devices, patch endpoints and avoid pasting credentials into unverified domains. Do not collect a client's password in chat; use supported secure login or invitation mechanisms. Never bypass a browser security warning.


Reference basis, checked 2026-10-13: [NIST small business cybersecurity resources](https://www.nist.gov/itl/smallbusinesscyber), [NIST SP 800-61r3 incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final), and [FTC small business cybersecurity](https://www.ftc.gov/business-guidance/small-businesses/cybersecurity). These inform the proposed controls; following a checklist is not a certification.
