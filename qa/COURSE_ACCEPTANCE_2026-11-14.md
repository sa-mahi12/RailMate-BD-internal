# Course acceptance — 24 teacher requirements (2026-11-14)

Owner authorized controlled publication and signed +28 on 2026-11-21.
Publication is in preparation; no new CI/artifact/runtime evidence is inferred.
Historical requirement evidence below remains dated to its original source.

**LATEST CORRECTIVE STATUS (2026-11-21):** +27 remains the original8df1654
artifact, now known to omit map-provider.js and contain reviewed Telegram
account/lifecycle/delivery defects. Local uncommitted repairs passed639 Flutter,
Deno29 mocked updates+4 mocked actual-handler and Node11, format214/0/analyzer
clean. No corrected CI/build/release/hosted/device result. R-05 PARTIAL and R-10
DEVIATION remain; current closure record supersedes pre-fix wording below.

P41 revision 2026-11-21: source `8df1654`, signed release `+27`, 630 Flutter
tests, 21 mocked Telegram-update tests and 11 Node tests (exit 0). Artifact
hash/signature/version checked; +27 install/runtime not verified (no device
connected). Historical LIVE API and signed +25/+26 EMULATOR observations below
remain attached to their original builds/dates. Telegram alternative is staged,
not deployed/live-verified; Google and live BYOK remain owner-blocked. Details:
`coordination/P41_FINAL_CLOSURE_2026-11-21.md`.

Scope: the original 24 numbered teacher requirements, the later six-item
announcement, and the audit pack in
`RailMateBD_Full_Course_Closure_Autonomous_Agent_Handoff_2026-11-14.zip`.

Evidence labels used below (see `operations/EVIDENCE_TAXONOMY.md`):

- **STATIC** — source/file inspected at a named commit.
- **UNIT** — deterministic Flutter test, named file, run locally or in CI.
- **HOSTED SCHEMA** — read directly from the hosted project metadata.
- **LIVE API** — a real hosted request from a real signed-in session.
- **EMULATOR** — Android emulator with the installed signed release APK.
- **TWO DEVICE** — two physical devices; not claimed anywhere in this file.
- **BLOCKED_OWNER** — needs an owner account, provider, budget or consent.

No row is marked PASS on the strength of a checkbox or an unverified claim.

## Results

