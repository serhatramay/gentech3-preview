#!/usr/bin/env python3
"""
GENTECH GROUP — Production Live Deployment Engine (gentech.ae)
Transfers all verified HTML files, sitemap, robots, CSS, JS, and image assets.
"""

import ftplib, os, sys

HOST = '178.210.173.34'
USER = 'gentech1'
PWD = 'PAnda1881'
REMOTE_BASE = '/gentech.ae/wwwroot'
LOCAL_BASE = '/Users/ramay/gentech3-app'

def deploy():
    print(f"Connecting to live FTP server {HOST}...")
    ftp = ftplib.FTP(HOST, timeout=45)
    ftp.login(USER, PWD)
    print("✓ FTP Authentication Successful!")

    # 1. Ensure remote directories exist
    remote_dirs = ['', '/assets', '/assets/css', '/assets/js', '/assets/images']
    for sub in remote_dirs:
        try:
            ftp.mkd(f"{REMOTE_BASE}{sub}")
        except Exception:
            pass

    # 2. Upload Root Files (HTML, XML, TXT)
    root_files = [f for f in os.listdir(LOCAL_BASE) if f.endswith(('.html', '.xml', '.txt', '.ico'))]
    ftp.cwd(REMOTE_BASE)
    print(f"\n--- Uploading {len(root_files)} Root Files (HTML, Sitemap, Robots) ---")
    for rf in sorted(root_files):
        lp = os.path.join(LOCAL_BASE, rf)
        with open(lp, 'rb') as f:
            ftp.storbinary(f"STOR {rf}", f)
        print(f"✓ Uploaded {rf}")

    # 3. Sync CSS Assets
    css_dir = os.path.join(LOCAL_BASE, 'assets', 'css')
    if os.path.exists(css_dir):
        ftp.cwd(f"{REMOTE_BASE}/assets/css")
        css_files = [f for f in os.listdir(css_dir) if f.endswith('.css')]
        print(f"\n--- Uploading {len(css_files)} CSS Stylesheets ---")
        for cf in css_files:
            with open(os.path.join(css_dir, cf), 'rb') as f:
                ftp.storbinary(f"STOR {cf}", f)
            print(f"✓ Uploaded assets/css/{cf}")

    # 4. Sync JS Assets
    js_dir = os.path.join(LOCAL_BASE, 'assets', 'js')
    if os.path.exists(js_dir):
        ftp.cwd(f"{REMOTE_BASE}/assets/js")
        js_files = [f for f in os.listdir(js_dir) if f.endswith('.js')]
        print(f"\n--- Uploading {len(js_files)} JS Scripts ---")
        for jf in js_files:
            with open(os.path.join(js_dir, jf), 'rb') as f:
                ftp.storbinary(f"STOR {jf}", f)
            print(f"✓ Uploaded assets/js/{jf}")

    # 5. Sync Images (webp, png, jpg)
    img_dir = os.path.join(LOCAL_BASE, 'assets', 'images')
    if os.path.exists(img_dir):
        ftp.cwd(f"{REMOTE_BASE}/assets/images")
        img_files = [f for f in os.listdir(img_dir) if f.endswith(('.webp', '.png', '.jpg', '.svg', '.jpeg'))]
        print(f"\n--- Verifying/Uploading {len(img_files)} Image Assets ---")
        # Get existing remote files to avoid re-uploading unchanged heavy images
        try:
            remote_existing = set(ftp.nlst())
        except Exception:
            remote_existing = set()
        
        uploaded_count = 0
        for im in img_files:
            if im not in remote_existing:
                with open(os.path.join(img_dir, im), 'rb') as f:
                    ftp.storbinary(f"STOR {im}", f)
                uploaded_count += 1
                if uploaded_count % 10 == 0:
                    print(f"  ...uploaded {uploaded_count} new images")
        print(f"✓ Images synchronized! ({uploaded_count} new uploaded, {len(img_files) - uploaded_count} already up-to-date)")

    ftp.quit()
    print("\n" + "="*60)
    print("🚀 GENTECH GROUP LIVE PRODUCTION DEPLOYMENT FINISHED!")
    print("🌐 Live URL: https://gentech.ae/")
    print("="*60)

if __name__ == '__main__':
    deploy()
