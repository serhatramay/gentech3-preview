import os
from generate_all_pages import get_footer

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>GenTech Global LLC | Sovereign Payment Systems, Concave Smart Rings & Titanium Metal Cards</title>
    <meta name="description" content="GenTech Global LLC - Dubai-based pioneer in wearable payment technologies, 28.5g solid titanium cards, 5G Super SIMs, POS hardware, and municipal transit solutions.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Three.js 3D WebGL Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <!-- Core Stylesheet -->
    <link rel="stylesheet" href="assets/css/style.css?v=12.0">
</head>
<body>

<!-- Serene Sticky Navigation -->
<header class="main-header">
    <div class="container">
        <nav class="main-nav">
            <a href="index.html" class="nav-brand">
                <div class="nav-brand-dot"></div>
                <div class="brand-text">
                    <span class="brand-title">GENTECH</span>
                    <span class="brand-sub">GLOBAL LLC</span>
                </div>
            </a>

            <div class="nav-links">
                <a href="index.html" class="nav-link active">Home</a>
                <a href="about.html" class="nav-link">About &amp; Künye</a>
                <div class="nav-dropdown-wrapper">
                    <a href="service.html" class="nav-link">Services ▾</a>
                    <div class="nav-dropdown-menu">
                        <a href="emvcards.html" class="dropdown-item">Smart &amp; EMV Cards</a>
                        <a href="metalcards.html" class="dropdown-item">Metal &amp; Titanium Cards</a>
                        <a href="ceramiccards.html" class="dropdown-item">Ceramic Cards</a>
                        <a href="chipmodules.html" class="dropdown-item">Bespoke Chip Modules</a>
                        <a href="wearable.html" class="dropdown-item">Wearable Payment Devices</a>
                        <a href="transport.html" class="dropdown-item">Transport &amp; City Cards</a>
                        <a href="telecom.html" class="dropdown-item">Telecommunications (5G SIM)</a>
                        <a href="hardware.html" class="dropdown-item">Banking &amp; POS Hardware</a>
                        <a href="chip.html" class="dropdown-item">Card &amp; Chip Integration</a>
                    </div>
                </div>
                <a href="products.html" class="nav-link">Products (7 Categories)</a>
                <a href="hardware.html" class="nav-link">Hardware &amp; 5G</a>
                <a href="contact.html" class="nav-link">Contact</a>
            </div>

            <div class="nav-actions">
                <a href="contact.html" class="btn-primary nav-cta">
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
            <div class="calm-tag">✦ Dubai Engineering Center (RAKEZ) • Grade-5 Titanium &amp; Biometric Wearables</div>
            <h1 class="serif-title">
                Calm technology. <br>
                <span class="gradient-text">Substance in every touch.</span>
            </h1>
            <p class="hero-description">
                A serene synthesis of 28.5g solid titanium cards, concave titanium smart rings with BioActive optical sensors, Super NFC 5G SIMs, and sub-50ms municipal transit cards — engineered with whisper-quiet precision in Dubai.
            </p>

            <div class="hero-cta-group">
                <a href="#configurator" class="btn-primary">Design Sovereign Card</a>
                <a href="products.html" class="btn-secondary">Explore 22+ Products</a>
            </div>

            <!-- 3D Studio Stage -->
            <div class="hero-3d-box">
                <div id="canvas3D"></div>
                <div class="studio-toolbar">
                    <button class="toolbar-btn active artifact-toggle-btn" data-artifact="ring">💍 Galaxy Smart Ring</button>
                    <button class="toolbar-btn artifact-toggle-btn" data-artifact="card">💳 Titanium Card</button>
                    
                    <!-- Ring Finish Sub-toolbar -->
                    <div class="finish-selector" id="ringFinishSelector" style="display: flex;">
                        <button class="finish-pill-btn ring-finish-btn active" data-finish="silver">Titanium Silver</button>
                        <button class="finish-pill-btn ring-finish-btn" data-finish="black">Titanium Black</button>
                        <button class="finish-pill-btn ring-finish-btn" data-finish="gold">Titanium Gold</button>
                    </div>

                    <!-- Card Finish Sub-toolbar -->
                    <div class="finish-selector hidden" id="cardFinishSelector">
                        <button class="finish-pill-btn card-finish-btn active" data-card-finish="stealth">Stealth Black</button>
                        <button class="finish-pill-btn card-finish-btn" data-card-finish="titanium">Pale Titanium</button>
                        <button class="finish-pill-btn card-finish-btn" data-card-finish="gold">24K Mirror Gold</button>
                    </div>
                </div>
            </div>
            <div class="hero-hint">
                ✦ Drag to rotate artifacts in 3D space • Switch metal finishes &amp; concave contours in real time
            </div>

            <!-- Trust Badges Row -->
            <div class="trust-badges-row">
                <div class="trust-badge-item">
                    <span class="badge-dot"></span>
                    <span>EMVCo Certified</span>
                </div>
                <div class="trust-badge-item">
                    <span class="badge-dot"></span>
                    <span>PCI-DSS Level 1</span>
                </div>
                <div class="trust-badge-item">
                    <span class="badge-dot"></span>
                    <span>ISO/IEC 14443 Type A/B</span>
                </div>
                <div class="trust-badge-item">
                    <span class="badge-dot"></span>
                    <span>GSMA 5G Compliant</span>
                </div>
                <div class="trust-badge-item">
                    <span class="badge-dot"></span>
                    <span>RAKEZ Dubai UAE</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. CORPORATE IDENTITY, ABOUT & KÜNYE (6 VALUE PILLARS) -->
    <section class="section-spacing about-section" id="about">
        <div class="container">
            <div class="section-header-center">
                <div class="calm-tag">Corporate Identity &amp; Künye</div>
                <h2 class="serif-title">Pioneering the future of global exchange.</h2>
                <p class="section-subtitle">
                    Founded in Dubai in the first quarter of 2025, GENTECH Global LLC is an international technology house specializing in advanced payment systems, smart cards, and biometric wearable technologies.
                </p>
            </div>

            <!-- About Grid -->
            <div class="about-hero-grid">
                <div class="about-story-card">
                    <div class="about-img-box">
                        <img src="assets/images/about.png" alt="GenTech Global Dubai HQ" class="about-img">
                    </div>
                    <div class="about-story-content">
                        <h3 class="serif-title">Engineered in Dubai for Sovereign Institutions</h3>
                        <p>
                            GENTECH Global develops smart, secure payment solutions that simplify financial experiences. Our products include contactless payment cards, wearable payment devices, and digital identity systems designed for banks, financial institutions, telecoms, and sovereign brands.
                        </p>
                        <p>
                            With a user-centered ergonomic approach and bank-grade security standards, we bring the future of payment technology to the present day.
                        </p>
                        
                        <div class="corporate-meta-box">
                            <div class="meta-row">
                                <span class="meta-label">Company Name:</span>
                                <span class="meta-val">GENTECH GLOBAL LLC</span>
                            </div>
                            <div class="meta-row">
                                <span class="meta-label">Headquarters:</span>
                                <span class="meta-val">Ras Al Khaimah Economic Zone (RAKEZ), Dubai, UAE</span>
                            </div>
                            <div class="meta-row">
                                <span class="meta-label">Establishment:</span>
                                <span class="meta-val">Q1 2025 (Dubai, UAE)</span>
                            </div>
                            <div class="meta-row">
                                <span class="meta-label">Operating Hours:</span>
                                <span class="meta-val">Mon - Fri : 09:00 AM - 09:00 PM (GST)</span>
                            </div>
                            <div class="meta-row">
                                <span class="meta-label">Direct Desk:</span>
                                <span class="meta-val"><a href="mailto:info@gentech.ae">info@gentech.ae</a></span>
                            </div>
                        </div>

                        <div style="margin-top: 1.5rem;">
                            <a href="about.html" class="btn-primary" style="padding: 0.6rem 1.4rem; font-size: 0.85rem;">Read Full Corporate Künye →</a>
                        </div>
                    </div>
                </div>

                <div class="mission-vision-container">
                    <div class="mv-card">
                        <div class="mv-icon">🎯</div>
                        <h3 class="serif-title">Our Mission</h3>
                        <p>To make life easier and transactions frictionless through secure, innovative, and sustainable payment technologies.</p>
                    </div>
                    <div class="mv-card">
                        <div class="mv-icon">🌍</div>
                        <h3 class="serif-title">Our Vision</h3>
                        <p>To become the leading global sovereign brand in wearable, smart card, and digital payment mobility solutions.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. COMPREHENSIVE 9 SERVICES SUITE -->
    <section class="section-spacing services-section" id="services">
        <div class="container">
            <div class="section-header-center">
                <div class="calm-tag">Enterprise Portfolio</div>
                <h2 class="serif-title">Our Nine Core Services</h2>
                <p class="section-subtitle">
                    Each service is backed by dedicated in-house production lines, engineering teams, and dedicated pages. Click any service to view full specifications.
                </p>
            </div>

            <div class="services-grid-9">
                <!-- Service 1 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-1.jpg" alt="Smart & EMV Cards">
                        <span class="service-tag">Core Banking</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Smart &amp; EMV Cards</h3>
                        <p class="service-desc">Certified payment cards supporting Visa, Mastercard, and Discover networks. Produced with advanced security chips and customizable eco-friendly materials.</p>
                        <a href="emvcards.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Open Dedicated Page →</a>
                    </div>
                </div>

                <!-- Service 2 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-7.jpg" alt="Metal Cards">
                        <span class="service-tag">Tactile Luxury</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Metal Cards</h3>
                        <p class="service-desc">Exclusive metal bank cards offering a superior tactile experience compared to standard PVC, designed for private banking and VIP portfolios.</p>
                        <a href="metalcards.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Open Dedicated Page →</a>
                    </div>
                </div>

                <!-- Service 3 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-8.jpg" alt="Ceramic Cards">
                        <span class="service-tag">High Precision</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Ceramic Cards</h3>
                        <p class="service-desc">Produced from high-performance engineering ceramics (alumina and zirconia), delivering extreme scratch resistance, mirror gloss, and silky tactile touch.</p>
                        <a href="ceramiccards.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Open Dedicated Page →</a>
                    </div>
                </div>

                <!-- Service 4 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-9.jpg" alt="Chip Modules">
                        <span class="service-tag">Artisan Hardware</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Chip Modules</h3>
                        <p class="service-desc">Custom laser-engraved contact surfaces styled with your corporate logo or symbol. 24K gold flash mirror plating crafted for elite brand identity.</p>
                        <a href="chipmodules.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Open Dedicated Page →</a>
                    </div>
                </div>

                <!-- Service 5 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-2.jpg" alt="Wearable Payment Devices">
                        <span class="service-tag">Biometrics & NFC</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Wearable Payment Devices</h3>
                        <p class="service-desc">Innovative smart rings, wristbands, and key fobs designed for convenient contactless transactions — combining luxury jewelry aesthetics with EMV technology.</p>
                        <a href="wearable.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Open Dedicated Page →</a>
                    </div>
                </div>

                <!-- Service 6 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-3.jpg" alt="Transport & City Cards">
                        <span class="service-tag">Smart Mobility</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Transport &amp; City Cards</h3>
                        <p class="service-desc">Integrated contactless smart cards for public transportation systems, offering sub-50ms gate latency, rapid passenger throughput, and Account-Based Ticketing (ABT).</p>
                        <a href="transport.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Open Dedicated Page →</a>
                    </div>
                </div>

                <!-- Service 7 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-4.jpg" alt="Telecommunications">
                        <span class="service-tag">5G & IoT</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Telecommunications</h3>
                        <p class="service-desc">GSM, 5G, and IoT SIM cards with dedicated operator profiles, alongside our breakthrough Super NFC SIM unifying cellular, transit, and banking on one chip.</p>
                        <a href="telecom.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Open Dedicated Page →</a>
                    </div>
                </div>

                <!-- Service 8 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-5.jpg" alt="Banking Hardware">
                        <span class="service-tag">Terminal Fleet</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Hardware &amp; Terminals</h3>
                        <p class="service-desc">Physical devices and transaction processing hardware for financial institutions, including Countertop POS, mobile mPOS, QR Code Sound Boxes, and Cloud Printers.</p>
                        <a href="hardware.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Open Dedicated Page →</a>
                    </div>
                </div>

                <!-- Service 9 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-6.jpg" alt="Card & Chip Integration">
                        <span class="service-tag">Personalization</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Card &amp; Chip Integration</h3>
                        <p class="service-desc">Full control over chip module integration, prelam manufacturing, laser personalization, and Hardware Security Module (HSM) cryptographic key management.</p>
                        <a href="chip.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Open Dedicated Page →</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. FEATURED PRODUCTS PREVIEW -->
    <section class="section-spacing products-section" id="products">
        <div class="container">
            <div class="section-header-center">
                <div class="calm-tag">Portfolio Showcase</div>
                <h2 class="serif-title">Featured Products Fleet</h2>
                <p class="section-subtitle">
                    Explore our certified fleet across 7 core categories. Click below to view the entire catalog with interactive category filters.
                </p>
                <div style="margin-top: 1.5rem;">
                    <a href="products.html" class="btn-primary" style="padding: 0.75rem 1.8rem;"><span>Open All 7 Categories (22 Products) →</span></a>
                </div>
            </div>

            <!-- Filter Navigation Bar -->
            <div class="portfolio-filter-container">
                <button class="filter-btn active" data-filter="all">All Featured</button>
                <button class="filter-btn" data-filter="pvc">PVC Cards</button>
                <button class="filter-btn" data-filter="metal">Metal Cards</button>
                <button class="filter-btn" data-filter="ceramic">Ceramic Cards</button>
                <button class="filter-btn" data-filter="sim">GSM &amp; 5G SIM</button>
                <button class="filter-btn" data-filter="ring">Smart Rings</button>
                <button class="filter-btn" data-filter="wristband">Smart Wristbands</button>
            </div>

            <!-- Products Grid Preview (Sample 8 Items) -->
            <div class="products-portfolio-grid" id="portfolioGrid">
                
                <!-- Item 1 (PVC) -->
                <div class="product-item-card" data-category="pvc">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-1.png" alt="Shell Foil PVC Card" class="product-img">
                        <span class="product-badge">PVC Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Shell Foil PVC Cards</h4>
                        <p class="product-brief">PVC card enhanced with handcrafted 3D grain arrangement and shell-like iridescent light reflection.</p>
                        <div class="product-footer">
                            <a href="emvcards.html" style="font-size: 0.78rem; font-weight: 700; color: var(--accent-hermes);">View EMV Specs →</a>
                        </div>
                    </div>
                </div>

                <!-- Item 2 (Metal) -->
                <div class="product-item-card" data-category="metal">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-3.png" alt="Titanium Cards" class="product-img">
                        <span class="product-badge">Metal Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Titanium Monolith Cards</h4>
                        <p class="product-brief">100% solid Grade-5 titanium body with brushed micro-texture and laser engraved typography.</p>
                        <div class="product-footer">
                            <a href="metalcards.html" style="font-size: 0.78rem; font-weight: 700; color: var(--accent-hermes);">View Metal Specs →</a>
                        </div>
                    </div>
                </div>

                <!-- Item 3 (Ceramic) -->
                <div class="product-item-card" data-category="ceramic">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-20.png" alt="Ceramic Credit Card" class="product-img">
                        <span class="product-badge">Ceramic Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Ceramic Credit Card (Zirconia)</h4>
                        <p class="product-brief">Engineered from sintered zirconia ceramic, yielding unscratchable surface luster and luxury density.</p>
                        <div class="product-footer">
                            <a href="ceramiccards.html" style="font-size: 0.78rem; font-weight: 700; color: var(--accent-hermes);">View Ceramic Specs →</a>
                        </div>
                    </div>
                </div>

                <!-- Item 4 (SIM) -->
                <div class="product-item-card" data-category="sim">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-12.png" alt="Super NFC SIM" class="product-img">
                        <span class="product-badge">GSM / 5G SIM</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Super NFC 5G SIM Card</h4>
                        <p class="product-brief">Highly integrated module unifying 5G mobile communication, subway/bus transit, and bank cards.</p>
                        <div class="product-footer">
                            <a href="telecom.html" style="font-size: 0.78rem; font-weight: 700; color: var(--accent-hermes);">View SIM Specs →</a>
                        </div>
                    </div>
                </div>

                <!-- Item 5 (Ring) -->
                <div class="product-item-card" data-category="ring">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-6.png" alt="Smart Health Ceramic Ring Black" class="product-img">
                        <span class="product-badge">Smart Ring</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Smart Health Ceramic Ring</h4>
                        <p class="product-brief">Wearable electronic ring with integrated BioActive sensors monitoring health telemetry and NFC.</p>
                        <div class="product-footer">
                            <a href="wearable.html" style="font-size: 0.78rem; font-weight: 700; color: var(--accent-hermes);">View Ring Specs →</a>
                        </div>
                    </div>
                </div>

                <!-- Item 6 (Wristband) -->
                <div class="product-item-card" data-category="wristband">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-13.png" alt="Smart Ceramic Wristband" class="product-img">
                        <span class="product-badge">Smart Wristband</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Smart Ceramic Wristband</h4>
                        <p class="product-brief">Wearable bracelet with modular ceramic links enabling fast contactless payments at gates &amp; POS.</p>
                        <div class="product-footer">
                            <a href="wearable.html" style="font-size: 0.78rem; font-weight: 700; color: var(--accent-hermes);">View Wristband Specs →</a>
                        </div>
                    </div>
                </div>

                <!-- Item 7 (Metal) -->
                <div class="product-item-card" data-category="metal">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-4.png" alt="Stainless Steel Card" class="product-img">
                        <span class="product-badge">Metal Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Stainless Steel Cards</h4>
                        <p class="product-brief">Heavyweight stainless steel cards designed for sovereign private wealth and VIP cardholders.</p>
                        <div class="product-footer">
                            <a href="metalcards.html" style="font-size: 0.78rem; font-weight: 700; color: var(--accent-hermes);">View Metal Specs →</a>
                        </div>
                    </div>
                </div>

                <!-- Item 8 (Sticker) -->
                <div class="product-item-card" data-category="sticker">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-21.png" alt="NFC Payment Sticker" class="product-img">
                        <span class="product-badge">Sticker</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">NFC Payment Sticker</h4>
                        <p class="product-brief">Ultra-thin adhesive payment microtag attachable to smartphones and devices for tap-to-pay.</p>
                        <div class="product-footer">
                            <a href="products.html" style="font-size: 0.78rem; font-weight: 700; color: var(--accent-hermes);">View in Catalog →</a>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- 5. BESPOKE CARD BUILDER (LIVE 3D CONFIGURATOR) -->
    <section class="section-spacing configurator-section" id="configurator">
        <div class="container">
            <div class="section-header-center">
                <div class="calm-tag">Live Card Builder</div>
                <h2 class="serif-title">Design your bank's sovereign card.</h2>
                <p class="section-subtitle">
                    Customize precious alloys, choose chip geometries, and preview live typography in real time.
                </p>
            </div>

            <div class="configurator-card">
                <div class="configurator-grid">
                    <!-- Left: Live Card Mockup -->
                    <div style="text-align: center;">
                        <div class="live-card-mockup ceramic" id="liveCardMockup">
                            <div class="live-card-top">
                                <div class="chip-graphic"></div>
                                <span class="live-card-brand">GENTECH</span>
                            </div>
                            <div class="live-card-bottom">
                                <div class="live-card-label">CARDHOLDER</div>
                                <div id="mockupCardholder" class="live-card-name">ALEXANDER VANCE</div>
                                <div id="mockupSerial" class="live-card-serial">GT-9482-2026</div>
                            </div>
                        </div>
                        <div style="margin-top: 1.2rem; font-size: 0.85rem; color: var(--text-muted);">
                            ✦ 28.5g Solid Monolith • CC EAL6+ Certified Secure Element
                        </div>
                    </div>

                    <!-- Right: Configurator Controls -->
                    <div class="config-controls">
                        <!-- Metal Alloy Selector -->
                        <div style="margin-bottom: 1.5rem;">
                            <label style="font-size:0.88rem; font-weight:600; display:block; margin-bottom:0.6rem;">Select Precious Metal Finish:</label>
                            <div class="alloy-buttons-group">
                                <button class="alloy-pill-btn active" data-alloy="ceramic">Hermes Alabaster</button>
                                <button class="alloy-pill-btn" data-alloy="titanium">Pale Titanium</button>
                                <button class="alloy-pill-btn" data-alloy="champagne">Champagne Gold</button>
                                <button class="alloy-pill-btn" data-alloy="gold">24K Mirror Gold</button>
                                <button class="alloy-pill-btn" data-alloy="stealth">Stealth Black</button>
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

                        <a href="contact.html" class="btn-primary" style="width: 100%; justify-content: center; padding: 0.95rem; text-align: center;">
                            <span>Request Fleet Production Quote</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. WEIGHT SPECS COMPARATOR -->
    <section class="section-spacing weight-section" id="weight">
        <div class="container">
            <div class="section-header-center">
                <div class="calm-tag">Physical Gravitas</div>
                <h2 class="serif-title">The unmistakable heft of quality.</h2>
                <p class="section-subtitle">
                    The tactile difference between commercial plastic and solid Grade-5 titanium monoliths.
                </p>
            </div>

            <div class="comparator-row">
                <div class="comparator-card">
                    <span style="font-size:0.8rem; color:var(--text-dim); text-transform:uppercase; font-weight:600;">Commercial Plastic</span>
                    <div class="weight-display" style="color: #94a3b8;">5.0g</div>
                    <div style="font-size:0.95rem; font-weight:700; color:var(--text-muted); margin-bottom:1rem;">Standard PVC Plastic</div>
                    <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">Prone to flexing, corner delamination, and rapid surface wear over time.</p>
                </div>
                <div class="comparator-card">
                    <span style="font-size:0.8rem; color:var(--text-dim); text-transform:uppercase; font-weight:600;">Hybrid Metal Card</span>
                    <div class="weight-display" style="color: #64748b;">16.0g</div>
                    <div style="font-size:0.95rem; font-weight:700; color:var(--text-muted); margin-bottom:1rem;">Steel Veneer + Plastic Core</div>
                    <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">Thin metal veneer laminated over a synthetic plastic substrate for mid-tier banking.</p>
                </div>
                <div class="comparator-card featured">
                    <span style="font-size:0.8rem; color:var(--accent-hermes); text-transform:uppercase; font-weight:700;">GenTech Sovereign</span>
                    <div class="weight-display gradient-text">28.5g</div>
                    <div style="font-size:0.95rem; font-weight:700; color:var(--accent-hermes); margin-bottom:1rem;">100% Solid Grade-5 Titanium</div>
                    <p style="font-size:0.88rem; color:var(--text-main); font-weight:500;">Precision CNC milled from single-billet solid titanium monolith blocks, engineered for permanence.</p>
                </div>
            </div>
        </div>
    </section>

</main>
"""
index_html += get_footer().replace('<script src="assets/js/app.js?v=12.0"></script>', '<script src="assets/js/scene3d.js?v=12.0"></script>\n<script src="assets/js/app.js?v=12.0"></script>')

with open('/Users/ramay/gentech3-app/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Updated index.html with multi-page navigation successfully!")
