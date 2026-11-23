# P41 — final closure and owner handoff (2026-11-21)

## 1. Executive summary

**PUBLICATION AUTHORIZED / PREPARING (2026-11-21).** Owner explicitly approved
controlled publication and a new signed +28, preserving +27. Original 18 app
and nine documentation changes were reviewed in full. Source version targets
1.0.0+28; old source was +1, while the workflow overrode it to +27. All historical
authorization-pending statements below are superseded. New commits,
committed-HEAD tests, CI/release, artifact and runtime gates are still pending.
Public publication copies omit local paths, private account details and session
IDs; original local evidence is preserved. No hosted/provider/rotation/visibility
action is authorized or claimed. The following is the historical local snapshot.

**LOCAL CORRECTIVE PATCH; COURSE CLOSURE STILL PENDING.** Original runtime
source `8df16542093f4a6cabb7efa86497cd2eced551e1` is published as signed
`v1.0.0+27`, but review established Telegram account/lifecycle/delivery defects
and the APK omits `map-provider.js`. Repairs are uncommitted and unreleased.
The repaired tree passed 639 Flutter tests, 29 mocked-update + 4 mocked-handler
Deno tests and 11 Node tests; format214/0 and analyzer clean. Telegram is not
deployed/live-verified; Google remains an unverified opt-in/R-10 deviation,
OSM delivered. BYOK live demonstration, physical-device testing and urgent
exposed-credential retirement remain owner-side. No repaired-tree CI/build,
new signed release or overall course PASS is claimed.

## 2. Packet scope, governance and checklist

Continuation uses the preceding owner P41 request and already-pushed commit,
not a new feature packet. The documentation checkout is
the existing adjacent internal checkout (machine paths withheld in this public copy).
Mandatory START_HERE, product contract, matrix and operations docs were read.
App start SHA `8df1654`; docs start SHA `230c774`. Both repos have only `main`.
Coordinator identity observed as `sa-mahi12`,
`212235795+sa-mahi12@users.noreply.github.com`; no identity change.
Generated `.flutter-plugins-dependencies` and `.serena/` are untouched.

Private model/session and machine diagnostics are withheld from this public
publication copy; the review verdicts and dated verification results remain.

- [x] Resume actual state without reimplementing committed P41 code.
- [x] Verify CI/release result and published artifacts.
- [x] Repaired-tree full run: +639/exit0; format214/0, analyze clean; Deno29+4/0, Node11/0 (2026-11-21). Pre-fix gates below remain historical.
- [x] Reconcile README, matrix, acceptance, current/closure and ledger with corrective results.
- [x] Correct owner instructions for Google JS restrictions and Supabase keys.
- [x] Initial independent read-only review: NOT SAFE TO HAND OFF; four Important Telegram defects and incorrect masked-storage disclosure.
- [x] Packaging RED then GREEN: real generated bundle could not load map-provider.js; asset declaration repaired; focused test +1/exit 0 (2026-11-21).
- [x] Account-switch isolation and stale async/poll lifecycle: 8 reproduced RED failures; focused23/exit0 after repair.
- [x] Transient webhook/redelivery: 5 RED cases + completion-ack RED + actual-handler HTTP200-vs503 RED, then passing; safe lease/retry/consume recovery.
- [x] Digits-only contact: sender-owned and typed-number cases RED, then GREEN.
- [x] UI/bot privacy disclosure: full number protected, display masked; existing visual system unchanged, no unsupported at-rest masking promise.
- [x] Final bounded read-only verdict SAFE AS LOCAL PATCH; no Critical/Important; minor restore-failure fixture corrected. Exact paths/branches/secret scan/link/matrix/ledger/diff gates pass locally.
- [x] Owner authorized controlled publication and signed +28; security/review/test gates still apply, and +27 must remain unchanged.
- [ ] Resulting committed HEADs, committed-HEAD checks, corrected CI/release and artifact/runtime verification.

Continuation allowed paths: app `README.md`, `docs/owner/{maps,telegram}-setup.md`,
`docs/security/{security-audit-2026-11-20,credential-rotation-runbook}.md`;
internal `coordination/{V4_CURRENT,COURSE_CLOSURE_2026-11-14,P41_FINAL_CLOSURE_2026-11-21}.md`,
`governance/REQUIREMENTS_MATRIX.md`, `qa/COURSE_ACCEPTANCE_2026-11-14.md`,
`tasking/V4_TASK_LEDGER.json`, `operations/{CURRENT,TASK_BOARD,DECISIONS}.md`.
Dependencies: committed P41 implementation, completed P40 evidence and hosted
release. No concurrent editor owns these files; initial read-only reviewer finished.

