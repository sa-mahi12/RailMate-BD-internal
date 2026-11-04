# Demo-readiness pass (P39) — 2026-11-04

Coordinator-run after the `v1.0.0+11` release. No app code, CI, secrets or
release assets changed; app HEAD remains `41e8e57` and +11 remains the build.

## 1. Demo timetable refreshed
The released +11 app lets the owner pick today..today+20, but the hosted
timetable stopped at `2026-11-08`. From 2026-11-09 onward search would honestly
show no trains, i.e. the demo would look broken within days.

- Ran the existing owner/admin RPC: `select public.refresh_demo_horizon(20)`
  -> returned `648` (the documented idempotent slot count).
- Hosted after: trips `1186 -> 1682`, trip seats `47320 -> 67160`,
  `min departure 2026-09-28`, `max departure 2026-11-24`.
- Last selectable day (today+20) holds `32` trips. `bookings=0`,
  occupied seats `0`, so the refresh did not touch any confirmed booking.
- Four stale trips from 2026-10-15/16 still carry only 10 seats instead of 40.
  They are past the picker window and unreachable from the app; left untouched
  rather than deleting data outside this packet.

## 2. Auth-function advisories closed
Before: advisors 0011 (`normalize_username` mutable search_path) and 0028/0029
(`bootstrap_new_user` SECURITY DEFINER callable by `anon`/`authenticated`).

- Migration applied hosted as version `20261104060034`
  (`auth_function_hardening`), committed as
  `supabase/migrations/20261104000001_auth_function_hardening.sql`.
- `public.normalize_username()` recreated with `SET search_path = ''` and
  `pg_catalog`-qualified `lower`/`btrim`.
- `EXECUTE` on `public.bootstrap_new_user()` revoked from `PUBLIC`, `anon` and
  `authenticated`. ACL now `postgres=X | service_role=X`. Both functions are
  trigger-only, and PostgreSQL does not check EXECUTE when a trigger fires.
- Smoke test (`mailjet-gate/auth-hardening-smoke.ps1`, exit 0):
  admin-created user still got its profile row and a normalised username claim;
  anonymous `POST /rest/v1/rpc/bootstrap_new_user` returned HTTP 404 (no longer
  exposed); smoke user deleted, rows cascaded.
- Advisors re-read: 0011/0028/0029 gone. Remaining WARNs are deliberate:
  0026/0027 pg_graphql table exposure (required for R-18 and for PostgREST
  grants; row access stays RLS-gated) and `auth_leaked_password_protection`
  disabled — enabling it would reject the owner's chosen demo password.

## 3. Live user-flow verification (hosted, `exit=0`)
Script `mailjet-gate/verify-user-flows.ps1`, using the seeded demo account:

| Flow | Observed |
|---|---|
| Login | password grant issued a session |
| Photo upload | authenticated upload to `<uid>/verify-*.png` -> HTTP 200 |
| Photo read | public URL -> HTTP 200, 70 bytes |
| Photo delete | own object delete -> 200/204 |
| Board write | own post + comment + reaction accepted under RLS, then removed |
| Logout | global logout ok; refresh token rejected afterwards (HTTP 400) |
| Password recovery | `POST /auth/v1/recover` -> HTTP 200 (real Mailjet dispatch) |

Limits stated honestly:
- Access JWTs stay valid until their normal expiry after logout; the client
  discards its session. No "instant JWT death" claim.
- The recovery request proves dispatch was accepted, not inbox delivery; one
  real recovery email was sent to the owner address on 2026-11-04.
- Independent owner-side signal: a real 645 KB `.jpg` appeared in `post-media`
  at 11:58 +06:00, so photo upload has been exercised from the app itself.

## 4. Live booking E2E (deployed Edge Functions, `exit=0` per step)
Script `mailjet-gate/booking-e2e-steps.ps1`; every state claim below was read
back with SQL, because `@(Invoke-RestMethod ...)` wraps a JSON array as one
element (an empty result reports `Count=1`) and would make count assertions
vacuous.

| Step | Result |
|---|---|
| Declined simulation (`simulateSuccess=false`) | `PAYMENT_SIMULATION_FAILED` + `DEMONSTRATION ONLY - no booking created, no charge`; booking count and held-seat count unchanged, so nothing was written |
| 2-passenger booking | `CONFIRMED`, booking `cddd66e6-...`, fare 1080, seats `A9`/`B1`, `booking_seats=2`, held seats `2` |
| Cancel | `CANCELLED`; held seats back to `0`; seats no longer tied to the booking; passenger/seat audit rows kept |
| Final demo booking (kept) | `f463cead-...` `CONFIRMED`, passengers `Sanjida Mahi` + `Demo Companion`, seats `A2`/`A3`, fare 1250, Dhaka -> Chattogram, departs 2026-11-06 07:00 Asia/Dhaka |

