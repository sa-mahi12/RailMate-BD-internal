# Lean OpenCode toolchain configuration and permissions


**Minimal first:** Git CLI/gh CLI and Flutter's Dart analysis are more dependable than installing every available MCP/LSP. Install only when a task has a demonstrated need. Every MCP can add tools/context, external process startup, credentials and failure modes; six heavyweight servers undermine the resource goal.

**MCP stage A (optional read-only):** GitHub MCP to inspect two repos/issues/actions, Supabase MCP limited to the exact project in read-only mode if officially supported. Verify current official package/version/auth procedure before installation; do not paste API tokens into OpenCode JSON or model prompts. Disable both for worker sessions by default if their permissions cannot prevent write operations. Never let a worker run DB SQL through MCP even when a tool is present. Prefer `gh` for low-context repository inspection and Supabase dashboard/CLI for setup.

**MCP stage B (only if needed):** Context7 or documentation lookup MCP for library docs; not required if official docs and project-local skills suffice. No Playwright browser MCP unless web-guide tests actually need it; Android device tests use Flutter/ADB. Do not enable generic filesystem/terminal MCP duplicating built-in OpenCode tools.

**LSP:** Flutter uses Dart analysis server from installed Flutter SDK. Run `flutter doctor`, `dart --version`, `flutter analyze`; OpenCode's native LSP support or editor DAP can be used if actual schema/config says so. Web-guide needs TypeScript/JavaScript language service only if JS gets nontrivial; our one HTML page should be tiny. SQL linting through pg tooling/CI is preferred to a permanent local SQL server. No JVM/Java LSP for minimal Flutter project unless editing native Android code becomes necessary.

**Skills:** project-local `.opencode/skills/` has typed frontmatter and task-specific instructions: repo governance, Flutter slice, Supabase RLS, seat transaction, evidence and handoff, privacy/BYOK, release. Workers load just one relevant skill, not every skill in each prompt. One session's skills are not permission to exceed file ownership. Skills are in code repo for OpenCode discovery; full explanation stays in private docs repo.

**Configuration compatibility:** OpenCode v2 examples in official docs place MCP under `mcp.servers`, agents under `agents`, permissions as ordered lists, compaction `keep.tokens`/`buffer`; older OpenCode docs differ. Validate against the actual binary and https://opencode.ai/config.json before copy. Package templates contain no non-empty secret values and no guessed AgentRouter model listing; install script merges only safe keys after backup.
