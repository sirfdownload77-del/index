# app.py
import streamlit as st

# ── Page config ────────────────────────────────────────
st.set_page_config(
    page_title="Neon Horizon • Karachi Tech Horizon",
    page_icon="⚡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Cyber-futuristic CSS (2025–2026 trends) ────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@600;800;900&display=swap');

    :root {
        --bg: #05070f;
        --text: #e0f2ff;
        --neon-cyan: #00f5ff;
        --neon-magenta: #ff00d4;
        --neon-purple: #9d4edd;
        --card: rgba(15, 23, 42, 0.72);
        --blur: blur(18px);
        --radius: 1.5rem;
    }

    [data-testid="stAppViewContainer"] {
        background: var(--bg);
        background-image: 
            radial-gradient(circle at 8% 15%, rgba(0,245,255,0.22) 0%, transparent 35%),
            radial-gradient(circle at 92% 78%, rgba(157,78,221,0.18) 0%, transparent 42%),
            radial-gradient(circle at 50% 50%, rgba(255,0,212,0.08) 0%, transparent 60%);
        background-attachment: fixed;
        color: var(--text);
        font-family: 'Inter', system-ui, sans-serif;
    }

    header, #MainMenu, .stDeployButton, footer { visibility: hidden !important; }

    .hero-title {
        font-family: 'Orbitron', monospace;
        font-size: 9.5rem;
        font-weight: 900;
        letter-spacing: -0.07em;
        background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta), var(--neon-purple), var(--neon-cyan));
        background-size: 400% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: neon-flow 10s linear infinite;
        text-align: center;
        margin: 1.2rem 0 0.6rem;
        text-shadow: 0 0 90px rgba(0,245,255,0.6), 0 0 50px rgba(157,78,221,0.45);
    }

    @keyframes neon-flow {
        0%   { background-position: 0% center; }
        100% { background-position: 400% center; }
    }

    .hero-subtitle {
        font-size: 1.75rem;
        max-width: 820px;
        margin: 0 auto 3rem;
        color: #94a3b8;
        line-height: 1.4;
        font-weight: 300;
        text-align: center;
        letter-spacing: 0.5px;
    }

    .btn-group {
        text-align: center;
        margin: 2.8rem 0 6rem;
    }

    .futuristic-btn {
        display: inline-block;
        padding: 1.2rem 3rem;
        font-size: 1.22rem;
        font-weight: 600;
        border-radius: 999px;
        text-decoration: none;
        transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
        position: relative;
        overflow: hidden;
        margin: 0 1.1rem;
    }

    .btn-glow {
        background: linear-gradient(135deg, var(--neon-purple), var(--neon-magenta));
        color: white;
        box-shadow: 0 15px 45px rgba(157,78,221,0.5), inset 0 0 20px rgba(255,255,255,0.12);
    }

    .btn-glow:hover {
        transform: translateY(-6px) scale(1.04);
        box-shadow: 0 30px 80px rgba(157,78,221,0.7);
    }

    .btn-outline-glow {
        background: transparent;
        border: 2.5px solid var(--neon-cyan);
        color: var(--neon-cyan);
        box-shadow: 0 0 25px rgba(0,245,255,0.3);
    }

    .btn-outline-glow:hover {
        background: rgba(0,245,255,0.12);
        transform: translateY(-5px) scale(1.03);
        box-shadow: 0 0 45px rgba(0,245,255,0.55);
    }

    .features {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
        gap: 2.6rem;
        max-width: 1400px;
        margin: 0 auto 7rem;
        padding: 0 1.5rem;
    }

    .feature-card {
        background: var(--card);
        backdrop-filter: var(--blur);
        border: 1px solid rgba(0,245,255,0.28);
        border-radius: var(--radius);
        padding: 2.8rem 2.4rem;
        transition: all 0.5s ease;
        position: relative;
        overflow: hidden;
    }

    .feature-card::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, transparent, rgba(0,245,255,0.08), transparent);
        opacity: 0;
        transition: opacity 0.6s;
    }

    .feature-card:hover::before {
        opacity: 1;
    }

    .feature-card:hover {
        transform: translateY(-18px) scale(1.03);
        border-color: var(--neon-cyan);
        box-shadow: 0 40px 90px rgba(0,0,0,0.6), 0 0 60px rgba(0,245,255,0.35);
    }

    .feature-card h3 {
        font-size: 2rem;
        margin-bottom: 1.2rem;
        color: var(--neon-cyan);
        text-shadow: 0 0 20px rgba(0,245,255,0.5);
    }

    .feature-card p {
        color: #cbd5e1;
        line-height: 1.65;
    }

    .footer {
        text-align: center;
        padding: 6rem 1rem 7rem;
        color: #64748b;
        font-size: 1rem;
        border-top: 1px solid rgba(157,78,221,0.15);
    }

    @media (max-width: 1024px) {
        .hero-title { font-size: 7.2rem; }
        .hero-subtitle { font-size: 1.45rem; padding: 0 2rem; }
    }

    @media (max-width: 640px) {
        .hero-title { font-size: 5.4rem; }
        .futuristic-btn { padding: 1rem 2.4rem; font-size: 1.1rem; margin: 0.7rem; }
    }
</style>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────
st.markdown('<h1 class="hero-title">NEON HORIZON</h1>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero-subtitle">
        Karachi's window to tomorrow.<br>
        Innovation • Speed • Cyber Edge.
    </div>
    """,
    unsafe_allow_html=True
)

# Buttons
st.markdown("""
<div class="btn-group">
    <a href="#features" class="futuristic-btn btn-glow">Launch Now</a>
    <a href="#" class="futuristic-btn btn-outline-glow">Enter the Matrix</a>
</div>
""", unsafe_allow_html=True)

# ── Features ───────────────────────────────────────────
st.markdown('<div id="features" class="features">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡️ Hyper Speed</h3>
        <p>Instant load, buttery-smooth interactions, optimized for 5G & beyond — zero lag, pure adrenaline.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🌃 Cyber Aesthetic</h3>
        <p>Neon pulses, liquid glass, holographic depth — UI that feels hacked from 2049.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🛡️ Built for Scale</h3>
        <p>From Karachi startup MVP to global platform — architecture engineered to dominate.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer with local touch
st.markdown(
    '<div class="footer">© 2026 Neon Horizon — Forged in Karachi, Pakistan • Powered by vision & code ⚡️</div>',
    unsafe_allow_html=True
)
