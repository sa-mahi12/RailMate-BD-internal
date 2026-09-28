# SESSION ROSTER

| Session | Model | Lane | Task | Allowed paths | Last checkpoint | State |
|---|---|---|---|---|---|---|
| coordinator | muse-spark-1.3 | integration | F00 | shared (lib/main.dart, lib/app/**, pubspec*, android/*, .github/**, migrations, git) | 2026-09-28 F00 reconcile | active |
| worker-a | - | auth/profile | - | lib/features/auth/**, lib/features/profile/** | - | standby |
| worker-b | - | booking | - | lib/features/search/**, lib/features/booking/**, lib/features/bookings/**, lib/features/ticket/** | - | standby |
| worker-c | - | board | - | lib/features/board/** | - | standby |
| worker-d | - | guide-ai-ml | - | lib/features/station_guide/**, web-guide/**, lib/features/ai/**, lib/features/search/ml/**, ml/** | - | standby |
| reviewer | - | QA | - | read-only | - | standby |
