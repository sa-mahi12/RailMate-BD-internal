# R-21 — Modern frontend: planned exhaustive casebook

**Evidence state: NOT TESTED.** These are generated combinatorial test designs, not completed test results. Every case must be run or explicitly marked unselected/blocked; never bulk-mark PASS. They provide reproducible input/failure expectations and link to course row.

**Core acceptance:** Native app launches on phone and relevant screens respond.

| Area | Bound |
|---|---|
| Repository | Only main in code and documentation repos |
| Account | Use synthetic test identities and scoped JWTs |
| Source | Actual Flutter/Supabase/CI/Android as named, not fake provider |
| Evidence | Exact commit, dated command, result, screenshots and sanitized backend trace |

## Numbered test cases

### R-21-T001 — cold app launch; tap Home

**Precondition and scope.** Prepare a synthetic fixture representing cold app launch. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Home through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing route. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T002 — small physical phone; return from Station Guide

**Precondition and scope.** Prepare a synthetic fixture representing small physical phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger return from Station Guide through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: widget exception. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T003 — large text setting; select seat

**Precondition and scope.** Prepare a synthetic fixture representing large text setting. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger select seat through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: poor tap target. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T004 — sign-in transition; open Profile

**Precondition and scope.** Prepare a synthetic fixture representing sign-in transition. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Profile through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: state lost. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T005 — booking navigation; open Journey Board

**Precondition and scope.** Prepare a synthetic fixture representing booking navigation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Journey Board through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: back-stack loop. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T006 — background-foreground restore; tap Bookings

**Precondition and scope.** Prepare a synthetic fixture representing background-foreground restore. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Bookings through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: slow initial frame. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T007 — cold app launch; tap Bookings

**Precondition and scope.** Prepare a synthetic fixture representing cold app launch. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Bookings through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing route. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T008 — small physical phone; tap Home

**Precondition and scope.** Prepare a synthetic fixture representing small physical phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Home through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: widget exception. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T009 — large text setting; return from Station Guide

**Precondition and scope.** Prepare a synthetic fixture representing large text setting. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger return from Station Guide through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: poor tap target. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T010 — sign-in transition; select seat

**Precondition and scope.** Prepare a synthetic fixture representing sign-in transition. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger select seat through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: state lost. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T011 — booking navigation; open Profile

**Precondition and scope.** Prepare a synthetic fixture representing booking navigation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Profile through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: back-stack loop. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T012 — background-foreground restore; open Journey Board

**Precondition and scope.** Prepare a synthetic fixture representing background-foreground restore. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Journey Board through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing route. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T013 — cold app launch; open Journey Board

**Precondition and scope.** Prepare a synthetic fixture representing cold app launch. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Journey Board through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: widget exception. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T014 — small physical phone; tap Bookings

**Precondition and scope.** Prepare a synthetic fixture representing small physical phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Bookings through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: poor tap target. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T015 — large text setting; tap Home

**Precondition and scope.** Prepare a synthetic fixture representing large text setting. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Home through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: state lost. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T016 — sign-in transition; return from Station Guide

**Precondition and scope.** Prepare a synthetic fixture representing sign-in transition. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger return from Station Guide through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: back-stack loop. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T017 — booking navigation; select seat

**Precondition and scope.** Prepare a synthetic fixture representing booking navigation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger select seat through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: slow initial frame. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T018 — background-foreground restore; open Profile

**Precondition and scope.** Prepare a synthetic fixture representing background-foreground restore. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Profile through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing route. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T019 — cold app launch; open Profile

**Precondition and scope.** Prepare a synthetic fixture representing cold app launch. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Profile through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: widget exception. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T020 — small physical phone; open Journey Board

**Precondition and scope.** Prepare a synthetic fixture representing small physical phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Journey Board through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: poor tap target. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T021 — large text setting; tap Bookings

**Precondition and scope.** Prepare a synthetic fixture representing large text setting. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Bookings through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: state lost. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T022 — sign-in transition; tap Home

**Precondition and scope.** Prepare a synthetic fixture representing sign-in transition. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Home through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: back-stack loop. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T023 — booking navigation; return from Station Guide

**Precondition and scope.** Prepare a synthetic fixture representing booking navigation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger return from Station Guide through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing route. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T024 — background-foreground restore; select seat

**Precondition and scope.** Prepare a synthetic fixture representing background-foreground restore. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger select seat through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: widget exception. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T025 — cold app launch; select seat

**Precondition and scope.** Prepare a synthetic fixture representing cold app launch. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger select seat through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: poor tap target. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T026 — small physical phone; open Profile

**Precondition and scope.** Prepare a synthetic fixture representing small physical phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Profile through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: state lost. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T027 — large text setting; open Journey Board

**Precondition and scope.** Prepare a synthetic fixture representing large text setting. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Journey Board through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: back-stack loop. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T028 — sign-in transition; tap Bookings

**Precondition and scope.** Prepare a synthetic fixture representing sign-in transition. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Bookings through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: slow initial frame. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T029 — booking navigation; tap Home

**Precondition and scope.** Prepare a synthetic fixture representing booking navigation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Home through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing route. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T030 — background-foreground restore; return from Station Guide

**Precondition and scope.** Prepare a synthetic fixture representing background-foreground restore. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger return from Station Guide through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: widget exception. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T031 — cold app launch; return from Station Guide

**Precondition and scope.** Prepare a synthetic fixture representing cold app launch. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger return from Station Guide through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: poor tap target. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T032 — small physical phone; select seat

**Precondition and scope.** Prepare a synthetic fixture representing small physical phone. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger select seat through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: state lost. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T033 — large text setting; open Profile

**Precondition and scope.** Prepare a synthetic fixture representing large text setting. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Profile through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: back-stack loop. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T034 — sign-in transition; open Journey Board

**Precondition and scope.** Prepare a synthetic fixture representing sign-in transition. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger open Journey Board through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing route. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T035 — booking navigation; tap Bookings

**Precondition and scope.** Prepare a synthetic fixture representing booking navigation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Bookings through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: widget exception. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-21-T036 — background-foreground restore; tap Home

**Precondition and scope.** Prepare a synthetic fixture representing background-foreground restore. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tap Home through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: poor tap target. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Actual Flutter Android application launches, renders and navigates with usable layout and no fatal errors. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A Figma mock, screenshot or unbuilt Dart source is not a launched frontend. Record installed APK hash, device model/OS and on-phone walkthrough. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-21, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.
