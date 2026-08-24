import os

css_content = """/* ==========================================================================
   GENTECH 3 - NEXT-GEN FULL-STACK HEADLESS FINTECH PLATFORM
   Architecture: Apple/Stripe-tier 3D WebGL, Bank Client Portal & NFC Simulator
   Version: 4.0.0
   ========================================================================== */

:root {
  --bg-deep: #030509;
  --bg-surface: #080c16;
  --bg-surface-elevated: #0f172a;
  --bg-card: rgba(13, 19, 35, 0.75);
  --bg-glass: rgba(8, 12, 22, 0.85);

  --gold-primary: #d4af37;
  --gold-light: #f6e27a;
  --gold-dark: #8c6d1f;
  --gold-gradient: linear-gradient(135deg, #f6e27a 0%, #d4af37 40%, #aa7c11 75%, #593e00 100%);
  
  --cyan-accent: #00f0ff;
  --cyan-gradient: linear-gradient(135deg, #00f0ff 0%, #0284c7 100%);
  
  --emerald-accent: #10b981;
  --violet-accent: #a855f7;
  
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --text-dim: #64748b;
  
  --border-luxury: rgba(212, 175, 55, 0.3);
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-cyan: rgba(0, 240, 255, 0.3);
  
  --font-serif: 'Cinzel', 'Playfair Display', Georgia, serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', 'Courier New', monospace;
  
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-full: 9999px;
  
  --shadow-gold: 0 0 35px rgba(212, 175, 55, 0.25);
  --shadow-cyan: 0 0 35px rgba(0, 240, 255, 0.25);
  --shadow-depth: 0 25px 50px -12px rgba(0, 0, 0, 0.9);
  
  --transition-smooth: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-spring: 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-sans);
  background-color: var(--bg-deep);
  color: var(--text-main);
  line-height: 1.65;
  overflow-x: hidden;
  position: relative;
}

body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: 
    radial-gradient(circle at 10% 10%, rgba(212, 175, 55, 0.04) 0%, transparent 40%),
    radial-gradient(circle at 90% 80%, rgba(0, 240, 255, 0.04) 0%, transparent 45%),
    radial-gradient(circle at 50% 50%, rgba(168, 85, 247, 0.02) 0%, transparent 60%);
  pointer-events: none;
  z-index: 0;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-serif);
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--text-main);
}

h1 { font-size: clamp(2.5rem, 5.5vw, 4.5rem); line-height: 1.1; font-weight: 800; }
h2 { font-size: clamp(2rem, 3.8vw, 3rem); line-height: 1.2; }
h3 { font-size: clamp(1.35rem, 2.2vw, 1.85rem); }

.gold-text {
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.cyan-text {
  background: var(--cyan-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

a { color: inherit; text-decoration: none; transition: all var(--transition-smooth); }
button { cursor: pointer; border: none; background: none; font: inherit; color: inherit; }
img { max-width: 100%; height: auto; display: block; }

.container {
  width: 100%;
  max-width: 1340px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 2rem;
  padding-right: 2rem;
  position: relative;
  z-index: 1;
}

.section-spacing {
  padding-top: clamp(5rem, 9vw, 9rem);
  padding-bottom: clamp(5rem, 9vw, 9rem);
}

.section-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 1.1rem;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  background: rgba(212, 175, 55, 0.08);
  border: 1px solid var(--border-luxury);
  color: var(--gold-primary);
  margin-bottom: 1.5rem;
}

/* Header */
.gentech3-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background: var(--bg-glass);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border-bottom: 1px solid var(--border-subtle);
}

.gentech3-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 85px;
}

.brand-wrap {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-emblem {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: linear-gradient(135deg, #1e293b, #030509);
  border: 1px solid var(--border-luxury);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 15px rgba(212, 175, 55, 0.25);
}

.brand-titles h2 { font-size: 1.25rem; letter-spacing: 0.12em; font-weight: 800; }
.brand-titles span { font-size: 0.65rem; letter-spacing: 0.25em; text-transform: uppercase; color: var(--gold-primary); display: block; }

.nav-links {
  display: flex;
  align-items: center;
  gap: 1.75rem;
}

@media (max-width: 1024px) {
  .nav-links { display: none; }
}

.nav-link-item {
  font-size: 0.88rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--text-muted);
  position: relative;
  padding: 0.5rem 0;
}

.nav-link-item:hover, .nav-link-item.active {
  color: var(--gold-light);
}

.nav-link-item.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--gold-gradient);
}

.btn-gold {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.85rem 1.85rem;
  border-radius: var(--radius-full);
  background: var(--gold-gradient);
  color: #030509;
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  box-shadow: var(--shadow-gold);
  transition: all var(--transition-smooth);
}

.btn-gold:hover { transform: translateY(-2px); box-shadow: 0 0 45px rgba(212, 175, 55, 0.5); }

.btn-outline {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.85rem 1.85rem;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-luxury);
  color: var(--gold-light);
  font-weight: 600;
  font-size: 0.85rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  backdrop-filter: blur(10px);
  transition: all var(--transition-smooth);
}

.btn-outline:hover { background: rgba(212, 175, 55, 0.1); transform: translateY(-2px); }

/* 3D Scene Section */
.hero-stage-section {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding-top: 110px;
  padding-bottom: 60px;
}

.hero-grid-split {
  display: grid;
  grid-template-columns: 1fr 1.25fr;
  gap: 3.5rem;
  align-items: center;
}

@media (max-width: 1024px) {
  .hero-grid-split { grid-template-columns: 1fr; text-align: center; }
}

.scene-3d-box {
  position: relative;
  width: 100%;
  height: 520px;
  background: radial-gradient(circle at center, rgba(15, 23, 42, 0.7) 0%, rgba(3, 5, 9, 0.95) 75%);
  border-radius: var(--radius-lg);
  border: 1px solid var(--border-luxury);
  box-shadow: var(--shadow-depth), inset 0 0 50px rgba(0,0,0,0.8);
  overflow: hidden;
}

#canvas3D { width: 100%; height: 100%; display: block; }

.stage-overlay-bar {
  position: absolute;
  bottom: 20px;
  left: 20px;
  right: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(3, 5, 9, 0.85);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  padding: 0.5rem 1.25rem;
  z-index: 10;
}

.artifact-toggle-btn {
  padding: 0.45rem 1rem;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--text-muted);
  transition: all var(--transition-smooth);
}

.artifact-toggle-btn.active {
  background: var(--gold-gradient);
  color: #030509;
  box-shadow: 0 0 15px rgba(212, 175, 55, 0.3);
}

/* Bank Client Portal Styles */
.bank-portal-container {
  background: var(--bg-surface);
  border: 1px solid var(--border-cyan);
  border-radius: var(--radius-lg);
  padding: clamp(2rem, 4vw, 3.5rem);
  box-shadow: var(--shadow-cyan), var(--shadow-depth);
}

.bank-tabs-bar {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 2.5rem;
  overflow-x: auto;
  padding-bottom: 0.5rem;
}

.bank-select-btn {
  padding: 0.6rem 1.4rem;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-muted);
  transition: all var(--transition-smooth);
  white-space: nowrap;
}

.bank-select-btn.active {
  background: var(--cyan-gradient);
  color: #030509;
  border-color: var(--cyan-accent);
  box-shadow: 0 0 15px rgba(0, 240, 255, 0.35);
}

.portal-dashboard-grid {
  display: grid;
  grid-template-columns: 1.4fr 0.8fr;
  gap: 2.5rem;
}

@media (max-width: 1024px) {
  .portal-dashboard-grid { grid-template-columns: 1fr; }
}

.pipeline-step {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.25rem;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  margin-bottom: 0.75rem;
}

.pipeline-step.done { border-color: var(--emerald-accent); }
.pipeline-step.active { border-color: var(--cyan-accent); background: rgba(0, 240, 255, 0.05); }

/* NFC Simulator Styles */
.terminal-simulator-box {
  background: radial-gradient(circle at center, rgba(16, 185, 129, 0.08) 0%, var(--bg-surface) 75%);
  border: 1px solid rgba(16, 185, 129, 0.3);
  border-radius: var(--radius-lg);
  padding: clamp(2rem, 4vw, 3.5rem);
  box-shadow: 0 0 35px rgba(16, 185, 129, 0.2);
}

.terminal-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

@media (max-width: 900px) {
  .terminal-grid { grid-template-columns: 1fr; }
}

.terminal-display {
  background: #000;
  border-radius: var(--radius-md);
  border: 2px solid #1e293b;
  padding: 1.75rem;
  font-family: var(--font-mono);
  font-size: 0.82rem;
  line-height: 1.6;
  min-height: 220px;
  position: relative;
  overflow: hidden;
}

.terminal-led {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #64748b;
  display: inline-block;
  margin-right: 0.5rem;
  transition: all 0.3s;
}

/* Ecosystem 6 Pillars */
.ecosystem-grid-6 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 3.5rem;
}

@media (max-width: 1024px) {
  .ecosystem-grid-6 { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 640px) {
  .ecosystem-grid-6 { grid-template-columns: 1fr; }
}

.eco-card-item {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 2.25rem 2rem;
  position: relative;
  backdrop-filter: blur(16px);
  transition: all var(--transition-smooth);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.eco-card-item:hover {
  transform: translateY(-8px);
  border-color: var(--border-luxury);
  box-shadow: var(--shadow-gold), var(--shadow-depth);
}

.eco-thumb-box {
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at center, rgba(212, 175, 55, 0.06) 0%, transparent 70%);
  border-radius: var(--radius-md);
  margin: 1.25rem 0;
  overflow: hidden;
}

.eco-thumb-box img {
  max-height: 160px;
  object-fit: contain;
  transition: transform var(--transition-spring);
  filter: drop-shadow(0 12px 24px rgba(0,0,0,0.6));
}

.eco-card-item:hover .eco-thumb-box img {
  transform: scale(1.1) rotate(-3deg);
}

.eco-pill-tag {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.25rem 0.65rem;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  color: var(--text-muted);
}

.eco-pill-tag.gold {
  background: rgba(212, 175, 55, 0.1);
  border-color: var(--border-luxury);
  color: var(--gold-light);
}

.eco-pill-tag.cyan {
  background: rgba(0, 240, 255, 0.1);
  border-color: var(--border-cyan);
  color: var(--cyan-accent);
}

/* Atelier */
.atelier-box {
  background: radial-gradient(circle at 70% 30%, rgba(15, 23, 42, 0.8) 0%, var(--bg-surface) 80%);
  border: 1px solid var(--border-luxury);
  border-radius: var(--radius-lg);
  padding: clamp(2rem, 5vw, 4rem);
  box-shadow: var(--shadow-depth);
}

.engraving-preview-stage {
  position: relative;
  height: 320px;
  background: #000;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.laser-beam {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent 0%, rgba(212, 175, 55, 0.4) 50%, rgba(255, 255, 255, 0.8) 52%, transparent 55%);
  pointer-events: none;
  opacity: 0;
}

.laser-beam.firing {
  opacity: 1;
  animation: laserScan 1.2s infinite;
}

@keyframes laserScan {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(200%); }
}

.live-engraved-text {
  position: absolute;
  bottom: 30px;
  right: 40px;
  font-family: var(--font-serif);
  font-size: 1.1rem;
  letter-spacing: 0.25em;
  color: var(--gold-light);
  text-shadow: 0 0 10px var(--gold-primary);
  text-transform: uppercase;
}

.form-control-haute {
  width: 100%;
  padding: 0.95rem 1.25rem;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  color: var(--text-main);
  font-size: 0.95rem;
  transition: border-color var(--transition-smooth);
}

.form-control-haute:focus {
  outline: none;
  border-color: var(--gold-primary);
  box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.15);
}

.gentech3-footer {
  background: #020306;
  border-top: 1px solid var(--border-subtle);
  padding: 5rem 0 3rem 0;
}
"""

