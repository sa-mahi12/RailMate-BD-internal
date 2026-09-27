# R-15 — GSAP / Framer Motion: planned exhaustive casebook

**Evidence state: NOT TESTED.** These are generated combinatorial test designs, not completed test results. Every case must be run or explicitly marked unselected/blocked; never bulk-mark PASS. They provide reproducible input/failure expectations and link to course row.

**Core acceptance:** Visible entrance animation observed in embedded HTML page.

| Area | Bound |
|---|---|
| Repository | Only main in code and documentation repos |
| Account | Use synthetic test identities and scoped JWTs |
| Source | Actual Flutter/Supabase/CI/Android as named, not fake provider |
| Evidence | Exact commit, dated command, result, screenshots and sanitized backend trace |

## Numbered test cases

### R-15-T001 — Station Guide first open; title entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing Station Guide first open. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger title entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: GSAP script missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T002 — guide after returning from app; tap after animation

**Precondition and scope.** Prepare a synthetic fixture representing guide after returning from app. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap after animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: JS disabled. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T003 — reduced-motion enabled; interrupt animation

**Precondition and scope.** Prepare a synthetic fixture representing reduced-motion enabled. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger interrupt animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: layout shift. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T004 — small phone; scroll to animated section

**Precondition and scope.** Prepare a synthetic fixture representing small phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger scroll to animated section through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: reduced-motion preference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T005 — landscape phone; reopen page

**Precondition and scope.** Prepare a synthetic fixture representing landscape phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger reopen page through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: WebView reset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T006 — webpage network slow; card entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing webpage network slow. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger card entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: animation completes twice. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T007 — Station Guide first open; card entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing Station Guide first open. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger card entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: GSAP script missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T008 — guide after returning from app; title entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing guide after returning from app. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger title entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: JS disabled. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T009 — reduced-motion enabled; tap after animation

**Precondition and scope.** Prepare a synthetic fixture representing reduced-motion enabled. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap after animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: layout shift. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T010 — small phone; interrupt animation

**Precondition and scope.** Prepare a synthetic fixture representing small phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger interrupt animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: reduced-motion preference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T011 — landscape phone; scroll to animated section

**Precondition and scope.** Prepare a synthetic fixture representing landscape phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger scroll to animated section through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: WebView reset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T012 — webpage network slow; reopen page

**Precondition and scope.** Prepare a synthetic fixture representing webpage network slow. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger reopen page through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: GSAP script missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T013 — Station Guide first open; reopen page

**Precondition and scope.** Prepare a synthetic fixture representing Station Guide first open. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger reopen page through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: JS disabled. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T014 — guide after returning from app; card entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing guide after returning from app. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger card entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: layout shift. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T015 — reduced-motion enabled; title entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing reduced-motion enabled. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger title entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: reduced-motion preference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T016 — small phone; tap after animation

**Precondition and scope.** Prepare a synthetic fixture representing small phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap after animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: WebView reset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T017 — landscape phone; interrupt animation

**Precondition and scope.** Prepare a synthetic fixture representing landscape phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger interrupt animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: animation completes twice. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T018 — webpage network slow; scroll to animated section

**Precondition and scope.** Prepare a synthetic fixture representing webpage network slow. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger scroll to animated section through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: GSAP script missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T019 — Station Guide first open; scroll to animated section

**Precondition and scope.** Prepare a synthetic fixture representing Station Guide first open. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger scroll to animated section through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: JS disabled. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T020 — guide after returning from app; reopen page

**Precondition and scope.** Prepare a synthetic fixture representing guide after returning from app. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger reopen page through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: layout shift. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T021 — reduced-motion enabled; card entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing reduced-motion enabled. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger card entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: reduced-motion preference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T022 — small phone; title entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing small phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger title entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: WebView reset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T023 — landscape phone; tap after animation

**Precondition and scope.** Prepare a synthetic fixture representing landscape phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap after animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: GSAP script missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T024 — webpage network slow; interrupt animation

**Precondition and scope.** Prepare a synthetic fixture representing webpage network slow. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger interrupt animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: JS disabled. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T025 — Station Guide first open; interrupt animation

**Precondition and scope.** Prepare a synthetic fixture representing Station Guide first open. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger interrupt animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: layout shift. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T026 — guide after returning from app; scroll to animated section

**Precondition and scope.** Prepare a synthetic fixture representing guide after returning from app. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger scroll to animated section through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: reduced-motion preference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T027 — reduced-motion enabled; reopen page

**Precondition and scope.** Prepare a synthetic fixture representing reduced-motion enabled. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger reopen page through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: WebView reset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T028 — small phone; card entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing small phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger card entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: animation completes twice. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T029 — landscape phone; title entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing landscape phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger title entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: GSAP script missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T030 — webpage network slow; tap after animation

**Precondition and scope.** Prepare a synthetic fixture representing webpage network slow. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap after animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: JS disabled. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T031 — Station Guide first open; tap after animation

**Precondition and scope.** Prepare a synthetic fixture representing Station Guide first open. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap after animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: layout shift. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T032 — guide after returning from app; interrupt animation

**Precondition and scope.** Prepare a synthetic fixture representing guide after returning from app. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger interrupt animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: reduced-motion preference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T033 — reduced-motion enabled; scroll to animated section

**Precondition and scope.** Prepare a synthetic fixture representing reduced-motion enabled. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger scroll to animated section through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: WebView reset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T034 — small phone; reopen page

**Precondition and scope.** Prepare a synthetic fixture representing small phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger reopen page through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: GSAP script missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T035 — landscape phone; card entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing landscape phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger card entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: JS disabled. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-15-T036 — webpage network slow; title entrance animation

**Precondition and scope.** Prepare a synthetic fixture representing webpage network slow. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger title entrance animation through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: layout shift. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Visible GSAP-controlled animation runs while text remains readable and interactive; reduced-motion choice is respected where possible. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not call standard Flutter animation a GSAP demonstration. Show embedded page source imports and record on-device visible animation. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-15, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.