| ID | Requirement | Status | Evidence (dated 2026-11-14 unless noted) |
|---|---|---|---|
| R-01 | Scalable ERD PDF | PASS | STATIC: `docs/erd/railmate.mmd` declares 12 entities and their cardinalities; the PDF (`docs/erd/railmate.pdf`, 1 page) text-extracts all 12 with PK/FK/unique/cascade notes. HOSTED SCHEMA: exactly those 12 `public` base tables. The earlier "13 tables" count included `auth.users`, which is outside `public`; the ERD header now matches the applied schema. |
| R-02 | Real-time comments | PASS (LIVE API) + EMULATOR UI | LIVE API: two signed-in clients, client A subscribed to Postgres Changes on `post_comments`; client B inserted then deleted a comment and A observed `insert,delete` with no refresh (`tool/live_board_probe.dart`). UNIT: `test/board/comment_section_realtime_test.dart`. Emulator: see device section. |
| R-03 | Live like/dislike | PASS (LIVE API) + EMULATOR UI | LIVE API: same probe, `post_reactions` delivered `insert,update,delete` (LIKE → DISLIKE → removed). Aggregates in the app are always recomputed from rows (`ReactionState`), so an echo cannot double count. UNIT: `test/board/post_engagement_realtime_test.dart`. |
| R-04 | Live unique username | CODE-COMPLETE (UNIT + HOSTED SCHEMA); UI EMULATOR | Historical schema inspection: normalized unique index, username PK and unique user_id protect claims; RLS recorded intact. UNIT: username validation/availability/timeout tests. A live concurrent registration race was not run; P41 corrects the earlier PASS wording rather than inferring that observation from a constraint. |
| R-05 | Email + phone verification | PARTIAL / BLOCKED_OWNER | Historical email proof retained. +27 Telegram account/lifecycle/redelivery defects repaired only locally with focused23 lifecycle/account and Deno29+4 mocked tests. Full639 Flutter. Corrected schema not applied/functions not deployed or release published; no bot/contact/teacher proof. Method telegram_contact, no phone_confirmed_at write; full number protected, display masked. Legacy SMS still requires provider approval. |
| R-06 | Text boxes and dropdowns | PASS | UNIT: registration (phone/email/username/display name) and search (station fields, date) validation tests in `test/auth/*`, `test/home/home_search_screen_test.dart`; EMULATOR: forms render and validate. |
| R-07 | Interactive real-time rating | PASS (LIVE API) + EMULATOR UI | LIVE API: probe inserted 5 stars, updated to 2, deleted, and the second client observed `insert,update,delete`, rows 0 after cleanup. SOURCE: new `post_ratings` publication migration, `RatingRealtimeEvent`, shared `public:board-ratings` channel, 80 ms debounce/coalescing, `RatingState` stale-load token. UNIT: `test/board/rating_realtime_test.dart` (9), stale-load test in `test/board_f13_test.dart`. |
| R-08 | Five-item pagination | PASS (UNIT) + EMULATOR | UNIT: cursor paginator tests (`test/board_f11_test.dart`, `board_f13_test.dart`) prove page size 5, stable cursor, no duplicates. EMULATOR: Journey Board lists posts and loads the next page. |
| R-09 | External video embed | PASS (EMULATOR playback, bundled asset) | SOURCE: `web-guide/index.html` now plays a copy of the Wikimedia Commons clip "Cox'sBazar Express Train" (Frameofashik, CC BY-SA 4.0) bundled at `web-guide/media/coxsbazar-express-480p.webm` (4,039,910 B, unmodified 480p VP9 transcode) with its poster and `web-guide/media/README.md` licence notice. The earlier YouTube iframe returned "Error 153" from `file:///android_asset` (no Referer); the streaming Commons fallback was then falsified on-device: CDP on a debuggable build of `1fb40b4` showed the page's own fetch returning **HTTP 403 + text/html** from Wikimedia (rate limiting), which Chromium blocks as `net::ERR_BLOCKED_BY_ORB`, so the media element errored ~200 ms after `loadstart` (an identical instrumented run 20 minutes earlier reached `readyState 4` and played) — the failure was server-side, not code. **EMULATOR (installed debuggable build of `f20bed2`, 2026-11-18 11:14–11:18 +06):** the page autoplays from `file:///android_asset/.../media/coxsbazar-express-480p.webm` with `networkState 1 (IDLE)`, `readyState 4`, `duration 20.374`, `currentTime` advancing; the page button reads "Pause video" while playing and "Play video" when paused; screenshots `20-video-playing.png` and `20-video-paused-time.png` (the latter shows `0:18 / 0:20`). UNIT: `test/guide_f15_test.dart` fails if the source/poster leave `media/`, if any remote media host returns, if the clip on disk is missing/under 2 MB/over 8 MB, or if attribution or the retired YouTube embed returns. |
| R-10 | Google Maps / iframe | DEVIATION (interactive OSM map PASS on device) | The teacher's newest list says "Maps"; the original sheet said Google Maps. The guide ships a real interactive **Leaflet 1.9.4 + OpenStreetMap** map with a marker per station and a genuine offline fallback. **EMULATOR (`v1.0.0+26`, installed signed release, 2026-11-20 10:51 +06):** OSM tiles for Dhaka render with zoom controls, marker, attribution and the "Dhaka (DAC) DEMONSTRATION ONLY" popup; tapping the CGP chip re-renders Chattogram tiles without blanking (`shots/26-map.png`, `shots/26-map-cgp.png`). Honest history: the map box was **blank** in every earlier build, and the earlier "renders in the app WebView" claim was wrong. Root cause (`6e3ce42`): the Flutter screen injects `window.RailMateGuide.showStation(code)` after the asset loads, so `renderMap()` runs twice, and the second call cleared the container with `textContent = ''` while reusing the existing Leaflet instance — deleting Leaflet's panes, tiles, controls and attribution. Reproduced deterministically in Chromium against the same asset (7 panes / 6 tiles / 2 controls → 0 / 0 / 0 with no exception) and fixed by clearing only when the map is created, rebuilding if the panes were torn down, and calling `invalidateSize()` twice for late WebView layout. No Google API key or billing exists and no Google iframe was added untested, so "Google Maps" specifically stays a deviation. |
| R-11 | Session / JWT | PASS (LIVE API, 2026-11-04) | Live: password login, protected reads with the access token, global logout revoked the refresh token (refresh returned HTTP 400). Supabase access JWTs expire by design; the client refreshes. |
| R-12 | TFLite on-device ML | PASS (UNIT) + EMULATOR | SOURCE: `assets/models/ranker.tflite` is bundled and `trip_ranker.dart` runs a real interpreter; the ranking is inferred from features, not a hand-written sort. UNIT: model loading/score-change tests. EMULATOR: score changes for different inputs (device section). |
| R-13 | Cloud file upload | PASS (LIVE API, 2026-11-04) | Authenticated upload to the owner's folder in `post-media`, public read 200, own delete; RLS unchanged. |
| R-14 | Datepicker | PASS (UNIT) + EMULATOR | UNIT: picker bounds reject dates outside today..+20 (`test/home/home_search_screen_test.dart`). HOSTED: demo horizon refreshed today so the window is full: `refresh_demo_horizon(20)` → 648 slots, 1,994 trips, last departure 2026-12-04, 32 trips on the last day. EMULATOR: open picker, pick a future date, results load. |
| R-15 | GSAP / animation | PASS (EMULATOR) | `web-guide/guide.js` uses GSAP for entrance motion with a no-CDN fallback; Flutter screens use their own motion. EMULATOR 2026-11-18: the guide cards render and animate on the installed release build; the page states plainly that without the CDN it renders statically and nothing is faked. |
| R-16 | SASS | PASS | `web-guide/guide.scss` compiles to the committed `web-guide/styles.css`, which the page links; `test/guide_f15_test.dart` asserts the compiled file is linked and non-trivial. |
| R-17 | Git workflow | PASS | Both repos are single-branch `main` under owner identity `sa-mahi12`; every change in this pass is a direct owner commit + push (`0ddaac8`, `711717e`, `329ef88`, `fd8c5cf`, `d4eaacc`, `d8f51263`, `08c141d`, `93925bb`, `0d3b491`, `d05c41a`, `2a5ee13`, `1fb40b4`, `f20bed2`, `6e3ce42`, plus docs commits). No PRs, branches or worktrees. |
| R-18 | GraphQL | PASS (LIVE API) | Live 2026-11-14: `POST /graphql/v1 { stationsCollection(first:5) }` returned 5 station nodes with the anon key. |
| R-19 | REST / SOAP | PASS (LIVE API) | Live 2026-11-14: `GET /rest/v1/stations?select=code,name` returned 24 demo stations; the same request without a key returned 401, so RLS + key gating are real. |
| R-20 | Crystal Reports | EXEMPT | The teacher's own sheet exempts it; nothing is fabricated. |
| R-21 | Modern frontend | EMULATOR PASS (historical); PHYSICAL PENDING | Signed +25/+26 emulator evidence retained; +27 hash/signature/version checked, no connected device and no +27 install/runtime proof. Physical checklist has 26 unperformed checks. |
| R-22 | CI / containerization | PASS | GitHub Actions runs format, analyze, tests, debug APK and a signed release workflow on `main` only. Every commit in this pass is green: Flutter CI `43606864828`, `44352520137`, `44676098450`; release `43607854945`, `43612411501`, `43619639479`, `43623485003`, `43660496831`, `43663662668`, `43665603777`, `43667412762`, `43669859460`, `44352608469`, `44676107796`. The tree under test is the tree that ships: release and CI runs are dispatched from the same `main` SHA. |
| R-23 | Generative AI | CODE-COMPLETE / LIVE PROVIDER DEMONSTRATION PENDING | P41 12 audit tests at 8df1654: key removal, logout, short-key masking, errors, timeout, explicit-key gate, no logs/key literals, source-level booking independence. Existing HTTP tests are mocked; no real OpenRouter success. Owner procedure: app docs/owner/openrouter-demo.md. |
| R-24 | Additional TBD | NOT ANNOUNCED | No new item was announced; recorded as pending, nothing invented. |