with open('/Users/ramay/gentech3-app/assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# Write index.html
html_content = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>GENTECH 3 | Headless Full-Stack FinTech & B2B Bank Issuance Platform</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Three.js 3D WebGL Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <!-- Core Stylesheet -->
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<!-- Header -->
<header class="gentech3-header">
    <div class="container">
        <nav class="gentech3-nav">
            <a href="index.html" class="brand-wrap">
                <div class="brand-emblem">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
                        <circle cx="12" cy="12" r="10" stroke="url(#gold_emblem)" stroke-width="2"/>
                        <path d="M12 6V18M6 12H18" stroke="url(#gold_emblem)" stroke-width="2"/>
                        <defs><linearGradient id="gold_emblem" x1="0" y1="0" x2="24" y2="24"><stop stop-color="#F6E27A"/><stop offset="1" stop-color="#AA7C11"/></linearGradient></defs>
                    </svg>
                </div>
                <div class="brand-titles">
                    <h2>GENTECH 3</h2>
                    <span>Haute-Fintech • Headless Platform</span>
                </div>
            </a>

            <div class="nav-links">
                <a href="#hero" class="nav-link-item active">3D Studio</a>
                <a href="#ecosystem" class="nav-link-item">6 Pillars</a>
                <a href="#portal" class="nav-link-item">B2B Bank Portal</a>
                <a href="#simulator" class="nav-link-item">NFC Simulator</a>
                <a href="#atelier" class="nav-link-item">Laser Atelier</a>
                <a href="#vault" class="nav-link-item">Dubai Vault</a>
            </div>

            <div style="display: flex; align-items: center; gap: 1rem;">
                <button id="soundToggleBtn" style="font-size: 0.8rem; font-weight: 700; color: #f59e0b; padding: 0.4rem 0.8rem; border-radius: var(--radius-full); background: rgba(245,158,11,0.1); border: 1px solid rgba(245,158,11,0.3);">
                    🔊 Sound: ON
                </button>
                <div id="liveDubaiTime" style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--gold-light); background: rgba(0,0,0,0.5); padding: 0.4rem 0.8rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                    00:00:00 GST (Dubai)
                </div>
                <a href="#portal" class="btn-gold" style="padding: 0.65rem 1.4rem; font-size: 0.8rem;">
                    <span>Bank Console</span>
                </a>
            </div>
        </nav>
    </div>
