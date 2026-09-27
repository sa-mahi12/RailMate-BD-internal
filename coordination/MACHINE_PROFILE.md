# MACHINE_PROFILE.md — Windows native (2026-09-27)
# Observed via PowerShell, no tokens recorded.

- Windows: Windows 11 Pro 10.0.26100 Build 26100, HP EliteBook 840 G6, x64
- CPU: Intel i7-8665U 1.90GHz, 4 cores / 8 logical, MaxClock 2112MHz — usable
- RAM total: 16,190 MB (16,578,692 KB visible, 16,976,580,608 bytes)
- RAM free at check: ~7,752 MB (7,896,844 KB FreePhysicalMemory) — usable, 2-worker max
- Disk C free: ~169 GB, Disk D free: ~98.8 GB, D used: ~8.5 GB — usable
- PowerShell: 7.6.6 — usable
- git: C:\Program Files\Git\cmd\git.exe, 2.51.0.windows.1 — usable
- git identity global: sa-mahi12 / sanjidamahi2005@gmail.com — VERIFIED, do not change silently
- gh: MISSING — BLOCKER, action required: install via winget, then `gh auth login`, `gh auth status`
- flutter: MISSING — BLOCKER, action required: install Flutter SDK stable + Dart, then `flutter doctor -v`
- dart: MISSING (comes with Flutter) — BLOCKER with Flutter
- java: Oracle Java 24.0.2 (javapath) — usable, note: Android Gradle prefers JDK 17; verify via flutter doctor later
- node: v26.7.0 — usable
- npm: 11.19.0 — usable
- python: 3.13.14 — usable
- opencode: 1.18.30 at WinGet path — usable
- opencode config: %USERPROFILE%\.config\opencode\opencode.jsonc (minimal `{"$schema"...}`), backed up to opencode.jsonc.bak-20260927 — usable/not-configured
- supabase CLI: MISSING — not blocker yet (dashboard-first allowed), install later if migration workflow needs it
- adb/Android SDK: MISSING, ANDROID_HOME/ANDROID_SDK_ROOT unset, no LocalAndroid Sdk — BLOCKER for local build/device, mitigated by GitHub Actions CI for builds + physical phone via adb later
- VS Code: present (code.cmd) — usable
- Android Studio: not found at default path — verify, install only if Flutter doctor requires it
- USB: SAMSUNG Mobile USB Composite Device seen (status Unknown) — possible physical phone, verify with adb after SDK install
- AgentRouter: not yet verified as service; `opencode models` lists `agentrouter/*` catalogue (deepseek-v4-flash present) — needs auth/route proof in Prompt 2
- Admin rights: not tested; no install attempted yet. If Flutter/Android SDK install needs admin or reboot or large disk, STOP and ask owner.

## Actions required (owner approval before paid/billing/reboot steps)
1. Install `gh` + `flutter`/`dart` + Android SDK platform-tools/build-tools (owner approves disk/admin).
2. Do NOT install Docker, PostgreSQL, local Supabase.
3. Prefer physical phone via adb over emulator (RAM guardrail).

## Update 2026-09-27 ~10:30 (+06:00)
- gh 2.101 installed via winget; auth OK sa-mahi12 id 212235795 scopes gist/read:org/repo/workflow.
- Flutter 3.47.5 stable installed at D:\Apps\flutter (from Downloads zip 3.47.5, 1.9GB); Dart 3.13.4; User PATH updated.
- Android Studio 2026.1.4.7 installed via winget; SDK at %LOCALAPPDATA%\Android\Sdk (cmdline-tools latest + platform-tools + android-35/36 + build-tools 35/36/28.0.3); ANDROID_HOME set; licenses accepted; flutter doctor Android toolchain PASS (SDK 36.0.0).
- adb resolves to SDK platform-tools; WinGet PlatformTools duplicate left on disk (uninstall access-denied) but off PATH — cosmetic only.
- Visual Studio absent (Windows-desktop only, not needed for Android — accepted gap); cocoapods network check fails (iOS only — accepted gap).