## The teacher's later six-item announcement

P41 R-10 addendum: optional Google JS rendering code now exists but is
unverified and was not bundled correctly in +27 (map-provider.js absent).
Actual-bundle regression RED→GREEN proves the local declaration repair only;
corrected signed APK remains pending. 11 Node provider tests and 6 Flutter configuration tests do not
prove Google authorization or tiles. +27 has no Google key; an approved secure
HTTPS referrer origin, key/billing and live verification are prerequisites.
The original R-10 OSM deviation and +26 emulator proof above remain in force.
P41 R-22: CI `44871742168` and signed release `44871752519` succeeded at
`8df1654` (2026-11-21); local suite 630/630, format/analyze exit 0.

1. Embedded video (R-09) — fixed and device-proven above.
2. Mapping (R-10) — interactive OSM map; Google Maps is the recorded deviation.
3. Real-time rating (R-07) — live, cross-client.
4. SASS, 5. GSAP, 6. Flutter frontend — R-16, R-15, R-21 above.

## Releases cut in this pass

Every release is a signed `main` build published by the release workflow; the
x86_64 APK hashes below were recomputed locally from the downloaded asset and
matched against the release's own `SHA256SUMS.txt`.

| Tag | Release run | Commit | Verified locally |
|---|---|---|---|
| `v1.0.0+16` | `43607854945` | `329ef88` | manifest versionCode 16, signed |
| `v1.0.0+17` | `43612411501` | — | manifest signed, asset set complete |
| `v1.0.0+18` | `43619639479` | — | asset set complete |
| `v1.0.0+19` | `43623485003` | — | asset set complete |
| `v1.0.0+20` | `43660496831` | — | asset set complete |
| `v1.0.0+21` | `43663662668` | — | asset set complete |
| `v1.0.0+22` | `43665603777` | — | asset set complete |
| `v1.0.0+23` | `43667412762` | — | asset set complete |
| `v1.0.0+24` | `43669859460` | — | x86_64 `7127949454a6ae68b302ffa7562389648f413854f78d0ad448a45ea410ef1400`, device versionCode 4024 |
| `v1.0.0+25` | `44352608469` | `f20bed2` | x86_64 40,240,392 B, `60cf5ff8cd1cdc9e5c992861f143575ec74c287057012a0c6bc93a3e70cb11f1`, manifest versionCode 25 / device 4025, signed, 8 assets, bundled guide clip |
| `v1.0.0+26` | `44676107796` | `6e3ce42` | x86_64 40,240,680 B, `1f77e51b83395d273723bf6420a3464694ab6295d21bfb3f3729a0f5a685e7c5`, manifest versionCode 26 / device 4026, signed, 8 assets, map fix |
| `v1.0.0+27` | `44871752519` | `8df1654` | x86_64 40,307,452 B, `adae4fefe37332de08661db92f8a61548a9cf81a33239faa22acfcf72541c2a5`, published manifest build 27 / APK versionCode 4027 (aapt), v2 signature verifies, 8 assets; no install/runtime check |