Corrective scope (same P41 functionality, base still 8df1654): app
`pubspec.yaml`, `test/guide_asset_bundle_test.dart`,
`lib/app/dependencies.dart`, `lib/features/auth/telegram/{telegram_verification_state,telegram_verify_section}.dart`,
`test/{telegram_verification_state_test,telegram_account_isolation_test}.dart`,
`test/support/telegram_fakes.dart`, `supabase/functions/_shared/telegram{,_test}.ts`,
`supabase/functions/telegram-webhook/{index,index_test}.ts`, and staged migration
`supabase/migrations/20261120000001_telegram_phone_verification.sql`.
Owner subsequently authorized source version +28, controlled publication and
one new signed +28 release. Hosted changes, credential rotation, bot setup,
Google activation and live OpenRouter use still require separate authorization.

## 3. Telegram verification

Paths: `supabase/functions/_shared/telegram{,_test}.ts`,
`telegram-challenge/index.ts`, `telegram-webhook/index.ts`,
`supabase/migrations/20261120000001_telegram_phone_verification.sql`,
`lib/features/auth/telegram/`, profile/app composition, corresponding tests.
Challenge: 32 random bytes, SHA-256 hash storage, five-minute expiry, one active
challenge, rate limit, link carries no user id/phone. Webhook: secret header,
private chat, sender-owned contact, identity binding, update-id deduplication;
RLS read-own/service-role writes. Profile restores a prior verified row and
shows a masked number. Method is `telegram_contact`, not SMS; no Supabase
`phone_confirmed_at` update. Full number is stored in a protected backend
record, **not only masked at rest**.

The original +27 had 29 Flutter and 21 mocked-update tests but omitted the
reviewed lifecycle/retry cases. Corrective focused lifecycle/account tests:
23 pass; full Flutter suite639. Corrective backend: 29 mocked updates and
4 actual Edge-handler tests with mocked HTTP/storage (33 pass). These are
UNIT evidence, not hosted/live/device proof. State now binds to auth identity
independently of HomeShell, resets hydration on logout/switch, invalidates
stale futures by generation/challenge, prevents overlapping polls and ignores
results after disposal. Backend leases distinguish processing/completed;
failed claims release or expire after two minutes, transient/busy HTTP503
allows redelivery, exact verification_update_id resumes an ambiguous consume
without re-verifying. A successful verification notification is best effort;
the protected row remains authoritative. Same-sender start resumes a bound
prompt after a delivery failure. International digits-only own cards become
E.164; typed numbers never count as proof. Full number is protected/display
masked in both UI and bot disclosure.

Migration apply, function deployments, bot secrets, webhook registration and
real contact proof were not performed. Owner guide:
`RailMateBD/docs/owner/telegram-setup.md`.

## 4. Maps resolution

`web-guide/map-provider.js` and `map_provider_config.dart` select Google only
with an owner-supplied build key; +27 supplies none. Tests: 11 Node provider
tests and 6 Flutter configuration tests. Google renderer/authorization is not
live-verified. OSM rendering proof is historical signed +26 EMULATOR evidence.
Actual +27 APK inspection found the referenced `map-provider.js` absent:
explicit pubspec assets omitted it. An actual generated-Flutter-bundle test
failed to load the module (exit1); the one-line asset declaration repair made
that test pass (+1/exit0). That does not rebuild or repair the published +27.
JavaScript API keys require Website restrictions, not Android package/SHA-1.
The current `file:///android_asset` origin has no reliable HTTP referrer; a
secure approved origin (or separately scoped native Maps SDK work), key,
billing and live test are prerequisites. Do not weaken key restrictions.

## 5. R-23 BYOK audit

12 audit tests cover key removal/logout, full masking of short keys, request
errors, finite timeout, explicit-key gate, no logging/key literals and
source-level booking independence. Existing HTTP tests are mocked. Consent is
per request, secure storage is account-scoped, suggestions need explicit
acceptance. Real OpenRouter completion is **not demonstrated**; the owner must
enter a private key in-app, never in chat/source/docs. Guide:
`RailMateBD/docs/owner/openrouter-demo.md`.

