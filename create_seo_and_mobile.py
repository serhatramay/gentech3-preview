import os

base_dir = "/Users/ramay/gentech3-app"

# 1. Generate sitemap.xml
pages = [
    ("", "1.0", "daily"),
    ("about.html", "0.9", "weekly"),
    ("chairman.html", "0.9", "weekly"),
    ("group-canada.html", "0.8", "monthly"),
    ("group-uae.html", "0.8", "monthly"),
    ("group-africa.html", "0.9", "weekly"),
    ("solutions-cards.html", "0.8", "weekly"),
    ("solutions-payments.html", "0.8", "weekly"),
    ("solutions-mobility.html", "0.9", "weekly"),
    ("solutions-telecom.html", "0.8", "weekly"),
    ("solutions-infrastructure.html", "0.8", "weekly"),
    ("solutions-capital.html", "0.8", "weekly"),
    ("africa-national-mobility-program.html", "0.95", "daily"),
    ("projects.html", "0.8", "weekly"),
    ("news.html", "0.8", "daily"),
    ("contact.html", "0.9", "monthly"),
    ("privacy.html", "0.5", "monthly"),
    ("terms.html", "0.5", "monthly"),
    ("legal.html", "0.5", "monthly"),
    ("compliance.html", "0.5", "monthly"),
]

sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
for page, priority, changefreq in pages:
    url = f"https://gentech.ae/{page}"
    sitemap_xml += f"""  <url>
    <loc>{url}</loc>
    <lastmod>2026-08-31</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>
"""
sitemap_xml += "</urlset>\n"

with open(os.path.join(base_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print("Created sitemap.xml")

# 2. Generate robots.txt
robots_txt = """User-agent: *
Allow: /

Sitemap: https://gentech.ae/sitemap.xml
"""
with open(os.path.join(base_dir, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)
print("Created robots.txt")

# 3. Generate 404.html
from build_all_gentech_group import get_header, get_footer

four_oh_four = get_header(title="404 Page Not Found — GENTECH GROUP", desc="The requested page could not be located on GENTECH GROUP.", active_nav="")
four_oh_four += """
<section class="section-spacing" style="padding-top: 160px; min-height: 70vh; display: flex; align-items: center;">
    <div class="container" style="text-align: center; max-width: 680px; margin: 0 auto;">
        <span class="calm-tag">404 // NOT FOUND</span>
        <h1 class="serif-title gradient-text" style="font-size: clamp(3rem, 7vw, 5.5rem); margin: 1rem 0;">404</h1>
        <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">Page Not Located</h2>
        <p style="font-size: 1.05rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 2rem;">
            The URL you requested does not exist or has been restructured under the new GENTECH GROUP corporate platform. Please navigate using our main directory below.
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="index.html" class="btn-primary">
                <span>Return to Homepage</span>
            </a>
            <a href="contact.html" class="btn-secondary">
                <span>Contact Corporate Office</span>
            </a>
        </div>
    </div>
</section>
""" + get_footer()

with open(os.path.join(base_dir, "404.html"), "w", encoding="utf-8") as f:
    f.write(four_oh_four)
print("Created 404.html")

