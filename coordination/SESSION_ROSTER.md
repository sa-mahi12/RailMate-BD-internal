# SESSION_ROSTER.md (2026-09-27)
| Role | Model | Session | Cwd | Task | Files | Status |
|---|---|---|---|---|---|---|
| Coordinator/setup | muse-spark-1.3-contributor-free (current) | this session | D:\RailMateBD + D:\RailMateBD-internal | Prompt 1 Phases A–C partial | coordination/*, no app edits yet | IN PROGRESS |
| Worker A | opencode/mimo-v2.6-flash-free | TBD | TBD | TBD after Prompt 2 | disjoint TBD | NOT STARTED |
| Worker B | opencode/muse-spark-1.3-contributor-free | TBD | TBD | TBD after Prompt 2 | disjoint TBD | NOT STARTED |

Rules: two workers must not own same file; coordinator alone pushes/migrates/heavy builds.

## Wave A01+B01 (2026-09-27)
| Worker A (A01) | subagent TASK | D:\RailMateBD | packet A01 | lib/core/config/**, lib/core/supabase/** | ACTIVE |
| Worker B (B01) | subagent TASK | D:\RailMateBD | packet B01 | supabase/seed/**, lib/features/search/models/** | ACTIVE |
Base SHAs: code fabd791, docs d185dfe. Coordinator owns commits/pushes/migrations/heavy ops.


## Wave A01+B01 CLOSED (2026-09-27)
- worker-A-subagent (A01) and worker-B-subagent (B01) sub-sessions DELETED after handoff review. No dangling sessions.
- Gate: paths disjoint OK, secrets clean, schema match OK, tests 11/11, analyze clean, seed applied as migration 20260927000005, live REST verify 4/4/40 + DAC->CGP search OK.
- Code commits: 505e8fe (features) + 0d399ac (untrack .temp). B01-U1 open: no is_demo column (prefix convention for now).


## Wave A02+B02 (2026-09-27)
| Worker A (A02) | subagent | D:\RailMateBD | lib/features/auth/** EXCEPT username/ | ACTIVE |
| Worker B (B02) | subagent | D:\RailMateBD | supabase/migrations/*username*, lib/features/auth/username/** | ACTIVE |
Base SHA: code 0d399ac. UI spec: design/UI_VISUAL_SPEC.md + design/reference/.


## Wave A02+B02 CLOSED (2026-09-27)
- Both sub-sessions DELETED. Gate: disjoint OK, secrets clean, 26/26 tests, analyze clean, migration 20260927055200 applied (local==remote 6/6). Live 2-user concurrent-claim NOT TESTED (deferred to Q01). Code ba04f67.


## Wave A03+B03 (2026-09-27)
| Worker A (A03) | subagent | lib/features/auth/phone/** | ACTIVE (S04 SMS: NO provider/budget -> live SMS BLOCKED, UI+fallback only) |
| Worker B (B03) | subagent | lib/features/search/** except models/ | ACTIVE |
Base SHA: code ba04f67.


## Wave A03+B03 CLOSED (2026-09-27)
- Both sub-sessions DELETED. Gate: disjoint OK, secrets clean, 36/36 tests, analyze clean. Live SMS BLOCKED (S04 unmet). Live search query NOT TESTED on device (widget/unit only).


## Wave B04+A04 (2026-09-27)
| Worker A (A04) | subagent | lib/features/booking/seat_ui/** | ACTIVE |
| Worker B (B04) | subagent | lib/features/graphql/** + supabase/migrations/*graphql* (one file) | ACTIVE |
Base SHA: code 48ee1a3.


## Wave B04+A04 CLOSED (2026-09-27)
- Both sub-sessions DELETED. Gate: disjoint OK, secrets clean, 45/45 tests, analyze clean, pg_graphql enabled + LIVE query returns 4 stations. Device NOT TESTED.


## Wave B05+A05 (2026-09-27)
| Worker B (B05) | subagent | lib/features/booking/passenger_ui/** | ACTIVE |
| Worker A (A05) | subagent | supabase/migrations/*booking*, supabase/functions/book-trip/** | ACTIVE |
Base SHA: code b135793. Note: A05 runs parallel (file-independent from B05); skill preload infra-error, using architecture docs.


## Wave B05+A05 CLOSED (2026-09-27)
- Both sub-sessions DELETED. Gate: disjoint OK, secrets clean, 64/64 tests, analyze clean, booking_atomic migration applied (8/8 sync). LIVE concurrency proof NOT TESTED — needs service-role execution path (Edge deploy + secrets, owner step; see Q02).


## Wave B06+A06 CLOSED (2026-09-27)
- Both sub-sessions DELETED. Gate: disjoint OK, secrets clean, 70/70 tests, analyze clean. No new deps (qr/pdf deferred). No migrations. Device NOT TESTED.


## Wave B07+A07 CLOSED (2026-09-27)
- Both sub-sessions DELETED. Gate: disjoint OK, secrets clean, 79/79 tests, analyze clean. cancel-booking Edge NOT DEPLOYED; post-media bucket existence NOT VERIFIED (policies applied); live proofs deferred to Q01/Q02.

