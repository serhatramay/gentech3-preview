import os

# Helper template components
def get_header(title, desc, active_nav=""):
    nav_home = "active" if active_nav == "home" else ""
    nav_about = "active" if active_nav == "about" else ""
    nav_services = "active" if active_nav == "services" else ""
    nav_products = "active" if active_nav == "products" else ""
    nav_hardware = "active" if active_nav == "hardware" else ""
    nav_contact = "active" if active_nav == "contact" else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>{title} | GenTech Global LLC</title>
    <meta name="description" content="{desc}">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
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
                <a href="index.html" class="nav-link {nav_home}">Home</a>
                <a href="about.html" class="nav-link {nav_about}">About &amp; Künye</a>
                <div class="nav-dropdown-wrapper">
                    <a href="service.html" class="nav-link {nav_services}">Services ▾</a>
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
                <a href="products.html" class="nav-link {nav_products}">Products</a>
                <a href="hardware.html" class="nav-link {nav_hardware}">Hardware &amp; 5G</a>
                <a href="contact.html" class="nav-link {nav_contact}">Contact</a>
            </div>

            <div class="nav-actions">
                <a href="contact.html" class="btn-primary nav-cta">
                    <span>Inquire Fleet</span>
                </a>
            </div>
        </nav>
    </div>
</header>
"""

def get_page_banner(title, sub, crumb):
    return f"""
<div class="page-banner-header">
    <div class="container">
        <div class="calm-tag" style="margin-bottom: 0.8rem;">✦ GenTech Global LLC • Dubai Engineering Center</div>
        <h1 class="serif-title page-banner-title">{title}</h1>
        <p class="page-banner-sub">{sub}</p>
        <div class="breadcrumbs-trail">
            <a href="index.html">Home</a> <span>/</span> <span class="current-crumb">{crumb}</span>
        </div>
    </div>
</div>
"""

def get_footer():
    return """
<footer class="footer-serene">
    <div class="container">
        <div class="footer-top-grid">
            <div class="footer-col-main">
                <div class="nav-brand" style="margin-bottom: 1rem;">
                    <div class="nav-brand-dot"></div>
                    <div class="brand-text">
                        <span class="brand-title">GENTECH</span>
                        <span class="brand-sub">GLOBAL LLC</span>
                    </div>
                </div>
                <p style="font-size: 0.9rem; color: #B8ADA5; max-width: 320px; line-height: 1.6;">
                    Innovative technology house founded in Dubai (Q1 2025). Specializing in payment systems, precious metal cards, 5G SIMs, and wearable payment technologies.
                </p>
                <div style="font-size: 0.85rem; color: #8C8077; margin-top: 1rem;">
                    Ras Al Khaimah Economic Zone, Dubai, UAE • <a href="mailto:info@gentech.ae" style="color: #EB651A;">info@gentech.ae</a>
                </div>
            </div>

            <div class="footer-col">
                <h4 class="footer-title">Services (9)</h4>
                <ul class="footer-list">
                    <li><a href="emvcards.html">Smart &amp; EMV Cards</a></li>
                    <li><a href="metalcards.html">Metal &amp; Titanium Cards</a></li>
                    <li><a href="ceramiccards.html">Ceramic Cards</a></li>
                    <li><a href="chipmodules.html">Custom Chip Modules</a></li>
                    <li><a href="wearable.html">Wearable Payment Devices</a></li>
                    <li><a href="transport.html">Transport &amp; City Cards</a></li>
                    <li><a href="telecom.html">Telecommunications (5G SIM)</a></li>
                    <li><a href="hardware.html">Banking Hardware &amp; POS</a></li>
                    <li><a href="chip.html">Card &amp; Chip Integration</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4 class="footer-title">Products (7 Categories)</h4>
                <ul class="footer-list">
                    <li><a href="products.html">PVC &amp; Shell Foil Cards</a></li>
                    <li><a href="products.html">Titanium Monolith Cards</a></li>
                    <li><a href="products.html">Zirconia Ceramic Cards</a></li>
                    <li><a href="products.html">Super NFC 5G SIM</a></li>
                    <li><a href="products.html">Contactless Payment Stickers</a></li>
                    <li><a href="products.html">Smart Health Ceramic Rings</a></li>
                    <li><a href="products.html">Smart Ceramic Wristbands</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4 class="footer-title">Corporate &amp; Legal</h4>
                <ul class="footer-list">
                    <li><a href="about.html">About GenTech Global</a></li>
                    <li><a href="about.html#mission">Mission &amp; Vision</a></li>
                    <li><a href="about.html#pillars">6 Corporate Pillars</a></li>
                    <li><a href="index.html#configurator">3D Card Studio</a></li>
                    <li><a href="index.html#weight">Physical Gravitas Specs</a></li>
                    <li><a href="contact.html">Contact &amp; Dubai Desk</a></li>
                </ul>
            </div>
        </div>

        <div class="footer-compliance-bar">
            <div style="font-size: 0.82rem; font-weight: 700; color: var(--accent-hermes); text-transform: uppercase; letter-spacing: 0.05em;">
                Global Standards Compliance:
            </div>
            <div class="footer-standards-list">
                <span>EMVCo Level 1 &amp; 2</span>
                <span>PCI-DSS Level 1</span>
                <span>ISO/IEC 7810</span>
                <span>ISO/IEC 7811</span>
                <span>ISO/IEC 7813</span>
                <span>ISO/IEC 14443 Type A/B</span>
                <span>MIFARE &amp; FeliCa</span>
                <span>GSMA 5G Standalone</span>
            </div>
        </div>

        <div class="footer-bottom-row">
            <div>&copy; 2025–2026 GenTech Global LLC. All rights reserved. Registered in RAKEZ, Dubai, United Arab Emirates.</div>
            <div>GenTech 3 • Serene Hermes Warm Light Suite</div>
        </div>
    </div>
</footer>

