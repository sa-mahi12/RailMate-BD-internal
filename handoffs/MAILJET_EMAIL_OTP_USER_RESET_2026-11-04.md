# Mailjet signup OTP + user reset handoff

Date: 2026-11-04. Sole coordinator; two repositories, `main` only.
Model: `agentrouter/gpt-6.1-sol` (current harness metadata). Coordinator OpenCode
session ID is not exposed in this checkpoint; reviewer ID below is not ours.
Code: `5ebbf70f13509c0f5e86ed7668630264b40276b5`, pushed successfully.
Current app HEAD: `41e8e57f474b72166209d077792356950ae8c3a1` (README-only
558-count/date/SHA correction; `[skip ci]`; +11 runtime files unchanged).
Release: signed `v1.0.0+11` published 2026-11-04T05:37:12Z, run `41779702127`
completed success. CI run `41779699297` also completed success on this code SHA.
URL: https://github.com/sa-mahi12/RailMate-BD/actions/runs/41779702127
Download: https://github.com/sa-mahi12/RailMate-BD/releases/tag/v1.0.0%2B11

## Hosted reset — COMPLETE
- Target: RailMate `psuzlyingfmstnyfvlnj`, verified against published +10 URL.
  No Norfold request. Schema matched packet before deletion.
- Original Admin 401 did NOT delete data. Read-only corrected server User-Agent
  request returned 200 using current secret key; no legacy key used.
- `reset-api.ps1 -Phase Storage` -> 1 uploaded object removed, exit 0.
- Packet transaction -> profiles 3, usernames 3, bookings 1, passengers 2,
  booking_seats 2, posts 1 removed (12 app rows); engagements 0; 2 seats freed.
- `reset-api.ps1 -Phase Auth -AppRowsCleared` -> 3 removed, 0 remain, exit 0.
- Post SQL: users/profile/username/booking/post/object counts 0; `post-media`
  bucket retained; stations 24, trips 1186, seats 47320, occupied 0; public
  Realtime remains posts/post_comments/post_reactions. No DDL, function or
  publication change. Issued JWTs may remain valid until expiry; external email
  logs/backups/history are not claimed erased.

## Email configuration — existing settings verified, not rewritten
Read-only `auth-config.ps1` exit 0: exact supplied signup HTML match true;
Token true, confirmation link false, OTP length 6, confirmation required,
Mailjet in-v3.mailjet.com:587 credentials configured (values never printed).
Recovery remains link-based. No SMTP/template patch needed.

## Code and review
Changed exact paths: README.md; four source files
`lib/features/auth/{auth_repository,auth_state,supabase_auth_client,verify_screen}.dart`;
`test/app_gate_p03_test.dart`, `test/auth/verify_screen_test.dart`, new
`test/auth/email_otp_{adapter_test,fakes,lifecycle_test}.dart`.

Kept email/password signup, username metadata/checks, login/logout, password-reset
links/callbacks, photo upload, phone OTP and old auth callbacks. AppGate unchanged.
One labeled numeric input with six-digit limit/paste/autofill; safe retries keep
input/route; separate busy guard; resend cooldown. SDK verify type `email`, resend
`signup`. Only real session user can authenticate. Generation guards and screen's
own ModalRoute prevent late-response/logout and unintended-pop regressions.

Independent reviewer `ses_e5b035a8effewRvvIy1oKayPqz` found three important cases.
Flat user/no-session test RED; late verify/resend after logout tests RED; intervening
route RED; all corrected. No further reviewer dispatch, no extra feature expansion.
Author final diff check and exact-path secret scan exit 0, zero secret patterns;
owner GitHub login/id and Git identity verified; only pre-existing `.serena/`
untracked remains. Source commit contains no credentials or real user data.

## Evidence limits and next action
Already-running final pass finished 2026-11-04T11:30:50.6625203+06:00:
- `dart format --output=none --set-exit-if-changed lib test tool` -> exit 0.
- `flutter analyze --no-pub` -> exit 0.
- `flutter test --no-pub --reporter expanded` -> `+558: All tests passed!`, exit 0.
Evidence: approved Temp `mailjet-gate/verification-status.json`, `verify.ps1`,
`format-final.log`, `analyze-final.log`, `suite-final.log`. Script's captured base
is pre-commit `cafa3f0` with the final OTP working tree; those files were committed
as `5ebbf70` while the pass was running. Pre-review 552/552 is historical only.
Owner requested no more local tests; no additional local pass was launched.
`gh run watch ... --exit-status` -> exit 0 for both `41779702127` and
`41779699297`; release and CI succeeded on `5ebbf70`. Release logs show format
198 files/0 changed, analyze No issues found, embedded Supabase host check passed.
Existing PDF Unicode-font warnings are unrelated, not concealed as clean output.
No local Android build or device/emulator proof; owner drop remains binding.