## 6. Physical-device checklist

`RailMateBD/docs/qa/physical-device-checklist.md` contains 26 checks with actual
result, screenshot and status fields. All are unperformed. `adb devices -l`
returned no devices in this continuation (exit 0); no emulator/remote device
was launched and +27 installation/runtime was not verified. Prior emulator
observations do not establish a physical-phone or TWO DEVICE pass.

## 7. Security findings and rotation

Publication scan: Gitleaks8.30.1 current publishable-tree scans with archive
depth3 exited0 in both repos. Reachable-history scan app exit1: two JWT findings
(anon/service-role), internal exit0. Supplemental metadata-only scans covered
330 app files/665 blobs and216 docs files/357 blobs; credential assignments in
A02 are FakeAuthClient examples, phone strings in A03 are test placeholders.
App provider-token hits are synthetic in-memory BYOK audit fixtures. Current
email/password-like test values are mocked or generated ephemeral probe data;
GitHub no-reply identity is public provenance. Personal owner account details,
machine paths, model diagnostics and session IDs are withheld in the nine
publication documents. Existing public docs elsewhere still contain personal/
operational metadata and history retains it; broader cleanup is not performed.
Gitleaks handled supported archives; supplemental regex skips binary contents,
which are inventoried separately. Scanning is not proof of universal absence,
and the historical privileged credential was not tested or revoked.

P41 audit found both repos PUBLIC and a historical service-role JWT in
`app.env.json` history (October 2026); no value is reproduced. Current HEAD
does not track the key. Whether the historical credential has already been
revoked is unknown; owner verification/retirement is urgent. New keys alone
do not revoke legacy keys. Custom `SUPABASE_` secrets are reserved; adapters
need a reviewed migration to platform publishable/secret dictionaries before
legacy-key deactivation and legacy JWT-secret revocation. This compatibility
work and all hosted changes remain owner-authorized follow-up, not P41 edits.
Official Google/Supabase instructions were read on 2026-11-21 and runbook
corrected. No credential rotation, history rewrite, local key deletion,
visibility change or signing-secret change was performed.

## 8. Tests and commands actually observed

Historical pre-fix commands below are dated 2026-11-21 at original runtime
source `8df1654`; they are not repaired-tree verification:

| Command | Actual output/result | Exit | Evidence class |
|---|---|---:|---|
| `git status --short --branch`, `git rev-parse HEAD`, `git branch --format` in both repos | app main 8df1654; docs main 230c774; only generated/local app paths dirty initially | 0 | STATIC |
| `dart format --output=none --set-exit-if-changed lib test` | 212 files, 0 changed | 0 | STATIC |
| `flutter analyze --no-pub` | No issues found | 0 | STATIC |
| `flutter test --no-pub --reporter expanded` | `+630: All tests passed!` | 0 | UNIT |
| `node --test web-guide/map-provider.test.cjs` | 11 pass / 0 fail | 0 | UNIT |
| `npx --yes deno@2 test supabase/functions/_shared/telegram_test.ts` | 21 pass / 0 fail | 0 | UNIT (mocked updates) |
| `gh run view 44871752519`, CI run listing | release and CI 44871742168 success, same source SHA | 0 | HOSTED CI |
| `gh release download v1.0.0+27` (manifest/checksums/provenance/x86_64 APK) | files downloaded | 0 | STATIC artifact |
| `Get-FileHash ...x86_64.apk -Algorithm SHA256` | matches published SHA256SUMS and release digest | 0 | STATIC artifact |
| `aapt dump badging ...x86_64.apk` | bd.railmate.railmate_bd / 1.0.0 / 4027, min SDK 24, target 36 | 0 | STATIC artifact |
| `apksigner verify --verbose --print-certs ...x86_64.apk` | Verifies, v2 true, one RSA-4096 signer | 0 | STATIC signature |
| `adb devices -l` | no connected devices | 0 | NOT runtime proof |

Full historical Flutter stdout is preserved locally as
`p41-flutter-test-final.log`; machine paths are withheld.
Downloaded artifacts are in adjacent temp folder `p41-release-27`.
No heavy local Android build ran; private machine diagnostics are withheld.

Corrective commands, 2026-11-21, **uncommitted diff against 8df1654**:

