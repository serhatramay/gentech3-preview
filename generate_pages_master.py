import os
import sys

BASE_DIR = "/Users/ramay/gentech3-app"

# Import helper layout functions from build_all_gentech_group
from build_all_gentech_group import get_header, get_page_banner, get_footer, write_file

print("Starting generation of 20+ GENTECH GROUP pages...")

# ==============================================================================
# 1. INDEX.HTML — MASTER HOMEPAGE
# ==============================================================================
def build_index():
    header = get_header(
        title="Global Capital, Payment Technologies & Digital Infrastructure",
        desc="Gentech Group operates across Canada, UAE, and South Africa, uniting global holding governance, high-security payment manufacturing, and national-scale transit automation.",
        active_nav="home"
    )
    
    body = """

<!-- Hero Section -->
<section class="hero-section" id="overview">
    <div class="container">
        <div class="calm-tag">✦ GLOBAL CAPITAL • PAYMENT TECHNOLOGIES • DIGITAL INFRASTRUCTURE</div>
        <h1 class="serif-title">
            Architecting Sovereign Payment Technologies <br>
            <span class="gradient-text">&amp; Global Digital Infrastructure</span>
        </h1>
        <p class="hero-description">
            Gentech Group unifies Canadian investment governance, UAE high-security card and fintech engineering, and South Africa national-scale mobility operations into a singular, trusted global power.
        </p>

        <div class="hero-cta-group">
            <a href="#solutions" class="btn-primary">
                <span>Explore Solutions</span>
            </a>
            <a href="africa-national-mobility-program.html" class="btn-secondary">
                <span>South Africa National Program</span>
            </a>
            <a href="contact.html" class="btn-secondary">
                <span>Contact Corporate Hubs</span>
            </a>
        </div>

        <!-- Global Ticker -->
        <div style="text-align: center; margin-bottom: 2.5rem;">
            <div class="hero-hubs-ticker">
                <span>🍁 Toronto, Canada (Holding)</span>
                <span>•</span>
                <span>🇦🇪 Ras Al Khaimah, UAE (Tech &amp; Trade)</span>
                <span>•</span>
                <span>🇿🇦 Johannesburg, South Africa (Africa Hub)</span>
            </div>
        </div>

        <!-- 3D Studio Stage (Smart Ring & Titanium Card) -->
        <div class="hero-3d-box">
            <div id="canvas3D"></div>
            
            <div class="studio-toolbar">
                <div class="artifact-toggle-group">
                    <button class="toolbar-btn active artifact-toggle-btn" data-artifact="ring" aria-label="View Galaxy Smart Ring 3D">💍 Galaxy Smart Ring</button>
                    <button class="toolbar-btn artifact-toggle-btn" data-artifact="card" aria-label="View Titanium Card 3D">💳 Sovereign Titanium Card</button>
                </div>
                
                <!-- Ring Finish Sub-toolbar -->
                <div class="finish-selector" id="ringFinishSelector">
                    <button class="finish-pill-btn ring-finish-btn active" data-finish="silver" aria-label="Titanium Silver finish">Titanium Silver</button>
                    <button class="finish-pill-btn ring-finish-btn" data-finish="black" aria-label="Titanium Black finish">Titanium Black</button>
                    <button class="finish-pill-btn ring-finish-btn" data-finish="gold" aria-label="Titanium Gold finish">Titanium Gold</button>
                </div>

                <!-- Card Finish Sub-toolbar -->
                <div class="finish-selector hidden" id="cardFinishSelector">
                    <button class="finish-pill-btn card-finish-btn active" data-card-finish="stealth" aria-label="Stealth Black finish">Stealth Black</button>
                    <button class="finish-pill-btn card-finish-btn" data-card-finish="titanium" aria-label="Pale Titanium finish">Pale Titanium</button>
                    <button class="finish-pill-btn card-finish-btn" data-card-finish="gold" aria-label="24K Mirror Gold finish">24K Mirror Gold</button>
                    <button class="finish-pill-btn card-finish-btn" data-card-finish="ceramic" aria-label="Hermes Ceramic finish">Ceramic</button>
                </div>
            </div>
        </div>
        
        <div class="hero-hint">
            ✦ Drag to rotate artifacts in 3D space • Switch metal finishes &amp; concave contours in real time
        </div>
    </div>
</section>

<!-- Scale & Operational Metrics Bar -->
<section class="metrics-section">
    <div class="container">
        <div class="metrics-grid-5">
            <div class="metric-card-box">
                <div class="metric-val">3</div>
                <div class="metric-lbl">Global Hubs</div>
                <div class="metric-sub">Canada • UAE • South Africa</div>
            </div>
            <div class="metric-card-box">
                <div class="metric-val">10 YRS</div>
                <div class="metric-lbl">National Concession</div>
                <div class="metric-sub">South Africa Mobility &amp; Payments</div>
            </div>
            <div class="metric-card-box">
                <div class="metric-val">500,000</div>
                <div class="metric-lbl">Transit Fleet Target</div>
                <div class="metric-sub">Minibus Taxi Network Automation</div>
            </div>
            <div class="metric-card-box">
                <div class="metric-val">65,000,000</div>
                <div class="metric-lbl">Commuters Target</div>
                <div class="metric-sub">Daily Contactless Fare Access</div>
            </div>
            <div class="metric-card-box">
                <div class="metric-val">CC EAL6+</div>
                <div class="metric-lbl">Silicon Security</div>
                <div class="metric-sub">Hardware Cryptographic Trust</div>
            </div>
        </div>
    </div>
</section>

<!-- Executive Overview Section -->
<section class="section-spacing">
    <div class="container">
        <div style="max-width: 920px; margin: 0 auto; text-align: center;">
            <div class="calm-tag">CORPORATE PROFILE</div>
            <h2 class="serif-title" style="margin-bottom: 1.5rem; font-size: clamp(1.8rem, 3.8vw, 2.8rem);">
                A Global Powerhouse in Financial Technology, Hardware Precision &amp; Sovereign Operations
            </h2>
            <p style="font-size: 1.08rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 2rem;">
                Gentech Group operates at the convergence of technology engineering, high-security manufacturing, software architecture, capital mobilization, and large-scale field deployment. Across our global operational hubs in Canada, the United Arab Emirates, and South Africa, we design, deploy, and govern mission-critical financial technologies—delivering turnkey ecosystems for central banks, sovereign transport networks, commercial banks, and multinational telecom operators.
            </p>
            <div style="display: flex; gap: 1rem; justify-content: center;">
                <a href="about.html" class="btn-primary">
                    <span>Discover Gentech Group</span>
                </a>
                <a href="about.html#governance" class="btn-secondary">
                    <span>Holding Governance</span>
                </a>
            </div>
        </div>
    </div>
</section>

<!-- The 6 Core Solutions Pillars -->
<section class="section-spacing" id="solutions" style="background: var(--bg-card-subtle); border-top: 1px solid var(--border-light); border-bottom: 1px solid var(--border-light);">
    <div class="container">
        <div class="section-header-center">
            <div class="calm-tag">THE 6 CORE PILLARS</div>
            <h2 class="serif-title">Integrated Solutions &amp; Platforms</h2>
            <p class="section-subtitle">
                Engineered for sovereign security, high transaction velocity, and turnkey institutional deployment.
            </p>
        </div>

        <div class="solutions-grid-6">
            <!-- Pillar 1 -->
            <div class="pillar-card">
                <div class="pillar-num">PILLAR // 01</div>
                <h3 class="pillar-title">Cards &amp; Card Manufacturing</h3>
                <p class="pillar-desc">
                    Full-spectrum design, high-security personalization, and laser engraving for smart EMV, pure titanium, ceramic, and wearable payment products.
                </p>
                <ul class="pillar-features">
                    <li>Smart &amp; Contactless EMV Cards</li>
                    <li>Pure Titanium, Metal &amp; Ceramic Bodies</li>
                    <li>Wearable Payment Rings &amp; Accessories</li>
                    <li>Bespoke Laser-Engraved Chip Modules</li>
                </ul>
                <a href="solutions-cards.html" class="pillar-link">Explore Card Solutions →</a>
            </div>

            <!-- Pillar 2 -->
            <div class="pillar-card">
                <div class="pillar-num">PILLAR // 02</div>
                <h3 class="pillar-title">Payment Technologies</h3>
                <p class="pillar-desc">
                    Omnichannel acceptance infrastructure spanning ruggedized Android POS terminals, digital wallet tokenisation, and high-velocity payment gateways.
                </p>
                <ul class="pillar-features">
                    <li>Smart Android POS &amp; Mobile Terminals</li>
                    <li>NFC &amp; QR Multi-rail Acceptance</li>
                    <li>Digital Wallet &amp; Tokenisation Engines</li>
                    <li>Real-Time Settlement &amp; Anti-Fraud</li>
                </ul>
                <a href="solutions-payments.html" class="pillar-link">Explore Payment Tech →</a>
            </div>

            <!-- Pillar 3 -->
            <div class="pillar-card">
                <div class="pillar-num">PILLAR // 03</div>
                <h3 class="pillar-title">Smart Mobility Systems</h3>
                <p class="pillar-desc">
                    Turnkey Automated Fare Collection (AFC), Account-Based Ticketing (ABT), in-vehicle dual-bus validators, and driver operational telemetry consoles.
                </p>
                <ul class="pillar-features">
                    <li>Automated Fare Collection (AFC / ABT)</li>
                    <li>EMV Open-Loop &amp; Closed-Loop Tap</li>
                    <li>In-Vehicle Dual-Bus Validators</li>
                    <li>Fleet Telemetry &amp; Driver Consoles</li>
                </ul>
                <a href="solutions-mobility.html" class="pillar-link">Explore Mobility Systems →</a>
            </div>

            <!-- Pillar 4 -->
            <div class="pillar-card">
                <div class="pillar-num">PILLAR // 04</div>
                <h3 class="pillar-title">Telecommunications &amp; Connected Devices</h3>
                <p class="pillar-desc">
                    Next-generation cellular identity solutions, Super SIM 5G multi-IMSI architectures, eSIM remote management, and secure IoT telemetry modules.
                </p>
                <ul class="pillar-features">
                    <li>5G Super SIM &amp; Multi-IMSI Roaming</li>
                    <li>eSIM Remote Provisioning (RSP)</li>
                    <li>Connected Vehicle Telemetry Modules</li>
                    <li>M2M Cryptographic Security Hardware</li>
                </ul>
                <a href="solutions-telecom.html" class="pillar-link">Explore Telecom Solutions →</a>
            </div>

            <!-- Pillar 5 -->
            <div class="pillar-card">
                <div class="pillar-num">PILLAR // 05</div>
                <h3 class="pillar-title">Digital Infrastructure</h3>
                <p class="pillar-desc">
                    High-throughput clearing platforms, Hardware Security Module (HSM) key injection, sovereign identity systems, and big data transit analytics.
                </p>
                <ul class="pillar-features">
                    <li>Sovereign Cloud &amp; Clearing Infrastructure</li>
                    <li>HSM Root Key Cryptographic Injection</li>
                    <li>Identity &amp; Access Management (IAM)</li>
                    <li>Real-Time Transit &amp; Transaction Analytics</li>
                </ul>
                <a href="solutions-infrastructure.html" class="pillar-link">Explore Digital Infra →</a>
            </div>

            <!-- Pillar 6 -->
            <div class="pillar-card">
                <div class="pillar-num">PILLAR // 06</div>
                <h3 class="pillar-title">Capital &amp; Strategic Projects</h3>
                <p class="pillar-desc">
                    Structured project financing, Public-Private Partnerships (PPP), sovereign concession frameworks, and turnkey emerging-market execution.
                </p>
                <ul class="pillar-features">
                    <li>Infrastructure Project Development</li>
                    <li>Public-Private Partnership (PPP) Concessions</li>
                    <li>Strategic FinTech Investment Governance</li>
                    <li>Cross-Border Market-Entry Frameworks</li>
                </ul>
                <a href="solutions-capital.html" class="pillar-link">Explore Capital Projects →</a>
            </div>
        </div>
    </div>
</section>

<!-- Flagship Feature: South Africa National Mobility & Payments Program -->
<section class="section-spacing">
    <div class="container">
        <div class="africa-flagship-section">
            <div class="africa-flagship-grid">
                <div>
                    <div class="san-badge">🇿🇦 10-YEAR NATIONAL CONCESSION • SIGNED &amp; ACTIVE</div>
                    <h2 class="serif-title" style="color: #FAF2EB; font-size: clamp(1.8rem, 3.5vw, 2.7rem); margin-bottom: 1rem;">
                        South Africa National Mobility &amp; Payments Program
                    </h2>
                    <p style="color: #E8DDD4; font-size: 1.05rem; line-height: 1.7; margin-bottom: 1.5rem;">
                        Executed by <strong>GENTECH CAPITAL HOLDING (PTY) LTD</strong> in partnership with the South African National Taxi Council (SANTACO) through TaxiChoice. A generational digital transformation deploying smart contactless transit payments and banking inclusion across the national minibus taxi network.
                    </p>
                    
                    <div class="africa-stats-row">
                        <div class="san-stat-card">
                            <div class="san-stat-val">500,000</div>
                            <div class="san-stat-lbl">Transit Vehicles Scope</div>
                        </div>
                        <div class="san-stat-card">
                            <div class="san-stat-val">65M</div>
                            <div class="san-stat-lbl">Commuters Target</div>
                        </div>
                        <div class="san-stat-card">
                            <div class="san-stat-val">1,000</div>
                            <div class="san-stat-lbl">Mpumalanga Pilot Fleet</div>
                        </div>
                    </div>

                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <a href="africa-national-mobility-program.html" class="btn-primary" style="background: var(--accent-hermes); color: #fff;">
                            <span>View Full Program Architecture</span>
                        </a>
                        <a href="group-africa.html" class="btn-secondary" style="background: rgba(255,255,255,0.1); color: #fff; border-color: rgba(255,255,255,0.2);">
                            <span>Gentech Africa Hub (Johannesburg)</span>
                        </a>
                    </div>
                </div>

                <div class="san-architecture-card">
                    <h4 style="color: #FAF2EB; font-size: 1.1rem; margin-bottom: 0.5rem;">Turnkey Ecosystem Architecture</h4>
                    <p style="font-size: 0.82rem; color: #D1C4BA;">
                        An end-to-end multi-tier transaction pipeline engineered for extreme reliability in rugged transit environments.
                    </p>
                    <ul class="arch-flow-list">
                        <li class="arch-flow-item">
                            <span class="arch-flow-num">01.</span>
                            <span><strong>Commuter Tap:</strong> Smart NFC Card, Mobile QR or EMV Open-Loop.</span>
                        </li>
                        <li class="arch-flow-item">
                            <span class="arch-flow-num">02.</span>
                            <span><strong>In-Vehicle Validator:</strong> Ruggedized Android Dual-Bus POS with sub-50ms cryptographic clearing.</span>
                        </li>
                        <li class="arch-flow-item">
                            <span class="arch-flow-num">03.</span>
                            <span><strong>Driver Terminal:</strong> Real-time fare confirmation, route tracking, and shift balancing.</span>
                        </li>
                        <li class="arch-flow-item">
                            <span class="arch-flow-num">04.</span>
                            <span><strong>4G/5G Gateway:</strong> Encrypted telemetry to sovereign cloud clearing house.</span>
                        </li>
                        <li class="arch-flow-item">
                            <span class="arch-flow-num">05.</span>
                            <span><strong>Daily Settlement:</strong> Automated reconciliation and direct payout to taxi owners and associations.</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Global Presence (The 3 Registered Holding Pillars) -->
<section class="section-spacing" style="background: var(--bg-card-subtle); border-top: 1px solid var(--border-light); border-bottom: 1px solid var(--border-light);">
    <div class="container">
        <div class="section-header-center">
            <div class="calm-tag">GLOBAL PRESENCE</div>
            <h2 class="serif-title">Tri-Continental Operational Pillars</h2>
            <p class="section-subtitle">
                A seamless corporate holding structure connecting North American capital, Middle Eastern technology, and African field operations.
            </p>
        </div>

        <div class="hubs-grid-3">
            <!-- Hub Canada -->
            <div class="hub-card">
                <div class="hub-flag-badge">🍁</div>
                <h3 class="hub-name">Canada</h3>
                <div class="hub-entity-title">GENTECH CAPITAL HOLDINGS INC.</div>
                <p class="hub-role-desc">
                    The parent holding company responsible for capital allocation, international treasury governance, equity participation, and strategic global expansion.
                </p>
                <div class="hub-meta-list">
                    <div class="hub-meta-item"><strong>Location:</strong> Toronto, Ontario, Canada</div>
                    <div class="hub-meta-item"><strong>Mandate:</strong> Capital, Investment &amp; Governance</div>
                    <div class="hub-meta-item"><strong>Inquiries:</strong> investments@gentech.ae</div>
                </div>
                <a href="group-canada.html" class="pillar-link">Explore Canada Holding →</a>
            </div>

            <!-- Hub UAE -->
            <div class="hub-card">
                <div class="hub-flag-badge">🇦🇪</div>
                <h3 class="hub-name">United Arab Emirates</h3>
                <div class="hub-entity-title">GENTECH GLOBAL FZ-LLC</div>
                <p class="hub-role-desc">
                    The technology and international trade hub directing high-security smart card production, POS terminal hardware, chip module design, and telecom procurement.
                </p>
                <div class="hub-meta-list">
                    <div class="hub-meta-item"><strong>Location:</strong> Ras Al Khaimah (RAKEZ), UAE</div>
                    <div class="hub-meta-item"><strong>Mandate:</strong> Technology, Engineering &amp; Trade</div>
                    <div class="hub-meta-item"><strong>Inquiries:</strong> cards@gentech.ae</div>
                </div>
                <a href="group-uae.html" class="pillar-link">Explore UAE Technology Hub →</a>
            </div>

            <!-- Hub South Africa -->
            <div class="hub-card">
                <div class="hub-flag-badge">🇿🇦</div>
                <h3 class="hub-name">South Africa</h3>
                <div class="hub-entity-title">GENTECH CAPITAL HOLDING (PTY) LTD</div>
                <p class="hub-role-desc">
                    The Africa operating company spearheading regional large-scale infrastructure deployments, including the 10-year National Mobility and Payments Program.
                </p>
                <div class="hub-meta-list">
                    <div class="hub-meta-item"><strong>Location:</strong> Johannesburg, South Africa</div>
                    <div class="hub-meta-item"><strong>Mandate:</strong> Africa Operations &amp; Program Execution</div>
                    <div class="hub-meta-item"><strong>Inquiries:</strong> africa@gentech.ae</div>
                </div>
                <a href="group-africa.html" class="pillar-link">Explore Africa Operations →</a>
            </div>
        </div>
    </div>
</section>

<!-- Chairman's Message Spotlight Section -->
<section class="section-spacing">
    <div class="container">
        <div class="chairman-spotlight">
            <div class="chairman-grid">
                <div class="chairman-portrait-box">
                    <div class="portrait-avatar-placeholder">MS</div>
                    <h3 class="chairman-name">Mustafa Sertkaya</h3>
                    <div class="chairman-title-label">Chairman, Gentech Group</div>
                    <p style="font-size: 0.84rem; color: var(--text-dim); margin-top: 0.75rem;">
                        Executive Governance • Strategic FinTech Leadership • Sovereign Infrastructure
                    </p>
                    <div style="margin-top: 1.5rem;">
                        <a href="chairman.html" class="btn-secondary" style="font-size: 0.85rem; padding: 0.6rem 1.2rem;">
                            <span>Read Full Statement</span>
                        </a>
                    </div>
                </div>

                <div>
                    <div class="calm-tag">CHAIRMAN'S VISION</div>
                    <div class="chairman-quote">
                        "At Gentech Group, we believe the true measure of technology lies in the trust, convenience, and enduring economic opportunity it creates in people’s daily lives."
                    </div>
                    <p class="chairman-body-text">
                        From smart and EMV-compliant payment cards to pure titanium and ceramic bodies, wearable payment devices, bespoke chip modules, POS terminals, and advanced telecommunications solutions, our operations span the full spectrum of sovereign financial technologies.
                    </p>
                    <p class="chairman-body-text">
                        Our national digital mobility and payments program in South Africa stands as a flagship testament to this vision—uniting a 500,000-vehicle transit network to serve 65 million commuters with secure contactless transit and digital financial access.
                    </p>
                    <a href="chairman.html" class="pillar-link" style="font-size: 1rem;">Read Complete Chairman's Address (English &amp; Türkçe) →</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Institutional Partnerships & Sector Solutions -->
<section class="section-spacing" style="background: var(--bg-card-subtle); border-top: 1px solid var(--border-light);">
    <div class="container">
        <div class="section-header-center">
            <div class="calm-tag">INSTITUTIONAL PARTNERS</div>
            <h2 class="serif-title">Serving Critical Global Sectors</h2>
            <p class="section-subtitle">
                Tailored financial infrastructure solutions for tier-1 enterprises, governments, and institutional partners.
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.5rem;">
            <div style="background: #fff; padding: 1.8rem; border-radius: var(--radius-md); border: 1px solid var(--border-light);">
                <h4 style="margin-bottom: 0.5rem; font-size: 1.1rem;">Banks &amp; FinTechs</h4>
                <p style="font-size: 0.86rem; color: var(--text-muted);">Turnkey luxury metal issuance, dual-interface EMV personalization, and instant cardholder issuance hubs.</p>
            </div>
            <div style="background: #fff; padding: 1.8rem; border-radius: var(--radius-md); border: 1px solid var(--border-light);">
                <h4 style="margin-bottom: 0.5rem; font-size: 1.1rem;">Transport Authorities</h4>
                <p style="font-size: 0.86rem; color: var(--text-muted);">Automated fare collection, national transit concession management, and open-loop validator deployments.</p>
            </div>
            <div style="background: #fff; padding: 1.8rem; border-radius: var(--radius-md); border: 1px solid var(--border-light);">
                <h4 style="margin-bottom: 0.5rem; font-size: 1.1rem;">Telecom Operators</h4>
                <p style="font-size: 0.86rem; color: var(--text-muted);">Super SIM 5G multi-IMSI platforms, eSIM remote profile provisioning, and encrypted IoT fleet modules.</p>
            </div>
            <div style="background: #fff; padding: 1.8rem; border-radius: var(--radius-md); border: 1px solid var(--border-light);">
                <h4 style="margin-bottom: 0.5rem; font-size: 1.1rem;">Governments &amp; Public Sector</h4>
                <p style="font-size: 0.86rem; color: var(--text-muted);">National identity cards, biometric social grant disbursement systems, and sovereign data infrastructure.</p>
            </div>
        </div>
    </div>
</section>

<!-- Call to Action Banner -->
<section class="section-spacing">
    <div class="container">
        <div style="background: linear-gradient(135deg, #1A130E 0%, #3D2211 100%); color: #FAF2EB; border-radius: var(--radius-lg); padding: clamp(2.5rem, 5vw, 4.5rem); text-align: center; border: 1px solid rgba(235, 101, 26, 0.3);">
            <h2 class="serif-title" style="color: #FAF2EB; font-size: clamp(2rem, 4vw, 3rem); margin-bottom: 1rem;">
                Partner with Gentech Group
            </h2>
            <p style="max-width: 650px; margin: 0 auto 2rem auto; color: #E8DDD4; font-size: 1.05rem; line-height: 1.7;">
                Connect with our executive management across Toronto, Ras Al Khaimah, and Johannesburg to discuss strategic investments, card issuance programs, or national mobility partnerships.
            </p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <a href="contact.html" class="btn-primary" style="background: var(--accent-hermes); color: #fff;">
                    <span>Submit Institutional Inquiry</span>
                </a>
                <a href="about.html" class="btn-secondary" style="background: rgba(255,255,255,0.1); color: #fff; border-color: rgba(255,255,255,0.2);">
                    <span>Corporate Profile</span>
                </a>
            </div>
        </div>
    </div>
</section>

<!-- Three.js Library & 3D WebGL Script for interactive visualizer -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="assets/js/scene3d.js?v=20.0"></script>
"""
    three_scripts = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n<script src="assets/js/scene3d.js?v=21.0"></script>'
    write_file("index.html", header + body + get_footer(three_scripts))

