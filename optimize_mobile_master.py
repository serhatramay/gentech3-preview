import re

css_path = "/Users/ramay/gentech3-app/assets/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

mobile_master_patch = """
/* ==========================================================================
   COMPREHENSIVE MOBILE REFINEMENT & RESPONSIVE POLISH (AUDIT 2026)
   ========================================================================== */

/* 1. Form Inputs & Grids on Mobile */
@media (max-width: 640px) {
  #gentechInquiryForm div[style*="grid-template-columns: 1fr 1fr"],
  #gentechInquiryForm .form-row-2col {
    grid-template-columns: 1fr !important;
    gap: 1rem !important;
  }

  #gentechInquiryForm {
    padding: 1.5rem 1rem !important;
  }
}

/* 2. Responsive Table Wrappers */
.table-responsive {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 1.25rem 0;
  border-radius: var(--radius-sm);
}

.legal-table {
  min-width: 480px;
}

@media (max-width: 600px) {
  .legal-table th, .legal-table td {
    padding: 0.6rem 0.75rem !important;
    font-size: 0.82rem !important;
  }
}

/* 3. 3D Canvas Stage Height on Mobile */
@media (max-width: 768px) {
  .hero-3d-box {
    height: 400px !important;
    max-height: 55vh !important;
  }
}

@media (max-width: 420px) {
  .hero-3d-box {
    height: 360px !important;
  }
}

/* 4. Hero CTA Buttons on Mobile */
@media (max-width: 580px) {
  .hero-cta-group {
    flex-direction: column !important;
    align-items: center !important;
    gap: 0.75rem !important;
  }

  .hero-cta-group .btn-primary,
  .hero-cta-group .btn-secondary {
    width: 100% !important;
    max-width: 320px !important;
    text-align: center !important;
    padding: 0.7rem 1.2rem !important;
    font-size: 0.88rem !important;
  }

  .hero-hubs-ticker {
    flex-direction: column !important;
    gap: 0.35rem !important;
    padding: 0.75rem 1rem !important;
    border-radius: 16px !important;
    text-align: center !important;
    width: 100% !important;
    max-width: 340px !important;
  }

  .hero-hubs-ticker span:nth-child(2),
  .hero-hubs-ticker span:nth-child(4) {
    display: none !important; /* Hide dot separators in stacked mobile mode */
  }
}

/* 5. Africa Flagship & Chairman Spotlight on Mobile */
@media (max-width: 768px) {
  .africa-flagship-section {
    padding: 1.8rem 1.2rem !important;
    margin: 2rem 0 !important;
  }

  .chairman-spotlight {
    padding: 1.8rem 1.2rem !important;
    margin: 2rem 0 !important;
  }

  .chairman-portrait-box {
    padding: 1.5rem 1rem !important;
  }

  .portrait-avatar-placeholder {
    width: 100px !important;
    height: 100px !important;
    font-size: 1.8rem !important;
    margin-bottom: 1rem !important;
  }

  .san-architecture-card {
    padding: 1.2rem !important;
  }

  .arch-flow-item {
    font-size: 0.80rem !important;
    padding: 0.5rem 0.65rem !important;
  }
}

/* 6. Legal Container & Detail Pages on Mobile */
@media (max-width: 768px) {
  .legal-container {
    padding: 1.5rem 1.1rem !important;
  }

  .page-banner-header {
    padding-bottom: 2rem !important;
  }

  .page-banner-title {
    font-size: clamp(1.6rem, 5vw, 2.2rem) !important;
  }

  .section-spacing {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n" + mobile_master_patch)

print("Appended comprehensive mobile master patch to style.css.")
