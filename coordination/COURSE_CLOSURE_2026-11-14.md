# RailMate BD — full course closure checkpoint (2026-11-14 → 2026-11-20)

Written by the coordinator while executing
`RailMateBD_Full_Course_Closure_Autonomous_Agent_Handoff_2026-11-14.zip`.
This is the resume point: read the live governance first, then this file.

> Owner authorized controlled publication and signed +28 on 2026-11-21.
> Follow the P41 closure publication block for current gates; older statements
> requiring release authorization are historical. +27 stays unchanged.

> **Superseded resume point (P41, 2026-11-21):** read
> `P41_FINAL_CLOSURE_2026-11-21.md` and the latest V4_CURRENT block. Runtime
> source `8df1654` shipped as +27; CI/release green, 630 Flutter tests plus
> 21 mocked Telegram-update and 11 Node tests. Telegram is staged/not deployed,
> Google remains a deviation, live BYOK and physical-device work owner-side.
> +27 artifact/hash/signature/version verified, not installation/runtime.
> P40 facts below are historical and retain their original source/evidence.

> **P41 correction:** the +27 asset inspection and review subsequently found
> missing map-provider.js and Telegram account/lifecycle/delivery bugs. Local
> uncommitted fixes pass639 Flutter/Deno29+4 mocked/Node11; no corrected release,
> CI, hosted or device proof. Follow P41 current corrective handoff rather than
> treating the original code-complete snapshot as closure.

## Snapshot

- Packet opened 2026-11-14 (Asia/Dhaka); last device work 2026-11-20.
- App repo `sa-mahi12/RailMate-BD`, branch `main`, HEAD at packet start
  `437447f` (`v1.0.0+15`); final HEAD `6e3ce42` (`v1.0.0+26`).
- Closure commits in order: `0ddaac8` (ratings realtime + guide video),
  `711717e` (Flutter 3.47.5 pin), `329ef88` (+16), `fd8c5cf`, `d4eaacc`,
  `d8f51263`, `08c141d`, `93925bb`, `0d3b491`, `d05c41a`, `2a5ee13`,
  `1fb40b4`, `f20bed2` (bundled guide clip, +25), `6e3ce42` (map fix, +26).
- Docs repo `sa-mahi12/RailMate-BD-internal`, branch `main`.
- Both remotes PUBLIC, so every artifact here is redacted: no emails, user
  ids, tokens, keys or phone numbers.
- Dirty app paths deliberately left uncommitted: `.flutter-plugins-
  dependencies` (generated), `.serena/` (local agent state).

## Task table

| Packet | Scope | Status | Files |
|---|---|---|---|
| P0-1 | Working embedded video | DONE (bundled clip + tests + EMULATOR playback in `+25` and `+26`) | `web-guide/index.html`, `web-guide/guide.js`, `web-guide/media/*`, `pubspec.yaml`, `test/guide_f15_test.dart` |
| P0-2 | Real-time 1-5 star ratings | DONE (code + tests + hosted migration + live API) | `lib/features/board/ratings/*`, `lib/features/board/post/*`, `lib/app/home_shell.dart`, `supabase/migrations/20261114142438_post_ratings_realtime.sql`, `test/board/rating_realtime_test.dart` |
| P0-3 | Maps | DONE for Leaflet/OSM (blank-map defect found and fixed in `6e3ce42`, device-proven in `+26`); Google Maps stays a recorded DEVIATION | `web-guide/guide.js`, `test/guide_f15_test.dart` |
| P1 | All 24 requirements | Per-row evidence in `qa/COURSE_ACCEPTANCE_2026-11-14.md` | docs only |
| P2 | Releases + docs | `v1.0.0+16` … `v1.0.0+26` published; this file, matrix, ledger | this file, `governance/REQUIREMENTS_MATRIX.md`, `tasking/V4_TASK_LEDGER.json` |

No worker branches, PRs or worktrees were created; both repos have `main`
only and every change is a direct owner commit + push as `sa-mahi12`, with no
AI/human `Co-authored-by` trailers.

## Tests actually observed (final tree, `6e3ce42`)