Owner selected **I will sign up**. NO agent signup/email request, NO generated
password. Install published +11, register a fresh account, read the code
in Inbox/Spam and enter it privately. Login/logout, reset-password link and photo
upload remain available. No inbox delivery or live OTP success is claimed.

## Repository preflight
`gh api user` -> login `sa-mahi12`, id `212235795`; Git identity matches
`sa-mahi12` / `212235795+sa-mahi12@users.noreply.github.com`. Both local and
remote branch lists show only `main`; observed commands exit 0.
Internal remote visibility is PUBLIC, not private: confirmed by `gh api repos`.
This matches the explicit owner-public decision recorded in `handoffs/F00.md`;
no visibility change made. The internal-folder label must not imply secrecy.
Only credential-free, user-record-free evidence is eligible for this remote.

## Artifact verification and remaining action
`gh release view v1.0.0+11` -> eight non-empty assets (4 APKs, AAB, manifest,
checksums, provenance). `gh release download` -> exit 0 for the three small
evidence files; literal manifest assertions exit 0: versionCode=11, signed=true,
commit=5ebbf70f13509c0f5e86ed7668630264b40276b5, correct RailMate URL.
Universal APK size: 85,478,967 bytes. Published SHA256:
`69fe44835a3aaa2e906184f87011ab12775cc900d2ac31ad479a6b9855f0aff3`.
This is the published checksum, not a locally downloaded APK rehash/signature
inspection. Evidence saved in approved Temp `mailjet-gate/release-11/`.
Workflow deprecation annotations (Node/setup-java/runner image) did not fail the
build; workflow modernization is outside this packet. No CI/secrets change made.
Next action: owner installs +11 and signs up privately; existing account data was
erased, so an old account must be recreated. Inbox/OTP, login/logout, recovery and
photo-upload runtime acceptance remain owner-side, never inferred from CI.

## Owner-requested demo account (2026-11-04 11:55 +06:00)
Owner overrode the personal-signup choice and asked for an immediate demo login,
including deletion of any conflicting existing account.

- Email `sanjidamahi2005@gmail.com`, username `sanjidamahi2005`, password chosen
  by the owner (demo strength only; never written to either repository, logs,
  prompts or screenshots).
- Provisioned with Supabase Admin API `POST /auth/v1/admin/users`, `email_confirm`
  true, username in `user_metadata` only; no `app_metadata` role change, so the
  account is an ordinary `authenticated` user under normal RLS.
- Conflict policy executed: pre-scan for matching email or username claim found
  0 accounts, deleted 0, recheck found 0. Nothing else was removed.
- Verification: an independent rerun signed in with the password grant, read its
  own profile and username rows, then closed the session locally. Observed output:
  `authUsers=1 emailMatches=1 emailConfirmed=True role=authenticated
  profileRows=1 usernameRows=1`.
- Script: approved Temp `mailjet-gate/provision-demo-user.ps1`; it pins RailMate
  `psuzlyingfmstnyfvlnj` only. Exit 0; no repository files changed.
- This is a host-side seeded account, not proof that the app's OTP signup UI or
  Mailjet delivery works. The owner still needs to install +11 and log in.

## Requirement impact and documentation gate
- R-05: signup email uses numeric OTP; live delivery/acceptance NOT VERIFIED,
  phone-provider blocker unchanged. No whole-requirement PASS claimed.
- R-11: session required for email OTP, stale completions guarded; login/logout
  and recovery preserved. R-13: photo upload code/policies preserved; reset
  removed old objects, not the bucket. No new device/live PASS for either.
- Booking, seed inventory, ML, guide, BYOK, payments untouched by this code pass.
- Final docs paths: `coordination/V4_CURRENT.md`, `tasking/V4_TASK_LEDGER.json`,
  `handoffs/MAILJET_OTP_2026-11-04_PLAN.md`, this handoff. V4 current/ledger are
  the active records; historical V1 operations records were not overwritten.
- Post-pass: exact path review, JSON parse, credential-pattern scan and
  `git diff --check` completed; focused Flutter rerun intentionally not launched
  for documentation-only corrections. Model/session limitations noted above.
- Internal documentation HEAD: this commit; coordinator pushes these exact four
  paths separately. Do not infer a remote success until push stdout/exit 0.
