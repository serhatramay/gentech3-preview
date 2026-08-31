import re

css_path = "/Users/ramay/gentech3-app/assets/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace border-bottom on footer-top-grid
css = re.sub(r'\.footer-top-grid\s*\{[^}]*border-bottom:[^;]+;', '.footer-top-grid {\n  border-bottom: none !important;', css)

# Also ensure footer-top-grid has no bottom border in the override block
css += """
/* Single Clean Divider in Footer */
.footer-top-grid {
  border-bottom: none !important;
  padding-bottom: 1.5rem !important;
}

.footer-legal-entities {
  margin-top: 1.5rem !important;
  padding-top: 2rem !important;
  border-top: 1px solid rgba(255, 255, 255, 0.12) !important;
}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Updated style.css: Removed redundant footer divider line.")

