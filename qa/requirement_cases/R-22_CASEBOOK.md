# R-22 — Containerization or deployment pipeline: planned exhaustive casebook

**Evidence state: NOT TESTED.** These are generated combinatorial test designs, not completed test results. Every case must be run or explicitly marked unselected/blocked; never bulk-mark PASS. They provide reproducible input/failure expectations and link to course row.

**Core acceptance:** Hosted CI actually analyzes/tests/builds debug APK; Docker not needed.

| Area | Bound |
|---|---|
| Repository | Only main in code and documentation repos |
| Account | Use synthetic test identities and scoped JWTs |
| Source | Actual Flutter/Supabase/CI/Android as named, not fake provider |
| Evidence | Exact commit, dated command, result, screenshots and sanitized backend trace |

## Numbered test cases

### R-22-T001 — main push; checkout main

**Precondition and scope.** Prepare a synthetic fixture representing main push. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checkout main through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: dependency unavailable. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T002 — manual CI run; flutter build apk --debug

**Precondition and scope.** Prepare a synthetic fixture representing manual CI run. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter build apk --debug through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: format diff. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T003 — Flutter source absent initially; flutter test

**Precondition and scope.** Prepare a synthetic fixture representing Flutter source absent initially. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter test through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: test failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T004 — Flutter project after scaffold; flutter analyze

**Precondition and scope.** Prepare a synthetic fixture representing Flutter project after scaffold. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter analyze through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: Android build failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T005 — CI test failure; dart format check

**Precondition and scope.** Prepare a synthetic fixture representing CI test failure. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger dart format check through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: artifact missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T006 — debug APK artifact; flutter pub get

**Precondition and scope.** Prepare a synthetic fixture representing debug APK artifact. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter pub get through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: unexpected PR trigger. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T007 — main push; flutter pub get

**Precondition and scope.** Prepare a synthetic fixture representing main push. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter pub get through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: dependency unavailable. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T008 — manual CI run; checkout main

**Precondition and scope.** Prepare a synthetic fixture representing manual CI run. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checkout main through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: format diff. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T009 — Flutter source absent initially; flutter build apk --debug

**Precondition and scope.** Prepare a synthetic fixture representing Flutter source absent initially. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter build apk --debug through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: test failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T010 — Flutter project after scaffold; flutter test

**Precondition and scope.** Prepare a synthetic fixture representing Flutter project after scaffold. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter test through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: Android build failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T011 — CI test failure; flutter analyze

**Precondition and scope.** Prepare a synthetic fixture representing CI test failure. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter analyze through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: artifact missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T012 — debug APK artifact; dart format check

**Precondition and scope.** Prepare a synthetic fixture representing debug APK artifact. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger dart format check through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: dependency unavailable. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T013 — main push; dart format check

**Precondition and scope.** Prepare a synthetic fixture representing main push. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger dart format check through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: format diff. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T014 — manual CI run; flutter pub get

**Precondition and scope.** Prepare a synthetic fixture representing manual CI run. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter pub get through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: test failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T015 — Flutter source absent initially; checkout main

**Precondition and scope.** Prepare a synthetic fixture representing Flutter source absent initially. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checkout main through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: Android build failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T016 — Flutter project after scaffold; flutter build apk --debug

**Precondition and scope.** Prepare a synthetic fixture representing Flutter project after scaffold. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter build apk --debug through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: artifact missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T017 — CI test failure; flutter test

**Precondition and scope.** Prepare a synthetic fixture representing CI test failure. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter test through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: unexpected PR trigger. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T018 — debug APK artifact; flutter analyze

**Precondition and scope.** Prepare a synthetic fixture representing debug APK artifact. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter analyze through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: dependency unavailable. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T019 — main push; flutter analyze

**Precondition and scope.** Prepare a synthetic fixture representing main push. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter analyze through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: format diff. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T020 — manual CI run; dart format check

**Precondition and scope.** Prepare a synthetic fixture representing manual CI run. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger dart format check through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: test failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T021 — Flutter source absent initially; flutter pub get

**Precondition and scope.** Prepare a synthetic fixture representing Flutter source absent initially. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter pub get through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: Android build failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T022 — Flutter project after scaffold; checkout main

**Precondition and scope.** Prepare a synthetic fixture representing Flutter project after scaffold. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checkout main through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: artifact missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T023 — CI test failure; flutter build apk --debug

**Precondition and scope.** Prepare a synthetic fixture representing CI test failure. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter build apk --debug through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: dependency unavailable. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T024 — debug APK artifact; flutter test

**Precondition and scope.** Prepare a synthetic fixture representing debug APK artifact. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter test through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: format diff. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T025 — main push; flutter test

**Precondition and scope.** Prepare a synthetic fixture representing main push. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter test through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: test failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T026 — manual CI run; flutter analyze

**Precondition and scope.** Prepare a synthetic fixture representing manual CI run. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter analyze through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: Android build failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T027 — Flutter source absent initially; dart format check

**Precondition and scope.** Prepare a synthetic fixture representing Flutter source absent initially. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger dart format check through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: artifact missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T028 — Flutter project after scaffold; flutter pub get

**Precondition and scope.** Prepare a synthetic fixture representing Flutter project after scaffold. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter pub get through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: unexpected PR trigger. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T029 — CI test failure; checkout main

**Precondition and scope.** Prepare a synthetic fixture representing CI test failure. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checkout main through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: dependency unavailable. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T030 — debug APK artifact; flutter build apk --debug

**Precondition and scope.** Prepare a synthetic fixture representing debug APK artifact. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter build apk --debug through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: format diff. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T031 — main push; flutter build apk --debug

**Precondition and scope.** Prepare a synthetic fixture representing main push. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter build apk --debug through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: test failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T032 — manual CI run; flutter test

**Precondition and scope.** Prepare a synthetic fixture representing manual CI run. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter test through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: Android build failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T033 — Flutter source absent initially; flutter analyze

**Precondition and scope.** Prepare a synthetic fixture representing Flutter source absent initially. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter analyze through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: artifact missing. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T034 — Flutter project after scaffold; dart format check

**Precondition and scope.** Prepare a synthetic fixture representing Flutter project after scaffold. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger dart format check through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: dependency unavailable. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T035 — CI test failure; flutter pub get

**Precondition and scope.** Prepare a synthetic fixture representing CI test failure. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger flutter pub get through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: format diff. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-22-T036 — debug APK artifact; checkout main

**Precondition and scope.** Prepare a synthetic fixture representing debug APK artifact. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checkout main through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: test failure. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** GitHub-hosted pipeline runs actual checks and builds retrievable APK from same reviewed SHA without Docker/PR. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** A workflow YAML file or skipped scaffold job is not APK build evidence. Record Actions run URL, commit SHA, job statuses, artifact hash and archive contents. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-22, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.
