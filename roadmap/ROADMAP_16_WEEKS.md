# Sixteen-week implementation schedule with fast parallel lanes

This schedule is an upper-bound academic plan, not a promise that every dependency can be finished automatically. The owner wants speed; the execution strategy front-loads cloud and agent setup, builds the booking vertical slice by week 7, and runs inexpensive bounded UI/backend tasks concurrently only when their interfaces and file ownership are separated. The teacher's 24 features remain traceable; we do not replace a requirement with a mock to hit a date. Workers are not allowed to build/test/commit/push autonomously. Main coordinator is the only integration owner.

## Week 1 — setup, no product features
Days 1–2: WSL/host resource preflight, GitHub identity, create exactly two private single-main repositories. Days 2–3: hosted Supabase project, project URL/publishable key, Auth settings and SMS-provider cost gate; freeze logical entities. Day 3: verify AgentRouter DeepSeek route and free MiMo/Muse IDs through actual listing plus short requests; save distinct session IDs, run resume/compaction replay. Day 4: add only necessary skills and inspect MCP/LSP; disable high-cost servers. Day 5: Flutter skeleton and GitHub Actions baseline debug build. STOP if any setup gate is unknown: a build without real URL or token policy is not completion.

## Week 2 — hosted public data, minimal runtime and contracts
Worker A (exclusive `lib/core/**`) initializes Supabase Flutter safely and one public-stations read. Worker B (`supabase/seed/**` and search model contracts) drafts 3 train trips + date-specific seats; main reviews schema/RLS and approves hosted migration. Main tests actual hosted REST/GraphQL extension availability, not a mocked API. End-of-week demo: phone launches and lists sample stations with authenticated session plumbing. No heavy local builds with two workers active.

## Week 3 — authentication and search in parallel
Worker A: email registration, deep-link confirmation, session restore/logout, protected navigation. Worker B: username reservation and source/destination/date search, with coordination on shared auth paths serialized. Real phone OTP only after provider/billing approved. Focused CI and one physical device smoke. Acceptance: two different users can register distinct names, duplicate race protected; demo route returns hosted trips. `R-05` can remain BLOCKED only with honest evidence if SMS provider unavailable.

## Week 4 — coach and forms
Worker A: coach/seat schematic in its own UI module; Worker B: passenger form/review with mapping contract frozen first. Main freezes edge-function booking request/response schema, maximum 4 passengers, distinct seat constraint and idempotency key. Acceptance: selected seats match passengers and fare in review, no backend booked writes by client.

## Week 5 — transaction first
Worker A owns atomic SQL/Edge booking logic; Worker B builds simulated payment UI using a fixture adapter, not integrated backend writes. Main reviews SQL/RLS/service-role scopes and tests in hosted staging/empty project (owner-approved) before live apply. Run conflicting seat contention and idempotency. No e-ticket polishing before backend passes. Never accidentally charge an account for fake payment.

## Week 6 — e-ticket and cancellation
Worker A builds ticket/QR/PDF based on confirmed server snapshot; Worker B builds history and whole-booking cancellation path. Main serializes shared route integration and checks multi-user privacy. End-of-week demonstration: two passengers/two seats booked atomically, PDF clearly invalid for travel, cancellation frees only correct seats; failure leaves no partial booking.

## Week 7 — minimal community board foundation
Worker A creates posts and Storage images; Worker B comments and cursor pages in separate folders. Main enables only relevant Realtime publication and verifies two-account observation. No social graph, DM, notification service, advanced feed moderation or AI chat history.

## Week 8 — ratings/reactions and Station Guide
Worker A owns ratings/reactions with unique `(post_id,user_id)` state; Worker B builds single embedded guide with real map/video and SASS/GSAP. Check teacher WebView approval; otherwise revisit design before claiming R-15/R-16. Main checks storage path privacy and aggregate consistency.

## Week 9 — tiny ML and BYOK in parallel
Worker A produces hosted-trained TFLite asset + native search inference, without local model training. Worker B builds OpenRouter secure BYOK setup and one selected-draft rewrite function. Main verifies no real key in APK/source, no service-role leak, and authorized provider request only. ML is not a fancy feature: use real inference on a tiny search ranking vector.

## Week 10 — integration and exact 24-row walkthrough
Main serializes app-wide route and theme integration and runs low-resource CI. Two workers repair separate focused defects only. Check every teacher row: real comment/ratings, phone SMS if authorized, actual video/map/animation, REST and GraphQL, no Docker, CI artifact, BYOK and ML. Crystal Report is exempt; additional item remains future announcement. Reconcile docs and code commit references.

## Week 11 — negative and concurrency cases
Run a selected suite from the huge planned-case appendix: two-user privacy, duplicate username, overlapping multi-seat booking, same idempotency UUID, retry after uncertain response, stale reaction counts, image upload RLS, GraphQL permissions and offline errors. No destructive live testing. Record true evidence grade for each.

## Week 12 — Android physical-device acceptance
Install a CI-produced APK on a real Android phone. Test login and back stack; 1–4 passenger booking; cancellation; Journey Board; Station Guide map/video; actual bundled TFLite inference; BYOK success and no-key fallback. If direct phone testing fails, the requirement remains NOT TESTED DEVICE, regardless of green CI. Fix real device bugs in targeted packets.

## Week 13 — performance and cost cleanup
Observe memory impact of WebView and TFLite asset, avoid simultaneously keeping both expensive views alive; dispose on navigation. Limit Realtime subscriptions, upload size and API response size. Review Supabase usage, SMS fees, OpenRouter user disclosure, OpenCode free quotas and CI minutes. Eliminate unused packages and heavy scripts, never remove a teacher feature to hide a cost without logging teacher gate.

## Week 14 — documentation and ERD reconciliation
Export a **real scalable PDF** from updated ERD after actual schema is applied and compared; not merely `.mmd` source. Prepare screenshots, architecture diagram, deployment instructions, provider disclosure, cost assumptions, demo test accounts, code/Docs repo links and measured limitations. Freeze API/schema changes except bugs.

## Week 15 — release rehearsal
From clean main SHAs reproduce CI and installed phone demo with network available; include one duplicate-seat race and one provider failure case. Produce debug APK with hash and CI link. Confirm only two repos, only main branches, actual account commits, no bot/AI trailers, no key in source/artifact, and that docs repo remains private. Ask teacher if additional item #24 has been announced.

## Week 16 — submission
Push final reviewed code main and private docs main, retain immutable commit SHAs and artifacts. Submit APK, source, ERD PDF, report and viva flow through required course process. No PR/feature branch/Docker/local database. If a feature remains blocked by a real external cost or instructor decision, disclose it and the attempted integration rather than claiming a fake PASS.

## Accelerated option
Once S0–S9 are actually complete, execute two low-cost workers in parallel at each disjoint stage, with CI after the pair. You may compress weeks 2–10 into several intense weeks if tests and provider availability allow; **do not** compress away the setup gate, atomic booking review, credential protection or installed-device proof. A third worker is review-only or on an independent task if measured free RAM exceeds the threshold. Faster execution comes from narrower scope and stable interfaces, not 5–6 simultaneous OpenCode processes.