<!-- Scripts -->
<script src="assets/js/app.js?v=12.0"></script>
</body>
</html>
"""

# ----------------------------------------------------
# 1. ABOUT.HTML
# ----------------------------------------------------
about_html = get_header("About Us & Corporate Künye", "Learn about GenTech Global LLC founded in Dubai Q1 2025, specializing in sovereign payment technologies.", "about")
about_html += get_page_banner("About GenTech Global LLC", "Pioneering sovereign payment systems, wearable devices, and smart cards from Dubai.", "About Us")
about_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        
        <!-- Story & Identity Grid -->
        <div class="about-hero-grid" style="margin-bottom: 4rem;">
            <div class="about-story-card">
                <div class="about-img-box">
                    <img src="assets/images/about.png" alt="GenTech Global Dubai HQ" class="about-img">
                </div>
                <div class="about-story-content">
                    <h2 class="serif-title" style="margin-bottom: 1rem;">Who We Are</h2>
                    <p>
                        <strong>GENTECH Global LLC</strong> is an innovative technology company founded in Dubai in the first quarter of 2025, specializing in payment systems, precious metal cards, and wearable payment technologies.
                    </p>
                    <p>
                        We develop smart and secure payment solutions that simplify financial experiences. Our products include contactless payment cards, wearable payment devices, and digital identity systems designed for banks, financial institutions, telecoms, and global sovereign brands.
                    </p>
                    <p>
                        With a user-centered ergonomic approach and bank-grade security standards, we bring the future of payment technology to the present day.
                    </p>

                    <div class="corporate-meta-box">
                        <div class="meta-row">
                            <span class="meta-label">Legal Name:</span>
                            <span class="meta-val">GENTECH GLOBAL LLC</span>
                        </div>
                        <div class="meta-row">
                            <span class="meta-label">Headquarters:</span>
                            <span class="meta-val">Ras Al Khaimah Economic Zone (RAKEZ), Dubai, UAE</span>
                        </div>
                        <div class="meta-row">
                            <span class="meta-label">Established:</span>
                            <span class="meta-val">First Quarter 2025 (Q1 2025)</span>
                        </div>
                        <div class="meta-row">
                            <span class="meta-label">Operating Schedule:</span>
                            <span class="meta-val">Monday – Friday : 09:00 AM – 09:00 PM (GST)</span>
                        </div>
                        <div class="meta-row">
                            <span class="meta-label">Direct Contact:</span>
                            <span class="meta-val"><a href="mailto:info@gentech.ae">info@gentech.ae</a></span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="mission-vision-container" id="mission">
                <div class="mv-card">
                    <div class="mv-icon">🎯</div>
                    <h3 class="serif-title">Our Mission</h3>
                    <p>To make life easier and transactions frictionless through secure, innovative, and sustainable payment technologies.</p>
                </div>
                <div class="mv-card">
                    <div class="mv-icon">🌍</div>
                    <h3 class="serif-title">Our Vision</h3>
                    <p>To become the leading global brand in wearable, smart card, and digital payment mobility solutions.</p>
                </div>
                <div class="mv-card" style="background: var(--bg-card-subtle);">
                    <div class="mv-icon">🛡️</div>
                    <h3 class="serif-title">Certified Security</h3>
                    <p>All facilities and hardware comply strictly with EMVCo Level 1 & 2, PCI-DSS Level 1, ISO/IEC 7810/7811/7813, and CQM reliability frameworks.</p>
                </div>
            </div>
        </div>

        <!-- 6 Pillars -->
        <div id="pillars" style="margin-top: 5rem;">
            <div class="section-header-center">
                <div class="calm-tag">Our 6 Core Capabilities</div>
                <h2 class="serif-title">Why Global Institutions Choose GenTech</h2>
                <p class="section-subtitle">A synthesis of precision engineering, international compliance, and local Dubai responsiveness.</p>
            </div>

            <div class="pillars-grid-6">
                <div class="pillar-card">
                    <div class="pillar-num">01</div>
                    <h4>Innovation-Driven Technology</h4>
                    <p>We combine advanced engineering and creative design to deliver next-generation payment and identification technologies from smart cards to wearable payment solutions.</p>
                </div>
                <div class="pillar-card">
                    <div class="pillar-num">02</div>
                    <h4>Proven Quality &amp; Security</h4>
                    <p>All our products meet international standards such as EMV, PCI DSS, and ISO, ensuring maximum data protection, durability, and reliability in every transaction.</p>
                </div>
                <div class="pillar-card">
                    <div class="pillar-num">03</div>
                    <h4>End-to-End Production Capability</h4>
                    <p>From chip module integration to final personalization, milling, and packaging, every stage of production is managed within our controlled and certified facilities.</p>
                </div>
                <div class="pillar-card">
                    <div class="pillar-num">04</div>
                    <h4>Customization &amp; Flexibility</h4>
                    <p>We design tailor-made hardware and software solutions for banks, telecom operators, governments, and enterprises adapting to your brand and technical requirements.</p>
                </div>
                <div class="pillar-card">
                    <div class="pillar-num">05</div>
                    <h4>Global Expertise, Local Support</h4>
                    <p>With our international network and regional partners, we offer global technology backed by local expertise and responsive support teams.</p>
                </div>
                <div class="pillar-card">
                    <div class="pillar-num">06</div>
                    <h4>Sustainable Innovation</h4>
                    <p>We are committed to environmentally conscious manufacturing, using eco-friendly materials such as rPVC, PLA bioplastics, and ocean-bound plastics in all our production lines.</p>
                </div>
            </div>
        </div>

        <!-- CTA Box -->
        <div class="page-cta-box" style="margin-top: 5rem; text-align: center; background: #FFFFFF; padding: 3rem; border-radius: var(--radius-lg); border: 1px solid var(--border-light); box-shadow: var(--shadow-card);">
            <h2 class="serif-title" style="margin-bottom: 1rem;">Ready to Commission Your Fleet?</h2>
            <p style="color: var(--text-muted); max-width: 600px; margin: 0 auto 2rem auto;">Speak directly with our Dubai engineering team to arrange physical material sample boxes and technical briefings.</p>
            <a href="contact.html" class="btn-primary" style="padding: 0.85rem 2rem;"><span>Contact Dubai Desk →</span></a>
        </div>

    </div>
</main>
"""
about_html += get_footer()
with open('/Users/ramay/gentech3-app/about.html', 'w', encoding='utf-8') as f:
    f.write(about_html)


