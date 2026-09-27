# Exact evidence grades and rejection rules


Evidence classes: `SOURCE` means code exists; `STATIC` means lint/typecheck executed; `UNIT-MOCK` means controlled fixtures passed; `INTEGRATION-STAGING` means the actual hosted staging database/Edge Function passed; `CI-BUILD` means hosted pipeline created artifact; `DEVICE` means installed Android app observed; `PROVIDER-LIVE` means actual user-authorized remote API call was verified. A weaker class cannot be silently promoted to a stronger one. A source file named `booking_test.dart` proves nothing if the test was not executed.

Each report must record date/time, task ID, repo name, commit before/after, exact executable command and exit code, essential output, source file paths, failing cases/limits, provider/mock distinction, device model/OS if applicable, screenshot or file hash and whether costs were incurred. Redact access tokens, emails, phone numbers, passenger data and model prompts. For backend migration, record project ref, migration ID, row counts, RLS tests and the approved apply step. For GitHub CI, record run URL and commit SHA; for APK, record build file path and SHA-256. Unknown is a valid honest state.
