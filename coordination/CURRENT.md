# CURRENT.md — authoritative current state (2026-09-27)
State: SETUP IN PROGRESS — Prompt 1 Phases A–C partial, D–J pending
Date: 2026-09-27

- Code local: D:\RailMateBD (seed copied from kit repo-code/, git init -b main done, no remote yet)
- Docs local: D:\RailMateBD-internal (seed copied from kit repo-docs/ + coordination/ started, git init -b main done, no remote yet)
- Remote repos: NOT CREATED — blocked on `gh` install + `gh auth login` + owner CREATE confirmation
- Branches: local `main` only (verify with `git branch -a` before first commit)
- Git identity: global sa-mahi12 / sanjidamahi2005@gmail.com verified; local repo identity to be set to authenticated GitHub login/noreply at remote-create time per create_repos.sh
- Supabase: NOT CREATED/NOT VERIFIED — dashboard decision pending, no local DB, no Docker
- OpenCode: 1.18.30 works; `opencode models` lists opencode/mimo-v2.6-flash-free, opencode/muse-spark-1.3-contributor-free, agentrouter/deepseek-v4-flash — route proof pending (Prompt 2)
- Flutter/Android: BLOCKED — flutter/dart/SDK/adb missing; CI baseline (.github/workflows/flutter-ci.yml) present in seed but NOT RUN
- MCP/LSP/skills: NOT CONFIGURED — default no-MCP, Dart LSP after Flutter install
- Heavy lock: coordination/heavy.lock protocol created, no heavy op running
- Next actions:
  1. Install gh, flutter/dart, Android SDK (owner approves)
  2. `gh auth login` + verify identity, then create two private repos with explicit confirmation
  3. Supabase hosted project decision (no billing without approval)
  4. Prompt 2 model registry + route proof
  5. S08 Flutter skeleton + CI run

## Update 2026-09-27 ~10:30
- Remotes LIVE: https://github.com/sa-mahi12/RailMate-BD (PRIVATE, main only, 30a71fc) + RailMate-BD-internal (PRIVATE, main only, e869266). Local git identity set to noreply for future commits.
- Flutter skeleton (railmate_bd, bd.railmate, android-only) created; pub get OK (27 deps); analyze NO ISSUES; test: skeleton ships zero test files (nothing to run).
- CI workflow present, not yet run on push (next: commit skeleton triggers CI).
- Supabase: still NOT CREATED — owner dashboard step next. DeepSeek route proof still pending.


## Update 2026-09-27 ~10:40
- Skeleton corrected: full lib/test/android trees committed (ae70e64, 45 tracked files); flutter test 1/1 PASS; analyze NO ISSUES; pushed, CI triggered.


## Update 2026-09-27 ~10:50
- CI GREEN on ae70e64 (run 36294784667 success, artifact railmate-debug-apk). MiMo route proven. DeepSeek route FAILED (provider Invalid input) — coordinator = opencode models for now.
- NEXT OWNER STEP: create hosted Supabase project in dashboard (region/billing/SMS decisions), then S03/S04 packets. No app feature work started.


## Update 2026-09-27 ~11:00
- DeepSeek coordinator route FIXED + PROVEN (ROUTE_OK). Coordinator may now use agentrouter/deepseek-v4-flash (cap 256K).


## Update 2026-09-27 ~11:30
- Supabase project linked: psuzlyingfmstnyfvlnj (RailMateBD_samahi, Singapore).
- Migrations applied via CLI (4 files): initial_schema, rls, booking_rpc, storage_policy. Remote DB up to date.
- Docker not needed for hosted push; local dev shadow DB requires Docker (optional).


## Update 2026-09-27 ~11:20
- A01 DONE (bootstrap slice + 6 tests), B01 DONE (seed 4/4/40 live + 4 model tests). Code at 0d399ac. Next packets: A02 (email auth) + B02 (usernames) — predecessors met.

