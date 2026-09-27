# Stalls, lock leaks, compaction failures and CI recovery


When a worker has no tool progress for ten minutes or the CLI exits unexpectedly: do not spawn a replacement immediately. Capture PID, session ID, model, log tail, current task packet and git diff, then stop or resume same session. If memory is below 2 GiB, pause additional workers; below 1 GiB terminate off-critical workers and prevent builds. Check WSL swap and disk pressure, not just process count. Restart with one worker plus coordinator if a crash happened. Record worker output as partial, never PASSED.

Heavy lock is an atomic directory created only by coordinator; metadata contains PID, host and start timestamp. Release with trap and `rm -rf` only exact lock directory. A stale lock may be removed only after verifying no process owns it. On drvfs/Windows-mount, `rmdir` can fail due to auto-created `desktop.ini`; do not accidentally delete unrelated parent paths.

Compaction failure: open the private checkpoint, rehydrate owner decisions and current source, don't treat summary as authority. Push failure: verify remote branch and credential, retry same local commits without creating another branch. CI failure: inspect exact job and commit, ask assigned worker for targeted fix, do not skip tests to achieve green. Database migration failure: stop, inspect state, use forward-only correction rather than reapplying destructive scripts. OpenRouter key error: keep booking operational and show actionable error, never fall back to developer secret.
