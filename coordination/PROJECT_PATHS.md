# PROJECT_PATHS.md — native Windows (2026-09-27)

- Code repo (local): `D:\RailMateBD` → intended remote `RailMate-BD` (private, main only)
- Docs repo (local): `D:\RailMateBD-internal` → intended remote `RailMate-BD-internal` (private, main only)
- Kit source (read-only): `C:\Users\sanji\Downloads\Mahi_Number_9\RailMate_BD_Execution_Kit\RailMate_BD_Execution_Kit`
- OpenCode config: `%USERPROFILE%\.config\opencode\opencode.jsonc`
- OpenCode backup: `%USERPROFILE%\.config\opencode\opencode.jsonc.bak-20260927`

Rules:
- All scripts/instructions must use Windows paths + PowerShell. Do NOT copy old /home/... WSL paths.
- Exactly two repos, each exactly one branch `main`, no PRs, no feature branches, no force-push.
- AGENTS.md path note: repo-code AGENTS.md references `../RailMate-BD-internal/` (hyphen names). On this machine the adjacent folders are `D:\RailMateBD` and `D:\RailMateBD-internal` (user naming). Treat them as the same two-repo pair; do not create extra hyphen-named folders on D:.
