# Consumer-readiness batch - 2026-10-19

Status: COMMITTED on `main` in both repositories, pushed, and released.
No branches, no PRs, no force-pushes. This closes the gap between the
2026-10-14 re-freeze (code `315b6a9`, `v1.0.0+7`) and current HEAD.

## 1. Code commit

| Commit | Change | Evidence |
|---|---|---|
| `3d2a73b` | Consumer gate, batch A+B: real upcoming-booking wiring (`fetchTripById`/`fetchStationById`/`fetchBookingSeatCodes`), username checker forwarded through every signup entry point, one-shot booking-submit guard, and raw-error/developer-copy removal across auth, phone, GraphQL, search, seats, board compose, guide WebView, ticket PDF, payment status, history and AI settings | `dart format` clean; `flutter analyze --no-pub` -> **No issues found**; full suite **523/523** |

### What was actually broken and fixed

- **Home upcoming card was a permanent empty state.** `_loadNextUpcomingBooking`
  returned null even when the signed-in user had a confirmed booking, and the
  card's `View ticket / details` action actually opened the history list.
  It now resolves the earliest future CONFIRMED booking (trip, station labels,
  seat codes); failures propagate to the honest "could not load" card, and
  the action reads `View my bookings`.
- **Live username availability vanished on some signup paths.** Only the
  central `/register` route built a checker; `AppGate` welcome, welcome and
  login pushed `RegisterScreen` without one. All entry points now share
  `AppDependencies.usernameChecker`.
- **Booking submit had no in-flight guard.** A duplicated payment callback
  can no longer issue a second booking request.
- **Raw exception/developer text could reach consumers.** Auth restore/sign
  out/verify/reset, phone OTP errors, GraphQL and search failures, seat
  loading, board submit/delete/picker, guide WebView failure, ticket PDF,
  payment `unknown` status, unknown booking status and AI-key notices now
  render plain-language copy; codes stay in exceptions/logs.
- **AI key screen lied about connectivity.** Saving to secure storage showed
  `Connected successfully.` and the test-connection success echoed arbitrary
  model output. Both now say what actually happened (`Key saved on this
  device.` / `Connection test succeeded.`).
- **Date-dependent tests had silently expired.** `search_state_test.dart`
  used a fixed `2026-10-15` date; after that date the validation correctly
  rejected it as past, failing three tests. The tests now use tomorrow.

## 2. Release

- `v1.0.0+8` published 2026-10-19 from `3d2a73b`, run `39205358414`
  (success): 4 signed APKs (universal, arm64-v8a, armeabi-v7a, x86_64) +
  AAB + `release-manifest.json` + `SHA256SUMS.txt` + `PROVENANCE.md`.
- `v1.0.0+7` is superseded; do not install it for the retest.
- Owner retest (no agent runtime gate): install `+8`, then tap a FRESH
  signup confirmation email on the signup device.

## 3. Demo data

- `refresh_demo_horizon()` ran 2026-10-19 (idempotent owner-only RPC):
  648 slots touched, no `booking_id` writes.
- Live after refresh: 24 stations, 1186 trips, 47,320 seats (40/trip),
  horizon through 2026-11-08, 1 booking, 3 profiles.

## 4. Backend advisories observed (not changed this pass)

- `normalize_username` mutable `search_path`.
- pg_graphql schema discovery exposes 12 public tables to `anon` and
  `authenticated`; row access remains RLS-gated, and stations/trips are
  needed for the GraphQL requirement.
- `bootstrap_new_user()` is RPC-executable by `anon`/`authenticated`
  (signup trigger); revoking needs a signup smoke test.
- Leaked-password protection disabled (dashboard/owner decision).

## 5. Remaining owner actions

1. Install `v1.0.0+8` on the device.
2. Tap a fresh signup confirmation email.
3. Rotate the exposed legacy privileged credential and update the hosted
   `SUPABASE_SERVICE_ROLE_KEY` for `book-trip` + `cancel-booking`, then
   redeploy/verify. Secret values are never recorded here.
