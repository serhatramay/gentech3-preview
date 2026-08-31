import re

css_path = "/Users/ramay/gentech3-app/assets/css/style.css"

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Add styles for GENTECH GROUP branding, holding architecture, Africa program, and compliance
new_styles = """
/* ==========================================================================
   GENTECH GROUP — MASTER HOLDING & CORPORATE PLATFORM EXTENSIONS
   Canada • United Arab Emirates • South Africa
   ========================================================================== */

/* Top Utility Bar */
.top-utility-bar {
  background: #110B07;
  color: #E6D7CC;
  font-size: 0.76rem;
  padding: 0.45rem 0;
  border-bottom: 1px solid rgba(235, 101, 26, 0.2);
}

.utility-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.utility-left {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.utility-dot {
  width: 6px;
  height: 6px;
  background: #00E676;
  border-radius: 50%;
  display: inline-block;
  box-shadow: 0 0 6px #00E676;
}

.utility-badge {
  font-weight: 700;
  letter-spacing: 0.08em;
  color: var(--accent-hermes);
  font-family: var(--font-mono);
}

.utility-hubs {
  color: #BDB0A6;
}

.utility-right {
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.utility-link {
  color: #E6D7CC;
  transition: color 0.2s;
  font-weight: 500;
}

.utility-link:hover {
  color: var(--accent-hermes);
}

.utility-sep {
  color: rgba(255,255,255,0.2);
}

@media (max-width: 820px) {
  .top-utility-bar { display: none; }
}

/* Solutions Dropdown Menu Extended */
.solutions-menu {
  min-width: 320px;
}

.solutions-menu .dropdown-item small {
  display: block;
  font-size: 0.74rem;
  color: var(--text-dim);
  font-weight: 400;
  margin-top: 2px;
}

.dropdown-item strong {
  display: block;
  font-size: 0.88rem;
  color: var(--text-main);
}

/* Scale & Metrics Grid */
.metrics-section {
  background: #1A130E;
  color: #FAF2EB;
  padding: 4.5rem 0;
  position: relative;
  overflow: hidden;
}

.metrics-section::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: radial-gradient(circle at 50% 50%, rgba(235, 101, 26, 0.12) 0%, transparent 70%);
  pointer-events: none;
}

.metrics-grid-5 {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1.5rem;
  position: relative;
  z-index: 2;
}

@media (max-width: 1024px) {
  .metrics-grid-5 { grid-template-columns: repeat(3, 1fr); }
}

@media (max-width: 640px) {
  .metrics-grid-5 { grid-template-columns: repeat(2, 1fr); }
}

.metric-card-box {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(235, 101, 26, 0.22);
  border-radius: var(--radius-md);
  padding: 1.8rem 1.2rem;
  text-align: center;
  backdrop-filter: blur(10px);
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.metric-card-box:hover {
  transform: translateY(-5px);
  border-color: var(--accent-hermes);
  background: rgba(255, 255, 255, 0.07);
}

.metric-val {
  font-size: clamp(1.8rem, 3.5vw, 2.5rem);
  font-weight: 800;
  font-family: var(--font-mono);
  color: #FAF2EB;
  margin-bottom: 0.35rem;
  background: linear-gradient(135deg, #FFFFFF 0%, #F5A623 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.metric-lbl {
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #BDB0A6;
}

.metric-sub {
  font-size: 0.72rem;
  color: rgba(235, 101, 26, 0.9);
  margin-top: 0.3rem;
}

/* 6-Pillar Solutions Grid */
.solutions-grid-6 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

@media (max-width: 950px) {
  .solutions-grid-6 { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 600px) {
  .solutions-grid-6 { grid-template-columns: 1fr; }
}

.pillar-card {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-card);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.pillar-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 0%;
  background: var(--accent-hermes);
  transition: height 0.3s ease;
}

.pillar-card:hover {
  transform: translateY(-6px);
  border-color: var(--border-hover);
  box-shadow: var(--shadow-float);
}

.pillar-card:hover::before {
  height: 100%;
}

.pillar-num {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--accent-hermes);
  margin-bottom: 0.75rem;
}

.pillar-title {
  font-size: 1.35rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
  color: var(--text-main);
}

.pillar-desc {
  font-size: 0.92rem;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 1.4rem;
  flex-grow: 1;
}

.pillar-features {
  list-style: none;
  padding: 0;
  margin: 0 0 1.5rem 0;
  border-top: 1px solid rgba(235, 101, 26, 0.1);
  padding-top: 1rem;
}

.pillar-features li {
  font-size: 0.84rem;
  color: var(--text-dim);
  margin-bottom: 0.45rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.pillar-features li::before {
  content: '✓';
  color: var(--accent-hermes);
  font-weight: bold;
}

.pillar-link {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--accent-hermes);
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  transition: gap 0.2s;
}

.pillar-link:hover {
  gap: 0.7rem;
}

/* Flagship Africa Program Box */
.africa-flagship-section {
  background: linear-gradient(135deg, #18110B 0%, #2A1A0F 100%);
  color: #FAF2EB;
  border-radius: var(--radius-lg);
  padding: clamp(2.5rem, 5vw, 4.5rem);
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(235, 101, 26, 0.3);
  box-shadow: var(--shadow-float);
  margin: 3.5rem 0;
}

.africa-flagship-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 3rem;
  align-items: center;
}

@media (max-width: 900px) {
  .africa-flagship-grid { grid-template-columns: 1fr; }
}

.san-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(235, 101, 26, 0.18);
  border: 1px solid rgba(235, 101, 26, 0.4);
  padding: 0.4rem 1rem;
  border-radius: var(--radius-full);
  font-size: 0.78rem;
  font-weight: 700;
  color: #FF9E66;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 1.25rem;
}

.africa-stats-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin: 2rem 0;
}

@media (max-width: 600px) {
  .africa-stats-row { grid-template-columns: 1fr; }
}

.san-stat-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 1.2rem;
  border-radius: var(--radius-md);
}

.san-stat-val {
  font-size: 1.6rem;
  font-weight: 800;
  font-family: var(--font-mono);
  color: #FFB380;
}

.san-stat-lbl {
  font-size: 0.76rem;
  color: #D1C4BA;
  text-transform: uppercase;
  margin-top: 0.2rem;
}

.san-architecture-card {
  background: rgba(0, 0, 0, 0.35);
  border: 1px solid rgba(235, 101, 26, 0.35);
  border-radius: var(--radius-md);
  padding: 2rem;
}

.arch-flow-list {
  list-style: none;
  padding: 0;
  margin: 1.2rem 0 0 0;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.arch-flow-item {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  font-size: 0.86rem;
  color: #E8DDD4;
  padding: 0.6rem 0.8rem;
  background: rgba(255, 255, 255, 0.04);
  border-radius: var(--radius-sm);
  border-left: 3px solid var(--accent-hermes);
}

.arch-flow-num {
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--accent-hermes);
}

/* Global 3 Hubs Cards */
.hubs-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

@media (max-width: 900px) {
  .hubs-grid-3 { grid-template-columns: 1fr; }
}

.hub-card {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 2.2rem;
  box-shadow: var(--shadow-card);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}

.hub-card:hover {
  transform: translateY(-5px);
  border-color: var(--accent-hermes);
  box-shadow: var(--shadow-float);
}

.hub-flag-badge {
  font-size: 1.8rem;
  margin-bottom: 0.75rem;
}

.hub-name {
  font-size: 1.3rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
}

.hub-entity-title {
  font-size: 0.84rem;
  font-weight: 700;
  font-family: var(--font-mono);
  color: var(--accent-hermes);
  margin-bottom: 0.8rem;
}

.hub-role-desc {
  font-size: 0.92rem;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 1.2rem;
  flex-grow: 1;
}

.hub-meta-list {
  font-size: 0.82rem;
  color: var(--text-dim);
  border-top: 1px solid rgba(235, 101, 26, 0.1);
  padding-top: 0.9rem;
  margin-bottom: 1.2rem;
}

.hub-meta-item {
  margin-bottom: 0.35rem;
}

/* Chairman Spotlight Section */
.chairman-spotlight {
  background: #FFFFFF;
  border-radius: var(--radius-lg);
  border: 1px solid var(--border-light);
  padding: clamp(2.5rem, 5vw, 4.5rem);
  box-shadow: var(--shadow-card);
  margin: 3.5rem 0;
}

.chairman-grid {
  display: grid;
  grid-template-columns: 0.9fr 1.3fr;
  gap: 3.5rem;
  align-items: center;
}

@media (max-width: 900px) {
  .chairman-grid { grid-template-columns: 1fr; }
}

.chairman-portrait-box {
  background: linear-gradient(135deg, #FAF2EB 0%, #F3E4D6 100%);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 2.5rem 2rem;
  text-align: center;
}

.portrait-avatar-placeholder {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  background: linear-gradient(135deg, #1A130E 0%, #C0581A 100%);
  color: #FAF2EB;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.5rem;
  font-family: var(--font-serif);
  margin: 0 auto 1.5rem auto;
  box-shadow: 0 10px 25px rgba(235, 101, 26, 0.3);
  border: 3px solid #FFFFFF;
}

.chairman-name {
  font-size: 1.45rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
}

.chairman-title-label {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--accent-hermes);
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.chairman-quote {
  font-family: var(--font-serif);
  font-size: clamp(1.15rem, 2vw, 1.45rem);
  line-height: 1.6;
  color: var(--text-main);
  font-style: italic;
  margin-bottom: 1.5rem;
  position: relative;
}

.chairman-body-text {
  font-size: 0.96rem;
  color: var(--text-muted);
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

/* Footer Legal Entities */
.footer-legal-entities {
  margin-top: 3rem;
  padding-top: 2rem;
  border-top: 1px solid rgba(235, 101, 26, 0.15);
}

.entities-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

@media (max-width: 850px) {
  .entities-grid { grid-template-columns: 1fr; }
}

.entity-card {
  background: rgba(255, 255, 255, 0.6);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  padding: 1.2rem;
}

.entity-tag {
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--accent-hermes);
  letter-spacing: 0.06em;
  display: block;
  margin-bottom: 0.3rem;
}

.entity-card h5 {
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 0.35rem;
}

.entity-card p {
  font-size: 0.8rem;
  color: var(--text-dim);
  line-height: 1.5;
}

/* Hub pill */
.hub-pill {
  display: inline-block;
  background: var(--bg-card-subtle);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-full);
  padding: 0.25rem 0.75rem;
  font-size: 0.74rem;
  font-weight: 600;
  color: var(--text-main);
  margin-right: 0.4rem;
  margin-bottom: 0.4rem;
}

.footer-desc {
  font-size: 0.88rem;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 1.2rem;
}

.footer-badge-row {
  margin-top: 0.8rem;
}

.footer-contact-item {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-bottom: 0.65rem;
  line-height: 1.4;
}

.footer-contact-item strong {
  display: block;
  color: var(--text-main);
  font-weight: 600;
}

/* Legal and Governance Pages Layout */
.legal-container {
  max-width: 900px;
  margin: 0 auto;
  background: #FFFFFF;
  border-radius: var(--radius-lg);
  border: 1px solid var(--border-light);
  padding: clamp(2rem, 4vw, 4rem);
  box-shadow: var(--shadow-card);
}

.legal-section-block {
  margin-bottom: 2.5rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid rgba(235, 101, 26, 0.1);
}

.legal-section-block:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.legal-section-block h2, .legal-section-block h3 {
  margin-bottom: 0.8rem;
}

.legal-section-block p, .legal-section-block li {
  font-size: 0.96rem;
  color: var(--text-muted);
  line-height: 1.7;
  margin-bottom: 0.8rem;
}

.legal-section-block ul {
  padding-left: 1.4rem;
  margin-bottom: 1rem;
}

.legal-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5rem 0;
  font-size: 0.88rem;
}

.legal-table th, .legal-table td {
  padding: 0.8rem 1rem;
  border: 1px solid var(--border-light);
  text-align: left;
}

.legal-table th {
  background: var(--bg-card-subtle);
  font-weight: 700;
}
"""

if "GENTECH GROUP — MASTER HOLDING" not in css:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(new_styles)
    print("Extended style.css with GENTECH GROUP Master Holding extensions.")
else:
    print("style.css already contains GENTECH GROUP extensions.")
