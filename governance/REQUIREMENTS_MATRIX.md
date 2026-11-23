# Course requirements — 24-row acceptance matrix

The source is the user-provided teacher screenshot, not the earlier RailMate plan. Every listed implementation is a PROPOSAL until verified. `#20=EXEMPT`; `#24=NOT ANNOUNCED`. No hardcoded mock equals a real provider demonstration.

| ID | Teacher requirement | Minimal integration | Evidence to mark PASS | Current status |
|---|---|---|---|---|
| R-01 | ERD scalable PDF | docs/erd/railmate.mmd, generated scalable PDF | ERD exported as PDF with all logical entities, cardinalities and relationships legible at 200% zoom. | VERIFIED (R01 PDF) |
| R-02 | Real-time comments on own DB | Journey Board comments channel | Two accounts see a newly submitted comment without explicit refresh; source is Supabase Realtime and persistent Postgres. | VERIFIED 2026-11-14 (LIVE API + EMULATOR): two signed-in clients, A subscribed, B inserted then deleted -> A observed `insert,delete` (`tool/live_board_probe.dart`); on the emulator a comment added in the app appeared and was deleted from the UI |
| R-03 | Live like/dislike count | Journey Board reactions | Like then dislike changes one user reaction and both clients see correct aggregate counts. | VERIFIED 2026-11-14 (LIVE API + EMULATOR): same probe saw `insert,update,delete` on `post_reactions` (LIKE -> DISLIKE -> removed); emulator showed the like count moving 1 -> 2 after one tap and aggregates recomputed from rows |
| R-04 | Live unique username | registration usernames lookup + unique index | Concurrent same-normalized-name registration produces exactly one owner; availability is never sole protection. | CODE-COMPLETE (UNIT + previously observed HOSTED SCHEMA); schema enforces normalized uniqueness. A live concurrent registration race was not demonstrated; do not call that criterion PASS. P41 reconciles the acceptance table to this narrower claim. |
| R-05 | Email and phone verification | Supabase email OTP; proposed Telegram contact-sharing alternative; legacy SMS retained | Both real verification flows demonstrated; teacher approves any SMS substitution; no fake OTP. | PARTIAL / BLOCKED_OWNER (2026-11-23): historical Mailjet/email OTP evidence in P39/P40. The reviewed account/lifecycle/retry/format repairs are now published in `a3d2c30` and shipped in signed `+28` (639 Flutter, 33 Deno, 11 Node at that commit). Still not hosted-applied: migration not applied, functions not deployed, no bot/webhook/live contact proof and no teacher acceptance. Method telegram_contact; never phone_confirmed_at. Legacy SMS provider-blocked. |
| R-06 | Text boxes and dropdowns | search + registration + passenger forms | Multiple text and selectable form inputs validate and persist values. | VERIFIED |
| R-07 | Interactive real-time rating | Journey Board 1–5 ratings | Per-user rating changes update aggregate on second client without reload. | VERIFIED 2026-11-14 (LIVE API + EMULATOR UI): two signed-in clients observed post_ratings insert,update,delete without refresh; hosted publication membership and cleanup recorded in qa/COURSE_ACCEPTANCE_2026-11-14.md. Not TWO DEVICE evidence and not a new P41 live run. |
| R-08 | Pagination | Board cursor pagination five rows | Stable cursor loads next page without repeat/skip for fixed data snapshot. | VERIFIED 2026-11-14 (UNIT + EMULATOR): cursor tests pin page size 5, stable cursor and no duplicates; emulator listed posts and loaded the next page |
| R-09 | External audio/video embed | Station Guide YouTube embed | Real external video visibly plays in Android WebView. | VERIFIED 2026-11-20 (EMULATOR, `+25` and `+26`): a licensed CC BY-SA 4.0 Bangladesh railway clip is bundled in the APK (`web-guide/media/coxsbazar-express-480p.webm`, 4,039,910 B, attribution in `web-guide/media/README.md`) and plays in the page's own HTML5 player to `0:20 / 0:20` with no network. The YouTube iframe was tried and fails at this origin ("Error 153" - `file:///android_asset` sends no Referer); the Wikimedia streaming fallback then failed with HTTP 403 + `text/html` (`net::ERR_BLOCKED_BY_ORB`); both attempts are documented rather than hidden. `test/guide_f15_test.dart` guards the bundled path, the on-disk size, the licence notice and the absence of any remote media host |
| R-10 | Google Maps / iframe | Station Guide optional Google API layer; delivered Leaflet/OSM | Embedded map locates sample station in Android WebView; provider substitution requires acceptance. | DEVIATION (2026-11-23): OSM proven on +26 EMULATOR only. The +27 packaging failure is repaired in `a3d2c30`: signed `+28` APKs/AAB verifiably contain `web-guide/map-provider.js` byte-identical to the committed blob, and the actual-bundle regression test passes. No new rendering observation exists for `+28` (the guide needs an authenticated session), and optional Google config/fallback UNIT tests still do not prove Google rendering. No key/billing or reliable JS referrer at file:///android_asset; Android-app restrictions cannot authorize Maps JavaScript. Teacher acceptance of OSM or secure-origin work plus live proof still required. |
| R-11 | Session or JWT auth | Supabase Auth session/JWT | Session restores, expires/refreshes safely, logout blocks protected data. | VERIFIED (F08/F20 live JWT); 2026-11-04 live: password login + global logout revoked the refresh token (refresh HTTP 400). Access JWT expires on schedule by design |
| R-12 | TFLite/equivalent on-device ML | TFLite search ranking | Bundled .tflite runs on Android and visibly changes scores with different input. | VERIFIED 2026-11-14 (UNIT + EMULATOR): `assets/models/ranker.tflite` is bundled and `trip_ranker.dart` runs a real interpreter; emulator search results carry "ML - ordered on-device by the bundled ranking model" |
| R-13 | File upload + cloud storage | Supabase Storage post image | Image bytes uploaded to protected bucket and visible according to policy. | VERIFIED (F20 live); re-confirmed 2026-11-04: authenticated upload to own `post-media` folder, public read 200, own delete |
| R-14 | Datepicker | departure date | Picker selects date and invalid old dates are rejected. | VERIFIED 2026-11-14 (UNIT + EMULATOR): picker bounds tests plus a device run where past days are disabled, the window reads "Up to 5 Dec, 2026" and a picked future date loads results |
| R-15 | GSAP / Framer Motion | Station Guide GSAP | Visible entrance animation observed in embedded HTML page. | VERIFIED 2026-11-14 (EMULATOR): the bundled page loads GSAP 3.12.5 from CDN and cards animate in; the `typeof gsap` guard keeps the static fallback when the CDN is unreachable |
| R-16 | SASS or Tailwind | Station Guide SASS | SCSS compiled to CSS and loaded by embedded page; unused SCSS does not count. | VERIFIED (F15) |
| R-17 | Git / modern workflow | GitHub single-main direct commits | Authenticated owner commits, pushes and has traceable history; no extra branch or PR. | VERIFIED (single-main) |
| R-18 | GraphQL / modern API layer | Supabase pg_graphql | One real authenticated query returns stations from hosted DB. | VERIFIED layer (live pg_graphql). Advisor 0026/0027 exposure is intentional and RLS-gated (2026-11-04 review) |
| R-19 | RESTful / SOAP API | Supabase generated PostgREST | App calls real hosted REST endpoint through SDK/network layer. | VERIFIED (F08/F20 live) |
| R-20 | Crystal Report — exception | none | Explicit exception; mark EXEMPT and do not fabricate integration. | EXEMPT |
| R-21 | Modern frontend | Flutter Android | Native app launches on phone and relevant screens respond. | EMULATOR VERIFIED (historical signed +25/+26); PHYSICAL PHONE PENDING. Signed `+28` installs and launches on an Android 15 x86_64 AVD and reaches the login gate, and the installed base APK is byte-identical to the verified release asset; the historical +25/+26 screen tour was not repeated and no map screen was opened. No physical device is connected, so physical-phone acceptance is still unperformed. App docs/qa/physical-device-checklist.md has 26 unperformed checks. |
| R-22 | Containerization or deployment pipeline | GitHub Actions CI | Hosted CI actually analyzes/tests/builds debug APK; Docker not needed. | VERIFIED (CI green) |
| R-23 | Generative AI feature | OpenRouter user BYOK rewrite | User supplies/removes key, action calls real LLM and handles errors without breaking booking. | CODE-COMPLETE / LIVE PROVIDER DEMONSTRATION PENDING (2026-11-21): 12 audit tests at 8df1654 cover key removal, consent/request handling, timeout, masking, no logging and source-level booking independence; existing HTTP tests are mocked. Owner enters a key privately in-app; no live OpenRouter success claimed. |
| R-24 | TBD additional task-specific | future decision gate | Record teacher announcement and implement only after scope approval; currently NOT ANNOUNCED. | NOT ANNOUNCED |

