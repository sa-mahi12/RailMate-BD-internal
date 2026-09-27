# DECISIONS.md — Windows adaptation (2026-09-27)
- D1: Use native Windows + PowerShell; no WSL switch (per First_Instruction Prompt 1).
- D2: Local folders are D:\RailMateBD (code) + D:\RailMateBD-internal (docs), mapping to remotes RailMate-BD / RailMate-BD-internal. Do not create extra hyphen variants on D:.
- D3: Remote creation BLOCKED until gh installed + auth + explicit CREATE confirmation. No overwrite of existing paths/remotes.
- D4: Hosted Supabase only; no Docker/Postgres/local DB.
- D5: Context cap policy: configuredContext = min(256000, VERIFIED_REAL_LIMIT). No fake 256K.
- D6: Max 2 workers, 1 heavy op at a time via coordination/heavy.lock.
- D7: No secrets in git; service-role never in app; OpenRouter BYOK only.
