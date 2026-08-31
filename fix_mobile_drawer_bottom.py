import re

# 1. Update style.css
css_path = "/Users/ramay/gentech3-app/assets/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

drawer_fix_css = """
/* ==========================================================================
   MOBILE DRAWER FULL HEIGHT & SAFE AREA INSET FIX (ZERO CLIPPING)
   ========================================================================== */
.mobile-nav-drawer {
  position: fixed !important;
  top: 0 !important;
  right: -100% !important;
  width: 85% !important;
  max-width: 380px !important;
  height: 100% !important;
  height: 100dvh !important; /* Modern Dynamic Viewport Height */
  background: #FFFFFF !important;
  box-shadow: -10px 0 35px rgba(0, 0, 0, 0.25) !important;
  z-index: 2000 !important;
  transition: right 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  padding: 1.5rem 1.5rem 0 1.5rem !important;
  overflow-y: auto !important;
  -webkit-overflow-scrolling: touch !important;
  display: flex !important;
  flex-direction: column !important;
}

.mobile-nav-drawer.open {
  right: 0 !important;
}

.mobile-drawer-footer {
  margin-top: 2rem !important;
  padding-top: 1rem !important;
  padding-bottom: max(4.5rem, env(safe-area-inset-bottom) + 3rem) !important;
  border-top: 1px solid var(--border-light) !important;
  flex-shrink: 0 !important;
}

.mobile-drawer-footer .btn-primary {
  width: 100% !important;
  text-align: center !important;
  display: block !important;
  padding: 0.85rem 1rem !important;
  font-size: 0.88rem !important;
  border-radius: var(--radius-full) !important;
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n" + drawer_fix_css)

print("Updated style.css with dynamic viewport & safe area drawer padding.")

# 2. Update build_all_gentech_group.py header template
base_path = "/Users/ramay/gentech3-app/build_all_gentech_group.py"
with open(base_path, "r", encoding="utf-8") as f:
    code = f.read()

old_drawer_footer = """    <div style="margin-top: auto; padding-top: 2rem;">
        <a href="contact.html" class="btn-primary" style="width: 100%; text-align: center; display: block;">
            <span>Submit Institutional Inquiry</span>
        </a>
    </div>"""

new_drawer_footer = """    <div class="mobile-drawer-footer">
        <a href="contact.html" class="btn-primary">
            <span>Submit Institutional Inquiry</span>
        </a>
    </div>"""

code = code.replace(old_drawer_footer, new_drawer_footer)

with open(base_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_all_gentech_group.py with mobile-drawer-footer container.")

