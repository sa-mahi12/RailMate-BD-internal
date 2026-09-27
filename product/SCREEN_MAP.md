# Minimum screen map and UI states

Bottom navigation: Home, My Bookings, Journey Board, Profile. Home navigates to Train Results → Seat Selection → Passenger Details/Review → Simulated Payment → Confirmation/Ticket. Station Guide opens from Home as a separate route; profile owns OpenRouter key connect/remove, account details and logout. Login/register/verification form exists outside signed-in bottom tabs. One simple admin seed-maintenance page is optional only if the submitted proposal requires it; do not spend weeks building CRUD dashboards.

**Home:** origin, destination dropdown, date picker, search action, one upcoming journey summary. Invalid same-origin/destination and past date block query. Loading/empty/error/result states exist. Search displays seeded trips and small on-device ML relevance indicator only when model loaded; fallback sort is labelled.

**Results/Seat selection:** one coach graphic showing 12 seats per dated trip, selected 1–4, occupied disabled. Stale server availability must be revalidated by protected backend at booking. Passenger form dynamically renders N person rows, each explicitly mapped to one selected seat, no sensitive government ID for prototype. Review computes fare snapshot and shows demonstration-only notice. Payment screen has Simulate Success/Fail and request UUID; no real PIN/card fields. Confirmation displays stable booking reference and PDF/QR.

**My Bookings:** upcoming/previous, details and whole-booking cancellation; two accounts cannot open one another's passenger records. On uncertain backend response, query idempotency status rather than falsely tell user failure. Ticket remains labelled demo.

**Journey Board:** simple five-post feed with optional image, comment thread, like/dislike, 1–5 star rating and Load More; one Improve Wording button on the user's draft using their own OpenRouter key. No followers, private messages, social account import, content recommendations or unannounced features. Realtime updates should not cause duplicate counting; subscribe/unsubscribe with route lifecycle.

**Station Guide:** packaged HTML/WebView showing one map and one externally embedded YouTube video, GSAP animation and CSS compiled from SASS. Android back handles exiting WebView; link navigation to external providers is explicitly controlled. Offline failure shows clear links/messages.

**All screens:** loading, disabled action, validation, empty, retry, permission denied, stale session and offline state. Responsive phone layout; readable at 200% font scaling if possible. Don't burn time designing a complex motion system or separate web frontend.
