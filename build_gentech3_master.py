import os

index_html_content = """<!DOCTYPE html>
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
    <link rel="stylesheet" href="assets/css/style.css?v=10.0">
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
                <a href="#overview" class="nav-link">Overview</a>
                <a href="#about" class="nav-link">About & Künye</a>
                <a href="#services" class="nav-link">Services (9)</a>
                <a href="#products" class="nav-link">Products</a>
                <a href="#hardware" class="nav-link">Hardware & 5G</a>
                <a href="#configurator" class="nav-link">3D Card Studio</a>
                <a href="#weight" class="nav-link">Specs</a>
                <a href="#contact" class="nav-link">Contact</a>
            </div>

            <div class="nav-actions">
                <a href="#contact" class="btn-primary nav-cta">
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
            <div class="calm-tag">✦ Dubai Engineering Center (RAKEZ) • Grade-5 Titanium & Biometric Wearables</div>
            <h1 class="serif-title">
                Calm technology. <br>
                <span class="gradient-text">Substance in every touch.</span>
            </h1>
            <p class="hero-description">
                A serene synthesis of 28.5g solid titanium cards, concave titanium smart rings with BioActive optical sensors, Super NFC 5G SIMs, and sub-50ms municipal transit cards — engineered with whisper-quiet precision in Dubai.
            </p>

            <div class="hero-cta-group">
                <a href="#configurator" class="btn-primary">Design Sovereign Card</a>
                <a href="#products" class="btn-secondary">Explore Product Fleet</a>
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
                    <div class="finish-selector" id="cardFinishSelector" style="display: none;">
                        <button class="finish-pill-btn card-finish-btn active" data-card-finish="stealth">Stealth Black</button>
                        <button class="finish-pill-btn card-finish-btn" data-card-finish="titanium">Pale Titanium</button>
                        <button class="finish-pill-btn card-finish-btn" data-card-finish="gold">24K Mirror Gold</button>
                        <button class="finish-pill-btn card-finish-btn" data-card-finish="ceramic">Hermes Ceramic</button>
                    </div>
                </div>
            </div>
            <div class="hero-hint">
                ✦ Drag to rotate artifacts in 3D space • Switch metal finishes & concave contours in real time
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
                <div class="calm-tag">Corporate Identity & Künye</div>
                <h2 class="serif-title">Pioneering the future of global exchange.</h2>
                <p class="section-subtitle">
                    Founded in Dubai in the first quarter of 2025, GENTECH Global LLC is an international technology house specializing in advanced payment systems, smart cards, and biometric wearable technologies.
                </p>
            </div>

            <!-- About Grid (2 Columns: Story & Mission/Vision) -->
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

            <!-- 6 Core Corporate Capability Pillars (Why Choose Us) -->
            <div style="margin-top: 4.5rem;">
                <div class="section-header-center" style="margin-bottom: 2.5rem;">
                    <div class="calm-tag">Core Capabilities</div>
                    <h2 class="serif-title" style="font-size: 2.1rem;">Why Sovereign Institutions Choose GenTech</h2>
                </div>

                <div class="pillars-grid-6">
                    <!-- 1 -->
                    <div class="pillar-card">
                        <div class="pillar-num">01</div>
                        <h4>Innovation-Driven Technology</h4>
                        <p>We combine precision micro-engineering and creative design to deliver next-generation payment and identification technologies — from smart cards to biometric wearable rings.</p>
                    </div>
                    <!-- 2 -->
                    <div class="pillar-card">
                        <div class="pillar-num">02</div>
                        <h4>Proven Quality & Security</h4>
                        <p>All our products meet international standards including EMVCo, PCI DSS, and ISO/IEC 7810/7811/7813, ensuring maximum cryptographic data protection, durability, and transaction reliability.</p>
                    </div>
                    <!-- 3 -->
                    <div class="pillar-card">
                        <div class="pillar-num">03</div>
                        <h4>End-to-End Production Capability</h4>
                        <p>From chip module integration and prelam manufacturing to laser personalization, milling, and secure packaging, every stage is executed within controlled and certified facilities.</p>
                    </div>
                    <!-- 4 -->
                    <div class="pillar-card">
                        <div class="pillar-num">04</div>
                        <h4>Customization & Enterprise Flexibility</h4>
                        <p>We design tailor-made hardware and software solutions for central banks, telecom operators, municipal governments, and enterprise clients, adapting to custom brand requirements.</p>
                    </div>
                    <!-- 5 -->
                    <div class="pillar-card">
                        <div class="pillar-num">05</div>
                        <h4>Global Expertise, Local Support</h4>
                        <p>With our international distribution network and regional partners, we deliver world-class technology backed by our responsive Dubai engineering support desk.</p>
                    </div>
                    <!-- 6 -->
                    <div class="pillar-card">
                        <div class="pillar-num">06</div>
                        <h4>Sustainable Innovation</h4>
                        <p>We are dedicated to environmentally conscious manufacturing, incorporating eco-friendly materials such as rPVC, PLA bioplastics, and ocean-bound plastics across all production lines.</p>
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
                    End-to-end payment and identification technologies engineered for banks, telecom operators, and municipal transit systems.
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
                        <h3 class="service-title">Smart & EMV Cards</h3>
                        <p class="service-desc">Certified payment cards supporting Visa, Mastercard, and Discover networks. Produced with advanced security chips and customizable eco-friendly materials.</p>
                        <ul class="service-bullets">
                            <li>Multi-layer durable lamination</li>
                            <li>Eco materials: rPVC, PLA & Ocean Plastic</li>
                            <li>Shell Foil 3D grain texture finishing</li>
                        </ul>
                        <button class="btn-detail-modal" data-modal="modal-service-emv">View Technical Specs →</button>
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
                        <ul class="service-bullets">
                            <li>Solid Grade-5 Titanium & Stainless Steel</li>
                            <li>Substantial heft up to 28.5 grams</li>
                            <li>Dual-interface hybrid antenna integration</li>
                        </ul>
                        <button class="btn-detail-modal" data-modal="modal-service-metal">View Technical Specs →</button>
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
                        <ul class="service-bullets">
                            <li>High-density Alumina & Zirconia ceramics</li>
                            <li>Diamond-level surface scratch resistance</li>
                            <li>Hypoallergenic & electromagnetic neutrality</li>
                        </ul>
                        <button class="btn-detail-modal" data-modal="modal-service-ceramic">View Technical Specs →</button>
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
                        <ul class="service-bullets">
                            <li>Laser-engraved proprietary contact geometries</li>
                            <li>24K gold flash mirror & palladium plating</li>
                            <li>Contact & dual-interface secure architectures</li>
                        </ul>
                        <button class="btn-detail-modal" data-modal="modal-service-chip">View Technical Specs →</button>
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
                        <ul class="service-bullets">
                            <li>Concave Titanium Smart Rings with BioActive sensors</li>
                            <li>Waterproof ceramic & silicone payment wristbands</li>
                            <li>Zero-battery passive NFC payment architecture</li>
                        </ul>
                        <button class="btn-detail-modal" data-modal="modal-service-wearable">View Technical Specs →</button>
                    </div>
                </div>

                <!-- Service 6 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-3.jpg" alt="Transport & City Cards">
                        <span class="service-tag">Smart Mobility</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Transport & City Cards</h3>
                        <p class="service-desc">Integrated contactless smart cards for public transportation systems, offering sub-50ms gate latency, rapid passenger throughput, and Account-Based Ticketing (ABT).</p>
                        <ul class="service-bullets">
                            <li>High-speed Calypso & MIFARE standard transit</li>
                            <li>Open-loop EMV transit payment integration</li>
                            <li>Multi-modal city card and parking token support</li>
                        </ul>
                        <button class="btn-detail-modal" data-modal="modal-service-transport">View Technical Specs →</button>
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
                        <ul class="service-bullets">
                            <li>5G Standalone & Non-Standalone authentication</li>
                            <li>Dedicated IoT connection management segments</li>
                            <li>Over-the-Air (OTA) secure multi-app updates</li>
                        </ul>
                        <button class="btn-detail-modal" data-modal="modal-service-telecom">View Technical Specs →</button>
                    </div>
                </div>

                <!-- Service 8 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-5.jpg" alt="Banking Hardware">
                        <span class="service-tag">Terminal Fleet</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Hardware & Terminals</h3>
                        <p class="service-desc">Physical devices and transaction processing hardware for financial institutions, including Countertop POS, mobile mPOS, QR Code Sound Boxes, and Cloud Printers.</p>
                        <ul class="service-bullets">
                            <li>Countertop, mPOS & Android Smart POS terminals</li>
                            <li>Z20 QR Code Sound Box with 2.4" LCD & 4G/WiFi</li>
                            <li>Cloud thermal printers for remote document syncing</li>
                        </ul>
                        <button class="btn-detail-modal" data-modal="modal-service-hardware">View Technical Specs →</button>
                    </div>
                </div>

                <!-- Service 9 -->
                <div class="service-card-item">
                    <div class="service-img-wrap">
                        <img src="assets/images/service-6.jpg" alt="Card & Chip Integration">
                        <span class="service-tag">Personalization</span>
                    </div>
                    <div class="service-body">
                        <h3 class="service-title">Card & Chip Integration</h3>
                        <p class="service-desc">Full control over chip module integration, prelam manufacturing, laser personalization, and Hardware Security Module (HSM) cryptographic key management.</p>
                        <ul class="service-bullets">
                            <li>Prelam manufacturing & antenna embedding</li>
                            <li>High-speed laser engraving & thermal printing</li>
                            <li>Bank-grade HSM key generation & validation</li>
                        </ul>
                        <button class="btn-detail-modal" data-modal="modal-service-integration">View Technical Specs →</button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. COMPLETE FILTERABLE PRODUCTS CATALOG (7 CATEGORIES, 20+ ITEMS) -->
    <section class="section-spacing products-section" id="products">
        <div class="container">
            <div class="section-header-center">
                <div class="calm-tag">Portfolio Showcase</div>
                <h2 class="serif-title">Our Products Catalog</h2>
                <p class="section-subtitle">
                    Explore our certified fleet of smart cards, precious metal monoliths, biometric rings, and telecom modules.
                </p>
            </div>

            <!-- Filter Navigation Bar -->
            <div class="portfolio-filter-container">
                <button class="filter-btn active" data-filter="all">All Products (22)</button>
                <button class="filter-btn" data-filter="pvc">PVC Cards</button>
                <button class="filter-btn" data-filter="metal">Metal Cards</button>
                <button class="filter-btn" data-filter="ceramic">Ceramic Cards</button>
                <button class="filter-btn" data-filter="sim">GSM & 5G SIM</button>
                <button class="filter-btn" data-filter="sticker">Payment Stickers</button>
                <button class="filter-btn" data-filter="ring">Smart Rings</button>
                <button class="filter-btn" data-filter="wristband">Smart Wristbands</button>
            </div>

            <!-- Products Grid (22 Items) -->
            <div class="products-portfolio-grid" id="portfolioGrid">
                
                <!-- Item 1 (PVC) -->
                <div class="product-item-card" data-category="pvc">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-1.png" alt="Shell Foil PVC Card" class="product-img">
                        <span class="product-badge">PVC Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Shell Foil PVC Cards (Noble Texture)</h4>
                        <p class="product-brief">PVC card enhanced with handcrafted 3D grain arrangement and shell-like iridescent light reflection.</p>
                        <div class="product-footer">
                            <span class="product-meta">ISO/IEC 7810 Compliant</span>
                        </div>
                    </div>
                </div>

                <!-- Item 2 (PVC) -->
                <div class="product-item-card" data-category="pvc">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-2.png" alt="Shell Foil PVC Card Pattern" class="product-img">
                        <span class="product-badge">PVC Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Shell Foil PVC Cards (Pattern Matrix)</h4>
                        <p class="product-brief">Decorative geometric shell foil finish providing high atmospheric elegance for VIP club cards.</p>
                        <div class="product-footer">
                            <span class="product-meta">Customizable Color Layout</span>
                        </div>
                    </div>
                </div>

                <!-- Item 3 (Metal) -->
                <div class="product-item-card" data-category="metal">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-3.png" alt="Titanium Cards" class="product-img">
                        <span class="product-badge">Metal Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Titanium Monolith Cards</h4>
                        <p class="product-brief">100% solid Grade-5 titanium body with brushed micro-texture and laser engraved typography.</p>
                        <div class="product-footer">
                            <span class="product-meta">28.5g Monolith Weight</span>
                        </div>
                    </div>
                </div>

                <!-- Item 4 (Metal) -->
                <div class="product-item-card" data-category="metal">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-4.png" alt="Stainless Steel Card" class="product-img">
                        <span class="product-badge">Metal Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Stainless Steel Cards</h4>
                        <p class="product-brief">Heavyweight stainless steel cards designed for sovereign private wealth and VIP cardholders.</p>
                        <div class="product-footer">
                            <span class="product-meta">Dual Interface NFC</span>
                        </div>
                    </div>
                </div>

                <!-- Item 5 (Metal) -->
                <div class="product-item-card" data-category="metal">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-5.png" alt="Stealth Metal Card" class="product-img">
                        <span class="product-badge">Metal Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Stealth Black Metal Hybrid</h4>
                        <p class="product-brief">Matte black PVD-coated steel face bonded to a precision composite core with embedded microchip.</p>
                        <div class="product-footer">
                            <span class="product-meta">16.0g Hybrid Weight</span>
                        </div>
                    </div>
                </div>

                <!-- Item 6 (Ceramic) -->
                <div class="product-item-card" data-category="ceramic">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-20.png" alt="Ceramic Credit Card" class="product-img">
                        <span class="product-badge">Ceramic Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Ceramic Credit Card (Zirconia)</h4>
                        <p class="product-brief">Engineered from sintered zirconia ceramic, yielding unscratchable surface luster and luxury density.</p>
                        <div class="product-footer">
                            <span class="product-meta">High Scratch Resistance</span>
                        </div>
                    </div>
                </div>

                <!-- Item 7 (Ceramic) -->
                <div class="product-item-card" data-category="ceramic">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-19.png" alt="Ceramic Cards Alumina" class="product-img">
                        <span class="product-badge">Ceramic Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Alumina White Ceramic Card</h4>
                        <p class="product-brief">Pristine white ceramic banking card with high dielectric constant and satin touch.</p>
                        <div class="product-footer">
                            <span class="product-meta">Electromagnetic Neutral</span>
                        </div>
                    </div>
                </div>

                <!-- Item 8 (SIM) -->
                <div class="product-item-card" data-category="sim">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-12.png" alt="Super NFC SIM" class="product-img">
                        <span class="product-badge">GSM / 5G SIM</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Super NFC 5G SIM Card</h4>
                        <p class="product-brief">Highly integrated module unifying 5G mobile communication, subway/bus transit, and bank cards.</p>
                        <div class="product-footer">
                            <span class="product-meta">OTA Multi-Application</span>
                        </div>
                    </div>
                </div>

                <!-- Item 9 (SIM) -->
                <div class="product-item-card" data-category="sim">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-11.png" alt="Normal 5G GSM SIM" class="product-img">
                        <span class="product-badge">GSM / 5G SIM</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Normal 5G GSM SIM Card</h4>
                        <p class="product-brief">Standard 5G intelligent card for high-speed network authentication, security keys, and IoT fleets.</p>
                        <div class="product-footer">
                            <span class="product-meta">High Cryptographic Sec</span>
                        </div>
                    </div>
                </div>

                <!-- Item 10 (Sticker) -->
                <div class="product-item-card" data-category="sticker">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-21.png" alt="NFC Payment Sticker" class="product-img">
                        <span class="product-badge">Sticker</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">NFC Contactless Payment Sticker</h4>
                        <p class="product-brief">Ultra-thin adhesive payment microtag attachable to smartphones and devices for tap-to-pay.</p>
                        <div class="product-footer">
                            <span class="product-meta">Anti-Metal Shield Layer</span>
                        </div>
                    </div>
                </div>

                <!-- Item 11 (Sticker) -->
                <div class="product-item-card" data-category="sticker">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-22.png" alt="Metallic Sticker" class="product-img">
                        <span class="product-badge">Sticker</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Metallic Branded Payment Sticker</h4>
                        <p class="product-brief">Metallic finish payment sticker customized with bank crest and EMV cryptographic applets.</p>
                        <div class="product-footer">
                            <span class="product-meta">Instant Micro-Payment</span>
                        </div>
                    </div>
                </div>

                <!-- Item 12 (Sticker) -->
                <div class="product-item-card" data-category="sticker">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-23.png" alt="Encrypted Sticker" class="product-img">
                        <span class="product-badge">Sticker</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Encrypted Transit & Access Sticker</h4>
                        <p class="product-brief">Multi-purpose RFID/NFC smart sticker for city transit, campus access, and micro-purchases.</p>
                        <div class="product-footer">
                            <span class="product-meta">MIFARE & FeliCa Support</span>
                        </div>
                    </div>
                </div>

                <!-- Item 13 (Ring) -->
                <div class="product-item-card" data-category="ring">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-6.png" alt="Smart Health Ceramic Ring Black" class="product-img">
                        <span class="product-badge">Smart Ring</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Smart Health Ceramic Ring (Black)</h4>
                        <p class="product-brief">Wearable electronic ring with integrated BioActive sensors monitoring health telemetry and NFC.</p>
                        <div class="product-footer">
                            <span class="product-meta">5ATM Waterproof</span>
                        </div>
                    </div>
                </div>

                <!-- Item 14 (Ring) -->
                <div class="product-item-card" data-category="ring">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-7.png" alt="Smart Health Ceramic Ring White" class="product-img">
                        <span class="product-badge">Smart Ring</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Smart Health Ceramic Ring (White)</h4>
                        <p class="product-brief">Ergonomic polished white ceramic ring delivering real-time sleep and vital biometrics.</p>
                        <div class="product-footer">
                            <span class="product-meta">Medical Grade Sensors</span>
                        </div>
                    </div>
                </div>

                <!-- Item 15 (Ring) -->
                <div class="product-item-card" data-category="ring">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-8.png" alt="Ceramic Ring Silver Accent" class="product-img">
                        <span class="product-badge">Smart Ring</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Smart Ceramic Ring (Silver Rim)</h4>
                        <p class="product-brief">Dual-tone ceramic and titanium ring combining fine jewelry design with tap payment chips.</p>
                        <div class="product-footer">
                            <span class="product-meta">Passive NFC Tap-to-Pay</span>
                        </div>
                    </div>
                </div>

                <!-- Item 16 (Ring) -->
                <div class="product-item-card" data-category="ring">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-9.png" alt="Smart Ceramic Ring Gold" class="product-img">
                        <span class="product-badge">Smart Ring</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Smart Ceramic Ring (Rose Gold)</h4>
                        <p class="product-brief">Rose gold bezel ceramic ring engineered for seamless institutional contactless payments.</p>
                        <div class="product-footer">
                            <span class="product-meta">Zero Battery Required</span>
                        </div>
                    </div>
                </div>

                <!-- Item 17 (Wristband) -->
                <div class="product-item-card" data-category="wristband">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-13.png" alt="Smart Ceramic Wristband" class="product-img">
                        <span class="product-badge">Smart Wristband</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Smart Ceramic Wristband</h4>
                        <p class="product-brief">Wearable bracelet with modular ceramic links enabling fast contactless payments at gates & POS.</p>
                        <div class="product-footer">
                            <span class="product-meta">EMVCo Level 2 Approved</span>
                        </div>
                    </div>
                </div>

                <!-- Item 18 (Wristband) -->
                <div class="product-item-card" data-category="wristband">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-14.png" alt="Executive Ceramic Wristband" class="product-img">
                        <span class="product-badge">Smart Wristband</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Executive Sport & Luxury Wristband</h4>
                        <p class="product-brief">High-durability silicone and ceramic composite wristband for festivals, resorts, and city transit.</p>
                        <div class="product-footer">
                            <span class="product-meta">Waterproof IP68</span>
                        </div>
                    </div>
                </div>

                <!-- Item 19 (PVC) -->
                <div class="product-item-card" data-category="pvc">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-15.png" alt="Metal Sticker PVC Card" class="product-img">
                        <span class="product-badge">PVC Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Metal Sticker PVC Cards</h4>
                        <p class="product-brief">Standard thickness PVC cards embedded with metal sticker accents and 3D metallic luster.</p>
                        <div class="product-footer">
                            <span class="product-meta">Cost-Effective Luxury</span>
                        </div>
                    </div>
                </div>

                <!-- Item 20 (PVC) -->
                <div class="product-item-card" data-category="pvc">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-17.png" alt="3D Coating PVC Cards" class="product-img">
                        <span class="product-badge">PVC Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">3D Coating PVC Cards</h4>
                        <p class="product-brief">Special UV tactile coating creating micro-embossed 3D textures across the card surface.</p>
                        <div class="product-footer">
                            <span class="product-meta">Anti-Scratch UV Finish</span>
                        </div>
                    </div>
                </div>

                <!-- Item 21 (PVC) -->
                <div class="product-item-card" data-category="pvc">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-18.png" alt="3D Coating PVC Cards Reflective" class="product-img">
                        <span class="product-badge">PVC Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">3D Coating Optical Depth Cards</h4>
                        <p class="product-brief">Reflective multi-angle light diffusion coating for high-security identity cards.</p>
                        <div class="product-footer">
                            <span class="product-meta">Holographic Security</span>
                        </div>
                    </div>
                </div>

                <!-- Item 22 (PVC) -->
                <div class="product-item-card" data-category="pvc">
                    <div class="product-img-box">
                        <img src="assets/images/portfolio-16.png" alt="Smart Card PVC" class="product-img">
                        <span class="product-badge">PVC Card</span>
                    </div>
                    <div class="product-info">
                        <h4 class="product-name">Standard Smart Card (PVC / rPVC)</h4>
                        <p class="product-brief">Certified chip-based smart payment card widely used by global banking and financial institutions.</p>
                        <div class="product-footer">
                            <span class="product-meta">Visa / Mastercard / Discover</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- 5. HARDWARE & TELECOM SHOWCASE (POS, QR SOUND BOX, CLOUD PRINTER, SUPER SIM) -->
    <section class="section-spacing hardware-section" id="hardware">
        <div class="container">
            <div class="section-header-center">
                <div class="calm-tag">Transaction Terminals & Infrastructure</div>
                <h2 class="serif-title">Hardware, POS & 5G Telecom Infrastructure</h2>
                <p class="section-subtitle">
                    Turnkey point-of-sale terminals, smart QR sound boxes, cloud printing systems, and unified 5G Super SIM cards.
                </p>
            </div>

            <!-- Hardware Showcase 2x2 Grid -->
            <div class="hardware-grid-4">
                
                <!-- HW 1: POS Terminals Fleet -->
                <div class="hardware-card">
                    <div class="hardware-img-box">
                        <img src="assets/images/pos.png" alt="POS Terminals Fleet">
                    </div>
                    <div class="hardware-body">
                        <span class="hw-pill">Payment Processing</span>
                        <h3 class="serif-title">POS Terminal Fleet</h3>
                        <p class="hw-text">
                            A complete range of electronic devices enabling secure, rapid credit card and contactless transactions for merchant networks.
                        </p>
                        <div class="hw-specs-list">
                            <div class="hw-spec-row">
                                <strong>Countertop POS:</strong> Fixed Ethernet/PSTN terminal for high-volume retail.
                            </div>
                            <div class="hw-spec-row">
                                <strong>Mobile POS (mPOS):</strong> Compact Bluetooth/4G/5G handheld for couriers & taxis.
                            </div>
                            <div class="hw-spec-row">
                                <strong>Smart Android POS:</strong> Touchscreen terminal supporting dynamic QR, cameras & e-invoicing.
                            </div>
                            <div class="hw-spec-row">
                                <strong>Virtual POS:</strong> Secure API gateway for e-commerce and mobile apps.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- HW 2: QR Code Sound Box Z20 -->
                <div class="hardware-card">
                    <div class="hardware-img-box">
                        <img src="assets/images/pos.png" alt="QR Code Sound Box Z20" style="filter: hue-rotate(30deg);">
                    </div>
                    <div class="hardware-body">
                        <span class="hw-pill">Instant Audio Broadcast</span>
                        <h3 class="serif-title">Z20 QR Code Sound Box</h3>
                        <p class="hw-text">
                            A sleek payment confirmation terminal with a 2.4-inch front LCD screen and high-volume audio broadcast for instant merchant verification.
                        </p>
                        <div class="hw-specs-list">
                            <div class="hw-spec-row">
                                <strong>Display:</strong> 2.4-inch high-contrast front LCD for dynamic QR display.
                            </div>
                            <div class="hw-spec-row">
                                <strong>Connectivity:</strong> 4G LTE & Wi-Fi dual network redundancy.
                            </div>
                            <div class="hw-spec-row">
                                <strong>Audio Engine:</strong> High-decibel crystal clear voice broadcast of paid amount.
                            </div>
                            <div class="hw-spec-row">
                                <strong>Security:</strong> Anti-fraud dynamic QR regeneration with chip encryption.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- HW 3: Cloud Printers -->
                <div class="hardware-card">
                    <div class="hardware-img-box">
                        <img src="assets/images/service-5.jpg" alt="Cloud Printer Solution">
                    </div>
                    <div class="hardware-body">
                        <span class="hw-pill">Cloud Printing Technology</span>
                        <h3 class="serif-title">Cloud Thermal Printer Solutions</h3>
                        <p class="hw-text">
                            Cloud-based printing technology enabling documents, kitchen orders, and transaction receipts to be printed seamlessly over the internet without host cables.
                        </p>
                        <div class="hw-specs-list">
                            <div class="hw-spec-row">
                                <strong>Cloud Sync:</strong> Direct API printing from any remote server or mobile app.
                            </div>
                            <div class="hw-spec-row">
                                <strong>Speed:</strong> High-speed thermal mechanism (&gt;220mm/sec) with auto-cutter.
                            </div>
                            <div class="hw-spec-row">
                                <strong>Sustainability:</strong> Energy-efficient design minimizing paper and power usage.
                            </div>
                            <div class="hw-spec-row">
                                <strong>Integration:</strong> Seamless compatibility with modern POS cloud architectures.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- HW 4: Super NFC 5G SIM -->
                <div class="hardware-card">
                    <div class="hardware-img-box">
                        <img src="assets/images/supersim.png" alt="Super NFC 5G SIM Architecture">
                    </div>
                    <div class="hardware-body">
                        <span class="hw-pill">Unified Multi-App SIM</span>
                        <h3 class="serif-title">Super NFC 5G SIM Architecture</h3>
                        <p class="hw-text">
                            A breakthrough single-chip architecture combining mobile telecommunications, subway/bus transit tokens, bank payment cards, and electronic IDs.
                        </p>
                        <div class="hw-specs-list">
                            <div class="hw-spec-row">
                                <strong>One-Card Integration:</strong> Telecom + Transit + Bank + e-ID on one physical/eSIM.
                            </div>
                            <div class="hw-spec-row">
                                <strong>Secure OS:</strong> Multi-tenant secure environment supporting ISO/IEC standards.
                            </div>
                            <div class="hw-spec-row">
                                <strong>OTA Management:</strong> Remote over-the-air applet updates and credentials.
                            </div>
                            <div class="hw-spec-row">
                                <strong>NFC Protocols:</strong> ISO/IEC 14443 Type A/B, MIFARE, and FeliCa formats.
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- 6. BESPOKE CARD BUILDER (LIVE 3D CONFIGURATOR) -->
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

                        <a href="#contact" class="btn-primary" style="width: 100%; justify-content: center; padding: 0.95rem; text-align: center;">
                            <span>Request Fleet Production Quote</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 7. WEIGHT SPECS COMPARATOR -->
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

    <!-- 8. ENTERPRISE CONTACT & CORPORATE DESK -->
    <section class="section-spacing contact-section" id="contact">
        <div class="container">
            <div class="section-header-center">
                <div class="calm-tag">Private Banking & Institutional Fleet</div>
                <h2 class="serif-title">Commission your institutional fleet.</h2>
                <p class="section-subtitle">
                    Connect with our Dubai engineering desk to request material sample boxes, volume production schedules, or bespoke hardware configurations.
                </p>
            </div>

            <div class="contact-card-grid">
                <!-- Left: Corporate Impressum / Künye Contact Info -->
                <div class="contact-info-panel">
                    <h3 class="serif-title" style="margin-bottom: 1.5rem;">Corporate Headquarters</h3>
                    
                    <div class="contact-detail-item">
                        <div class="detail-icon">📍</div>
                        <div>
                            <strong>Physical Headquarters:</strong>
                            <p>Ras Al Khaimah Economic Zone (RAKEZ), Dubai, United Arab Emirates</p>
                        </div>
                    </div>

                    <div class="contact-detail-item">
                        <div class="detail-icon">⏰</div>
                        <div>
                            <strong>Operational Hours:</strong>
                            <p>Monday – Friday : 09:00 AM – 09:00 PM (GST)</p>
                        </div>
                    </div>

                    <div class="contact-detail-item">
                        <div class="detail-icon">✉️</div>
                        <div>
                            <strong>Official Enterprise Email:</strong>
                            <p><a href="mailto:info@gentech.ae" style="color: var(--accent-hermes); font-weight: 600;">info@gentech.ae</a></p>
                        </div>
                    </div>

                    <div class="contact-detail-item">
                        <div class="detail-icon">📞</div>
                        <div>
                            <strong>Direct Engineering Desk:</strong>
                            <p><a href="tel:+971500000000" style="color: var(--text-main); font-weight: 600;">+971 (Dubai Corporate Line)</a></p>
                        </div>
                    </div>

                    <div style="margin-top: 2rem; padding: 1rem; border-radius: var(--radius-sm); background: rgba(235, 101, 26, 0.08); border: 1px solid rgba(235, 101, 26, 0.2);">
                        <span style="font-size: 0.85rem; font-weight: 600; color: var(--accent-hermes); display: block;">✦ Turnaround Schedule</span>
                        <span style="font-size: 0.8rem; color: var(--text-muted);">Sample boxes dispatched internationally within 48 hours via secure courier.</span>
                    </div>
                </div>

                <!-- Right: Fleet Inquiry Form -->
                <div class="contact-form-panel">
                    <h3 class="serif-title" style="margin-bottom: 1.5rem;">Direct Fleet Inquiry</h3>
                    
                    <form class="fleet-inquiry-form" onsubmit="event.preventDefault(); alert('Thank you for reaching GenTech Global LLC. Our Dubai engineering desk will contact you within 4 hours.');">
                        <div class="form-row-2">
                            <div class="form-group">
                                <label>Your Full Name *</label>
                                <input type="text" class="form-input-clean" placeholder="Alexander Vance" required>
                            </div>
                            <div class="form-group">
                                <label>Corporate Email *</label>
                                <input type="email" class="form-input-clean" placeholder="a.vance@bank.com" required>
                            </div>
                        </div>

                        <div class="form-row-2">
                            <div class="form-group">
                                <label>Institution / Organization *</label>
                                <input type="text" class="form-input-clean" placeholder="Emirates NBD / Telecom Corp" required>
                            </div>
                            <div class="form-group">
                                <label>Interested Fleet Product</label>
                                <select class="form-input-clean">
                                    <option value="titanium-cards">28.5g Sovereign Titanium Cards</option>
                                    <option value="smart-rings">Concave Titanium Smart Rings</option>
                                    <option value="ceramic-cards">Zirconia / Alumina Ceramic Cards</option>
                                    <option value="super-sim">Super NFC 5G SIM Cards</option>
                                    <option value="transit-cards">Municipal Transport & City Cards</option>
                                    <option value="hardware-pos">POS Terminals & QR Sound Box Z20</option>
                                    <option value="sample-box">Request Physical Material Sample Box</option>
                                </select>
                            </div>
                        </div>

                        <div class="form-group" style="margin-bottom: 1.5rem;">
                            <label>Project Scope & Estimated Fleet Volume</label>
                            <textarea class="form-input-clean" rows="4" placeholder="Describe card/wearable quantities, chip requirements, timeline, or bespoke packaging needs..."></textarea>
                        </div>

                        <button type="submit" class="btn-primary" style="width: 100%; justify-content: center; padding: 1rem;">
                            <span>Submit Enterprise Inquiry</span>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>
</main>

<!-- FOOTER WITH COMPLETE LEGAL KÜNYE AND COMPLIANCE STANDARDS -->
<footer class="footer-serene">
    <div class="container">
        <!-- Top Footer Grid -->
        <div class="footer-top-grid">
            <div class="footer-col-main">
                <div class="nav-brand" style="margin-bottom: 1rem;">
                    <div class="nav-brand-dot"></div>
                    <div class="brand-text">
                        <span class="brand-title">GENTECH</span>
                        <span class="brand-sub">GLOBAL LLC</span>
                    </div>
                </div>
                <p style="font-size: 0.9rem; color: var(--text-muted); max-width: 320px; line-height: 1.6;">
                    Innovative technology house founded in Dubai (Q1 2025). Specializing in payment systems, precious metal cards, and wearable payment technologies.
                </p>
                <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 1rem;">
                    Ras Al Khaimah Economic Zone, Dubai, UAE • info@gentech.ae
                </div>
            </div>

            <div class="footer-col">
                <h4 class="footer-title">Services</h4>
                <ul class="footer-list">
                    <li><a href="#services">Smart & EMV Cards</a></li>
                    <li><a href="#services">Metal Cards</a></li>
                    <li><a href="#services">Ceramic Cards</a></li>
                    <li><a href="#services">Custom Chip Modules</a></li>
                    <li><a href="#services">Wearable Payment Devices</a></li>
                    <li><a href="#services">Transport & City Cards</a></li>
                    <li><a href="#services">Telecommunications (5G SIM)</a></li>
                    <li><a href="#services">Banking Hardware & POS</a></li>
                    <li><a href="#services">Card & Chip Integration</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4 class="footer-title">Products</h4>
                <ul class="footer-list">
                    <li><a href="#products">PVC & Shell Foil Cards</a></li>
                    <li><a href="#products">Titanium Monolith Cards</a></li>
                    <li><a href="#products">Zirconia Ceramic Cards</a></li>
                    <li><a href="#products">Super NFC 5G SIM</a></li>
                    <li><a href="#products">Contactless Payment Stickers</a></li>
                    <li><a href="#products">Smart Health Ceramic Rings</a></li>
                    <li><a href="#products">Concave Titanium Rings</a></li>
                    <li><a href="#products">Smart Ceramic Wristbands</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4 class="footer-title">Corporate & Legal</h4>
                <ul class="footer-list">
                    <li><a href="#about">About GenTech Global</a></li>
                    <li><a href="#about">Mission & Vision</a></li>
                    <li><a href="#about">6 Corporate Pillars</a></li>
                    <li><a href="#configurator">Card Studio Configurator</a></li>
                    <li><a href="#weight">Physical Gravitas Specs</a></li>
                    <li><a href="#contact">Contact & Dubai Desk</a></li>
                </ul>
            </div>
        </div>

        <!-- Compliance Badges Bar -->
        <div class="footer-compliance-bar">
            <div style="font-size: 0.82rem; font-weight: 700; color: var(--accent-hermes); text-transform: uppercase; letter-spacing: 0.05em;">
                Global Standards Compliance:
            </div>
            <div class="footer-standards-list">
                <span>EMVCo Level 1 & 2</span>
                <span>PCI-DSS Level 1</span>
                <span>ISO/IEC 7810</span>
                <span>ISO/IEC 7811</span>
                <span>ISO/IEC 7813</span>
                <span>ISO/IEC 14443 Type A/B</span>
                <span>MIFARE & FeliCa</span>
                <span>GSMA 5G Standalone</span>
            </div>
        </div>

        <!-- Copyright Bottom -->
        <div class="footer-bottom-row">
            <div>&copy; 2025–2026 GenTech Global LLC. All rights reserved. Registered in RAKEZ, Dubai, United Arab Emirates.</div>
            <div>GenTech 3 • Serene Hermes Warm Light Master Edition</div>
        </div>
    </div>
</footer>

<!-- TECHNICAL DETAIL MODALS CONTAINER -->
<div class="modal-backdrop" id="modalBackdrop">
    <div class="modal-dialog" id="modalDialog">
        <button class="modal-close-btn" id="modalCloseBtn">&times;</button>
        <div class="modal-content" id="modalContent">
            <!-- Injected via JavaScript -->
        </div>
    </div>
</div>

<!-- Scripts -->
<script src="assets/js/scene3d.js?v=10.0"></script>
<script src="assets/js/app.js?v=10.0"></script>
</body>
</html>
"""

with open('/Users/ramay/gentech3-app/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html_content)

print("index.html successfully updated!")
