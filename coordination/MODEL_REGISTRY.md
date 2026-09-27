# MODEL_REGISTRY.md — verified 2026-09-27 via `opencode models --verbose`
Policy: configuredContext = min(256000, VERIFIED_REAL_CONTEXT_LIMIT). No fake 256K.

| Model | Provider | Free? | Verified context | Verified output | Configured context | Role | Notes |
|---|---|---|---|---|---|---|---|
| opencode/mimo-v2.6-flash-free | opencode (zen) | yes (cost 0) | 200000 | 32000 | 200000 | Worker A | REAL <256K → must NOT set 256K; checkpoint ~140K/soft, ~160K strong |
| opencode/muse-spark-1.3-contributor-free | opencode (zen) | yes (cost 0) | 1048576 | 131072 | 256000 (capped) | Worker B / current session | REAL 1M → cap 256K; checkpoint ~180K soft, ~195-200K strong |
| agentrouter/deepseek-v4-flash | agentrouter | listed cost 0, auth/billing unverified | 1000000 | 384000 | 256000 (capped) | Coordinator (preferred) | Route NOT proven; needs tiny non-project request + auth check; local 127.0.0.1:4000 unreachable (no local router service) |
| opencode/big-pickle | opencode | yes | 200000 | 32000 | 200000 if used | spare | not assigned |
| opencode/ling-3.0-flash-fin-free | opencode | yes | 262144 | 32768 | 256000 if used | spare | not assigned |

Exceptions: MiMo CANNOT be 256K. Any unknown-limit model → mark UNKNOWN, use safest catalogue number.
Source: `opencode models --verbose` on this machine, opencode 1.18.30.
