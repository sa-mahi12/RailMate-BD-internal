# RailMate BD — Install & Demo Guide (2026-09-27, code SHA 0994746)

## 1. Prereqs
- Flutter 3.47.5 (Dart 3.13.4), Android SDK 36 + build-tools, JDK 17 for builds.
- Accounts: GitHub `sa-mahi12`, Supabase project ref `psuzlyingfmstnyfvlnj` (Singapore).

## 2. Run the app (debug)
1. `git clone https://github.com/sa-mahi12/RailMate-BD` (PRIVATE, main only), `cd RailMate-BD`.
2. Create `app.env.json` next to pubspec: `{"SUPABASE_URL":"https://psuzlyingfmstnyfvlnj.supabase.co","SUPABASE_ANON_KEY":"<anon>","SUPABASE_SERVICE_ROLE_KEY":""}` (never commit).
3. `flutter pub get && flutter analyze && flutter test` (expect 108/108 at SHA 3d2f656; later SHAs re-run).
4. Connect a phone (`adb devices`), `flutter run` — or install the CI APK (SHA e77d14b7…, see handoffs/Q04.md).

## 3. Backend (already applied, read-only)
- `supabase link --project-ref psuzlyingfmstnyfvlnj`, `supabase migration list` → 8/8 in sync.
- Seed: 4 stations (DAC/CGP/SYL/RJH), 4 trips, 40 seats. Search DAC→CGP to demo.
- Auth: email flow works when Supabase SMTP configured; SMS needs provider/budget (BLOCKED, S04).

## 4. Demo script (5 min)
1. Boot → 4 tabs (Home/Search, My Trips, Board, Guide).
2. Search DAC→CGP, pick seats, add passengers (ref-4 fare math 2×700+40=1440), simulated payment, DEMO ticket.
3. Board: compose post → comment → like → rating (works offline-first in UI; live sync needs login).
4. Guide: offline station cards (embeds pending teacher approval).
5. AI Settings: save BYOK key → Test Connection (stub reply, DEMONSTRATION ONLY).

## 5. ML (R-12)
- Hosted training: Actions `ml-train` run 36304165531 SUCCESS → `assets/models/ranker.tflite` (1280B).
- On-device two-vector score proof: NOT DONE (needs phone, minSdk 26 note in A10 handoff).

All tickets state DEMONSTRATION ONLY. No real money, no real SMS, no production data.
