# Session roster — fill only with observed values
| Role | Actual session ID | Verified provider/model | Directory | Claimed paths | State | Last heartbeat |
|---|---|---|---|---|---|---|
| Coordinator | UNSET | AgentRouter DeepSeek variant UNVERIFIED | code checkout | integration/commit | NOT STARTED | — |
| Worker A | UNSET | `opencode/mimo-v2.6-flash-free` CANDIDATE | code checkout | assigned per packet | NOT STARTED | — |
| Worker B | UNSET | `opencode/muse-spark-1.3-contributor-free` CANDIDATE | code checkout | assigned per packet | NOT STARTED | — |
| Worker C optional | UNSET | one verified free model | code checkout | exclusive | DISABLED | — |

Do not claim a session is pinned to a model merely because a prompt says so. Record the actual OpenCode session ID and selected model from CLI/provider output. Confirm a real tool call, not just model listing. Model availability, free quotas and context can change. Check at each startup.