- `dart format --set-exit-if-changed lib test` → `0 changed`.
- `flutter analyze` (3.47.5) → `No issues found!`
- `flutter test` (3.47.5, local, 2026-11-20) → `+583: All tests passed!`
  (baseline was 571; the +12 covers rating-realtime event/widget tests, the
  stale-load `RatingState` test, the bundled-video guide guards and the new
  map re-render regression test).
- CI `44676098450` (Flutter CI, `6e3ce42`) and release `44676107796` green.
- Earlier in the packet, CI run `43606166340` failed with 79 analyze *infos*
  from an upstream stable bump; fixed by pinning `flutter-version: '3.47.5'`
  (`711717e`) rather than weakening the analyze gate.

## Releases published in this packet

| Tag | Release run | Commit | Verified locally |
|---|---|---|---|
| `v1.0.0+16` | `43607854945` | `329ef88` | manifest versionCode 16, signed |
| `v1.0.0+17` | `43612411501` | — | signed, 8 assets |
| `v1.0.0+18` | `43619639479` | — | signed, 8 assets |
| `v1.0.0+19` | `43623485003` | — | signed, 8 assets |
| `v1.0.0+20` | `43660496831` | — | signed, 8 assets |
| `v1.0.0+21` | `43663662668` | — | signed, 8 assets |
| `v1.0.0+22` | `43665603777` | — | signed, 8 assets |
| `v1.0.0+23` | `43667412762` | — | signed, 8 assets |
| `v1.0.0+24` | `43669859460` | `1fb40b4` | x86_64 `7127949454a6ae68b302ffa7562389648f413854f78d0ad448a45ea410ef1400`, device versionCode 4024 |
| `v1.0.0+25` | `44352608469` | `f20bed2` | x86_64 40,240,392 B, `60cf5ff8cd1cdc9e5c992861f143575ec74c287057012a0c6bc93a3e70cb11f1`, manifest versionCode 25 / device 4025, signed, 8 assets |
| `v1.0.0+26` | `44676107796` | `6e3ce42` | x86_64 40,240,680 B, `1f77e51b83395d273723bf6420a3464694ab6295d21bfb3f3729a0f5a685e7c5`, manifest versionCode 26 / device 4026, signed, 8 assets |

Each verification downloaded the published x86_64 APK, recomputed SHA256 and
matched the release's own `SHA256SUMS.txt`, and read `release-manifest.json`
(`versionCode`, `commit`, `signed=true`, RailMate project URL).

## Video (R-09): three failures, proven, then solved

1. A YouTube iframe was the first fix and the video is genuinely embeddable
   (oEmbed 200, `playableInEmbed=true`), but the page runs from
   `file:///android_asset`, so the player gets no valid HTTP Referer and
   refuses with "Error 153". Proven on the emulator with `+16`.
2. The fallback streamed the same licensed clip from Wikimedia Commons. It
   played once, then failed: CDP on a debuggable build showed the WebView's
   own fetch answered **HTTP 403 + text/html** (rate limiting), which
   Chromium blocks as `net::ERR_BLOCKED_BY_ORB`; an identical instrumented run
   20 minutes earlier reached `readyState 4` and played. The failure was
   server-side, not code.
3. The shipped page therefore bundles the clip in the APK:
   `web-guide/media/coxsbazar-express-480p.webm` (4,039,910 B, unmodified 480p
   VP9 transcode, CC BY-SA 4.0, attribution in `web-guide/media/README.md`),
   plus its poster. `guide.js` recovers a `NETWORK_NO_SOURCE` element with
   `load()`, budgets two automatic retries, and makes every tap a real
   recovery attempt so a tap is never a silent dead end.

Device proof on the installed signed release (`+25`, then `+26`): real frames,
four consecutive screenshots differing, button "Pause video"/"Play video"
following the element state, and native controls reading `0:20 / 0:20` for the
20.374 s clip. Debug-build CDP corroborated the numbers (`networkState 1`,
`readyState 4`, `duration 20.374`).

## Maps (R-10): a real defect, found and fixed

