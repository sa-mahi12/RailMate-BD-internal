# V4 SESSION ROSTER (reset 2026-10-09)

The September 30 worker sessions below are all CLOSED. No September worker
is active or standby. A compacted agent must not treat them as live leases.

| Session | Model | Lane | Task | Allowed paths | Last checkpoint | State |
|---|---|---|---|---|---|---|
| coordinator | muse-spark-1.3 | integration | P00–P33 done solo; consumer-readiness + emulator gate next | shared (main/app/pubspec/android/CI/migrations/git) | 2026-10-09 ledger consistency fix | active |
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
