import os

print("Completely redesigning GenTech 3 with Apple/Linear-style Bento Grid & Holographic Hardware Lab...")

css_content = """/* ==========================================================================
   GENTECH 3 - NEXT-GEN HOLOGRAPHIC HARDWARE LAB & BENTO PLATFORM (RADICAL REDESIGN)
   Aesthetic: Apple Pro / Linear / Stripe / Tesla Cyber-Hardware
   Colors: Obsidian Zero (#000206), Liquid Mercury, Prismatic Hologram, Neon Mint
   ========================================================================== */

:root {
  --bg-deep: #000206;
  --bg-bento: rgba(10, 15, 26, 0.65);
  --bg-bento-elevated: rgba(16, 24, 40, 0.85);
  --bg-glass: rgba(5, 8, 15, 0.88);
  
  --prismatic-gradient: linear-gradient(135deg, #00f5d4 0%, #7b2cbf 50%, #f72585 100%);
  --hologram-cyan: #00f5d4;
  --hologram-violet: #9d4edd;
  --hologram-pink: #f72585;
  --mercury-silver: #e2e8f0;
  
  --text-primary: #ffffff;
  --text-secondary: #94a3b8;
  --text-dimmed: #475569;
  
  --border-subtle: rgba(255, 255, 255, 0.07);
  --border-active: rgba(0, 245, 212, 0.4);
  --border-hologram: rgba(157, 78, 221, 0.4);
  
  --font-display: 'Syne', 'Space Grotesk', -apple-system, sans-serif;
  --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  
  --radius-sm: 10px;
  --radius-md: 18px;
  --radius-lg: 28px;
  --radius-full: 9999px;
  
  --shadow-bento: 0 20px 40px -15px rgba(0, 0, 0, 0.8), 0 0 1px 1px rgba(255, 255, 255, 0.05);
  --shadow-glow: 0 0 30px rgba(0, 245, 212, 0.2);
  
  --transition-smooth: 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-spring: 0.55s cubic-bezier(0.34, 1.56, 0.64, 1);
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
  font-family: var(--font-body);
  background-color: var(--bg-deep);
  color: var(--text-primary);
  line-height: 1.6;
  overflow-x: hidden;
}

/* Background Cyber Grid */
body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-image: 
    linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
  background-size: 60px 60px;
  mask-image: radial-gradient(circle at center, black 40%, transparent 85%);
  -webkit-mask-image: radial-gradient(circle at center, black 40%, transparent 85%);
  pointer-events: none;
  z-index: 0;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-display);
  font-weight: 800;
  letter-spacing: -0.03em;
  color: var(--text-primary);
}

h1 { font-size: clamp(2.8rem, 6vw, 5.2rem); line-height: 1.05; }
h2 { font-size: clamp(2.2rem, 4vw, 3.4rem); line-height: 1.15; }
h3 { font-size: clamp(1.4rem, 2.5vw, 2rem); }

.gradient-hologram {
  background: var(--prismatic-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.gradient-mercury {
  background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

a { color: inherit; text-decoration: none; transition: all var(--transition-smooth); }
button { cursor: pointer; border: none; background: none; font: inherit; color: inherit; }
img { max-width: 100%; height: auto; display: block; }

.container {
  width: 100%;
  max-width: 1360px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 2rem;
  padding-right: 2rem;
  position: relative;
  z-index: 1;
}

.section-spacing {
  padding-top: clamp(5rem, 8vw, 8.5rem);
  padding-bottom: clamp(5rem, 8vw, 8.5rem);
}

/* Linear-Style Pill Tag */
.telemetry-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.4rem 1rem;
  border-radius: var(--radius-full);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  background: rgba(0, 245, 212, 0.08);
  border: 1px solid rgba(0, 245, 212, 0.3);
  color: var(--hologram-cyan);
  box-shadow: 0 0 15px rgba(0, 245, 212, 0.15);
}

.pulse-led {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--hologram-cyan);
  box-shadow: 0 0 8px var(--hologram-cyan);
  animation: pulseLed 1.8s infinite;
}

@keyframes pulseLed {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(0.8); opacity: 0.3; }
}

/* --------------------------------------------------------------------------
   Linear/Apple Minimalist Navigation
   -------------------------------------------------------------------------- */
.cyber-nav-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background: var(--bg-glass);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-subtle);
}

.cyber-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 80px;
}

.brand-emblem-box {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.brand-cube {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: linear-gradient(135deg, #00f5d4, #7b2cbf);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 20px rgba(0, 245, 212, 0.3);
}

.brand-cube svg {
  width: 22px;
  height: 22px;
  fill: #000206;
}

.brand-name {
  font-family: var(--font-display);
  font-size: 1.3rem;
  font-weight: 900;
  letter-spacing: -0.02em;
}

.brand-tagline {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: var(--hologram-cyan);
  letter-spacing: 0.15em;
  text-transform: uppercase;
}

.nav-links-cyber {
  display: flex;
  align-items: center;
  gap: 2rem;
}

@media (max-width: 1024px) {
  .nav-links-cyber { display: none; }
}

.nav-link-cyber {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-secondary);
  transition: all var(--transition-smooth);
  position: relative;
  padding: 0.4rem 0;
}

.nav-link-cyber:hover, .nav-link-cyber.active {
  color: var(--text-primary);
}

.nav-link-cyber.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--prismatic-gradient);
}

/* Linear-style Action Buttons */
.btn-cyber-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  padding: 0.75rem 1.6rem;
  border-radius: var(--radius-full);
  background: #ffffff;
  color: #000206;
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: -0.01em;
  transition: all var(--transition-smooth);
  box-shadow: 0 4px 20px rgba(255, 255, 255, 0.2);
}

.btn-cyber-primary:hover {
  background: var(--hologram-cyan);
  box-shadow: 0 0 25px rgba(0, 245, 212, 0.5);
  transform: translateY(-2px);
}

.btn-cyber-glass {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  padding: 0.75rem 1.6rem;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  color: var(--text-primary);
  font-weight: 600;
  font-size: 0.85rem;
  backdrop-filter: blur(12px);
  transition: all var(--transition-smooth);
}

.btn-cyber-glass:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: var(--hologram-cyan);
  transform: translateY(-2px);
}

/* --------------------------------------------------------------------------
   Hardware Engineering Lab Hero (Full Interactive 3D Workstation)
   -------------------------------------------------------------------------- */
.hardware-lab-hero {
  padding-top: 130px;
  padding-bottom: 50px;
  position: relative;
}

.lab-workstation-frame {
  background: radial-gradient(circle at center, rgba(16, 24, 40, 0.7) 0%, rgba(3, 6, 12, 0.95) 85%);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-bento);
  position: relative;
  overflow: hidden;
  margin-top: 2.5rem;
}

.lab-header-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.75rem;
  background: rgba(0, 2, 6, 0.75);
  border-bottom: 1px solid var(--border-subtle);
  font-family: var(--font-mono);
  font-size: 0.8rem;
}

.lab-hud-controls {
  display: flex;
  gap: 0.6rem;
}

.hud-btn {
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-sm);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  color: var(--text-secondary);
  font-size: 0.75rem;
  font-weight: 600;
  transition: all var(--transition-smooth);
}

.hud-btn.active, .hud-btn:hover {
  background: rgba(0, 245, 212, 0.15);
  border-color: var(--hologram-cyan);
  color: var(--hologram-cyan);
}

.lab-3d-stage {
  height: 520px;
  position: relative;
  width: 100%;
}

#canvas3D {
  width: 100%;
  height: 100%;
  display: block;
}

.stage-floating-telemetry {
  position: absolute;
  top: 20px;
  left: 20px;
  background: rgba(0, 2, 6, 0.85);
  backdrop-filter: blur(12px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1rem 1.25rem;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--text-secondary);
  pointer-events: none;
  line-height: 1.7;
}

.stage-floating-telemetry strong {
  color: var(--hologram-cyan);
}

/* --------------------------------------------------------------------------
   THE BENTO GRID ECOSYSTEM (Apple/Linear 12-Column Architecture)
   -------------------------------------------------------------------------- */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1.5rem;
  margin-top: 3.5rem;
}

.bento-card {
  background: var(--bg-bento);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 2.25rem;
  backdrop-filter: blur(20px);
  box-shadow: var(--shadow-bento);
  position: relative;
  overflow: hidden;
  transition: all var(--transition-smooth);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.bento-card:hover {
  border-color: var(--border-active);
  transform: translateY(-4px);
  box-shadow: var(--shadow-glow), var(--shadow-bento);
}

/* Bento Spans */
.span-8 { grid-column: span 8; }
.span-4 { grid-column: span 4; }
.span-6 { grid-column: span 6; }
.span-12 { grid-column: span 12; }

@media (max-width: 1024px) {
  .span-8, .span-4, .span-6 { grid-column: span 12; }
}

.bento-media-box {
  height: 220px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at center, rgba(0, 245, 212, 0.05) 0%, transparent 70%);
  border-radius: var(--radius-md);
  margin: 1.5rem 0;
  position: relative;
  overflow: hidden;
}

.bento-media-box img {
  max-height: 180px;
  object-fit: contain;
  transition: transform var(--transition-spring);
  filter: drop-shadow(0 15px 30px rgba(0,0,0,0.8));
}

.bento-card:hover .bento-media-box img {
  transform: scale(1.08) rotate(-2deg);
}

/* --------------------------------------------------------------------------
   Live Cryptographic NFC Simulator Component
   -------------------------------------------------------------------------- */
.nfc-terminal-hud {
  background: #000;
  border-radius: var(--radius-md);
  border: 1px solid #1e293b;
  padding: 1.5rem;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  line-height: 1.6;
  min-height: 200px;
}

.terminal-status-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--hologram-cyan);
  display: inline-block;
  margin-right: 0.5rem;
  box-shadow: 0 0 10px var(--hologram-cyan);
}

/* --------------------------------------------------------------------------
   B2B Bank Client Pipeline Matrix Component
   -------------------------------------------------------------------------- */
.bank-pipeline-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.85rem 1.1rem;
  border-radius: var(--radius-sm);
  background: var(--bg-bento-elevated);
  border: 1px solid var(--border-subtle);
  margin-bottom: 0.65rem;
  font-size: 0.88rem;
}

.bank-pipeline-row.done { border-color: rgba(16, 185, 129, 0.4); }
.bank-pipeline-row.active { border-color: var(--hologram-cyan); background: rgba(0, 245, 212, 0.06); }

/* --------------------------------------------------------------------------
   Laser Engraving Studio
   -------------------------------------------------------------------------- */
.laser-card-preview {
  position: relative;
  height: 260px;
  background: #000;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.laser-scanner-line {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent 0%, rgba(0, 245, 212, 0.4) 50%, rgba(255, 255, 255, 0.8) 52%, transparent 55%);
  pointer-events: none;
  opacity: 0;
}

.laser-scanner-line.firing {
  opacity: 1;
  animation: laserSweep 1.2s infinite;
}

@keyframes laserSweep {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(200%); }
}

.engraved-live-text {
  position: absolute;
  bottom: 25px;
  right: 30px;
  font-family: var(--font-display);
  font-size: 1.05rem;
  letter-spacing: 0.2em;
  color: var(--hologram-cyan);
  text-shadow: 0 0 10px rgba(0, 245, 212, 0.8);
  text-transform: uppercase;
}

/* Footer */
.cyber-footer {
  background: #000;
  border-top: 1px solid var(--border-subtle);
  padding: 4.5rem 0 2.5rem 0;
}
"""

