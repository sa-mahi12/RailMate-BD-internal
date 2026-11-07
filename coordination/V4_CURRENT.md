# V4 CURRENT — signup email OTP + RailMate user reset (P38)

Timestamp: 2026-11-04 (Asia/Dhaka).
Code pushed to `main`: `5ebbf70f13509c0f5e86ed7668630264b40276b5`.
Current app-repo HEAD: `41e8e57f474b72166209d077792356950ae8c3a1` (README-only
evidence correction, pushed with `[skip ci]`; released app binary unchanged).
Signed `v1.0.0+11` PUBLISHED 2026-11-04T05:37:12Z: release run `41779702127`
completed success. Downloaded manifest confirms versionCode 11, signed true,
commit `5ebbf70f13509c0f5e86ed7668630264b40276b5`, correct RailMate backend.
Eight assets: four APKs, AAB, manifest, checksums, provenance.
Release: https://github.com/sa-mahi12/RailMate-BD/releases/tag/v1.0.0%2B11

- RailMate-only purge COMPLETE: Storage API removed 1 object; packet app-row
  transaction removed 12 rows and released 2 occupied seats; Auth Admin API
  removed 3 users. Post-query shows users/user data/objects 0, bucket retained.
  Preserved 24 stations, 1186 trips, 47320 seats, schema, Realtime and functions.
- Initial 401 resolved with explicit server User-Agent using the CURRENT secret
  key in process memory. No exposed legacy credential used, no rotation performed.
- Hosted signup HTML EXACT MATCH to supplied token-only template; Mailjet already
  configured, confirmation required, six digits; recovery remains link-based.
  No template or SMTP mutation needed/performed.
- OTP UI/state/adapter shipped: numeric paste, duplicate guard, cooldown, safe
  errors retain input/route, real session required, stale results cannot undo
  newer auth state; root does not pop other routes. Password/username registration,
  login/logout, forgotten-password callbacks, photo upload and phone OTP retained.
- Owner selected **I will sign up**. Agent sent NO signup email, generated NO
  password. Inbox/provider delivery and hosted OTP acceptance are NOT VERIFIED.
- Owner then requested an immediate demo account and authorised deleting a
  conflicting account. Provisioned 2026-11-04 11:55 +06:00 via Auth Admin API:
  `sanjidamahi2005@gmail.com`, username `sanjidamahi2005`,
  administrator-approved email status, normal `authenticated` role. Owner chose
  the password; it is stored in neither repo. Conflict scan found 0 accounts and
  deleted 0. Independent rerun: password grant succeeds, own profile and username
  rows present, session closed. Demo seed only, not OTP-path proof.
- Independent review findings reproduced and corrected. Already-running final
  verification finished 2026-11-04 11:30:50 +06:00: format/analyze/test exit 0,
  558/558 tests. No additional local test pass launched after owner request.
  GitHub runs `41779702127` and `41779699297` completed success on `5ebbf70`;
  release APKs/AAB and CI debug APK built. Live/device proof remains distinct.
- Record: `handoffs/MAILJET_OTP_2026-11-04_PLAN.md` and
  `handoffs/MAILJET_EMAIL_OTP_USER_RESET_2026-11-04.md`.

**Superseded below:** 2026-10-14 no-custom-SMTP/link-first signup decision and
  no-agent-task state are historical; the owner Mailjet handoff overrides them.

## P39 — demo readiness pass (2026-11-04, after +11)

Coordinator-run, additive, no app-code change. App HEAD stays `41e8e57`.

1. **Demo timetable refreshed.** `select public.refresh_demo_horizon(20)` ->
   `648` (idempotent slot count). Live: 1,682 trips, 67,160 seats, horizon now
   `2026-11-24` (was `2026-11-08`, which had become shorter than the app's
   today..+20 picker window). 32 trips exist on the last selectable day.
   `bookings=0`, occupied seats `0`. Four stale 10-seat 2026-10-15/16 test trips
   remain, past the picker window and therefore unreachable.