# ----------------------------------------------------
# 2. SERVICE.HTML (SERVICES HUB)
# ----------------------------------------------------
service_html = get_header("Our Services", "Comprehensive suite of 9 payment, smart card, and wearable technologies by GenTech Global.", "services")
service_html += get_page_banner("Our Services Suite", "Nine specialized pillars of physical, digital, and biometric exchange.", "Services")
service_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="section-header-center">
            <div class="calm-tag">Enterprise Ecosystem</div>
            <h2 class="serif-title">Tailor-Made Solutions for Banks &amp; Telecoms</h2>
            <p class="section-subtitle">Click on any service below to explore detailed technical specifications, materials, and production capabilities.</p>
        </div>

        <div class="services-grid-9">
            <!-- 1 -->
            <div class="service-card-item">
                <div class="service-img-wrap">
                    <img src="assets/images/service-1.jpg" alt="Smart & EMV Cards">
                    <span class="service-tag">Core Banking</span>
                </div>
                <div class="service-body">
                    <h3 class="service-title">Smart &amp; EMV Cards</h3>
                    <p class="service-desc">Certified payment cards supporting Visa, Mastercard, and Discover networks. Produced with advanced security chips and eco-friendly rPVC, PLA, and ocean plastics.</p>
                    <a href="emvcards.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Explore EMV Cards →</a>
                </div>
            </div>

            <!-- 2 -->
            <div class="service-card-item">
                <div class="service-img-wrap">
                    <img src="assets/images/service-7.jpg" alt="Metal Cards">
                    <span class="service-tag">Tactile Luxury</span>
                </div>
                <div class="service-body">
                    <h3 class="service-title">Metal Cards</h3>
                    <p class="service-desc">Exclusive metal bank cards offering a superior tactile experience compared to standard PVC, typically designed for premium, private, and VIP banking portfolios.</p>
                    <a href="metalcards.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Explore Metal Cards →</a>
                </div>
            </div>

            <!-- 3 -->
            <div class="service-card-item">
                <div class="service-img-wrap">
                    <img src="assets/images/service-8.jpg" alt="Ceramic Cards">
                    <span class="service-tag">High Precision</span>
                </div>
                <div class="service-body">
                    <h3 class="service-title">Ceramic Cards</h3>
                    <p class="service-desc">Ceramic smart cards produced from high-performance engineering ceramics such as alumina and zirconia, offering extreme hardness, silky touch, and scratch immunity.</p>
                    <a href="ceramiccards.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Explore Ceramic Cards →</a>
                </div>
            </div>

            <!-- 4 -->
            <div class="service-card-item">
                <div class="service-img-wrap">
                    <img src="assets/images/service-9.jpg" alt="Chip Modules">
                    <span class="service-tag">Artisan Hardware</span>
                </div>
                <div class="service-body">
                    <h3 class="service-title">Chip Modules</h3>
                    <p class="service-desc">We can customize chip modules with your corporate logo or symbol representing your audience. 24K gold flash mirror plating crafted for elite brand identity.</p>
                    <a href="chipmodules.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Explore Chip Modules →</a>
                </div>
            </div>

            <!-- 5 -->
            <div class="service-card-item">
                <div class="service-img-wrap">
                    <img src="assets/images/service-2.jpg" alt="Wearable Payment Devices">
                    <span class="service-tag">Biometrics & NFC</span>
                </div>
                <div class="service-body">
                    <h3 class="service-title">Wearable Payment Devices</h3>
                    <p class="service-desc">Innovative wristbands, smart rings, and key fobs designed for convenient contactless transactions — combining luxury jewelry aesthetics with EMV technology.</p>
                    <a href="wearable.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Explore Wearables →</a>
                </div>
            </div>

            <!-- 6 -->
            <div class="service-card-item">
                <div class="service-img-wrap">
                    <img src="assets/images/service-3.jpg" alt="Transport & City Cards">
                    <span class="service-tag">Smart Mobility</span>
                </div>
                <div class="service-body">
                    <h3 class="service-title">Transport &amp; City Cards</h3>
                    <p class="service-desc">Integrated contactless smart cards for public transportation systems, offering sub-50ms gate latency, rapid passenger throughput, and Account-Based Ticketing (ABT).</p>
                    <a href="transport.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Explore Transit Cards →</a>
                </div>
            </div>

            <!-- 7 -->
            <div class="service-card-item">
                <div class="service-img-wrap">
                    <img src="assets/images/service-4.jpg" alt="Telecommunications">
                    <span class="service-tag">5G & IoT</span>
                </div>
                <div class="service-body">
                    <h3 class="service-title">Telecommunications</h3>
                    <p class="service-desc">GSM, 5G, and IoT SIM cards with dedicated operator profiles, alongside our breakthrough Super NFC SIM unifying cellular, transit, and banking on one chip.</p>
                    <a href="telecom.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Explore 5G Telecom →</a>
                </div>
            </div>

            <!-- 8 -->
            <div class="service-card-item">
                <div class="service-img-wrap">
                    <img src="assets/images/service-5.jpg" alt="Banking Hardware">
                    <span class="service-tag">Terminal Fleet</span>
                </div>
                <div class="service-body">
                    <h3 class="service-title">Hardware &amp; POS</h3>
                    <p class="service-desc">Banking hardware refers to the physical devices and systems used by financial institutions to enable secure, efficient payment processing: POS, QR sound box, and cloud printers.</p>
                    <a href="hardware.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Explore Hardware →</a>
                </div>
            </div>

            <!-- 9 -->
            <div class="service-card-item">
                <div class="service-img-wrap">
                    <img src="assets/images/service-6.jpg" alt="Card & Chip Integration">
                    <span class="service-tag">Personalization</span>
                </div>
                <div class="service-body">
                    <h3 class="service-title">Card &amp; Chip Integration</h3>
                    <p class="service-desc">Full control over chip module integration, prelam manufacturing, and personalization — enabling tailor-made solutions for banks, telecoms, and sovereign governments.</p>
                    <a href="chip.html" class="btn-primary" style="padding: 0.55rem 1.2rem; font-size: 0.82rem; margin-top: auto;">Explore Integration →</a>
                </div>
            </div>
        </div>
    </div>
</main>
"""
service_html += get_footer()
with open('/Users/ramay/gentech3-app/service.html', 'w', encoding='utf-8') as f:
    f.write(service_html)


# ----------------------------------------------------
# 3. PRODUCTS.HTML (CATALOG WITH TABS & LIGHTBOX)
# ----------------------------------------------------
products_html = get_header("Our Products Catalog", "Explore 22+ certified smart cards, titanium monoliths, ceramic rings, and 5G SIM cards.", "products")
products_html += get_page_banner("Our Products Catalog", "Precision-engineered smart cards, sovereign precious metals, and biometric wearables.", "Products")
products_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="section-header-center">
            <div class="calm-tag">Categorized Fleet</div>
            <h2 class="serif-title">Explore by Product Category</h2>
            <p class="section-subtitle">Filter through our certified fleet of PVC, Metal, Ceramic, 5G SIM, Stickers, Smart Rings, and Smart Wristbands.</p>
        </div>

        <!-- Filter Navigation Bar -->
        <div class="portfolio-filter-container">
            <button class="filter-btn active" data-filter="all">All Products (22)</button>
            <button class="filter-btn" data-filter="pvc">PVC Cards</button>
            <button class="filter-btn" data-filter="metal">Metal Cards</button>
            <button class="filter-btn" data-filter="ceramic">Ceramic Cards</button>
            <button class="filter-btn" data-filter="sim">GSM &amp; 5G SIM</button>
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
                    <h4 class="product-name">Encrypted Transit &amp; Access Sticker</h4>
                    <p class="product-brief">Multi-purpose RFID/NFC smart sticker for city transit, campus access, and micro-purchases.</p>
                    <div class="product-footer">
                        <span class="product-meta">MIFARE &amp; FeliCa Support</span>
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
                    <p class="product-brief">Wearable bracelet with modular ceramic links enabling fast contactless payments at gates &amp; POS.</p>
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
                    <h4 class="product-name">Executive Sport &amp; Luxury Wristband</h4>
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
</main>
"""
products_html += get_footer()
with open('/Users/ramay/gentech3-app/products.html', 'w', encoding='utf-8') as f:
    f.write(products_html)


