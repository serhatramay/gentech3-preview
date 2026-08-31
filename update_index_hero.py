import re

# Update build_index in generate_pages_master.py
with open("/Users/ramay/gentech3-app/generate_pages_master.py", "r", encoding="utf-8") as f:
    code = f.read()

new_index_body = '''
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
'''

# Replace inside build_index in generate_pages_master.py
pattern = re.compile(r'<!-- Hero Section -->.*?<!-- Scale & Operational Metrics Bar -->', re.DOTALL)
replacement = new_index_body + '\n<!-- Scale & Operational Metrics Bar -->'

code = pattern.sub(replacement, code)

with open("/Users/ramay/gentech3-app/generate_pages_master.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated generate_pages_master.py with restored 3D studio and polished hero.")
