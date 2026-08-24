import os

print("Creating the Apple / Revolut Ultra / Stripe Tier FinTech Flagship...")

# 1. CSS for Apple-Grade FinTech UI
css = """/* ==========================================================================
   GENTECH 3 - THE APPLE / REVOLUT ULTRA / STRIPE FINTECH FLAGSHIP
   Design Language: Cupertino Precision + London Ultra-Fintech + Nordic Minimalism
   ========================================================================== */

:root {
  --apple-black: #000000;
  --apple-dark-gray: #0d0d0f;
  --apple-card-surface: rgba(22, 22, 26, 0.7);
  --apple-glass: rgba(10, 10, 12, 0.8);
  
  --titanium-white: #f5f5f7;
  --titanium-silver: #d2d2d7;
  --titanium-dark: #86868b;
  --titanium-border: rgba(255, 255, 255, 0.12);
  
  --apple-blue: #2997ff;
  --apple-gold: #e3a857;
  --apple-emerald: #30d158;
  
  /* Apple Card Iridescent Holographic Sheen */
  --iridescent-sheen: linear-gradient(135deg, 
    #ff9a9e 0%, 
    #fecfef 20%, 
    #a1c4fd 40%, 
    #c2e9fb 60%, 
    #d4fc79 80%, 
    #96e6a1 100%);

  --font-sf: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', 'Plus Jakarta Sans', sans-serif;
  --font-mono: 'SF Mono', 'JetBrains Mono', Menlo, monospace;
  
  --radius-apple: 22px;
  --radius-pill: 980px;
  
  --shadow-apple: 0 30px 60px rgba(0, 0, 0, 0.6);
  --shadow-soft: 0 10px 30px rgba(0, 0, 0, 0.3);
  
  --ease-apple: cubic-bezier(0.16, 1, 0.3, 1);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
  background-color: var(--apple-black);
  color: var(--titanium-white);
  font-family: var(--font-sf);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  background-color: var(--apple-black);
  color: var(--titanium-white);
  line-height: 1.5;
  overflow-x: hidden;
}

/* Apple Pro Headings */
h1, h2, h3, h4 {
  font-family: var(--font-sf);
  letter-spacing: -0.035em;
  font-weight: 700;
  color: var(--titanium-white);
}

h1 {
  font-size: clamp(3rem, 7vw, 6.2rem);
  line-height: 1.02;
  font-weight: 800;
}

h2 {
  font-size: clamp(2.4rem, 5vw, 4.2rem);
  line-height: 1.08;
}

h3 {
  font-size: clamp(1.5rem, 3vw, 2.4rem);
  line-height: 1.2;
}

.subheadline {
  font-size: clamp(1.2rem, 2.2vw, 1.75rem);
  color: var(--titanium-dark);
  font-weight: 500;
  line-height: 1.4;
  letter-spacing: -0.015em;
}

.gradient-iridescent {
  background: var(--iridescent-sheen);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.gradient-silver {
  background: linear-gradient(180deg, #ffffff 0%, #a1a1a6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

a { color: inherit; text-decoration: none; }
button { cursor: pointer; border: none; background: none; font: inherit; }

.container {
  width: 100%;
  max-width: 1280px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 2rem;
  padding-right: 2rem;
}

.section-spacing {
  padding-top: clamp(6rem, 12vw, 12rem);
  padding-bottom: clamp(6rem, 12vw, 12rem);
}

/* --------------------------------------------------------------------------
   Apple Style Navigation Bar
   -------------------------------------------------------------------------- */
.apple-nav-blur {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 9999;
  background: var(--apple-glass);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  height: 52px;
  display: flex;
  align-items: center;
}

.apple-nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.apple-brand {
  font-weight: 700;
  font-size: 1.1rem;
  letter-spacing: -0.02em;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.apple-nav-menu {
  display: flex;
  gap: 2.5rem;
}

@media (max-width: 900px) {
  .apple-nav-menu { display: none; }
}

.apple-nav-link {
  font-size: 0.8rem;
  font-weight: 400;
  color: var(--titanium-silver);
  opacity: 0.8;
  transition: opacity 0.2s;
}

.apple-nav-link:hover {
  opacity: 1;
  color: #ffffff;
}

.btn-apple-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--apple-blue);
  color: #ffffff;
  font-size: 0.78rem;
  font-weight: 500;
  padding: 0.35rem 0.95rem;
  border-radius: var(--radius-pill);
  transition: all 0.2s;
}

.btn-apple-pill:hover {
  background: #0071e3;
  transform: scale(1.02);
}

.btn-apple-ghost {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  font-size: 0.95rem;
  font-weight: 500;
  padding: 0.85rem 1.85rem;
  border-radius: var(--radius-pill);
  border: 1px solid var(--titanium-border);
  transition: all 0.3s var(--ease-apple);
}

.btn-apple-ghost:hover {
  background: rgba(255, 255, 255, 0.18);
  border-color: rgba(255, 255, 255, 0.4);
}

.btn-apple-cta {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: #ffffff;
  color: #000000;
  font-size: 0.95rem;
  font-weight: 600;
  padding: 0.85rem 1.85rem;
  border-radius: var(--radius-pill);
  transition: all 0.3s var(--ease-apple);
}

.btn-apple-cta:hover {
  background: #e8e8ed;
  transform: scale(1.03);
}

/* --------------------------------------------------------------------------
   Hero Section: Apple Card 3D Tilt Experience
   -------------------------------------------------------------------------- */
.apple-hero {
  padding-top: 140px;
  padding-bottom: 80px;
  text-align: center;
  position: relative;
}

.apple-eyebrow {
  font-size: 0.95rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: var(--apple-blue);
  margin-bottom: 0.8rem;
}

.apple-3d-stage-box {
  width: 100%;
  max-width: 1050px;
  height: 520px;
  margin: 3.5rem auto 1.5rem auto;
  border-radius: var(--radius-apple);
  background: radial-gradient(circle at center, #151518 0%, #050507 80%);
  border: 1px solid var(--titanium-border);
  box-shadow: var(--shadow-apple);
  position: relative;
  overflow: hidden;
}

#canvas3D {
  width: 100%;
  height: 100%;
  display: block;
}

.apple-stage-controls {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 0.5rem;
  background: rgba(18, 18, 22, 0.85);
  backdrop-filter: blur(20px);
  padding: 0.35rem 0.5rem;
  border-radius: var(--radius-pill);
  border: 1px solid var(--titanium-border);
  z-index: 10;
}

.apple-chip-btn {
  padding: 0.4rem 1rem;
  border-radius: var(--radius-pill);
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--titanium-silver);
  transition: all 0.2s;
}

.apple-chip-btn.active {
  background: #ffffff;
  color: #000000;
  font-weight: 600;
}

/* --------------------------------------------------------------------------
   Apple Style Showcase Cards (Apple Card / Watch / Ultra Style)
   -------------------------------------------------------------------------- */
.apple-cards-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-top: 4rem;
}

@media (max-width: 900px) {
  .apple-cards-grid { grid-template-columns: 1fr; }
}

.apple-feature-tile {
  background: var(--apple-dark-gray);
  border-radius: var(--radius-apple);
  border: 1px solid var(--titanium-border);
  padding: clamp(2.5rem, 5vw, 4rem);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
  min-height: 520px;
  transition: all 0.4s var(--ease-apple);
}

.apple-feature-tile:hover {
  border-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-4px);
}

.apple-tile-media {
  height: 240px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 2rem 0;
}

.apple-tile-media img {
  max-height: 200px;
  object-fit: contain;
  filter: drop-shadow(0 20px 40px rgba(0, 0, 0, 0.8));
  transition: transform 0.6s var(--ease-apple);
}

.apple-feature-tile:hover .apple-tile-media img {
  transform: scale(1.08);
}

/* --------------------------------------------------------------------------
   Apple Card Weight & Haptic Tactile Comparison
   -------------------------------------------------------------------------- */
.weight-comparator-section {
  background: #08080a;
  border-top: 1px solid var(--titanium-border);
  border-bottom: 1px solid var(--titanium-border);
}

.comparator-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 3.5rem;
}

@media (max-width: 900px) {
  .comparator-grid { grid-template-columns: 1fr; }
}

.comparator-box {
  background: rgba(22, 22, 26, 0.5);
  border: 1px solid var(--titanium-border);
  border-radius: var(--radius-apple);
  padding: 2.5rem 2rem;
  text-align: center;
  transition: all 0.3s;
}

.comparator-box.highlight {
  border-color: var(--apple-blue);
  background: radial-gradient(circle at top, rgba(41, 151, 255, 0.1) 0%, rgba(22, 22, 26, 0.8) 100%);
  box-shadow: 0 0 35px rgba(41, 151, 255, 0.15);
}

.weight-number {
  font-size: 3.8rem;
  font-weight: 800;
  letter-spacing: -0.04em;
  margin: 1rem 0 0.5rem 0;
  line-height: 1;
}

/* --------------------------------------------------------------------------
   Live Laser Atelier & Material Picker (Apple Studio Style)
   -------------------------------------------------------------------------- */
.material-picker-bar {
  display: flex;
  justify-content: center;
  gap: 1.25rem;
  margin: 2rem 0;
}

.material-orb-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--titanium-dark);
  transition: all 0.2s;
}

.material-orb {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 2px solid transparent;
  transition: all 0.2s;
}

.material-orb-btn.active .material-orb {
  border-color: #ffffff;
  transform: scale(1.15);
}

.material-orb-btn.active {
  color: #ffffff;
  font-weight: 600;
}

/* Apple Footer */
.apple-footer {
  background: #000000;
  padding: 4rem 0;
  font-size: 0.78rem;
  color: var(--titanium-dark);
  border-top: 1px solid var(--titanium-border);
}
"""