## Pass discipline
A requirement is PASSED only when a saved dated result references a precise source commit, test or actual device observation, backend project reference redacted as appropriate, and relevant screenshot/log. A green unit test proves the unit only. Unavailable SMS billing or provider configuration must be BLOCKED and brought to instructor; do not mark skipped as passed.

### 2026-11-04 demo-readiness note
Device/emulator proof remains dropped by the owner (P34/P35 SUPERSEDED), so
"device proof dropped by owner" rows are code-complete only; their absence is
not a failing test result. On this date the hosted backend was re-verified
directly over the public API with a seeded demo account: password login, own
`post-media` upload + public read + delete, own post/comment/reaction inserts
under RLS, global logout revoking the refresh token, and one Mailjet recovery
email dispatch (HTTP 200). Inbox delivery and SMS OTP remain unverified.
Multi-passenger booking was also exercised live through the deployed Edge
Functions: the declined-simulation path wrote nothing, a 2-passenger booking was
CONFIRMED with both seats bound, cancellation released both seats, and one
CONFIRMED 2-passenger demo booking was left in place.

### 2026-11-14 course-closure note
Rows marked VERIFIED above were re-opened on this date and are backed by dated
evidence in `qa/COURSE_ACCEPTANCE_2026-11-14.md`:

- LIVE API: two synthetic signed-in clients against the hosted RailMate project
  (`tool/live_board_probe.dart`) observed `post_comments` `insert,delete`,
  `post_reactions` and `post_ratings` `insert,update,delete`; every synthetic
  account, post, comment, reaction and rating was then deleted.
