# V4 CURRENT — v1.0.0+7 published; P36 re-freeze VERIFIED

Timestamp: 2026-10-14 UTC
Code HEAD: 315b6a9 (pushed 2026-10-14; full suite 516/516 local, analyze zero
issues, format clean)
Docs HEAD: this commit
Phase: **P36 re-freeze VERIFIED at code 315b6a9 / docs this commit.
v1.0.0+7 published (replaces the buggy +6 on device). Owner retest: install
+7, tap a FRESH confirmation email on the signup device. One owner action
remains: privileged-credential rotation (see BLOCKED_OWNER). Full record:
`handoffs/POST_FREEZE.md` + `handoffs/TAKEOVER.md` +
`handoffs/HOTFIX_AUTH_DEEPLINK.md`.**

Superseded-directive note (do NOT follow the paragraph below):
`governance/OWNER_DIRECTIVE_DEVICE_TESTS.md` once reopened emulator
verification (2026-10-05 deferral LIFTED, P34/P35 open). That reopen is
HISTORICAL and was superseded by the binding 2026-10-14 owner drop
recorded under OWNER DROP NOTICE. P34/P35 stay SUPERSEDED.

## VERIFIED
- P00–P33 except P30/P31/P32/P33 individual closure notes where superseded;
  see the ledger. P36's earlier freeze evidence is RETAINED AS HISTORY but
  P36 itself is TODO (no runtime gate in front of it anymore).
- Post-freeze batch committed 2026-10-09 → 2026-10-14: consumer gate
  (`a598fcb`), board comments (`e75584a`), reset deep link (`3217b45`),
  username claim trigger (`27c6b2b`), signup bootstrap (`e34b67b`),
  emulator findings (`87b0892`), signup localhost fix (`b4f008d`;
  503/503 green). Detail: `handoffs/POST_FREEZE.md`.
- Takeover batch 2026-10-14: link-first verify UI + 3 widget tests
  (`0489e61`; 506/506 green), release-gate analyze fix (`210ad8a`;
  zero issues), tracked `app.env.json` removed from HEAD (rotation still
  owed, see BLOCKED_OWNER). Detail: `handoffs/TAKEOVER.md`.
- Auth deep-link hotfix 2026-10-14 (`315b6a9`; 516/516 green):
  `flutter_deeplinking_enabled=false`, `/auth/*` defensive routes, single
  PKCE-exchange ownership + consumed-code guard. The `v1.0.0+6` build
  contains the RouteErrorScreen regression and must be replaced on device
  by `v1.0.0+7`. Detail: `handoffs/HOTFIX_AUTH_DEEPLINK.md`.

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

## OWNER-COMPLETED SUPABASE WORK (2026-10-14, reported by owner)
- Dashboard URL/deep-link configuration for signup + password reset: DONE.
  Expected callbacks `railmatebd://auth/verify`, `railmatebd://auth/reset-password`.
- Deliberate owner choice: NO custom domain, NO custom SMTP; default mailer
  retained. Production signup verification is therefore confirmation-link
  based. Do NOT list `{{ .Token }}` template editing as an owner task, and
  do NOT ask the owner for domain/SMTP work.
- App aligned in code `0489e61`: link-first verify UI, no 6-digit signup
  OTP promise; `verifyCode`/`verifyEmailOtp` kept as a dormant seam only.

## BLOCKED_OWNER
- SMS provider (carried from V3; phone OTP honestly reports unavailability).
- Social login: unimplemented by design; the UI must stop advertising it.
- Privileged credential rotation: the tracked `app.env.json` was removed
  from code HEAD in `0489e61`, but the exposed legacy credential stays valid
  until rotated dashboard-side. OWNER ACTION: rotate/invalidate the legacy
  key, update the hosted `SUPABASE_SERVICE_ROLE_KEY` secret for the
  `book-trip` + `cancel-booking` Edge Functions, redeploy/verify them, and
  only then treat the exposed copy as dead. No history rewrite needed once
  the key is invalid. (Secret value never recorded in docs.)
- Runtime proof: none required (P34/P35 SUPERSEDED) — not a gap.

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
- `v1.0.0+6` (2026-10-14, `210ad8a`) — LATEST. Signed 4 APKs
  (arm64-v8a, armeabi-v7a, universal, x86_64) + AAB + release-manifest +
  SHA256SUMS + PROVENANCE. Contains the link-first verify UI and the
  `app.env.json` removal.
- `v1.0.0+7` (2026-10-14, `315b6a9`) — LATEST. Auth deep-link hotfix build:
  4 signed APKs + AAB + manifest + SHA256SUMS + PROVENANCE. `v1.0.0+6`
  contains the RouteErrorScreen regression — replace it on device.

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
