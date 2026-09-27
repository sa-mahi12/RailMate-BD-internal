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
