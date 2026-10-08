# OWNER DIRECTIVE — device deferral REPLACED by Android emulator verification

Owner instruction, 2026-10-05. **This supersedes the earlier
`OWNER_DIRECTIVE_DEVICE_TESTS.md` "permanently defer all device tests" note.**

## Decision

Physical-device verification is **no longer required** for RailMate BD's
academic/demo acceptance. P34/P35 change from:

> `BLOCKED_OWNER — physical device required`

to:

> `EMULATOR_RUNTIME_VERIFICATION`, and on pass:
> `VERIFIED — Android Emulator runtime` (evidence label
> `ANDROID_EMULATOR_RUNTIME_PROOF`).

An emulator is not identical to a phone, so the final documentation must
always state: **"Verified on Android Emulator (release x86_64 build);
physical-device verification not performed."**

## Mandatory order before runtime acceptance

1. **Reconcile real GitHub state.** `RailMate-BD/main` is `e4187b1`. The
   published `v1.0.0+3` points to the OLDER `5107c05`, so it must NOT be used
   as final runtime proof. Push the missing V4 files to
   `RailMate-BD-internal/main` (remote was still at V3 `c696eeb`).
2. **Audit/fix remaining production unwired paths** — Journey Board comments
   (`CommentThread` exists but the feed card never exposes it).
3. **Complete the password-reset deep-link / recovery path** — the app sends
   `railmatebd://auth/reset-password` but the Android manifest has no
   VIEW/BROWSABLE filter and no Supabase `passwordRecovery` handling.
4. **Publish a new signed release from the final HEAD**, monotonic build
   number, preferably `v1.0.0+4`.
5. **Use the release x86_64 APK** on an Android Studio x86_64 Google Play
   emulator (one Pixel-class API 35 AVD; clear app data first; release APK,
   not debug).

## Consumer-readiness gate (must run BEFORE the emulator gate)

Goal: a normal person picks up the app and it feels finished. **No new
features.** Rule:

> If an existing visible feature is incomplete, finish it. If an unnecessary
> visible feature is incomplete, remove it. If an error exposes developer
> internals, humanize it. If an existing screen looks crude, polish it. Do
> NOT invent new product scope.

Areas: (1) no developer language in UI — raw UUIDs, internal error codes
(`NOT_FOUND`/`UNAUTHORIZED`/`BOOKING_CANCEL_FAILED`), "setup required",
"dependencies missing", raw exceptions, implementation terminology, visible
coming-soon/TODO; (2) no dead controls — remove the no-op "Remember me" and
disabled Google/Facebook buttons rather than advertise them; (3) every major
journey ends properly; (4) behavior polish (keyboard, back, double-submit,
retry, confirm-destructive, restore-on-restart); (5) consumer presentation
(route/train/date/seats instead of DB ids; account-page profile); (6) visual
consistency judged on the emulator, not just "it renders".

## Walkthrough scope (emulator)

fresh launch → onboarding → account create/login → verification → Home →
search → TFLite ranking → seats → passengers → simulated payment → live
booking → ticket/PDF → Bookings → cancel → Board → comments/realtime →
reactions/ratings → image upload → Station Guide/WebView/video/map → AI BYOK
→ Profile → logout → relaunch. Second emulator only for two-client Realtime
proof, and only if RAM safely permits.

## Emulator cannot honestly replace

real SMS, real cellular behaviour, hardware-backed security differences,
camera quality, haptics, OEM rendering quirks, battery/performance. None is
central to this academic demo.

## Constraints

No new features during this pass. Fix only real defects found by source audit
or emulator runtime. Screenshots come from the release build.

## Superseded
The earlier "permanently defer all device tests until I say so separately"
note is **lifted by this document** — the owner has now said so separately,
and directed emulator verification instead.