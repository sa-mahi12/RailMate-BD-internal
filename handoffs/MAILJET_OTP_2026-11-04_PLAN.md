# Signup email OTP implementation plan

**Goal:** Execute the owner-supplied Mailjet OTP/reset ZIP, not a redesign.
**Spec:** `RailMateBD_Mailjet_Email_OTP_User_Reset_Handoff_2026-11-04.zip`,
especially `AGENT_PROMPT.txt`, `IMPLEMENTATION.md`, `USER_DATA_RESET.md`.
**Architecture:** Retain email/password signup, username metadata, phone OTP,
and recovery callbacks. Reuse AuthState/repository/Supabase adapter. Preserve
the existing auth theme; one numeric/pasteable input avoids six-box focus traps.
**Base:** code `cafa3f01c67a66dd647f7cf40f27f0cae786c78a`, docs `68424f6`.
**Execution:** Sole release coordinator, inline; no branches/worktrees.

## Constraints and scope
- Only RailMate `psuzlyingfmstnyfvlnj`; never Norfold.
- Initial reset HALTED on Admin API HTTP 401, before deletion; subsequently
  authorization resolved and reset completed (see current checkpoint/progress).
- Never print credentials, tokens, real user records or OTPs.
- No dependency installation or local Android build. Release workflow +11.
- Claimed app paths: `lib/features/auth/{verify_screen,auth_state,auth_repository,supabase_auth_client}.dart`,
  relevant `test/auth/` files, `test/app_gate_p03_test.dart`, README auth copy if needed.
- Private evidence/plan lives here, not in source-only repository.

## Review focus
- Invalid/expired code preserves root verification route and input.
- In-flight verify/resend suppresses duplicate/stale button submissions.
- Missing or unconfirmed verification response must not authenticate.
- Root success advances Home without popping the root route; pushed success returns.
- Resend failures remain safe and retryable; cooldown only follows acceptance.

## Task 1 — OTP UI/state/adapter (shared interface: existing verifyCode/resend)
- [x] Write failing widget/gate tests for numeric paste, validation, duplicate
  verify/resend, invalid retention, root/pushed success, null response, safe resend.
- [x] Add SDK transport test pinning outgoing verify type `email`, signup resend
  type `signup`, and retained email/password registration.
- [x] Run focused tests; record actual expected RED.
- [x] Minimal implementation: retain needsVerification while busy/error using a
  separate busy flag; replace link instructions with input and Verify code;
  validate six ASCII digits in repository; use SDK `OtpType.email` for verify.
- [x] Format, analyze, focused and full suite; independent read-only review.

## Task 2 — Hosted template/release/evidence
- [x] Compare exact hosted signup HTML to supplied token-only template; apply
  only signup template/subject if different, verify SMTP/recovery unchanged.
- [x] Post-pass: review exact paths, secret scan, owner identity + both main
  branches; coordinator commit/push only reviewed paths.
- [x] Dispatch signed release build 11; verify manifest SHA/versionCode/assets.
- [x] Report actual reset COMPLETE / signup NOT SENT (owner personal signup).
  Keep provider delivery separate from API acceptance.

## Current checkpoint (supersedes historical progress below)
- Code `5ebbf70f13509c0f5e86ed7668630264b40276b5` pushed on `main`.
- Final already-running verification finished 2026-11-04 11:30:50 +06:00:
  `dart format --output=none --set-exit-if-changed lib test tool`,
  `flutter analyze --no-pub`, `flutter test --no-pub --reporter expanded` ->
  exits 0/0/0, **558/558**. No new local test pass after owner stop request.
- GitHub release `41779702127` and CI `41779699297` completed success on
  `5ebbf70`. `v1.0.0+11` published 2026-11-04T05:37:12Z, 8 assets; downloaded
  manifest asserted SHA/versionCode=11/signed=true/correct RailMate backend.
- Source exact-path secret scan/diff gate/owner identity done; private docs
  reconciliation complete; sync in this documentation commit. README-only
  correction pushed as `41e8e57f474b72166209d077792356950ae8c3a1` with skip-ci;
  +11 app binary unchanged.
- Initial reset halt, route RED pending, and final-suite pending statements in
  historical progress below are superseded. No further reset or signup request.

