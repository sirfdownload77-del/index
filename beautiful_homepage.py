# beautiful_homepage.py
from pathlib import Path

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Neon Horizon • Welcome</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@500;700;900&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg: #0a0e17;
      --text: #e0e7ff;
      --primary: #7c3aed;
      --primary-dark: #5b21b6;
      --accent: #00f0ff;
      --gray: #64748b;
      --card: rgba(30, 41, 59, 0.6);
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Inter', system-ui, sans-serif;
      min-height: 100vh;
      background-image: 
        radial-gradient(circle at 15% 50%, rgba(124,58,237,0.12) 0%, transparent 25%),
        radial-gradient(circle at 85% 30%, rgba(0,240,255,0.09) 0%, transparent 35%);
      overflow-x: hidden;
    }

    .container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 5vw;
    }

    header {
      padding: 5rem 0 10rem;
      text-align: center;
      position: relative;
    }

    .glow-text {
      font-family: 'Orbitron', monospace;
      font-size: clamp(3.5rem, 12vw, 11rem);
      font-weight: 900;
      letter-spacing: -0.04em;
      background: linear-gradient(90deg, #c084fc, #a78bfa, #7c3aed, #00f0ff, #c084fc);
      background-size: 200% auto;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: shine 8s linear infinite;
      text-shadow: 0 0 60px rgba(124,58,237,0.5);
    }

    @keyframes shine {
      to { background-position: 200% center; }
    }

    .tagline {
      font-size: 1.5rem;
      max-width: 680px;
      margin: 1.8rem auto 3rem;
      color: var(--gray);
      line-height: 1.6;
      font-weight: 300;
    }

    .btn-group {
      display: flex;
      gap: 1.5rem;
      justify-content: center;
      flex-wrap: wrap;
    }

    .btn {
      padding: 1rem 2.4rem;
      font-size: 1.1rem;
      font-weight: 600;
      border-radius: 50px;
      text-decoration: none;
      transition: all 0.35s ease;
      position: relative;
      overflow: hidden;
    }

    .btn-primary {
      background: linear-gradient(45deg, var(--primary), #9f7aea);
      color: white;
      box-shadow: 0 10px 30px rgba(124,58,237,0.35);
    }

    .btn-primary:hover {
      transform: translateY(-4px);
      box-shadow: 0 20px 40px rgba(124,58,237,0.5);
    }

    .btn-outline {
      border: 2px solid var(--accent);
      color: var(--accent);
      background: transparent;
    }

    .btn-outline:hover {
      background: rgba(0,240,255,0.08);
      transform: translateY(-3px);
    }

    .btn::before {
      content: '';
      position: absolute;
      top: 0; left: -100%;
      width: 100%; height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent);
      transition: 0.7s;
    }

    .btn:hover::before {
      left: 100%;
    }

    .features {
      padding: 6rem 0;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 2.5rem;
    }

    .card {
      background: var(--card);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(124,58,237,0.18);
      border-radius: 1.2rem;
      padding: 2.5rem;
      transition: all 0.4s ease;
    }

    .card:hover {
      transform: translateY(-12px);
      border-color: rgba(124,58,237,0.45);
      box-shadow: 0 25px 60px rgba(0,0,0,0.4);
    }

    .card h3 {
      font-size: 1.6rem;
      margin-bottom: 1.2rem;
      color: var(--accent);
    }

    .card p {
      color: #cbd5e1;
      line-height: 1.7;
    }

    footer {
      text-align: center;
      padding: 4rem 0 6rem;
      color: var(--gray);
      font-size: 0.95rem;
    }

    @media (max-width: 640px) {
      header { padding: 4rem 0 8rem; }
      .glow-text { font-size: clamp(3rem, 10vw, 7rem); }
      .tagline { font-size: 1.25rem; }
    }
  </style>
</head>
<body>

  <div class="container">

    <header>
      <h1 class="glow-text">NEON HORIZON</h1>
      <p class="tagline">
        Where tomorrow’s ideas meet today’s ambition.<br>
        Fast. Beautiful. Unstoppable.
      </p>

      <div class="btn-group">
        <a href="#features" class="btn btn-primary">Explore Now</a>
        <a href="#" class="btn btn-outline">Watch Demo</a>
      </div>
    </header>

    <section class="features" id="features">
      <div class="card">
        <h3>⚡ Lightning Fast</h3>
        <p>Sub-second load times, smooth animations, and zero bloat — built for users who hate waiting.</p>
      </div>
      <div class="card">
        <h3>🌌 Cosmic Design</h3>
        <p>Neon gradients, glassmorphism, micro-interactions — interfaces that feel like the future.</p>
      </div>
      <div class="card">
        <h3>🛠 Built to Scale</h3>
        <p>From landing page to full platform — architecture that grows with your vision.</p>
      </div>
    </section>

    <footer>
      <p>© 2026 Neon Horizon — Crafted with passion in the dark 🌙</p>
    </footer>

  </div>

</body>
</html>
"""

# Save to file
output_path = Path("beautiful_homepage.html")
output_path.write_text(html_content, encoding="utf-8")

print(f"Homepage created successfully!")
print(f"Open this file in your browser:  {output_path.absolute()}")
