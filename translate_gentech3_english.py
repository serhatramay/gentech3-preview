import os
import zipfile

print("Translating GenTech 3 into prestigious, international English...")

english_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>GenTech 3 | Serene Alabaster Edition — Smart Rings & Titanium Metal Cards</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Three.js 3D WebGL Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <!-- Core Stylesheet -->
    <link rel="stylesheet" href="assets/css/style.css?v=6.0">
</head>
<body>

<!-- Serene Sticky Navigation -->
<header class="main-header">
    <div class="container">
        <nav class="main-nav">
            <a href="index.html" class="nav-brand">
                <div class="nav-brand-dot"></div>
                <span>GenTech</span>
            </a>

            <div class="nav-links">
                <a href="#overview" class="nav-link">Overview</a>
                <a href="#configurator" class="nav-link">Card Studio</a>
                <a href="#ecosystem" class="nav-link">Ecosystem</a>
                <a href="#weight" class="nav-link">Weight Specs</a>
                <a href="#inquire" class="nav-link">Contact</a>
            </div>

            <div style="display: flex; align-items: center; gap: 1rem;">
                <a href="#inquire" class="btn-primary" style="padding: 0.55rem 1.4rem; font-size: 0.82rem;">
                    <span>Inquire Fleet</span>
                </a>
            </div>
        </nav>
    </div>
</header>

