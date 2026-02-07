# app.py
import streamlit as st

# ────────────────────────────────────────────────
#   EDIT YOUR CARDS HERE — very simple list of dicts
# ────────────────────────────────────────────────
cards = [
    {"emoji": "1️⃣", "title": "Fast Start",     "text": "Launch your app in minutes with zero frontend hassle."},
    {"emoji": "2️⃣", "title": "Beautiful UI",   "text": "Modern cards, clean typography, automatic responsiveness."},
    {"emoji": "3️⃣", "title": "Easy Updates",   "text": "Change content in this list — app updates instantly."},
    {"emoji": "4️⃣", "title": "Data Display",   "text": "Perfect for metrics, features, team members or products."},
    {"emoji": "5️⃣", "title": "Dark Mode",      "text": "Streamlit handles light/dark mode automatically."},
    {"emoji": "6️⃣", "title": "Interactive",    "text": "Add buttons, sliders, charts — anything Streamlit offers."},
    {"emoji": "7️⃣", "title": "Free Hosting",   "text": "Deploy to Streamlit Community Cloud in one click."},
    {"emoji": "8️⃣", "title": "Custom Images",  "text": "Replace emoji with real photos very easily."},
    {"emoji": "9️⃣", "title": "Flexible Grid",  "text": "4–3–2–1 columns depending on your screen size."},
    {"emoji": "🔟",  "title": "No JS Needed",   "text": "Pure Python — no JavaScript or CSS required."},
    {"emoji": "11",  "title": "Community",      "text": "Huge gallery of components & helpful forum."},
    {"emoji": "12",  "title": "Get Started",    "text": "Just `pip install streamlit` and run this file!"},
]

# ────────────────────────────────────────────────
#   Styling (you can tweak or remove)
# ────────────────────────────────────────────────
st.markdown("""
    <style>
        .card {
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            padding: 1.4rem;
            text-align: center;
            height: 100%;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 12px 24px rgba(0,0,0,0.12);
        }
        .emoji {
            font-size: 3.2rem;
            margin-bottom: 0.8rem;
        }
        .card h3 {
            margin: 0.6rem 0;
            font-size: 1.35rem;
            color: #1e293b;
        }
        .card p {
            color: #64748b;
            font-size: 1rem;
            line-height: 1.5;
            margin: 0;
        }
        /* Dark mode adjustments */
        @media (prefers-color-scheme: dark) {
            .card {
                background: #1e293b;
            }
            .card h3 { color: #f1f5f9; }
            .card p   { color: #94a3b8; }
        }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
#   Page layout
# ────────────────────────────────────────────────
st.title("12 Feature Cards – Streamlit Edition")
st.markdown("Edit the `cards` list above and watch your app update live!")

# Create 4 columns (good responsive base: 4→3→2→1 on narrow screens)
cols = st.columns(4, gap="medium", vertical_alignment="center")

for i, card in enumerate(cards):
    # Cycle through columns
    with cols[i % 4]:
        with st.container():
            st.markdown(f"""
            <div class="card">
                <div class="emoji">{card.get('emoji', '⭐')}</div>
                <h3>{card.get('title', 'Card Title')}</h3>
                <p>{card.get('text', 'Card description goes here...')}</p>
            </div>
            """, unsafe_allow_html=True)

# Optional footer
st.markdown("---")
st.caption("Made with ❤️ in Peshawar • Deploy to streamlit.app by pushing to GitHub")
