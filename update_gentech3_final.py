import os
import zipfile

print("Updating GenTech 3 project with the approved Live Card Builder design...")

# 1. Copy the updated code from gentech3-lab to gentech3-app
os.system("cp /Users/ramay/gentech3-lab/assets/css/style.css /Users/ramay/gentech3-app/assets/css/style.css")
os.system("cp /Users/ramay/gentech3-lab/assets/js/app.js /Users/ramay/gentech3-app/assets/js/app.js")
os.system("cp /Users/ramay/gentech3-lab/assets/js/scene3d.js /Users/ramay/gentech3-app/assets/js/scene3d.js")
os.system("cp /Users/ramay/gentech3-lab/index.html /Users/ramay/gentech3-app/index.html")

# 2. Update the WordPress theme in /Users/ramay/gentech3-wp/gentech3-theme/
wp_theme_dir = '/Users/ramay/gentech3-wp/gentech3-theme'
os.makedirs(f'{wp_theme_dir}/assets/css', exist_ok=True)
os.makedirs(f'{wp_theme_dir}/assets/js', exist_ok=True)
os.makedirs(f'{wp_theme_dir}/assets/images', exist_ok=True)

os.system(f"cp /Users/ramay/gentech3-app/assets/css/style.css {wp_theme_dir}/assets/css/style.css")
os.system(f"cp /Users/ramay/gentech3-app/assets/js/* {wp_theme_dir}/assets/js/")
os.system(f"cp /Users/ramay/gentech3-app/assets/images/* {wp_theme_dir}/assets/images/")

with open('/Users/ramay/gentech3-app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

header_html = html.split('<main id="overview">')[0]
main_body = '<main id="overview">' + html.split('<main id="overview">')[1].split('</main>')[0] + '</main>'
footer_html = '<footer class="footer-serene">' + html.split('<footer class="footer-serene">')[1]

header_php = """<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<header class="main-header">
    <div class="container">
        <nav class="main-nav">
            <a href="<?php echo esc_url(home_url('/')); ?>" class="nav-brand">
                <div class="nav-brand-dot"></div>
                <span><?php bloginfo('name'); ?></span>
            </a>
            <div class="nav-links">
                <a href="#overview" class="nav-link">Overview</a>
                <a href="#configurator" class="nav-link">3D Card Builder</a>
                <a href="#transit" class="nav-link">Transit Matrix</a>
                <a href="#ecosystem" class="nav-link">Ecosystem</a>
                <a href="#weight" class="nav-link">Weight Specs</a>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem;">
                <a href="#inquire" class="btn-primary" style="padding: 0.55rem 1.4rem; font-size: 0.82rem;">
                    <span>Inquire Fleet</span>
                </a>
            </div>
        </nav>
    </div>
</header>
"""
with open(f'{wp_theme_dir}/header.php', 'w', encoding='utf-8') as f:
    f.write(header_php)

footer_php = footer_html.replace('</body>\n</html>', '<?php wp_footer(); ?>\n</body>\n</html>')
with open(f'{wp_theme_dir}/footer.php', 'w', encoding='utf-8') as f:
    f.write(footer_php)

with open(f'{wp_theme_dir}/front-page.php', 'w', encoding='utf-8') as f:
    f.write("<?php get_header(); ?>\n" + main_body + "\n<?php get_footer(); ?>")
with open(f'{wp_theme_dir}/index.php', 'w', encoding='utf-8') as f:
    f.write("<?php get_header(); ?>\n" + main_body + "\n<?php get_footer(); ?>")

# 3. Create fresh ZIP
zip_path = '/Users/ramay/gentech3-wp/gentech3-modern-theme.zip'
if os.path.exists(zip_path):
    os.remove(zip_path)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(wp_theme_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(wp_theme_dir))
            zipf.write(file_path, arcname)

# 4. Copy to live WordPress instance
os.system(f"cp -r {wp_theme_dir}/* /Users/ramay/gentech-wp-instance/wp-content/themes/gentech3-theme/")

print(f"GenTech 3 updated and WordPress ZIP rebuilt: {zip_path} ({os.path.getsize(zip_path)/(1024*1024):.2f} MB)")
