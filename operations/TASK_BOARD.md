# Task board — coordinator updates this each pass

## Latest — P41 publication (2026-11-23)

Owner authorized controlled publication and one new signed +28 on 2026-11-21;
execution was 2026-11-23. The 18 reviewed app paths are committed and pushed as
`a3d2c30`, source CI succeeded, and committed-HEAD local checks passed. Release
and artifact gates are recorded when observed, not predicted.

| Task | State | Evidence / next gate |
|---|---|---|
| P41 original implementation + signed release | HISTORICAL CI; NOT CLOSURE | 8df1654/+27, pre-fix630/21/11; known packaging and Telegram defects |
| P41 corrective source publication | PUBLISHED | a3d2c30, exact18 paths, CI 45212454835 success; local committed-HEAD 639/33/11, format214/0, analyze clean, deno fmt4/0 |
| P41 documentation reconciliation | PUBLISHING | README/matrix/acceptance/current/closure/ledger/guides reconciled; secret scan0, diff-check0; docs published after this record |
| Telegram hosted setup + real contact + teacher acceptance | BLOCKED_OWNER | Migration staged, functions not deployed, bot not configured; no live provider proof |
| Google requirement | BLOCKED_OWNER / DEVIATION | OSM delivered; secure JS origin, key/billing/live test or teacher acceptance needed |
| Live OpenRouter rewrite | BLOCKED_OWNER | Owner BYOK key/consent; no provider success claimed |
| Corrected signed +28 release | PUBLISHED | Run 45213896700 success; 8 assets, digests, v2 signatures, versionCode4028, map-provider.js present in all APKs/AAB; +27 preserved |
| Physical-phone smoke test | BLOCKED_OWNER | No connected physical phone; 26-row checklist unperformed; +28 emulator launch only |
| Historical exposed-credential retirement | BLOCKED_OWNER / URGENT | Review compatible API-key migration; legacy revocation unknown, not performed |

## Historical preparation board (superseded, retained)

| Task | State | Owner session | Files | Gate |
|---|---|---|---|---|
| SET-01 Preflight | TODO | main | setup logs | exact identity + memory |
| SET-02 Two repos | TODO | main | GitHub | two main branches only |
| SET-03 Hosted Supabase | TODO | main | project | URL, publishable key, costs, RLS plan |
| SET-04 AgentRouter/DeepSeek | TODO | main | private config | verified route + one cheap test |
| SET-05 Free worker models | TODO | main | roster | exact model IDs + session IDs |
| SET-06 Skills/MCP/LSP | TODO | main | .opencode | only selected servers start |
| SET-07 Flutter baseline | TODO | worker A/main | code repo | phone launch + CI |
| APP-01 Authentication | TODO | worker A | feature/auth | verified flow |
| APP-02 Trip search | TODO | worker B | feature/search | hosted data |
| APP-03 Multi-seat atomic booking | TODO | worker A | booking/backend | contention proof |
| APP-04 Demo payment and tickets | TODO | worker B | ticket | no real payment |
| APP-05 Journey Board | TODO | worker A | board | live data |
| APP-06 Station Guide | TODO | worker B | guide | media/map/animation |
| APP-07 ML and BYOK | TODO | worker A/B disjoint | ml/ai | actual model and provider |
| APP-08 CI/device/release | TODO | main | workflow/evidence | build+device truth |
