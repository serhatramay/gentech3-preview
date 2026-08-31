import re

css_path = "/Users/ramay/gentech3-app/assets/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

metrics_mobile_fix = """
/* ==========================================================================
   PERFECT MOBILE RESPONSIVE METRICS GRID (ZERO OVERFLOW / COMPACT TILES)
   ========================================================================== */
@media (max-width: 768px) {
  .metrics-section {
    padding: 2.5rem 0 !important;
  }

  .metrics-grid-5 {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 0.75rem !important;
  }

  .metric-card-box {
    padding: 1rem 0.6rem !important;
    border-radius: 12px !important;
  }

  /* Make the 5th odd card centered nicely spanning full width */
  .metrics-grid-5 .metric-card-box:last-child {
    grid-column: 1 / -1 !important;
    max-width: 340px !important;
    margin: 0 auto !important;
    width: 100% !important;
  }

  .metric-val {
    font-size: 1.45rem !important;
    margin-bottom: 0.2rem !important;
    line-height: 1.1 !important;
  }

  .metric-lbl {
    font-size: 0.68rem !important;
    letter-spacing: 0.04em !important;
    line-height: 1.3 !important;
  }

  .metric-sub {
    font-size: 0.64rem !important;
    margin-top: 0.2rem !important;
    line-height: 1.25 !important;
  }
}

@media (max-width: 380px) {
  .metrics-grid-5 {
    gap: 0.5rem !important;
  }

  .metric-card-box {
    padding: 0.85rem 0.4rem !important;
  }

  .metric-val {
    font-size: 1.25rem !important;
  }

  .metric-lbl {
    font-size: 0.62rem !important;
  }
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n" + metrics_mobile_fix)

print("Updated style.css with mobile metrics fix.")