</header>

<main id="hero">
    <!-- 1. Hero 3D Stage -->
    <section class="hero-stage-section">
        <div class="container">
            <div class="hero-grid-split">
                <div>
                    <div class="section-tag">Phase 2 Headless Platform • Dubai R&D</div>
                    <h1>
                        Next-Gen FinTech. <br>
                        <span class="gold-text">Autonomous 3D Ecosystem.</span>
                    </h1>
                    <p style="color: var(--text-muted); font-size: 1.1rem; line-height: 1.8; margin-bottom: 2.25rem; max-width: 540px;">
                        The ultimate hybrid architecture: 60fps GPU WebGL rendering, institutional B2B card issuance tracking, real-time NFC transit simulation, and sub-micron laser engraving in Dubai.
                    </p>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 2.5rem;">
                        <a href="#portal" class="btn-gold">
                            <span>Open B2B Bank Portal</span>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                        </a>
                        <a href="#simulator" class="btn-outline">
                            <span>Test NFC Simulator</span>
                        </a>
                    </div>
                    <div style="display: flex; gap: 2rem; border-top: 1px solid var(--border-subtle); padding-top: 1.5rem; flex-wrap: wrap;">
                        <div>
                            <span style="font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Card Heft</span>
                            <h4 style="color:var(--gold-primary); font-size:1.35rem;">28.5g Titanium</h4>
                        </div>
                        <div>
                            <span style="font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">Wearable RF</span>
                            <h4 style="color:var(--cyan-accent); font-size:1.35rem;">0% Battery</h4>
                        </div>
                        <div>
                            <span style="font-size:0.75rem; text-transform:uppercase; color:var(--text-muted);">NFC Handshake</span>
                            <h4 style="color:var(--emerald-accent); font-size:1.35rem;">&lt;42ms Speed</h4>
                        </div>
                    </div>
                </div>

                <div>
                    <div class="scene-3d-box">
                        <div id="canvas3D"></div>
                        <div class="stage-overlay-bar">
                            <div style="display:flex; gap:0.5rem;">
                                <button class="artifact-toggle-btn active" data-artifact="both">Both</button>
                                <button class="artifact-toggle-btn" data-artifact="ring">Apex Ring</button>
                                <button class="artifact-toggle-btn" data-artifact="card">Sovereign Card</button>
                            </div>
                            <button id="explodedViewBtn" style="display:flex; align-items:center; gap:0.4rem; font-size:0.75rem; font-weight:700; color:var(--gold-light); padding:0.4rem 0.8rem; border-radius:var(--radius-full); background:rgba(255,255,255,0.06); border:1px solid var(--border-luxury);">
                                <span>Exploded X-Ray</span>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8M8 12h8"/></svg>
                            </button>
                        </div>
                    </div>
                    <div style="text-align: center; margin-top: 0.75rem; font-size: 0.75rem; color: var(--text-dim);">
                        ✦ Real-time WebGL 3D Engine • Orbit & Drag with Mouse / Touch
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. The 6 Haute Pillars of GenTech -->
    <section class="section-spacing" id="ecosystem">
        <div class="container">
            <div style="text-align: center; max-width: 760px; margin: 0 auto 3.5rem auto;">
                <div class="section-tag">Complete FinTech Ecosystem</div>
                <h2>Six Master Pillars of Hardware Engineering</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-top: 0.75rem;">
                    From sovereign metal cards and smart rings to city transit ticketing and 5G Super SIMs.
                </p>
            </div>

            <div class="ecosystem-grid-6">
                <!-- 1 -->
                <div class="eco-card-item">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="eco-pill-tag gold">Pillar I • Wearable Tech</span>
                            <span style="font-size:0.75rem; color:var(--text-dim);">IP68 50m</span>
                        </div>
                        <div class="eco-thumb-box">
                            <img src="assets/images/wearable.png" alt="Apex Smart Rings & Wristbands">
                        </div>
                        <h3>Apex Rings & NFC Wristbands</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-top: 0.5rem;">
                            Waterproof zirconia ceramic rings and medical silicone wristbands powered by passive RF resonance. Zero battery, zero charging for life.
                        </p>
                    </div>
                    <button class="btn-outline" style="width:100%; justify-content:center; margin-top:1.5rem; font-size:0.75rem;">Configure Wearables</button>
                </div>

                <!-- 2 -->
                <div class="eco-card-item">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="eco-pill-tag gold">Pillar II • Luxury Cards</span>
                            <span style="font-size:0.75rem; color:var(--gold-primary);">28.5g Heavy</span>
                        </div>
                        <div class="eco-thumb-box">
                            <img src="assets/images/portfolio-4.png" alt="Sovereign Titanium Card">
                        </div>
                        <h3>Sovereign Metal & Ceramic Cards</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-top: 0.5rem;">
                            Grade-5 titanium, 24K gold mirror finish, and diamond-gloss zirconia ceramic cards for VIP private banking and fintech prestige tiers.
                        </p>
                    </div>
                    <button class="btn-gold" style="width:100%; justify-content:center; margin-top:1.5rem; font-size:0.75rem;">Configure Metal Cards</button>
                </div>

                <!-- 3 -->
                <div class="eco-card-item">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="eco-pill-tag cyan">Pillar III • Transit</span>
                            <span style="font-size:0.75rem; color:var(--cyan-accent);">&lt;100ms Gate</span>
                        </div>
                        <div class="eco-thumb-box">
                            <img src="assets/images/transportcards.png" alt="Transport & City Cards">
                        </div>
                        <h3>Transport & Smart City Cards</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-top: 0.5rem;">
                            High-throughput contactless fare collection for subways, bus fleets, and municipal smart city multi-application cards.
                        </p>
                    </div>
                    <button class="btn-outline" style="width:100%; justify-content:center; margin-top:1.5rem; font-size:0.75rem;">Inquire Transit Cards</button>
                </div>

                <!-- 4 -->
                <div class="eco-card-item">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="eco-pill-tag gold">Pillar IV • 5G Telecom</span>
                            <span style="font-size:0.75rem; color:var(--emerald-accent);">Super SIM</span>
                        </div>
                        <div class="eco-thumb-box">
                            <img src="assets/images/supersim.png" alt="Super NFC 5G SIM Cards">
                        </div>
                        <h3>Super NFC 5G SIM & Telecom</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-top: 0.5rem;">
                            Combines telecom subscription, banking payment applets, electronic ID, and transit tokens into a single secure mobile element.
                        </p>
                    </div>
                    <button class="btn-outline" style="width:100%; justify-content:center; margin-top:1.5rem; font-size:0.75rem;">Inquire Super SIMs</button>
                </div>

                <!-- 5 -->
                <div class="eco-card-item">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="eco-pill-tag gold">Pillar V • Micro-Plates</span>
                            <span style="font-size:0.75rem; color:var(--gold-light);">Laser Art</span>
                        </div>
                        <div class="eco-thumb-box">
                            <img src="assets/images/customize-chip.png" alt="Custom Chip Modules">
                        </div>
                        <h3>Bespoke Chip Modules</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-top: 0.5rem;">
                            Transform standard contact plates into branded art. Custom laser engraved logo geometries, 24K gold mirror plating, and micro-grooved luxury finishes.
                        </p>
                    </div>
                    <button class="btn-outline" style="width:100%; justify-content:center; margin-top:1.5rem; font-size:0.75rem;">Inquire Custom Chips</button>
                </div>

                <!-- 6 -->
                <div class="eco-card-item">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="eco-pill-tag">Pillar VI • Hardware</span>
                            <span style="font-size:0.75rem; color:var(--text-dim);">POS & Issuance</span>
                        </div>
                        <div class="eco-thumb-box">
                            <img src="assets/images/pos.png" alt="Banking POS & Issuance Hardware">
                        </div>
                        <h3>Banking POS & Hardware</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-top: 0.5rem;">
                            Card personalization machines, desktop embossers, high-speed thermal printers, Android POS terminals, and cryptographic HSM modules.
                        </p>
                    </div>
                    <button class="btn-outline" style="width:100%; justify-content:center; margin-top:1.5rem; font-size:0.75rem;">Inquire Hardware</button>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Interactive B2B Bank Client Portal (Dashboard Mockup) -->
    <section class="section-spacing" id="portal" style="background: rgba(0,240,255,0.015);">
        <div class="container">
            <div style="text-align: center; max-width: 760px; margin: 0 auto 3rem auto;">
                <div class="section-tag" style="color: var(--cyan-accent); border-color: var(--border-cyan);">B2B Institutional Console</div>
                <h2>Live Bank Client Portal (Issuance Tracker)</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-top: 0.75rem;">
                    Institutional clients can track live production batches, upload card artwork for 3D soft-proofing, and monitor cryptographic key injection in Dubai.
                </p>
            </div>

            <div class="bank-portal-container">
                <!-- Institution Selector -->
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 2rem;">
                    <div>
                        <span style="font-size:0.75rem; text-transform:uppercase; color:var(--text-dim); letter-spacing:0.1em; display:block;">Select Partner Institution:</span>
                        <div class="bank-tabs-bar" style="margin-top:0.5rem; margin-bottom:0;">
                            <button class="bank-select-btn active" data-bank="enbd">Emirates NBD</button>
                            <button class="bank-select-btn" data-bank="fab">First Abu Dhabi Bank (FAB)</button>
                            <button class="bank-select-btn" data-bank="sc">Standard Chartered</button>
                            <button class="bank-select-btn" data-bank="revolut">Revolut ME</button>
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <span style="font-size:0.75rem; color:var(--cyan-accent); font-weight:700; text-transform:uppercase;">Vault Status: Online</span>
                        <div style="font-size:0.85rem; color:var(--text-muted);">Encrypted TLS 1.3 / HSM Active</div>
                    </div>
                </div>

                <!-- Dashboard Grid -->
                <div class="portal-dashboard-grid">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem;">
                            <h4 style="font-size: 1.2rem;" id="portalBankName">Emirates NBD • Private Wealth</h4>
                            <span class="eco-pill-tag gold" id="portalBatchNumber">PO-GT-9482</span>
                        </div>
                        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1.5rem;">
                            Active Production Order: <strong style="color:var(--text-main);" id="portalActiveVolume">50,000 Cards (24K Gold Plated Titanium)</strong>
                        </p>

                        <!-- Step 1 -->
                        <div class="pipeline-step done">
                            <div>
                                <strong style="display:block; font-size:0.95rem;">1. CNC Titanium Monolith Milling</strong>
                                <span style="font-size:0.8rem; color:var(--text-muted);">Sub-micron chamfering & 28.5g weight calibration</span>
                            </div>
                            <span style="color:var(--emerald-accent); font-weight:bold; font-size:0.85rem;">✓ 100% Done</span>
                        </div>

                        <!-- Step 2 -->
                        <div class="pipeline-step done">
                            <div>
                                <strong style="display:block; font-size:0.95rem;">2. 24K Gold Sputter & Prelam Antenna Bonding</strong>
                                <span style="font-size:0.8rem; color:var(--text-muted);">Dual-interface inductive copper coil embedding</span>
                            </div>
                            <span style="color:var(--emerald-accent); font-weight:bold; font-size:0.85rem;">✓ 100% Done</span>
                        </div>

                        <!-- Step 3 -->
                        <div class="pipeline-step active">
                            <div>
                                <strong style="display:block; font-size:0.95rem; color:var(--cyan-accent);">3. CC EAL6+ Cryptographic Key Injection & Personalization</strong>
                                <span style="font-size:0.8rem; color:var(--text-muted);">JavaCard OS applet flashing & laser cardholder serialization</span>
                            </div>
                            <span style="color:var(--cyan-accent); font-weight:bold; font-size:0.85rem;">⚡ 84% In Progress</span>
                        </div>

                        <!-- Step 4 -->
                        <div class="pipeline-step">
                            <div>
                                <strong style="display:block; font-size:0.95rem;">4. EMVCo & PCI-DSS Final Quality Certification</strong>
                                <span style="font-size:0.8rem; color:var(--text-muted);">Optical character verification & magnetic stripe QC</span>
                            </div>
                            <span style="color:var(--text-dim); font-size:0.85rem;">Pending Step 3</span>
                        </div>

                        <!-- Step 5 -->
                        <div class="pipeline-step">
                            <div>
                                <strong style="display:block; font-size:0.95rem;">5. Armored Courier & Diplomatic Global Dispatch</strong>
                                <span style="font-size:0.8rem; color:var(--text-muted);">Direct delivery to central bank vaults</span>
                            </div>
                            <span style="color:var(--text-dim); font-size:0.85rem;">Scheduled</span>
                        </div>
                    </div>

                    <!-- Soft Proofing & Quick Specs -->
                    <div style="background: var(--bg-surface-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.75rem; display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <h4 style="font-size: 1.1rem; margin-bottom: 1rem;">Artwork Soft-Proof Studio</h4>
                            <div style="border: 2px dashed rgba(212,175,55,0.3); border-radius: var(--radius-sm); padding: 2rem 1rem; text-align: center; margin-bottom: 1.5rem; background: rgba(0,0,0,0.3);">
                                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin:0 auto 0.75rem auto; color:var(--gold-primary);"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
                                <strong style="font-size:0.85rem; display:block;">Drag & Drop Bank Vector (.SVG / .AI)</strong>
                                <span style="font-size:0.75rem; color:var(--text-muted);">Instant 3D Preview Generation</span>
                            </div>
                            <div style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.8;">
                                <div>• Lead Time: <strong>12 Business Days</strong></div>
                                <div>• Security Grade: <strong>CC EAL6+ Certified</strong></div>
                                <div>• Production Corridors: <strong>Dubai RAK Hub</strong></div>
                            </div>
                        </div>
                        <button class="btn-gold" style="width: 100%; justify-content: center; margin-top: 1.5rem; font-size: 0.8rem;">
                            <span>Download Full Batch Audit (PDF)</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Interactive NFC Transit Gate & POS Handshake Simulator -->
    <section class="section-spacing" id="simulator">
        <div class="container">
            <div style="text-align: center; max-width: 760px; margin: 0 auto 3rem auto;">
                <div class="section-tag" style="color: var(--emerald-accent); border-color: rgba(16,185,129,0.3);">Real-Time Cryptographic Emulator</div>
                <h2>Interactive NFC Gate & Terminal Simulator</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-top: 0.75rem;">
                    Click to simulate tapping an Apex Ring or Sovereign Card onto a subway turnstile or POS terminal. Listen to the synthesized chime and observe the sub-50ms cryptographic handshake log.
                </p>
            </div>

            <div class="terminal-simulator-box">
                <div class="terminal-grid">
                    <!-- Controls -->
                    <div>
                        <span class="eco-pill-tag cyan" style="margin-bottom: 1rem; display: inline-block;">Test Payment Form Factor:</span>
                        <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">Select Artifact to Tap:</h3>
                        <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 2rem;">
                            <button class="btn-gold sim-tap-btn" data-device="Apex Smart Ring">
                                <span>💍 Tap Apex Ring (NFC)</span>
                            </button>
                            <button class="btn-outline sim-tap-btn" data-device="Sovereign Titanium Card">
                                <span>💳 Tap Sovereign Card (EMV)</span>
                            </button>
                        </div>
                        <div style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.8;">
                            <p>✦ <strong>Passive Inductive RF:</strong> The device draws 100% of operating power from the terminal's 13.56 MHz carrier frequency.</p>
                            <p>✦ <strong>Ultra-Low Latency:</strong> Dual-interface JavaCard OS completes cryptographic certificate exchange in under <strong>42 milliseconds</strong>.</p>
                        </div>
                    </div>

                    <!-- Digital Terminal Display -->
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                            <div style="display: flex; align-items: center;">
                                <span class="terminal-led" id="terminalStatusLed"></span>
                                <strong style="font-size: 0.85rem; font-family: var(--font-mono); color: var(--text-muted);">POS-READER-GTX-900</strong>
                            </div>
                            <span id="gateStatusBadge" style="font-family: var(--font-mono); font-size: 0.85rem; font-weight: bold; color: var(--text-dim);">IDLE / READY</span>
                        </div>
                        <div class="terminal-display" id="terminalLogScreen">
                            <div style="color: #64748b;">[STANDBY] Waiting for 13.56 MHz contactless target...</div>
                            <div style="color: #64748b;">[TIP] Click one of the buttons on the left to initiate transaction.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Live Laser Engraving Atelier -->
    <section class="section-spacing" id="atelier">
        <div class="container">
            <div class="atelier-box">
                <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 3.5rem; align-items: center;">
                    <div>
                        <div class="section-tag" style="color: var(--gold-light); border-color: var(--border-luxury);">Customization Atelier</div>
                        <h2 style="margin-bottom: 1rem;">Live Laser Engraving Studio</h2>
                        <p style="color: var(--text-muted); margin-bottom: 2rem;">
                            Personalize your bank's sovereign artifacts. Type any name or VIP cardholder serial to watch the precision laser scan across the card and ring surface in real time.
                        </p>

                        <div style="margin-bottom: 2rem;">
                            <label style="font-size:0.85rem; text-transform:uppercase; letter-spacing:0.1em; color:var(--gold-primary); display:block; margin-bottom:0.6rem; font-weight:700;">
                                Live Laser Engraving Text Preview:
                            </label>
                            <input type="text" id="engravingTextInput" class="form-control-haute" placeholder="Type Cardholder Name (e.g. ALEXANDER VANCE)" value="ALEXANDER VANCE" maxlength="28">
                        </div>

                        <div>
                            <label style="font-size:0.85rem; text-transform:uppercase; letter-spacing:0.1em; color:var(--text-muted); display:block; margin-bottom:0.6rem;">
                                Select Precious Alloy / Finish:
                            </label>
                            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                                <button class="swatch-btn active" data-material="gold" style="padding:0.75rem 1rem; border-radius:var(--radius-md); background:var(--bg-surface-elevated); border:1px solid var(--border-luxury); display:flex; align-items:center; gap:0.5rem; font-size:0.75rem; font-weight:700;">
                                    <div style="width:20px; height:20px; border-radius:50%; background:linear-gradient(135deg, #f6e27a, #aa7c11);"></div>
                                    <span>24K Gold</span>
                                </button>
                                <button class="swatch-btn" data-material="rosegold" style="padding:0.75rem 1rem; border-radius:var(--radius-md); background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); display:flex; align-items:center; gap:0.5rem; font-size:0.75rem; font-weight:700;">
                                    <div style="width:20px; height:20px; border-radius:50%; background:linear-gradient(135deg, #f7d6c8, #8c5332);"></div>
                                    <span>Rose Gold</span>
                                </button>
                                <button class="swatch-btn" data-material="titanium" style="padding:0.75rem 1rem; border-radius:var(--radius-md); background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); display:flex; align-items:center; gap:0.5rem; font-size:0.75rem; font-weight:700;">
                                    <div style="width:20px; height:20px; border-radius:50%; background:linear-gradient(135deg, #ffffff, #475569);"></div>
                                    <span>Titanium</span>
                                </button>
                                <button class="swatch-btn" data-material="obsidian" style="padding:0.75rem 1rem; border-radius:var(--radius-md); background:var(--bg-surface-elevated); border:1px solid var(--border-subtle); display:flex; align-items:center; gap:0.5rem; font-size:0.75rem; font-weight:700;">
                                    <div style="width:20px; height:20px; border-radius:50%; background:linear-gradient(135deg, #1e293b, #030509); border:1px solid #00f0ff;"></div>
                                    <span>Obsidian</span>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div>
                        <div class="engraving-preview-stage">
                            <div class="laser-beam"></div>
                            <img src="assets/images/portfolio-4.png" alt="Laser Engraving Card" style="max-height: 220px; filter: drop-shadow(0 10px 25px rgba(212,175,55,0.4));">
                            <div class="live-engraved-text" id="liveEngravedText">ALEXANDER VANCE</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem; font-size: 0.8rem; color: var(--text-dim);">
                            <span>Precision: 0.01mm Fiber Laser</span>
                            <span style="color: var(--gold-primary);">Ready for Instant Production in Dubai</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. Dubai Private Vault & Closing Requisition -->
    <section class="section-spacing" id="vault">
        <div class="container">
            <div style="background: radial-gradient(circle at 50% 50%, rgba(212,175,55,0.15) 0%, #060911 75%); border: 1px solid var(--border-luxury); border-radius: var(--radius-lg); padding: clamp(3rem, 6vw, 5.5rem); text-align: center; box-shadow: var(--shadow-gold);">
                <div class="section-tag" style="margin-bottom: 1.25rem;">Private Banking & Sovereign FinTechs</div>
                <h2 style="font-size: clamp(2.2rem, 4vw, 3.5rem); margin-bottom: 1.25rem;">
                    Deploy Next-Gen FinTech Hardware in Dubai
                </h2>
                <p style="color: var(--text-muted); max-width: 680px; margin: 0 auto 2.5rem auto; font-size: 1.1rem; line-height: 1.8;">
                    Turnkey manufacturing, White-Glove sample kits, cryptographic key injection, and global armed dispatch for Tier-1 banks, telecoms, and digital neobanks.
                </p>
                <div style="display: flex; justify-content: center; gap: 1.25rem; flex-wrap: wrap;">
                    <a href="mailto:info@gentech.ae" class="btn-gold">
                        <span>Direct Wire to Dubai Vault</span>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </a>
                </div>
            </div>
        </div>
    </section>
