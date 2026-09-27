# Mandatory post-pass control gate
Run after EVERY worker packet and before any second packet, commit, push, claim or handoff.

1. `git status --short --branch` in both repos; ensure only `main` and no worker-created branches/PRs.
2. List exact changed files; compare to worker's exclusive path claims and packet. Stop on overlap or unexpected deletion.
3. Run secret scan; reject .env, private keys, service role, JWT, OpenRouter/AgentRouter keys, actual user data or keystore in changes.
4. Run focused formatter/analyzer/tests; if no Flutter project yet, record NOT APPLICABLE rather than PASS.
5. If a local heavy operation must run, coordinator acquires the exclusive heavy lock; do not run a full Android build concurrently with free worker processes on a constrained PC.
6. Read worker evidence: commands, exit codes, dates, commit base, mocks vs live, successful vs blocked.
7. Run requirement impact check. Update matrix, decisions, task board and CURRENT in documentation repo.
8. Commit only reviewed code paths on `main` using verified owner identity, then push `origin main`; separately commit private docs on its own `main`. Never `git add -A` as an automatic shortcut.
9. Capture resulting commit SHA and `git status` after push. If push fails, do NOT claim remote success; resume from local state without re-creating commit.
10. If CI claims build success, capture job URL/hash and artifact; only installed-on-phone evidence establishes real device pass.
