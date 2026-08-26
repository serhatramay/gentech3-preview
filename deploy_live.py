#!/usr/bin/env python3
import ftplib, os, sys

HOST = '178.210.173.34'
USER = 'gentech1'
PWD = 'PAnda1881'
REMOTE_BASE = '/gentech.ae/wwwroot'
LOCAL_BASE = '/Users/ramay/gentech3-app'

def deploy():
    print(f"Connecting to FTP {HOST}...")
    ftp = ftplib.FTP(HOST, timeout=30)
    ftp.login(USER, PWD)
    print("✓ FTP Login successful!")

    # Ensure remote dirs exist
    for sub in ['', '/assets', '/assets/css', '/assets/js', '/assets/images']:
        try:
            ftp.mkd(f"{REMOTE_BASE}{sub}")
        except Exception:
            pass

    # Files to sync
    html_files = [f for f in os.listdir(LOCAL_BASE) if f.endswith('.html')]
    for hf in html_files:
        lp = os.path.join(LOCAL_BASE, hf)
        ftp.cwd(REMOTE_BASE)
        with open(lp, 'rb') as f:
            ftp.storbinary(f"STOR {hf}", f)
        print(f"✓ Uploaded {hf}")

    # Sync CSS
    css_dir = os.path.join(LOCAL_BASE, 'assets', 'css')
    if os.path.exists(css_dir):
        ftp.cwd(f"{REMOTE_BASE}/assets/css")
        for cf in os.listdir(css_dir):
            if cf.endswith('.css'):
                with open(os.path.join(css_dir, cf), 'rb') as f:
                    ftp.storbinary(f"STOR {cf}", f)
                print(f"✓ Uploaded assets/css/{cf}")

    # Sync JS
    js_dir = os.path.join(LOCAL_BASE, 'assets', 'js')
    if os.path.exists(js_dir):
        ftp.cwd(f"{REMOTE_BASE}/assets/js")
        for jf in os.listdir(js_dir):
            if jf.endswith('.js'):
                with open(os.path.join(js_dir, jf), 'rb') as f:
                    ftp.storbinary(f"STOR {jf}", f)
                print(f"✓ Uploaded assets/js/{jf}")

    ftp.quit()
    print("🚀 Deployment to gentech.ae completed successfully!")

if __name__ == '__main__':
    deploy()
