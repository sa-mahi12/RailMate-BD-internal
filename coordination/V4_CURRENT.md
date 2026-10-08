# V4 CURRENT — FREEZE (P36)

Timestamp: 2026-10-05 ~18:10 UTC
Code HEAD: e4187b1 (pushed; CI `flutter test` gates)
Docs HEAD: this commit
Phase: V4 product polish — COMPLETE except owner-deferred device work

## VERIFIED (34 of 37 V4 tasks)
- P00 baseline, P01 design/motion layer, P02 icon+splash, P03 app gate,
  P04 onboarding, P05 auth, P06 register/forgot-password, P07 username+
  confirm-password, P08 verification, P09 home shell, P10 home sections,
  P11 station/service drafts, P12 richness migration (live, 648-trip
  refresh proven idempotent), P13 search polish, P14 seat polish,
  P15 passenger/review polish, P16 payment polish, P17 ticket polish,
  P18 history polish, P19 board posts draft, P20 board feed polish,
  P21 engagement motion, P22 station guide, P23 profile polish, P24 AI UX
  polish, P25 ranking honesty caption, P26 state library, P27 a11y pins,
  P28 release signing, P29 release workflow, P30 release evidence,
  P31 root-flow integration, P32 screen audit, P33 backend QA.

## BLOCKED_OWNER (binding deferral, OWNER_DIRECTIVE_DEVICE_TESTS.md)
- P34 device walkthrough — PERMANENTLY DEFERRED until the owner lifts it
  separately. Nothing here is device-verified.
- P35 release screenshots — same deferral.
- SMS provider (carried from V3; phone OTP honestly reports unavailability).
- Social login remains unimplemented by design; the UI says so.

## BLOCKED_EXTERNAL
- (none)

## IN_PROGRESS / READY_FOR_REVIEW
- (none)

## Demo-data state (live, verified 2026-10-05)
- 24 stations, 32 service codes, 726 demo trips (8 legacy + 648 current),
  29,080 seats, every trip 40 seats, occupancy avg 57.5% (0–85% spread).
- Horizon refresh is idempotent (648 again, zero churn). Horizon runs to
  2026-10-24 (today+20); retired codes RM741/RM753 age out as documented.
- 0 profiles, 0 bookings: no test rows in production.
- Board posts: none seeded (deliberate — no fake community content).

## Release state
- Latest: **v1.0.0+3 (build 3)**, signed, installable over old builds:
  universal + 3 ABI APKs + AAB, SHA256SUMS.txt, release-manifest.json,
  PROVENANCE.md. Universal APK sha256 recorded in `handoffs/P30.md` footer.
- versionCode monotonic (2 → 3). Release evidence parser pinned against the
  real published manifest (`tool/release_evidence.dart`, 14 tests).

## Last gates
- format: clean
- analyze: clean (full repo, including new test dirs)
- tests: **476/476 green**
- visual: owner-deferred (no claim)
- device: owner-deferred (no claim)

## Known follow-ups (not regressions, tracked for a future pass)
- 2.0x accessibility text scale still overflows in some fixed-height rows;
  1.5x is proven clean.
- `refresh_demo_horizon()` is invoked manually; if it is not re-run, the
  horizon expires ~2026-10-24. A scheduled refresh needs a service-role
  secret the repo correctly never holds.
- Live two-account RLS proof was last done in V3; V4 made no schema/RLS
  change, but re-running is on the next backend touch.
- Resend-countdown, ticker and shimmer animations are correct but were only
  ever host-asserted, never eyeballed on a screen.

## Exact next action
1. Nothing open. The next session starts only on a new owner instruction
   (device deferral lift, new feature, or backend touch).
