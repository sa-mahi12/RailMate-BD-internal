# Detailed acceptance casebooks

All cases are planned, generated from the requirement-specific contexts, inputs and failures. Individual combinations may be superseded by instructor decisions or validated as redundant during test selection; do not claim they ran just because they exist. Cases for R-20 (explicit Crystal Report exception) and R-24 (not yet announced) are intentionally not fabricated.

| Requirement | Planned casebook | Case count |
|---|---|---:|
| R-01 ERD scalable PDF | [R-01_CASEBOOK.md](requirement_cases/R-01_CASEBOOK.md) | 36 |
| R-02 Real-time comments on own DB | [R-02_CASEBOOK.md](requirement_cases/R-02_CASEBOOK.md) | 36 |
| R-03 Live like/dislike count | [R-03_CASEBOOK.md](requirement_cases/R-03_CASEBOOK.md) | 36 |
| R-04 Live unique username | [R-04_CASEBOOK.md](requirement_cases/R-04_CASEBOOK.md) | 36 |
| R-05 Email and phone verification | [R-05_CASEBOOK.md](requirement_cases/R-05_CASEBOOK.md) | 36 |
| R-06 Text boxes and dropdowns | [R-06_CASEBOOK.md](requirement_cases/R-06_CASEBOOK.md) | 36 |
| R-07 Interactive real-time rating | [R-07_CASEBOOK.md](requirement_cases/R-07_CASEBOOK.md) | 36 |
| R-08 Pagination | [R-08_CASEBOOK.md](requirement_cases/R-08_CASEBOOK.md) | 36 |
| R-09 External audio/video embed | [R-09_CASEBOOK.md](requirement_cases/R-09_CASEBOOK.md) | 36 |
| R-10 Google Maps / iframe | [R-10_CASEBOOK.md](requirement_cases/R-10_CASEBOOK.md) | 36 |
| R-11 Session or JWT auth | [R-11_CASEBOOK.md](requirement_cases/R-11_CASEBOOK.md) | 36 |
| R-12 TFLite/equivalent on-device ML | [R-12_CASEBOOK.md](requirement_cases/R-12_CASEBOOK.md) | 36 |
| R-13 File upload + cloud storage | [R-13_CASEBOOK.md](requirement_cases/R-13_CASEBOOK.md) | 36 |
| R-14 Datepicker | [R-14_CASEBOOK.md](requirement_cases/R-14_CASEBOOK.md) | 36 |
| R-15 GSAP / Framer Motion | [R-15_CASEBOOK.md](requirement_cases/R-15_CASEBOOK.md) | 36 |
| R-16 SASS or Tailwind | [R-16_CASEBOOK.md](requirement_cases/R-16_CASEBOOK.md) | 36 |
| R-17 Git / modern workflow | [R-17_CASEBOOK.md](requirement_cases/R-17_CASEBOOK.md) | 36 |
| R-18 GraphQL / modern API layer | [R-18_CASEBOOK.md](requirement_cases/R-18_CASEBOOK.md) | 36 |
| R-19 RESTful / SOAP API | [R-19_CASEBOOK.md](requirement_cases/R-19_CASEBOOK.md) | 36 |
| R-21 Modern frontend | [R-21_CASEBOOK.md](requirement_cases/R-21_CASEBOOK.md) | 36 |
| R-22 Containerization or deployment pipeline | [R-22_CASEBOOK.md](requirement_cases/R-22_CASEBOOK.md) | 36 |
| R-23 Generative AI feature | [R-23_CASEBOOK.md](requirement_cases/R-23_CASEBOOK.md) | 36 |

### Test selection policy
At least one basic, one negative and one cross-account case per applicable requirement must be selected into core demonstration coverage. The full combinatorial corpus is optional regression depth, not a requirement to manually run thousands of cases for this four-month app. Keep runtime low: focused tests for code changes, CI suite for each integration, physical-device smoke before viva. Avoid redundant exhaustive live SMS/LLM requests that would charge money.

### Execution capture template
Case ID: ; tested SHA: ; observed time UTC: ; mode: UNIT-MOCK / STAGING / DEVICE / PROVIDER-LIVE / CI-BUILD; precondition: ; command/actions: ; expected: ; actual: ; result: PASS/FAIL/BLOCKED; linked artifact: ; cost authorization: ; reviewer: .
