# V4 SESSION ROSTER (reset 2026-10-09)

The September 30 worker sessions below are all CLOSED. No September worker
is active or standby. A compacted agent must not treat them as live leases.

| Session | Model | Lane | Task | Allowed paths | Last checkpoint | State |
|---|---|---|---|---|---|---|
| coordinator-2026-11-03 | `opencode/deepseek-v4.1-flash-free` | integration | Teacher final gate code pass: real phone-OTP routing, shared per-table realtime comments/reactions, hosted realtime publication (`posts`/`post_comments`/`post_reactions`), README honesty; `cafa3f0`; 542/542 local + CI (`41661488425`); `v1.0.0+10` (run `41661512576`) | shared (main/app/pubspec/android/CI/migrations/git) | 2026-11-03 (V4_CURRENT + ledger P37 + TEACHER_FINAL_GATE handoff) | active |
| coordinator-2026-10-19 | `agentrouter/deepseek-v4-flash` | integration | Consumer-readiness batch: real upcoming booking wiring, username checker on all signup paths, booking submit guard + non-contract failure handling, raw-error/copy gate; `3d2a73b` + `6c0ddf8`; 523/523; `v1.0.0+9` (run 39206584037); post-release docs/test sync `d683e14` + `a265c92` (no lib/ change, +9 unchanged) | shared (main/app/pubspec/android/CI/migrations/git) | 2026-11-03 (V4_CURRENT + ledger + CURRENT + CONSUMER_READINESS handoff) | closed |
| coordinator | muse-spark-1.3 | integration | Takeover batch: link-first verify UI (`0489e61`, 506/506) + analyze fix (`210ad8a`); app.env.json untracked (rotation = owner action); v1.0.0+6 dispatched; V4_CURRENT contradiction fixed | shared (main/app/pubspec/android/CI/migrations/git) | 2026-10-14 takeover (ledger + V4_CURRENT + TAKEOVER handoff) | closed |
| worker-a | - | design/motion | P01 done | lib/design/** | closed 2026-09-30 | closed |
| worker-b | - | onboarding/auth | P04 done | lib/features/onboarding/** | closed 2026-09-30 | closed |
| worker-c | - | home/search/data | P11 draft done | supabase/seed drafts | closed 2026-09-30 | closed |
| worker-d | - | booking/ticket | (cancelled, reverted) | - | closed 2026-10-02 | closed |
| worker-e | - | board/guide/profile | P19 draft done | supabase/seed drafts | closed 2026-09-30 | closed |
| worker-f | - | QA/release | (never launched) | - | - | closed |
| reviewer | - | QA | (never launched) | read-only | - | closed |

Rules for any future subagent: single worker at a time, coordinator-owned
files (main/app/pubspec/android/workflows/migrations) stay coordinator-only,
and no two workers share one file.