build_index()

# ==============================================================================
# 2. ABOUT.HTML — GENTECH GROUP OVERVIEW & GOVERNANCE
# ==============================================================================
def build_about():
    header = get_header(
        title="About Gentech Group — Global Capital, Technology & Operations",
        desc="Learn about Gentech Group's tri-continental holding architecture across Canada, UAE, and South Africa, executive governance, and sovereign infrastructure mission.",
        active_nav="about"
    )
    banner = get_page_banner(
        title="About Gentech Group",
        sub="A Tri-Continental Architecture of Capital, Technology Engineering, and Field Operations.",
        crumb="About Gentech Group",
        badge="✦ GENTECH GROUP • CORPORATE PROFILE"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">SOVEREIGN MISSION &amp; VISION</span>
                <h2 class="serif-title" style="margin-bottom: 1.25rem;">Transforming Critical Infrastructure into Long-Term Economic Value</h2>
                <p>
                    Gentech Group is an international holding and technology group operating at the nexus of high-security payment engineering, sovereign digital infrastructure, telecommunications, and long-term public-private partnerships.
                </p>
                <p>
                    Rooted in a disciplined tri-continental model, Gentech Group bridges North American capital mobilization (Canada), Middle Eastern technical manufacturing and global trade (United Arab Emirates), and African operational field deployment (South Africa). We do not merely manufacture cards or build standalone software; we engineer, deploy, and operate end-to-end mission-critical financial ecosystems.
                </p>

                <h3 style="margin-top: 2.5rem; margin-bottom: 1rem;" id="entities">The Tri-Continental Holding Model</h3>
                <p>
                    To ensure absolute legal clarity, regulatory compliance, and operational excellence, Gentech Group operates through three distinct, legally verified corporate entities:
                </p>

                <div style="display: flex; flex-direction: column; gap: 1.5rem; margin: 2rem 0;">
                    <div style="background: #fff; border: 1px solid var(--border-light); border-left: 4px solid var(--accent-hermes); border-radius: var(--radius-md); padding: 1.8rem; box-shadow: var(--shadow-soft);">
                        <span class="calm-tag" style="margin-bottom: 0.4rem;">CANADA • PARENT HOLDING</span>
                        <h4 style="font-size: 1.2rem; margin-bottom: 0.3rem;">GENTECH CAPITAL HOLDINGS INC.</h4>
                        <p style="font-size: 0.92rem; color: var(--text-muted); margin-bottom: 0.8rem;">
                            Headquartered in Toronto, Ontario, Canada. Serves as the overarching holding company responsible for capital allocation, international treasury governance, equity participation, and strategic global partnerships.
                        </p>
                        <a href="group-canada.html" class="pillar-link">View Canada Holding Profile →</a>
                    </div>

                    <div style="background: #fff; border: 1px solid var(--border-light); border-left: 4px solid var(--accent-hermes); border-radius: var(--radius-md); padding: 1.8rem; box-shadow: var(--shadow-soft);">
                        <span class="calm-tag" style="margin-bottom: 0.4rem;">UAE • TECHNOLOGY &amp; TRADE HUB</span>
                        <h4 style="font-size: 1.2rem; margin-bottom: 0.3rem;">GENTECH GLOBAL FZ-LLC</h4>
                        <p style="font-size: 0.92rem; color: var(--text-muted); margin-bottom: 0.8rem;">
                            Registered in the Ras Al Khaimah Economic Zone (RAKEZ), UAE. Directs smart card production, EMV personalisation, bespoke chip module design, Android POS terminal hardware, and international telecommunications procurement.
                        </p>
                        <a href="group-uae.html" class="pillar-link">View UAE Technology Hub Profile →</a>
                    </div>

                    <div style="background: #fff; border: 1px solid var(--border-light); border-left: 4px solid var(--accent-hermes); border-radius: var(--radius-md); padding: 1.8rem; box-shadow: var(--shadow-soft);">
                        <span class="calm-tag" style="margin-bottom: 0.4rem;">SOUTH AFRICA • AFRICA OPERATIONS HUB</span>
                        <h4 style="font-size: 1.2rem; margin-bottom: 0.3rem;">GENTECH CAPITAL HOLDING (PTY) LTD</h4>
                        <p style="font-size: 0.92rem; color: var(--text-muted); margin-bottom: 0.8rem;">
                            Headquartered in Johannesburg, South Africa. Functions as Gentech Group's dedicated African operating entity, spearheading regional infrastructure programs including the 10-year National Mobility &amp; Payments Program with SANTACO/TaxiChoice.
                        </p>
                        <a href="group-africa.html" class="pillar-link">View South Africa Operations Profile →</a>
                    </div>
                </div>

                <h3 style="margin-top: 2.5rem; margin-bottom: 1rem;" id="governance">Corporate Governance &amp; Ethical Standards</h3>
                <p>
                    Gentech Group adheres to world-class regulatory standards. We maintain strict compliance with Anti-Money Laundering (AML), Know Your Customer (KYC), General Data Protection Regulation (GDPR), South Africa's Protection of Personal Information Act (POPIA), and UAE Federal Data Protection frameworks.
                </p>
            </div>

            <!-- Sidebar -->
            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">QUICK FACTS</span>
                    <h4 style="margin-bottom: 1rem;">Gentech at a Glance</h4>
                    
                    <div style="display: flex; flex-direction: column; gap: 0.8rem; font-size: 0.88rem; color: var(--text-muted);">
                        <div><strong>Parent Brand:</strong> GENTECH GROUP</div>
                        <div><strong>Global Presence:</strong> Canada • UAE • South Africa</div>
                        <div><strong>Executive Chairman:</strong> Mustafa Sertkaya</div>
                        <div><strong>Primary Sectors:</strong> Payments, Smart Cards, Transit Mobility, 5G Telecom, Sovereign Infrastructure</div>
                        <div><strong>Flagship Program:</strong> SANTACO 10-Year National Mobility Program</div>
                    </div>

                    <hr style="border: 0; border-top: 1px solid var(--border-light); margin: 1.5rem 0;">

                    <a href="chairman.html" class="btn-primary" style="width: 100%; text-align: center; display: block;">
                        <span>Chairman's Statement</span>
                    </a>
                    <a href="contact.html" class="btn-secondary" style="width: 100%; text-align: center; display: block; margin-top: 0.5rem;">
                        <span>Contact Corporate Office</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("about.html", header + body + get_footer())

# ==============================================================================
# 3. CHAIRMAN.HTML — MUSTAFA SERTKAYA (CHAIRMAN'S MESSAGE VERBATIM)
# ==============================================================================
def build_chairman():
    header = get_header(
        title="Chairman's Statement — Mustafa Sertkaya | GENTECH GROUP",
        desc="Official statement and strategic address by Mustafa Sertkaya, Chairman of Gentech Group, on global payment technologies, card manufacturing, and sovereign mobility infrastructure.",
        active_nav="chairman"
    )
    banner = get_page_banner(
        title="Chairman's Statement",
        sub="A message from Mustafa Sertkaya, Chairman of Gentech Group, on our vision, technologies, and long-term economic value creation.",
        crumb="Chairman's Statement",
        badge="✦ GENTECH GROUP • EXECUTIVE LEADERSHIP"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="legal-container" style="max-width: 960px;">
            <div style="display: flex; align-items: center; gap: 2rem; margin-bottom: 2.5rem; flex-wrap: wrap;">
                <div class="portrait-avatar-placeholder" style="width: 110px; height: 110px; font-size: 2rem; margin: 0;">MS</div>
                <div>
                    <h2 class="serif-title" style="margin-bottom: 0.3rem;">Mustafa Sertkaya</h2>
                    <div style="font-size: 1rem; font-weight: 700; color: var(--accent-hermes); text-transform: uppercase; letter-spacing: 0.05em;">
                        Chairman, Gentech Group
                    </div>
                    <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 0.3rem;">
                        Canada • United Arab Emirates • South Africa
                    </div>
                </div>
            </div>

            <!-- English Official Address -->
            <div class="legal-section-block">
                <span class="calm-tag">OFFICIAL ADDRESS // ENGLISH</span>
                <h3 class="serif-title" style="margin-top: 1rem; margin-bottom: 1.5rem; font-size: 1.5rem;">
                    "Engineering Trust, Technological Precision, and Generational Value"
                </h3>
                
                <p style="font-size: 1.05rem; line-height: 1.8; color: var(--text-main); font-weight: 500; margin-bottom: 1.25rem;">
                    At Gentech Group, we believe the true measure of technology lies in the trust, convenience, and enduring economic opportunity it creates in people’s daily lives.
                </p>
                <p>
                    From smart and EMV-compliant payment cards to titanium and ceramic cards, wearable payment devices, bespoke chip modules, POS terminals, and advanced telecommunications solutions, to end-to-end digital payment architectures and smart mobility ecosystems, our operations span the full spectrum of sovereign financial technologies.
                </p>
                <p>
                    In card technologies, we engineer, produce, personalise, and integrate chip-level security tailored to the rigorous demands of tier-1 banks, financial institutions, telecom operators, government entities, and global enterprises. Our objective transcends hardware supply; we forge secure, scalable ecosystems uniting hardware, micro-firmware, and enterprise operations.
                </p>
                <p>
                    In smart mobility, we seamlessly bridge automated fare collection, account-based ticketing, in-vehicle validators, driver consoles, central dispatch, telemetry data, and institutional financial access into a singular unified ecosystem.
                </p>
                <p>
                    Our national digital mobility and payments program in South Africa stands as a flagship testament to this vision—uniting a 500,000-vehicle transit network to serve 65 million commuters with secure contactless transit and digital financial access.
                </p>
                <p>
                    Our vision is to serve as a globally trusted partner in payments, card manufacturing, digital mobility, and connected infrastructure—driving technology transfer, local industrial capacity, high-value employment, and generational economic value across every market we operate.
                </p>
                <p>
                    Gentech advances with an unwavering commitment: solving today's mission-critical needs while engineering the digital payment infrastructure of tomorrow.
                </p>
                
                <div style="margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--border-light);">
                    <div style="font-weight: 700; font-size: 1.1rem; color: var(--text-main);">Mustafa Sertkaya</div>
                    <div style="font-size: 0.85rem; color: var(--accent-hermes); font-weight: 600;">Chairman, Gentech Group</div>
                </div>
            </div>

            <!-- Turkish Translation Edition -->
            <div class="legal-section-block" style="background: var(--bg-card-subtle); padding: 2rem; border-radius: var(--radius-md); border: 1px solid var(--border-light);">
                <span class="calm-tag">RESMÎ METİN // TÜRKÇE</span>
                <h3 class="serif-title" style="margin-top: 1rem; margin-bottom: 1.25rem; font-size: 1.35rem;">
                    Başkanın Mesajı
                </h3>
                
                <p style="font-size: 0.98rem; line-height: 1.8; color: var(--text-main); font-weight: 500;">
                    Gentech olarak teknolojinin gerçek değerinin, insanların günlük hayatında oluşturduğu güven, kolaylık ve yeni fırsatlarla ölçüldüğüne inanıyoruz.
                </p>
                <p style="font-size: 0.94rem; line-height: 1.7; color: var(--text-muted);">
                    Akıllı ve EMV uyumlu ödeme kartlarından metal ve seramik kartlara, giyilebilir ödeme ürünlerinden özel çip modüllerine; POS cihazlarından telekomünikasyon çözümlerine, dijital ödeme altyapılarından akıllı ulaşım sistemlerine kadar geniş bir alanda faaliyet gösteriyoruz.
                </p>
                <p style="font-size: 0.94rem; line-height: 1.7; color: var(--text-muted);">
                    Kart teknolojilerinde tasarım, üretim, kişiselleştirme, çip entegrasyonu ve tedarik süreçlerini; bankaların, finansal kuruluşların, telekomünikasyon şirketlerinin, kamu kurumlarının ve küresel markaların ihtiyaçlarına uygun şekilde yönetiyoruz. Amacımız yalnızca ürün sağlamak değil; donanım, yazılım ve operasyonu bir araya getiren güvenli ve ölçeklenebilir çözümler geliştirmektir.
                </p>
                <p style="font-size: 0.94rem; line-height: 1.7; color: var(--text-muted);">
                    Dijital ulaşım alanında ise ücret toplama, kart ve cüzdan sistemleri, validasyon cihazları, sürücü terminalleri, merkezi operasyon, veri yönetimi ve finansal erişim bileşenlerini aynı ekosistem içerisinde buluşturuyoruz.
                </p>
                <p style="font-size: 0.94rem; line-height: 1.7; color: var(--text-muted);">
                    Güney Afrika’da yürüttüğümüz ulusal dijital ulaşım ve ödeme programı, bu vizyonun önemli uygulamalarından biridir. Hedefimiz; 500.000 aracı kapsayan, 65 milyon kişiye ulaşan ve ulaşım ile ödeme altyapısını bütünleştiren sürdürülebilir bir dijital ekosistem oluşturmaktır.
                </p>
                <p style="font-size: 0.94rem; line-height: 1.7; color: var(--text-muted);">
                    Vizyonumuz; ödeme teknolojileri, kart üretimi, dijital mobilite ve bağlantılı altyapılar alanında uluslararası ölçekte güvenilir bir çözüm ortağı olmak; faaliyet gösterdiğimiz pazarlarda teknoloji transferi, yerel kapasite, istihdam ve uzun vadeli ekonomik değer yaratmaktır.
                </p>
                <p style="font-size: 0.94rem; line-height: 1.7; color: var(--text-muted);">
                    Gentech, bugünün ihtiyaçlarını karşılayan ürünler geliştirirken geleceğin ödeme ve dijital altyapı sistemlerini kurma kararlılığıyla ilerlemektedir.
                </p>
                
                <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid var(--border-light);">
                    <div style="font-weight: 700; font-size: 1rem; color: var(--text-main);">Mustafa Sertkaya</div>
                    <div style="font-size: 0.82rem; color: var(--accent-hermes); font-weight: 600;">Chairman, Gentech Group</div>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("chairman.html", header + body + get_footer())

build_about()
build_chairman()

# ==============================================================================
# 4. GROUP-CANADA.HTML — GENTECH CAPITAL HOLDINGS INC.
# ==============================================================================
def build_group_canada():
    header = get_header(
        title="Gentech Canada — GENTECH CAPITAL HOLDINGS INC.",
        desc="Gentech Capital Holdings Inc. is the group parent holding company headquartered in Toronto, Ontario, Canada, governing capital allocation, investments, and global expansion.",
        active_nav="group"
    )
    banner = get_page_banner(
        title="Gentech Canada",
        sub="GENTECH CAPITAL HOLDINGS INC. • Group Parent Holding & Strategic Capital",
        crumb="Gentech Canada",
        badge="✦ GROUP COMPANY PROFILE • ONTARIO, CANADA"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">HOLDING GOVERNANCE</span>
                <h2 class="serif-title" style="margin-bottom: 1.25rem;">Capital Allocation, Strategic Investment &amp; Sovereign Expansion</h2>
                <p>
                    <strong>GENTECH CAPITAL HOLDINGS INC.</strong> is the supreme holding entity of Gentech Group, registered in Ontario, Canada. Headquartered in Toronto, the Canadian corporation steers group-wide investment strategy, capital mobilization, subsidiary governance, and international concession frameworks.
                </p>
                
                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">Core Mandates &amp; Scope</h3>
                <ul style="padding-left: 1.5rem; line-height: 1.8; color: var(--text-muted); margin-bottom: 1.5rem;">
                    <li><strong>Global Capital Mobilization:</strong> Structuring debt and equity facilities for multi-million-dollar national infrastructure concessions.</li>
                    <li><strong>Subsidiary Governance:</strong> Directing the operations and risk compliance of Gentech Global FZ-LLC (UAE) and Gentech Capital Holding (Pty) Ltd (South Africa).</li>
                    <li><strong>Public-Private Partnerships (PPP):</strong> Negotiating sovereign concession agreements with transport authorities, central banks, and government ministries.</li>
                    <li><strong>Intellectual Property &amp; Patent Holding:</strong> Custody of Gentech's proprietary smart transit architectures, chip firmware designs, and encryption methods.</li>
                </ul>

                <div class="sidebar-box" style="margin-top: 2rem; background: var(--bg-card-subtle);">
                    <h4 style="margin-bottom: 0.8rem;">Corporate Entity Verification</h4>
                    <table class="legal-table">
                        <tr><th>Full Legal Name</th><td>GENTECH CAPITAL HOLDINGS INC.</td></tr>
                        <tr><th>Jurisdiction</th><td>Ontario, Canada</td></tr>
                        <tr><th>Corporate Role</th><td>Parent Holding Company</td></tr>
                        <tr><th>Headquarters</th><td>Toronto, Ontario, Canada</td></tr>
                        <tr><th>Primary Focus</th><td>Strategic Investments, PPP Projects, Treasury &amp; Governance</td></tr>
                        <tr><th>Inquiries</th><td>investments@gentech.ae</td></tr>
                    </table>
                </div>
            </div>

            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">TORONTO HUB</span>
                    <h4 style="margin-bottom: 0.8rem;">Investor Relations</h4>
                    <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1rem;">
                        For institutional capital inquiries, shareholder relations, and cross-border joint venture discussions:
                    </p>
                    <div style="font-size: 0.85rem; color: var(--text-dim); margin-bottom: 1.2rem;">
                        <strong>Gentech Capital Holdings Inc.</strong><br>
                        Toronto, Ontario, Canada<br>
                        Email: <a href="mailto:investments@gentech.ae" style="color:var(--accent-hermes); font-weight:600;">investments@gentech.ae</a>
                    </div>
                    <a href="contact.html?dept=investments" class="btn-primary" style="width: 100%; text-align: center; display: block;">
                        <span>Inquire with Holding</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("group-canada.html", header + body + get_footer())

# ==============================================================================
# 5. GROUP-UAE.HTML — GENTECH GLOBAL FZ-LLC
# ==============================================================================
def build_group_uae():
    header = get_header(
        title="Gentech UAE — GENTECH GLOBAL FZ-LLC",
        desc="Gentech Global FZ-LLC is the technology, smart card manufacturing, and international trade powerhouse of Gentech Group, registered in RAKEZ, UAE.",
        active_nav="group"
    )
    banner = get_page_banner(
        title="Gentech United Arab Emirates",
        sub="GENTECH GLOBAL FZ-LLC • Payment Technologies, Smart Card Engineering & Global Trade",
        crumb="Gentech UAE",
        badge="✦ GROUP COMPANY PROFILE • RAS AL KHAIMAH, UAE"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">TECHNOLOGY &amp; TRADE HUB</span>
                <h2 class="serif-title" style="margin-bottom: 1.25rem;">Payment Engineering, Smart Silicon &amp; Global Procurement</h2>
                <p>
                    <strong>GENTECH GLOBAL FZ-LLC</strong> is the primary operating company for technology engineering, card manufacturing oversight, and international equipment trade within Gentech Group. Registered in the Ras Al Khaimah Economic Zone (RAKEZ), United Arab Emirates, the entity serves commercial banks, telecom operators, and international enterprises across EMEA.
                </p>
                
                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">Core Capabilities &amp; Operations</h3>
                <ul style="padding-left: 1.5rem; line-height: 1.8; color: var(--text-muted); margin-bottom: 1.5rem;">
                    <li><strong>Smart &amp; EMV Card Solutions:</strong> Dual-interface contact/contactless cards, luxury metal cards (pure titanium, brass, 24K gold plated), and high-durability ceramic bodies.</li>
                    <li><strong>Bespoke Chip Modules:</strong> Laser-etched custom chip contact layouts engineered with CC EAL6+ certified secure elements.</li>
                    <li><strong>Payment Terminal Hardware:</strong> Android POS, unattended transit validators, and mobile payment acceptance devices.</li>
                    <li><strong>5G Telecommunications Hardware:</strong> Super SIM 5G multi-IMSI cards, IoT cellular modules, and M2M secure cryptographic keys.</li>
                    <li><strong>Global Supply Chain &amp; Logistics:</strong> Worldwide fulfillment and secure chain-of-custody delivery.</li>
                </ul>

                <div class="sidebar-box" style="margin-top: 2rem; background: var(--bg-card-subtle);">
                    <h4 style="margin-bottom: 0.8rem;">Corporate Entity Verification</h4>
                    <table class="legal-table">
                        <tr><th>Full Legal Name</th><td>GENTECH GLOBAL FZ-LLC</td></tr>
                        <tr><th>Jurisdiction</th><td>Ras Al Khaimah Economic Zone (RAKEZ), UAE</td></tr>
                        <tr><th>Registered Address</th><td>Compass Building, Al Shohada Road, AL Hamra Industrial Zone-FZ, Ras Al Khaimah, United Arab Emirates</td></tr>
                        <tr><th>Corporate Role</th><td>Technology, Card Engineering &amp; Global Trade</td></tr>
                        <tr><th>Primary Focus</th><td>EMV Cards, POS Hardware, SIM/eSIM, Chip Modules &amp; Trade</td></tr>
                        <tr><th>Inquiries</th><td>cards@gentech.ae / info@gentech.ae</td></tr>
                    </table>
                </div>
            </div>

            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">UAE HUB</span>
                    <h4 style="margin-bottom: 0.8rem;">Commercial &amp; Tech Orders</h4>
                    <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1rem;">
                        For card manufacturing batches, POS terminal hardware tenders, and bespoke chip personalization:
                    </p>
                    <div style="font-size: 0.85rem; color: var(--text-dim); margin-bottom: 1.2rem;">
                        <strong>Gentech Global FZ-LLC</strong><br>
                        Compass Building, Al Shohada Rd,<br>
                        AL Hamra Industrial Zone-FZ,<br>
                        Ras Al Khaimah, United Arab Emirates<br>
                        Email: <a href="mailto:cards@gentech.ae" style="color:var(--accent-hermes); font-weight:600;">cards@gentech.ae</a>
                    </div>
                    <a href="contact.html?dept=cards" class="btn-primary" style="width: 100%; text-align: center; display: block;">
                        <span>Inquire Products &amp; Batches</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("group-uae.html", header + body + get_footer())

# ==============================================================================
# 6. GROUP-AFRICA.HTML — GENTECH CAPITAL HOLDING (PTY) LTD
# ==============================================================================
def build_group_africa():
    header = get_header(
        title="Gentech Africa — GENTECH CAPITAL HOLDING (PTY) LTD",
        desc="Gentech Capital Holding (Pty) Ltd is Gentech Group's dedicated African operating entity in Johannesburg, South Africa, executing national-scale mobility and digital payment infrastructure.",
        active_nav="group"
    )
    banner = get_page_banner(
        title="Gentech South Africa",
        sub="GENTECH CAPITAL HOLDING (PTY) LTD • Africa Operations Hub & National Program Execution",
        crumb="Gentech Africa",
        badge="✦ GROUP COMPANY PROFILE • JOHANNESBURG, SOUTH AFRICA"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">AFRICA OPERATIONS HUB</span>
                <h2 class="serif-title" style="margin-bottom: 1.25rem;">National Infrastructure Deployment &amp; Sovereign Operations</h2>
                <p>
                    <strong>GENTECH CAPITAL HOLDING (PTY) LTD</strong> is Gentech Group's registered South African operating company, based in Johannesburg. The entity spearheads all field deployments, operator onboarding, financial inclusion initiatives, and local stakeholder engagements across the African continent.
                </p>
                
                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">Flagship Program: South Africa National Mobility &amp; Payments</h3>
                <p>
                    Gentech Africa is the exclusive contractual executor of the 10-year national agreement signed on June 8, 2026, with the South African National Taxi Council (SANTACO) through TaxiChoice. Under this agreement, Gentech is deploying automated fare collection, in-vehicle POS validators, and digital transit cards across 500,000 minibus taxis serving 65 million commuters nationwide.
                </p>

                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">African Expansion Strategy</h3>
                <ul style="padding-left: 1.5rem; line-height: 1.8; color: var(--text-muted); margin-bottom: 1.5rem;">
                    <li><strong>Mass Transit Digitization:</strong> Scaling closed-loop and EMV open-loop fare systems from South Africa to regional SADC transport corridors.</li>
                    <li><strong>Financial Inclusion &amp; Unbanked Populations:</strong> Equipping millions of informal commuters with interoperable contactless payment credentials.</li>
                    <li><strong>Local Job Creation &amp; Skills Transfer:</strong> Establishing regional technical support depots, field training hubs, and certified hardware maintenance facilities.</li>
                    <li><strong>Regulatory Compliance:</strong> Full compliance with POPIA (Protection of Personal Information Act) and South African Reserve Bank (SARB) payment clearing frameworks.</li>
                </ul>

                <div class="sidebar-box" style="margin-top: 2rem; background: var(--bg-card-subtle);">
                    <h4 style="margin-bottom: 0.8rem;">Corporate Entity Verification</h4>
                    <table class="legal-table">
                        <tr><th>Full Legal Name</th><td>GENTECH CAPITAL HOLDING (PTY) LTD</td></tr>
                        <tr><th>Jurisdiction</th><td>Johannesburg, South Africa</td></tr>
                        <tr><th>Corporate Role</th><td>Africa Operating Hub</td></tr>
                        <tr><th>Headquarters</th><td>Johannesburg, South Africa</td></tr>
                        <tr><th>Primary Focus</th><td>SANTACO National Mobility Program, Transit Payments &amp; SADC Scale</td></tr>
                        <tr><th>Inquiries</th><td>africa@gentech.ae</td></tr>
                    </table>
                </div>
            </div>

            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">JOHANNESBURG HUB</span>
                    <h4 style="margin-bottom: 0.8rem;">Africa Operations</h4>
                    <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1rem;">
                        For African transport partnerships, transit pilot coordination, and provincial association inquiries:
                    </p>
                    <div style="font-size: 0.85rem; color: var(--text-dim); margin-bottom: 1.2rem;">
                        <strong>Gentech Capital Holding (Pty) Ltd</strong><br>
                        Johannesburg, South Africa<br>
                        Email: <a href="mailto:africa@gentech.ae" style="color:var(--accent-hermes); font-weight:600;">africa@gentech.ae</a>
                    </div>
                    <a href="africa-national-mobility-program.html" class="btn-primary" style="width: 100%; text-align: center; display: block; margin-bottom: 0.5rem;">
                        <span>View National Program</span>
                    </a>
                    <a href="contact.html?dept=africa" class="btn-secondary" style="width: 100%; text-align: center; display: block;">
                        <span>Contact Africa Hub</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("group-africa.html", header + body + get_footer())

# ==============================================================================
# 7. SOLUTIONS-CARDS.HTML — PILLAR 1: CARDS & CARD MANUFACTURING
# ==============================================================================
def build_solutions_cards():
    header = get_header(
        title="Cards & Card Manufacturing — GENTECH GROUP",
        desc="Turnkey design, high-security personalization, and laser engraving for smart EMV, pure titanium, ceramic, and wearable payment products.",
        active_nav="solutions"
    )
    banner = get_page_banner(
        title="Cards &amp; Card Manufacturing",
        sub="Smart &amp; EMV Cards, Pure Titanium &amp; Ceramic Bodies, Wearables &amp; Bespoke Chip Modules.",
        crumb="Solutions / Cards",
        badge="✦ PILLAR 01 // PAYMENT HARDWARE &amp; SECURE ELEMENTS"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">HARDWARE PRECISION</span>
                <h2 class="serif-title" style="margin-bottom: 1.25rem;">Sovereign Security, Exotic Materials &amp; CC EAL6+ Silicon</h2>
                <p>
                    Gentech Group engineers, customizes, and delivers high-security card solutions for tier-1 retail banks, neo-fintechs, government identity programs, telecom giants, and ultra-high-net-worth brand portfolios.
                </p>
                
                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">Product Families</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
                    <div style="background: #fff; border: 1px solid var(--border-light); padding: 1.5rem; border-radius: var(--radius-md);">
                        <h4 style="margin-bottom: 0.5rem;">Pure Titanium &amp; Metal Cards</h4>
                        <p style="font-size: 0.86rem; color: var(--text-muted);">CNC-milled aeronautical grade titanium, brushed stainless steel, and 24K gold electroplated finishes for premier banking portfolios.</p>
                    </div>
                    <div style="background: #fff; border: 1px solid var(--border-light); padding: 1.5rem; border-radius: var(--radius-md);">
                        <h4 style="margin-bottom: 0.5rem;">Zirconia Ceramic Cards</h4>
                        <p style="font-size: 0.86rem; color: var(--text-muted);">Scratch-proof high-density zirconia ceramic with deep optical luster and unmatched tactile luxury.</p>
                    </div>
                    <div style="background: #fff; border: 1px solid var(--border-light); padding: 1.5rem; border-radius: var(--radius-md);">
                        <h4 style="margin-bottom: 0.5rem;">Smart &amp; Dual-Interface EMV</h4>
                        <p style="font-size: 0.86rem; color: var(--text-muted);">High-volume PVC, recycled ocean plastic, and bio-composite EMV cards equipped with global payment scheme compliance.</p>
                    </div>
                    <div style="background: #fff; border: 1px solid var(--border-light); padding: 1.5rem; border-radius: var(--radius-md);">
                        <h4 style="margin-bottom: 0.5rem;">Wearable Payment Devices</h4>
                        <p style="font-size: 0.86rem; color: var(--text-muted);">Apex Titanium &amp; Ceramic NFC smart rings, biometric fobs, and passive smart jewelry for frictionless tap-and-pay.</p>
                    </div>
                </div>

                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">Bespoke Chip Module Customization</h3>
                <p>
                    We offer laser-micro-etched chip contact surfaces, transforming standard smart silicon into bespoke brand assets. All modules support dual-interface (contact &amp; contactless) cryptographic communication with Common Criteria EAL6+ certified microcontrollers.
                </p>

                <!-- Technical Specification Table -->
                <div class="sidebar-box" style="margin-top: 2rem; background: var(--bg-card-subtle);">
                    <h4 style="margin-bottom: 0.8rem;">Technical Specifications</h4>
                    <table class="legal-table">
                        <tr><th>Form Factors</th><td>ISO/IEC 7810 ID-1, Custom Die-Cut, Wearable Rings</td></tr>
                        <tr><th>Silicon Security</th><td>Common Criteria EAL6+ Certified Secure Elements</td></tr>
                        <tr><th>Interfaces</th><td>ISO/IEC 14443 Type A/B, ISO/IEC 7816 Contact, NFC Forum Tag 4</td></tr>
                        <tr><th>Materials</th><td>Grade-5 Titanium, Stainless Steel, Zirconia Ceramic, Recycled PVC</td></tr>
                        <tr><th>Personalisation</th><td>Fiber Laser Engraving, Thermal Re-transfer, Drop-on-Demand (DoD) Inkjet</td></tr>
                        <tr><th>Operating Entity</th><td>GENTECH GLOBAL FZ-LLC (Ras Al Khaimah, UAE)</td></tr>
                    </table>
                </div>
            </div>

            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">ISSUANCE INQUIRIES</span>
                    <h4 style="margin-bottom: 0.8rem;">Custom Card Orders</h4>
                    <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1rem;">
                        Request design templates, material sample kits, or volume production quotes:
                    </p>
                    <a href="contact.html?dept=cards" class="btn-primary" style="width: 100%; text-align: center; display: block; margin-bottom: 0.5rem;">
                        <span>Inquire Production Batch</span>
                    </a>
                    <a href="index.html" class="btn-secondary" style="width: 100%; text-align: center; display: block;">
                        <span>Try 3D Card Studio</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("solutions-cards.html", header + body + get_footer())

# ==============================================================================
# 8. SOLUTIONS-PAYMENTS.HTML — PILLAR 2: PAYMENT TECHNOLOGIES
# ==============================================================================
def build_solutions_payments():
    header = get_header(
        title="Payment Technologies — GENTECH GROUP",
        desc="Omnichannel payment acceptance hardware, ruggedized Android POS terminals, digital wallets, tokenisation, and high-velocity payment gateways.",
        active_nav="solutions"
    )
    banner = get_page_banner(
        title="Payment Technologies",
        sub="Android POS Terminals, Multi-Rail Acceptance, Tokenisation &amp; Real-Time Clearing.",
        crumb="Solutions / Payment Technologies",
        badge="✦ PILLAR 02 // TRANSACTION ACCEPTANCE &amp; CLEARING"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">TRANSACTION VELOCITY</span>
                <h2 class="serif-title" style="margin-bottom: 1.25rem;">Omnichannel Acceptance, Android POS &amp; Clearing Infrastructure</h2>
                <p>
                    Gentech Group develops, supplies, and integrates state-of-the-art payment acceptance infrastructure engineered for high-concurrency commercial retail, rugged mobile transit environments, and digital banking platforms.
                </p>
                
                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">Core Technology Capabilities</h3>
                <ul style="padding-left: 1.5rem; line-height: 1.8; color: var(--text-muted); margin-bottom: 1.5rem;">
                    <li><strong>Smart Android POS Terminals:</strong> High-performance quad-core mobile POS devices featuring integrated thermal printers, 4G/5G, Wi-Fi, barcode scanners, and PCI PTS security.</li>
                    <li><strong>Dual-Interface Transit Acceptors:</strong> Ultra-fast contactless card readers optimized for sub-50ms transaction clearing at vehicle boarding turnstiles.</li>
                    <li><strong>Digital Wallet &amp; Tokenisation Engine:</strong> Host Card Emulation (HCE), cloud tokenisation, and mobile wallet SDKs for white-label banking applications.</li>
                    <li><strong>Payment Gateway &amp; Reconciliation:</strong> Real-time multi-rail routing, ISO 20022 messaging compliance, automated batch settlement, and anti-fraud telemetry.</li>
                </ul>

                <div class="sidebar-box" style="margin-top: 2rem; background: var(--bg-card-subtle);">
                    <h4 style="margin-bottom: 0.8rem;">Technical Architecture</h4>
                    <table class="legal-table">
                        <tr><th>Terminal OS</th><td>Secure Android 12/13 with Remote MDM Control</td></tr>
                        <tr><th>Connectivity</th><td>4G LTE, 5G NR, Dual-Band Wi-Fi 6, Bluetooth 5.2, GPS</td></tr>
                        <tr><th>Transaction Speed</th><td>&lt; 50ms Contactless NFC APDU Cycle</td></tr>
                        <tr><th>Security Standards</th><td>PCI-PTS 6.x, EMV L1 &amp; L2 Contact/Contactless, ISO 27001</td></tr>
                        <tr><th>Settlement Engine</th><td>Real-Time Automated Split Payout &amp; Direct Bank API</td></tr>
                    </table>
                </div>
            </div>

            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">HARDWARE &amp; GATEWAY</span>
                    <h4 style="margin-bottom: 0.8rem;">Terminal Tenders</h4>
                    <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1rem;">
                        Procure Android POS fleets or integrate our secure payment gateway APIs:
                    </p>
                    <a href="contact.html?dept=cards" class="btn-primary" style="width: 100%; text-align: center; display: block;">
                        <span>Inquire POS Hardware</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("solutions-payments.html", header + body + get_footer())

# ==============================================================================
# 9. SOLUTIONS-MOBILITY.HTML — PILLAR 3: SMART MOBILITY SYSTEMS
# ==============================================================================
def build_solutions_mobility():
    header = get_header(
        title="Smart Mobility Systems — GENTECH GROUP",
        desc="Turnkey Automated Fare Collection (AFC), Account-Based Ticketing (ABT), in-vehicle validators, and driver operational telemetry consoles.",
        active_nav="solutions"
    )
    banner = get_page_banner(
        title="Smart Mobility Systems",
        sub="Automated Fare Collection, Account-Based Ticketing, Open-Loop EMV &amp; Fleet Telemetry.",
        crumb="Solutions / Smart Mobility",
        badge="✦ PILLAR 03 // TRANSIT AUTOMATION &amp; SMART FARE"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">MASS TRANSIT AUTOMATION</span>
                <h2 class="serif-title" style="margin-bottom: 1.25rem;">Digitizing National Public Transit Networks</h2>
                <p>
                    Gentech Group architects sovereign smart mobility ecosystems that eliminate cash leakage, reduce passenger boarding queues, and provide transit operators and regulators with real-time operational transparency.
                </p>
                
                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">System Components</h3>
                <ul style="padding-left: 1.5rem; line-height: 1.8; color: var(--text-muted); margin-bottom: 1.5rem;">
                    <li><strong>Automated Fare Collection (AFC):</strong> Full-stack fare engines supporting distance-based, zone-based, flat-rate, and multi-modal transit tariffs.</li>
                    <li><strong>Account-Based Ticketing (ABT):</strong> Cloud-centric fare calculation allowing commuters to tap transit smart cards, bank EMV cards, or mobile phones interchangeably.</li>
                    <li><strong>In-Vehicle Dual-Bus Validators:</strong> Shock-resistant, vibration-tested validator units mounted at vehicle entry doors with sub-50ms passenger feedback.</li>
                    <li><strong>Driver Consoles &amp; Shift Management:</strong> Touchscreen driver terminals displaying route adherence, boarding counts, real-time fare receipts, and automated daily shift closeout.</li>
                    <li><strong>Central Operational Dashboard:</strong> Real-time cloud telematics monitoring vehicle GPS locations, passenger volumes, revenue collection, and fleet maintenance alerts.</li>
                </ul>

                <div class="sidebar-box" style="margin-top: 2rem; background: var(--bg-card-subtle);">
                    <h4 style="margin-bottom: 0.8rem;">Live Program Execution</h4>
                    <p style="font-size: 0.92rem; color: var(--text-muted);">
                        This architecture forms the operational core of the <strong>South Africa National Mobility and Payments Program</strong>, currently rolling out across 500,000 minibus taxis nationwide.
                    </p>
                    <a href="africa-national-mobility-program.html" class="pillar-link" style="margin-top: 0.5rem;">View SANTACO National Program Case Study →</a>
                </div>
            </div>

            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">TRANSIT AUTHORITIES</span>
                    <h4 style="margin-bottom: 0.8rem;">Concession Inquiries</h4>
                    <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1rem;">
                        Consult with our mobility architects on municipal transit digitization and national fare collection concessions:
                    </p>
                    <a href="contact.html?dept=africa" class="btn-primary" style="width: 100%; text-align: center; display: block;">
                        <span>Inquire Mobility Project</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("solutions-mobility.html", header + body + get_footer())

# ==============================================================================
# 10. SOLUTIONS-TELECOM.HTML — PILLAR 4: TELECOMMUNICATIONS & CONNECTED DEVICES
# ==============================================================================
def build_solutions_telecom():
    header = get_header(
        title="Telecommunications & Connected Devices — GENTECH GROUP",
        desc="5G Super SIM cards, eSIM remote profile management, connected vehicle telemetry, and secure IoT hardware solutions.",
        active_nav="solutions"
    )
    banner = get_page_banner(
        title="Telecommunications &amp; Connected Devices",
        sub="5G Super SIM, eSIM Remote Lifecycle Management, Vehicle Telematics &amp; M2M Security.",
        crumb="Solutions / Telecommunications",
        badge="✦ PILLAR 04 // CELLULAR IDENTITY &amp; IOT"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">SECURE CONNECTIVITY</span>
                <h2 class="serif-title" style="margin-bottom: 1.25rem;">Next-Gen Cellular Identity &amp; Connected Vehicle Modules</h2>
                <p>
                    Gentech Group provides high-security telecommunication products engineered to connect millions of payment terminals, transit vehicles, and mobile subscribers with carrier-grade reliability.
                </p>
                
                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">Core Offerings</h3>
                <ul style="padding-left: 1.5rem; line-height: 1.8; color: var(--text-muted); margin-bottom: 1.5rem;">
                    <li><strong>Super SIM 5G Multi-IMSI:</strong> Smart SIM cards with dynamic multi-carrier network auto-switching, ensuring 99.999% uptime for remote payment validators.</li>
                    <li><strong>eSIM Remote Provisioning (RSP):</strong> GSMA-compliant M2M and Consumer eSIM platforms for over-the-air subscription profile switching.</li>
                    <li><strong>Connected Vehicle Telematics:</strong> Rugged on-board units (OBU) delivering continuous CAN-bus diagnostic telemetry, GPS geofencing, and emergency communications.</li>
                    <li><strong>Cryptographic IoT Elements:</strong> Hardware root-of-trust chips preventing SIM swapping, data tampering, and unauthorized terminal cloning.</li>
                </ul>
            </div>

            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">TELECOM INQUIRIES</span>
                    <h4 style="margin-bottom: 0.8rem;">Carrier Solutions</h4>
                    <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1rem;">
                        Procure carrier SIM batches or integrate eSIM remote subscription platforms:
                    </p>
                    <a href="contact.html?dept=cards" class="btn-primary" style="width: 100%; text-align: center; display: block;">
                        <span>Inquire SIM Solutions</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("solutions-telecom.html", header + body + get_footer())

# ==============================================================================
# 11. SOLUTIONS-INFRASTRUCTURE.HTML — PILLAR 5: DIGITAL INFRASTRUCTURE
# ==============================================================================
def build_solutions_infrastructure():
    header = get_header(
        title="Digital Infrastructure & Cloud Clearing — GENTECH GROUP",
        desc="Sovereign cloud platforms, high-throughput clearing, HSM key injection, big data transit analytics, and cybersecurity.",
        active_nav="solutions"
    )
    banner = get_page_banner(
        title="Digital Infrastructure",
        sub="Sovereign Cloud Platforms, HSM Key Injection, Clearing Engines &amp; Big Data.",
        crumb="Solutions / Digital Infrastructure",
        badge="✦ PILLAR 05 // CLOUD CLEARING &amp; CYBERSECURITY"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">SOVEREIGN RESILIENCE</span>
                <h2 class="serif-title" style="margin-bottom: 1.25rem;">Enterprise-Scale Cloud Clearing &amp; Hardware Cryptography</h2>
                <p>
                    Gentech Group builds the back-office backbone for multi-million-user transaction networks. We combine sovereign cloud hosting, dedicated Hardware Security Modules (HSMs), and real-time big data pipelines to ensure zero-loss financial settlement.
                </p>
                
                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">Capabilities</h3>
                <ul style="padding-left: 1.5rem; line-height: 1.8; color: var(--text-muted); margin-bottom: 1.5rem;">
                    <li><strong>High-Throughput Clearing Engine:</strong> Scalable microservices handling tens of thousands of concurrent fare and retail transactions per second.</li>
                    <li><strong>HSM Key Management &amp; Injection:</strong> FIPS 140-2 Level 3 hardware security facilities for cryptographic root key generation and remote key injection.</li>
                    <li><strong>Identity &amp; Access Management (IAM):</strong> Biometric identity verification and role-based operational permissions.</li>
                    <li><strong>Big Data Analytics:</strong> Actionable dashboards for transit route optimization, passenger heatmaps, and financial fraud prevention.</li>
                </ul>
            </div>

            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">INFRASTRUCTURE</span>
                    <h4 style="margin-bottom: 0.8rem;">Cloud &amp; Security</h4>
                    <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1rem;">
                        Consult with our enterprise architects on sovereign clearing and HSM key management:
                    </p>
                    <a href="contact.html?dept=partnerships" class="btn-primary" style="width: 100%; text-align: center; display: block;">
                        <span>Inquire Infrastructure</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("solutions-infrastructure.html", header + body + get_footer())

# ==============================================================================
# 12. SOLUTIONS-CAPITAL.HTML — PILLAR 6: CAPITAL & STRATEGIC PROJECTS
# ==============================================================================
def build_solutions_capital():
    header = get_header(
        title="Capital & Strategic Projects — GENTECH GROUP",
        desc="Project financing, sovereign concession frameworks, Public-Private Partnerships (PPP), and emerging market execution.",
        active_nav="solutions"
    )
    banner = get_page_banner(
        title="Capital &amp; Strategic Projects",
        sub="Project Finance, PPP Concessions, Sovereign Infrastructure Investment &amp; Market Execution.",
        crumb="Solutions / Capital & Projects",
        badge="✦ PILLAR 06 // STRUCTURED FINANCE &amp; PPP CONCESSIONS"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">STRATEGIC GOVERNANCE</span>
                <h2 class="serif-title" style="margin-bottom: 1.25rem;">Structuring Multi-Year Sovereign Infrastructure Concessions</h2>
                <p>
                    Through <strong>GENTECH CAPITAL HOLDINGS INC.</strong> (Canada) and regional operating entities, Gentech Group finances, structures, and executes large-scale public-private partnerships (PPP) in digital payments, transit automation, and national telecommunications infrastructure.
                </p>
                
                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">Our Investment Principles</h3>
                <ul style="padding-left: 1.5rem; line-height: 1.8; color: var(--text-muted); margin-bottom: 1.5rem;">
                    <li><strong>Long-Term Value Creation:</strong> Structuring 10+ year concessions that generate predictable, recurring transaction yields while transforming national economic infrastructure.</li>
                    <li><strong>Turnkey Execution:</strong> We don't just provide capital—we deliver the hardware manufacturing, software engineering, and on-the-ground operational deployment.</li>
                    <li><strong>Risk-Balanced Concession Frameworks:</strong> Structuring contractual alignments between state transit authorities, private operator associations, and international debt financiers.</li>
                </ul>
            </div>

            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">HOLDING CAPITAL</span>
                    <h4 style="margin-bottom: 0.8rem;">Project Financing</h4>
                    <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1rem;">
                        For government concession discussions, sovereign co-investments, and PPP structuring:
                    </p>
                    <a href="contact.html?dept=investments" class="btn-primary" style="width: 100%; text-align: center; display: block;">
                        <span>Contact Investment Office</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("solutions-capital.html", header + body + get_footer())

# ==============================================================================
# 13. AFRICA-NATIONAL-MOBILITY-PROGRAM.HTML — FLAGSHIP PROGRAM
# ==============================================================================
def build_africa_program():
    header = get_header(
        title="South Africa National Mobility & Payments Program — GENTECH GROUP",
        desc="Executed by Gentech Capital Holding (Pty) Ltd under a 10-year national agreement with SANTACO through TaxiChoice, deploying smart transit payments across 500,000 minibus taxis.",
        active_nav="africa"
    )
    banner = get_page_banner(
        title="South Africa National Mobility &amp; Payments Program",
        sub="A 10-Year Generational Concession Digitizing 500,000 Minibus Taxis and Serving 65 Million Commuters.",
        crumb="Africa Program",
        badge="🇿🇦 FLAGSHIP NATIONAL INFRASTRUCTURE • SIGNED &amp; EFFECTIVE"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">OFFICIAL NATIONAL PROGRAM OVERVIEW</span>
                <h2 class="serif-title" style="margin-bottom: 1.25rem;">Transforming South Africa's Minibus Taxi Economy</h2>
                <p>
                    On <strong>June 8, 2026</strong>, <strong>GENTECH CAPITAL HOLDING (PTY) LTD</strong> entered into a binding, 10-year national contractual agreement with the South African National Taxi Council (<strong>SANTACO</strong>) through its commercial vehicle <strong>TaxiChoice</strong>.
                </p>
                <p>
                    Under this national mandate, Gentech Group serves as the primary technology provider, payment clearing operator, and hardware deployment partner to digitize South Africa's vast minibus taxi network—the lifeblood of the nation's public transportation.
                </p>

                <!-- Program Scope Grid -->
                <div class="africa-stats-row" style="margin: 2.5rem 0;">
                    <div class="san-stat-card" style="background: #fff; border: 1px solid var(--border-light);">
                        <div class="san-stat-val" style="color: var(--accent-hermes);">500,000</div>
                        <div class="san-stat-lbl" style="color: var(--text-main);">Minibus Taxis Nationwide</div>
                    </div>
                    <div class="san-stat-card" style="background: #fff; border: 1px solid var(--border-light);">
                        <div class="san-stat-val" style="color: var(--accent-hermes);">65M</div>
                        <div class="san-stat-lbl" style="color: var(--text-main);">Target Commuters Served</div>
                    </div>
                    <div class="san-stat-card" style="background: #fff; border: 1px solid var(--border-light);">
                        <div class="san-stat-val" style="color: var(--accent-hermes);">10 YRS</div>
                        <div class="san-stat-lbl" style="color: var(--text-main);">Contractual Concession</div>
                    </div>
                </div>

                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">Phased Rollout: Mpumalanga Pilot to National Scale</h3>
                <p>
                    The national deployment commences with a dedicated <strong>1,000-vehicle pilot phase in Mpumalanga</strong>, testing and calibrating validator hardware, cellular telemetry across rural and urban routes, driver shift balancing, and automated daily bank settlements before nationwide scaling across all 9 provinces.
                </p>

                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">The End-to-End System Architecture</h3>
                <ul class="arch-flow-list" style="margin-bottom: 2rem;">
                    <li class="arch-flow-item" style="background: #fff; border: 1px solid var(--border-light); color: var(--text-main);">
                        <span class="arch-flow-num">01. Commuter Smart Tap</span>
                        <span>Commuters pay via dual-interface closed-loop Transit Smart Cards, EMV contactless bank cards, or mobile QR wallets.</span>
                    </li>
                    <li class="arch-flow-item" style="background: #fff; border: 1px solid var(--border-light); color: var(--text-main);">
                        <span class="arch-flow-num">02. In-Vehicle POS Validator</span>
                        <span>Rugged Android dual-bus terminal mounted at vehicle entry captures tap data in under 50ms with instant audio-visual confirmation.</span>
                    </li>
                    <li class="arch-flow-item" style="background: #fff; border: 1px solid var(--border-light); color: var(--text-main);">
                        <span class="arch-flow-num">03. Driver Telemetry Terminal</span>
                        <span>Driver console displays live passenger tallies, shift revenue, and route telemetry.</span>
                    </li>
                    <li class="arch-flow-item" style="background: #fff; border: 1px solid var(--border-light); color: var(--text-main);">
                        <span class="arch-flow-num">04. 5G Encrypted Clearing Gateway</span>
                        <span>Transactions are securely batched and dispatched via Super SIM 5G telemetry to Gentech's sovereign cloud clearing house.</span>
                    </li>
                    <li class="arch-flow-item" style="background: #fff; border: 1px solid var(--border-light); color: var(--text-main);">
                        <span class="arch-flow-num">05. Automated Daily Settlement</span>
                        <span>Funds are reconciled and disbursed directly into taxi owner and regional association bank accounts each evening.</span>
                    </li>
                </ul>

                <h3 style="margin-top: 2rem; margin-bottom: 1rem;">Generational Socio-Economic Impact</h3>
                <p>
                    By transitioning the taxi industry from physical cash to secure digital transit payments, the program reduces armed robbery risks for drivers, eliminates cash handling losses for fleet owners, brings millions of unbanked citizens into the formal financial ecosystem, and creates thousands of local technical support jobs across South Africa.
                </p>
            </div>

            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">JOHANNESBURG HUB</span>
                    <h4 style="margin-bottom: 0.8rem;">Program Office</h4>
                    <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1rem;">
                        <strong>Gentech Capital Holding (Pty) Ltd</strong><br>
                        Johannesburg, South Africa<br>
                        Official Program Inquiries:<br>
                        <a href="mailto:africa@gentech.ae" style="color:var(--accent-hermes); font-weight:600;">africa@gentech.ae</a>
                    </p>
                    <a href="contact.html?dept=africa" class="btn-primary" style="width: 100%; text-align: center; display: block; margin-bottom: 0.5rem;">
                        <span>Contact Africa Hub</span>
                    </a>
                    <a href="group-africa.html" class="btn-secondary" style="width: 100%; text-align: center; display: block;">
                        <span>Gentech Africa Profile</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("africa-national-mobility-program.html", header + body + get_footer())

# ==============================================================================
# 14. PROJECTS.HTML — STRATEGIC CASE STUDIES
# ==============================================================================
def build_projects():
    header = get_header(
        title="Projects &amp; Strategic Case Studies — GENTECH GROUP",
        desc="Explore selected approved implementations, national mobility programs, luxury bank metal issuance, and telecom infrastructure deployments.",
        active_nav="projects"
    )
    banner = get_page_banner(
        title="Projects &amp; Case Studies",
        sub="Approved Strategic Deployments Across Mass Transit, Tier-1 Banking, and Telecom Infrastructure.",
        crumb="Projects",
        badge="✦ GENTECH GROUP • PROVEN DEPLOYMENTS"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
            <div class="pillar-card">
                <span class="calm-tag" style="margin-bottom: 0.5rem;">NATIONAL CONCESSION</span>
                <h3 class="pillar-title">South Africa National Transit Digitization</h3>
                <p class="pillar-desc">
                    10-year contractual program with SANTACO / TaxiChoice automating fare collection and banking inclusion across 500,000 minibus taxis.
                </p>
                <a href="africa-national-mobility-program.html" class="pillar-link">Read Full Case Study →</a>
            </div>

            <div class="pillar-card">
                <span class="calm-tag" style="margin-bottom: 0.5rem;">TIER-1 BANKING</span>
                <h3 class="pillar-title">Sovereign Metal Card Portfolio</h3>
                <p class="pillar-desc">
                    Bespoke CNC titanium and 24K gold-plated EMV card issuance for premier banking institutions in the Middle East and international markets.
                </p>
                <a href="solutions-cards.html" class="pillar-link">Explore Card Tech →</a>
            </div>

            <div class="pillar-card">
                <span class="calm-tag" style="margin-bottom: 0.5rem;">TELECOMMUNICATIONS</span>
                <h3 class="pillar-title">5G Super SIM &amp; IoT Fleet Rollout</h3>
                <p class="pillar-desc">
                    High-resilience multi-carrier cellular SIM deployment powering real-time financial telemetry for connected transport and payment terminals.
                </p>
                <a href="solutions-telecom.html" class="pillar-link">Explore Telecom Tech →</a>
            </div>
        </div>
    </div>
</section>
"""
    write_file("projects.html", header + body + get_footer())

# ==============================================================================
# 15. NEWS.HTML — NEWS & MEDIA KIT
# ==============================================================================
def build_news():
    header = get_header(
        title="News &amp; Media — GENTECH GROUP",
        desc="Official corporate announcements, press releases, media kits, and verified milestones from Gentech Group.",
        active_nav="news"
    )
    banner = get_page_banner(
        title="News &amp; Media Center",
        sub="Official Press Releases, Corporate Milestones &amp; Brand Resources.",
        crumb="News & Media",
        badge="✦ GENTECH GROUP • PRESS &amp; INSIGHTS"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <div class="detail-page-layout">
            <div class="detail-main-content">
                <span class="calm-tag">OFFICIAL ANNOUNCEMENTS</span>
                <h2 class="serif-title" style="margin-bottom: 1.5rem;">Corporate Communications</h2>

                <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                    <div style="background: #fff; border: 1px solid var(--border-light); padding: 1.8rem; border-radius: var(--radius-md);">
                        <div style="font-size: 0.78rem; font-family: var(--font-mono); color: var(--accent-hermes); margin-bottom: 0.3rem;">30 AUGUST 2026 // CORPORATE</div>
                        <h4 style="font-size: 1.25rem; margin-bottom: 0.5rem;">Gentech Group Announces Tri-Continental Corporate Restructuring</h4>
                        <p style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.6;">
                            Gentech Group officially unifies its governance across Canada (Holding), UAE (Technology &amp; Trade), and South Africa (Africa Operations) under the centralized leadership of Chairman Mustafa Sertkaya.
                        </p>
                    </div>

                    <div style="background: #fff; border: 1px solid var(--border-light); padding: 1.8rem; border-radius: var(--radius-md);">
                        <div style="font-size: 0.78rem; font-family: var(--font-mono); color: var(--accent-hermes); margin-bottom: 0.3rem;">8 JUNE 2026 // SIGNED CONTRACT</div>
                        <h4 style="font-size: 1.25rem; margin-bottom: 0.5rem;">Execution of 10-Year National Mobility &amp; Payments Agreement in South Africa</h4>
                        <p style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.6;">
                            Gentech Capital Holding (Pty) Ltd executes a 10-year national agreement with SANTACO via TaxiChoice to deploy automated contactless transit payment systems across 500,000 minibus taxis.
                        </p>
                    </div>
                </div>
            </div>

            <div class="detail-sidebar">
                <div class="sidebar-box">
                    <span class="calm-tag" style="margin-bottom: 0.5rem;">MEDIA KIT</span>
                    <h4 style="margin-bottom: 0.8rem;">Press Resources</h4>
                    <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1rem;">
                        For verified logo files, high-res executive portraits, and official company fact sheets:
                    </p>
                    <div style="font-size: 0.85rem; color: var(--text-dim); margin-bottom: 1.2rem;">
                        <strong>Media Relations:</strong><br>
                        Email: <a href="mailto:media@gentech.ae" style="color:var(--accent-hermes); font-weight:600;">media@gentech.ae</a>
                    </div>
                    <a href="contact.html?dept=media" class="btn-primary" style="width: 100%; text-align: center; display: block;">
                        <span>Inquire with Media Office</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    write_file("news.html", header + body + get_footer())

# ==============================================================================
# 16. CONTACT.HTML — MULTI-HUB DIRECTORY & INQUIRY ROUTER
# ==============================================================================
def build_contact():
    header = get_header(
        title="Contact Gentech Group — Toronto • Ras Al Khaimah • Johannesburg",
        desc="Contact Gentech Group corporate offices across Canada, UAE, and South Africa. Route inquiries to Investment, Card Production, Mobility, or Media.",
        active_nav="contact"
    )
    banner = get_page_banner(
        title="Contact Gentech Group",
        sub="Direct Inquiries to Our Global Operational Hubs in Canada, the United Arab Emirates, and South Africa.",
        crumb="Contact",
        badge="✦ GENTECH GROUP • GLOBAL DIRECTORY"
    )
    
    body = f"""{banner}
<section class="section-spacing">
    <div class="container">
        <!-- 3 Registered Hubs Directory -->
        <div class="hubs-grid-3" style="margin-bottom: 3.5rem;">
            <!-- Toronto -->
            <div class="hub-card">
                <div class="hub-flag-badge">🍁</div>
                <h3 class="hub-name">Toronto, Canada</h3>
                <div class="hub-entity-title">GENTECH CAPITAL HOLDINGS INC.</div>
                <p class="hub-role-desc">Holding Governance, Investor Relations, Concessions &amp; Strategic Treasury.</p>
                <div class="hub-meta-list">
                    <div><strong>Jurisdiction:</strong> Ontario, Canada</div>
                    <div><strong>Email:</strong> investments@gentech.ae</div>
                </div>
            </div>

            <!-- UAE -->
            <div class="hub-card">
                <div class="hub-flag-badge">🇦🇪</div>
                <h3 class="hub-name">Ras Al Khaimah, UAE</h3>
                <div class="hub-entity-title">GENTECH GLOBAL FZ-LLC</div>
                <p class="hub-role-desc">Smart Card Production, POS Terminals, Chip Modules &amp; International Trade.</p>
                <div class="hub-meta-list">
                    <div><strong>Address:</strong> Compass Building, Al Shohada Rd, AL Hamra Industrial Zone-FZ, RAK, UAE</div>
                    <div><strong>Email:</strong> cards@gentech.ae / info@gentech.ae</div>
                </div>
            </div>

            <!-- South Africa -->
            <div class="hub-card">
                <div class="hub-flag-badge">🇿🇦</div>
                <h3 class="hub-name">Johannesburg, South Africa</h3>
                <div class="hub-entity-title">GENTECH CAPITAL HOLDING (PTY) LTD</div>
                <p class="hub-role-desc">Africa Operations, SANTACO National Mobility Program &amp; Field Support.</p>
                <div class="hub-meta-list">
                    <div><strong>Jurisdiction:</strong> Johannesburg, South Africa</div>
                    <div><strong>Email:</strong> africa@gentech.ae</div>
                </div>
            </div>
        </div>

        <!-- Interactive Departmental Inquiry Routing Form -->
        <div style="max-width: 860px; margin: 0 auto; background: #fff; border: 1px solid var(--border-light); border-radius: var(--radius-lg); padding: clamp(2rem, 4vw, 3.5rem); box-shadow: var(--shadow-card);">
            <div class="calm-tag" style="margin-bottom: 0.5rem;">DEPARTMENTAL ROUTING</div>
            <h3 class="serif-title" style="margin-bottom: 0.5rem;">Submit Institutional Inquiry</h3>
            <p style="font-size: 0.92rem; color: var(--text-muted); margin-bottom: 2rem;">
                Your inquiry will be automatically routed to the responsible managing executive and logged in our secure CRM.
            </p>

            <form id="gentechInquiryForm" onsubmit="event.preventDefault(); document.getElementById('formSuccessMsg').style.display='block'; this.reset();">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">
                    <div>
                        <label style="display: block; font-size: 0.84rem; font-weight: 700; margin-bottom: 0.4rem;">Full Name *</label>
                        <input type="text" required placeholder="e.g. David Sterling" style="width: 100%; padding: 0.8rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-light); font-size: 0.92rem;">
                    </div>
                    <div>
                        <label style="display: block; font-size: 0.84rem; font-weight: 700; margin-bottom: 0.4rem;">Corporate / Institutional Email *</label>
                        <input type="email" required placeholder="e.g. d.sterling@bank.com" style="width: 100%; padding: 0.8rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-light); font-size: 0.92rem;">
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">
                    <div>
                        <label style="display: block; font-size: 0.84rem; font-weight: 700; margin-bottom: 0.4rem;">Organization / Company *</label>
                        <input type="text" required placeholder="e.g. Sovereign Transport Authority" style="width: 100%; padding: 0.8rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-light); font-size: 0.92rem;">
                    </div>
                    <div>
                        <label style="display: block; font-size: 0.84rem; font-weight: 700; margin-bottom: 0.4rem;">Inquiry Department *</label>
                        <select required style="width: 100%; padding: 0.8rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-light); font-size: 0.92rem; background: #fff;">
                            <option value="general">General Corporate Enquiries (info@gentech.ae)</option>
                            <option value="cards">Card Manufacturing &amp; Hardware (cards@gentech.ae)</option>
                            <option value="investments">Investment &amp; Holding (investments@gentech.ae)</option>
                            <option value="africa">Africa Operations &amp; Mobility (africa@gentech.ae)</option>
                            <option value="partnerships">Strategic Partnerships (partnerships@gentech.ae)</option>
                            <option value="media">Media &amp; Press (media@gentech.ae)</option>
                            <option value="procurement">Procurement &amp; Suppliers (procurement@gentech.ae)</option>
                        </select>
                    </div>
                </div>

                <div style="margin-bottom: 1.5rem;">
                    <label style="display: block; font-size: 0.84rem; font-weight: 700; margin-bottom: 0.4rem;">Inquiry Details *</label>
                    <textarea required rows="4" placeholder="Specify your requirements, project scope, or technical specifications..." style="width: 100%; padding: 0.8rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-light); font-size: 0.92rem;"></textarea>
                </div>

                <div style="margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.6rem;">
                    <input type="checkbox" required id="privacyConsent" style="width: 16px; height: 16px;">
                    <label for="privacyConsent" style="font-size: 0.82rem; color: var(--text-muted);">
                        I agree to the processing of my business contact data in accordance with the <a href="privacy.html" style="color:var(--accent-hermes); text-decoration:underline;">Privacy Policy</a> (GDPR/POPIA).
                    </label>
                </div>

                <button type="submit" class="btn-primary" style="width: 100%; justify-content: center;">
                    <span>Submit Inquiry to Gentech Group</span>
                </button>
            </form>

            <div id="formSuccessMsg" style="display: none; margin-top: 1.5rem; padding: 1.2rem; background: #E8F5E9; border: 1px solid #4CAF50; border-radius: var(--radius-sm); color: #2E7D32; font-size: 0.9rem; text-align: center;">
                ✓ <strong>Thank you.</strong> Your inquiry has been securely logged and dispatched to the designated Gentech Group management office. Our executive team will respond shortly.
            </div>
        </div>
    </div>
</section>
"""
    write_file("contact.html", header + body + get_footer())

# ==============================================================================
# 17-20. LEGAL & COMPLIANCE SUITE (PRIVACY, TERMS, LEGAL, COMPLIANCE)
# ==============================================================================
def build_legal_suite():
    # Privacy Policy
    p_header = get_header(title="Privacy Policy — GENTECH GROUP", desc="Privacy Policy compliant with GDPR, South Africa POPIA, and UAE Federal Law No. 45.")
    p_banner = get_page_banner(title="Privacy Policy", sub="Data Protection & Privacy Framework (GDPR, POPIA, UAE Law)", crumb="Privacy Policy", badge="✦ LEGAL &amp; COMPLIANCE")
    p_body = f"""{p_banner}
<section class="section-spacing">
    <div class="container">
        <div class="legal-container">
            <div class="legal-section-block">
                <h2>1. Commitment to Data Protection</h2>
                <p>Gentech Group (comprising Gentech Capital Holdings Inc. in Canada, Gentech Global FZ-LLC in the United Arab Emirates, and Gentech Capital Holding (Pty) Ltd in South Africa) is dedicated to protecting the privacy, confidentiality, and security of personal and institutional data entrusted to us.</p>
                <p>This Privacy Policy outlines our data processing standards in full compliance with the European Union General Data Protection Regulation (GDPR), South Africa's Protection of Personal Information Act 4 of 2013 (POPIA), and UAE Federal Decree-Law No. 45 of 2021 regarding Personal Data Protection.</p>
            </div>
            <div class="legal-section-block">
                <h2>2. Data Collection and Lawful Basis</h2>
                <p>We process personal and organizational information strictly where necessary to execute contractual agreements, maintain public-private concession operations, provide secure financial terminal access, and respond to legitimate institutional inquiries.</p>
            </div>
            <div class="legal-section-block">
                <h2>3. Contact Data Protection Officer</h2>
                <p>For data access requests or privacy inquiries, contact: <a href="mailto:info@gentech.ae">info@gentech.ae</a>.</p>
            </div>
        </div>
    </div>
</section>
"""
    write_file("privacy.html", p_header + p_body + get_footer())

    # Terms of Use
    t_header = get_header(title="Terms of Use — GENTECH GROUP", desc="Terms of Use for gentech.ae and Gentech Group digital platforms.")
    t_banner = get_page_banner(title="Terms of Use", sub="Website Terms of Use and Intellectual Property Notice.", crumb="Terms of Use", badge="✦ LEGAL &amp; COMPLIANCE")
    t_body = f"""{t_banner}
<section class="section-spacing">
    <div class="container">
        <div class="legal-container">
            <div class="legal-section-block">
                <h2>1. Acceptance of Terms</h2>
                <p>By accessing or utilizing the website gentech.ae and associated digital portals operated by Gentech Group, you agree to be bound by these Terms of Use and all applicable laws and regulations.</p>
            </div>
            <div class="legal-section-block">
                <h2>2. Intellectual Property Rights</h2>
                <p>All content, 3D models, technical diagrams, trademarks, logos, and software code displayed on gentech.ae are the exclusive intellectual property of Gentech Group or its licensors and are protected under international copyright and intellectual property treaties.</p>
            </div>
        </div>
    </div>
</section>
"""
    write_file("terms.html", t_header + t_body + get_footer())

    # Legal Notice
    l_header = get_header(title="Legal Notice & Disclaimers — GENTECH GROUP", desc="Official Corporate Registry Details, Jurisdictional Disclaimers, and Regulatory Disclosures.")
    l_banner = get_page_banner(title="Legal Notice &amp; Disclaimer", sub="Official Corporate Registry &amp; Regulatory Disclosures.", crumb="Legal Notice", badge="✦ LEGAL &amp; COMPLIANCE")
    l_body = f"""{banner_legal}""" if 'banner_legal' in locals() else f"""{l_banner}
<section class="section-spacing">
    <div class="container">
        <div class="legal-container">
            <div class="legal-section-block">
                <h2>Corporate Registration Disclosures</h2>
                <p>Gentech Group operates globally through three legally distinct entities:</p>
                <table class="legal-table">
                    <tr><th>Entity Name</th><th>Jurisdiction</th><th>Role</th></tr>
                    <tr><td><strong>GENTECH CAPITAL HOLDINGS INC.</strong></td><td>Ontario, Canada</td><td>Parent Holding &amp; Capital Governance</td></tr>
                    <tr><td><strong>GENTECH GLOBAL FZ-LLC</strong></td><td>Ras Al Khaimah (RAKEZ), UAE</td><td>Payment Technologies &amp; International Trade</td></tr>
                    <tr><td><strong>GENTECH CAPITAL HOLDING (PTY) LTD</strong></td><td>Johannesburg, South Africa</td><td>Africa Operations &amp; Transit Program Execution</td></tr>
                </table>
            </div>
        </div>
    </div>
</section>
"""
    write_file("legal.html", l_header + l_body + get_footer())

    # Compliance
    c_header = get_header(title="Compliance &amp; Governance — GENTECH GROUP", desc="Information Security, AML/KYC, Anti-Bribery and Corruption, and Supplier Standards.")
    c_banner = get_page_banner(title="Compliance &amp; Governance", sub="Anti-Money Laundering, Anti-Bribery, Information Security &amp; Ethics.", crumb="Compliance", badge="✦ GOVERNANCE FRAMEWORK")
    c_body = f"""{c_banner}
<section class="section-spacing">
    <div class="container">
        <div class="legal-container">
            <div class="legal-section-block">
                <h2>1. Anti-Money Laundering (AML) &amp; KYC Standards</h2>
                <p>Gentech Group maintains rigorous AML and Know-Your-Customer protocols across all payment hardware distribution, smart card issuance, and merchant settlement accounts.</p>
            </div>
            <div class="legal-section-block">
                <h2>2. Information Security Standards</h2>
                <p>Our digital infrastructure adheres to ISO/IEC 27001 information security principles, FIPS 140-2 Level 3 HSM hardware encryption, and PCI PTS terminal security standards.</p>
            </div>
            <div class="legal-section-block">
                <h2>3. Anti-Bribery &amp; Corruption Policy</h2>
                <p>Gentech Group strictly prohibits any form of bribery, extortion, or unethical facilitation payments in all jurisdictions where we operate.</p>
            </div>
        </div>
    </div>
</section>
"""
    write_file("compliance.html", c_header + c_body + get_footer())

# ==============================================================================
# 21. ALIAS REDIRECTS (FOR OLD URL COMPATIBILITY)
# ==============================================================================
def build_alias_redirects():
    redirects = {
        "emvcards.html": "solutions-cards.html",
        "metalcards.html": "solutions-cards.html",
        "ceramiccards.html": "solutions-cards.html",
        "chipmodules.html": "solutions-cards.html",
        "wearable.html": "solutions-cards.html",
        "chip.html": "solutions-cards.html",
        "perso.html": "solutions-cards.html",
        "products.html": "solutions-cards.html",
        "service.html": "solutions-cards.html",
        "hardware.html": "solutions-payments.html",
        "transport.html": "solutions-mobility.html",
        "telecom.html": "solutions-telecom.html",
    }
    
    for old_file, target in redirects.items():
        content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url={target}">
    <title>Redirecting to {target} | GENTECH GROUP</title>
    <link rel="canonical" href="https://gentech.ae/{target}">
</head>
<body>
    <p>Redirecting to <a href="{target}">{target}</a>...</p>
</body>
</html>"""
        write_file(old_file, content)

# Execute All Generators
build_group_canada()
build_group_uae()
build_group_africa()
build_solutions_cards()
build_solutions_payments()
build_solutions_mobility()
build_solutions_telecom()
build_solutions_infrastructure()
build_solutions_capital()
build_africa_program()
build_projects()
build_news()
build_contact()
build_legal_suite()
build_alias_redirects()

print("ALL GENTECH GROUP PAGES COMPILED SUCCESSFULLY!")
