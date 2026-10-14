# Takeover batch — 2026-10-14 (agent handoff ZIP execution)

Takeover source: owner-supplied `RailMate-BD-Agent-Handoff-2026-10-14.zip`
(7 files; secrets-free). Canonical state stayed in the two GitHub
repositories; the ZIP was read-only input. Owner write to the internal
repo failed with HTTP 403 on their side — the agent committed directly.

## 1. Code commits (all on `main`, all pushed)

| Commit | Change | Evidence |
|---|---|---|
| `0489e61` | Link-first verify UI for the default-mailer reality: 3-step link flow, primary "I've confirmed — re-check", resend with 60 s throttle, `railmatebd://auth/verify` exchange untouched, password-reset link untouched. No 6-digit signup OTP promise. `verifyCode`/`verifyEmailOtp` kept as a dormant seam (doc-noted). Tracked `app.env.json` removed from HEAD (`.gitignore` already covered it; builds use `--dart-define` publishable values only). | `test/auth/verify_screen_test.dart` 3 widget tests; format clean; analyze clean; full suite **506/506** |
| `210ad8a` | Release-gate fix: `tool/check_v4_release.dart` doc-comment angle brackets (2 pre-existing infos) made `flutter analyze` exit 1 in CI and failed the first `v1.0.0+6` dispatch. | `flutter analyze --no-pub`: **No issues found** |

First `v1.0.0+6` dispatch (run `38518097957`) failed exactly on those 2
infos; re-dispatched after `210ad8a` (run `38518404447`).

## 2. Security state — exposed privileged credential

- Confirmed at handoff HEAD: public repo tracked `app.env.json` holding a
  live privileged credential (key names only ever inspected; value never
  copied to docs, logs, prompts or commits).
- Repository-side remediation DONE in `0489e61`: file untracked; nothing in
  the Flutter app, tests, CI or release workflow ever read it (verified by
  source search); Edge Functions `book-trip` + `cancel-booking` (both ACTIVE
  v1) read `SUPABASE_SERVICE_ROLE_KEY` from hosted env only — no code change
  needed for rotation.
- NOT done (no access + worker deploy rules): key rotation/invalidation and
  hosted function-secret update/redeploy. This is ONE explicit owner action
  (steps in `V4_CURRENT.md` BLOCKED_OWNER). Deletion from Git is not
  rotation — the handoff and this file do not claim otherwise. No
  force-push/history rewrite (single-main rule unchanged).

## 3. Owner-completed Supabase setup (2026-10-14, owner-reported)

Dashboard URL/deep-link work treated as complete; no custom domain/SMTP by
owner choice; production signup is confirmation-link based. `{{ .Token }}`
template editing is NOT an outstanding owner task. App side aligned in
`0489e61`.

## 4. Docs

- `coordination/V4_CURRENT.md`: stale reopen paragraph replaced with an
  explicit supersession note; header now tracks code `210ad8a` / 506/506;
  owner-completed setup + rotation action recorded. No contradictory
  runtime requirement remains.
- P34/P35 stay SUPERSEDED; no device/emulator/screenshot gate was
  requested or run.

## 5. Release + P36

- `v1.0.0+6` dispatched from `210ad8a` after the analyze fix (run
  `38518404447`). Record the published tag here and in `V4_CURRENT.md`
  once the run completes, then mark P36 VERIFIED with final heads.
