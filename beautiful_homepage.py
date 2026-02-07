# app.py
import streamlit as st

# Page config
st.set_page_config(
    page_title="Neon Horizon • MUHAMMAD HASSAN",
    page_icon="⚡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Ultimate Cyberpunk CSS (2026 Karachi edition) ────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@700;900&display=swap');

    :root {
        --bg: #03050a;
        --text: #e8f5ff;
        --neon-cyan: #00ffff;
        --neon-magenta: #ff00ea;
        --neon-purple: #c066ff;
        --card: rgba(10, 15, 30, 0.78);
        --blur: blur(22px);
        --radius: 1.7rem;
    }

    [data-testid="stAppViewContainer"] {
        background: var(--bg);
        background-image: 
            radial-gradient(circle at 6% 12%, rgba(0,255,255,0.32) 0%, transparent 42%),
            radial-gradient(circle at 94% 82%, rgba(192,102,255,0.25) 0%, transparent 48%),
            radial-gradient(circle at 50% 55%, rgba(255,0,234,0.15) 0%, transparent 58%);
        background-attachment: fixed;
        color: var(--text);
        font-family: 'Inter', system-ui, sans-serif;
    }

    header, #MainMenu, .stDeployButton, footer { visibility: hidden !important; }

    .hero-title {
        font-family: 'Orbitron', monospace;
        font-size: 11rem;
        font-weight: 900;
        letter-spacing: -0.09em;
        background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta), var(--neon-purple), var(--neon-cyan));
        background-size: 600% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: pulse-flow 8s linear infinite;
        text-align: center;
        margin: 0.8rem 0 0.4rem;
        text-shadow: 0 0 140px rgba(0,255,255,0.8), 0 0 70px rgba(192,102,255,0.6);
    }

    @keyframes pulse-flow {
        0%   { background-position: 0% center; }
        50%  { background-position: 300% center; }
        100% { background-position: 600% center; }
    }

    .hero-subtitle {
        font-size: 1.95rem;
        max-width: 900px;
        margin: 0 auto 3.5rem;
        color: #99b3e0;
        line-height: 1.35;
        font-weight: 300;
        text-align: center;
        letter-spacing: 0.7px;
    }

    .btn-group {
        text-align: center;
        margin: 3.5rem 0 7rem;
    }

    .cyber-btn {
        display: inline-block;
        padding: 1.4rem 3.8rem;
        font-size: 1.32rem;
        font-weight: 700;
        border-radius: 999px;
        text-decoration: none;
        transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
        position: relative;
        overflow: hidden;
        margin: 0 1.4rem;
    }

    .btn-primary {
        background: linear-gradient(135deg, var(--neon-purple), var(--neon-magenta), var(--neon-cyan));
        background-size: 300% auto;
        color: white;
        box-shadow: 0 20px 60px rgba(192,102,255,0.6), inset 0 0 30px rgba(255,255,255,0.18);
        animation: glow-shift 7s linear infinite;
    }

    @keyframes glow-shift {
        0%   { background-position: 0% center; }
        100% { background-position: 300% center; }
    }

    .btn-primary:hover {
        transform: translateY(-8px) scale(1.06);
        box-shadow: 0 40px 110px rgba(192,102,255,0.9);
    }

    .btn-outline {
        background: transparent;
        border: 3.5px solid var(--neon-cyan);
        color: var(--neon-cyan);
        box-shadow: 0 0 40px rgba(0,255,255,0.5);
    }

    .btn-outline:hover {
        background: rgba(0,255,255,0.18);
        transform: translateY(-7px) scale(1.05);
        box-shadow: 0 0 80px rgba(0,255,255,0.85);
    }

    .features {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
        gap: 3rem;
        max-width: 1500px;
        margin: 0 auto 9rem;
        padding: 0 2.5rem;
    }

    .feature-card {
        background: var(--card);
        backdrop-filter: var(--blur);
        border: 2px solid rgba(0,255,255,0.35);
        border-radius: var(--radius);
        padding: 3.2rem 2.8rem;
        transition: all 0.6s ease;
        position: relative;
        overflow: hidden;
    }

    .feature-card::before {
        content: '';
        position: absolute;
        inset: -60%;
        background: conic-gradient(from 0deg, transparent, rgba(0,255,255,0.15), transparent 50%);
        opacity: 0;
        transition: opacity 1s;
        animation: spin 25s linear infinite;
    }

    @keyframes spin {
        100% { transform: rotate(360deg); }
    }

    .feature-card:hover::before {
        opacity: 0.8;
    }

    .feature-card:hover {
        transform: translateY(-22px) scale(1.05);
        border-color: var(--neon-cyan);
        box-shadow: 0 50px 120px rgba(0,0,0,0.7), 0 0 100px rgba(0,255,255,0.55);
    }

    .feature-card h3 {
        font-size: 2.3rem;
        margin-bottom: 1.4rem;
        color: var(--neon-cyan);
        text-shadow: 0 0 30px rgba(0,255,255,0.7);
    }

    .feature-card p {
        color: #d6e6ff;
        line-height: 1.75;
        font-size: 1.12rem;
    }

    .footer {
        text-align: center;
        padding: 8rem 1rem 9rem;
        color: #6b829e;
        font-size: 1.1rem;
        border-top: 1px solid rgba(192,102,255,0.2);
    }

    @media (max-width: 1200px) {
        .hero-title { font-size: 9rem; }
        .hero-subtitle { font-size: 1.65rem; padding: 0 3rem; }
    }

    @media (max-width: 768px) {
        .hero-title { font-size: 7rem; }
        .cyber-btn { padding: 1.2rem 3rem; font-size: 1.2rem; margin: 1rem 0.8rem; }
    }

    @media (max-width: 480px) {
        .hero-title { font-size: 5.5rem; }
    }
</style>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────
st.markdown('<h1 class="hero-title">NEON HORIZON</h1>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero-subtitle">
        MUHAMMAD HASSAN's cyber gateway from Karachi.<br>
        Where Sindh streets meet infinite digital neon — code runs faster here.
    </div>
    """,
    unsafe_allow_html=True
)

# Buttons
st.markdown("""
<div class="btn-group">
    <a href="#features" class="cyber-btn btn-primary">Enter My Grid</a>
    <a href="#" class="cyber-btn btn-outline">Scan the Signal</a>
</div>
""", unsafe_allow_html=True)

# ── Features ───────────────────────────────────────────
st.markdown('<div id="features" class="features">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡️ Hyper Karachi Pulse</h3>
        <p>Sub-50ms response, electric flow optimized for 5G/Starlink — born in the heat of Sindh, built to dominate globally.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🌌 Neon Sindh Matrix</h3>
        <p>Glass holograms + cyber outlines + Karachi night glow — UI that feels like hacking the future from Saddar to the stars.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🛡️ Eternal Scale Core</h3>
        <p>From solo dev project to planetary infrastructure — engineered to scale without limits, just like Karachi never sleeps.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer – personalized
st.markdown(
    '<div class="footer">© 2026 Neon Horizon • Created by MUHAMMAD HASSAN in Karachi, Sindh, Pakistan • Fueled by chai, code & cyber dreams ⚡️</div>',
    unsafe_allow_html=True
)
