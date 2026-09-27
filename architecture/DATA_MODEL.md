# Hosted Postgres schema and ERD decisions


Normalized logical entities: `profiles` (PK auth user), `usernames` (normalized PK), `stations`, `trips`, `trip_seats`, `bookings` (owner, trip, idempotency, status), `booking_passengers`, `booking_seats`, `posts`, `post_comments`, `post_reactions`, `post_ratings`. `trip_seats` is date-specific; never store a global train seat status. A booking has N passengers and N distinct seats (N=1..4). Fare snapshot prevents old ticket recalculations after admin changes. Use database constraints and unique keys rather than solely client validation.

ERD submission can be generated from `erd/railmate.mmd`; export scalable PDF via Mermaid CLI on GitHub Actions or another installed rendering tool. Do not call the source itself the submitted PDF. The static diagrams must identify relationships/cardinalities and be legible at 200% zoom. SQL/migration is the database source of truth; ERD must reconcile with live applied schema and the right migration hash.

Index and scalability: `trips(origin_station_id,destination_station_id,departure_at)`, `bookings(user_id,created_at)`, comments `(post_id,created_at,id)`, reactions unique `(post_id,user_id)`, ratings unique `(post_id,user_id)`, seat `(trip_id,seat_code)` unique. Limit pagination to 5–10 and order deterministically. For realtime aggregate counts, prefer server-maintained counters or a bounded aggregate query followed by Realtime updates; do not write aggregate counts from a public client without a trusted transaction.

Privacy: Synthetic sample names/phones. The user's profile can never SELECT another person's booking passenger rows; direct insert/update to booking seats must be denied. Only protected server operation can book/release. Delete requests need referential and media cleanup policy; do not use CASCADE in a live project without impact analysis. Database records are not a substitute for Storage byte backups.