# ----------------------------------------------------
# 4. CONTACT.HTML
# ----------------------------------------------------
contact_html = get_header("Contact & Dubai Desk", "Direct access to GenTech Global LLC engineering desk in RAKEZ Dubai.", "contact")
contact_html += get_page_banner("Contact Us", "Connect directly with our Dubai headquarters and global distribution desk.", "Contact")
contact_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="section-header-center">
            <div class="calm-tag">Global Headquarters</div>
            <h2 class="serif-title">Get in Touch with GenTech Desk</h2>
            <p class="section-subtitle">Request physical material sample boxes, batch volume timelines, or tailored technical specifications.</p>
        </div>

        <div class="contact-card-grid">
            <div class="contact-info-panel">
                <h3 class="serif-title" style="margin-bottom: 1.5rem;">Corporate Impressum</h3>
                
                <div class="contact-detail-item">
                    <div class="detail-icon">📍</div>
                    <div>
                        <strong>Physical Address:</strong>
                        <p>Ras Al Khaimah Economic Zone (RAKEZ), Dubai, United Arab Emirates</p>
                    </div>
                </div>

                <div class="contact-detail-item">
                    <div class="detail-icon">⏰</div>
                    <div>
                        <strong>Working Schedule:</strong>
                        <p>Monday – Friday : 09:00 AM – 09:00 PM (Gulf Standard Time)</p>
                    </div>
                </div>

                <div class="contact-detail-item">
                    <div class="detail-icon">✉️</div>
                    <div>
                        <strong>Official Inquiries:</strong>
                        <p><a href="mailto:info@gentech.ae" style="color: var(--accent-hermes); font-weight: 700;">info@gentech.ae</a></p>
                    </div>
                </div>

                <div class="contact-detail-item">
                    <div class="detail-icon">📞</div>
                    <div>
                        <strong>Telephone:</strong>
                        <p>+971 (Dubai Corporate Desk)</p>
                    </div>
                </div>

                <div style="margin-top: 2.5rem; padding: 1.25rem; border-radius: var(--radius-md); background: rgba(235, 101, 26, 0.08); border: 1px solid rgba(235, 101, 26, 0.2);">
                    <strong style="color: var(--accent-hermes); font-size: 0.9rem; display: block; margin-bottom: 0.3rem;">✦ Global Sample Box Dispatch</strong>
                    <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">Physical sample presentation boxes containing titanium, ceramic, shell foil, and smart ring artifacts are prepared and dispatched internationally within 48 hours.</p>
                </div>
            </div>

            <div class="contact-form-panel">
                <h3 class="serif-title" style="margin-bottom: 1.5rem;">Direct Fleet Inquiry</h3>
                <form class="fleet-inquiry-form" onsubmit="event.preventDefault(); alert('Thank you for reaching GenTech Global LLC. Our Dubai engineering desk will contact you within 4 hours.');">
                    <div class="form-row-2">
                        <div class="form-group">
                            <label>Full Name *</label>
                            <input type="text" class="form-input-clean" placeholder="Alexander Vance" required>
                        </div>
                        <div class="form-group">
                            <label>Corporate Email *</label>
                            <input type="email" class="form-input-clean" placeholder="a.vance@bank.com" required>
                        </div>
                    </div>

                    <div class="form-row-2">
                        <div class="form-group">
                            <label>Institution / Enterprise *</label>
                            <input type="text" class="form-input-clean" placeholder="National Bank / Telco" required>
                        </div>
                        <div class="form-group">
                            <label>Interested Solution</label>
                            <select class="form-input-clean">
                                <option value="titanium">28.5g Sovereign Titanium Cards</option>
                                <option value="rings">Concave Titanium Smart Rings</option>
                                <option value="ceramic">High-Tech Ceramic Cards</option>
                                <option value="sim">Super NFC 5G SIM Cards</option>
                                <option value="transit">Transport &amp; City Transit Cards</option>
                                <option value="pos">POS Hardware &amp; QR Sound Box Z20</option>
                                <option value="sample">Physical Sample Presentation Box</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-group" style="margin-bottom: 1.5rem;">
                        <label>Scope, Volume &amp; Specifications</label>
                        <textarea class="form-input-clean" rows="5" placeholder="Please describe required quantities, security applet requirements, or custom finishing wishes..."></textarea>
                    </div>

                    <button type="submit" class="btn-primary" style="width: 100%; justify-content: center; padding: 1rem;">
                        <span>Transmit Enterprise Request</span>
                    </button>
                </form>
            </div>
        </div>
    </div>
</main>
"""
contact_html += get_footer()
with open('/Users/ramay/gentech3-app/contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)


# ----------------------------------------------------
# 5. EMVCARDS.HTML (SMART & EMV CARDS)
# ----------------------------------------------------
emvcards_html = get_header("Smart & EMV Cards", "Certified PVC, rPVC, PLA Bioplastic, and Shell Foil banking cards.", "services")
emvcards_html += get_page_banner("Smart &amp; EMV Cards", "Certified payment cards supporting Visa, Mastercard, and Discover networks.", "EMV Cards")
emvcards_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <div class="calm-tag">Certified Banking Hardware</div>
                <h2 class="serif-title" style="margin-bottom: 1.2rem;">PVC &amp; Eco-Friendly EMV Cards</h2>
                <p>
                    PVC (Polyvinyl Chloride) is the most widely used card printing material in the world, including bank cards (credit and debit cards), ID cards, and magnetic stripe cards. PVC has long been the backbone of the banking card industry, being cost-effective, reliable, and widely accepted.
                </p>
                <p>
                    However, growing environmental awareness and sustainability demands are pushing the industry toward greener alternatives. Today, many banks are beginning to offer eco-friendly card options and implement recycling programs for end-of-life cards.
                </p>

                <div class="detail-img-box" style="margin: 2rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-light);">
                    <img src="assets/images/emv.png" alt="EMV Card Architecture" style="width: 100%;">
                </div>

                <h3 class="serif-title" style="margin-top: 2rem; margin-bottom: 1rem;">Sustainable Alternatives to Standard PVC</h3>
                <div class="pillars-grid-6" style="grid-template-columns: repeat(2, 1fr); margin-bottom: 2.5rem;">
                    <div class="pillar-card">
                        <h4>Recycled PVC (rPVC)</h4>
                        <p>Made from post-industrial and post-consumer waste PVC, reducing the need for virgin raw petroleum materials by up to 85%.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Bioplastic (PLA)</h4>
                        <p>Derived from renewable resources such as cornstarch and sugarcane. Industrially compostable and ecologically neutral.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Ocean Plastic</h4>
                        <p>Produced from recycled plastic waste intercepted from coastal regions and marine ecosystems, certified by environmental auditors.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Polycarbonate (PC)</h4>
                        <p>Highly durable, tamper-evident thermoplastic material used for high-security sovereign identification and long-life cards.</p>
                    </div>
                </div>

                <h3 class="serif-title" style="margin-top: 2rem; margin-bottom: 1rem;">Shell Foil Decorative Technology</h3>
                <p>
                    <strong>Features:</strong> Noble 3D grain surface presentation, multi-color surface reflection, superior scratch protection, and customized layout sizes filled with natural shell texture elements.
                </p>
                <p>
                    <strong>Principle:</strong> Shell Foil is manufactured with PVC added through proprietary arrangement and handicraft processing methods, yielding a colorful, three-dimensional shell-like effect.
                </p>
                <p>
                    <strong>Application Field:</strong> Widely adopted by financial institutions for VIP bank cards, private wealth cards, and luxury membership credentials.
                </p>
                <p>
                    <strong>Physical Compliance:</strong> Full compliance with ISO/IEC 7810, ISO/IEC 7811, ISO/IEC 7813, and MasterCard/Visa CQM reliability criteria.
                </p>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 2rem 0;">
                    <img src="assets/images/shell.png" alt="Shell Foil Technology" style="border-radius: var(--radius-md); border: 1px solid var(--border-light);">
                    <img src="assets/images/shell-card.png" alt="Shell Card Inlay" style="border-radius: var(--radius-md); border: 1px solid var(--border-light);">
                </div>
            </div>

            <!-- Sidebar -->
            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <h4 class="serif-title" style="margin-bottom: 1rem;">Technical Specifications</h4>
                    <table class="modal-specs-table">
                        <tr><th>Networks</th><td>Visa, Mastercard, Discover</td></tr>
                        <tr><th>Secure Element</th><td>CC EAL6+ Certified</td></tr>
                        <tr><th>Substrates</th><td>PVC, rPVC, PLA, PC</td></tr>
                        <tr><th>Standards</th><td>ISO/IEC 7810, 7811, 7813</td></tr>
                        <tr><th>Reliability</th><td>CQM Tested</td></tr>
                    </table>
                    <a href="contact.html" class="btn-primary" style="width: 100%; justify-content: center; margin-top: 1.5rem;">
                        <span>Request EMV Card Quote</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</main>
"""
emvcards_html += get_footer()
with open('/Users/ramay/gentech3-app/emvcards.html', 'w', encoding='utf-8') as f:
    f.write(emvcards_html)


