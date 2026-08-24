import os

# Helper template components
HEADER_TEMPLATE = """<!DOCTYPE html>
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
    <link rel="stylesheet" href="assets/css/style.css?v=11.0">
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

PAGE_HERO_TEMPLATE = """
<!-- Page Banner Header -->
<div class="page-banner-header">
    <div class="container">
        <div class="calm-tag" style="margin-bottom: 0.8rem;">✦ GenTech Global LLC • Dubai Engineering Desk</div>
        <h1 class="serif-title page-banner-title">{banner_title}</h1>
        <p class="page-banner-sub">{banner_sub}</p>
        <div class="breadcrumbs-trail">
            <a href="index.html">Home</a> <span>/</span> <span class="current-crumb">{crumb}</span>
        </div>
    </div>
</div>
"""

FOOTER_TEMPLATE = """
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
                <p style="font-size: 0.9rem; color: #B8ADA5; max-width: 320px; line-height: 1.6;">
                    Innovative technology company founded in Dubai (Q1 2025). Specializing in payment systems, precious metal cards, 5G SIMs, and wearable payment technologies.
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

        <!-- Compliance Badges Bar -->
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

        <!-- Copyright Bottom -->
        <div class="footer-bottom-row">
            <div>&copy; 2025–2026 GenTech Global LLC. All rights reserved. Registered in RAKEZ, Dubai, United Arab Emirates.</div>
            <div>GenTech 3 • Serene Hermes Warm Light Suite</div>
        </div>
    </div>
</footer>

<!-- Scripts -->
<script src="assets/js/app.js?v=11.0"></script>
</body>
</html>
"""

print("Helper templates initialized.")