2. **Auth-function advisories fixed** (hosted migration
   `20261104060034 auth_function_hardening`, committed as
   `supabase/migrations/20261104000001_auth_function_hardening.sql`):
   - 0011: `public.normalize_username` now `SET search_path = ''` and uses
     `pg_catalog`-qualified built-ins.
   - 0028/0029: `EXECUTE` on the `SECURITY DEFINER` signup trigger
     `public.bootstrap_new_user()` revoked from `PUBLIC`, `anon`,
     `authenticated`; ACL now `postgres`/`service_role` only. Trigger firing does
     not check EXECUTE, so signup is unaffected.
   - Smoke test after the change: admin-created user still produced its profile
     row and a normalised username claim; anonymous
     `POST /rest/v1/rpc/bootstrap_new_user` -> HTTP 404 (not exposed); smoke user
     deleted and its rows cascaded. Advisors 0011/0028/0029 no longer fire.
   - Remaining WARNs are intentional/owner-side: 0026/0027 pg_graphql table
     exposure (needed for R-18 and PostgREST grants, RLS-gated) and
     `auth_leaked_password_protection` disabled (owner decision; enabling it
     would reject the owner's chosen demo password).
3. **Live user-flow re-verification** against RailMate with the seeded demo
   account (`exit=0`): password login -> session; authenticated upload to
   `<uid>/...png` in `post-media` + public read (HTTP 200, 70 bytes) + own
   delete; own post + comment + reaction inserts accepted under RLS and cleaned
   up; global logout -> refresh token rejected (HTTP 400); one Mailjet recovery
   request returned HTTP 200. Access JWTs remain valid until their normal expiry
   — standard Supabase behaviour, stated instead of claiming instant JWT death.
   Owner-side evidence also observed: a real 645 KB `.jpg` appeared in
   `post-media` at 11:58 +06:00, so photo upload has been exercised from the app.
4. **Live booking E2E re-verified** through the deployed `book-trip` /
   `cancel-booking` Edge Functions with the demo account (`exit=0` each step,
   state read back with SQL rather than wrapped PowerShell arrays):
   - `simulateSuccess=false` -> `PAYMENT_SIMULATION_FAILED`
     (`DEMONSTRATION ONLY - no booking created, no charge`); booking count and
     held-seat count unchanged afterwards, so the declined path truly writes
     nothing.
   - 2-passenger booking -> `CONFIRMED`, booking
     `cddd66e6-2520-4e06-98f2-150dadeb7577`, fare 1080, seats `A9`/`B1`,
     `booking_seats=2`, held seats `2`.
   - Cancel -> `CANCELLED`, held seats back to `0`, seats no longer tied to the
     booking, passenger + seat audit rows retained.
   - Final demo booking left in place: `f463cead-2a63-4a48-a1a0-1656a23e2ebf`,
     `CONFIRMED`, 2 passengers (Sanjida Mahi / Demo Companion), seats `A2`,`A3`,
     fare 1250, Dhaka -> Chattogram departing 2026-11-06 07:00 Asia/Dhaka.
     Hosted totals: 2 booking rows (1 CONFIRMED + 1 CANCELLED history), 2 held
     seats.
5. **Data hygiene:** verification posts/comments/reactions/objects removed; only
   the seed post/comment/reaction, the owner's uploaded photo, 1 profile, 1 demo
   account and the demo booking pair above remain.
6. **Signup/OTP proven on-device (emulator + released APK).** Installed the
   published `RailMate-BD-1.0.0-x86_64.apk` (SHA256 matches `SHA256SUMS.txt`),
   cleared app data, and drove the real UI: onboarding -> Create Account -> form
   -> **Verify your account** screen -> 6-digit code -> Home
   ("Good afternoon, UI Probe"), with Profile showing *Email verified* and
   `@uiprobe2026`. The live username checker showed *Available*, and the home
   date picker displayed *Up to 24 Nov, 2026*, i.e. the refreshed horizon is
   visible in the shipped app.
   - Backend replay of the same contract also passed: `POST /auth/v1/signup`
     returns 200 with `confirmation_sent_at`, `type=email` OTP verification
     returns a session, and the bootstrap trigger creates the profile +
     normalised username.
   - Client-side rule found while driving the form: the app requires a password
     of **at least 8 characters**; a shorter one is rejected locally and the
     screen shows the generic *"Registration failed. Please try again."*, which
     can look like a broken signup. Usernames are normalised to lowercase and
     must be 3-20 chars of `[a-z0-9_]` starting with a letter.
   - Genuine signup OTP requested for the owner-requested recipient address
     (withheld from this PUBLIC docs repo) at 12:25 +06:00 (Auth 200,
     `user_confirmation_requested`, Mailjet dispatch accepted). **Inbox delivery
     and code entry remain unverified** - that step belongs to the inbox holder
     per the packet. The temporary account created for that send was deleted
     again (only the demo account remains) so the owner can register that address
     with their own password.
   - All probe accounts (`railmate.probe*`, `railmate.pw*`, `railmate.ui.probe`,
     `railmate.shortpw`) were removed; verified `auth_users=1`,
     `profiles=1`, `usernames=1`, no orphan rows.
   - **Mailjet pipe and template content verified end to end without touching an
     owner inbox:** a signup for a disposable third-party mailbox (address
     withheld) produced the hosted *"Verify your RailMate BD account"* email in
     about 10 s. The body is OTP-only - "Enter this one-time verification code
     in the RailMate BD app to complete your registration" followed by the six
     digits - and contains **no confirmation link** (the only URLs are Mailjet
     open/click tracking), so the packet's OTP-only template requirement holds.
     Sender is the owner Gmail address, which is why Gmail may file these under
     Spam; the disposable account was deleted immediately afterwards.

6b. **Owner-reported "signup fails": root cause found, fixed in `v1.0.0+12`.**
   - Reproduced on the device with the published `+11` build: a 6-character
     password (`qwerty`, the same shape as the demo password) is rejected by the
     **local** validator and the form shows only *"Registration failed. Please
     try again."* Nothing reaches Supabase - the auth log records no signup
     event at all for that attempt - so the user sees what looks like a server
     failure.
   - Fix (`986f994`): the client-side validation messages are now exported
     constants on `AuthRepository`, and `AuthState._publicAuthError` returns
     those messages **verbatim** through an allow-list. Any other
     `ArgumentError` (SDK text that could carry backend detail) still falls
     through to the generic sentence, so the consumer gate is intact.
   - Evidence: two new unit tests (verbatim rule + allow-list gate), full suite
     `560/560` local, `flutter analyze` clean, format clean; CI run
     `41788348858` success; release run `41788362168` success ->
     `v1.0.0+12` (8 assets, versionCode 12, signed).
   - Verified on the emulator with the published `+12` APK: the same 6-character
     password now renders **"Password must be at least 8 characters."**
   - Genuine signup for the owner-requested address driven from the shipped app
     at 19:26 +06:00: `POST /auth/v1/signup` accepted (account created,
     `confirmation_sent_at` set, `user_confirmation_requested` 200) and the app
     reached **"Verify your account - Enter the 6-digit code sent to ..."**.
     The account is left **unconfirmed on purpose** so the inbox holder can
     finish the code step; its password is a disposable one, so the owner can
     use *Forgot password* afterwards to set their own (or ask for it to be
     deleted and register from scratch).

### Remaining after P39 (owner-side only, no agent gate)
1. Install `v1.0.0+12` and log in with the seeded demo account.
2. Change the weak demo password before any public demonstration.
3. Read the real signup OTP from the inbox once to accept the email lane
   (or use the recovery email already sent to reset the account).
4. SMS provider + approved recipient for the live phone-OTP claim.
5. Privileged credential rotation (legacy `app.env.json` key) — unchanged.
6. Two-device realtime observation is owner-side and **not required** (P34/P35
   SUPERSEDED).

Historical P37 section follows.

## Historical P37 teacher final gate — v1.0.0+10

Timestamp: 2026-11-03 (Asia/Dhaka).
Code HEAD: `cafa3f0` is BOTH the app-code commit for this pass and the
`v1.0.0+10` release commit (manifest `versionCode=10`, `signed=true`).
Docs HEAD: this commit.
Phase: **P37 code pass VERIFIED at `cafa3f0` / release `v1.0.0+10` (run
`41661512576`, 8 assets, latest). Full suite 542/542 local and CI (run
`41661488425`), analyze zero issues, format clean. Teacher acceptance itself
is owner-side: live SMS delivery is BLOCKED_OWNER and two-device runtime
observation was not performed.** Record: `handoffs/TEACHER_FINAL_GATE_2026-11-03.md`.

Superseded-directive note (do NOT follow the paragraph below):
`governance/OWNER_DIRECTIVE_DEVICE_TESTS.md` once reopened emulator
verification (2026-10-05 deferral LIFTED, P34/P35 open). That reopen is
HISTORICAL and was superseded by the binding 2026-10-14 owner drop
recorded under OWNER DROP NOTICE. P34/P35 stay SUPERSEDED.

## VERIFIED
- P00-P33 VERIFIED (P30/P31/P32/P33 individual closure notes where
  superseded; see the ledger).
- P37 VERIFIED at code `cafa3f0`, release `v1.0.0+10`, 542/542 (2026-11-03
  teacher final gate code pass). Code scope only: production phone-OTP
  routing + cross-client board comments/reactions + hosted realtime
  publication. Live SMS and two-device runtime are NOT verified.
- P36 VERIFIED at code `6c0ddf8`, release `v1.0.0+9`, 523/523. Earlier
  freeze evidence (v1.0.0+3 era, +6 era, +7 era, +8 era) is RETAINED AS
  HISTORY in the ledger entry.
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
- Consumer-readiness batch 2026-10-19 (`3d2a73b` + `6c0ddf8`; 523/523 local
  and CI, analyze zero, format clean):
  - Home upcoming-booking card now reads real data: earliest future
    CONFIRMED booking, trip/station lookups and its seat codes; load
    failures render the honest failure card (no "no bookings" lie), and
    the card action says `View my bookings` because it opens the history
    list.
  - Live username availability is retained through EVERY signup entry
    point (`AppGate` welcome, welcome, login, register) via
    `AppDependencies.usernameChecker`; no path silently drops the field.
  - Booking submit has a one-shot in-flight guard (a duplicated payment
    event cannot issue a second booking call) and maps non-contract Edge /
    transport failures to plain-language copy instead of an uncaught error.
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
- Teacher final gate code pass 2026-11-03 (`cafa3f0`; 542/542 local + CI,
  analyze zero, format 197 files/0 changed, release `v1.0.0+10` run
  `41661512576`):
  - **Realtime publication was the real blocker.** Hosted
    `pg_publication_tables` listed NO `public` table in `supabase_realtime`
    (only internal `realtime.messages_*`), so Postgres Changes delivered
    nothing — the pre-existing `public.posts` channel was dead as well. With
    owner approval, `public.posts` / `public.post_comments` /
    `public.post_reactions` were added (additive, reversible, no row
    touched); committed as idempotent migration
    `supabase/migrations/20261103000001_realtime_publication.sql` and
    re-verified hosted.
  - **Phone OTP is reachable and real**: `AppDependencies.create()` composes
    `SupabasePhoneOtpClient` (fake is test-only); signed-in requests use
    `updateUser(phone:)` + `verifyOTP(phoneChange)` so the number attaches to
    the existing account, no-session requests use `signInWithOtp` +
    `verifyOTP(sms)`. The Verify screen phone button now opens
    `PhoneVerifyScreen` instead of a placeholder dialog; the DEMO notice is
    gated on the injected fake (`PhoneState.isDemo`) only.
  - **Cross-client comments**: one shared `public.post_comments` channel at
    the shell root, typed `CommentRealtimeEvent`s on a broadcast stream,
    filtered per card. Loaded threads merge inserts/deletes with no refetch;
    other posts ignored; never-loaded threads merge nothing (no invented
    count); own-echo insert dedupes by row id; subscription cancelled on
    dispose.
  - **Cross-client reaction counts**: one shared `public.post_reactions`
    channel; `ReactionRealtimeEvent` carries `post_id` (PK `(post_id,
    user_id)` so deletes carry it), each card filters to its own post and
    calls the existing authoritative `refresh()` — echoed own votes refetch
    once, never double-count.
  - 19 new hermetic tests (`comment_section_realtime_test.dart` 7,
    `post_engagement_realtime_test.dart` 7, `phone_production_wiring_test.dart`
    5); no polling and no per-card channels were introduced.
  - README corrected: phone OTP is no longer described as unimplemented;
    realtime publication + 542 tests + the live-proof limits are stated.
- Post-release docs/test sync 2026-11-03 (`d683e14`, `a265c92`; NO `lib/`
  change, so the `+9` APK and manifest still match `6c0ddf8`): README now
  names `v1.0.0+9`, 523 tests, the live demo counts and the 2026-10-14
  owner drop instead of the superseded directive; the home-search widget
  test stopped hardcoding `2026-10-02` as its clock, which had silently
  expired (the app correctly refused a date past that clock's today+20
  horizon). Re-verified 2026-11-03: format 193 files/0 changed, analyze
  zero issues, full suite **523/523**; CI `Flutter CI - main only`
  run `41638600872` green on `a265c92`.

## STATE
- P34 SUPERSEDED - DROPPED BY OWNER 2026-10-14.
- P35 SUPERSEDED - DROPPED BY OWNER 2026-10-14.
- P37 VERIFIED (code scope) at `cafa3f0` / release `v1.0.0+10`; 542/542 local
  and CI. Teacher acceptance is owner-side: live SMS is BLOCKED_OWNER and no
  two-device runtime observation was made.
- P36 VERIFIED - final V4 freeze at code `6c0ddf8` / release `v1.0.0+9`.
  Repo HEAD `a265c92` was docs/test-only (no app-code change).
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
- SMS provider (carried from V3): the app now composes the REAL
  `SupabasePhoneOtpClient`, so phone verification works as soon as the hosted
  project has an SMS provider and an approved test recipient. Without it the
  request fails honestly (no fake code, no fallback). Owner action before
  claiming the phone feature live.
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
- `v1.0.0+8` (2026-10-19, `3d2a73b`, run `39205358414`) - superseded by +9.
- `v1.0.0+9` (2026-10-19, `6c0ddf8`, run `39206584037`) - superseded by +10.
- `v1.0.0+10` (2026-11-03, `cafa3f0`, run `41661512576`) - LATEST AND ONLY
  SUPPORTED BUILD: 4 signed APKs + AAB + manifest + SHA256SUMS +
  PROVENANCE. Teacher final gate code pass: real phone-OTP routing, shared
  per-table realtime comments/reactions, hosted realtime publication
  (`posts`, `post_comments`, `post_reactions`), 542 tests.

## Remaining - owner-side only (no agent gate)
1. Install `v1.0.0+10` on the owner device (replaces `+9`).
2. Owner taps a FRESH signup confirmation email on the signup device.
3. Configure the hosted SMS provider + an approved test recipient, then send
   one real OTP to claim the phone feature live (BLOCKED_OWNER); if none is
   available, present the phone lane as "wired, provider pending".
4. Two-device demo for the teacher: cross-client comment and like/dislike
   count updates without refresh (the code + hosted publication are ready;
   runtime observation is owner-side).
5. Privileged-credential rotation (see BLOCKED_OWNER) - the single
   outstanding owner-only security action.
