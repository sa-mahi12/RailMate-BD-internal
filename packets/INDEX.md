# Bounded execution packet index

Every packet is individually scoped. A worker sees only its allowed paths, dependency contract and task-specific source. `MAIN` means coordinator-only action, not background automation. Full source/acceptance is in private docs; only actual verified evidence can change task status.

| Packet | Title | Lane | Prerequisites |
|---|---|---|---|
| S01 | [Read-only machine and identity preflight](S01.md) | MAIN | none |
| S02 | [Create exactly two private repositories](S02.md) | MAIN | S01 |
| S03 | [Create one hosted Supabase project](S03.md) | MAIN | S02 |
| S04 | [Inspect Supabase SMS and Auth costs](S04.md) | MAIN | S03 |
| S05 | [Validate AgentRouter DeepSeek route](S05.md) | MAIN | S01 |
| S06 | [Enumerate and resume free worker sessions](S06.md) | MAIN | S05 |
| S07 | [Configure lean MCP skills and LSP](S07.md) | MAIN | S06 |
| S08 | [Create Flutter skeleton and hosted CI](S08.md) | MAIN | S02,S03,S07 |
| A01 | [Build Supabase app bootstrap](A01.md) | A | S03,S08 |
| B01 | [Seed public station and trip dataset](B01.md) | B | S03,S08 |
| A02 | [Email Auth and verified session](A02.md) | A | A01 |
| B02 | [Username server uniqueness](B02.md) | B | A01 |
| A03 | [Phone OTP with provider gate](A03.md) | A | S04,A02 |
| B03 | [Trip search REST-backed UI](B03.md) | B | B01,A01 |
| B04 | [GraphQL station query](B04.md) | B | B01 |
| A04 | [Seat inventory and selection](A04.md) | A | B01,B03 |
| B05 | [Multi-passenger form and review](B05.md) | B | A04 |
| A05 | [Atomic booking function and Edge route](A05.md) | A | A04,B05 |
| B06 | [Simulated payment state](B06.md) | B | A05 |
| A06 | [E-ticket QR and PDF](A06.md) | A | A05,B06 |
| B07 | [Booking history and cancel](B07.md) | B | A05,A06 |
| A07 | [Board posts and media](A07.md) | A | A02 |
| B08 | [Real-time comments and pagination](B08.md) | B | A07 |
| A08 | [Live reactions and ratings](A08.md) | A | A07,B08 |
| B09 | [Station guide HTML/CSS/JS](B09.md) | B | S08 |
| A09 | [Tiny hosted ML training](A09.md) | A | B03 |
| A10 | [On-device search inference](A10.md) | A | A09,B03 |
| B10 | [OpenRouter BYOK secure vault](B10.md) | B | A02 |
| B11 | [One generative rewrite feature](B11.md) | B | B10,A07 |
| I01 | [Integrate final navigation](I01.md) | MAIN | A02,B03,A06,B07,A08,B09,A10,B11 |
| Q01 | [RLS cross-account verification](Q01.md) | MAIN | A05,A07,A08 |
| Q02 | [Booking collision integration](Q02.md) | MAIN | A05,B07 |
| Q03 | [Course feature live smoke](Q03.md) | MAIN | I01 |
| Q04 | [GitHub Actions and APK proof](Q04.md) | MAIN | I01,Q01,Q02 |
| R01 | [Final ERD and docs submission](R01.md) | MAIN | Q03,Q04 |
| R02 | [Freeze release and handover](R02.md) | MAIN | R01 |
