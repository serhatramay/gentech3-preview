import re

# 1. Update build_all_gentech_group.py get_footer with bulletproof inline styles
base_path = "/Users/ramay/gentech3-app/build_all_gentech_group.py"
with open(base_path, "r", encoding="utf-8") as f:
    code = f.read()

old_footer_block = """        <!-- Registered Legal Entities Accordion/Block -->
        <div class="footer-legal-entities">
            <div class="entities-grid">
                <div class="entity-card">
                    <span class="entity-tag">Holding Company</span>
                    <h5>GENTECH CAPITAL HOLDINGS INC.</h5>
                    <p>Registered in Ontario, Canada. Capital allocation, investment portfolio management and strategic governance.</p>
                </div>
                <div class="entity-card">
                    <span class="entity-tag">Technology &amp; Trade Hub</span>
                    <h5>GENTECH GLOBAL FZ-LLC</h5>
                    <p>Registered in RAKEZ, Ras Al Khaimah, UAE. Smart card engineering, payment terminals, chip design and international trade.</p>
                </div>
                <div class="entity-card">
                    <span class="entity-tag">Africa Operations Hub</span>
                    <h5>GENTECH CAPITAL HOLDING (PTY) LTD</h5>
                    <p>Registered in Johannesburg, South Africa. Execution of the 10-year National Mobility and Payments Program.</p>
                </div>
            </div>
        </div>"""

new_footer_block = """        <!-- Registered Legal Entities Accordion/Block (Guaranteed High Contrast) -->
        <div class="footer-legal-entities" style="margin-top: 3rem; padding-top: 2.5rem; border-top: 1px solid rgba(255, 255, 255, 0.1);">
            <div class="entities-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
                <div class="entity-card" style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(235, 101, 26, 0.35); border-radius: 12px; padding: 1.5rem; backdrop-filter: blur(10px);">
                    <span class="entity-tag" style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: #FF9E66; letter-spacing: 0.08em; display: block; margin-bottom: 0.4rem; font-family: monospace;">Holding Company</span>
                    <h5 style="color: #FFFFFF; font-size: 1rem; font-weight: 700; margin-bottom: 0.5rem; letter-spacing: 0.02em;">GENTECH CAPITAL HOLDINGS INC.</h5>
                    <p style="color: #D5C8BD; font-size: 0.84rem; line-height: 1.6; margin: 0;">Registered in Ontario, Canada. Capital allocation, investment portfolio management and strategic governance.</p>
                </div>
                <div class="entity-card" style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(235, 101, 26, 0.35); border-radius: 12px; padding: 1.5rem; backdrop-filter: blur(10px);">
                    <span class="entity-tag" style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: #FF9E66; letter-spacing: 0.08em; display: block; margin-bottom: 0.4rem; font-family: monospace;">Technology &amp; Trade Hub</span>
                    <h5 style="color: #FFFFFF; font-size: 1rem; font-weight: 700; margin-bottom: 0.5rem; letter-spacing: 0.02em;">GENTECH GLOBAL FZ-LLC</h5>
                    <p style="color: #D5C8BD; font-size: 0.84rem; line-height: 1.6; margin: 0;">Registered in RAKEZ, Ras Al Khaimah, UAE. Smart card engineering, payment terminals, chip design and international trade.</p>
                </div>
                <div class="entity-card" style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(235, 101, 26, 0.35); border-radius: 12px; padding: 1.5rem; backdrop-filter: blur(10px);">
                    <span class="entity-tag" style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: #FF9E66; letter-spacing: 0.08em; display: block; margin-bottom: 0.4rem; font-family: monospace;">Africa Operations Hub</span>
                    <h5 style="color: #FFFFFF; font-size: 1rem; font-weight: 700; margin-bottom: 0.5rem; letter-spacing: 0.02em;">GENTECH CAPITAL HOLDING (PTY) LTD</h5>
                    <p style="color: #D5C8BD; font-size: 0.84rem; line-height: 1.6; margin: 0;">Registered in Johannesburg, South Africa. Execution of the 10-year National Mobility and Payments Program.</p>
                </div>
            </div>
        </div>"""

code = code.replace(old_footer_block, new_footer_block)

# Also fix the bottom flex row with guaranteed inline styles
old_bottom_row = """        <div class="footer-bottom-flex">
            <div class="copyright-text">
                © 2026 GENTECH GROUP. All rights reserved. Global Capital, Payment Technologies and Digital Infrastructure.
            </div>
            <div class="footer-bottom-links">
                <a href="privacy.html">Privacy Policy (GDPR / POPIA)</a>
                <a href="terms.html">Terms of Use</a>
                <a href="legal.html">Legal Notice &amp; Disclaimer</a>
                <a href="compliance.html">Compliance &amp; Governance</a>
            </div>
        </div>"""

new_bottom_row = """        <div class="footer-bottom-flex" style="display: flex; justify-content: space-between; align-items: center; padding-top: 2.2rem; margin-top: 2.5rem; border-top: 1px solid rgba(255, 255, 255, 0.1); flex-wrap: wrap; gap: 1rem;">
            <div class="copyright-text" style="font-size: 0.82rem; color: #A89C94;">
                © 2026 GENTECH GROUP. All rights reserved. Global Capital, Payment Technologies and Digital Infrastructure.
            </div>
            <div class="footer-bottom-links" style="display: flex; gap: 1.2rem; flex-wrap: wrap;">
                <a href="privacy.html" style="font-size: 0.82rem; color: #CFC2B7; transition: color 0.2s;">Privacy Policy (GDPR / POPIA)</a>
                <a href="terms.html" style="font-size: 0.82rem; color: #CFC2B7; transition: color 0.2s;">Terms of Use</a>
                <a href="legal.html" style="font-size: 0.82rem; color: #CFC2B7; transition: color 0.2s;">Legal Notice &amp; Disclaimer</a>
                <a href="compliance.html" style="font-size: 0.82rem; color: #CFC2B7; transition: color 0.2s;">Compliance &amp; Governance</a>
            </div>
        </div>"""

code = code.replace(old_bottom_row, new_bottom_row)

with open(base_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_all_gentech_group.py with guaranteed inline footer styles.")

# 2. Clean duplicate old .entity-card in style.css
css_path = "/Users/ramay/gentech3-app/assets/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace any old rgba(255, 255, 255, 0.6)
css = css.replace("background: rgba(255, 255, 255, 0.6);", "background: rgba(255, 255, 255, 0.05);")
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Cleaned CSS file.")
