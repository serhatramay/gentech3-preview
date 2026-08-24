import os
import zipfile

wp_dir = '/Users/ramay/gentech3-wp/gentech3-theme'
os.makedirs(f'{wp_dir}/assets/css', exist_ok=True)
os.makedirs(f'{wp_dir}/assets/js', exist_ok=True)
os.makedirs(f'{wp_dir}/assets/images', exist_ok=True)

# Copy files
os.system(f'cp /Users/ramay/gentech3-app/assets/css/style.css {wp_dir}/assets/css/style.css')
os.system(f'cp /Users/ramay/gentech3-app/assets/js/* {wp_dir}/assets/js/')
os.system(f'cp /Users/ramay/gentech3-app/assets/images/* {wp_dir}/assets/images/')

# style.css for WP
style_css = """/*
Theme Name: GenTech 3 Serene
Theme URI: https://gentech.ae/
Author: GenTech Global Innovation Hub
Author URI: https://gentech.ae/
Description: Serene Alabaster & Pure Ceramic Light Edition — Ultra-fast, SEO-optimized, next-generation FinTech theme with 3D WebGL, bespoke studio, and comprehensive hardware ecosystem.
Version: 3.5.0
Requires at least: 6.0
Tested up to: 6.7
Requires PHP: 7.4
License: GNU General Public License v2 or later
Text Domain: gentech3-serene
*/

@import url('assets/css/style.css');
"""
with open(f'{wp_dir}/style.css', 'w', encoding='utf-8') as f:
    f.write(style_css)

# functions.php
functions_php = """<?php
function gentech3_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', array('search-form', 'comment-form', 'comment-list', 'gallery', 'caption'));
}
add_action('after_setup_theme', 'gentech3_setup');

function gentech3_scripts() {
    wp_enqueue_style('gentech3-fonts-playfair', 'https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap', array(), null);
    wp_enqueue_style('gentech3-style', get_stylesheet_uri(), array(), '3.5.0');
    wp_enqueue_script('threejs', 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js', array(), null, true);
    wp_enqueue_script('gentech3-audio', get_template_directory_uri() . '/assets/js/audio.js', array(), '3.5.0', true);
    wp_enqueue_script('gentech3-scene3d', get_template_directory_uri() . '/assets/js/scene3d.js', array('threejs'), '3.5.0', true);
    wp_enqueue_script('gentech3-app', get_template_directory_uri() . '/assets/js/app.js', array('gentech3-scene3d'), '3.5.0', true);
}
add_action('wp_enqueue_scripts', 'gentech3_scripts');
"""
with open(f'{wp_dir}/functions.php', 'w', encoding='utf-8') as f:
    f.write(functions_php)

# header.php & footer.php
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
<header class="serene-header">
    <div class="container">
        <nav class="serene-nav">
            <a href="<?php echo esc_url(home_url('/')); ?>" class="serene-brand">
                <div class="brand-dot"></div>
                <div class="brand-title"><?php bloginfo('name'); ?></div>
            </a>
            <div class="serene-menu">
                <a href="#overview" class="serene-link">Overview</a>
                <a href="#ecosystem" class="serene-link">Ecosystem</a>
                <a href="#materials" class="serene-link">Materials & Weight</a>
                <a href="#studio" class="serene-link">Bespoke Studio</a>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem;">
                <button id="soundToggleBtn" style="font-size: 0.8rem; font-weight: 500; color: var(--text-muted); padding: 0.4rem 0.8rem; border-radius: var(--radius-full); background: var(--bg-secondary); border: 1px solid var(--border-light);">
                    Sound: Soft
                </button>
                <a href="#inquire" class="btn-calm-primary" style="padding: 0.55rem 1.4rem; font-size: 0.82rem;">
                    <span>Inquire Fleet</span>
                </a>
            </div>
        </nav>
    </div>
</header>
"""
with open(f'{wp_dir}/header.php', 'w', encoding='utf-8') as f:
    f.write(header_php)

footer_php = footer_html.replace('</body>\n</html>', '<?php wp_footer(); ?>\n</body>\n</html>')
with open(f'{wp_dir}/footer.php', 'w', encoding='utf-8') as f:
    f.write(footer_php)

with open(f'{wp_dir}/front-page.php', 'w', encoding='utf-8') as f:
    f.write("<?php get_header(); ?>\n" + main_body + "\n<?php get_footer(); ?>")
with open(f'{wp_dir}/index.php', 'w', encoding='utf-8') as f:
    f.write("<?php get_header(); ?>\n" + main_body + "\n<?php get_footer(); ?>")

# Make ZIP
zip_path = '/Users/ramay/gentech3-wp/gentech3-modern-theme.zip'
if os.path.exists(zip_path):
    os.remove(zip_path)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(wp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(wp_dir))
            zipf.write(file_path, arcname)

print(f"GenTech 3 WordPress theme packaged: {zip_path} ({os.path.getsize(zip_path)/(1024*1024):.2f} MB)")