<main id="overview">
    <!-- 1. Serene Hero Section -->
    <section class="hero-section">
        <div class="container">
            <div class="calm-tag">✦ Dubai Engineering Center • Pure Ceramic & Titanium</div>
            <h1 class="serif-title">
                Calm technology. <br>
                <span class="gradient-text">Substance in every touch.</span>
            </h1>
            <p style="font-size: clamp(1.1rem, 2vw, 1.3rem); color: var(--text-muted); max-width: 660px; margin: 1.25rem auto 2.25rem auto;">
                A serene synthesis of 28.5g solid titanium cards, battery-free zirconia ceramic smart rings, and sub-50ms municipal transit cards — engineered with whisper-quiet precision in Dubai.
            </p>

            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="#configurator" class="btn-primary">Design Your Card</a>
                <a href="#ecosystem" class="btn-secondary">Explore 6 Pillars</a>
            </div>

            <!-- 3D Studio Stage -->
            <div class="hero-3d-box">
                <div id="canvas3D"></div>
                <div class="studio-toolbar">
                    <button class="toolbar-btn active artifact-toggle-btn" data-artifact="card">💳 Titanium Card</button>
                    <button class="toolbar-btn artifact-toggle-btn" data-artifact="ring">💍 Smart Ring</button>
                </div>
            </div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">
                ✦ Rotate artifacts to inspect precision metallic light reflections
            </div>
        </div>
    </section>

    <!-- 2. BESPOKE CARD BUILDER (LIVE CONFIGURATOR) -->
    <section class="section-spacing configurator-section" id="configurator">
        <div class="container">
            <div style="text-align: center; max-width: 680px; margin: 0 auto;">
                <div class="calm-tag">Live Card Builder</div>
                <h2 class="serif-title">Design your bank's sovereign card.</h2>
                <p style="color: var(--text-muted); font-size: 1.05rem; margin-top: 0.5rem;">
                    Customize precious alloys, choose chip geometries, and preview live typography in real time.
                </p>
            </div>

            <div class="configurator-card">
                <div class="configurator-grid">
                    <!-- Left: Live Card Mockup -->
                    <div style="text-align: center;">
                        <div class="live-card-mockup ceramic" id="liveCardMockup">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div class="chip-graphic"></div>
                                <span style="font-family: var(--font-mono); font-size: 0.85rem; font-weight: 700; letter-spacing: 0.05em;">GENTECH</span>
                            </div>
                            <div style="text-align: left;">
                                <div style="font-size: 0.75rem; opacity: 0.6; text-transform: uppercase; letter-spacing: 0.05em;">CARDHOLDER</div>
                                <div id="mockupCardholder" style="font-size: 1.25rem; font-weight: 700; letter-spacing: 0.12em;">ALEXANDER VANCE</div>
                                <div id="mockupSerial" style="font-family: var(--font-mono); font-size: 0.78rem; opacity: 0.7; margin-top: 0.25rem;">GT-9482-2026</div>
                            </div>
                        </div>
                        <div style="margin-top: 1rem; font-size: 0.82rem; color: var(--text-muted);">
                            28.5g Solid Monolith • CC EAL6+ Certified
                        </div>
                    </div>

                    <!-- Right: Configurator Controls -->
                    <div>
                        <!-- Metal Alloy Selector -->
                        <div style="margin-bottom: 1.5rem;">
                            <label style="font-size:0.88rem; font-weight:600; display:block; margin-bottom:0.6rem;">Select Precious Metal Finish:</label>
                            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                                <button class="alloy-pill-btn active" data-alloy="ceramic">Pure Ceramic</button>
                                <button class="alloy-pill-btn" data-alloy="titanium">Pale Titanium</button>
                                <button class="alloy-pill-btn" data-alloy="champagne">Champagne Gold</button>
                                <button class="alloy-pill-btn" data-alloy="gold">24K Mirror Gold</button>
                            </div>
                        </div>

                        <!-- Cardholder Name Input -->
                        <div style="margin-bottom: 1.25rem;">
                            <label style="font-size:0.88rem; font-weight:600; display:block; margin-bottom:0.4rem;">Cardholder Name:</label>
                            <input type="text" id="configNameInput" class="form-input-clean" value="ALEXANDER VANCE" maxlength="26">
                        </div>

                        <!-- Batch Serial Input -->
                        <div style="margin-bottom: 1.75rem;">
                            <label style="font-size:0.88rem; font-weight:600; display:block; margin-bottom:0.4rem;">Batch Serial Number:</label>
                            <input type="text" id="configSerialInput" class="form-input-clean" value="GT-9482-2026" maxlength="20">
                        </div>

                        <button class="btn-primary" style="width: 100%; justify-content: center; padding: 0.95rem;">
                            <span>Request Fleet Production Quote</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Complete 6-Pillar Ecosystem Grid -->
    <section class="section-spacing" id="ecosystem">
        <div class="container">
            <div style="text-align: center; max-width: 720px; margin: 0 auto 3rem auto;">
                <div class="calm-tag">Complete Hardware Suite</div>
                <h2 class="serif-title">Refined instruments of exchange.</h2>
                <p style="color: var(--text-muted); font-size: 1.05rem; margin-top: 0.5rem;">
                    From bespoke private banking cards and smart rings to 5G Super SIMs and personalization hardware.
                </p>
            </div>

            <div class="eco-grid-6">
                <!-- 1 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--accent-sage); text-transform:uppercase;">Wearable Hardware</span>
                        <div class="eco-thumb"><img src="assets/images/wearable.png" alt="Apex Smart Rings & Wristbands"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Apex Smart Rings & Wristbands</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">100% battery-free passive RF resonance. IP68 50m waterproof zirconia ceramic body.</p>
                    </div>
                </div>

                <!-- 2 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--accent-gold); text-transform:uppercase;">Tactile Luxury</span>
                        <div class="eco-thumb"><img src="assets/images/portfolio-4.png" alt="Titanium Cards"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Sovereign 28.5g Titanium</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">Machined from single-billet Grade-5 titanium monoliths for private banking and VIP portfolios.</p>
                    </div>
                </div>

                <!-- 3 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--accent-blue); text-transform:uppercase;">Smart Cities</span>
                        <div class="eco-thumb"><img src="assets/images/transportcards.png" alt="Transit Cards"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Municipal Transit Cards</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">High-speed fare collection cards for subway and bus networks (&lt;42ms gate latency, Calypso & MIFARE).</p>
                    </div>
                </div>

                <!-- 4 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--text-dim); text-transform:uppercase;">5G Telecom</span>
                        <div class="eco-thumb"><img src="assets/images/supersim.png" alt="Super SIM"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Super NFC 5G SIM Cards</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">Unifies 5G cellular connectivity, banking payments, and municipal transit tokens on a single chip.</p>
                    </div>
                </div>

                <!-- 5 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--accent-gold); text-transform:uppercase;">Artisan Chips</span>
                        <div class="eco-thumb"><img src="assets/images/customize-chip.png" alt="Bespoke Chip Modules"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Bespoke Laser Chip Modules</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">Custom laser engraved contact geometries with 24K gold flash mirror plating.</p>
                    </div>
                </div>

                <!-- 6 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--text-dim); text-transform:uppercase;">Hardware & POS</span>
                        <div class="eco-thumb"><img src="assets/images/pos.png" alt="POS Terminals"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Personalization & POS Hardware</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">Turnkey desktop card embossers, thermal personalization printers, Android smart POS, and HSMs.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Weight Specs Comparator -->
    <section class="section-spacing" id="weight" style="background: var(--bg-secondary);">
        <div class="container">
            <div style="text-align: center; max-width: 680px; margin: 0 auto 3rem auto;">
                <div class="calm-tag">Physical Gravitas</div>
                <h2 class="serif-title">The unmistakable heft of quality.</h2>
                <p style="color: var(--text-muted); font-size: 1.05rem; margin-top: 0.5rem;">
                    The tactile difference between commercial plastic and solid titanium.
                </p>
            </div>

            <div class="comparator-row">
                <div class="comparator-card">
                    <span style="font-size:0.8rem; color:var(--text-dim); text-transform:uppercase; font-weight:600;">Commercial Plastic</span>
                    <div class="weight-display" style="color: #94a3b8;">5.0g</div>
                    <div style="font-size:0.9rem; font-weight:600; color:var(--text-muted); margin-bottom:1rem;">Standard PVC Plastic</div>
                    <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6;">Prone to flexing, edge splitting, and rapid surface wear.</p>
                </div>
                <div class="comparator-card">
                    <span style="font-size:0.8rem; color:var(--text-dim); text-transform:uppercase; font-weight:600;">Hybrid Metal Card</span>
                    <div class="weight-display" style="color: #64748b;">16.0g</div>
                    <div style="font-size:0.9rem; font-weight:600; color:var(--text-muted); margin-bottom:1rem;">Steel Veneer + Plastic Core</div>
                    <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6;">Thin metal veneer laminated over a synthetic plastic substrate.</p>
                </div>
                <div class="comparator-card featured">
                    <span style="font-size:0.8rem; color:var(--accent-gold); text-transform:uppercase; font-weight:700;">GenTech Sovereign</span>
                    <div class="weight-display gradient-text">28.5g</div>
                    <div style="font-size:0.9rem; font-weight:600; color:var(--accent-gold); margin-bottom:1rem;">100% Solid Grade-5 Titanium</div>
                    <p style="font-size:0.85rem; color:var(--text-main); font-weight:500;">Precision CNC milled from solid titanium monolith blocks, engineered for permanence.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Enterprise Inquiries -->
    <section class="section-spacing" id="inquire" style="text-align: center;">
        <div class="container">
            <div class="calm-tag">Private Banking & Institutional Fleet</div>
            <h2 class="serif-title">Commission your bank's fleet.</h2>
            <p style="color: var(--text-muted); font-size: 1.1rem; max-width: 620px; margin: 1rem auto 2.5rem auto;">
                Connect with our Dubai engineering desk to request material sample boxes and volume production schedules.
            </p>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="mailto:info@gentech.ae" class="btn-primary">Initiate Fleet Inquiry</a>
                <a href="tel:+971500000000" class="btn-secondary">Direct Dubai Desk</a>
            </div>
        </div>
    </section>
