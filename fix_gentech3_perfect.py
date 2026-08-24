import os
import zipfile

print("Fixing and assembling pixel-perfect GenTech 3...")

# Complete, Self-Contained, Bulletproof CSS
complete_css = """/* ==========================================================================
   GENTECH 3 - SERENE ALABASTER & PURE CERAMIC (PIXEL PERFECT EDITION)
   ========================================================================== */

:root {
  --bg-primary: #fbfbfc;
  --bg-secondary: #f4f4f7;
  --bg-card: #ffffff;
  --bg-glass: rgba(255, 255, 255, 0.92);
  
  --text-main: #0f172a;
  --text-muted: #64748b;
  --text-dim: #94a3b8;
  
  --accent-gold: #b38b4d;
  --accent-champagne: #c5a880;
  --accent-sage: #3f6e5c;
  --accent-blue: #2563eb;
  
  --border-light: rgba(0, 0, 0, 0.07);
  --border-focus: rgba(0, 0, 0, 0.15);
  --border-gold: rgba(179, 139, 77, 0.35);
  
  --font-serif: 'Playfair Display', Georgia, serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  
  --radius-sm: 12px;
  --radius-md: 20px;
  --radius-lg: 32px;
  --radius-full: 9999px;
  
  --shadow-soft: 0 10px 30px -10px rgba(0, 0, 0, 0.05);
  --shadow-card: 0 20px 45px -15px rgba(0, 0, 0, 0.07);
  --shadow-float: 0 30px 60px -20px rgba(0, 0, 0, 0.09);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
  background-color: var(--bg-primary);
  color: var(--text-main);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
}

body {
  background-color: var(--bg-primary);
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
    radial-gradient(circle at 12% 18%, rgba(197, 168, 128, 0.06) 0%, transparent 45%),
    radial-gradient(circle at 88% 82%, rgba(63, 110, 92, 0.04) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}

h1, h2, h3, h4 {
  color: var(--text-main);
  font-weight: 600;
  letter-spacing: -0.025em;
  line-height: 1.15;
}

h1 { font-size: clamp(2.8rem, 5.5vw, 4.8rem); font-weight: 700; }
h2 { font-size: clamp(2.2rem, 3.8vw, 3.2rem); }
h3 { font-size: clamp(1.35rem, 2.2vw, 1.85rem); }

.serif-title {
  font-family: var(--font-serif);
  font-weight: 500;
  letter-spacing: -0.01em;
}

.gradient-text {
  background: linear-gradient(135deg, #0f172a 0%, #8d7b68 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

a { color: inherit; text-decoration: none; }
button { cursor: pointer; border: none; background: none; font: inherit; color: inherit; }
img { max-width: 100%; height: auto; display: block; }

.container {
  width: 100%;
  max-width: 1260px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 2rem;
  padding-right: 2rem;
  position: relative;
  z-index: 1;
}

.section-spacing {
  padding-top: clamp(5.5rem, 9vw, 9rem);
  padding-bottom: clamp(5.5rem, 9vw, 9rem);
}

.calm-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 1.1rem;
  border-radius: var(--radius-full);
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  background: rgba(179, 139, 77, 0.12);
  color: var(--accent-gold);
  border: 1px solid rgba(179, 139, 77, 0.25);
  margin-bottom: 1.5rem;
}

/* Header & Nav */
.main-header, .serene-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background: var(--bg-glass);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-light);
}

.main-nav, .serene-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 84px;
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.25rem;
  font-weight: 700;
}

.nav-brand-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--accent-gold);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 2.25rem;
}

@media (max-width: 900px) {
  .nav-links { display: none; }
}

.nav-link {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text-muted);
  transition: color 0.2s;
}

.nav-link:hover { color: var(--text-main); }

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.8rem 1.8rem;
  border-radius: var(--radius-full);
  background: var(--text-main);
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
  transition: all 0.3s;
}

.btn-primary:hover {
  background: #1e293b;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.8rem 1.8rem;
  border-radius: var(--radius-full);
  background: #ffffff;
  border: 1px solid var(--border-light);
  color: var(--text-main);
  font-size: 0.85rem;
  font-weight: 600;
  box-shadow: var(--shadow-soft);
  transition: all 0.3s;
}

.btn-secondary:hover {
  border-color: var(--border-focus);
  transform: translateY(-2px);
}

/* Hero & 3D Stage */
.hero-section {
  padding-top: 150px;
  padding-bottom: 60px;
  text-align: center;
}

.hero-3d-box {
  width: 100%;
  max-width: 1060px;
  height: 500px;
  margin: 3rem auto 1.5rem auto;
  background: radial-gradient(circle at center, #ffffff 0%, #f4f4f7 85%);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-float);
  position: relative;
  overflow: hidden;
}

#canvas3D {
  width: 100%;
  height: 100%;
  display: block;
}

.studio-toolbar {
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 1.25rem;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(16px);
  padding: 0.4rem 1.25rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-light);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  z-index: 10;
}

.toolbar-btn {
  padding: 0.45rem 1rem;
  border-radius: var(--radius-full);
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--text-muted);
  transition: all 0.2s;
}

.toolbar-btn.active {
  background: var(--text-main);
  color: #ffffff;
}

/* --------------------------------------------------------------------------
   CANLI KART OLUŞTURUCU (THE APPROVED BESPOKE BUILDER)
   -------------------------------------------------------------------------- */
.configurator-section {
  background: var(--bg-secondary);
}

.configurator-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: clamp(2rem, 4vw, 3.5rem);
  box-shadow: var(--shadow-card);
  margin-top: 3rem;
}

.configurator-grid {
  display: grid;
  grid-template-columns: 1.15fr 1fr;
  gap: 3.5rem;
  align-items: center;
}

@media (max-width: 960px) {
  .configurator-grid { grid-template-columns: 1fr; }
}

.live-card-mockup {
  width: 100%;
  max-width: 440px;
  height: 260px;
  margin: 0 auto;
  border-radius: 20px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.12);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 2rem;
  transition: all 0.4s ease;
}

.live-card-mockup.ceramic {
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
  border: 1px solid #e2e8f0;
  color: #0f172a;
}

.live-card-mockup.titanium {
  background: linear-gradient(135deg, #e2e8f0 0%, #cbd5e1 100%);
  border: 1px solid #94a3b8;
  color: #0f172a;
}

.live-card-mockup.champagne {
  background: linear-gradient(135deg, #faf5eb 0%, #d6c5af 100%);
  border: 1px solid #c8b6a6;
  color: #292524;
}

.live-card-mockup.gold {
  background: linear-gradient(135deg, #fef08a 0%, #eab308 100%);
  border: 1px solid #ca8a04;
  color: #422006;
}

.chip-graphic {
  width: 52px;
  height: 40px;
  border-radius: 8px;
  background: linear-gradient(135deg, #eab308 0%, #a16207 100%);
  border: 1px solid #ca8a04;
  position: relative;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.chip-graphic::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: 1px;
  background: rgba(0,0,0,0.25);
}

.alloy-pill-btn {
  padding: 0.55rem 1.1rem;
  border-radius: var(--radius-full);
  background: #ffffff;
  border: 1px solid var(--border-light);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-main);
  box-shadow: 0 2px 6px rgba(0,0,0,0.03);
  transition: all 0.2s;
}

.alloy-pill-btn.active {
  border-color: var(--accent-gold);
  color: var(--accent-gold);
  background: rgba(179, 139, 77, 0.08);
}

.form-input-clean {
  width: 100%;
  padding: 0.95rem 1.2rem;
  background: var(--bg-secondary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  font-size: 1rem;
  color: var(--text-main);
  transition: all 0.2s;
}

.form-input-clean:focus {
  outline: none;
  background: #ffffff;
  border-color: var(--accent-gold);
  box-shadow: 0 0 0 3px rgba(179, 139, 77, 0.12);
}

/* --------------------------------------------------------------------------
   Ecosystem 6 Pillars Grid
   -------------------------------------------------------------------------- */
.eco-grid-6 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 3.5rem;
}

@media (max-width: 1024px) {
  .eco-grid-6 { grid-template-columns: 1fr; }
}

.eco-tile {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 2.5rem 2rem;
  box-shadow: var(--shadow-soft);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.eco-tile:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-card);
  border-color: var(--border-gold);
}

.eco-thumb {
  height: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at center, rgba(197, 168, 128, 0.08) 0%, transparent 70%);
  border-radius: var(--radius-sm);
  margin: 1.25rem 0;
}

.eco-thumb img {
  max-height: 140px;
  object-fit: contain;
  filter: drop-shadow(0 12px 20px rgba(0, 0, 0, 0.06));
}

/* --------------------------------------------------------------------------
   Weight Specs Comparator
   -------------------------------------------------------------------------- */
.comparator-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
  margin-top: 3.5rem;
}

@media (max-width: 840px) {
  .comparator-row { grid-template-columns: 1fr; }
}

.comparator-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 2.5rem 2rem;
  text-align: center;
  box-shadow: var(--shadow-soft);
}

.comparator-card.featured {
  border-color: var(--accent-gold);
  box-shadow: 0 20px 45px rgba(179, 139, 77, 0.12);
}

.weight-display {
  font-size: 3.5rem;
  font-weight: 700;
  letter-spacing: -0.04em;
  margin: 0.75rem 0;
  line-height: 1;
}

/* Footer */
.footer-serene {
  background: var(--bg-secondary);
  border-top: 1px solid var(--border-light);
  padding: 4.5rem 0 2.5rem 0;
  font-size: 0.88rem;
  color: var(--text-muted);
}
"""