| Command | Actual output/result | Exit | Class |
|---|---|---:|---|
| `flutter test --no-pub test/guide_asset_bundle_test.dart --reporter expanded` | RED missing map-provider.js; GREEN +1 after pubspec declaration | 1 then 0 | UNIT actual generated bundle |
| `flutter test --no-pub test/telegram_verification_state_test.dart test/telegram_account_isolation_test.dart --reporter expanded` | RED 8 named lifecycle/account failures; GREEN23 | 1 then 0 | UNIT deferred futures + real auth/dependency composition |
| `npx --yes deno@2 test supabase/functions/_shared/telegram_test.ts` | RED5 delivery cases; separately RED completion-ack and 2 digits-only cases, then GREEN29 | 1 then 0 | UNIT mocked updates |
| `npx --yes deno@2 test supabase/functions/telegram-webhook/index_test.ts` | RED expected503 got200; GREEN4 including completed/busy/expired ownership filters | 1 then 0 | UNIT actual handler, HTTP/storage mocked |
| `flutter test --no-pub --reporter expanded` | +639 All tests passed | 0 | UNIT full suite |
| `dart format --output=none --set-exit-if-changed lib test` | 214 files, 0 changed | 0 | STATIC |
| `flutter analyze --no-pub` | First run: curly_braces info/exit1; corrected, fresh run No issues found | 1 then 0 | STATIC |
| `npx --yes deno@2 fmt` (four changed TS paths) | Checked4 files | 0 | STATIC |
| `node --test web-guide/map-provider.test.cjs` | 11 pass/0 fail | 0 | UNIT |

Corrective full-suite stdout:
`p41-flutter-test-corrective.log` (preserved locally; machine path withheld).
Initial test-authoring compile error (cascade arrow-body precedence) was
corrected before the eight genuine lifecycle REDs; it is not regression proof.
Second reviewer dispatch followed the local resource gate.

Post-pass validation (2026-11-21): Python checked exact changed-path scope
(18 app paths, 9 internal paths), both branch lists `main` only, bounded
secret-like-value scan0 and README local links; exit0. Ledger JSON parses,
task IDs unique, matrix24 rows/R20 EXEMPT/R24 NOT ANNOUNCED, report12 sections;
exit0. Both `git diff --check` results exit0. Generated/local state excluded
and left unstaged. These checks do not prove absence of historical credentials.

Exact app corrective paths for coordinator review/staging:

```text
README.md
docs/owner/maps-setup.md
docs/owner/telegram-setup.md
docs/security/credential-rotation-runbook.md
docs/security/security-audit-2026-11-20.md
lib/app/dependencies.dart
lib/features/auth/telegram/telegram_verification_state.dart
lib/features/auth/telegram/telegram_verify_section.dart
pubspec.yaml
supabase/functions/_shared/telegram.ts
supabase/functions/_shared/telegram_test.ts
supabase/functions/telegram-webhook/index.ts
supabase/functions/telegram-webhook/index_test.ts
supabase/migrations/20261120000001_telegram_phone_verification.sql
test/guide_asset_bundle_test.dart
test/support/telegram_fakes.dart
test/telegram_account_isolation_test.dart
test/telegram_verification_state_test.dart
```

App patch snapshot SHA256 (tracked binary diff followed by sorted new-path
name/NUL/content) at the scan:
`16ef9abef53ef3f1aa02097e7ae4e3edc5c4ae1c31a37fa43ec38d66a6d7b70e`.
Internal snapshot before this evidence addition:
`058c148b97aaf376214a0420167d4e8eb66019f12af5a723eb86af51f418b745`;
it is not a hash of this final self-updated record.
Internal changed paths: this record, `coordination/{COURSE_CLOSURE_2026-11-14,V4_CURRENT}.md`,
`governance/REQUIREMENTS_MATRIX.md`, `qa/COURSE_ACCEPTANCE_2026-11-14.md`,
`operations/{CURRENT,TASK_BOARD,DECISIONS}.md`, `tasking/V4_TASK_LEDGER.json`.

## 9. Release integrity

- Tag: `v1.0.0+27`, published `2026-11-21T05:44:15Z`.
- Source: `8df16542093f4a6cabb7efa86497cd2eced551e1`.
- Release run: https://github.com/sa-mahi12/RailMate-BD/actions/runs/44871752519
- Flutter CI: https://github.com/sa-mahi12/RailMate-BD/actions/runs/44871742168
- Eight assets: four APKs, AAB, manifest, checksums, provenance.
- Published manifest is key/value text despite its `.json` filename: build 27,
  signed=true. APK independently reports split-ABI Android versionCode 4027.
