# Client credential handling

Version 0.1 · Prepared 2026-10-13 · Proposed operating practice pending owner adoption

Prefer client-owned accounts that invite named Noirdaz users with the minimum necessary role. Record account owner, approved scope, approver, vault reference, expiry and revocation plan privately.

Before access: verify service URL and contact authority; state the data/access needed and purpose; obtain required approval. Use delegated OAuth only with understood scopes and explicit approval for persistent access. Do not ask for a master account when a scoped role will work.

If a client sends a secret through an unsafe channel, do not repeat it. Ask them to rotate/revoke it through a safe channel and use a secure transfer/invitation. Record the exposure without copying the value and assess incident impact. Never store cardholder data, authentication codes or recovery material in client records.

At handover or offboarding: transfer ownership through provider-supported flows, verify receipt, rotate shared secrets, revoke Noirdaz access and record date/evidence. Do not change credentials or remove the client's access without explicit authority. Keep production keys separate from sandbox credentials and verify endpoints before any test.
