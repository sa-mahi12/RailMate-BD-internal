# V4 CURRENT — consumer-readiness + emulator acceptance (reopened)

Timestamp: 2026-10-09 UTC
Code HEAD: e4187b1 (pushed, CI green, 476/476)
Docs HEAD: this commit
Phase: **V4 consumer-readiness + emulator acceptance, reopened by owner directive**

Owner directive now in force:
`governance/OWNER_DIRECTIVE_DEVICE_TESTS.md` — the 2026-10-05 permanent
device deferral is LIFTED and replaced by Android Emulator verification
(`ANDROID_EMULATOR_RUNTIME_PROOF`). P34/P35 are open again. The final line
must always read: "Verified on Android Emulator; physical-device
verification not performed."

## VERIFIED
- P00–P33 except P30/P31/P32/P33 individual closure notes where superseded;
  see the ledger. P36's earlier freeze evidence is RETAINED AS HISTORY but
  P36 itself is back to TODO (it depends on P35).

## IN_PROGRESS / READY
- P34 READY (coordinator): emulator runtime verification.
- P35 TODO: emulator screenshot pass after P34.
- P36 TODO: final freeze after P35.

## BLOCKED_OWNER
- SMS provider (carried from V3; phone OTP honestly reports unavailability).
- Social login: unimplemented by design; the UI must stop advertising it.
- Physical-device verification: explicitly NOT required; document the gap.

## BLOCKED_EXTERNAL
- (none)

## Demo-data state (live, verified 2026-10-05)
- 24 stations, 32 service codes, 726 demo trips, 29,080 seats, all trips
  40 seats, occupancy avg 57.5% (0–85%). Horizon idempotent (648, zero
  churn). Board empty by policy. 0 profiles / 0 bookings.
- NOTE: horizon needs re-running (`refresh_demo_horizon()`) before it
  expires ~2026-10-24.

## Release state
- Latest published: **v1.0.0+3 → commit 5107c05 (STALE)**. Do NOT use as
  final runtime proof. V4 HEAD is e4187b1 with later fixes.
- Next: publish **v1.0.0+4** (or higher) from the post-cleanup HEAD and use
  its **x86_64 APK** on the emulator.

## Exact next sequence
1. Consumer-readiness/source audit (no raw UUIDs, no internal codes, no
   "Setup required", no dead/coming-soon controls, no raw exceptions).
2. Genuine wiring fixes: Board comments entry point; password-recovery
   deep link + session handling; profile/username bootstrap if live DB
   proves it missing; useful booking history/details.
3. Consumer-behavior sweep: keyboard, back, retry, double-submit,
   confirm-destructive, session restore, restart, wording.
4. Fresh signed release from the new HEAD (monotonic build number).
5. Emulator walkthrough on the release x86_64 APK (Pixel-class API 35 AVD,
   data cleared, full consumer journey).
6. Screenshot-based visual review; fix only defects found.
7. P34 VERIFIED (`ANDROID_EMULATOR_RUNTIME_PROOF`) → P35 VERIFIED →
   P36 final freeze.