- Downloaded x86_64 APK: **40,307,452 bytes**, SHA256
  `adae4fefe37332de08661db92f8a61548a9cf81a33239faa22acfcf72541c2a5`.
- Signing certificate SHA256:
  `37c67c4c119d3adea7dcbeaae99ae69d8ab14e231ca2fecee9b6134190f2f155`.
- Signature/hash prove integrity of the original artifact, not functional
  correctness. The +27 APK lacks map-provider.js and contains the reviewed
  Telegram bugs. Local source repairs do not change that binary.
- No install/launch claim, corrected release/CI/build or new build number.
  Coordinator must review exact source paths and obtain the publication
  decision; a corrected signed release requires a new number (e.g. +28), never
  overwrite +27. Then verify provider/video/model assets, signature/hash/version
  and perform real-phone smoke tests before claiming runtime closure.

## 10. Requirement/document reconciliation

R-04 is code/schema-supported, not a demonstrated concurrent registration
race; acceptance table's earlier PASS was narrowed. R-07 is historical LIVE
API + EMULATOR UI verified, not merely code-complete. R-05 stays PARTIAL with
Telegram alternative/teacher acceptance pending. R-10 stays DEVIATION. R-21
physical-phone and +27 runtime pending; R-23 live provider pending. R-20
EXEMPT and R-24 NOT ANNOUNCED unchanged. README no longer carries obsolete
558-test/no-emulator language; P38/P40 historical results are retained.

## 11. Review, rulings and publication gate

Ruling: publish only privacy-reviewed copies of the nine assigned docs —
owner's no-sensitive-publication constraint supersedes raw operational handoffs.
Original evidence is retained locally; no history rewrite, broad cleanup or
visibility change. Cost: older public copies remain an owner privacy risk.

Owner publication authorization is recorded and does not authorize hosted
changes. The original corrective pass and its no-publication record below are
historical. Controlled publication has not yet reached its commit/release gates.

Publication review: independent read-only reviewer inspected all18 app/nine
docs current files but could not execute exact Git diffs. It established an
Important privacy finding in historical V4_CURRENT passenger-name/typed-handle
text; this was reproduced by a privacy assertion (exit1) and corrected with
redaction, including actual booking IDs and password-related operational hints.
The expanded privacy assertion now gates all nine documents. Its Minor scope
list discrepancy was regraded Important for exact-path staging integrity and
corrected: the unchanged Telegram widget test is not a changed path. Coordinator
read the complete original exact diffs and new files; that is coordinator
evidence, not independent diff re-execution. No new runtime feature was added.

Ruling: work stays inline on existing `main`; no worktree/branch — repository
governance overrides generic execution skill isolation. No extra isolation is
available if a conflicting editor appears; stop on overlap.

Ruling: no +27 runtime/device claim — no connected device; prior +26 proof
cannot be transferred to the new binary. Cost: a remaining owner smoke test.

Ruling: correct owner setup docs without expanding runtime features — official
provider constraints invalidate the earlier instructions. Cost: Google needs
secure-origin work and credential retirement needs reviewed key compatibility
work before hosted execution. Neither is falsely marked complete.

Initial read-only review (session ID withheld): NOT SAFE TO HAND OFF;
four Important findings (account isolation, stale futures, suppressed delivery
retry, digits-only contact) and privacy-disclosure issue. Verified/replicated
before repair, not blindly accepted. The independent APK packaging finding is
also repaired locally. No initial Critical defect was established; exposed
credential validity was not tested. A fresh bounded corrective reviewer
returned **SAFE TO HAND OFF AS LOCAL PATCH**;
no Critical/Important defects established. Not approval of closure/deployment/
release readiness. It independently read saved corrective stdout639, inspected
named corrective content and tests, but could not execute git-diff commands;
the exact-diff inventory and command exits are coordinator evidence, not review
re-execution. One Minor finding: the original restore-failure test set a fake
field that fetchLatestVerified ignored. The fixture now explicitly throws via
restoreResponse and checks an honest unverified state plus successful retry;
no production change for that finding. Fresh full-suite rerun after the fixture
correction: `+639: All tests passed!`, exit0, saved at
`p41-flutter-test-corrective-reviewed.log` (local preservation; path withheld).
Fresh format214/0, analyzer clean, Deno format4/0, Deno33 and Node11 all exit0.