## Progress
- Post-reset SQL confirms Auth users/profiles/usernames/bookings/posts/Storage
  objects all 0, bucket `post-media` retained; seed counts unchanged; Realtime
  still `post_comments`, `post_reactions`, `posts`. No reset rerun needed.
- Final review corrections: flat no-session fixture confirmed RED; removed
  adapter's user-only fallback. Auth-stream null + late verify success/failure,
  late resend failure, explicit logout + late success confirmed 4 RED failures;
  generation guards now ignore stale completions (confirmed event still wins).
- Route reproduction confirmed RED exit 1: root verify popped `other route`.
  Now pop only when this screen's own ModalRoute is current and not first.
- Post-review verification launched separately; old 552 result retained only as
  historical pre-fix evidence, not used to claim current code green.
- UI design gate: retained existing auth tokens/typography/spacing; removed three
  link-instruction rows; one labeled numeric field with OTP autofill and paste;
  primary action says Verify code; feedback stays local and countdown is quiet.
  No visual/device claims made; owner device/emulator drop remains binding.
- RESET COMPLETED (supersedes halt below): current secret key read-only Admin
  request with explicit `RailMate-Reset-Coordinator/1.0` User-Agent -> HTTP 200.
  Supabase docs confirm User-Agent checks for secret keys. Previous default
  requests returned 401; no legacy exposed credential used.
- Hosted before: profiles 3, usernames 3, bookings 1, passengers 2, booking
  seats 2, posts 1; comments/reactions/ratings 0; Auth users 3, object 1.
- `reset-api.ps1 -Phase Storage` -> removed 1, exit 0. Supplied app-row
  transaction via execute_sql -> remaining user rows 0, occupied seats 0,
  storage objects 0; preserved 24 stations / 1186 trips / 47320 seats.
- `reset-api.ps1 -Phase Auth -AppRowsCleared` -> removed 3, remaining 0, exit 0.
  No schema/migration/Realtime/function change, no Norfold request.
- Owner selected **I will sign up** instead of generated disposable password.
  Agent signup/email send is now intentionally NOT SENT, not an access blocker.
- Restart-resistant verification finished 2026-11-04 11:18 +06:00: format 199
  files 0 changed, analyze zero issues (108.1s), full suite 552/552 exit 0.
  Existing PDF Unicode-font warnings remain; no test failures.
- Independent reviewer `ses_e5b035a8effewRvvIy1oKayPqz` found 3 important cases:
  flat user-only response, late OTP completions superseding logout, root popping
  an intervening route. Confirmed flat-response RED expected null/actual user;
  adapter now requires session. Lifecycle RED 4 failures confirmed; generation
  invalidation implemented. Route RED still pending; final verification required.
- 2026-11-04: Tests saved before code. Initial focused RED exit 1 (missing
  OTP input, null-response route loss, nonnumeric token accepted). Corrected
  SDK test fixture constructor/PKCE setup; adapter RED then showed expected
  `email`, actual `signup`; resend characterization passed.
- Implemented four auth source files; AppGate untouched. Focused run reached
  19 passing / 1 failure: test finder matched both subtitle and validation
  message. Narrowed finder to validation message (test-only correction).
- Adapter tests 3/3 PASS exit 0: actual installed SDK HTTP verify payload uses
  `email`, resend uses `signup`, user-only/no-session response returns null.
  This is mocked transport evidence, NOT hosted token verification.
- Hosted `auth-config.ps1` read-only exit 0: supplied signup HTML exact match
  true, token true/link false, six digits, Mailjet configured, recovery link
  true. No template/config patch executed; existing settings satisfy packet.
- `dart format` on eight changed Dart files exit 0, 0 changed. Analysis attempt
  timed out/interrupted by server restarts before output: NOT a PASS.
- Restart checkpoint: source/tests retained. Remaining: full suite/analyze,
  independent review, exact-path commit/push, signed +11 release, private sync.
- Restart preflight: `git status --short --branch`, `git rev-parse HEAD` in both
  repositories -> exit 0; code unchanged, only pre-existing `.serena/` untracked.
- Ruling: owner packet explicitly says execute rather than only plan; no new
  design approval cycle. Existing auth visual system wins; scope is behavior.
- Ruling: no AppGate change planned: retaining needsVerification during OTP work
  keeps its current routing stable. Gate tests must prove this choice.