with open('/Users/ramay/gentech3-app/assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Write HTML with Apple / Stripe aesthetic
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>GenTech | Titanium Cards, Smart Rings & Autonomous FinTech</title>
    
    <!-- Apple SF Pro Font Fallbacks + Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Three.js 3D WebGL Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <!-- Core Stylesheet -->
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<!-- Apple Style Sticky Top Bar -->
<header class="apple-nav-blur">
    <div class="container">
        <div class="apple-nav-inner">
            <a href="index.html" class="apple-brand">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                <span>GenTech</span>
            </a>

            <div class="apple-nav-menu">
                <a href="#hero" class="apple-nav-link">Overview</a>
                <a href="#cards" class="apple-nav-link">Sovereign Card</a>
                <a href="#ring" class="apple-nav-link">Apex Ring</a>
                <a href="#transit" class="apple-nav-link">Transit & Super SIM</a>
                <a href="#compare" class="apple-nav-link">Weight Specs</a>
                <a href="#atelier" class="apple-nav-link">Studio</a>
            </div>

            <div style="display: flex; align-items: center; gap: 1rem;">
                <button id="soundToggleBtn" style="font-size: 0.75rem; color: #86868b; padding: 0.2rem 0.6rem; border-radius: var(--radius-pill); border: 1px solid var(--titanium-border);">
                    🔊 Haptics: ON
                </button>
                <a href="#inquire" class="btn-apple-pill">Request Fleet</a>
            </div>
        </div>
    </div>
</header>

<main id="hero">
    <!-- 1. Apple Hero Section -->
    <section class="apple-hero">
        <div class="container">
            <div class="apple-eyebrow">The New Titanium Standard</div>
            <h1>
                Titanium. In a class <br>
                <span class="gradient-silver">of its own.</span>
            </h1>
            <p class="subheadline" style="max-width: 680px; margin: 1.25rem auto 2.5rem auto;">
                A solid 28.5g Grade-5 titanium monolith credit card and a 100% battery-free smart payment ring. Precision engineered in Dubai for sovereign wealth and Tier-1 banks.
            </p>

            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="#atelier" class="btn-apple-cta">Configure in Studio</a>
                <a href="#cards" class="btn-apple-ghost">Explore Engineering</a>
            </div>

            <!-- Apple 3D Stage Box -->
            <div class="apple-3d-stage-box">
                <div id="canvas3D"></div>
                <div class="apple-stage-controls">
                    <button class="apple-chip-btn active artifact-toggle-btn" data-artifact="both">Both Artifacts</button>
                    <button class="apple-chip-btn artifact-toggle-btn" data-artifact="ring">Apex Ring</button>
                    <button class="apple-chip-btn artifact-toggle-btn" data-artifact="card">Sovereign Card</button>
                    <button class="apple-chip-btn" id="explodedViewBtn">Exploded X-Ray</button>
                </div>
            </div>
            <div style="font-size: 0.8rem; color: var(--titanium-dark); margin-top: 0.5rem;">
                Drag to rotate in real-time 3D • Sub-micron laser chamfered edges
            </div>
        </div>
    </section>

    <!-- 2. The Dual Flagship Showcase (Apple Pro Style Cards) -->
    <section class="section-spacing" id="cards">
        <div class="container">
            <div style="text-align: center; max-width: 700px; margin: 0 auto 3rem auto;">
                <div class="apple-eyebrow">Flagship Hardware</div>
                <h2>Substance you can feel.</h2>
                <p class="subheadline" style="margin-top: 0.75rem;">
                    Every curve, chamfer, and conductive trace is calibrated to redefine how value is transacted.
                </p>
            </div>

            <div class="apple-cards-grid">
                <!-- Tile 1: Sovereign Card -->
                <div class="apple-feature-tile">
                    <div>
                        <span style="font-size:0.8rem; font-weight:600; color:var(--titanium-dark); text-transform:uppercase; letter-spacing:0.05em;">Artifact I</span>
                        <h3 style="margin-top: 0.5rem;">Sovereign Metal Card</h3>
                        <p style="color: var(--titanium-silver); margin-top: 0.5rem; font-size: 1rem; line-height: 1.6;">
                            Machined from a single block of aerospace Grade-5 titanium. At 28.5 grams, it delivers unmatched physical gravitas in every transaction.
                        </p>
                    </div>

                    <div class="apple-tile-media">
                        <img src="assets/images/portfolio-4.png" alt="Sovereign Titanium Card">
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: flex-end; border-top: 1px solid var(--titanium-border); padding-top: 1.5rem;">
                        <div>
                            <div style="font-size: 1.6rem; font-weight: 700;">28.5g</div>
                            <div style="font-size: 0.75rem; color: var(--titanium-dark);">Solid Ti-6Al-4V</div>
                        </div>
                        <div>
                            <div style="font-size: 1.6rem; font-weight: 700; color:var(--apple-blue);">CC EAL6+</div>
                            <div style="font-size: 0.75rem; color: var(--titanium-dark);">Secure Element</div>
                        </div>
                        <div>
                            <div style="font-size: 1.6rem; font-weight: 700;">24K Gold</div>
                            <div style="font-size: 0.75rem; color: var(--titanium-dark);">Chip Plating</div>
                        </div>
                    </div>
                </div>

                <!-- Tile 2: Apex Smart Ring -->
                <div class="apple-feature-tile" id="ring">
                    <div>
                        <span style="font-size:0.8rem; font-weight:600; color:var(--titanium-dark); text-transform:uppercase; letter-spacing:0.05em;">Artifact II</span>
                        <h3 style="margin-top: 0.5rem;">Apex Smart Ring</h3>
                        <p style="color: var(--titanium-silver); margin-top: 0.5rem; font-size: 1rem; line-height: 1.6;">
                            Zero charging cords. Zero batteries. Engineered with passive inductive NFC resonance that draws power directly from payment terminals.
                        </p>
                    </div>

                    <div class="apple-tile-media">
                        <img src="assets/images/wearable.png" alt="Apex Smart Rings & Wristbands">
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: flex-end; border-top: 1px solid var(--titanium-border); padding-top: 1.5rem;">
                        <div>
                            <div style="font-size: 1.6rem; font-weight: 700; color:var(--apple-emerald);">0% Battery</div>
                            <div style="font-size: 0.75rem; color: var(--titanium-dark);">Infinite Lifecycle</div>
                        </div>
                        <div>
                            <div style="font-size: 1.6rem; font-weight: 700;">50m</div>
                            <div style="font-size: 0.75rem; color: var(--titanium-dark);">IP68 Water Resistance</div>
                        </div>
                        <div>
                            <div style="font-size: 1.6rem; font-weight: 700;">13.56 MHz</div>
                            <div style="font-size: 0.75rem; color: var(--titanium-dark);">RF Carrier</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Apple Weight & Heft Comparison Matrix -->
    <section class="section-spacing weight-comparator-section" id="compare">
        <div class="container">
            <div style="text-align: center; max-width: 700px; margin: 0 auto;">
                <div class="apple-eyebrow">Gravitas & Engineering</div>
                <h2>A tactile difference you feel instantly.</h2>
                <p class="subheadline" style="margin-top: 0.75rem;">
                    Compare standard commercial cards against the GenTech Sovereign Titanium monolith.
                </p>
            </div>

            <div class="comparator-grid">
                <!-- Standard Plastic -->
                <div class="comparator-box">
                    <div style="font-size:0.85rem; color:var(--titanium-dark); font-weight:600; text-transform:uppercase;">Standard Bank Card</div>
                    <div class="weight-number" style="color: #636366;">5.0g</div>
                    <div style="font-size:0.9rem; color:var(--titanium-dark); margin-bottom: 1.5rem;">Generic PVC Plastic</div>
                    <p style="font-size:0.85rem; color:var(--titanium-dark); line-height:1.6;">
                        Easily bends, scratches within weeks, and ends up in ocean landfills.
                    </p>
                </div>

                <!-- Veneer Metal -->
                <div class="comparator-box">
                    <div style="font-size:0.85rem; color:var(--titanium-dark); font-weight:600; text-transform:uppercase;">Hybrid Metal Veneer</div>
                    <div class="weight-number" style="color: #a1a1a6;">16.0g</div>
                    <div style="font-size:0.9rem; color:var(--titanium-dark); margin-bottom: 1.5rem;">Thin Steel + PVC Backing</div>
                    <p style="font-size:0.85rem; color:var(--titanium-dark); line-height:1.6;">
                        Partial metal feel with plastic core prone to edge delamination over time.
                    </p>
                </div>

                <!-- GenTech Sovereign -->
                <div class="comparator-box highlight">
                    <div style="font-size:0.85rem; color:var(--apple-blue); font-weight:700; text-transform:uppercase;">GenTech Sovereign</div>
                    <div class="weight-number gradient-silver">28.5g</div>
                    <div style="font-size:0.9rem; color:var(--apple-blue); font-weight:600; margin-bottom: 1.5rem;">100% Solid Grade-5 Titanium</div>
                    <p style="font-size:0.85rem; color:var(--titanium-silver); line-height:1.6;">
                        Machined monolith billet, 24K gold sputter, laser serialized, indestructible.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Smart City Transit & 5G Super SIM -->
    <section class="section-spacing" id="transit">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
                <div>
                    <div class="apple-eyebrow">Smart Cities & Telecommunications</div>
                    <h2>Subway gates at the speed of thought.</h2>
                    <p class="subheadline" style="font-size: 1.15rem; margin: 1.25rem 0 2rem 0;">
                        GenTech transit cards clear turnstiles in under 42 milliseconds. Paired with our 5G Super SIM, users hold cellular subscription, banking credentials, and metro ticketing in a single secure chip.
                    </p>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; border-top: 1px solid var(--titanium-border); padding-top: 1.5rem;">
                        <div>
                            <div style="font-size: 1.8rem; font-weight: 700; color:var(--apple-blue);">&lt;42 ms</div>
                            <div style="font-size: 0.8rem; color:var(--titanium-dark);">Gate Authentication</div>
                        </div>
                        <div>
                            <div style="font-size: 1.8rem; font-weight: 700; color:var(--apple-emerald);">5G GSMA</div>
                            <div style="font-size: 0.8rem; color:var(--titanium-dark);">Multi-Applet SIM</div>
                        </div>
                    </div>
                </div>

                <div style="background: var(--apple-dark-gray); border: 1px solid var(--titanium-border); border-radius: var(--radius-apple); padding: 2.5rem; display: flex; flex-direction: column; align-items: center;">
                    <img src="assets/images/transportcards.png" alt="Smart City Transit Cards" style="max-height: 180px; object-fit: contain; filter: drop-shadow(0 15px 30px rgba(0,0,0,0.8)); margin-bottom: 2rem;">
                    <img src="assets/images/supersim.png" alt="Super NFC 5G SIM" style="max-height: 140px; object-fit: contain; filter: drop-shadow(0 15px 30px rgba(0,0,0,0.8));">
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Apple Studio Laser Engraving Atelier -->
    <section class="section-spacing" id="atelier" style="background: #050507;">
        <div class="container">
            <div style="text-align: center; max-width: 700px; margin: 0 auto 3rem auto;">
                <div class="apple-eyebrow">GenTech Studio</div>
                <h2>Make it unmistakably yours.</h2>
                <p class="subheadline" style="margin-top: 0.75rem;">
                    Personalize your bank's fleet with sub-micron fiber laser typography and precious alloy finishes.
                </p>

                <!-- Material Picker Orb Bar -->
                <div class="material-picker-bar">
                    <button class="material-orb-btn active swatch-btn" data-material="gold">
                        <div class="material-orb" style="background: linear-gradient(135deg, #f6e27a, #aa7c11);"></div>
                        <span>24K Gold</span>
                    </button>
                    <button class="material-orb-btn swatch-btn" data-material="rosegold">
                        <div class="material-orb" style="background: linear-gradient(135deg, #f7d6c8, #8c5332);"></div>
                        <span>Rose Gold</span>
                    </button>
                    <button class="material-orb-btn swatch-btn" data-material="titanium">
                        <div class="material-orb" style="background: linear-gradient(135deg, #ffffff, #86868b);"></div>
                        <span>Titanium</span>
                    </button>
                    <button class="material-orb-btn swatch-btn" data-material="obsidian">
                        <div class="material-orb" style="background: linear-gradient(135deg, #1d1d1f, #000000); border: 1px solid #2997ff;"></div>
                        <span>Space Black</span>
                    </button>
                </div>
            </div>

            <div style="max-width: 780px; margin: 0 auto; background: var(--apple-dark-gray); border: 1px solid var(--titanium-border); border-radius: var(--radius-apple); padding: clamp(2rem, 4vw, 3.5rem);">
                <div style="margin-bottom: 2rem;">
                    <label style="font-size:0.85rem; color:var(--titanium-silver); display:block; margin-bottom:0.6rem; font-weight:500;">
                        Type Name or Serial to Inscribe:
                    </label>
                    <input type="text" id="engravingTextInput" style="width: 100%; padding: 0.95rem 1.25rem; background: #000000; border: 1px solid var(--titanium-border); border-radius: 12px; color: #ffffff; font-size: 1rem;" placeholder="ALEXANDER VANCE" value="ALEXANDER VANCE" maxlength="28">
                </div>

                <div style="position: relative; height: 260px; background: #000000; border-radius: 16px; border: 1px solid var(--titanium-border); display: flex; align-items: center; justify-content: center; overflow: hidden;">
                    <div class="laser-beam"></div>
                    <img src="assets/images/portfolio-4.png" alt="Engraved Titanium Card" style="max-height: 200px; filter: drop-shadow(0 15px 35px rgba(255,255,255,0.1));">
                    <div id="liveEngravedText" style="position: absolute; bottom: 25px; right: 35px; font-family: var(--font-sf); font-size: 1.1rem; letter-spacing: 0.18em; color: #f5f5f7; text-shadow: 0 0 10px rgba(255,255,255,0.8); text-transform: uppercase;">
                        ALEXANDER VANCE
                    </div>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1.25rem; font-size: 0.8rem; color: var(--titanium-dark);">
                    <span>Fiber Laser Precision: 0.01mm</span>
                    <span style="color: var(--apple-blue);">Dubai RAK Production Hub</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. Enterprise Requisition (Apple B2B Style) -->
    <section class="section-spacing" id="inquire" style="text-align: center;">
        <div class="container">
            <div class="apple-eyebrow">Institutional Partnership</div>
            <h2>Equip your private banking fleet.</h2>
            <p class="subheadline" style="max-width: 620px; margin: 1.25rem auto 2.5rem auto;">
                Connect with our Dubai engineering team for custom samples, pre-personalization key injection, and turnkey volume production.
            </p>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="mailto:info@gentech.ae" class="btn-apple-cta">Initiate Consultation</a>
                <a href="tel:+971500000000" class="btn-apple-ghost">Call Dubai Desk</a>
            </div>
        </div>
    </section>
</main>

<!-- Apple Style Minimalist Footer -->
<footer class="apple-footer">
    <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--titanium-border); padding-bottom: 2rem; flex-wrap: wrap; gap: 1.5rem;">
            <div style="font-weight: 600; color: #ffffff; font-size: 0.95rem;">GenTech Global LLC • Dubai</div>
            <div style="display: flex; gap: 2rem; color: var(--titanium-silver);">
                <span>EMVCo Level 1 & 2</span>
                <span>PCI-DSS Compliant</span>
                <span>ISO 14443 Type A</span>
                <span>GSMA 5G Certified</span>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 1.5rem; flex-wrap: wrap; gap: 1rem;">
            <div>Copyright &copy; 2025-2026 GenTech Global LLC. All rights reserved. Mastered in Dubai, UAE.</div>
            <div>Apple-Grade FinTech Edition (GenTech 3)</div>
        </div>
    </div>
</footer>

<!-- Scripts -->
<script src="assets/js/audio.js"></script>
<script src="assets/js/scene3d.js"></script>
<script src="assets/js/app.js"></script>
</body>
</html>
"""

with open('/Users/ramay/gentech3-app/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Apple-grade FinTech Flagship built successfully!")
