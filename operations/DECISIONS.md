# Decision register
D-001: Two repositories, code + private internal, only `main`, no PRs. APPROVED.
D-002: Hosted Supabase single backend, no local business database or Docker. APPROVED.
D-003: Flutter plus embedded page for GSAP/SASS. OWNER APPROVED; TEACHER ACCEPTANCE PENDING.
D-004: Multi-passenger/multi-seat 1–4 with atomic reservation, mock payment. APPROVED.
D-005: AgentRouter DeepSeek main; verified OpenCode free MiMo/Muse worker models. APPROVED IN PRINCIPLE; ACTUAL ROUTE/MODEL TEST PENDING.
D-006: OpenRouter user BYOK, key not bundled or cloud-stored. APPROVED; security tradeoff documented.
D-007: Tiny TFLite search ranking. APPROVED; trainer/model/runtime actual validation pending.
D-008: Phone OTP requires actual SMS gateway and charges. OWNER COST PROVIDER CHOICE PENDING.
D-009: No bot/AI commit attribution trailers; GitHub identity from actual logged in user. APPROVED; course AI disclosure still applies.
D-010: No worker can commit, push, migrate database, change CI secrets, or build locally without coordinator gate. APPROVED.

## P41 continuation — 2026-11-21

D-011: Owner P41 request implements Telegram contact sharing as proposed SMS
alternative; method telegram_contact, no auth.users.phone_confirmed_at writes.
Code complete, hosted setup/live proof and TEACHER ACCEPTANCE PENDING. Original
SMS requirement is not silently removed; legacy SMS lane retained/provider-blocked.

D-012: OSM remains delivered; optional Google JS provider is UNVERIFIED. A key
alone is insufficient: Website restrictions need a reliable HTTP referrer,
absent at current file asset origin. Secure-origin/provider work needs separate
owner approval; do not weaken restrictions. R-10 DEVIATION stays.

D-013: Historical service-role JWT exposure remains an urgent owner risk;
current revocation unknown. Corrected runbook uses reviewed new API-key
compatibility, legacy-key retirement and JWT-signer revocation, not custom
SUPABASE_ secrets. No rotation, hosted deployment or visibility change authorized
by this continuation. Only coordinator publishes exact reviewed doc paths.

D-014: +27 artifact hash/signature/versionCode checked; no connected device,
therefore installation/runtime remains NOT VERIFIED. P40 emulator evidence
remains historical and does not become physical/TWO DEVICE proof.

D-015: P41 review and actual APK inspection established four Telegram defects,
incorrect masked-storage disclosure and omitted map-provider.js. Single local
corrective pass on8df1654, no new feature expansion: auth identity+generation
guards, nonoverlapping polls, leased retry/completion, exact-update consume
recovery, digits-only own contact and accurate disclosure; actual-bundle asset
fix. Full639 Flutter/Deno29+4 mocked/Node11 exit0. +27 must remain historical
and must not be overwritten; source publication and a newly numbered signed
release require coordinator review/decision. No deployment or migration applied.

D-016 (2026-11-21): Owner explicitly authorized controlled publication of the
18 corrective app paths and nine documentation paths plus one new signed
v1.0.0+28. Source version was 1.0.0+1; +27 used the workflow build-number
override. +28 is now the source target. Review/security gates precede exact-path
commits; both repositories remain PUBLIC and visibility is unchanged. Public
publication copies omit account details, local machine paths and session IDs;
original local evidence is preserved outside Git. Historical public credentials
and metadata remain disclosed risks, not a clean-history claim. No new hosted
or provider action is authorized by publication. Never dispatch/overwrite +27.

D-017 (2026-11-23): D-016 executed for source. Exactly the 18 reviewed app paths
were committed as a3d2c305dc0a96bd952abffd8eaec3349be87f5b and pushed to `main`
under the owner identity; generated `.flutter-plugins-dependencies` and
`.serena/` were excluded. Source CI 45212454835 passed, and committed-HEAD
reruns (Flutter639, Deno33, Node11, format214/0, deno fmt4/0, analyzer clean)
exited0. Final-tree secret rescans were0. One signed +28 release run
(45213896700) was dispatched on that SHA; +27 was preserved and never
redispatched. Documentation publication follows only after artifact evidence is
written. Hosted deployment, credential rotation, provider calls, visibility
changes and device actions remain outside this decision.

D-018 (2026-11-23): The +28 run succeeded and the release was verified rather
than assumed: eight assets match GitHub digests and SHA256SUMS; all four APKs
verify v2 with the unchanged certificate; versionCode4028/package correct;
manifest and unsigned provenance name the exact commit and run; and
map-provider.js is byte-identical to the committed blob in every APK/AAB. On an
emulator the signed APK installs (installed base APK byte-identical), launches
and reaches the login gate. Because the Station Guide requires an authenticated
session, +28 map rendering and all physical-phone checks remain unobserved and
are not claimed. Publication of the nine documents is the only remaining P41
action; hosted/owner gates are unchanged.

D-019 (2026-11-25): Revised P43 adopts an official published timetable as the
default discovery mode and keeps the academic demo booking as a clearly
separated mode. Only published fields are stored (train number, published name,
weekly off day, origin/destination and their printed times, source document,
page, printed serial, timetable number 54, effective 2025-03-10). Intermediate
stops, fare, platform, delay, ETA, occupancy and live status are never inferred;
the only external action is the official e-ticket portal. 130 intercity rows are
imported; the mail/express and commuter tables are explicitly not imported yet
and both the manifest and the UI state that gap. APPROVED by the handoff scope;
dataset expansion is a follow-up, not a silent omission.

D-020 (2026-11-25): Norfold is reference-only for P43. Its LICENSE.md is
PolyForm Noncommercial with a named copyright holder and the handoff requires a
rights-holder authority check before copying, so no Norfold file, identifier,
branding, SQL migration or asset is copied. Behavioural patterns (queue, case
review, audit, block, receipts) informed independent Dart and SQL. The Norfold
repository is not modified.

D-021 (2026-11-25): Production Supabase is frozen for P43 implementation. No
hosted DDL/DML, Storage write, auth change, RLS/grant/trigger/Realtime change,
Edge Function deploy or secret change until the full release candidate passes and
the project owner approves the database gate. Draft migrations may be committed
but not applied; the gate packet must list exact objects, rollback/forward repair,
data impact, recovery point and post-apply checks. No new Android release is
published before owner approval; v1.0.0+29 is preserved.
