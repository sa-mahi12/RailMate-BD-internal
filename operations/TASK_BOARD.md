# Task board - coordinator updates this each pass

## Latest - P43 official timetable + community completion (started 2026-11-25)

Revised handoff: coherent UI, source-backed official timetable as the default
discovery mode, completed Journey Board (post edit/delete + media cleanup,
comment replies/edit/delete/report, blocks, receipts), a real staff moderation
console, Norfold as reference only, and **no hosted database change** until the
owner approves the gate. Baseline app `f058afc`, docs `3b3812b`, release
`v1.0.0+29` preserved.

| Task | State | Evidence / next gate |
|---|---|---|
| Official timetable dataset | DONE | Both PDFs SHA-256 hashed; 130 intercity rows transcribed with page+serial; 4 ambiguous printed rows excluded; mail/express + commuter tables recorded as not imported; builder validates times/stations/serials |
| Official timetable app mode | DONE | `lib/features/timetable` models/repository/query/list/detail/station screens + home entry; analyze clean; 21 new tests in `test/timetable` |
| Official timetable public page | LIVE | `timetable.html` on Pages, 126 published rows rendered from `site/data/official-timetable.json`; 10 Node tests; deploy run 45562642693 success at `0e8c495` |
| Post edit/delete + My Posts | IN PROGRESS | worker packet: edited_at, attachment position, cleanup table, draft migration (not applied) |
| Comment replies/edit/delete/report | IN PROGRESS | worker packet: one-level threading, realtime update/delete, draft migration (not applied) |
| Moderation console + roles + blocks + receipts | IN PROGRESS | worker packet: staff_roles/capabilities, audit, visibility, sanctions, blocks, RPCs (draft only) |
| Hosted database | FROZEN | `D-021`; no DDL/DML/Storage/auth/secret change in P43 before owner approval |
| New Android release | NOT STARTED | Owner approval required; `+29` preserved |
| UI polish + before/after screenshots | PENDING | needs the board/admin screens to land first |
| Full CI + release candidate | PENDING | after integration and the UI pass |
| Owner database gate | BLOCKED_OWNER_APPROVAL | present migration set, rollback, data impact, recovery point, post-apply checks |

## P42 social web publication (2026-11-24/25)

Owner asked for a genuinely functional academic social transport prototype: a
live site backed by Supabase, real cross-account posts with permanent links,
multi-format attachments in Storage, public author identity, preserved
comments/likes/dislikes/ratings and reporting, proven with two independent
accounts. Published on `main` in seven direct commits (`c8565cd` … `c556e5d`).

| Task | State | Evidence / next gate |
|---|---|---|
| P42 hosted schema (`20261124000001_p42_social_web.sql`) | APPLIED | Management API HTTP 201 on `psuzlyingfmstnyfvlnj`; recorded in `supabase_migrations.schema_migrations`; attachments/views/reports/rate limits/bucket allowlist/realtime membership |
| P42 app feature (attachments, permalinks, profile, reporting, share) | PUBLISHED | 675 Flutter tests, analyze clean, format 229/0; CI success 45451672940 / 45451935841 |
| P42 public website | LIVE | https://sa-mahi12.github.io/RailMate-BD/ by deploy-pages; feed, post and profile pages verified in real Chrome with real data |
| P42 cross-account evidence | HOSTED PASS | run `mwv0r1ce33dd`, 22 checks: A publishes image+video+PDF+2 links, B reads/comments/likes/rates, cross-delete denied, report hidden from A, foreign storage path and self-report rejected, repeat report updates in place |
| P42 independent review | NO CRITICAL; IMPORTANT FIXED | storage_path was shape-only checked (fixed by `post_attachments_path_owner_chk`); cap-on-update, server-clock created_at, report upsert and self-report guard also fixed; three Dart-level follow-ups accepted for the next release |
| P42 uploaded-video playback | BROWSER PASS | deployed page, 848x480, `paused=false`, same element still playing after 37.7 s across a 20 s refresh boundary |
| Signed +29 with the P42 app changes | PUBLISHED + VERIFIED | release run 45453959869 from 84dd332; universal APK SHA256 matches the GitHub digest and SHA256SUMS, versionCode 29, apksigner exit 0 on the +28 certificate, P42 symbols inside libapp.so, `+28` untouched |
| Android device run of composer/attachments/deep links | BLOCKED_NO_DEVICE | Unit-tested only; no phone or emulator tap-through in this packet |
| Per-post Open Graph previews | NOT CLAIMED | Static hosting has no per-post HTML; documented in `docs/P42_SOCIAL_WEB.md` |

## Previous - P41 publication (2026-11-23)

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