# ----------------------------------------------------
# 6. METALCARDS.HTML (METAL & TITANIUM CARDS)
# ----------------------------------------------------
metalcards_html = get_header("Metal & Titanium Cards", "28.5g solid Grade-5 titanium monoliths and stainless steel bank cards.", "services")
metalcards_html += get_page_banner("Metal &amp; Titanium Cards", "Sovereign luxury, single-billet titanium CNC milling, and tactile gravitas.", "Metal Cards")
metalcards_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <div class="calm-tag">Precious Metallurgy</div>
                <h2 class="serif-title" style="margin-bottom: 1.2rem;">Solid Grade-5 Titanium &amp; Stainless Steel</h2>
                <p>
                    Metal bank cards are exclusive products that offer a superior tactile experience compared to standard PVC cards, typically designed for premium, private, or VIP banking customers.
                </p>
                <p>
                    GENTECH Global machines cards from single-billet Grade-5 aerospace titanium monoliths and heavy gauge stainless steel, creating the unmistakable heft of financial permanence.
                </p>

                <div class="detail-img-box" style="margin: 2rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-light);">
                    <img src="assets/images/metalcard.png" alt="Metal Card Monolith" style="width: 100%;">
                </div>

                <h3 class="serif-title" style="margin-top: 2rem; margin-bottom: 1rem;">Color Metallurgies &amp; Surface Finishes</h3>
                <p>
                    Our PVD (Physical Vapor Deposition) and electro-chemical coating facilities provide stunning metallic hues:
                </p>
                <div style="margin: 1.5rem 0;">
                    <img src="assets/images/metalcolor.png" alt="Metal Finishes" style="border-radius: var(--radius-md); border: 1px solid var(--border-light); max-width: 500px;">
                </div>

                <div class="pillars-grid-6" style="grid-template-columns: repeat(2, 1fr); margin-bottom: 2.5rem;">
                    <div class="pillar-card">
                        <h4>Stealth Brushed PVD Black</h4>
                        <p>Ultra-deep obsidian black coating with anti-fingerprint nano ceramic shield.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Pale Natural Titanium</h4>
                        <p>Raw satin brushed Grade-5 titanium alloy with mirror-polished chamfered edges.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>24K Mirror Champagne Gold</h4>
                        <p>Heavy gold flash plating with optical mirror reflectivity and laser engraved emblems.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Hybrid Metal Veneer</h4>
                        <p>16.0g stainless steel face bonded to composite core for dual-interface contactless agility.</p>
                    </div>
                </div>
            </div>

            <!-- Sidebar -->
            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <h4 class="serif-title" style="margin-bottom: 1rem;">Weight &amp; Specs</h4>
                    <table class="modal-specs-table">
                        <tr><th>Monolith Weight</th><td>28.5 Grams</td></tr>
                        <tr><th>Hybrid Weight</th><td>16.0 Grams</td></tr>
                        <tr><th>Base Alloy</th><td>Grade-5 Titanium (Ti-6Al-4V)</td></tr>
                        <tr><th>NFC Technology</th><td>Patented RF Booster</td></tr>
                        <tr><th>Engraving</th><td>Fiber Laser High-Def</td></tr>
                    </table>
                    <a href="contact.html" class="btn-primary" style="width: 100%; justify-content: center; margin-top: 1.5rem;">
                        <span>Request Metal Sample Box</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</main>
