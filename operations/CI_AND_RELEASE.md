# Cloud builds, one branch and Android proof


GitHub Actions on push to main and manual dispatch installs Flutter, runs `dart format --output=none --set-exit-if-changed .`, `flutter analyze`, `flutter test`, then builds a debug APK when source scaffolding exists. The job must not auto-commit, auto-push, create PRs or apply DB migrations. No Docker anywhere. Pin action versions after setup and audit permissions. App dependencies may need an ignored `app.env.json`; CI injects only project URL and **publishable** key using encrypted Actions secrets/variables, never service-role key. A public project URL can be present in shipped binaries; the secret-role key cannot.

A successful CI job is `CI-BUILD`, not `DEVICE`. Owner installs APK on physical Android, logs in using test identity, searches, books 2–4 seats, observes second-account conflict, completes mock payment, displays tickets, cancels and sees seats return, uses comments/ratings, invokes actual local model and BYOK only after consent, checks WebView/map/video. Record failure and retry path. Debug APK suffices for course unless teacher explicitly requests release AAB/Play Store; do not add signing/key management before needed.
