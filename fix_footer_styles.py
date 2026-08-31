import re

css_path = "/Users/ramay/gentech3-app/assets/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Refined Crystal-Clear Dark Footer Styles
footer_clean_css = """
/* ==========================================================================
   PERFECT LUXURY DARK FOOTER STYLING (HIGH CONTRAST & CRYSTAL CLEAR)
   ========================================================================== */
.footer-serene {
  background: #110B07 !important;
  color: #FAF2EB !important;
  padding-top: 4.5rem !important;
  padding-bottom: 3rem !important;
  margin-top: 5rem !important;
  border-top: 1px solid rgba(235, 101, 26, 0.25) !important;
}

.footer-top-grid {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
}

.footer-top-grid .brand-title { color: #FFFFFF !important; }
.footer-top-grid .brand-sub { color: #FF9E66 !important; }

.footer-heading {
  font-size: 0.92rem !important;
  font-weight: 700 !important;
  color: #FFFFFF !important;
  text-transform: uppercase !important;
  letter-spacing: 0.06em !important;
  margin-bottom: 1.2rem !important;
}

.footer-links {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0.65rem !important;
}

.footer-links li a {
  color: #CFC2B7 !important;
  font-size: 0.86rem !important;
  transition: color 0.2s ease !important;
}

.footer-links li a:hover {
  color: #FF9E66 !important;
  text-decoration: underline !important;
}

.footer-desc {
  color: #CFC2B7 !important;
  font-size: 0.9rem !important;
  line-height: 1.7 !important;
}

.footer-badge-row {
  margin-top: 1rem !important;
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 0.5rem !important;
}

.hub-pill {
  background: rgba(255, 255, 255, 0.06) !important;
  border: 1px solid rgba(235, 101, 26, 0.35) !important;
  border-radius: var(--radius-full) !important;
  padding: 0.3rem 0.85rem !important;
  font-size: 0.76rem !important;
  font-weight: 600 !important;
  color: #FAF2EB !important;
}

.footer-contact-item {
  font-size: 0.84rem !important;
  color: #CFC2B7 !important;
  margin-bottom: 0.8rem !important;
  line-height: 1.5 !important;
}

.footer-contact-item strong {
  display: block !important;
  color: #FFFFFF !important;
  font-weight: 700 !important;
  margin-bottom: 0.2rem !important;
}

/* 3 Legal Entities Cards (Crystal Clear Dark Glass) */
.footer-legal-entities {
  margin-top: 3rem !important;
  padding-top: 2.5rem !important;
  border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
}

.entities-grid {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 1.5rem !important;
}

@media (max-width: 850px) {
  .entities-grid { grid-template-columns: 1fr !important; }
}

.entity-card {
  background: rgba(255, 255, 255, 0.04) !important;
  border: 1px solid rgba(235, 101, 26, 0.25) !important;
  border-radius: 12px !important;
  padding: 1.5rem !important;
  backdrop-filter: blur(10px) !important;
  transition: all 0.3s ease !important;
}

.entity-card:hover {
  background: rgba(255, 255, 255, 0.07) !important;
  border-color: rgba(235, 101, 26, 0.5) !important;
  transform: translateY(-3px) !important;
}

.entity-tag {
  font-size: 0.72rem !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  color: #FF9E66 !important;
  letter-spacing: 0.08em !important;
  display: block !important;
  margin-bottom: 0.4rem !important;
  font-family: var(--font-mono) !important;
}

.entity-card h5 {
  font-size: 1rem !important;
  font-weight: 700 !important;
  color: #FFFFFF !important;
  margin-bottom: 0.5rem !important;
  letter-spacing: 0.02em !important;
}

.entity-card p {
  font-size: 0.84rem !important;
  color: #CFC2B7 !important;
  line-height: 1.6 !important;
  margin: 0 !important;
}

/* Footer Bottom Flex Row */
.footer-bottom-flex {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  padding-top: 2.2rem !important;
  margin-top: 2.5rem !important;
  border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
  flex-wrap: wrap !important;
  gap: 1rem !important;
}

.copyright-text {
  font-size: 0.82rem !important;
  color: #A89C94 !important;
}

.footer-bottom-links {
  display: flex !important;
  gap: 1.2rem !important;
  flex-wrap: wrap !important;
}

.footer-bottom-links a {
  font-size: 0.82rem !important;
  color: #CFC2B7 !important;
  transition: color 0.2s ease !important;
}

.footer-bottom-links a:hover {
  color: #FF9E66 !important;
  text-decoration: underline !important;
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n" + footer_clean_css)

print("Updated style.css with clean, high-contrast dark footer styles.")