with open('/Users/ramay/gentech3-app/assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Write index.html with Apple/Linear Bento Architecture
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>GENTECH 3 | Next-Gen Hardware Engineering & B2B Bento Platform</title>
    
    <!-- Google Fonts: Syne, Space Grotesk, JetBrains Mono, Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&family=Syne:wght@700;800;900&display=swap" rel="stylesheet">
    
    <!-- Three.js 3D WebGL Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <!-- Core Stylesheet -->
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<!-- Navigation Bar (Linear-style) -->
<header class="cyber-nav-header">
    <div class="container">
        <nav class="cyber-nav">
            <a href="index.html" class="brand-emblem-box">
                <div class="brand-cube">
                    <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                </div>
                <div>
                    <div class="brand-name">GENTECH <span style="color:var(--hologram-cyan);">3</span></div>
                    <div class="brand-tagline">Autonomous FinTech Lab</div>
                </div>
            </a>

            <div class="nav-links-cyber">
                <a href="#lab" class="nav-link-cyber active">3D Workstation</a>
                <a href="#bento" class="nav-link-cyber">Bento Ecosystem</a>
                <a href="#simulator" class="nav-link-cyber">NFC Terminal</a>
                <a href="#portal" class="nav-link-cyber">Bank Issuance Console</a>
                <a href="#atelier" class="nav-link-cyber">Laser Studio</a>
            </div>

            <div style="display: flex; align-items: center; gap: 1rem;">
                <button id="soundToggleBtn" style="font-family:var(--font-mono); font-size:0.75rem; color:var(--hologram-cyan); padding:0.35rem 0.8rem; border-radius:var(--radius-full); background:rgba(0,245,212,0.08); border:1px solid rgba(0,245,212,0.3);">
                    🔊 HAPTICS: ON
                </button>
                <div id="liveDubaiTime" style="font-family: var(--font-mono); font-size: 0.78rem; color: #94a3b8; background: rgba(0,0,0,0.6); padding: 0.35rem 0.8rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                    00:00:00 GST
                </div>
                <a href="#portal" class="btn-cyber-primary" style="padding: 0.55rem 1.25rem; font-size: 0.8rem;">
                    <span>Launch B2B Portal</span>
                </a>
            </div>
        </nav>
    </div>
</header>

<main>
    <!-- 1. Full 3D Hardware Engineering Workstation Hero -->
    <section class="hardware-lab-hero" id="lab">
        <div class="container">
            <div style="text-align: center; max-width: 840px; margin: 0 auto 1.5rem auto;">
                <div class="telemetry-tag">
                    <span class="pulse-led"></span> Phase 2 Hardware Lab • Dubai Hub
                </div>
                <h1 style="margin-top: 1rem;">
                    The Architecture of <br>
                    <span class="gradient-hologram">Autonomous Physical Fintech.</span>
                </h1>
                <p style="color: var(--text-secondary); font-size: 1.15rem; margin-top: 1rem;">
                    An end-to-end hardware platform: Real-time 3D GPU WebGL inspection, institutional bank issuance tracking, sub-50ms transit NFC handshakes, and sub-micron laser calibration.
                </p>
            </div>

            <!-- 3D Hardware Engineering Workstation Frame -->
            <div class="lab-workstation-frame">
                <div class="lab-header-bar">
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color:var(--hologram-cyan);">● WORKSTATION: GT-LAB-01</span>
                        <span style="color:var(--text-dimmed);">|</span>
                        <span>TARGET: DUAL 3D TELEMETRY</span>
                    </div>
                    <div class="lab-hud-controls">
                        <button class="hud-btn artifact-toggle-btn active" data-artifact="both">Both Artifacts</button>
                        <button class="hud-btn artifact-toggle-btn" data-artifact="ring">Apex Ring</button>
                        <button class="hud-btn artifact-toggle-btn" data-artifact="card">Sovereign Card</button>
                        <button class="hud-btn" id="explodedViewBtn">⚡ Exploded X-Ray</button>
                    </div>
                </div>

                <div class="lab-3d-stage">
                    <div id="canvas3D"></div>
                    <div class="stage-floating-telemetry">
                        <div>CHASSIS: <strong>Grade 5 Ti-6Al-4V</strong></div>
                        <div>RF RESONANCE: <strong>13.56 MHz (ISO 14443)</strong></div>
                        <div>CRYPTO CORE: <strong>JavaCard CC EAL6+</strong></div>
                        <div>BATTERY POWER: <strong>0% (Passive Inductive)</strong></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. The Apple/Linear Bento Grid Ecosystem -->
    <section class="section-spacing" id="bento">
        <div class="container">
            <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 2.5rem; flex-wrap: wrap; gap: 1.5rem;">
                <div>
                    <div class="telemetry-tag">Modular Capabilities</div>
                    <h2 style="margin-top: 0.5rem;">The GenTech Bento Ecosystem</h2>
                </div>
                <p style="color: var(--text-secondary); max-width: 480px; font-size: 0.95rem;">
                    Every hardware tier is manufactured under strict PCI-DSS Level 1 and EMVCo certification corridors in the Ras Al Khaimah Economic Zone.
                </p>
            </div>

            <!-- 12-Column Bento Grid -->
            <div class="bento-grid">
                <!-- Bento 1: Apex Smart Ring (Span 8) -->
                <div class="bento-card span-8">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="telemetry-tag" style="color:var(--hologram-cyan); border-color:rgba(0,245,212,0.3);">Artifact I • Wearable Tech</span>
                            <span style="font-family:var(--font-mono); font-size:0.8rem; color:var(--text-dimmed);">IP68 • 50M SUBMERSIBLE</span>
                        </div>
                        <h3 style="margin-top: 1rem;">The Apex Smart Payment Ring & Wristbands</h3>
                        <p style="color: var(--text-secondary); font-size: 0.95rem; margin-top: 0.5rem;">
                            Waterproof zirconia ceramic and titanium smart rings engineered with micro-tuned passive RF resonance. Zero battery, zero charging cords — tap anywhere in the world instantly.
                        </p>
                        
                        <div class="bento-media-box">
                            <img src="assets/images/wearable.png" alt="Apex Smart Rings & Wristbands">
                        </div>

                        <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; font-family: var(--font-mono); font-size: 0.8rem;">
                            <div>• POWER: <strong style="color:var(--hologram-cyan);">100% Battery-Free</strong></div>
                            <div>• FREQUENCY: <strong style="color:#ffffff;">13.56 MHz</strong></div>
                            <div>• RESISTANCE: <strong style="color:#10b981;">5 ATM Waterproof</strong></div>
                        </div>
                    </div>
                </div>

                <!-- Bento 2: Sovereign Metal Cards (Span 4) -->
                <div class="bento-card span-4">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="telemetry-tag" style="color:var(--hologram-pink); border-color:rgba(247,37,133,0.3);">Artifact II • Tactile</span>
                            <span style="font-family:var(--font-mono); font-size:0.8rem; color:var(--text-dimmed);">28.5G SOLID</span>
                        </div>
                        <h3 style="margin-top: 1rem;">Sovereign 28.5g Metal Cards</h3>
                        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.5rem;">
                            CNC-machined solid Grade-5 titanium and 24K mirror-gold credit cards with custom laser engraved chip contact geometry.
                        </p>

                        <div class="bento-media-box">
                            <img src="assets/images/portfolio-4.png" alt="Sovereign Titanium Card">
                        </div>

                        <div style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-secondary);">
                            <div>• WEIGHT: <strong style="color:#ffffff;">28.5 Grams</strong></div>
                            <div>• CORE: <strong style="color:var(--hologram-pink);">JavaCard CC EAL6+</strong></div>
                        </div>
                    </div>
                </div>

                <!-- Bento 3: Municipal City Transit Cards (Span 4) -->
                <div class="bento-card span-4">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="telemetry-tag" style="color:#38bdf8; border-color:rgba(56,189,248,0.3);">Transit NFC</span>
                            <span style="font-family:var(--font-mono); font-size:0.8rem; color:var(--text-dimmed);">&lt;100MS GATE</span>
                        </div>
                        <h3 style="margin-top: 1rem;">Smart City Transit Cards</h3>
                        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.5rem;">
                            High-throughput contactless fare ticketing for subways, bus transit, and unified municipal resident cards with Calypso & MIFARE.
                        </p>

                        <div class="bento-media-box">
                            <img src="assets/images/transportcards.png" alt="Transport & City Cards">
                        </div>

                        <div style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-secondary);">
                            <div>• STANDARD: <strong style="color:#38bdf8;">Calypso / DESFire EV3</strong></div>
                            <div>• BODY: <strong style="color:#10b981;">Bio-PVC Ocean Plastic</strong></div>
                        </div>
                    </div>
                </div>

                <!-- Bento 4: Super NFC 5G SIM & Telecom (Span 4) -->
                <div class="bento-card span-4">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="telemetry-tag" style="color:#a855f7; border-color:rgba(168,85,247,0.3);">5G Telecom</span>
                            <span style="font-family:var(--font-mono); font-size:0.8rem; color:var(--text-dimmed);">SUPER SIM</span>
                        </div>
                        <h3 style="margin-top: 1rem;">Super NFC 5G SIM Cards</h3>
                        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.5rem;">
                            Multi-tenant secure element integrating 5G cellular credentials, bank payment applets, transit tokens, and e-ID on a single SIM.
                        </p>

                        <div class="bento-media-box">
                            <img src="assets/images/supersim.png" alt="Super NFC 5G SIM">
                        </div>

                        <div style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-secondary);">
                            <div>• SPEED: <strong style="color:#a855f7;">5G Standalone (SA)</strong></div>
                            <div>• SECURITY: <strong style="color:#ffffff;">GSMA Multi-Applet</strong></div>
                        </div>
                    </div>
                </div>

                <!-- Bento 5: Custom Chip Modules & Banking POS (Span 4) -->
                <div class="bento-card span-4">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="telemetry-tag" style="color:#f59e0b; border-color:rgba(245,158,11,0.3);">Hardware & Chips</span>
                            <span style="font-family:var(--font-mono); font-size:0.8rem; color:var(--text-dimmed);">POS / EMBOSS</span>
                        </div>
                        <h3 style="margin-top: 1rem;">Custom Chips & POS Hardware</h3>
                        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.5rem;">
                            Custom laser-engraved chip contact plates, Android smart POS terminals, and cryptographic HSM modules.
                        </p>

                        <div class="bento-media-box">
                            <img src="assets/images/customize-chip.png" alt="Custom Chip Modules & POS">
                        </div>

                        <div style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-secondary);">
                            <div>• PLATING: <strong style="color:#f59e0b;">24K Gold Mirror Finish</strong></div>
                            <div>• POS: <strong style="color:#ffffff;">PCI PTS 6.x Certified</strong></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Real-Time Cryptographic NFC Transit & POS Simulator -->
    <section class="section-spacing" id="simulator" style="background: rgba(0, 245, 212, 0.015);">
        <div class="container">
            <div style="text-align: center; max-width: 760px; margin: 0 auto 3rem auto;">
                <div class="telemetry-tag">Interactive Hardware Simulator</div>
                <h2 style="margin-top: 0.5rem;">Contactless NFC Handshake Emulator</h2>
                <p style="color: var(--text-secondary); font-size: 1.05rem; margin-top: 0.75rem;">
                    Test the sub-50ms cryptographic handshake between a GenTech wearable or card and a POS terminal in real time with synthesized haptics.
                </p>
            </div>

            <div style="background: var(--bg-bento); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: clamp(2rem, 4vw, 3.5rem); box-shadow: var(--shadow-bento);">
                <div style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 3rem; align-items: center;">
                    <div>
                        <span style="font-family:var(--font-mono); font-size:0.8rem; color:var(--hologram-cyan); text-transform:uppercase;">Select Test Hardware:</span>
                        <h3 style="margin: 0.75rem 0 1.5rem 0;">Initiate High-Speed Contactless Tap</h3>
                        <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 2rem;">
                            <button class="btn-cyber-primary sim-tap-btn" data-device="Apex Smart Ring">
                                <span>💍 Tap Apex Ring (NFC)</span>
                            </button>
                            <button class="btn-cyber-glass sim-tap-btn" data-device="Sovereign Titanium Card">
                                <span>💳 Tap Sovereign Card (EMV)</span>
                            </button>
                        </div>
                        <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--text-secondary); line-height: 1.8;">
                            <div>• CARRIER WAVE: <strong style="color:#ffffff;">13.56 MHz (ISO 14443A)</strong></div>
                            <div>• POWER SOURCE: <strong style="color:var(--hologram-cyan);">100% Passive Inductive RF</strong></div>
                            <div>• HANDSHAKE LATENCY: <strong style="color:#10b981;">&lt;42 Milliseconds</strong></div>
                        </div>
                    </div>

                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                            <div style="display: flex; align-items: center;">
                                <span class="terminal-status-dot" id="terminalStatusLed"></span>
                                <strong style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-secondary);">GTX-900 TRANSIT TERMINAL</strong>
                            </div>
                            <span id="gateStatusBadge" style="font-family: var(--font-mono); font-size: 0.8rem; font-weight: bold; color: var(--text-dimmed);">STANDBY</span>
                        </div>
                        <div class="nfc-terminal-hud" id="terminalLogScreen">
                            <div style="color: #64748b;">[STANDBY] Waiting for 13.56 MHz contactless target...</div>
                            <div style="color: #64748b;">[TIP] Click one of the buttons on the left to initiate transaction.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Institutional B2B Bank Client Portal Console -->
    <section class="section-spacing" id="portal">
        <div class="container">
            <div style="text-align: center; max-width: 760px; margin: 0 auto 3rem auto;">
                <div class="telemetry-tag" style="color:var(--hologram-pink); border-color:rgba(247,37,133,0.3);">B2B Client Console</div>
                <h2 style="margin-top: 0.5rem;">Live Bank Issuance Tracker</h2>
                <p style="color: var(--text-secondary); font-size: 1.05rem; margin-top: 0.75rem;">
                    Institutional bank partners can monitor active production batches, verify cryptographic key injection, and preview vector artwork in 3D.
                </p>
            </div>

            <div style="background: var(--bg-bento); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: clamp(2rem, 4vw, 3.5rem); box-shadow: var(--shadow-bento);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; flex-wrap: wrap; gap: 1rem;">
                    <div style="display: flex; gap: 0.6rem; flex-wrap: wrap;">
                        <button class="bank-select-btn active" data-bank="enbd" style="padding:0.45rem 1rem; border-radius:var(--radius-full); background:var(--bg-bento-elevated); border:1px solid var(--border-active); font-size:0.8rem; font-weight:700; color:var(--hologram-cyan);">Emirates NBD</button>
                        <button class="bank-select-btn" data-bank="fab" style="padding:0.45rem 1rem; border-radius:var(--radius-full); background:var(--bg-bento-elevated); border:1px solid var(--border-subtle); font-size:0.8rem; font-weight:700; color:var(--text-secondary);">First Abu Dhabi Bank (FAB)</button>
                        <button class="bank-select-btn" data-bank="sc" style="padding:0.45rem 1rem; border-radius:var(--radius-full); background:var(--bg-bento-elevated); border:1px solid var(--border-subtle); font-size:0.8rem; font-weight:700; color:var(--text-secondary);">Standard Chartered</button>
                        <button class="bank-select-btn" data-bank="revolut" style="padding:0.45rem 1rem; border-radius:var(--radius-full); background:var(--bg-bento-elevated); border:1px solid var(--border-subtle); font-size:0.8rem; font-weight:700; color:var(--text-secondary);">Revolut ME</button>
                    </div>
                    <div style="font-family: var(--font-mono); font-size: 0.8rem; color: #10b981;">
                        ● DUBAI CLEANROOM: ONLINE (RAK ZONE)
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1.4fr 0.8fr; gap: 2.5rem;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                            <h4 id="portalBankName" style="font-size: 1.25rem;">Emirates NBD • Private Wealth</h4>
                            <span class="telemetry-tag" id="portalBatchNumber">PO-GT-9482</span>
                        </div>
                        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1.5rem;">
                            Order Scope: <strong id="portalActiveVolume" style="color:#ffffff;">50,000 Cards (24K Gold Plated Titanium)</strong>
                        </p>

                        <div class="bank-pipeline-row done">
                            <div><strong>1. CNC Monolith Titanium Milling</strong><br><small style="color:var(--text-secondary);">Sub-micron 28.5g weight calibration</small></div>
                            <span style="color:#10b981; font-weight:bold;">✓ 100% Done</span>
                        </div>
                        <div class="bank-pipeline-row done">
                            <div><strong>2. 24K Sputter & Prelam Antenna Bonding</strong><br><small style="color:var(--text-secondary);">Dual-interface inductive copper coil</small></div>
                            <span style="color:#10b981; font-weight:bold;">✓ 100% Done</span>
                        </div>
                        <div class="bank-pipeline-row active">
                            <div><strong style="color:var(--hologram-cyan);">3. CC EAL6+ Cryptographic Key Injection</strong><br><small style="color:var(--text-secondary);">JavaCard applet flash & laser serialization</small></div>
                            <span style="color:var(--hologram-cyan); font-weight:bold;">⚡ 84% In Progress</span>
                        </div>
                        <div class="bank-pipeline-row">
                            <div><strong>4. EMVCo & PCI-DSS Final Optical QC</strong><br><small style="color:var(--text-secondary);">Magnetic stripe & chip verify</small></div>
                            <span style="color:var(--text-dimmed);">Queued</span>
                        </div>
                    </div>

                    <div style="background: var(--bg-bento-elevated); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.75rem; display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <h4 style="font-size: 1.1rem; margin-bottom: 1rem;">Vector Soft-Proof Studio</h4>
                            <div style="border: 2px dashed rgba(0,245,212,0.3); border-radius: var(--radius-sm); padding: 2rem 1rem; text-align: center; margin-bottom: 1.5rem; background: rgba(0,0,0,0.3);">
                                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin:0 auto 0.5rem auto; color:var(--hologram-cyan);"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
                                <strong style="font-size:0.85rem; display:block;">Drop Bank Vector (.SVG / .AI)</strong>
                                <span style="font-size:0.75rem; color:var(--text-dimmed);">Instant GPU 3D Mesh Generation</span>
                            </div>
                        </div>
                        <button class="btn-cyber-primary" style="width: 100%; justify-content: center; font-size: 0.8rem;">
                            <span>Download Full Batch Audit Report (PDF)</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Live Laser Engraving Atelier -->
    <section class="section-spacing" id="atelier" style="background: rgba(255,255,255,0.01);">
        <div class="container">
            <div class="bento-card" style="padding: clamp(2rem, 4vw, 3.5rem);">
                <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 3rem; align-items: center;">
                    <div>
                        <div class="telemetry-tag">Sub-Micron Precision</div>
                        <h2 style="margin-top: 0.5rem;">Live Laser Engraving Studio</h2>
                        <p style="color: var(--text-secondary); margin: 0.75rem 0 1.5rem 0;">
                            Type any custom VIP cardholder name or crypto serial to watch the fiber laser scan across the titanium surface in real time.
                        </p>

                        <div style="margin-bottom: 1.5rem;">
                            <label style="font-family:var(--font-mono); font-size:0.8rem; text-transform:uppercase; color:var(--hologram-cyan); display:block; margin-bottom:0.5rem;">
                                Live Laser Engraving Text:
                            </label>
                            <input type="text" id="engravingTextInput" class="form-control-haute" placeholder="ALEXANDER VANCE" value="ALEXANDER VANCE" maxlength="28">
                        </div>

                        <div>
                            <label style="font-family:var(--font-mono); font-size:0.8rem; text-transform:uppercase; color:var(--text-dimmed); display:block; margin-bottom:0.5rem;">
                                Choose Precious Alloy:
                            </label>
                            <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                                <button class="swatch-btn active hud-btn" data-material="gold">24K Gold</button>
                                <button class="swatch-btn hud-btn" data-material="rosegold">Rose Gold</button>
                                <button class="swatch-btn hud-btn" data-material="titanium">Titanium</button>
                                <button class="swatch-btn hud-btn" data-material="obsidian">Obsidian DLC</button>
                            </div>
                        </div>
                    </div>

                    <div>
                        <div class="laser-card-preview">
                            <div class="laser-scanner-line"></div>
                            <img src="assets/images/portfolio-4.png" alt="Laser Engraving Titanium Card" style="max-height: 200px; filter: drop-shadow(0 10px 25px rgba(0,245,212,0.3));">
                            <div class="engraved-live-text" id="liveEngravedText">ALEXANDER VANCE</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 0.75rem; font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-dimmed);">
                            <span>FIBER LASER: 0.01mm</span>
                            <span style="color: var(--hologram-cyan);">DUBAI RAK PRODUCTION READY</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</main>

<!-- Footer -->
<footer class="cyber-footer">
    <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 2.5rem; border-bottom: 1px solid var(--border-subtle); flex-wrap: wrap; gap: 1.5rem;">
            <div>
                <div class="brand-name" style="font-size: 1.3rem;">GENTECH <span style="color:var(--hologram-cyan);">3</span></div>
                <p style="color: var(--text-secondary); font-size: 0.88rem; margin-top: 0.4rem;">
                    Autonomous FinTech & Hardware Platform • Ras Al Khaimah Economic Zone, Dubai, UAE.
                </p>
            </div>
            <div style="display: flex; gap: 1.5rem; font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-secondary); flex-wrap: wrap;">
                <span>🛡️ EMVCo</span>
                <span>🔒 PCI-DSS Level 1</span>
                <span>⚡ ISO 14443A</span>
                <span>📱 GSMA 5G</span>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 1.5rem; font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-dimmed); flex-wrap: wrap; gap: 1rem;">
            <div>&copy; 2025-2026 GENTECH GLOBAL LLC. All Rights Reserved.</div>
            <div style="color: var(--hologram-cyan);">GenTech 3 • Bento Hardware Platform Edition</div>
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

print("GenTech 3 complete overhaul finished successfully!")
