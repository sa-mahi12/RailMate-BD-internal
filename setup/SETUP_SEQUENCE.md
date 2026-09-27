# Milestone 0 — installation and cloud setup sequence


**Rule: no app implementation before steps S0–S9 are resolved and logged.** Setup is a sequence with observable acceptance gates, not a single giant shell script. The kit's script defaults to read-only/dry-run unless you deliberately invoke a creation command.

## S0 — machine constraints and credential hygiene
Run `bash setup/preflight.sh` inside WSL or an equivalent shell. Record physical RAM, WSL MemAvailable, disk space, CPU count, Flutter/Dart/Android SDK availability, Node, GitHub CLI, OpenCode, Supabase CLI, Git identity and network. Do NOT paste token output. Have one terminal for coordinator and two worker terminals at most. A missing tool is a blocker to install before proceeding; do not install Docker or start a local database. Configure WSL memory limits only after inspecting available physical RAM and the observed FindBack failure; no universal setting should be guessed.

## S1 — GitHub authentication and identity
Use `gh auth login` interactively and `gh auth status` to verify the correct account. In the setup script, query `gh api user` and derive name/email from a verified account email or GitHub account-specific noreply address. Confirm both repos will belong to that login, not to an unrelated organization. Never hardcode email copied from previous FindBack commits. If multiple GitHub accounts are signed in, stop and select one explicitly. The default script requires a confirmation phrase before remote repository creation.

## S2 — two private repositories, one branch each
Run `bash setup/create_repos.sh <workdir>` from the ZIP root. It copies seed code and internal docs to adjacent folders, initializes `main` only, records user identity, commits and pushes using the authenticated GitHub account. It does not make a pull request or feature branch. If either repo already exists, stop without overwriting it: the owner or coordinator must inspect and decide whether to reuse. Verify `gh repo view OWNER/RailMate-BD` and `OWNER/RailMate-BD-internal`, `git branch -a`, `git ls-remote --heads origin`, and the account metadata for both commits. Do not use `--force`.

## S3 — hosted Supabase (not local)
In the Supabase dashboard create one project under the owner account/organization; choose region by actual service accessibility and cost; save the **project ref** privately. Decide whether phone verification requires a paid SMS provider now. Obtain Project URL and **publishable** key; `service_role` stays backend-only, never in APK or GitHub source. Fill non-secret public config via a locally ignored `app.env.json` or `--dart-define`; do not commit credentials. In a staging/new empty project, plan migrations with SQL and RLS review before apply; for an already populated project, take backup and enumerate affected tables first. Do not run `supabase start` or local Postgres. For the initial milestone, no live SQL is required until the schema packet is approved.

## S4 — Supabase CLI and connection
`supabase login` is interactive; after signing in, `supabase link --project-ref <verified>` associates the source checkout with hosted project. Only main/coordinator may link or apply migrations. Disable automatic live database writes in MCP/agent permissions. Verify the project ref against dashboard and `supabase projects list`. Keep CLI access tokens out of shell transcript/logs. Select migrations-on-main with manual `workflow_dispatch` review gate if using hosted CI; CI should not silently mutate production on each push.

## S5 — OpenCode base version and provider route
`opencode --version`, `opencode run --help`, `opencode models opencode`, and `opencode models agentrouter` establish real flags/IDs. Use AgentRouter's current official setup instructions or authenticated dashboard to configure the key **through OpenCode auth/environment**, not a literal in the checked-in file. AgentRouter DeepSeek model IDs can change; inspect `opencode models agentrouter` before setting main model. Official AgentRouter docs were web-blocked at kit authoring; do not treat third-party proxy instructions as canonical. Run a tiny non-project request to prove the route works, record response without private key.

## S6 — workers and compaction
Validate actual `opencode/mimo-v2.6-flash-free` and `opencode/muse-spark-1.3-contributor-free` against provider listing; use exact IDs returned by your installed client. Start only two unique sessions with bounded packets and see their session IDs in the roster. Run one short pause/resume test using `opencode run --session <ID> ...` if supported; else follow that version's CLI semantics. Ensure `AGENTS.md` and current private state are loaded at each new turn and after compaction; never trust auto-summary to remember the two-repo invariant.

## S7 — MCPs, skills and LSP
Start with NO MCP servers enabled by default, then optionally enable GitHub read-only inspection and Supabase read-only inspection after verifying official packages and token scopes. Too many MCPs inflate context and consume RAM. Use project `.opencode/skills` for local procedures; Flutter/Dart analysis server is enough initially. Verify it works via `flutter analyze` before manually adding additional LSP processes. Deny write DB and GitHub mutations to workers even if an MCP exposes them; tool availability is not authorization. The MCP plan names actual gates rather than guessing unverified npm package names.

## S8 — CI baseline
After Flutter SDK is present, run `bash scripts/create_flutter_skeleton.sh` in the code repo. Add Supabase SDK only after project configuration is ready. The `.github/workflows/flutter-ci.yml` should run on push to main; inspect workflow log for checkout/pub get/format/analyze/test/build debug APK. GitHub Actions is the substitute for Docker. A skipped job because no `pubspec.yaml` yet is not proof that an APK was built.

## S9 — release of execution gate
Fill `SETUP_GATE.md`: two repos confirmed, only main branches, correct Git identity, hosted project URL, publishable key path, auth and storage policy approved, OpenCode actual provider and worker IDs verified, MCP/LSP/skills smoke-tested, CI baseline passes, machine health good. Only then mark app build `IN PROGRESS` and dispatch first narrow feature packet.