</main>

<footer class="footer-serene">
    <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-light); padding-bottom: 2rem; flex-wrap: wrap; gap: 1.5rem;">
            <div>
                <div style="font-size: 1.2rem; font-weight: 700; color: var(--text-main);">GenTech Global LLC</div>
                <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">
                    Ras Al Khaimah Economic Zone, Dubai, United Arab Emirates.
                </div>
            </div>
            <div style="display: flex; gap: 1.75rem; font-size: 0.82rem; font-weight: 600; color: var(--text-muted);">
                <span>EMVCo Certified</span>
                <span>PCI-DSS Level 1</span>
                <span>ISO 14443 Type A</span>
                <span>GSMA 5G</span>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 1.5rem; font-size: 0.82rem; color: var(--text-dim); flex-wrap: wrap; gap: 1rem;">
            <div>&copy; 2025-2026 GenTech Global LLC. All rights reserved.</div>
            <div>GenTech 3 • Serene Alabaster Edition</div>
        </div>
    </div>
</footer>

<!-- Scripts -->
<script src="assets/js/scene3d.js"></script>
<script src="assets/js/app.js"></script>
</body>
</html>
"""

with open('/Users/ramay/gentech3-app/index.html', 'w', encoding='utf-8') as f:
    f.write(english_html)

# Sync to WordPress Theme and Rebuild ZIP
wp_theme_dir = '/Users/ramay/gentech3-wp/gentech3-theme'
os.system(f"cp /Users/ramay/gentech3-app/index.html {wp_theme_dir}/front-page.php")
os.system(f"cp /Users/ramay/gentech3-app/index.html {wp_theme_dir}/index.php")

zip_path = '/Users/ramay/gentech3-wp/gentech3-modern-theme.zip'
if os.path.exists(zip_path):
    os.remove(zip_path)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(wp_theme_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(wp_theme_dir))
            zipf.write(file_path, arcname)

os.system(f"cp -r {wp_theme_dir}/* /Users/ramay/gentech-wp-instance/wp-content/themes/gentech3-theme/")
os.system("cp -r /Users/ramay/gentech3-app/* /Users/ramay/gentech3-lab/")

print("GenTech 3 is now 100% fluent, prestigious international English and synced everywhere!")
