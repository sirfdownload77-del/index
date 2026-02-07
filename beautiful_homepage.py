# app.py
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Neon Horizon • Welcome",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Modern neon + glassmorphism CSS ────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@600;800;900&display=swap');

    :root {
        --bg: #0b0f1a;
        --text: #e2e8f0;
        --primary: #7c3aed;
        --accent: #00eaff;
        --card: rgba(30, 41, 59, 0.7);
        --blur: blur(16px);
        --radius: 1.4rem;
    }

    [data-testid="stAppViewContainer"] {
        background: var(--bg);
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(124,58,237,0.18) 0%, transparent 30%),
            radial-gradient(circle at 90% 80%, rgba(0,234,255,0.13) 0%, transparent 40%);
        background-attachment: fixed;
        color: var(--text);
        font-family: 'Inter', sans-serif;
    }

    /* Hide Streamlit branding & menu */
    header, #MainMenu, .stDeployButton, footer { visibility: hidden !important; }
    .st-emotion-cache-1r6slb0 { margin-bottom: 0 !important; }

    .main-title {
        font-family: 'Orbitron', monospace;
        font-size: 8.5rem;
        font-weight: 900;
        letter-spacing: -0.06em;
        background: linear-gradient(90deg, #a78bfa, #7c3aed, #00eaff, #a78bfa);
        background-size: 300% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: flow 12s linear infinite;
        text-align: center;
        margin: 1.5rem 0 0.8rem;
        text-shadow: 0 0 70px rgba(124,58,237,0.55);
    }

    @keyframes flow {
        0% { background-position: 0% center; }
        100% { background-position: 300% center; }
    }

    .subtitle {
        font-size: 1.65rem;
        max-width: 780px;
        margin: 0 auto 2.8rem;
        color: #94a3b8;
        line-height: 1.45;
        font-weight: 300;
        text-align: center;
    }

    .btn-container {
        text-align: center;
        margin: 2.5rem 0 5rem;
    }

    .custom-btn {
        display: inline-block;
        padding: 1.1rem 2.8rem;
        font-size: 1.18rem;
        font-weight: 600;
        border-radius: 999px;
        text-decoration: none;
        transition: all 0.38s ease;
        position: relative;
        overflow: hidden;
        margin: 0 0.9rem;
    }

    .btn-primary {
        background: linear-gradient(135deg, var(--primary), #9f7aea);
        color: white;
        box-shadow: 0 12px 40px rgba(124,58,237,0.42);
    }

    .btn-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 25px 60px rgba(124,58,237,0.6);
    }

    .btn-secondary {
        background: transparent;
        border: 2px solid var(--accent);
        color: var(--accent);
    }

    .btn-secondary:hover {
        background: rgba(0,234,255,0.08);
        transform: translateY(-4px);
    }

    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
        gap: 2.4rem;
        max-width: 1350px;
        margin: 0 auto 6rem;
        padding: 0 1rem;
    }

    .feature-card {
        background: var(--card);
        backdrop-filter: var(--blur);
        border: 1px solid rgba(124,58,237,0.22);
        border-radius: var(--radius);
        padding: 2.6rem 2.2rem;
        transition: all 0.45s ease;
        color: #e2e8f0;
    }

    .feature-card:hover {
        transform: translateY(-16px);
        border-color: rgba(124,58,237,0.55);
        box-shadow: 0 35px 80px rgba(0,0,0,0.5);
    }

    .feature-card h3 {
        font-size: 1.85rem;
        margin-bottom: 1rem;
        color: var(--accent);
    }

    .footer {
        text-align: center;
        padding: 5rem 1rem 6rem;
        color: #64748b;
        font-size: 0.98rem;
    }

    @media (max-width: 992px) {
        .main-title { font-size: 6.2rem; }
        .subtitle { font-size: 1.4rem; padding: 0 1.5rem; }
    }

    @media (max-width: 576px) {
        .main-title { font-size: 4.8rem; }
        .custom-btn { padding: 1rem 2.2rem; font-size: 1.05rem; margin: 0.6rem; }
    }
</style>
""", unsafe_allow_html=True)

# ── Hero Section ──────────────────────────────────────────────────
st.markdown('<h1 class="main-title">NEON HORIZON</h1>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="subtitle">
        Tomorrow's vision, built today.<br>
        Fast • Elegant • Limitless.
    </div>
    """,
    unsafe_allow_html=True
)

# Buttons
st.markdown("""
<div class="btn-container">
    <a href="#features" class="custom-btn btn-primary">Get Started</a>
    <a href="#" class="custom-btn btn-secondary">Learn More</a>
</div>
""", unsafe_allow_html=True)

# ── Features ──────────────────────────────────────────────────────
st.markdown('<div id="features" class="features-grid">', unsafe_allow_html=True)

cols = st.columns(3)

with cols[0]:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡ Instant Performance</h3>
        <p>Blazing-fast loading, fluid animations, optimized for every device — no compromises.</p>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
    <div class="feature-card">
        <h3>🌌 Future Aesthetic</h3>
        <p>Neon glows, glass effects, micro-interactions — design language from 2030, available now.</p>
    </div>
    """, unsafe_allow_html=True)

with cols[2]:
    st.markdown("""
    <div class="feature-card">
        <h3>🛠 Ready to Grow</h3>
        <p>Scalable foundation — from beautiful landing page to powerful full-stack application.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    '<div class="footer">© 2026 Neon Horizon — Made with vision & code in Karachi 🌙</div>',
    unsafe_allow_html=True
)
