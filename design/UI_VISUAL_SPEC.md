# UI_VISUAL_SPEC.md — binding visual reference (2026-09-27)
Source: `design/reference/` (10 images, 30 screens). Follow STRONGLY. Functional, never a static shell: every button navigates or acts on real state; loading/error/empty states required.

## Design tokens
- Primary deep teal: #0E5A66 (headers, primary buttons, selected states)
- Header: teal block with rounded bottom corners (~24px), white title, back chevron in translucent circle
- Accent green: #1E9E6A (success, verified, available-seat base is light blue-grey)
- Seats: Available #EAF0F6 bg + dark text; Selected teal fill white text; Booked orange #F2994A fill
- Star/price teal-dark; danger red #E5484D (cancel)
- Cards: white, radius 16, soft shadow, 16 padding; page bg #F4F7F9
- Primary button: teal, radius 12, white bold text, full-width with arrow
- BottomNav: Home, Bookings, Board, Profile; active teal, inactive grey
- Inputs: light border, radius 10, leading icon, hint grey

## Screen map (image -> screens)
- ref-1 (Home/Search/Seat): Home search card (From/Dhaka, To/Khulna, swap btn, date chips 09-13, Search Trains btn, Station Guide promo card); Search Results (route header card, date strip, train cards: name, BDT price, times, duration, 5 Chair); Select Seat (train header, legend, coach chips, grid A1-E5, Selected Seats bar, Continue btn)
- ref-2 (Welcome/Login/Register): Welcome hero + Log In/Create Account buttons + dots; Login (email/phone+password, remember, Google/Facebook buttons decorative-disabled with NOTED note, signup link); Register (full name, email, phone, username + Available check, password + hint)
- ref-3 (Verify/Profile/Passengers): OTP 6 boxes + resend timer + Verify + phone fallback btn; Complete Profile (avatar, name, email, phone, station dropdown); Passengers list + Add Passenger
- ref-4 (PassengerDetails/Review/Payment): stepper Passengers>Review>Payment; passenger tabs; fare breakdown (Base 2x700 + Service 40 = 1440); payment methods (Mobile Banking bKash/Nagad/Rocket selected, card, internet, other); Pay Now button
- ref-5 (Confirmation/E-Ticket/Actions): success check + BDR5F9K3 ref + copy icon; E-Ticket (VALID TICKET badge, route, passenger table, QR + ref); Ticket Actions (Download PDF, Share, Reminder, details)
- ref-6 (Bookings/Details/Cancel): My Bookings Upcoming/Past tabs + status pills; Booking Details + QR + Download/Share; Cancel flow (warning card, policy, Keep/Confirm, cancelled state + refund BDT 630 + RFN ref)
- ref-7 (Board/Details/Comments): Journey Board chips (All/Tips/Stations/Experiences) + post cards (avatar, Live badge, likes/dislikes/comments/stars); Post Details + Comments(5) newest-first + input bar; Comments page
- ref-8 (CreatePost/Photos/AIImprove): title 100 + description 1000 counters, category chips (Station Info/Travel Tips/Food/General), photo picker; Add Photos (5 max, reorder, caption); AI Improve (original draft card -> arrow -> suggestion card, Use This Version / Keep Original)
- ref-9 (StationGuide x3): Overview (hero photo, name + Bangla, fact chips, description, Quick Information rows); Map tab (embed); Video tab (player card, channel, highlights list)
- ref-10 (Profile/Settings/AISettings): Profile header (avatar, Verified/Premium pills, stats 12/5/3/4.8, menu rows); Settings (toggles, theme/language dropdowns, support rows); AI Settings (BYOK explainer, key field, Save, Connected Successfully banner, usage note, Test Connection)

## Rules
- Ticket artifacts must ALSO state DEMONSTRATION ONLY (small banner) per AGENTS.md — keep visual layout, add one-line banner.
- Google/Facebook buttons: render but disabled with 'coming soon' note (no fake auth).
- No real money: payment screen visual kept, simulated result.
- Bangla text in refs is decorative; keep same strings.
