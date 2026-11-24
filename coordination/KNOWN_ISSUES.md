# KNOWN_ISSUES.md (2026-09-27)
- gh MISSING → remote creation + auth verification blocked.
- flutter/dart MISSING → skeleton/analyze/test/build blocked; CI file present but not run.
- Android SDK/adb MISSING → device verification blocked (Samsung USB device seen, unconfirmed).
- Supabase project UNKNOWN → hosted decision + billing/SMS gate pending.
- AgentRouter route UNPROVEN → need tiny non-project request proof (Prompt 2).
- AGENTS.md references ../RailMate-BD-internal hyphen path; actual locals are D:\RailMateBD(-internal) — mapped, no extra folders.

## Open follow-ups after P42 (2026-11-25)

- Auth recovery link: `AppGate` handles a recovery deep link on both cold start
  and the warm stream without the by-code guard that signup verification uses,
  so a single tap can attempt the single-use PKCE exchange twice and leave the
  just-reset user on the fallback screen. Pre-dates P42; needs a Dart change and
  therefore the next app release. Reported by the P42 read-only reviewer.
- `post_links.dart` `parsePostLink`/`parseProfileLink` accept `http://` as well as
  `https://`. Every accepted id is still uuid-validated and only the fixed
  sa-mahi12.github.io host is allowed, so there is no open redirect; tighten it
  in the same release.
- `post_attachments` RLS `attachments_read` is `using (true)`, which is correct
  while every post is public. If post moderation/hiding is ever added, the read
  policy must follow the post's visibility or attachment metadata leaks for
  hidden posts.
- P42 device gap: the composer, the per-kind attachment renderers and the
  `railmatebd://post|profile` deep links are unit-tested and observed through the
  hosted API, but no phone or emulator run of those screens was performed.
