import re

css_path = "/Users/ramay/gentech3-app/assets/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix header positioning and hero padding
fix_header_css = """
/* Fixed Header & Top Utility Bar Positioning */
.top-utility-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 36px;
  z-index: 1002;
  background: #110B07;
  display: flex;
  align-items: center;
}

.main-header {
  position: fixed;
  top: 36px;
  left: 0;
  width: 100%;
  height: 76px;
  z-index: 1001;
  background: var(--bg-glass);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border-bottom: 1px solid var(--border-light);
}

@media (max-width: 820px) {
  .top-utility-bar { display: none !important; }
  .main-header { top: 0 !important; }
}

.hero-section, .page-banner-header {
  padding-top: 160px !important;
}

@media (max-width: 820px) {
  .hero-section, .page-banner-header {
    padding-top: 110px !important;
  }
}

.hero-hubs-ticker {
  margin-top: 1.8rem;
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
  background: rgba(255, 255, 255, 0.75);
  border: 1px solid var(--border-light);
  padding: 0.5rem 1.2rem;
  border-radius: var(--radius-full);
  font-size: 0.82rem;
  color: var(--text-dim);
  font-weight: 600;
  box-shadow: var(--shadow-soft);
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n" + fix_header_css)
print("Updated style.css with header & hero fixes.")

