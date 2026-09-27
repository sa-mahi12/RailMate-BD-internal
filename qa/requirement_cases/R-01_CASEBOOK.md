# R-01 — ERD scalable PDF: planned exhaustive casebook

**Evidence state: NOT TESTED.** These are generated combinatorial test designs, not completed test results. Every case must be run or explicitly marked unselected/blocked; never bulk-mark PASS. They provide reproducible input/failure expectations and link to course row.

**Core acceptance:** ERD exported as PDF with all logical entities, cardinalities and relationships legible at 200% zoom.

| Area | Bound |
|---|---|
| Repository | Only main in code and documentation repos |
| Account | Use synthetic test identities and scoped JWTs |
| Source | Actual Flutter/Supabase/CI/Android as named, not fake provider |
| Evidence | Exact commit, dated command, result, screenshots and sanitized backend trace |

## Numbered test cases

### R-01-T001 — logical ERD after first schema freeze; 200% PDF zoom

**Precondition and scope.** Prepare a synthetic fixture representing logical ERD after first schema freeze. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger 200% PDF zoom through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing cardinality candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T002 — ERD after a forward-only migration; matching table names to migration

**Precondition and scope.** Prepare a synthetic fixture representing ERD after a forward-only migration. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger matching table names to migration through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: unreadable text candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T003 — ERD showing one-to-many booking passenger relation; checking required/nullable attributes

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing one-to-many booking passenger relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checking required/nullable attributes through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: obsolete table candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T004 — ERD showing dated trip seat relation; viewing all foreign keys

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing dated trip seat relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger viewing all foreign keys through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: broken connector candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T005 — ERD showing each community post relation; vector export at A3

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing each community post relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A3 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: image-only PDF candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T006 — ERD during teacher review; vector export at A4

**Precondition and scope.** Prepare a synthetic fixture representing ERD during teacher review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A4 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: schema mismatch candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T007 — logical ERD after first schema freeze; vector export at A4

**Precondition and scope.** Prepare a synthetic fixture representing logical ERD after first schema freeze. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A4 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing cardinality candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T008 — ERD after a forward-only migration; 200% PDF zoom

**Precondition and scope.** Prepare a synthetic fixture representing ERD after a forward-only migration. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger 200% PDF zoom through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: unreadable text candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T009 — ERD showing one-to-many booking passenger relation; matching table names to migration

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing one-to-many booking passenger relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger matching table names to migration through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: obsolete table candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T010 — ERD showing dated trip seat relation; checking required/nullable attributes

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing dated trip seat relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checking required/nullable attributes through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: broken connector candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T011 — ERD showing each community post relation; viewing all foreign keys

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing each community post relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger viewing all foreign keys through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: image-only PDF candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T012 — ERD during teacher review; vector export at A3

**Precondition and scope.** Prepare a synthetic fixture representing ERD during teacher review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A3 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing cardinality candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T013 — logical ERD after first schema freeze; vector export at A3

**Precondition and scope.** Prepare a synthetic fixture representing logical ERD after first schema freeze. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A3 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: unreadable text candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T014 — ERD after a forward-only migration; vector export at A4

**Precondition and scope.** Prepare a synthetic fixture representing ERD after a forward-only migration. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A4 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: obsolete table candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T015 — ERD showing one-to-many booking passenger relation; 200% PDF zoom

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing one-to-many booking passenger relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger 200% PDF zoom through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: broken connector candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T016 — ERD showing dated trip seat relation; matching table names to migration

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing dated trip seat relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger matching table names to migration through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: image-only PDF candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T017 — ERD showing each community post relation; checking required/nullable attributes

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing each community post relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checking required/nullable attributes through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: schema mismatch candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T018 — ERD during teacher review; viewing all foreign keys

**Precondition and scope.** Prepare a synthetic fixture representing ERD during teacher review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger viewing all foreign keys through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing cardinality candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T019 — logical ERD after first schema freeze; viewing all foreign keys

**Precondition and scope.** Prepare a synthetic fixture representing logical ERD after first schema freeze. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger viewing all foreign keys through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: unreadable text candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T020 — ERD after a forward-only migration; vector export at A3

