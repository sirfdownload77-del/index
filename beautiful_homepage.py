# app.py
import streamlit as st

# ── Page config ────────────────────────────────────────
st.set_page_config(
    page_title="Neon Horizon • MUHAMMAD HASSAN",
    page_icon="⚡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Max Cyberpunk Karachi 2026 CSS ────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@700;900&display=swap');

    :root {
        --bg: #020408;
        --text: #f0faff;
        --neon-cyan: #00ffea;
        --neon-magenta: #ff00d9;
        --neon-purple: #d070ff;
        --card: rgba(8, 12, 25, 0.82);
        --blur: blur(24px);
        --radius: 1.8rem;
    }

    [data-testid="stAppViewContainer"] {
        background: var(--bg);
        background-image: 
            radial-gradient(circle at 4% 8%, rgba(0,255,234,0.35) 0%, transparent 45%),
            radial-gradient(circle at 96% 88%, rgba(208,112,255,0.28) 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, rgba(255,0,217,0.18) 0%, transparent 60%);
        background-attachment: fixed;
        color: var(--text);
        font-family: 'Inter', system-ui, sans-serif;
    }

    header, #MainMenu, .stDeployButton, footer { visibility: hidden !important; }

    .hero-title {
        font-family: 'Orbitron', monospace;
        font-size: 11.5rem;
        font-weight: 900;
        letter-spacing: -0.1em;
        background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta), var(--neon-purple), var(--neon-cyan));
        background-size: 700% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: hyper-flow 7s linear infinite;
        text-align: center;
        margin: 0.6rem 0 0.3rem;
        text-shadow: 0 0 160px rgba(0,255,234,0.85), 0 0 80px rgba(208,112,255,0.65);
    }

    @keyframes hyper-flow {
        0%   { background-position: 0% center; }
        100% { background-position: 700% center; }
    }

    .hero-subtitle {
        font-size: 2.05rem;
        max-width: 940px;
        margin: 0 auto 3.8rem;
        color: #96b8e8;
        line-height: 1.32;
        font-weight: 300;
        text-align: center;
        letter-spacing: 0.8px;
    }

    .btn-group {
        text-align: center;
        margin: 4rem 0 7.5rem;
    }

    .cyber-btn {
        display: inline-block;
        padding: 1.45rem 4rem;
        font-size: 1.35rem;
        font-weight: 700;
        border-radius: 999px;
        text-decoration: none;
        transition: all 0.55s cubic-bezier(0.22, 0.9, 0.36, 1.2);
        position: relative;
        overflow: hidden;
        margin: 0 1.5rem;
    }

    .btn-primary {
        background: linear-gradient(135deg, var(--neon-purple), var(--neon-magenta), var(--neon-cyan));
        background-size: 400% auto;
        color: white;
        box-shadow: 0 22px 70px rgba(208,112,255,0.65), inset 0 0 35px rgba(255,255,255,0.2);
        animation: shift-glow 6s linear infinite;
    }

    @keyframes shift-glow {
        0%   { background-position: 0% center; }
        100% { background-position: 400% center; }
    }

    .btn-primary:hover {
        transform: translateY(-9px) scale(1.07);
        box-shadow: 0 45px 130px rgba(208,112,255,1);
    }

    .btn-outline {
        background: transparent;
        border: 4px solid var(--neon-cyan);
        color: var(--neon-cyan);
        box-shadow: 0 0 50px rgba(0,255,234,0.6);
    }

    .btn-outline:hover {
        background: rgba(0,255,234,0.22);
        transform: translateY(-8px) scale(1.06);
        box-shadow: 0 0 100px rgba(0,255,234,0.95);
    }

    .features {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(440px, 1fr));
        gap: 3.2rem;
        max-width: 1550px;
        margin: 0 auto 10rem;
        padding: 0 3rem;
    }

    .feature-card {
        background: var(--card);
        backdrop-filter: var(--blur);
        border: 2.2px solid rgba(0,255,234,0.38);
        border-radius: var(--radius);
        padding: 3.4rem 3rem;
        transition: all 0.65s ease;
        position: relative;
        overflow: hidden;
    }

    .feature-card::before {
        content: '';
        position: absolute;
        inset: -70%;
        background: conic-gradient(from 0deg, transparent, rgba(0,255,234,0.18), transparent 40%);
        opacity: 0;
        transition: opacity 1.2s;
        animation: eternal-spin 30s linear infinite;
    }

    @keyframes eternal-spin {
        100% { transform: rotate(360deg); }
    }

    .feature-card:hover::before {
        opacity: 0.9;
    }

    .feature-card:hover {
        transform: translateY(-24px) scale(1.06);
        border-color: var(--neon-cyan);
        box-shadow: 0 55px 140px rgba(0,0,0,0.75), 0 0 120px rgba(0,255,234,0.65);
    }

    .feature-card h3 {
        font-size: 2.4rem;
        margin-bottom: 1.5rem;
        color: var(--neon-cyan);
        text-shadow: 0 0 35px rgba(0,255,234,0.8);
    }

    .feature-card p {
        color: #dbefff;
        line-height: 1.8;
        font-size: 1.15rem;
    }

    .footer {
        text-align: center;
        padding: 9rem 1rem 10rem;
        color: #6a88b5;
        font-size: 1.15rem;
        border-top: 1px solid rgba(208,112,255,0.22);
    }

    @media (max-width: 1300px) {
        .hero-title { font-size: 9.5rem; }
        .hero-subtitle { font-size: 1.75rem; padding: 0 3.5rem; }
    }

    @media (max-width: 800px) {
        .hero-title { font-size: 7.5rem; }
        .cyber-btn { padding: 1.3rem 3.2rem; font-size: 1.25rem; margin: 1.2rem 1rem; }
    }

    @media (max-width: 500px) {
        .hero-title { font-size: 6rem; }
    }
</style>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────
st.markdown('<h1 class="hero-title">NEON HORIZON</h1>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero-subtitle">
        MUHAMMAD HASSAN's digital frontier — Karachi born, cyber unstoppable.<br>
        From the streets of Sindh to the edge of tomorrow — code glows brighter here.
    </div>
    """,
    unsafe_allow_html=True
)

# Buttons
st.markdown("""
<div class="btn-group">
    <a href="#features" class="cyber-btn btn-primary">Enter the Horizon</a>
    <a href="#" class="cyber-btn btn-outline">Trace the Neon</a>
</div>
""", unsafe_allow_html=True)

# ── Features ───────────────────────────────────────────
st.markdown('<div id="features" class="features">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡️ Karachi Hypercore</h3>
        <p>Lightning execution — under 40ms loads, fluid motion, wired for Pakistan's fastest networks and beyond.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🌌 Sindh Neon Grid</h3>
        <p>Holographic glass, electric outlines, midnight Karachi rain glow — interfaces that pulse like the city at 3 AM.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🛡️ Infinite Karachi Engine</h3>
        <p>Scales from one dev to global empire — built tough like the spirit of Karachi, no limits, no downtime.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Personalized Footer
st.markdown(
    '<div class="footer">© 2026 Neon Horizon • Crafted by MUHAMMAD HASSAN • Karachi, Sindh, Pakistan • Neon dreams + endless code ⚡️</div>',
    unsafe_allow_html=True
)
