# V4 CURRENT - v1.0.0+8 published; P36 re-freeze VERIFIED

Timestamp: 2026-10-19 UTC
Code HEAD: 3d2a73b (pushed 2026-10-19; full suite 523/523 local and CI,
analyze zero issues, format clean)
Docs HEAD: this commit
Phase: **P36 re-freeze VERIFIED at code 3d2a73b / docs this commit.
v1.0.0+8 published (replaces +7 on device). Owner retest: install +8.
One owner action remains: privileged-credential rotation (see
BLOCKED_OWNER). Full record: `handoffs/CONSUMER_READINESS_2026-10-19.md`
+ `handoffs/POST_FREEZE.md` + `handoffs/TAKEOVER.md` +
`handoffs/HOTFIX_AUTH_DEEPLINK.md`.**

Superseded-directive note (do NOT follow the paragraph below):
`governance/OWNER_DIRECTIVE_DEVICE_TESTS.md` once reopened emulator
verification (2026-10-05 deferral LIFTED, P34/P35 open). That reopen is
HISTORICAL and was superseded by the binding 2026-10-14 owner drop
recorded under OWNER DROP NOTICE. P34/P35 stay SUPERSEDED.

## VERIFIED
- P00-P33 VERIFIED (P30/P31/P32/P33 individual closure notes where
  superseded; see the ledger).
- P36 VERIFIED at code `3d2a73b`, release `v1.0.0+8`, 523/523. Earlier
  freeze evidence (v1.0.0+3 era, +6 era, +7 era) is RETAINED AS HISTORY
  in the ledger entry.
- Post-freeze batch committed 2026-10-09 to 2026-10-14: consumer gate
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
  PKCE-exchange ownership + consumed-code guard. Detail:
  `handoffs/HOTFIX_AUTH_DEEPLINK.md`.
- Consumer-readiness batch 2026-10-19 (`3d2a73b`; 523/523 local and CI,
  analyze zero, format clean):
  - Home upcoming-booking card now reads real data: earliest future
    CONFIRMED booking, trip/station lookups and its seat codes; load
    failures render the honest failure card (no "no bookings" lie), and
    the card action says `View my bookings` because it opens the history
    list.
  - Live username availability is retained through EVERY signup entry
    point (`AppGate` welcome, welcome, login, register) via
    `AppDependencies.usernameChecker`; no path silently drops the field.
  - Booking submit has a one-shot in-flight guard (a duplicated payment
    event cannot issue a second booking call).
  - Consumer copy/error gate: auth restore/sign-out/verify/reset map to
    plain language, phone OTP/picker state, GraphQL/search/seat errors,
    board compose/delete/picker, guide WebView, ticket PDF, payment
    simulation status, unknown history status, and AI-key notices no
    longer surface raw exception text or developer wording.
  - New tests: auth error mapping (5), raw phone failure (2); search
    state tests are now date-independent (the hardcoded 2026-10-15
    fixture became past-dated). Full suite **523/523**.
- Demo horizon refreshed 2026-10-19 via the idempotent, owner-only
  `refresh_demo_horizon()` RPC: 648 slots touched; live 24 stations,
  1186 trips, 47,320 seats, horizon 2026-11-08, 1 booking, 3 profiles.

## STATE
- P34 SUPERSEDED - DROPPED BY OWNER 2026-10-14.
- P35 SUPERSEDED - DROPPED BY OWNER 2026-10-14.
- P36 VERIFIED - final freeze at code `3d2a73b` / release `v1.0.0+8`.
  No agent-actionable task remains open; only owner-side items below.

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
- Runtime proof: none required (P34/P35 SUPERSEDED) - not a gap.

## BLOCKED_EXTERNAL
- (none)

## Known backend advisories (observed 2026-10-19; not changed this pass)
- `normalize_username` has a mutable `search_path` (advisor 0011).
- pg_graphql exposes 12 public tables to `anon`/`authenticated` schema
  discovery (advisors 0026/0027). Row access is still RLS-gated; the
  station/trip tables are intentionally part of the GraphQL requirement.
- `bootstrap_new_user()` is executable via RPC by `anon`/`authenticated`
  (advisors 0028/0029); it runs as a signup trigger. A revoke decision
  needs a signup smoke test, so it was not applied in this pass.
- Leaked-password protection is disabled (dashboard setting; owner decision).

## Demo-data state (live, verified 2026-10-19)
- 24 stations, 1186 trips, 47,320 seats (40 per trip), horizon through
  2026-11-08, 1 booking, 3 profiles. `refresh_demo_horizon()` returned 648
  (idempotent slot count) and never writes `booking_id`.
- Horizon is now valid for the app's today..+20 picker window.

## Release state (verified via `gh release list` 2026-10-19)
- `v1.0.0+3` (2026-10-05, `5107c05`) - STALE, do not use.
- `v1.0.0+4` (2026-10-09) - published from the post-cleanup HEAD.
- `v1.0.0+5` (2026-10-13, `87b0892`) - superseded; x86_64 APK used in the
  (now dropped) emulator walkthrough.
- `v1.0.0+6` (2026-10-14, `210ad8a`) - SUPERSEDED, DO NOT INSTALL:
  contains the auth deep-link RouteErrorScreen regression.
- `v1.0.0+7` (2026-10-14, `315b6a9`) - superseded by +8.
- `v1.0.0+8` (2026-10-19, `3d2a73b`, run `39205358414`) - LATEST AND ONLY
  SUPPORTED BUILD: 4 signed APKs + AAB + manifest + SHA256SUMS +
  PROVENANCE. Consumer-readiness batch + refreshed demo horizon.

## Remaining - owner-side only (no agent gate)
1. Install `v1.0.0+8` on the owner device (replaces `+7`).
2. Owner taps a FRESH signup confirmation email on the signup device.
3. Privileged-credential rotation (see BLOCKED_OWNER) - the single
   outstanding owner-only security action.
