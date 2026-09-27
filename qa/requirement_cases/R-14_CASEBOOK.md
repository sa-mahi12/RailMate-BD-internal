# R-14 — Datepicker: planned exhaustive casebook

**Evidence state: NOT TESTED.** These are generated combinatorial test designs, not completed test results. Every case must be run or explicitly marked unselected/blocked; never bulk-mark PASS. They provide reproducible input/failure expectations and link to course row.

**Core acceptance:** Picker selects date and invalid old dates are rejected.

| Area | Bound |
|---|---|
| Repository | Only main in code and documentation repos |
| Account | Use synthetic test identities and scoped JWTs |
| Source | Actual Flutter/Supabase/CI/Android as named, not fake provider |
| Evidence | Exact commit, dated command, result, screenshots and sanitized backend trace |

## Numbered test cases

### R-14-T001 — Home search; today

**Precondition and scope.** Prepare a synthetic fixture representing Home search. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger today through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: timezone offset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T002 — booking review; change date twice

**Precondition and scope.** Prepare a synthetic fixture representing booking review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger change date twice through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: cancel picker. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T003 — returning from result list; manual invalid date

**Precondition and scope.** Prepare a synthetic fixture representing returning from result list. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger manual invalid date through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: midnight rollover. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T004 — date at midnight boundary; yesterday

**Precondition and scope.** Prepare a synthetic fixture representing date at midnight boundary. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger yesterday through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: malformed date. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T005 — next seven days; last day allowed

**Precondition and scope.** Prepare a synthetic fixture representing next seven days. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger last day allowed through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: device clock difference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T006 — different Android locale; tomorrow

**Precondition and scope.** Prepare a synthetic fixture representing different Android locale. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tomorrow through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: rebuild UI. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T007 — Home search; tomorrow

**Precondition and scope.** Prepare a synthetic fixture representing Home search. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tomorrow through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: timezone offset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T008 — booking review; today

**Precondition and scope.** Prepare a synthetic fixture representing booking review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger today through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: cancel picker. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T009 — returning from result list; change date twice

**Precondition and scope.** Prepare a synthetic fixture representing returning from result list. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger change date twice through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: midnight rollover. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T010 — date at midnight boundary; manual invalid date

**Precondition and scope.** Prepare a synthetic fixture representing date at midnight boundary. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger manual invalid date through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: malformed date. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T011 — next seven days; yesterday

**Precondition and scope.** Prepare a synthetic fixture representing next seven days. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger yesterday through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: device clock difference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T012 — different Android locale; last day allowed

**Precondition and scope.** Prepare a synthetic fixture representing different Android locale. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger last day allowed through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: timezone offset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T013 — Home search; last day allowed

**Precondition and scope.** Prepare a synthetic fixture representing Home search. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger last day allowed through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: cancel picker. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T014 — booking review; tomorrow

**Precondition and scope.** Prepare a synthetic fixture representing booking review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tomorrow through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: midnight rollover. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T015 — returning from result list; today

**Precondition and scope.** Prepare a synthetic fixture representing returning from result list. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger today through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: malformed date. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T016 — date at midnight boundary; change date twice

**Precondition and scope.** Prepare a synthetic fixture representing date at midnight boundary. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger change date twice through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: device clock difference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T017 — next seven days; manual invalid date

**Precondition and scope.** Prepare a synthetic fixture representing next seven days. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger manual invalid date through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: rebuild UI. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T018 — different Android locale; yesterday

**Precondition and scope.** Prepare a synthetic fixture representing different Android locale. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger yesterday through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: timezone offset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T019 — Home search; yesterday

**Precondition and scope.** Prepare a synthetic fixture representing Home search. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger yesterday through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: cancel picker. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T020 — booking review; last day allowed

**Precondition and scope.** Prepare a synthetic fixture representing booking review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger last day allowed through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: midnight rollover. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T021 — returning from result list; tomorrow

**Precondition and scope.** Prepare a synthetic fixture representing returning from result list. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tomorrow through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: malformed date. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T022 — date at midnight boundary; today

**Precondition and scope.** Prepare a synthetic fixture representing date at midnight boundary. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger today through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: device clock difference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T023 — next seven days; change date twice

**Precondition and scope.** Prepare a synthetic fixture representing next seven days. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger change date twice through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: timezone offset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T024 — different Android locale; manual invalid date

**Precondition and scope.** Prepare a synthetic fixture representing different Android locale. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger manual invalid date through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: cancel picker. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T025 — Home search; manual invalid date

**Precondition and scope.** Prepare a synthetic fixture representing Home search. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger manual invalid date through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: midnight rollover. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T026 — booking review; yesterday

**Precondition and scope.** Prepare a synthetic fixture representing booking review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger yesterday through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: malformed date. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T027 — returning from result list; last day allowed

**Precondition and scope.** Prepare a synthetic fixture representing returning from result list. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger last day allowed through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: device clock difference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T028 — date at midnight boundary; tomorrow

**Precondition and scope.** Prepare a synthetic fixture representing date at midnight boundary. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tomorrow through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: rebuild UI. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T029 — next seven days; today

**Precondition and scope.** Prepare a synthetic fixture representing next seven days. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger today through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: timezone offset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T030 — different Android locale; change date twice

**Precondition and scope.** Prepare a synthetic fixture representing different Android locale. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger change date twice through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: cancel picker. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T031 — Home search; change date twice

**Precondition and scope.** Prepare a synthetic fixture representing Home search. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger change date twice through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: midnight rollover. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T032 — booking review; manual invalid date

**Precondition and scope.** Prepare a synthetic fixture representing booking review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger manual invalid date through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: malformed date. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T033 — returning from result list; yesterday

**Precondition and scope.** Prepare a synthetic fixture representing returning from result list. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger yesterday through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: device clock difference. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T034 — date at midnight boundary; last day allowed

**Precondition and scope.** Prepare a synthetic fixture representing date at midnight boundary. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger last day allowed through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: timezone offset. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T035 — next seven days; tomorrow

**Precondition and scope.** Prepare a synthetic fixture representing next seven days. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger tomorrow through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: cancel picker. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-14-T036 — different Android locale; today

**Precondition and scope.** Prepare a synthetic fixture representing different Android locale. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger today through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: midnight rollover. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Picker maps to intended local journey date and rejects disallowed dates without booking a past trip. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Do not silently reinterpret picked date as UTC previous day. Compare displayed date, query request date and hosted trip selection. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-14, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.
