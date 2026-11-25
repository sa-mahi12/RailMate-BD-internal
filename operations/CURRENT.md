# CURRENT — live status

## Latest — P43 official timetable + community completion, started 2026-11-25

IN PROGRESS; PRODUCTION DATABASE FROZEN. The revised P43 handoff asks for a
coherent UI, a source-backed official timetable, a completed Journey Board
(post edit/delete, comment replies/edit/delete/report, blocks, report receipts)
and a real staff moderation console, with Norfold used only as reference and no
hosted database change until the owner approves the gate.

Baseline: app `f058afc`, docs `3b3812b`; release `v1.0.0+29` preserved.

Done and pushed on `main` (owner identity, direct commits):
- `bf3f347` official timetable mode: both Bangladesh Railway PDFs hashed, 130
  intercity rows transcribed with page+serial provenance, 4 ambiguous printed
  rows excluded, coverage gaps recorded, Dart models/repository/query/list/
  detail/station screens, home entry card, 21 new Flutter tests.
- `0e8c495` public `timetable.html` with a pure filter module (10 new Node
  tests) reading `site/data/official-timetable.json`.
- `bd00b49` `docs/P43_PLAN.md` + deployed-page screenshot.

Data honesty: the Eastern PDF is a scan and the Western text layer extracts as
legacy-font mojibake, so rows were read from the rendered page images. Only
origin/destination, published times, weekly off day and provenance are stored;
intermediate stops, fare, platform and frequency are never inferred. The
mail/express and commuter tables (Eastern pages 3–8, Western pages 2–15) are
explicitly not imported yet and the manifest/UI say so.

Still open in this phase: post edit/delete + media cleanup, comment threading,
moderation console with roles/audit/blocks/receipts, draft migrations (not
applied), UI polish with screenshots, full CI, release candidate, then the owner
database gate. No new Android release and no hosted DDL/DML happened in P43.

## P42 — social web publication, 2026-11-24/25

PUBLIC WEB P42 PUBLISHED; HOSTED SCHEMA APPLIED; SIGNED +29 PUBLISHED AND
VERIFIED. The owner asked for a genuinely working academic social prototype: a
live public site backed by Supabase, real cross-account posts with permanent
links, multi-format attachments in Storage, public author identity, preserved
comments/likes/dislikes/ratings and reporting, verified with two independent
accounts.

Published on `main` (owner identity `sa-mahi12`, direct commits, no branch or
PR): `c8565cd` the P42 feature (55 files), then `96754ab` avatar initials,
`02273bb` no feed rebuild during video playback, `ad64f65` deploy-time asset
cache stamping, `84dd332` deployed-page evidence docs, `140d14c` `1 post`
inflection, `c556e5d` public-profile screenshot, `057909d` release evidence.
`.serena/` left untracked.

Hosted project `psuzlyingfmstnyfvlnj` received migration
`20261124000001_p42_social_web.sql` through the Management API on 2026-11-24
(HTTP 201, recorded in `supabase_migrations.schema_migrations`): typed
`post_attachments` with CHECK constraints (kind, https-only links, owner-folder
paths, 25 MiB, ten rows per post, owner must own the post), the
`public_profile_cards` and `public_post_stats` views, `post_reports` /
`user_reports` (one per reporter, no self-report, reporter-only read), board
rate-limit triggers, `post_attachments` added to the realtime publication, and
an explicit size/MIME allowlist on `post-media`.

Gates at the published tree: `flutter analyze` clean, `dart format` 229/0,
**675 Flutter tests** pass (639 pre-P42 + 36 new), 10 site `node --test` pass,
`npm run build:css` clean. Flutter CI success on the pushed SHAs (e.g.
`45451672940` at c8565cd, `45451935841` at 96754ab). Two CI/deploy failures were
real and fixed, not re-run: the site unit test caught `initialsFor('P42 Amina
(demo)')` returning `PD`, and the workflow token could not create the Pages
site ("Resource not accessible by integration") so the owner identity enabled
it with `gh api -X POST repos/…/pages`.

