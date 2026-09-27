# OPENCODE_RUNTIME_REPORT.md (2026-09-27) — partial, BLOCKED items noted
| Model | Provider | Free? | Verified ctx | Configured ctx | Output | Role | Tools? | Tested? | Status |
|---|---|---|---|---|---|---|---|---|---|
| agentrouter/deepseek-v4-flash | agentrouter | listed free, billing unverified | 1000000 | 256000 | 384000 | Coordinator | toolcall true | NOT TESTED (no route proof yet) | BLOCKED on auth/proof |
| opencode/mimo-v2.6-flash-free | opencode | yes | 200000 | 200000 | 32000 | Worker A | toolcall true | NOT TESTED | Model listed, session not launched |
| opencode/muse-spark-1.3-contributor-free | opencode | yes | 1048576 | 256000 | 131072 | Worker B | toolcall true | RESPONDING (this session) | PARTIAL — session works, resume/compaction test pending |

- Coordinator session ID: this session (Muse Spark) acting as setup coordinator; DeepSeek coordinator session TBD after route proof
- Worker A session ID: TBD
- Worker B session ID: TBD
- Compaction: NOT yet configured in opencode.jsonc (file is minimal schema-only + backup taken). Needs limit.context per model + auto-compaction + ACP conservative if present.
- Heavy lock: coordination/heavy.lock FREE.
- Verdict: BLOCKED (coordinator route unproven, worker sessions not launched/resumed, compaction not enabled, Flutter/gh/SDK missing).

## Route proof 2026-09-27 ~10:50
- opencode/mimo-v2.6-flash-free: PASS (tiny run returned ROUTE_OK).
- agentrouter/deepseek-v4-flash: FAILED x2 (default + --variant low) with provider error 'Invalid input: expected object, received null'. Coordinator stays on opencode free models until owner checks AgentRouter dashboard/docs.
- CI run 36294784667 on ae70e64: SUCCESS (artifact railmate-debug-apk). Prior run on fdd7a16: FAILURE (incomplete tree — superseded).

