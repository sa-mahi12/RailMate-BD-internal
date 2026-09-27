# Viva notes + truthful limitations (2026-09-27)

## What is REAL
- Flutter app, 108 unit/widget tests green, CI green (run 36307419959) + APK SHA-verified.
- Hosted Supabase: 12-table schema, RLS, atomic booking RPC (source-reviewed, migration applied), seed data, live REST + GraphQL reads, anon-write denials verified live.
- Hosted-trained TFLite ranker (CI run 36304165531, SHAs verified) + on-device interpreter wiring with labelled fallback.
- BYOK vault (Keystore) + rewrite accept/reject; 4-tab navigation; ERD PDF (this folder).

## What is NOT proven (say this in viva)
1. Live SMS OTP — no provider/budget (S04). Phone UI falls back, no fake OTP.
2. Two-client realtime/board sync — code + units only, no second device run.
3. Booking collision live proof — RPC is service-role-only; Edge deploy needs service_role key (owner step, Q02).
4. YouTube/Maps/GSAP/Sass — NO teacher approval recorded; placeholders only (R-09/10/15/16 BLOCKED).
5. On-device ML scores, device install/launch — no phone was attached during build.
6. Storage bucket upload proof — policies applied, bucket + upload not verified live.
7. Live OpenRouter call — stub only; needs owner key + budget.

## Likely questions
- "Is the booking atomic?" → Yes in one Postgres transaction (FOR UPDATE + unique request_id); live overlap test is the documented owner step.
- "Is that ML or a sort?" → Real .tflite (interpreter path) with a fallback that is explicitly labelled NON-ML; training ran in CI on synthetic data only.
- "Where is the key?" → User key in Android Keystore, per-account, single-use consent; AgentRouter/coordinator keys never in the app.
- "Why two repos?" → Governance: code repo + private docs repo, single main each, no PRs.