"""
metalcards_html += get_footer()
with open('/Users/ramay/gentech3-app/metalcards.html', 'w', encoding='utf-8') as f:
    f.write(metalcards_html)


# ----------------------------------------------------
# 7. CERAMICCARDS.HTML (CERAMIC CARDS)
# ----------------------------------------------------
ceramiccards_html = get_header("Ceramic Smart Cards", "High-performance Zirconia and Alumina engineering ceramic cards.", "services")
ceramiccards_html += get_page_banner("Ceramic Smart Cards", "Diamond-level scratch resistance and silky tactile touch.", "Ceramic Cards")
ceramiccards_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <div class="calm-tag">Engineering Ceramics</div>
                <h2 class="serif-title" style="margin-bottom: 1.2rem;">Zirconia &amp; Alumina Sintered Cards</h2>
                <p>
                    Ceramic smart cards are produced based on advanced ceramic materials (high-performance engineering ceramics such as alumina and zirconia). Sintered at temperatures exceeding 1,450°C, these cards possess a diamond-like hardness (Mohs 8.5+) and an unscratchable, silky surface.
                </p>

                <div class="detail-img-box" style="margin: 2rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-light);">
                    <img src="assets/images/ceramiccard.png" alt="Ceramic Card" style="width: 100%;">
                </div>

                <h3 class="serif-title" style="margin-top: 2rem; margin-bottom: 1rem;">Key Characteristics of Ceramic Banking Cards</h3>
                <ul class="service-bullets" style="font-size: 1rem; line-height: 2;">
                    <li><strong>Scratch Immunity:</strong> Resists keys, coins, and abrasive surfaces in everyday wallets.</li>
                    <li><strong>Electromagnetic Neutrality:</strong> Unlike metals, ceramic does not shield RF signals, providing superior NFC contactless tap distance and speed.</li>
                    <li><strong>Biocompatible &amp; Hypoallergenic:</strong> Completely chemically inert and pleasant to skin contact.</li>
                    <li><strong>Deep Color Saturation:</strong> Pure alabaster white, midnight onyx black, and custom bespoke pigments.</li>
                </ul>

                <div style="margin: 2rem 0;">
                    <img src="assets/images/ceramiccolor.png" alt="Ceramic Colors" style="border-radius: var(--radius-md); border: 1px solid var(--border-light); max-width: 500px;">
                </div>
            </div>

            <!-- Sidebar -->
            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <h4 class="serif-title" style="margin-bottom: 1rem;">Ceramic Specs</h4>
                    <table class="modal-specs-table">
                        <tr><th>Hardness</th><td>Mohs 8.5+ (Diamond Grade)</td></tr>
                        <tr><th>Material</th><td>Zirconia (ZrO2) / Alumina (Al2O3)</td></tr>
                        <tr><th>Finish</th><td>Mirror Gloss / Satin Matte</td></tr>
                        <tr><th>NFC Field</th><td>100% RF Transparent</td></tr>
                    </table>
                    <a href="contact.html" class="btn-primary" style="width: 100%; justify-content: center; margin-top: 1.5rem;">
                        <span>Inquire Ceramic Fleet</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</main>
"""
ceramiccards_html += get_footer()
with open('/Users/ramay/gentech3-app/ceramiccards.html', 'w', encoding='utf-8') as f:
    f.write(ceramiccards_html)


# ----------------------------------------------------
# 8. CHIPMODULES.HTML (CUSTOM CHIP MODULES)
# ----------------------------------------------------
chipmodules_html = get_header("Custom Chip Modules", "Laser-engraved contact surfaces with 24K gold flash mirror plating.", "services")
chipmodules_html += get_page_banner("Bespoke Chip Modules", "Custom laser contact geometries styled with your bank's logo or emblem.", "Chip Modules")
chipmodules_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <div class="calm-tag">Micro-Electronic Customization</div>
                <h2 class="serif-title" style="margin-bottom: 1.2rem;">Artisan Contact Geometry &amp; 24K Gold Plating</h2>
                <p>
                    We can customize the chip modules with your logo, crest, or a symbol that represents your audience or financial institution. Elevate your card from a commercial instrument to a bespoke work of technological art.
                </p>

                <div class="detail-img-box" style="margin: 2rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-light);">
                    <img src="assets/images/customize-chip.png" alt="Custom Chip Modules" style="width: 100%;">
                </div>

                <h3 class="serif-title" style="margin-top: 2rem; margin-bottom: 1rem;">Engineering Features</h3>
                <ul class="service-bullets" style="font-size: 1rem; line-height: 2;">
                    <li><strong>Laser Etched Trace Patterns:</strong> High-precision micro-laser engraving creating distinct geometric crests.</li>
                    <li><strong>Precious Metallurgies:</strong> 24K Flash Gold, Platinum Palladium, Rose Gold, and Dark Ruthenium plating.</li>
                    <li><strong>Cryptographic Security:</strong> Dual-interface CC EAL6+ Certified chips with RSA 4096 / ECC coprocessors.</li>
                </ul>
            </div>

            <!-- Sidebar -->
            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <h4 class="serif-title" style="margin-bottom: 1rem;">Module Specs</h4>
                    <table class="modal-specs-table">
                        <tr><th>Security Level</th><td>CC EAL6+ / EMVCo L1 &amp; L2</td></tr>
                        <tr><th>Plating</th><td>24K Gold / Palladium</td></tr>
                        <tr><th>Form Factor</th><td>8-Pin / 6-Pin Dual Interface</td></tr>
                    </table>
                    <a href="contact.html" class="btn-primary" style="width: 100%; justify-content: center; margin-top: 1.5rem;">
                        <span>Inquire Custom Chips</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</main>
"""
chipmodules_html += get_footer()
with open('/Users/ramay/gentech3-app/chipmodules.html', 'w', encoding='utf-8') as f:
    f.write(chipmodules_html)


# ----------------------------------------------------
# 9. WEARABLE.HTML (WEARABLE PAYMENT DEVICES)
# ----------------------------------------------------
wearable_html = get_header("Wearable Payment Devices", "Concave titanium smart rings, ceramic wristbands, and NFC wearables.", "services")
wearable_html += get_page_banner("Wearable Payment Devices", "Next-generation contactless transactions combining convenience, security, and jewelry elegance.", "Wearables")
wearable_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <div class="calm-tag">Biometrics &amp; Wearables</div>
                <h2 class="serif-title" style="margin-bottom: 1.2rem;">Smart Rings &amp; Payment Wristbands</h2>
                <p>
                    Wearable payment devices represent the next generation of contactless transactions, combining convenience, security, and innovation in a single form factor. GENTECH Global designs and manufactures customized wearable payment solutions that integrate EMV-certified chips into stylish, durable, and user-friendly accessories — enabling seamless, secure payments anywhere.
                </p>

                <div class="detail-img-box" style="margin: 2rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-light);">
                    <img src="assets/images/wearable.png" alt="Wearable Payment Devices" style="width: 100%;">
                </div>

                <h3 class="serif-title" style="margin-top: 2rem; margin-bottom: 1rem;">Complete Product Range</h3>
                <div class="pillars-grid-6" style="grid-template-columns: repeat(2, 1fr); margin-bottom: 2.5rem;">
                    <div class="pillar-card">
                        <h4>Smart Rings</h4>
                        <p>Elegant, concave titanium and zirconia ceramic rings enabling instant NFC tap-and-pay with BioActive vital telemetry.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Smart Bracelets &amp; Bands</h4>
                        <p>Silicone, leather, or ceramic-based designs for fitness, lifestyle, and premium luxury portfolios.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Key Fobs &amp; Microtags</h4>
                        <p>Practical, durable designs for versatile everyday city transit and contactless payments.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Smart Watches &amp; Straps</h4>
                        <p>Fully integrated EMV payment chips supporting Visa, Mastercard, and closed-loop municipal systems.</p>
                    </div>
                </div>
            </div>

            <!-- Sidebar -->
            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <h4 class="serif-title" style="margin-bottom: 1rem;">Wearable Specs</h4>
                    <table class="modal-specs-table">
                        <tr><th>Power</th><td>Zero-Battery Passive NFC</td></tr>
                        <tr><th>Water Rating</th><td>5ATM / IP68 Waterproof</td></tr>
                        <tr><th>Sensors</th><td>BioActive PPG Optical</td></tr>
                        <tr><th>Tokenization</th><td>Visa / Mastercard Certified</td></tr>
                    </table>
                    <a href="contact.html" class="btn-primary" style="width: 100%; justify-content: center; margin-top: 1.5rem;">
                        <span>Inquire Wearables Fleet</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</main>
"""
wearable_html += get_footer()
with open('/Users/ramay/gentech3-app/wearable.html', 'w', encoding='utf-8') as f:
    f.write(wearable_html)


