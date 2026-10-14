# V4 CURRENT — post-freeze fixes synced; P36 freeze pending

Timestamp: 2026-10-14 UTC
Code HEAD: b4f008d (pushed 2026-10-14; full suite 503/503 local, analyze + format clean)
Docs HEAD: this commit
Phase: **Post-freeze batch committed; owner dropped all runtime verification; P36 freeze pending. Full record: `handoffs/POST_FREEZE.md`.**

Owner directive now in force:
`governance/OWNER_DIRECTIVE_DEVICE_TESTS.md` — the 2026-10-05 permanent
device deferral is LIFTED and replaced by Android Emulator verification
(`ANDROID_EMULATOR_RUNTIME_PROOF`). P34/P35 are open again. The final line
must always read: "Verified on Android Emulator; physical-device
verification not performed."

## VERIFIED
- P00–P33 except P30/P31/P32/P33 individual closure notes where superseded;
  see the ledger. P36's earlier freeze evidence is RETAINED AS HISTORY but
  P36 itself is TODO (no runtime gate in front of it anymore).
- Post-freeze batch committed 2026-10-09 → 2026-10-14: consumer gate
  (`a598fcb`), board comments (`e75584a`), reset deep link (`3217b45`),
  username claim trigger (`27c6b2b`), signup bootstrap (`e34b67b`),
  emulator findings (`87b0892`), signup localhost fix (`b4f008d`;
  503/503 green). Detail: `handoffs/POST_FREEZE.md`.

## IN_PROGRESS / READY
- P34 SUPERSEDED — DROPPED BY OWNER 2026-10-14.
- P35 SUPERSEDED — DROPPED BY OWNER 2026-10-14.
- P36 TODO: final freeze (no runtime gate in front of it anymore).

## OWNER DROP NOTICE (2026-10-14, binding on reviewers)
Device verification AND emulator verification are both dropped completely.
No phone, emulator, screenshot-pack, or runtime proof of any kind is
required, expected, or to be requested. Do not treat their absence as a
gap: it is an explicit owner decision, recorded in the ledger (P34/P35
SUPERSEDED). The emulator walkthrough started 2026-10-13/14 was stopped
mid-journey (Booking Review) and will not resume.

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

## Release state (verified via `gh release list` 2026-10-14)
- `v1.0.0+3` (2026-10-05, `5107c05`) — STALE, do not use.
- `v1.0.0+4` (2026-10-09) — published from the post-cleanup HEAD.
- `v1.0.0+5` (2026-10-13, `87b0892`) — latest; x86_64 APK installed on the
  emulator during the (now dropped) walkthrough.
- No release cut from `b4f008d` yet; cut one only if/when code changes
  again or a fresh installable is wanted (monotonic build number).

## Exact next sequence
1. Consumer-readiness/source audit (no raw UUIDs, no internal codes, no
   "Setup required", no dead/coming-soon controls, no raw exceptions).
2. Genuine wiring fixes: Board comments entry point; password-recovery
   deep link + session handling; profile/username bootstrap if live DB
   proves it missing; useful booking history/details.
3. Consumer-behavior sweep: keyboard, back, retry, double-submit,
   confirm-destructive, session restore, restart, wording.
4. Fresh signed release from the new HEAD (monotonic build number).
5. ~~Emulator walkthrough~~ DROPPED 2026-10-14 (see drop notice above).
6. ~~Screenshot-based visual review~~ DROPPED 2026-10-14.
7. P36 final freeze (directly; P34/P35 SUPERSEDED).
