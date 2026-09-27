"""R01: vector ERD PDF generated from the applied schema (no external renderer).

Reads nothing live; the table/column inventory below mirrors
supabase/migrations/20260927000001_initial_schema.sql as applied to the hosted
project (migrations 000001..000005, 00055200, 00062800, 00063000 all in sync).
Regenerate: python docs/erd/generate_erd_pdf.py  (needs fpdf2: pip install fpdf2)
Output: docs/erd/railmate.pdf (A4 landscape, vector text/lines — sharp at 200%+).
"""
from fpdf import FPDF

TABLES = [
    ("profiles", ["id uuid PK (FK auth.users, cascade)", "display_name text",
                  "created_at timestamptz"], []),
    ("usernames", ["username text PK [a-z0-9_]{3,20}", "user_id uuid FK>profiles UQ casc",
                   "created_at timestamptz"], ["profiles"]),
    ("stations", ["id uuid PK", "code text UQ (DAC/CGP/SYL/RJH)", "name text",
                  "latitude numeric(9,6)?", "longitude numeric(9,6)?"], []),
    ("trips", ["id uuid PK", "train_name text", "origin_station_id FK>stations",
               "destination_station_id FK>stations", "departure_at timestamptz",
               "arrival_at timestamptz (CHECK > dep)", "fare_bdt int (>=0)",
               "active bool (CHECK endpoints differ)"], ["stations"]),
    ("bookings", ["id uuid PK", "user_id FK>profiles", "trip_id FK>trips",
                  "request_id (UQ per user)", "request_fingerprint text",
                  "status CONFIRMED|CANCELLED", "total_fare_bdt int (>=0)",
                  "created_at / cancelled_at?"], ["profiles", "trips"]),
    ("trip_seats", ["id uuid PK", "trip_id FK>trips", "seat_code (UQ per trip)",
                    "booking_id FK>bookings NULL"], ["trips", "bookings"]),
    ("booking_passengers", ["id uuid PK", "booking_id FK>bookings casc",
                            "passenger_order 1..4", "passenger_name 2..80"],
     ["bookings"]),
    ("booking_seats", ["id uuid PK", "booking_id FK>bookings casc",
                       "trip_seat_id FK>trip_seats", "passenger_id FK>passengers"],
     ["bookings", "trip_seats", "booking_passengers"]),
    ("posts", ["id uuid PK", "user_id FK>profiles", "body 1..2000",
               "image_path? (post-media)", "created_at"], ["profiles"]),
    ("post_comments", ["id uuid PK", "post_id FK>posts casc", "user_id FK>profiles",
                       "body 1..500", "created_at"], ["posts", "profiles"]),
    ("post_reactions", ["post_id FK>posts casc PK", "user_id FK>profiles PK",
                        "reaction LIKE|DISLIKE", "created_at"],
     ["posts", "profiles"]),
    ("post_ratings", ["post_id FK>posts casc PK", "user_id FK>profiles PK",
                      "stars 1..5", "created_at"], ["posts", "profiles"]),
]

# (name) -> (col, row) on a 4-col x 3-row grid
POS = {
    "profiles": (0, 0), "usernames": (0, 1), "stations": (1, 0), "trips": (1, 1),
    "bookings": (2, 0), "trip_seats": (2, 1), "booking_passengers": (3, 0),
    "booking_seats": (3, 1), "posts": (0, 2), "post_comments": (1, 2),
    "post_reactions": (2, 2), "post_ratings": (3, 2),
}

EDGES = [  # (child, parent, label)
    ("usernames", "profiles", "1:1"), ("bookings", "profiles", "N:1"),
    ("bookings", "trips", "N:1"), ("trips", "stations", "N:1 x2"),
    ("trip_seats", "trips", "N:1"), ("trip_seats", "bookings", "N:1?"),
    ("booking_passengers", "bookings", "N:1 casc"),
    ("booking_seats", "bookings", "N:1 casc"),
    ("booking_seats", "trip_seats", "N:1"),
    ("booking_seats", "booking_passengers", "N:1"),
    ("posts", "profiles", "N:1"), ("post_comments", "posts", "N:1 casc"),
    ("post_comments", "profiles", "N:1"), ("post_reactions", "posts", "N:1"),
    ("post_ratings", "posts", "N:1"),
]

W, H = 297, 210  # A4 landscape mm
COLW, ROWH = W / 4, (H - 18) / 3


def box_center(name):
    c, r = POS[name]
    return (c * COLW + COLW / 2, 10 + r * ROWH + ROWH / 2)


def main():
    pdf = FPDF(orientation="L", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(W, 8, "RailMate BD - Entity Relationship Diagram (applied schema, 2026-09-27)",
             align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 7)
    pdf.cell(
        W, 4,
        "public schema, hosted Supabase (12 tables). PK=primary key, FK>table=foreign key, "
        "UQ=unique, casc=on delete cascade, ?=nullable. DEMONSTRATION ONLY.",
        align="C", new_x="LMARGIN", new_y="NEXT")

    centers = {name: box_center(name) for name, _, _ in TABLES}
    # edges first (under boxes)
    pdf.set_draw_color(14, 90, 102)
    pdf.set_font("Helvetica", "", 5.5)
    for child, parent, label in EDGES:
        x1, y1 = centers[child]
        x2, y2 = centers[parent]
        pdf.line(x1, y1, x2, y2)
        pdf.set_xy((x1 + x2) / 2 - 8, (y1 + y2) / 2 - 3)
        pdf.cell(16, 3, label, align="C")

    pdf.set_fill_color(244, 247, 249)
    for name, cols, _ in TABLES:
        cx, cy = centers[name]
        bw, bh = COLW - 6, ROWH - 6
        x, y = cx - bw / 2, cy - bh / 2
        pdf.set_draw_color(14, 90, 102)
        pdf.rect(x, y, bw, bh, style="DF")
        pdf.set_xy(x, y + 1)
        pdf.set_font("Helvetica", "B", 8)
        pdf.cell(bw, 4, name, align="C")
        pdf.set_font("Helvetica", "", 5.5)
        pdf.set_xy(x + 1.5, y + 5.5)
        for col in cols:
            pdf.set_x(x + 1.5)
            pdf.cell(bw - 3, 2.6, "- " + col, new_x="LMARGIN", new_y="NEXT")

    pdf.output("docs/erd/railmate.pdf")
    print("wrote docs/erd/railmate.pdf")


if __name__ == "__main__":
    main()