Final post-pass command after the corrected fixture/docs: Python+git inventory,
main-only/staged0, 18 app/9 internal paths, bounded secret scan0, both
diff-check0, ledger/matrix/12-section report/README link validation; exit0.
Final base refs observed8df1654 and230c774; final app patch SHA recorded above.

No commits, pushes, stage operations, build-number edit, release dispatch,
hosted migration/deployment, secret/visibility change or device action occurred
in this corrective continuation. Source HEAD8df1654/docs230c774 remain the
base refs; only a coordinator may publish exact reviewed paths. Next step:
obtain the coordinator's corrected-source/release decision, then publish a new
numbered signed artifact and verify its assets. Do not redispatch/overwrite+27.

Declined-to-judge topics remain explicitly pending: hosted migration/RLS,
deployed adapters and live Telegram/teacher acceptance; Google rendering/
authorization; live OpenRouter/model availability; credential rotation; +27
installation/physical device lifecycle; transferring historical P40 facts to
current source. Unit/static review cannot establish those passes.

## 12. Remaining owner actions and why automation cannot close them

| Priority | Action | Why not autonomously completable | Guide |
|---|---|---|---|
| URGENT | Verify/retire exposed legacy Supabase credential; approve compatible-key migration and signed update | Privileged account access, session/client interruption and irreversible key retirement require owner control; legacy adapters need reviewed follow-up code | app docs/security/credential-rotation-runbook.md |
| HIGH | Apply reviewed Telegram migration, deploy functions, create/configure bot, register webhook and demonstrate own contact | Hosted schema/deploy forbidden without owner authorization; bot credentials absent and must stay private | app docs/owner/telegram-setup.md |
| HIGH | Obtain teacher approval of Telegram instead of SMS | Only instructor can accept requirement substitution | R-05 matrix |
| MEDIUM | Accept OSM deviation or approve secure Google origin/key/billing and live test | Teacher interpretation and paid/provider credentials are owner decisions; current file origin is unsuitable for reliable JS referrer restrictions | app docs/owner/maps-setup.md |
| MEDIUM | Perform live BYOK rewrite, removal and error demonstration | User-owned account/key/credit and explicit consent required; no key supplied | app docs/owner/openrouter-demo.md |
| AUTHORIZED / IN PROGRESS | Coordinator controlled publication and signed +28 | Owner authorization is recorded; security/review, committed-HEAD tests, CI, artifacts and runtime gates must be observed before completion. Original +27 must not be overwritten | exact changed paths and post-pass gate |
| MEDIUM | Install the newly corrected signed APK on a real phone, execute 26 smoke checks and save evidence | No physical device connected; genuine observation cannot be fabricated, +27 cannot serve as repaired-tree proof | app docs/qa/physical-device-checklist.md |
| REVIEW | Decide repository visibility | Account-level visibility consequences are owner-only; making private does not revoke leaked keys | security runbook |

Do not send credentials in chat. Use owner-controlled dashboards, secret
stores and in-app BYOK entry. The project remains an academic demonstration,
not production ticketing, billing or travel authority.

## Publication addendum — 2026-11-23

The 2026-11-21 authorization above was executed on 2026-11-23. Sections 1-12
remain the preparation/review record; this addendum is the only source for
publication results.

**Source.** Exactly the 18 reviewed app paths were committed as
`a3d2c305dc0a96bd952abffd8eaec3349be87f5b` on `main` under the owner identity
`sa-mahi12` and pushed; `.flutter-plugins-dependencies` and `.serena/` stayed
unstaged. Reviewed-path content SHA256 was unchanged from the reviewed
fingerprint. Flutter CI run
https://github.com/sa-mahi12/RailMate-BD/actions/runs/45212454835 succeeded on
that SHA.

**Committed-HEAD reruns (all exit 0).** Flutter 639 tests; Deno 33 (29 mocked
update cases + 4 actual-handler cases with mocked HTTP/storage); Node 11;
`dart format` 214 files/0 changed; `deno fmt` 4 files; `flutter analyze` no
issues. Final publishable-tree Gitleaks 8.30.1 rescans after the last privacy
redactions reported 0 findings in both repositories.