Every build up to `+25` showed an **empty grey map box** with no tiles, no zoom
controls and no attribution. The Flutter screen injects
`window.RailMateGuide.showStation(code)` after the asset loads, so `renderMap()`
ran twice; the second call did `el.textContent = ''` while reusing the existing
Leaflet instance, deleting Leaflet's own panes. Reproduced deterministically in
Chromium against the same asset (7 panes / 6 tiles / 2 controls → 0 / 0 / 0, no
exception thrown). Fixed in `6e3ce42`: the container is cleared only when the
map is created, a torn-down container forces a rebuild, and `invalidateSize()`
runs twice for late WebView layout. Device-proven on `+26` for Dhaka and after
switching to Chattogram, with attribution visible.

Google Maps specifically is still a **DEVIATION**: no API key, no billing, and
no Google iframe was added untested.

## Device evidence (EMULATOR, signed release APK)

- `+26` (versionCode 4026, installed over `+25`): Dhaka map with OSM tiles,
  zoom controls, marker and "Dhaka (DAC) DEMONSTRATION ONLY" popup; CGP chip
  re-renders Chattogram tiles without blanking; the guide video plays to
  `0:20 / 0:20` with native controls.
- `+25` (versionCode 4025): guide video autoplays from the bundled asset, four
  consecutive screenshots differ, pause/play labels follow the element state.
- Debug build of `f20bed2` (remote debugging on): CDP state
  `currentSrc=file:///android_asset/.../media/coxsbazar-express-480p.webm`,
  `networkState 1`, `readyState 4`, `duration 20.374`, `currentTime` advancing.
- No physical-phone capture exists; every device claim in this packet is
  EMULATOR evidence.

## Hosted backend changes (applied, not just staged)

- `post_ratings_realtime` (migration `20261114142438`): `public.post_ratings`
  added to the `supabase_realtime` publication idempotently. Verified after
  apply: `pg_publication_tables` lists `posts`, `post_comments`,
  `post_reactions`, `post_ratings`; RLS policies `ratings_read`,
  `ratings_insert_own`, `ratings_update_own`, `ratings_delete_own` unchanged.
- `select public.refresh_demo_horizon(20)` → `648` slots; the shipped app now
  offers a horizon out to 2026-12-10. Bookings and occupied seats unchanged.
- Live realtime proof (two synthetic signed-in clients): comments
  `insert,delete`, reactions `insert,update,delete`, ratings
  `insert,update,delete`, all observed by the second client without refresh.
- Hosted totals after cleanup: 2 users, 2 profiles, 2 posts, 2 comments,
  2 reactions, 0 ratings; public tables 12; stations 24. The synthetic device
  account used for the final captures and its one comment, one reaction and
  one rating were deleted after the last screenshot.

## Owner blockers (asked once, consolidated)

1. SMS OTP: needs an approved provider, one consented Bangladeshi recipient and
   a spend cap (or a written teacher waiver). Email OTP (Mailjet) is live.
2. Google Maps: confirm whether a generic interactive map is accepted; Google
   Maps specifically needs an API key and billing approval.
3. Repository visibility and privileged key rotation are owner-only actions and
   were not performed in this packet.
4. Generative AI (R-23): a real OpenRouter rewrite needs the owner's BYOK key;
   the app's key entry, secure storage and "sent only on explicit action"
   behaviour are implemented and unit-tested.
5. Physical-phone captures: everything here is emulator evidence.

## Next safe command

Historical P40 recommendation below has already been executed by P41; **do not
dispatch another +27 run**. `v1.0.0+27` is preserved and `v1.0.0+28` was
published once from `a3d2c30` on 2026-11-23 (run 45213896700). The current next
action is the consolidated owner checklist in the P41 handoff, starting with
exposed-credential retirement.

## 2026-11-23 publication result

Source `a3d2c305dc0a96bd952abffd8eaec3349be87f5b` (18 reviewed paths), CI
45212454835 green, committed-HEAD Flutter639/Deno33/Node11 with clean
format/analyze. Signed `v1.0.0+28` published with eight verified assets, v2
signatures and the historical certificate; all APKs/AAB carry
`map-provider.js`. The signed APK installs and launches on an Android 15
emulator to the login gate, but the Station Guide requires authentication, so
map rendering on `+28` remains unobserved. Physical-phone acceptance, hosted
Telegram proof, Google, live BYOK and credential retirement remain owner work.