with open('/Users/ramay/gentech3-app/assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(complete_css)

# Complete HTML with Exact Layout and Class Alignment
html_content = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>GenTech 3 | Serene Alabaster Edition — Akıllı Yüzükler & Titanyum Kartlar</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Three.js 3D WebGL Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <!-- Core Stylesheet -->
    <link rel="stylesheet" href="assets/css/style.css?v=5.0">
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
                <a href="#overview" class="nav-link">Genel Bakış</a>
                <a href="#configurator" class="nav-link">Kart Oluşturucu</a>
                <a href="#ecosystem" class="nav-link">Ekosistem</a>
                <a href="#weight" class="nav-link">Ağırlık Kıyaslama</a>
                <a href="#inquire" class="nav-link">İletişim</a>
            </div>

            <div style="display: flex; align-items: center; gap: 1rem;">
                <a href="#inquire" class="btn-primary" style="padding: 0.55rem 1.4rem; font-size: 0.82rem;">
                    <span>Filo Teklifi Al</span>
                </a>
            </div>
        </nav>
    </div>
</header>

<main id="overview">
    <!-- 1. Serene Hero Section -->
    <section class="hero-section">
        <div class="container">
            <div class="calm-tag">✦ Dubai Mühendislik Merkezi • Saf Seramik & Titanyum</div>
            <h1 class="serif-title">
                Sakin teknoloji. <br>
                <span class="gradient-text">Her dokunuşta gerçek kalite.</span>
            </h1>
            <p style="font-size: clamp(1.1rem, 2vw, 1.3rem); color: var(--text-muted); max-width: 660px; margin: 1.25rem auto 2.25rem auto;">
                28,5 gram yekpare titanyum kartlar, bataryasız zirkonya seramik akıllı yüzükler ve 50 milisaniyenin altında açılan şehir içi ulaşım kartları. Dubai'de tasarlandı.
            </p>

            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="#configurator" class="btn-primary">Kartınızı Tasarlayın</a>
                <a href="#ecosystem" class="btn-secondary">6 Temel Sütun</a>
            </div>

            <!-- 3D Studio Stage -->
            <div class="hero-3d-box">
                <div id="canvas3D"></div>
                <div class="studio-toolbar">
                    <button class="toolbar-btn active artifact-toggle-btn" data-artifact="both">Tüm Objeler</button>
                    <button class="toolbar-btn artifact-toggle-btn" data-artifact="ring">Akıllı Yüzük</button>
                    <button class="toolbar-btn artifact-toggle-btn" data-artifact="card">Titanyum Kart</button>
                    <button class="toolbar-btn" id="explodedViewBtn">Katman Ayrışımı</button>
                </div>
            </div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">
                ✦ Fareyle objeleri döndürebilir ve stüdyo ışık yansımalarını inceleyebilirsiniz
            </div>
        </div>
    </section>

    <!-- 2. CANLI KART OLUŞTURUCU (THE APPROVED BESPOKE BUILDER) -->
    <section class="section-spacing configurator-section" id="configurator">
        <div class="container">
            <div style="text-align: center; max-width: 680px; margin: 0 auto;">
                <div class="calm-tag">Canlı Kart Oluşturucu</div>
                <h2 class="serif-title">Bankanızın ulusal kartını tasarlayın.</h2>
                <p style="color: var(--text-muted); font-size: 1.05rem; margin-top: 0.5rem;">
                    Alaşımları özelleştirin, çip geometrilerini seçin ve canlı tipografiyi gerçek zamanlı olarak önizleyin.
                </p>
            </div>

            <div class="configurator-card">
                <div class="configurator-grid">
                    <!-- Sol: Canlı Önizleme Kartı -->
                    <div style="text-align: center;">
                        <div class="live-card-mockup ceramic" id="liveCardMockup">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div class="chip-graphic"></div>
                                <span style="font-family: var(--font-mono); font-size: 0.85rem; font-weight: 700; letter-spacing: 0.05em;">GENTECH</span>
                            </div>
                            <div style="text-align: left;">
                                <div style="font-size: 0.75rem; opacity: 0.6; text-transform: uppercase; letter-spacing: 0.05em;">KART SAHİBİ</div>
                                <div id="mockupCardholder" style="font-size: 1.25rem; font-weight: 700; letter-spacing: 0.12em;">ALEXANDER VANCE</div>
                                <div id="mockupSerial" style="font-family: var(--font-mono); font-size: 0.78rem; opacity: 0.7; margin-top: 0.25rem;">GT-9482-2026</div>
                            </div>
                        </div>
                        <div style="margin-top: 1rem; font-size: 0.82rem; color: var(--text-muted);">
                            28,5 g ağırlığında sağlam monolit • CC EAL6+ Sertifikalı
                        </div>
                    </div>

                    <!-- Sağ: Kontrol Paneli -->
                    <div>
                        <!-- Değerli Metal Kaplama Seçimi -->
                        <div style="margin-bottom: 1.5rem;">
                            <label style="font-size:0.88rem; font-weight:600; display:block; margin-bottom:0.6rem;">Değerli Metal Kaplama Seçin:</label>
                            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                                <button class="alloy-pill-btn active" data-alloy="ceramic">Saf Seramik</button>
                                <button class="alloy-pill-btn" data-alloy="titanium">Soluk Titanyum</button>
                                <button class="alloy-pill-btn" data-alloy="champagne">Şampanya Altını</button>
                                <button class="alloy-pill-btn" data-alloy="gold">24 Ayar Ayna Altın</button>
                            </div>
                        </div>

                        <!-- Kart Sahibinin Adı -->
                        <div style="margin-bottom: 1.25rem;">
                            <label style="font-size:0.88rem; font-weight:600; display:block; margin-bottom:0.4rem;">Kart Sahibinin Adı:</label>
                            <input type="text" id="configNameInput" class="form-input-clean" value="ALEXANDER VANCE" maxlength="26">
                        </div>

                        <!-- Parti Seri Numarası -->
                        <div style="margin-bottom: 1.75rem;">
                            <label style="font-size:0.88rem; font-weight:600; display:block; margin-bottom:0.4rem;">Parti Seri Numarası:</label>
                            <input type="text" id="configSerialInput" class="form-input-clean" value="GT-9482-2026" maxlength="20">
                        </div>

                        <button class="btn-primary" style="width: 100%; justify-content: center; padding: 0.95rem;">
                            <span>Filo Üretimi Teklifi İsteyin</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Ekosistemin 6 Temel Sütunu -->
    <section class="section-spacing" id="ecosystem">
        <div class="container">
            <div style="text-align: center; max-width: 720px; margin: 0 auto 3rem auto;">
                <div class="calm-tag">Tüm Donanım Ekosistemi</div>
                <h2 class="serif-title">Zarafetle tasarlanmış donanımlar.</h2>
                <p style="color: var(--text-muted); font-size: 1.05rem; margin-top: 0.5rem;">
                    Banka kartlarından akıllı yüzüklere, şehir içi ulaşım kartlarından 5G Super SIM çözümlerine kadar.
                </p>
            </div>

            <div class="eco-grid-6">
                <!-- 1 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--accent-sage); text-transform:uppercase;">Giyilebilir Donanım</span>
                        <div class="eco-thumb"><img src="assets/images/wearable.png" alt="Akıllı Yüzükler ve Bileklikler"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Apex Yüzükler & Bileklikler</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">%100 şarj gerektirmeyen indüktif NFC rezonansı. 50m su geçirmez zirkonya seramik gövde.</p>
                    </div>
                </div>

                <!-- 2 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--accent-gold); text-transform:uppercase;">Lüks Metal Kartlar</span>
                        <div class="eco-thumb"><img src="assets/images/portfolio-4.png" alt="Titanyum Kartlar"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Sovereign 28,5g Titanyum</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">Özel bankacılık ve VIP müşteriler için tek parça Grade-5 titanyum bloktan üretilir.</p>
                    </div>
                </div>

                <!-- 3 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--accent-blue); text-transform:uppercase;">Akıllı Şehirler</span>
                        <div class="eco-thumb"><img src="assets/images/transportcards.png" alt="Ulaşım Kartları"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Şehir İçi Ulaşım Kartları</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">Metro ve otobüs ağları için Calypso ve MIFARE uyumlu yüksek hızlı temassız kartlar.</p>
                    </div>
                </div>

                <!-- 4 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--text-dim); text-transform:uppercase;">5G Telekomünikasyon</span>
                        <div class="eco-thumb"><img src="assets/images/supersim.png" alt="Super SIM"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Super NFC 5G SIM Kartlar</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">Hücresel abonelik, bankacılık ödemeleri ve ulaşım biletlerini tek bir 5G SIM çipinde birleştirir.</p>
                    </div>
                </div>

                <!-- 5 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--accent-gold); text-transform:uppercase;">Özel Çip Modülleri</span>
                        <div class="eco-thumb"><img src="assets/images/customize-chip.png" alt="Özel Çip Modülleri"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Özel Lazer İşlemeli Çipler</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">24K ayna altın kaplama ve kurumsal logolu özel geometrili kontak plakaları.</p>
                    </div>
                </div>

                <!-- 6 -->
                <div class="eco-tile">
                    <div>
                        <span style="font-size:0.75rem; font-weight:600; color:var(--text-dim); text-transform:uppercase;">Donanım & POS</span>
                        <div class="eco-thumb"><img src="assets/images/pos.png" alt="POS Donanımları"></div>
                        <h3 class="serif-title" style="font-size:1.3rem;">Kişiselleştirme & POS Cihazları</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem;">Anahtar teslim kart kabartma makineleri, Android akıllı POS ve HSM kripto modülleri.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Ağırlık Kıyaslama -->
    <section class="section-spacing" id="weight" style="background: var(--bg-secondary);">
        <div class="container">
            <div style="text-align: center; max-width: 680px; margin: 0 auto 3rem auto;">
                <div class="calm-tag">Fiziksel Kalite</div>
                <h2 class="serif-title">Gerçek ağırlığın hissi.</h2>
                <p style="color: var(--text-muted); font-size: 1.05rem; margin-top: 0.5rem;">
                    Sıradan plastik kartlar ile yekpare titanyum arasındaki belirgin fark.
                </p>
            </div>

            <div class="comparator-row">
                <div class="comparator-card">
                    <span style="font-size:0.8rem; color:var(--text-dim); text-transform:uppercase; font-weight:600;">Sıradan Banka Kartı</span>
                    <div class="weight-display" style="color: #94a3b8;">5,0 g</div>
                    <div style="font-size:0.9rem; font-weight:600; color:var(--text-muted); margin-bottom:1rem;">Standart PVC Plastik</div>
                    <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6;">Kolayca bükülür ve kısa sürede çizilir.</p>
                </div>
                <div class="comparator-card">
                    <span style="font-size:0.8rem; color:var(--text-dim); text-transform:uppercase; font-weight:600;">Hibrit Kaplama Kart</span>
                    <div class="weight-display" style="color: #64748b;">16,0 g</div>
                    <div style="font-size:0.9rem; font-weight:600; color:var(--text-muted); margin-bottom:1rem;">Çelik Kaplama + Plastik Çekirdek</div>
                    <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6;">Plastik taban üzerine yapıştırılmış ince metal yüzey.</p>
                </div>
                <div class="comparator-card featured">
                    <span style="font-size:0.8rem; color:var(--accent-gold); text-transform:uppercase; font-weight:700;">GenTech Sovereign</span>
                    <div class="weight-display gradient-text">28,5 g</div>
                    <div style="font-size:0.9rem; font-weight:600; color:var(--accent-gold); margin-bottom:1rem;">%100 Saf Grade-5 Titanyum</div>
                    <p style="font-size:0.85rem; color:var(--text-main); font-weight:500;">Tek parça titanyum monolit bloktan frezelenir, ömür boyu dayanıklıdır.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Kurumsal İletişim -->
    <section class="section-spacing" id="inquire" style="text-align: center;">
        <div class="container">
            <div class="calm-tag">Özel Bankacılık & Kurumsal Talepler</div>
            <h2 class="serif-title">Bankanızın donanım filosunu başlatın.</h2>
            <p style="color: var(--text-muted); font-size: 1.1rem; max-width: 620px; margin: 1rem auto 2.5rem auto;">
                Numune kutuları ve üretim planlaması için Dubai mühendislik masamızla doğrudan iletişime geçin.
            </p>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="mailto:info@gentech.ae" class="btn-primary">Filo Talebi Gönder</a>
                <a href="tel:+971500000000" class="btn-secondary">Dubai Masasını Ara</a>
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
                    Ras Al Khaimah Economic Zone, Dubai, Birleşik Arap Emirlikleri.
                </div>
            </div>
            <div style="display: flex; gap: 1.75rem; font-size: 0.82rem; font-weight: 600; color: var(--text-muted);">
                <span>EMVCo Sertifikalı</span>
                <span>PCI-DSS Level 1</span>
                <span>ISO 14443 Type A</span>
                <span>GSMA 5G</span>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 1.5rem; font-size: 0.82rem; color: var(--text-dim); flex-wrap: wrap; gap: 1rem;">
            <div>&copy; 2025-2026 GenTech Global LLC. Tüm Hakları Saklıdır.</div>
            <div>GenTech 3 • Serene Alabaster Sürümü</div>
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
    f.write(html_content)

