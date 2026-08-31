import re

css_path = "/Users/ramay/gentech3-app/assets/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace mobile-drawer-footer padding
drawer_calibrated_css = """
/* ==========================================================================
   PERFECTLY CALIBRATED MOBILE DRAWER FOOTER (BALANCED BOTTOM GAP)
   ========================================================================== */
.mobile-nav-drawer {
  padding: 1.25rem 1.25rem 0.5rem 1.25rem !important;
}

.mobile-drawer-footer {
  margin-top: 1.25rem !important;
  padding-top: 0.9rem !important;
  padding-bottom: max(1.5rem, env(safe-area-inset-bottom) + 0.8rem) !important;
  border-top: 1px solid var(--border-light) !important;
  flex-shrink: 0 !important;
}

.mobile-drawer-footer .btn-primary {
  width: 100% !important;
  text-align: center !important;
  display: block !important;
  padding: 0.75rem 1rem !important;
  font-size: 0.86rem !important;
  font-weight: 700 !important;
  border-radius: var(--radius-full) !important;
  box-shadow: 0 4px 14px rgba(235, 101, 26, 0.25) !important;
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n" + drawer_calibrated_css)

print("Updated style.css with calibrated mobile drawer footer.")
