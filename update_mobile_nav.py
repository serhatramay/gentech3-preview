import re

js_path = "/Users/ramay/gentech3-app/assets/js/app.js"
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

mobile_js = """
  // Mobile Hamburger Menu Toggle
  const mobileToggle = document.getElementById('mobileMenuToggle');
  const mobileDrawer = document.getElementById('mobileNavDrawer');
  const mobileClose = document.getElementById('mobileNavClose');

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      mobileDrawer.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  }

  if (mobileClose && mobileDrawer) {
    mobileClose.addEventListener('click', () => {
      mobileDrawer.classList.remove('open');
      document.body.style.overflow = '';
    });
  }
"""

if "mobileMenuToggle" not in js:
    js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', () => {\n" + mobile_js)
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("Updated app.js with mobile drawer toggle.")
else:
    print("app.js already has mobile drawer logic.")

css_path = "/Users/ramay/gentech3-app/assets/css/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

mobile_css = """
/* Mobile Navigation Drawer */
.mobile-toggle-btn {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  color: var(--text-main);
  font-size: 1.5rem;
}

@media (max-width: 1024px) {
  .mobile-toggle-btn { display: block; }
}

.mobile-nav-drawer {
  position: fixed;
  top: 0;
  right: -100%;
  width: 85%;
  max-width: 380px;
  height: 100vh;
  background: #FFFFFF;
  box-shadow: -10px 0 30px rgba(0,0,0,0.15);
  z-index: 2000;
  transition: right 0.3s ease;
  padding: 2rem 1.5rem;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.mobile-nav-drawer.open {
  right: 0;
}

.mobile-drawer-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--border-light);
}

.mobile-drawer-close {
  font-size: 1.8rem;
  color: var(--text-muted);
  cursor: pointer;
  border: none;
  background: none;
}

.mobile-drawer-links {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.mobile-drawer-link {
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--text-main);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.mobile-drawer-link:hover {
  color: var(--accent-hermes);
}

.mobile-sublinks {
  padding-left: 1rem;
  margin-top: 0.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  border-left: 2px solid var(--border-light);
}

.mobile-sublink {
  font-size: 0.9rem;
  color: var(--text-muted);
}
"""

if "mobile-nav-drawer" not in css:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(mobile_css)
    print("Updated style.css with mobile drawer styles.")
else:
    print("style.css already has mobile drawer styles.")

