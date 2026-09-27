# Course requirements — 24-row acceptance matrix

The source is the user-provided teacher screenshot, not the earlier RailMate plan. Every listed implementation is a PROPOSAL until verified. `#20=EXEMPT`; `#24=NOT ANNOUNCED`. No hardcoded mock equals a real provider demonstration.

| ID | Teacher requirement | Minimal integration | Evidence to mark PASS | Current status |
|---|---|---|---|---|
| R-01 | ERD scalable PDF | docs/erd/railmate.mmd, generated scalable PDF | ERD exported as PDF with all logical entities, cardinalities and relationships legible at 200% zoom. | NOT TESTED |
| R-02 | Real-time comments on own DB | Journey Board comments channel | Two accounts see a newly submitted comment without explicit refresh; source is Supabase Realtime and persistent Postgres. | NOT TESTED |
| R-03 | Live like/dislike count | Journey Board reactions | Like then dislike changes one user reaction and both clients see correct aggregate counts. | NOT TESTED |
| R-04 | Live unique username | registration usernames lookup + unique index | Concurrent same-normalized-name registration produces exactly one owner; availability is never sole protection. | NOT TESTED |
| R-05 | Email and phone verification | Supabase Auth email + provider-backed SMS/OTP | Both real verification flows demonstrated, phone provider and real SMS cost authorized; no fake OTP. | NOT TESTED |
| R-06 | Text boxes and dropdowns | search + registration + passenger forms | Multiple text and selectable form inputs validate and persist values. | NOT TESTED |
| R-07 | Interactive real-time rating | Journey Board 1–5 ratings | Per-user rating changes update aggregate on second client without reload. | NOT TESTED |
| R-08 | Pagination | Board cursor pagination five rows | Stable cursor loads next page without repeat/skip for fixed data snapshot. | NOT TESTED |
| R-09 | External audio/video embed | Station Guide YouTube embed | Real external video visibly plays in Android WebView. | NOT TESTED |
| R-10 | Google Maps / iframe | Station Guide Google Maps embed | Embedded map locates sample station in Android WebView. | NOT TESTED |
| R-11 | Session or JWT auth | Supabase Auth session/JWT | Session restores, expires/refreshes safely, logout blocks protected data. | NOT TESTED |
| R-12 | TFLite/equivalent on-device ML | TFLite search ranking | Bundled .tflite runs on Android and visibly changes scores with different input. | NOT TESTED |
| R-13 | File upload + cloud storage | Supabase Storage post image | Image bytes uploaded to protected bucket and visible according to policy. | NOT TESTED |
| R-14 | Datepicker | departure date | Picker selects date and invalid old dates are rejected. | NOT TESTED |
| R-15 | GSAP / Framer Motion | Station Guide GSAP | Visible entrance animation observed in embedded HTML page. | NOT TESTED |
| R-16 | SASS or Tailwind | Station Guide SASS | SCSS compiled to CSS and loaded by embedded page; unused SCSS does not count. | NOT TESTED |
| R-17 | Git / modern workflow | GitHub single-main direct commits | Authenticated owner commits, pushes and has traceable history; no extra branch or PR. | NOT TESTED |
| R-18 | GraphQL / modern API layer | Supabase pg_graphql | One real authenticated query returns stations from hosted DB. | NOT TESTED |
| R-19 | RESTful / SOAP API | Supabase generated PostgREST | App calls real hosted REST endpoint through SDK/network layer. | NOT TESTED |
| R-20 | Crystal Report — exception | none | Explicit exception; mark EXEMPT and do not fabricate integration. | EXEMPT |
| R-21 | Modern frontend | Flutter Android | Native app launches on phone and relevant screens respond. | NOT TESTED |
| R-22 | Containerization or deployment pipeline | GitHub Actions CI | Hosted CI actually analyzes/tests/builds debug APK; Docker not needed. | NOT TESTED |
| R-23 | Generative AI feature | OpenRouter user BYOK rewrite | User supplies/removes key, action calls real LLM and handles errors without breaking booking. | NOT TESTED |
| R-24 | TBD additional task-specific | future decision gate | Record teacher announcement and implement only after scope approval; currently NOT ANNOUNCED. | NOT ANNOUNCED |

## Pass discipline
A requirement is PASSED only when a saved dated result references a precise source commit, test or actual device observation, backend project reference redacted as appropriate, and relevant screenshot/log. A green unit test proves the unit only. Unavailable SMS billing or provider configuration must be BLOCKED and brought to instructor; do not mark skipped as passed.

### Coverage IDs
The appendix contains generated planned cases `R-xx-Tyyy`; select smoke cases for every CI run, then full relevant cases before viva. Each appendix scenario is *not* a test result.
