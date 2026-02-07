# app.py
import streamlit as st

# ── Page config ────────────────────────────────────────
st.set_page_config(
    page_title="Neon Horizon • Welcome",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS (neon + glassmorphism + gradient bg) ────
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@500;700;900&display=swap');

    :root {
        --bg: #0a0e17;
        --text: #e0e7ff;
        --primary: #7c3aed;
        --primary-dark: #5b21b6;
        --accent: #00f0ff;
        --gray: #64748b;
        --card: rgba(30, 41, 59, 0.65);
        --blur: blur(12px);
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: var(--bg);
        color: var(--text);
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    .stApp {
        background-image: 
            radial-gradient(circle at 15% 50%, rgba(124,58,237,0.14) 0%, transparent 28%),
            radial-gradient(circle at 85% 30%, rgba(0,240,255,0.11) 0%, transparent 38%);
        background-attachment: fixed;
    }

    /* Hide default Streamlit elements we don't want */
    header, footer {visibility: hidden;}
    #MainMenu, .stDeployButton {visibility: hidden !important;}

    .glow-text {
        font-family: 'Orbitron', monospace;
        font-size: 9rem;
        font-weight: 900;
        letter-spacing: -0.04em;
        background: linear-gradient(90deg, #c084fc, #a78bfa, #7c3aed, #00f0ff, #c084fc);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: shine 10s linear infinite;
        text-shadow: 0 0 80px rgba(124,58,237,0.6), 0 0 40px rgba(0,240,255,0.4);
        text-align: center;
        margin: 2rem 0 1rem;
        line-height: 0.9;
    }

    @keyframes shine {
        to { background-position: 200% center; }
    }

    .tagline {
        font-size: 1.6rem;
        max-width: 720px;
        margin: 0 auto 3rem;
        color: var(--gray);
        line-height: 1.5;
        font-weight: 300;
        text-align: center;
    }

    .btn-group {
        display: flex;
        gap: 1.5rem;
        justify-content: center;
        flex-wrap: wrap;
        margin: 2rem 0 5rem;
    }

    .btn {
        padding: 1rem 2.5rem;
        font-size: 1.15rem;
        font-weight: 600;
        border-radius: 50px;
        text-decoration: none;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        border: none;
        cursor: pointer;
    }

    .btn-primary {
        background: linear-gradient(45deg, var(--primary), #9f7aea);
        color: white;
        box-shadow: 0 12px 35px rgba(124,58,237,0.4);
    }

    .btn-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 25px 50px rgba(124,58,237,0.55);
    }

    .btn-outline {
        background: transparent;
        border: 2px solid var(--accent);
        color: var(--accent);
    }

    .btn-outline:hover {
        background: rgba(0,240,255,0.1);
        transform: translateY(-4px);
    }

    .features {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
        gap: 2.2rem;
        padding: 3rem 1rem 6rem;
        max-width: 1300px;
        margin: 0 auto;
    }

    .card {
        background: var(--card);
        backdrop-filter: var(--blur);
        -webkit-backdrop-filter: var(--blur);
        border: 1px solid rgba(124,58,237,0.2);
        border-radius: 1.3rem;
        padding: 2.4rem;
        transition: all 0.45s ease;
        color: #e2e8f0;
    }

    .card:hover {
        transform: translateY(-14px);
        border-color: rgba(124,58,237,0.5);
        box-shadow: 0 30px 70px rgba(0,0,0,0.45);
    }

    .card h3 {
        font-size: 1.7rem;
        margin-bottom: 1.1rem;
        color: var(--accent);
    }

    .footer {
        text-align: center;
        padding: 4rem 1rem 5rem;
        color: var(--gray);
        font-size: 0.95rem;
    }

    @media (max-width: 768px) {
        .glow-text { font-size: 5.5rem; }
        .tagline { font-size: 1.35rem; padding: 0 1rem; }
    }

    @media (max-width: 480px) {
        .glow-text { font-size: 4.2rem; }
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────
st.markdown('<h1 class="glow-text">NEON HORIZON</h1>', unsafe_allow_html=True)

st.markdown(
    """
    <p class="tagline">
        Where tomorrow’s ideas meet today’s ambition.<br>
        Fast. Beautiful. Unstoppable.
    </p>
    """,
    unsafe_allow_html=True
)

# Buttons (Streamlit buttons don't support :before pseudo-elements well → using markdown links)
st.markdown(
    """
    <div class="btn-group">
        <a href="#features" class="btn btn-primary">Explore Now</a>
        <a href="#" class="btn btn-outline">Watch Demo</a>
    </div>
    """,
    unsafe_allow_html=True
)

# ── Features ───────────────────────────────────────────
st.markdown('<div id="features"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>⚡ Lightning Fast</h3>
            <p>Sub-second load times, smooth interactions, and zero bloat — built for users who hate waiting.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>🌌 Cosmic Design</h3>
            <p>Neon gradients, glassmorphism, micro-animations — interfaces that feel like the future.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>🛠 Built to Scale</h3>
            <p>From landing page to full platform — architecture that grows with your vision.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ── Footer ─────────────────────────────────────────────
st.markdown(
    '<div class="footer">© 2026 Neon Horizon — Crafted with passion in the dark 🌙</div>',
    unsafe_allow_html=True
)
