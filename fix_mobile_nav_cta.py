import re

css_path = "/Users/ramay/gentech3-app/assets/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

nav_cta_responsive = """
/* ==========================================================================
   RESPONSIVE HEADER & COMPACT MOBILE NAV-CTA BUTTON
   ========================================================================== */
.nav-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.nav-cta {
  padding: 0.55rem 1.25rem !important;
  font-size: 0.84rem !important;
  font-weight: 700 !important;
  border-radius: var(--radius-full) !important;
  white-space: nowrap !important;
  transition: all 0.2s ease !important;
}

@media (max-width: 1024px) {
  .nav-cta {
    padding: 0.45rem 1rem !important;
    font-size: 0.80rem !important;
  }
}

@media (max-width: 768px) {
  .main-nav {
    height: 68px !important;
  }
  
  .nav-brand-dot {
    width: 8px !important;
    height: 8px !important;
  }

  .brand-title {
    font-size: 1.05rem !important;
    letter-spacing: 0.05em !important;
  }

  .brand-sub {
    font-size: 0.58rem !important;
    letter-spacing: 0.1em !important;
  }

  .nav-actions {
    gap: 0.4rem !important;
  }

  .nav-cta {
    padding: 0.38rem 0.85rem !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.02em !important;
    box-shadow: 0 2px 10px rgba(235, 101, 26, 0.25) !important;
  }

  .mobile-toggle-btn {
    font-size: 1.35rem !important;
    padding: 0.3rem 0.5rem !important;
    color: var(--text-main) !important;
  }
}

@media (max-width: 420px) {
  .main-nav {
    height: 64px !important;
  }

  .brand-title {
    font-size: 0.95rem !important;
  }

  .brand-sub {
    font-size: 0.52rem !important;
  }

  .nav-cta {
    padding: 0.32rem 0.7rem !important;
    font-size: 0.70rem !important;
  }

  .mobile-toggle-btn {
    font-size: 1.25rem !important;
    padding: 0.25rem 0.4rem !important;
  }
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n" + nav_cta_responsive)

print("Appended responsive nav-cta styles to style.css.")