</main>

<footer class="gentech3-footer">
    <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 3rem; border-bottom: 1px solid var(--border-subtle); flex-wrap: wrap; gap: 2rem;">
            <div>
                <span style="font-family: var(--font-serif); font-size: 1.5rem; letter-spacing: 0.15em; font-weight: 800;" class="gold-text">GENTECH GLOBAL</span>
                <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 0.5rem; max-width: 440px;">
                    Dubai Haute-Fintech Center • Ras Al Khaimah Economic Zone, UAE.<br>
                    Next-Gen Headless Platform Architecture (Phase 2).
                </p>
            </div>
            <div style="display: flex; gap: 2rem; font-size: 0.85rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--gold-light); flex-wrap: wrap;">
                <span>🛡️ EMVCo Certified</span>
                <span>🔒 PCI-DSS Level 1</span>
                <span>⚡ ISO 14443 & 7816</span>
                <span>📱 GSMA 5G Compliant</span>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 2rem; font-size: 0.85rem; color: var(--text-dim); flex-wrap: wrap; gap: 1rem;">
            <div>&copy; 2025-2026 GENTECH GLOBAL LLC. All Rights Reserved. Mastered in Dubai, UAE.</div>
            <div style="color: var(--gold-primary);">GenTech 3 • Headless Platform Edition</div>
        </div>
    </div>
</footer>

<!-- Scripts -->
<script src="assets/js/audio.js"></script>
<script src="assets/js/scene3d.js"></script>
<script src="assets/js/simulator.js"></script>
<script src="assets/js/portal.js"></script>
<script src="assets/js/app.js"></script>
</body>
</html>
"""

with open('/Users/ramay/gentech3-app/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("GenTech 3 HTML & CSS built successfully!")