# Update app.js
app_js = """/**
 * GenTech 3 Master Controller
 */
document.addEventListener('DOMContentLoaded', () => {
  // Artifact Toggle
  const artifactBtns = document.querySelectorAll('.artifact-toggle-btn');
  artifactBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      artifactBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const art = btn.getAttribute('data-artifact');
      if (typeof setActiveArtifact === 'function') setActiveArtifact(art);
    });
  });

  // Exploded View
  const explodedBtn = document.getElementById('explodedViewBtn');
  explodedBtn?.addEventListener('click', () => {
    explodedBtn.classList.toggle('active');
    if (typeof toggleExplodedView === 'function') toggleExplodedView();
  });

  // Live Card Configurator (Approved Design)
  const mockup = document.getElementById('liveCardMockup');
  const cardName = document.getElementById('mockupCardholder');
  const cardSerial = document.getElementById('mockupSerial');
  const nameInput = document.getElementById('configNameInput');
  const serialInput = document.getElementById('configSerialInput');
  const alloyBtns = document.querySelectorAll('.alloy-pill-btn');

  alloyBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      alloyBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const alloy = btn.getAttribute('data-alloy');
      if (mockup) {
        mockup.className = `live-card-mockup ${alloy}`;
      }
      if (typeof set3DMaterial === 'function') set3DMaterial(alloy);
    });
  });

  nameInput?.addEventListener('input', (e) => {
    if (cardName) cardName.textContent = e.target.value.toUpperCase() || 'ALEXANDER VANCE';
  });

  serialInput?.addEventListener('input', (e) => {
    if (cardSerial) cardSerial.textContent = e.target.value || 'GT-9482-2026';
  });
});
"""

with open('/Users/ramay/gentech3-app/assets/js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

# Sync to WordPress theme and rebuild ZIP
wp_theme_dir = '/Users/ramay/gentech3-wp/gentech3-theme'
os.system(f"cp /Users/ramay/gentech3-app/assets/css/style.css {wp_theme_dir}/assets/css/style.css")
os.system(f"cp /Users/ramay/gentech3-app/assets/js/* {wp_theme_dir}/assets/js/")
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

print("GenTech 3 pixel-perfect fix complete and synced!")
