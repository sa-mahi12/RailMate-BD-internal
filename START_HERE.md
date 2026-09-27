# RailMate BD internal — Start Here


This private documentation checkout is the authority for the project, not remembered conversation text or OpenCode compaction summaries. The adjacent code checkout contains source only. Read `governance/PRODUCT_CONTRACT.md`, `governance/REQUIREMENTS_MATRIX.md`, `operations/CURRENT.md`, `operations/TASK_BOARD.md`, `operations/DECISIONS.md`, `operations/SESSION_ROSTER.md`, `operations/POST_PASS_GATE.md` before doing work. All `PASSED` statements must include a dated command, exact commit and actual stdout/exit code or device evidence. A markdown checkbox alone is not evidence.

## Execution phases
1. Owner preflight and GitHub login/identity verified; two repositories created as private single-main checkouts.
2. Hosted Supabase project created, billing/SMS decisions recorded, public URL/key obtained, no SQL yet applied without review.
3. OpenCode + AgentRouter route verified; actual free models enumerated, session rosters established, cheap MCPs/skills/LSP enabled, compaction replay tested.
4. Flutter skeleton bootstrapped locally without emulator; GitHub Actions performs builds.
5. Coordinator gives disjoint worker packets; workers edit only files, coordinator validates/commits/pushes.
6. One working booking slice before community/AI/ML/embedded web.

## Safety
Never commit secret `.env`, `service_role`, personal passenger data, keystores, OpenRouter keys, AgentRouter tokens, app signing credentials or provider cost receipts. App BYOK must never be uploaded to Supabase by default. No direct worker SQL execution against production. No unreviewed changes to RLS or financial operations. No repos/branches/PRs besides exactly two `main` branches.
