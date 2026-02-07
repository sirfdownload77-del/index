# app.py
import streamlit as st

# ── Page config ────────────────────────────────────────
st.set_page_config(
    page_title="Neon Horizon • Karachi Cyber Frontier",
    page_icon="⚡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Enhanced Cyberpunk CSS (2026 vibe) ────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@700;900&display=swap');

    :root {
        --bg: #04060c;
        --text: #e5f0ff;
        --neon-cyan: #00faff;
        --neon-magenta: #ff00e1;
        --neon-purple: #b14aff;
        --card-bg: rgba(12, 18, 35, 0.75);
        --blur: blur(20px);
        --radius: 1.6rem;
    }

    [data-testid="stAppViewContainer"] {
        background: var(--bg);
        background-image: 
            radial-gradient(circle at 5% 10%, rgba(0,250,255,0.28) 0%, transparent 40%),
            radial-gradient(circle at 95% 85%, rgba(177,74,255,0.22) 0%, transparent 45%),
            radial-gradient(circle at 50% 60%, rgba(255,0,225,0.12) 0%, transparent 55%);
        background-attachment: fixed;
        color: var(--text);
        font-family: 'Inter', system-ui, sans-serif;
    }

    header, #MainMenu, .stDeployButton, footer { visibility: hidden !important; }

    .hero-title {
        font-family: 'Orbitron', monospace;
        font-size: 10.5rem;
        font-weight: 900;
        letter-spacing: -0.08em;
        background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta), var(--neon-purple), var(--neon-cyan));
        background-size: 500% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: cyber-flow 9s linear infinite;
        text-align: center;
        margin: 1rem 0 0.5rem;
        text-shadow: 0 0 120px rgba(0,250,255,0.7), 0 0 60px rgba(177,74,255,0.5);
    }

    @keyframes cyber-flow {
        0%   { background-position: 0% center; }
        100% { background-position: 500% center; }
    }

    .hero-subtitle {
        font-size: 1.85rem;
        max-width: 860px;
        margin: 0 auto 3.2rem;
        color: #a0b0d0;
        line-height: 1.38;
        font-weight: 300;
        text-align: center;
        letter-spacing: 0.6px;
    }

    .btn-group {
        text-align: center;
        margin: 3rem 0 6.5rem;
    }

    .cyber-btn {
        display: inline-block;
        padding: 1.3rem 3.4rem;
        font-size: 1.28rem;
        font-weight: 700;
        border-radius: 999px;
        text-decoration: none;
        transition: all 0.45s cubic-bezier(0.23, 1, 0.32, 1);
        position: relative;
        overflow: hidden;
        margin: 0 1.3rem;
    }

    .btn-primary {
        background: linear-gradient(135deg, var(--neon-purple), var(--neon-magenta), var(--neon-cyan));
        background-size: 200% auto;
        color: white;
        box-shadow: 0 18px 50px rgba(177,74,255,0.55), inset 0 0 25px rgba(255,255,255,0.15);
        animation: btn-shine 6s linear infinite;
    }

    @keyframes btn-shine {
        0%   { background-position: 0% center; }
        100% { background-position: 200% center; }
    }

    .btn-primary:hover {
        transform: translateY(-7px) scale(1.05);
        box-shadow: 0 35px 90px rgba(177,74,255,0.8);
    }

    .btn-outline {
        background: transparent;
        border: 3px solid var(--neon-cyan);
        color: var(--neon-cyan);
        box-shadow: 0 0 30px rgba(0,250,255,0.4);
    }

    .btn-outline:hover {
        background: rgba(0,250,255,0.15);
        transform: translateY(-6px) scale(1.04);
        box-shadow: 0 0 60px rgba(0,250,255,0.7);
    }

    .features {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 2.8rem;
        max-width: 1450px;
        margin: 0 auto 8rem;
        padding: 0 2rem;
    }

    .feature-card {
        background: var(--card-bg);
        backdrop-filter: var(--blur);
        border: 1.5px solid rgba(0,250,255,0.32);
        border-radius: var(--radius);
        padding: 3rem 2.6rem;
        transition: all 0.55s ease;
        position: relative;
        overflow: hidden;
    }

    .feature-card::before {
        content: '';
        position: absolute;
        inset: -50%;
        background: conic-gradient(from 0deg at 50% 50%, transparent, rgba(0,250,255,0.12), transparent 60%);
        opacity: 0;
        transition: opacity 0.8s;
        animation: rotate 20s linear infinite;
    }

    @keyframes rotate {
        100% { transform: rotate(360deg); }
    }

    .feature-card:hover::before {
        opacity: 1;
    }

    .feature-card:hover {
        transform: translateY(-20px) scale(1.04);
        border-color: var(--neon-cyan);
        box-shadow: 0 45px 100px rgba(0,0,0,0.65), 0 0 80px rgba(0,250,255,0.45);
    }

    .feature-card h3 {
        font-size: 2.15rem;
        margin-bottom: 1.3rem;
        color: var(--neon-cyan);
        text-shadow: 0 0 25px rgba(0,250,255,0.6);
    }

    .feature-card p {
        color: #d1e0ff;
        line-height: 1.7;
        font-size: 1.08rem;
    }

    .footer {
        text-align: center;
        padding: 7rem 1rem 8rem;
        color: #718096;
        font-size: 1.05rem;
        border-top: 1px solid rgba(177,74,255,0.18);
    }

    @media (max-width: 1100px) {
        .hero-title { font-size: 8rem; }
        .hero-subtitle { font-size: 1.55rem; padding: 0 2.5rem; }
    }

    @media (max-width: 680px) {
        .hero-title { font-size: 6rem; }
        .cyber-btn { padding: 1.1rem 2.6rem; font-size: 1.15rem; margin: 0.8rem; }
    }
</style>
""", unsafe_allow_html=True)

# ── Hero Section ──────────────────────────────────────────────────
st.markdown('<h1 class="hero-title">NEON HORIZON</h1>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero-subtitle">
        Karachi's gateway to the cyber frontier.<br>
        Where code meets neon dreams — fast, fearless, future-proof.
    </div>
    """,
    unsafe_allow_html=True
)

# Buttons
st.markdown("""
<div class="btn-group">
    <a href="#features" class="cyber-btn btn-primary">Enter the Grid</a>
    <a href="#" class="cyber-btn btn-outline">Decode the Signal</a>
</div>
""", unsafe_allow_html=True)

# ── Features ──────────────────────────────────────────────────────
st.markdown('<div id="features" class="features">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡️ Zero-Latency Core</h3>
        <p>Engineered for instant response — sub-100ms loads, GPU-accelerated animations, Karachi's fastest digital pulse.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🌌 Neon Matrix Design</h3>
        <p>Glass holograms, electric outlines, dynamic glows — interfaces ripped straight from a 2049 Karachi night.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🛡️ Infinite Scale Engine</h3>
        <p>From street-level MVP to planetary platform — built to handle millions without breaking a sweat.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    '<div class="footer">© 2026 Neon Horizon • Forged in Karachi, Sindh • Powered by code, caffeine & neon dreams ⚡️</div>',
    unsafe_allow_html=True
)