# ----------------------------------------------------
# 10. TRANSPORT.HTML (TRANSPORT & CITY CARDS)
# ----------------------------------------------------
transport_html = get_header("Transport & City Cards", "High-speed contactless transit cards for subways, metros, and buses.", "services")
transport_html += get_page_banner("Transport &amp; City Cards", "Sub-50ms gate latency, Account-Based Ticketing (ABT), and intermodal mobility.", "Transport")
transport_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <div class="calm-tag">Smart Mobility Systems</div>
                <h2 class="serif-title" style="margin-bottom: 1.2rem;">High-Speed Public Transit Ticketing</h2>
                <p>
                    A transport card, also known as a smart transit card, is a contactless smart card used as a ticket or payment tool for public transportation systems — such as buses, metros, trams, ferries, and trains.
                </p>
                <p>
                    It allows passengers to load credit, tap at gates or validators, and travel quickly without cash. These systems help reduce cash handling, speed up passenger throughput, enable accurate fare collection, and provide real-time operational data for city management.
                </p>

                <div class="detail-img-box" style="margin: 2rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-light);">
                    <img src="assets/images/transportcards.png" alt="Transport Cards" style="width: 100%;">
                </div>

                <h3 class="serif-title" style="margin-top: 2rem; margin-bottom: 1rem;">The Future of Smart City Cards</h3>
                <p>
                    Future systems engineered by GenTech focus on:
                </p>
                <ul class="service-bullets" style="font-size: 1rem; line-height: 2;">
                    <li><strong>Account-Based Ticketing (ABT):</strong> Fare calculation calculated in the cloud in real time.</li>
                    <li><strong>EMV Open-Loop Payments:</strong> Direct acceptance of bank credit cards at subway turnstiles.</li>
                    <li><strong>Intermodal Transport Integration:</strong> Single card for metro, ferry, bus, e-scooter, and civic parking.</li>
                    <li><strong>Sustainable Substrates:</strong> Recycled ocean plastic and durable polycarbonate.</li>
                </ul>
            </div>

            <!-- Sidebar -->
            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <h4 class="serif-title" style="margin-bottom: 1rem;">Transit Specs</h4>
                    <table class="modal-specs-table">
                        <tr><th>Gate Latency</th><td>&lt;50 Milliseconds</td></tr>
                        <tr><th>Standards</th><td>Calypso, MIFARE DESFire, FeliCa</td></tr>
                        <tr><th>Architecture</th><td>Open Loop EMV &amp; ABT</td></tr>
                    </table>
                    <a href="contact.html" class="btn-primary" style="width: 100%; justify-content: center; margin-top: 1.5rem;">
                        <span>Inquire Transit Cards</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</main>
"""
transport_html += get_footer()
with open('/Users/ramay/gentech3-app/transport.html', 'w', encoding='utf-8') as f:
    f.write(transport_html)


# ----------------------------------------------------
# 11. TELECOM.HTML (TELECOMMUNICATIONS & 5G SIM)
# ----------------------------------------------------
telecom_html = get_header("Telecommunications & 5G SIM", "5G SIM cards, IoT data modules, and unified Super NFC 5G SIMs.", "services")
telecom_html += get_page_banner("Telecommunications", "5G cellular authentication, IoT fleet management, and Super NFC SIM cards.", "Telecom")
telecom_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <div class="calm-tag">5G &amp; IoT Cellular</div>
                <h2 class="serif-title" style="margin-bottom: 1.2rem;">SIM Cards &amp; Super NFC Architecture</h2>
                <p>
                    GENTECH provides highly reliable Internet of Things (IoT) cards, adopting operator-specific special number segments, supporting SMS, wireless data, and voice through private network element equipment, and providing user-independent terminal management.
                </p>
                <p>
                    A 5G SIM (Subscriber Identity Module) is an intelligent card used in 5G networks to authenticate the subscriber, ensure data security, and manage network connections.
                </p>

                <div class="detail-img-box" style="margin: 2rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-light);">
                    <img src="assets/images/5Gsim.png" alt="5G SIM Card" style="width: 100%;">
                </div>

                <h3 class="serif-title" style="margin-top: 2rem; margin-bottom: 1rem;">Super NFC SIM Innovation</h3>
                <p>
                    The Super NFC SIM is highly integrated with communication cards, subway and bus cards, bank cards, electronic ID cards, and one-card systems. Users enjoy secure, convenient mobile payments with a single device. Chip-level encryption provides enhanced security.
                </p>

                <div class="detail-img-box" style="margin: 2rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-light);">
                    <img src="assets/images/supersim.png" alt="Super NFC SIM" style="width: 100%;">
                </div>

                <h3 class="serif-title" style="margin-top: 2rem; margin-bottom: 1rem;">Key Product Features</h3>
                <ul class="service-bullets" style="font-size: 1rem; line-height: 2;">
                    <li>Supports full secondary applications (banking, transit, government ID).</li>
                    <li>Integrates multiple applications into one physical or eSIM card.</li>
                    <li>Supports multiple secure environments (Secure OS) with OTA remote updates.</li>
                    <li>Compliant with ISO/IEC 14443 Type A/B and GSMA 5G standards.</li>
                </ul>
            </div>

            <!-- Sidebar -->
            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <h4 class="serif-title" style="margin-bottom: 1rem;">Telecom Specs</h4>
                    <table class="modal-specs-table">
                        <tr><th>Networks</th><td>5G Standalone / NSA / 4G / GSM</td></tr>
                        <tr><th>SIM Types</th><td>Nano SIM / eSIM / Super NFC</td></tr>
                        <tr><th>NFC Chip</th><td>ISO/IEC 14443 Type A/B</td></tr>
                        <tr><th>Management</th><td>Remote Over-The-Air (OTA)</td></tr>
                    </table>
                    <a href="contact.html" class="btn-primary" style="width: 100%; justify-content: center; margin-top: 1.5rem;">
                        <span>Inquire 5G SIM Fleet</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</main>
"""
telecom_html += get_footer()
with open('/Users/ramay/gentech3-app/telecom.html', 'w', encoding='utf-8') as f:
    f.write(telecom_html)


