# SESSION ROSTER

| Session | Model | Lane | Task | Allowed paths | Last checkpoint | State |
|---|---|---|---|---|---|---|
| coordinator | muse-spark-1.3 | integration | F06+F15 launch, F07 | shared (lib/main.dart, lib/app/**, pubspec*, android/*, .github/**, migrations, git) | 2026-09-28 F05 verified, wave1 pushed e9adfb7 | active |
| worker-a | - | auth/profile | F03 done | lib/features/auth/**, lib/features/profile/** | 2026-09-28 handoff reviewed, in 9b20cbc | standby |
| worker-b | - | booking | F06 | lib/features/search/**, lib/features/booking/**, lib/features/bookings/**, lib/features/ticket/** | assigned 2026-09-28 | standby→active |
| worker-c | - | board | F11 done | lib/features/board/** | 2026-09-28 handoff reviewed, in 9b20cbc | standby |
| worker-d | - | guide-ai-ml | F15 | lib/features/station_guide/**, web-guide/**, lib/features/ai/**, lib/features/search/ml/**, ml/** | assigned 2026-09-28 | standby→active |
| reviewer | - | QA | - | read-only | - | standby |