Live site: https://sa-mahi12.github.io/RailMate-BD/ (deploy-pages runs
`45452161331`, `45452629320`, `45453214538`, `45454328891`, success). Verified in
real Chrome, not by test alone: the feed shows three real posts with images,
an HTML5 video player, a PDF card, a click-to-load YouTube button and a link
card; `post.html?id=…` shows the post, `Comments (1)` by the second account and
`1 like / 5.0 ★ (1) / 1 comment`; `profile.html?id=…` shows
`P42 Amina (demo) · @p42_amina_7s16e9 · Joined Nov 24 · 1 post`; the uploaded
WebM was measured playing (`paused=false`, 848x480) and still playing 37.7 s
later across a refresh boundary. Screenshots and measurements are in
`docs/qa/p42/`.

Cross-account evidence (real REST/Storage, two throw-away demo accounts, never
the owner's two accounts) run `mwv0r1ce33dd`, 22 checks: A publishes a post with
image + video + PDF + YouTube link + plain link; an anonymous reader and B see
all five; B comments/likes/rates; public stats show it; B's cross-account delete
removes nothing; B's report is stored and hidden from A; a non-HTTPS link, a
foreign owned attachment, a foreign storage path and a self-report are rejected;
a repeat report updates in place; a client-supplied `created_at` is replaced by
the server clock. `docs/qa/p42/cross-account-evidence.json`.

An independent read-only review of the live schema and client code found **no
Critical** issue and one Important one: `storage_path` only had to *look* like
`<uuid>/…`, so a user could point their own attachment row at another user's
object. Fixed in `20261125000001_p42_hardening.sql` (prefix must equal
`owner_id`), which also applies the ten-attachment cap on UPDATE, stamps
`posts`/`post_comments.created_at` from the server clock, adds own-row report
UPDATE policies and blocks self-reporting a post.
`20261125000002_p42_report_upsert.sql` resolves a repeat report inside the
database, because the shipped `+29` client upserts without naming the conflict
target (PostgREST answered 409). Both migrations are applied to the hosted
project and recorded in `supabase_migrations.schema_migrations`; the 22-check run
passes after them.

Accepted follow-ups that need a Dart change (therefore the next app release, not
this packet): the link parser accepts `http://` (ids are still uuid-validated, no
open redirect), `attachments_read` is `using (true)` and must be revisited if
post moderation is ever added, and a pre-existing recovery-link double-handling
path in the auth gate predates P42. No Android device run of the composer,
attachment renderers or the deep links was performed — those are unit-tested
only.

Signed `v1.0.0+29` published by release run `45453959869` from `84dd332` with
eight assets; the universal APK SHA256 `e2d67d17…e608eac6` matches the GitHub
asset digest and `SHA256SUMS.txt`, `aapt2 dump badging` reports `versionCode 29`,
`versionName 1.0.0`, `bd.railmate.railmate_bd`, `apksigner verify
--min-sdk-version 24` exits 0 with the same release certificate as `+28`
(`37c67c4c…`), and the extracted `libapp.so` contains the P42 symbols
`post_attachments`, `public_profile_cards` and `post_reports`. `v1.0.0+28` and
its eight assets are unchanged.

## P41 — publication, 2026-11-23 (previous)

PUBLICATION EXECUTED (source); DOCS AND ARTIFACT GATES IN PROGRESS. The owner
authorized controlled publication on 2026-11-21; execution happened 2026-11-23.
Exactly the 18 reviewed app paths were staged and committed as
`a3d2c305dc0a96bd952abffd8eaec3349be87f5b` on `main` by the owner identity
`sa-mahi12`, then pushed; generated `.flutter-plugins-dependencies` and
`.serena/` were left unstaged. Source CI run `45212454835` succeeded on that
SHA. Committed-HEAD local reruns, all exit0: Flutter 639 tests, Deno 33
(29 mocked updates + 4 actual-handler), Node 11, `dart format` 214 files/0
changed, `deno fmt` 4 files, `flutter analyze` no issues. Final-tree Gitleaks
8.30.1 rescans after the last privacy redactions found 0 leaks in both trees.

Signed `v1.0.0+28` (run `45213896700`, success) published from `a3d2c30` with
eight assets whose sizes and SHA256 values match the GitHub API digests and the
published checksums; every APK verifies with the historical v2 signing
certificate, `versionCode` is 4028 and all APKs/AAB bundle `map-provider.js`
byte-identical to the committed blob. `v1.0.0+27` kept its release id and asset
digests. On an Android 15 x86_64 AVD the signed APK installs, launches and
reaches the login gate; the Station Guide needs an authenticated session, so
`+28` map rendering is NOT observed and no physical-phone claim is made. The
nine documentation paths are committed in this pass. No hosted
migration, deployment, credential rotation, provider call, visibility change or
device action was performed. Owner gates (Telegram deployment/teacher
acceptance, Google secure origin, live BYOK, physical-phone smoke test, urgent
legacy-credential retirement) remain open.

## P41 preparation — 2026-11-21 (superseded by the 2026-11-23 entry)

PUBLICATION AUTHORIZED / PREPARING: owner approved controlled source/docs
publication and signed +28. All 18 app and nine documentation original changes
reviewed; publication copies redact private account/machine/session details.
Current-tree Gitleaks0 in both; app history has two JWT findings, including
service-role; internal history Gitleaks0 does not prove no personal data.
No new commit, CI, release or runtime result is yet claimed. Source version
targets 1.0.0+28; the local-corrective snapshot below is historical preparation.

LOCAL CORRECTIVE PATCH, NOT CLOSED: +27 is the defective original; missing map
provider asset and reviewed Telegram account/lifecycle/retry defects repaired
against8df1654 in uncommitted files. Full639 Flutter/Deno29+4 mocked/Node11,
format214/0/analyzer clean exit0. Final reviewer safe-as-LOCAL-PATCH (no
Critical/Important), Minor restore-test fixture corrected; local post-pass
validation passed. Publication is authorized, but no corrected CI/build/release
or hosted/device/provider proof. Owner
gates remain below. The following630/21 snapshot is historical pre-fix evidence.

Code and documentation use the existing adjacent checkouts; machine paths are withheld.
Runtime source 8df1654 published as signed v1.0.0+27; CI 44871742168 and release
44871752519 succeeded. Fresh 630 Flutter / 21 mocked-update / 11 Node tests
passed, format/analyze exit 0. Downloaded APK hash/signature/version verified;
no connected device, +27 install/runtime not verified. Telegram migration and
functions staged/not deployed; R-05 alternative acceptance pending, R-10
Google deviation, R-23 live BYOK and physical-phone pending. Urgent owner task:
verify/revoke historical exposed service-role credential using the corrected
runbook. No privileged hosted action/rotation/visibility change was performed.
Authority for current detail: coordination/P41_FINAL_CLOSURE_2026-11-21.md,
coordination/V4_CURRENT.md and governance/REQUIREMENTS_MATRIX.md.

## Historical preparation snapshot (superseded)

Date: 2026-09-25 (package preparation only)
State: PREPARED / NOT EXECUTED
Code repo URL: UNKNOWN until verified by `gh repo view`.
Docs repo URL: UNKNOWN until verified by `gh repo view`.
Supabase project ref: NOT CREATED/NOT VERIFIED.
OpenCode version, model roster and AgentRouter provider: NOT TESTED on owner's machine.
GitHub Actions: NOT RUN.
Flutter app: NOT CREATED.
APK/device: NOT TESTED.
Live OpenRouter call: NOT TESTED.
Phone SMS verification: BLOCKED until SMS provider and budget approved.
Next action: read setup/SETUP_SEQUENCE.md, run read-only preflight, confirm owner GitHub identity, create two private repos, record outputs.