Hosted totals after the pass: 2 booking rows (1 CONFIRMED + 1 CANCELLED
history), 2 held seats, 0 seats with a stale booking id.

## 5. Data hygiene
Verification posts, comments, reactions and storage objects were deleted. Live
counts after the pass: 1 seed post, 1 comment, 1 reaction, 1 storage object (the
owner's uploaded photo), 1 profile/username (demo account), 1682 trips, 0
bookings.

## 6. What is still owner-side
1. Install `v1.0.0+11`; log in with the seeded demo account.
2. Change the weak demo password before demonstrating.
3. Accept the email lane by reading one real signup OTP, or use the recovery
   email already sent.
4. SMS provider + approved recipient for the live phone-OTP claim.
5. Rotate the legacy exposed privileged key (unchanged owner task).
6. Two-device realtime observation is not required (owner dropped device proof).

## 7. Signup / email-OTP lane (addendum, 12:45 +06:00)

The owner reported that creating an account "seems to fail". Both halves of the
lane were therefore re-proven, and the probe accounts were cleaned up.

### 7.1 On-device proof with the published build
Installed the released `RailMate-BD-1.0.0-x86_64.apk` (SHA256 matched
`SHA256SUMS.txt`) on the emulator, cleared app data, and drove the real UI:

| Step | Observed |
|---|---|
| Fresh launch | onboarding -> Welcome |
| Create Account -> form | filled; live username checker showed *Available* |
| Submit | **Verify your account** screen, "Enter the 6-digit code ..." |
| Six-digit code | accepted -> Home ("Good afternoon, UI Probe") |
| Profile | *Email verified*, `@uiprobe2026` |
| Home date picker | days listed through **2026-11-24** (refreshed horizon) |

So the shipped +11 build completes signup + OTP verification end to end; the
failure the owner saw is not a broken lane.

### 7.2 Backend contract replay
`POST /auth/v1/signup` -> 200 with `confirmation_sent_at`; OTP verified with
`type=email` -> session with `email_confirmed_at`; the bootstrap trigger created
the profile and the normalised username. No 4xx/5xx signup responses and no SMTP
error events appeared in the auth logs for the window examined.

### 7.3 Client-side rules that can look like a failure
- Password is validated locally: **minimum 8 characters**. A shorter value never
  reaches the server and the screen only shows the generic
  *"Registration failed. Please try again."* - indistinguishable from a network
  failure to a user.
- Username: normalised to lowercase, must be 3-20 chars of `[a-z0-9_]` and start
  with a letter.
- An existing account for the same address yields *"An account with this email
  already exists. Try logging in instead."*

### 7.4 Genuine OTP send (packet step 4)One genuine signup OTP was requested for the owner-requested recipient through
the real Auth signup endpoint at 12:25 +06:00: Auth replied 200 with
`user_confirmation_requested` and the Mailjet dispatch was accepted. **Inbox
delivery and code entry are NOT verified** - per the packet only the inbox holder
can report receipt and type the code. The address is withheld from this PUBLIC
docs repo, and the temporary account created for that send was deleted so the
owner can register the address with their own password.

### 7.5 Cleanup
`railmate.probe*`, `railmate.pw*`, `railmate.ui.probe`, `railmate.shortpw` and
the temporary OTP-send account were deleted. Verified afterwards: `auth_users=1`
(demo), `profiles=1`, `usernames=1`, 0 orphan profile/username rows.

### 7.6 Open question for the owner
Which symptom did the failed attempt show: the generic *"Registration failed.
Please try again."*, a verify screen with no code email, or a rejected code?
That answer decides between (a) surfacing the local validation message and
shipping build +12, or (b) chasing Mailjet/Gmail deliverability with the owner's
dashboard.

### 7.7 Mailjet pipe + template content (verified without an owner inbox)
To separate "email does not arrive" from "app does not work", a signup was made
against a **disposable third-party mailbox** (address withheld; the auth user was
deleted straight after). Findings:

| Check | Result |
|---|---|
| Delivery | railmate message arrived in ~10 s at a provider that spam-filters aggressively |
| Subject | `Verify your RailMate BD account` |
| Body | OTP-only: "Enter this one-time verification code in the RailMate BD app to complete your registration" + the six digits |
| Confirmation link | **none** - the only URLs in the body are Mailjet open/click tracking (`*.mjt.lu`), so the packet's "no confirmation button/link" rule holds |
| Sender | the owner Gmail address, which is why Gmail itself may file these under Spam |

So the email lane is functional at the provider level as of 12:5x +06:00; a
missing code on the owner's phone most likely means Spam/Promotions placement
rather than a broken send.
