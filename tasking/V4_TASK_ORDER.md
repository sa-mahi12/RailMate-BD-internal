# V4 Task Order

1. **P00 — Recover baseline and open V4 coordination** — COORDINATOR; deps: none
2. **P01 — Central design tokens and motion primitives** — WORKER_A; deps: P00
3. **P02 — Branding, launcher icon, app name and splash** — COORDINATOR; deps: P00
4. **P03 — Root application gate and onboarding persistence** — COORDINATOR; deps: P00
5. **P04 — Three-page onboarding experience** — WORKER_B; deps: P01, P03
6. **P05 — Welcome and Login experience** — WORKER_B; deps: P01, P03
7. **P06 — Forgot-password flow** — WORKER_B; deps: P05
8. **P07 — Registration, live username and confirm-password** — WORKER_B; deps: P05
9. **P08 — Email verification and phone-verification states** — WORKER_B; deps: P07
10. **P09 — Animated app shell and bottom navigation** — WORKER_A; deps: P01, P03
11. **P10 — Home personalization and content sections** — WORKER_C; deps: P01, P03
12. **P11 — Expand station and service demo catalog** — WORKER_C; deps: P00
13. **P12 — Rolling 21-day demo generation migration** — COORDINATOR; deps: P11
14. **P13 — Search/date alignment and richer result cards** — WORKER_C; deps: P10, P12
15. **P14 — Seat-selection visual and motion polish** — WORKER_D; deps: P01, P12
16. **P15 — Passenger and review stepper polish** — WORKER_D; deps: P14
17. **P16 — Payment state polish** — WORKER_D; deps: P15
18. **P17 — Ticket and PDF visual polish** — WORKER_D; deps: P16
19. **P18 — Bookings history/details/cancel polish** — WORKER_D; deps: P16
20. **P19 — Seed populated Journey Board demo content** — WORKER_E; deps: P00
21. **P20 — Journey Board visual and motion polish** — WORKER_E; deps: P01, P19
22. **P21 — Comments/reactions/ratings interaction motion** — WORKER_E; deps: P20
23. **P22 — Expand Station Guide data and presentation** — WORKER_E; deps: P01
24. **P23 — Profile/settings/about polish** — WORKER_E; deps: P01, P08
25. **P24 — OpenRouter UX polish** — WORKER_E; deps: P23
26. **P25 — TFLite ranking presentation polish** — WORKER_C; deps: P13
27. **P26 — Global loading/empty/error/success states** — WORKER_A; deps: P01
28. **P27 — Accessibility and reduced-motion pass** — WORKER_F; deps: P04, P09, P13, P18, P21, P23
29. **P28 — Release signing configuration** — COORDINATOR; deps: P02
30. **P29 — Release CI workflow: universal/split APK and AAB** — COORDINATOR; deps: P28
31. **P30 — Versioning, release manifest and provenance** — WORKER_F; deps: P29
32. **P31 — Root/onboarding/auth integration tests** — WORKER_F; deps: P04, P05, P06, P07, P08
33. **P32 — Visual/motion integration QA** — WORKER_F; deps: P09, P13, P18, P21, P22, P23, P26
34. **P33 — Rich-data/backend QA** — WORKER_F; deps: P12, P13, P19, P22
35. **P34 — Release APK physical-device walkthrough** — COORDINATOR; deps: P27, P29, P31, P32, P33
36. **P35 — Screenshot pack and final visual defect pass** — WORKER_F; deps: P34
37. **P36 — Final V4 evidence matrix and freeze** — COORDINATOR; deps: P35