**Precondition and scope.** Prepare a synthetic fixture representing ERD after a forward-only migration. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A3 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: obsolete table candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T021 — ERD showing one-to-many booking passenger relation; vector export at A4

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing one-to-many booking passenger relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A4 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: broken connector candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T022 — ERD showing dated trip seat relation; 200% PDF zoom

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing dated trip seat relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger 200% PDF zoom through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: image-only PDF candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T023 — ERD showing each community post relation; matching table names to migration

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing each community post relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is final teacher demonstration rehearsal; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger matching table names to migration through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing cardinality candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T024 — ERD during teacher review; checking required/nullable attributes

**Precondition and scope.** Prepare a synthetic fixture representing ERD during teacher review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is two-client observable run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checking required/nullable attributes through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: unreadable text candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T025 — logical ERD after first schema freeze; checking required/nullable attributes

**Precondition and scope.** Prepare a synthetic fixture representing logical ERD after first schema freeze. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is low-bandwidth phone run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checking required/nullable attributes through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: obsolete table candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T026 — ERD after a forward-only migration; viewing all foreign keys

**Precondition and scope.** Prepare a synthetic fixture representing ERD after a forward-only migration. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger viewing all foreign keys through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: broken connector candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T027 — ERD showing one-to-many booking passenger relation; vector export at A3

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing one-to-many booking passenger relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A3 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: image-only PDF candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T028 — ERD showing dated trip seat relation; vector export at A4

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing dated trip seat relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A4 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: schema mismatch candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T029 — ERD showing each community post relation; 200% PDF zoom

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing each community post relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is fresh hosted project staging run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger 200% PDF zoom through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing cardinality candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T030 — ERD during teacher review; matching table names to migration

**Precondition and scope.** Prepare a synthetic fixture representing ERD during teacher review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is repeated run after a clean app restart; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger matching table names to migration through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: unreadable text candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T031 — logical ERD after first schema freeze; matching table names to migration

**Precondition and scope.** Prepare a synthetic fixture representing logical ERD after first schema freeze. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is unauthorized second-user probe; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger matching table names to migration through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: obsolete table candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T032 — ERD after a forward-only migration; checking required/nullable attributes

**Precondition and scope.** Prepare a synthetic fixture representing ERD after a forward-only migration. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is replay using same request identity; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger checking required/nullable attributes through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: broken connector candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T033 — ERD showing one-to-many booking passenger relation; viewing all foreign keys

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing one-to-many booking passenger relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger viewing all foreign keys through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: image-only PDF candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T034 — ERD showing dated trip seat relation; vector export at A3

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing dated trip seat relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is signed-in owner run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A3 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: missing cardinality candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T035 — ERD showing each community post relation; vector export at A4

**Precondition and scope.** Prepare a synthetic fixture representing ERD showing each community post relation. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is device orientation and keyboard run; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger vector export at A4 through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: unreadable text candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.

### R-01-T036 — ERD during teacher review; 200% PDF zoom

**Precondition and scope.** Prepare a synthetic fixture representing ERD during teacher review. Select the appropriate fresh or existing authenticated account and preserve exact `main` commit SHA. The selected verification mode is first run on an empty test account; a browser mock may be useful for early debugging, but it is not a replacement for the real integration/device observation required by the row.

**Action and controlled variation.** Trigger 200% PDF zoom through the smallest real user-visible path. Verify the associated hosted state, network request or packaged asset before declaring an output. Add the deliberate fault variation: obsolete table candidate. Where a real provider, SMS or billing step is involved, obtain that specific authorization first; otherwise record BLOCKED and use fixtures only for unit-level diagnosis.

**Observable oracle.** Every attribute and cardinality shown in the PDF matches reviewed schema, remains selectable/sharp, and has no fabricated relationship. Check that the failure variation yields a specific, understandable state without corruption, duplicate side effects or stale user-facing success. Compare the before/after persisted values and the relevant counterpart client view. If operation is asynchronous, wait for the true authoritative completion rather than a fixed timer or optimistic label.

**Negative invariant and evidence.** Never mark ERD passed from an unrendered Mermaid source or raster screenshot alone. Open generated PDF in a viewer, zoom and compare named relation with approved SQL migration. Save the sanitized test input, exact source commit, actual command or interaction, observed output, time, affected requirement R-01, and evidence grade. A result cannot be promoted from `UNIT-MOCK` to `DEVICE`, `CI-BUILD`, `STAGING`, or `PROVIDER-LIVE` without separately executing that grade.

**Disposition.** Initial status `NOT TESTED`; if environment prevents execution, use `BLOCKED` with exact missing prerequisite. If the expected invariant fails, create a bounded worker repair packet, verify the correction, rerun this case and a nearby regression case. Only coordinator updates the authoritative private matrix after post-pass review.
