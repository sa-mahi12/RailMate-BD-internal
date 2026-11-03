# Teacher final gate — code pass (2026-11-03)

Packet: owner-supplied `RailMateBD_Handoff_01_Teacher_Final_Gate_Code_2026-11-03.zip`
(frozen code baseline, three packets: PHONE_OTP, COMMENTS_REALTIME,
REACTIONS_REALTIME). This pass is the CODE pass; the six-feature acceptance
itself is the owner's live demo at the evaluation.

## Repos / SHAs

| Repo | Before | After | Note |
|---|---|---|---|
| `RailMate-BD` (app) | `a265c92` | `cafa3f0` | `cafa3f0` is the `+10` release commit |
| `RailMate-BD-internal` (docs) | `a5d6273` | this commit | this handoff + V4_CURRENT + ledger + roster |

## What changed (code)

1. **Phone OTP is reachable and real** (`lib/features/auth/phone/*`,
   `verify_screen.dart`, `app_gate.dart`, `dependencies.dart`).
   * `AppDependencies.create()` composes `SupabasePhoneOtpClient` — the fake
     is test-only.
   * `SupabasePhoneOtpClient` is session-aware: signed in →
     `updateUser(UserAttributes(phone:))` then
     `verifyOTP(type: OtpType.phoneChange, phone:, token:)` (attaches the
     number to the existing account, no identity swap); no session →
     `signInWithOtp(phone:)` then `verifyOTP(type: OtpType.sms, ...)`
     (genuine phone sign-in lane).
   * The Verify screen's phone button now pushes `PhoneVerifyScreen` instead
     of an "arrives later" dialog. The DEMO notice and the "no real code"
     copy render only when `PhoneState.isDemo` (the test fake).
2. **Realtime comments** (`comment_section.dart`, `feed_screen.dart`,
   `home_shell.dart`). One shared `public.post_comments` channel at the shell
   root maps INSERT/UPDATE/DELETE payloads to `CommentRealtimeEvent`s on a
   broadcast stream; every card subscribes. Events for other posts are
   ignored; deletes match only ids the loaded thread shows (the table keeps
   the default replica identity, so DELETE carries only `id`); a thread that
   was never loaded merges nothing, so no count is invented; an echoed own
   insert dedupes by row id.
3. **Realtime reaction counts** (`reaction_realtime.dart`,
   `post_engagement.dart`, `feed_screen.dart`, `home_shell.dart`). One shared
   `public.post_reactions` channel maps INSERT/UPDATE/DELETE to
   `ReactionRealtimeEvent`s carrying `post_id` (the PK is
   `(post_id, user_id)`, so delete payloads carry it too). A card filters to
   its own post and calls the existing authoritative `refresh()` — counts are
   recomputed from rows, so an echo costs one refetch and can never
   double-increment.
4. **Hosted Realtime publication** (the actual blocker).
   `pg_publication_tables` showed NO `public` table in `supabase_realtime`
   (only internal `realtime.messages_*`), i.e. Postgres Changes delivered
   nothing at all — the pre-existing `public.posts` feed channel was dead too.
   With owner approval, `public.posts`, `public.post_comments` and
   `public.post_reactions` were added (additive, reversible, no data touched).
   Recorded as `supabase/migrations/20261103000001_realtime_publication.sql`
   (idempotent DO block) so the repo matches hosted state.
5. README honesty: phone OTP is no longer described as unimplemented; the
   realtime publication + test count are stated, with the SMS/live proof limit
   spelled out.

Untouched, as instructed: session/JWT, username availability, email
verification, Storage upload, booking/atomic RPC, maps, TFLite, GSAP/SASS,
GraphQL, pagination, ticket PDF, AI/BYOK, timetable.

## Evidence (graded, never promoted)

* **STATIC** — `dart format --set-exit-if-changed lib test tool`: clean
  (197 files, 0 changed). `flutter analyze --no-pub`: No issues found.
* **UNIT-MOCK / hermetic widget** — full suite **542/542** green locally and on
  CI (`Flutter CI - main only`, run `41661488425`, commit `cafa3f0`).
  New in this pass (19 tests):
  * `test/board/comment_section_realtime_test.dart` (7): external insert with
    no refetch, external delete, other-post ignored, own-echo dedupe,
    no-merge-before-load, dispose cancels, signed-out read-only while live.
  * `test/board/post_engagement_realtime_test.dart` (7): external insert,
    update like→dislike, delete, other-post ignored, own-echo no double count,
    signed-out sees live counts but cannot vote, dispose cancels.
  * `test/phone_production_wiring_test.dart` (5): production adapter identity
    + demo flag, test composition is fake, phone button opens
    `PhoneVerifyScreen` (no dialog), no `DEMO`/`123456`/`no real code` in
    production copy, demo notice gated on the fake.
* **INTEGRATION-STAGING (hosted config only)** — `pg_publication_tables` now
  lists `public.posts`, `public.post_comments`, `public.post_reactions` in
  `supabase_realtime` (observed via SQL on
  `psuzlyingfmstnyfvlnj.supabase.co`). This is publication configuration, not
  an end-to-end event observation.
* **CI-BUILD** — release run `41661512576` green: `v1.0.0+10` is LATEST with
  8 assets (4 signed APKs, AAB, `release-manifest.json`, `SHA256SUMS.txt`,
  `PROVENANCE.md`). Manifest: `versionCode=10`,
  `commit=cafa3f01c67a66dd647f7cf40f27f0cae786c78a`, `signed=true`.
* **DEVICE** — none. No emulator/device is available in this environment and
  the owner dropped device verification (P34/P35 SUPERSEDED). No claim above
  is device-verified.
* **PROVIDER-LIVE (SMS)** — none. No OTP was sent; that requires the hosted
  project to have an SMS provider and an owner-approved test recipient.

## Six-feature checklist status (honest)

1. Session/JWT — regression-only, code untouched. No new live proof this
   pass; prior hosted evidence stands.
2. Live username availability — regression-only, code untouched. Server
   uniqueness remains the arbiter; no new live proof this pass.
3. Email + phone verification — email lane untouched. Phone lane is now
   production-reachable and hermetic-tested; **live SMS delivery is NOT
   verified** (owner-side provider/recipient).
4. Cloud upload — regression-only, code untouched. No new live proof this
   pass.
5. Realtime comments — code + single per-table channel + hosted publication
   enabled; hermetic cross-client tests green; ships in `+10`. **Two-device
   runtime observation not performed.**
6. Like/dislike live count — same as 5, with the authoritative-refetch
   reconcile.

## Blockers handed on

* **BLOCKED_OWNER — SMS provider/recipient for live phone OTP.** The code path
  is ready; without a configured provider the request fails honestly (no fake
  code, no fallback). Owner must configure the provider and test with a real
  handset before claiming the phone item live.
* **Runtime demonstration is owner-side** (teacher evaluation). Install
  `v1.0.0+10` (commit `cafa3f0`) on two clients to observe cross-client
  comments/counts without refresh.

## Next action

Owner: install `+10`, confirm the phone provider question, then run the
six-feature demo. If live SMS is unavailable, present the phone lane as
"wired, provider pending" rather than claiming a delivered code.
