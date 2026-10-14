# HOTFIX — auth deep-link routed to RouteErrorScreen (2026-10-14)

## Symptom (owner-observed on device, `v1.0.0+6` installed)

Tapping the signup confirmation email opened RailMate, then showed the
app's own generic error screen: "We couldn't open this page / Something
went wrong on our side." That copy is `RouteErrorScreen` — NOT a Supabase
failure. Dashboard configuration was never the problem.

## Root cause (confirmed in source before fixing)

1. Android delivered `railmatebd://auth/verify?code=…` correctly (intent
   filters present), but Flutter's built-in deep-link handler ALSO
   converted it into the Navigator named route `/auth/verify`.
2. `AppRoutes` had no `/auth/*` route, so it fell through to `_error`.
3. The project additionally uses the `app_links` plugin, which races the
   built-in handler for the same link. Current Flutter guidance: set
   `flutter_deeplinking_enabled=false` when a plugin owns links.

## Fix (code `315b6a9`, on `main`, pushed)

- `android/.../AndroidManifest.xml`: `flutter_deeplinking_enabled=false`
  inside `.MainActivity` — `app_links`/`AppGate` is now the sole consumer.
- `lib/app/routes.dart`: `/auth/verify` + `/auth/reset-password` resolve
  to the new `AuthCallbackScreen` (URI-path matched, so `?code=…` links
  match too) instead of `RouteErrorScreen`. Genuinely unknown routes still
  hit the error screen (existing test intact).
- Single-exchange audit: `Supabase.initialize` runs WITHOUT
  `authCallbackUrlHostname`, so no automatic Supabase-side exchange exists
  to race the gate. `AppGate` adds a consumed-PKCE-code guard (cold-start
  initial link + warm stream can deliver the same single-use code twice)
  plus injectable link/exchange seams. Stale "6-digit code" copy in the
  gate's failure paths corrected to resend wording.
- Tests: `test/auth/auth_callback_test.dart`, 10 tests — route table
  (bare + query-string links), callback screen (progress, manual Continue,
  auto-pop on authenticate), gate cold-start exchange, warm exchange,
  cold+warm exactly-once. Full suite **516/516**, analyze zero issues.

## Release + device retest protocol

- `v1.0.0+6` still contains the bug — it MUST be replaced on device.
- `v1.0.0+7` dispatched from `315b6a9` (run `38523128566`).
- Owner retest (no agent runtime gate): install +7, request a FRESH
  confirmation email, tap the new link on the SAME device that signed up.
  Do NOT reuse the old link (PKCE codes are single-use + short-lived).

## Credentials

Unchanged by this hotfix: privileged-credential rotation remains the one
explicit owner action (see `V4_CURRENT.md` BLOCKED_OWNER).
