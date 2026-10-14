# Post-freeze batch — consumer-readiness, signup repairs, releases (2026-10-09 → 2026-10-14)

Status: COMMITTED on `main` in both repositories. No branches, no PRs,
no force-pushes. This file closes the documentation gap between the P36
freeze matrix (code `e4187b1`, release `v1.0.0+3`) and current HEAD.

## 1. Code commits after the freeze (all on `main`, all pushed)

| Commit | Change | Evidence |
|---|---|---|
| `a598fcb` | Consumer gate: removed Remember-me + dead Google/Facebook buttons, humanized history/routes/booking-failure/ticket labels, booking-failure pops + snackbar | owner directive consumer-readiness |
| `e75584a` | Journey Board comments wired: per-post `CommentSection` on feed cards + production seams | `test/board/comment_section_test.dart`, 10 tests |
| `3217b45` | Password-reset deep link completed: manifest filter, `app_links`, recovery session, `startInRecovery` | `test/auth/password_recovery_test.dart`, 9 tests |
| `27c6b2b` | Signup username claim trigger (best-effort, never fails signup) | staging migration + live apply |
| `e34b67b` / `db2c775` | Signup bootstrap trigger creates profile + username (never raises); humanized auth failures. Fixed live "Database error saving new user" (usernames FK had no profile row) | `20261009000002_user_bootstrap.sql` applied live |
| `87b0892` | Emulator findings fixed: board feed loads on startup, real journey labels through seat/passenger/review, keyed tab entrance | emulator screenshots 141–155 |
| `b4f008d` | **Signup localhost fix (2026-10-14)**: `signUp`/`resend` pass `emailRedirectTo: railmatebd://auth/verify`; `AppGate` exchanges the PKCE `code` for a session; manifest `/verify` filter; verify copy covers link-or-code | `test/auth/signup_verify_test.dart` 8 tests; full suite **503/503**; `flutter analyze` clean; `dart format` clean |

Root cause of the localhost defect: with no `emailRedirectTo`, Supabase
builds the confirmation link from the project Site URL (localhost default),
so email taps died in the browser; the app also had no verify-link handler,
and the default email template carries no OTP code. Code half is fixed in
`b4f008d`; the dashboard half is still owed (see §3).

## 2. Releases published (verified via `gh release list` 2026-10-14)

| Tag | Published | Base at publish time |
|---|---|---|
| `v1.0.0+3` | 2026-10-05 | `5107c05` — STALE, do not use as proof |
| `v1.0.0+4` | 2026-10-09 | post-cleanup HEAD (`db2c775` line) |
| `v1.0.0+5` | 2026-10-13 | `87b0892`, x86_64 APK verified installed on emulator |

## 3. Owner actions still owed (Supabase dashboard — not doable from repo)

1. Authentication → URL Configuration → Redirect URLs: add
   `railmatebd://auth/**` (else Supabase refuses the redirect).
2. Site URL: set to a sane value (not localhost).
3. Email Templates → "Confirm signup": include `{{ .Token }}` so the
   6-digit OTP the app asks for actually arrives (link path already works
   once 1–2 are done).

## 4. Verification status

P34/P35 SUPERSEDED — owner dropped device AND emulator verification
completely on 2026-10-14 (ledger + `V4_CURRENT` drop notice). No runtime
proof of any kind is required or expected. The 2026-10-13/14 emulator
walkthrough stopped mid-journey (Booking Review) and will not resume.

## 5. Current task set (2026-10-14)

- P36 TODO: final freeze (evidence matrix refresh + clean/push) — no
  runtime gate in front of it.
- Owner dashboard actions (§3) before any new user can verify email live.
- A fresh signed release only if code changes again (HEAD `b4f008d`
  already builds; no release cut from it yet).