## Defects found and fixed in this pass

1. Embedded video (R-09) - three separate failures, each proven on-device
   before the fix: YouTube "Error 153" from the `file:///android_asset`
   origin; Wikimedia answering the WebView with HTTP 403 + `text/html`
   (`net::ERR_BLOCKED_BY_ORB`); and the media element sitting in
   `NETWORK_NO_SOURCE` with no `error`. The shipped answer is a licensed clip
   bundled in the APK with its own HTML5 player.
2. Station map (R-10) - blank box in every build up to `+25`, caused by a
   double `renderMap()` clearing Leaflet's DOM; fixed in `6e3ce42` and
   device-proven on `+26`.


## Hosted changes made in this pass

- `post_ratings_realtime` migration `20261114142438` - publication membership
  only; applied via the Supabase API and verified in `pg_publication_tables`.
- `select public.refresh_demo_horizon(20)` - keeps the full 20-day demo window
  available; the shipped app offers departures to 2026-12-10, and bookings and
  occupied seats are unchanged (2 / 2).

## Commands used

```
dart format --set-exit-if-changed .
flutter analyze
flutter test
dart run tool/live_board_probe.dart   # RM_URL / RM_ANON / RM_SERVICE from env
```

## 2026-11-23 publication note

Nothing in this acceptance record changes status through publication. The
reviewed P41 repairs are now committed as `a3d2c30` and shipped in signed
`v1.0.0+28` (run 45213896700), with CI 45212454835 green and committed-HEAD
tests Flutter639/Deno33/Node11 plus clean format/analyze. Those are unit,
static and artifact results: they do not add hosted, two-device, provider or
physical-phone evidence, so no row above is re-graded. The urgent owner action
remains retiring the historical exposed service-role credential, followed by
Telegram hosted setup with real contact and instructor acceptance.