# ----------------------------------------------------
# 12. HARDWARE.HTML (BANKING & POS HARDWARE)
# ----------------------------------------------------
hardware_html = get_header("Banking & Payment Hardware", "POS Terminals, QR Code Sound Box Z20, and Cloud Thermal Printers.", "hardware")
hardware_html += get_page_banner("Banking &amp; POS Hardware", "Payment terminals, smart audio QR sound boxes, and cloud printer fleets.", "Hardware")
hardware_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <div class="calm-tag">Transaction Terminals</div>
                <h2 class="serif-title" style="margin-bottom: 1.2rem;">POS Fleet &amp; Smart Payment Infrastructure</h2>
                <p>
                    Banking Hardware refers to the physical devices and systems used by financial institutions and merchant networks to enable secure, efficient, and reliable payment and transaction processing.
                </p>

                <h3 class="serif-title" style="margin-top: 2rem; margin-bottom: 1rem;">Types of POS Terminals</h3>
                <div class="pillars-grid-6" style="grid-template-columns: repeat(2, 1fr); margin-bottom: 2rem;">
                    <div class="pillar-card">
                        <h4>Countertop POS</h4>
                        <p>Fixed terminal connected via Ethernet or PSTN. Commonly deployed in retail stores, supermarkets, pharmacies, and hospitality venues.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Mobile POS (mPOS)</h4>
                        <p>Small, highly portable device connected via Bluetooth or mobile cellular data (4G/5G). Ideal for delivery couriers, taxis, and outdoor sales.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Smart Android POS</h4>
                        <p>Android-based device with a capacitive touchscreen interface. Supports invoicing, dynamic QR code payments, barcode cameras, and CRM apps.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Virtual POS</h4>
                        <p>High-security payment gateway for digital e-commerce websites and enterprise applications — no physical reader required.</p>
                    </div>
                </div>

                <div class="detail-img-box" style="margin: 2rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-light);">
                    <img src="assets/images/pos.png" alt="POS Terminals" style="width: 100%;">
                </div>

                <h3 class="serif-title" style="margin-top: 2.5rem; margin-bottom: 1rem;">QR Code Sound Box (Z20)</h3>
                <p>
                    Z20's sleek design and compact 2.4-inch front LCD display ensure clear visibility of dynamic QR codes, empowering customers to complete transactions effortlessly. With 4G/WiFi connectivity, enjoy uninterrupted access to payment networks for swift processing. Its high-decibel speaker broadcasts payment amounts instantly, eliminating merchant payment fraud.
                </p>

                <h3 class="serif-title" style="margin-top: 2.5rem; margin-bottom: 1rem;">Cloud Thermal Printers</h3>
                <p>
                    Cloud Print is a cloud-based printing technology that enables documents and receipts to be printed easily from any device over the internet without host cabling. Synchronizing with cloud servers, it enhances business agility, operational efficiency, and reduces paper waste.
                </p>
            </div>

            <!-- Sidebar -->
            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <h4 class="serif-title" style="margin-bottom: 1rem;">Hardware Specs</h4>
                    <table class="modal-specs-table">
                        <tr><th>Terminal Types</th><td>Countertop, mPOS, Smart Android</td></tr>
                        <tr><th>Sound Box</th><td>Z20 with 2.4" LCD + 4G/WiFi</td></tr>
                        <tr><th>Cloud Printing</th><td>Wireless Cloud Thermal</td></tr>
                        <tr><th>Certifications</th><td>PCI-PTS 6.x, EMV L1/L2, CE</td></tr>
                    </table>
                    <a href="contact.html" class="btn-primary" style="width: 100%; justify-content: center; margin-top: 1.5rem;">
                        <span>Inquire Hardware Fleet</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</main>
"""
hardware_html += get_footer()
with open('/Users/ramay/gentech3-app/hardware.html', 'w', encoding='utf-8') as f:
    f.write(hardware_html)


# ----------------------------------------------------
# 13. CHIP.HTML & PERSO.HTML (CARD & CHIP INTEGRATION)
# ----------------------------------------------------
chip_html = get_header("Card & Chip Integration", "Prelam manufacturing, chip embedding, laser personalization, and HSM security.", "services")
chip_html += get_page_banner("Card &amp; Chip Integration", "End-to-end personalization, prelam lamination, and cryptographic key injection.", "Chip Integration")
chip_html += """
<main class="page-content-wrapper">
    <div class="container section-spacing">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <div class="calm-tag">Certified Production Line</div>
                <h2 class="serif-title" style="margin-bottom: 1.2rem;">In-House Prelam &amp; Personalization Bureau</h2>
                <p>
                    Full control over chip module integration, prelam manufacturing, and personalization — enabling tailor-made solutions for banks, telecom operators, and sovereign governments.
                </p>

                <h3 class="serif-title" style="margin-top: 2rem; margin-bottom: 1rem;">Production Stages</h3>
                <div class="pillars-grid-6" style="grid-template-columns: repeat(2, 1fr); margin-bottom: 2rem;">
                    <div class="pillar-card">
                        <h4>Prelam Manufacturing</h4>
                        <p>Ultrasonic wire embedding and multi-layer sheet bonding creating robust composite antennas and chip cavities.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Laser Engraving &amp; Milling</h4>
                        <p>High-precision CNC cavity milling and fiber laser engraving of tactile cardholder typography and batch serials.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>HSM Cryptographic Key Injection</h4>
                        <p>Bank-grade Hardware Security Modules (FIPS 140-2 Level 3) injecting unique EMV cryptographic credentials.</p>
                    </div>
                    <div class="pillar-card">
                        <h4>Fulfillment &amp; Presentation</h4>
                        <p>Automated match-and-attach, tamper-evident courier sealing, and bespoke luxury packaging presentation boxes.</p>
                    </div>
                </div>

                <div class="detail-img-box" style="margin: 2rem 0; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-light);">
                    <img src="assets/images/service-6.jpg" alt="Card Personalization" style="width: 100%;">
                </div>
            </div>

            <!-- Sidebar -->
            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <h4 class="serif-title" style="margin-bottom: 1rem;">Facility Standards</h4>
                    <table class="modal-specs-table">
                        <tr><th>Security Level</th><td>Visa / Mastercard / PCI-CP</td></tr>
                        <tr><th>HSM Key Gen</th><td>FIPS 140-2 Level 3</td></tr>
                        <tr><th>Laser Tech</th><td>High-Speed Fiber Laser</td></tr>
                        <tr><th>Output Capacity</th><td>Multi-Million Units / Month</td></tr>
                    </table>
                    <a href="contact.html" class="btn-primary" style="width: 100%; justify-content: center; margin-top: 1.5rem;">
                        <span>Inquire Personalization Bureau</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</main>
"""
chip_html += get_footer()
with open('/Users/ramay/gentech3-app/chip.html', 'w', encoding='utf-8') as f:
    f.write(chip_html)
with open('/Users/ramay/gentech3-app/perso.html', 'w', encoding='utf-8') as f:
    f.write(chip_html)

print("Generated all standalone pages successfully!")
