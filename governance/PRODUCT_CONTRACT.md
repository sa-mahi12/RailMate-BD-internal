# Frozen v1 product contract


**Product:** RailMate BD, an individual Android academic demonstrator. **Users:** passenger and optionally a restricted administrator for seed maintenance. **Source of truth:** teacher screenshot's 24 numbered requirements plus owner decisions. **Data:** only small synthetic railway and account test data. All ticket screens clearly state `DEMONSTRATION TICKET — NOT VALID FOR TRAVEL`.

### Booking story
A verified account selects origin, destination and departure date; results show sample trips and one-coach schematic. A single booking may contain 1–4 passengers and exactly one distinct seat assigned to each passenger. The passenger completes forms, reviews fare, presses `Simulate success` or `Simulate failure`, and receives an atomic booking and demonstration tickets only on success. Payment never requests real financial credentials. A server-side transaction serializes conflicting seat operations and maintains idempotency on retry. Cancellation is whole-booking only; confirmed seats are returned by one protected operation. An administrator never bypasses passenger privacy to publish information.

### Supporting module 1 — Journey Board
Tiny public or authenticated post list with text, optional photo, live comments, per-user like/dislike, per-user 1–5 rating, and cursor pagination (five per page). One user-supplied OpenRouter-key action rewrites the user's own text and requests confirmation before replacement. No private messages, followers, arbitrary URLs, ads or social graphs.

### Supporting module 2 — Station Guide
One small HTML page rendered through Flutter WebView containing a tested external YouTube embed, tested Google Maps embed, GSAP animation and CSS compiled from SASS. It is a real running page, not a placeholder. Maps iframe is minimum acceptable according to teacher wording; do not invent live GPS. Teacher approval of using an embedded page for GSAP/SASS must be logged before UI phase.

### ML in search
Bundled tiny TFLite model scores sample trip relevance using normalized departure proximity, transfer count (always 0 in v1), duration, remaining seats ratio and fare relative to a range. Update visible model score when criteria change. Label it `experimental ranking from demonstration data`; never claim observed commuter demand or real prediction accuracy. Training occurs in Colab/hosted CI and the model file is downloaded into the app's assets only after integrity check. A deterministic sort fallback is explicitly labeled non-ML; requirement #12 is PASSED only with true on-device model execution.

### Out of scope
Production tickets/payment/SMS provider sponsorship/live railway feed/GPS/seat holds/partial cancellation/payments/refunds/dynamic pricing/multi-coach administration/custom chat assistant/recommendation engine/enterprise analytics/local DB/Docker. Functional core must remain usable with no AI key. Internet is required for hosted Supabase features.

### Scope change
Only owner can modify this contract; record change impact in `DECISIONS.md` and all dependent tests. Course instructions supersede owner simplifications if the teacher insists. Any deleted required row becomes `BLOCKED_TEACHER_CLARIFICATION`, not silently removed.