- HOSTED SCHEMA: migration `20261114142438` added `post_ratings` to the
  `supabase_realtime` publication (verified in `pg_publication_tables`) and
  `refresh_demo_horizon(20)` restored the full demo window to 2026-12-04 with
  bookings and occupied seats unchanged.
- EMULATOR: the published signed release APK (not a debug build) was installed
  and driven through login, profile, board rating/like/comment, search,
  datepicker, station guide, map and video. Physical-phone capture remains
  owner-side; no row here claims TWO DEVICE evidence.
- R-10 stays a DEVIATION on purpose: the map is Leaflet/OpenStreetMap, not
  Google Maps, because no Google Maps key or billing approval exists and an
  untested iframe would be a fabrication. The OSM map itself renders on the
  installed `+26` release (EMULATOR: Dhaka tiles, zoom controls, marker popup,
  and a station switch to Chattogram) after the blank-map defect was found and
  fixed in `6e3ce42`.

### Coverage IDs
The appendix contains generated planned cases `R-xx-Tyyy`; select smoke cases for every CI run, then full relevant cases before viva. Each appendix scenario is *not* a test result.

### 2026-11-21 P41 closure addendum

Owner authorized controlled publication and signed +28. Source targets
1.0.0+28; committed-HEAD tests, CI, artifact inspection and new-build map
observation remain gates, not yet evidence. Historical statuses below do not
mean authorization is still pending. R-20/R-24 remain unchanged.

`coordination/P41_FINAL_CLOSURE_2026-11-21.md` records release +27 from
`8df1654`, 630 Flutter tests, 21 mocked Telegram-update tests and 11 Node tests
(exit 0), plus the local downloaded-APK hash/signature/version checks. No P41
hosted migration, function deployment, provider call, key rotation or physical
device test was performed. R-20 EXEMPT and R-24 NOT ANNOUNCED remain unchanged.

**Corrective addendum:** the counts above are pre-fix/historical; +27 has the
independently observed missing-provider asset and reviewed Telegram defects.
Uncommitted repairs against8df1654 passed full639 Flutter, Deno29 mocked-update
+4 mocked-handler, Node11, format214/0 and clean analyzer. No repaired-tree CI,
APK build/publication or runtime proof exists; coordinator gates still pending.

### 2026-11-23 publication addendum

Source `a3d2c305dc0a96bd952abffd8eaec3349be87f5b` publishes exactly the 18
reviewed app paths; CI run 45212454835 passed and committed-HEAD reruns were
Flutter 639, Deno 33, Node 11, format214/0, analyzer clean, all exit 0.
Signing certificate, package and version are unchanged. One signed release
`v1.0.0+28` (run 45213896700) supersedes `+27`, which is preserved with
identical asset digests. No requirement row is upgraded to PASS by publication:
committed code, an installed artifact and a green unit suite do not demonstrate
hosted verification, provider rendering, two-device behaviour or physical-phone
acceptance. R-20 stays EXEMPT and R-24 stays NOT ANNOUNCED.