**Signed release.** One dispatch of the release workflow produced run
https://github.com/sa-mahi12/RailMate-BD/actions/runs/45213896700 (success) and
release https://github.com/sa-mahi12/RailMate-BD/releases/tag/v1.0.0%2B28 with
tag `v1.0.0+28` pointing at `a3d2c30`. `v1.0.0+27` was not redispatched: its
release id and all eight asset sizes/digests were captured before dispatch and
re-checked unchanged afterwards.

| Asset | Bytes | SHA256 |
|---|---:|---|
| RailMate-BD-1.0.0-universal.apk | 89,626,119 | `12934433e148f5b5edbcdad60263cf071456f83bb52c8b8cd556b04ffa65b581` |
| RailMate-BD-1.0.0-arm64-v8a.apk | 36,888,731 | `4cddfe0d43b3a1d5b0ee8e983a7661d1de87c79ce661c8a300f46f281e73bc71` |
| RailMate-BD-1.0.0-armeabi-v7a.apk | 32,126,231 | `f81f6db0a8b100ffec534e5674d0e75ba26b44060149f5512750ccd1bc20d407` |
| RailMate-BD-1.0.0-x86_64.apk | 40,309,313 | `13bdd890e3a77b9137247ab81c553fcb3efddcda754f6037d42e58c476ce07f1` |
| RailMate-BD-1.0.0.aab | 83,997,111 | `e97513fb6dd1ed6bb44852f410bd2e2d42967bf9dd85f20e8e73a4ae3c146b10` |
| SHA256SUMS.txt | 489 | `e79f08de2ec70011d321abe6fc5ef454537db2aa3521cf64f735270523c27cad` |
| release-manifest.json | 418 | `48fabb34ac3ea3568bb3a079a6541ee013eb7dde853b6db867fc508268fe198b` |
| PROVENANCE.md | 432 | `38ed556f49dc3ce5e8633618d738e159a49c347c7c37c45dfc95798b76295fac` |

Downloaded file sizes and SHA256 values match the GitHub API asset digests and
the published `SHA256SUMS.txt` for all five APKs/AAB.

**Signature and identity.** `apksigner verify --print-certs` reports
`Verifies` and `Verified using v2 scheme: true` for all four APKs, one signer
`CN=RailMate BD, OU=Demo Project, O=RailMate BD, L=Dhaka, C=BD`, certificate
SHA256 `37c67c4c119d3adea7dcbeaae99ae69d8ab14e231ca2fecee9b6134190f2f155`.
`aapt2 dump badging` reports package `bd.railmate.railmate_bd`,
`versionCode='4028'`, `versionName='1.0.0'`, target SDK 36. The published
manifest is still key/value text despite its `.json` name: `versionCode=28`,
`commit=a3d2c305dc0a96bd952abffd8eaec3349be87f5b`, `signed=true`. Provenance is
a workflow-generated unsigned summary naming that commit, run and version — not
a cryptographic attestation.

**Packaging repair verified in the real artifacts.** The universal APK, the
three split APKs and the AAB each contain `web-guide/map-provider.js` (4,240 B)
byte-identical to the committed blob, alongside `index.html`, `guide.js`,
`styles.css`, the bundled video, the poster and `assets/models/ranker.tflite`;
every local `<script src>` referenced by the bundled page is present. The +27
x86_64 APK contained five web-guide files and no `map-provider.js`; the +28
counterpart contains six. All seven required asset blobs compare equal in all
five artifacts.

**Emulator observation (not physical acceptance).** On AVD `railmate_pixel`
(Android 15, x86_64) the x86_64 `+28` APK installed (`versionCode=4028`), the
pulled installed `base.apk` was byte-identical to the release asset
(`13bdd890...`), the app launched without a RailMate BD crash entry (the crash
buffer held one unrelated Google Play Services failure) and reached the
login/create-account gate. The Station Guide sits behind an authenticated
session, so this pass did not open the guide page: **map rendering on `+28` is
NOT observed**, and no Google/OSM rendering claim is made. Creating a hosted
test account or using owner credentials was outside this authorization.

**Still open.** Hosted migration/deployment, bot and webhook setup, live
contact proof, teacher acceptance of the SMS alternative, Google secure-origin/
key/billing work, live OpenRouter BYOK demonstration, physical-phone smoke
test and retirement of the historical exposed credential remain owner actions.
R-20 EXEMPT and R-24 NOT ANNOUNCED are unchanged. No credential rotation,
visibility change, provider call or device-farm use occurred.
