# One embedded web page for web-specific requirements


Use `webview_flutter` to display a small app-packaged HTML/JS/CSS page (or bundled local assets copied into a supported WebView resource path, verified on Android). `styles.scss` is compiled by Dart-independent Sass CLI during CI/preparation; Flutter runtime loads CSS output only. GSAP animates a visible title/card; honor reduced-motion preference where available. YouTube embed uses a real permitted video and correct playback policies; Google Maps iframe displays a known station location. Do not request continuous location permission or build live train tracking.

Test the actual phone rather than assuming desktop iframe success proves Android WebView success. Android INTERNET permission and WebView network behavior must be accounted for. External embed can fail under policy/network; provide clear fallback link rather than pretend video/map played. Teacher acceptance of embedded WebView as meeting GSAP/SASS must be recorded as a separate approval gate. No third full frontend app, no Node server runtime and no additional repository are needed.
