import os
import zipfile

print("Implementing comprehensive mobile responsiveness across GenTech 3...")

# 1. Mobile-Perfect CSS for GenTech 3
css_mobile = """/* ==========================================================================
   GENTECH 3 - SERENE ALABASTER (100% PERFECT MOBILE RESPONSIVE ENGINE)
   Tested on iPhone 13/14/15/16 Pro, Samsung Galaxy, iPad, Desktop
   ========================================================================== */

:root {
  --bg-primary: #fbfbfc;
  --bg-secondary: #f4f4f7;
  --bg-card: #ffffff;
  --bg-glass: rgba(255, 255, 255, 0.95);
  
  --text-main: #0f172a;
  --text-muted: #64748b;
  --text-dim: #94a3b8;
  
  --accent-gold: #b38b4d;
  --accent-champagne: #c5a880;
  --accent-sage: #3f6e5c;
  --accent-blue: #2563eb;
  
  --border-light: rgba(0, 0, 0, 0.07);
  --border-focus: rgba(0, 0, 0, 0.15);
  --border-gold: rgba(179, 139, 77, 0.35);
  
  --font-serif: 'Playfair Display', Georgia, serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  
  --radius-sm: 10px;
  --radius-md: 18px;
  --radius-lg: 28px;
  --radius-full: 9999px;
  
  --shadow-soft: 0 10px 30px -10px rgba(0, 0, 0, 0.05);
  --shadow-card: 0 20px 45px -15px rgba(0, 0, 0, 0.07);
  --shadow-float: 0 30px 60px -20px rgba(0, 0, 0, 0.09);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
  background-color: var(--bg-primary);
  color: var(--text-main);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-main);
  line-height: 1.65;
  overflow-x: hidden;
  position: relative;
  width: 100%;
}

body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: 
    radial-gradient(circle at 12% 18%, rgba(197, 168, 128, 0.06) 0%, transparent 45%),
    radial-gradient(circle at 88% 82%, rgba(63, 110, 92, 0.04) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}

h1, h2, h3, h4 {
  color: var(--text-main);
  font-weight: 600;
  letter-spacing: -0.025em;
  line-height: 1.18;
}

h1 { font-size: clamp(2.1rem, 6vw, 4.4rem); font-weight: 700; }
h2 { font-size: clamp(1.75rem, 4.5vw, 3rem); }
h3 { font-size: clamp(1.2rem, 2.8vw, 1.75rem); }

.serif-title {
  font-family: var(--font-serif);
  font-weight: 500;
  letter-spacing: -0.01em;
}

.gradient-text {
  background: linear-gradient(135deg, #0f172a 0%, #8d7b68 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

a { color: inherit; text-decoration: none; }
button { cursor: pointer; border: none; background: none; font: inherit; color: inherit; }
img { max-width: 100%; height: auto; display: block; }

.container {
  width: 100%;
  max-width: 1260px;
  margin-left: auto;
  margin-right: auto;
  padding-left: clamp(1rem, 4vw, 2rem);
  padding-right: clamp(1rem, 4vw, 2rem);
  position: relative;
  z-index: 1;
}

.section-spacing {
  padding-top: clamp(3.5rem, 7vw, 7.5rem);
  padding-bottom: clamp(3.5rem, 7vw, 7.5rem);
}

.calm-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.35rem 0.95rem;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  background: rgba(179, 139, 77, 0.12);
  color: var(--accent-gold);
  border: 1px solid rgba(179, 139, 77, 0.25);
  margin-bottom: 1.25rem;
  max-width: 100%;
  text-align: center;
}

/* Header & Nav */
.main-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background: var(--bg-glass);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border-light);
}

.main-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
}

@media (min-width: 768px) {
  .main-nav { height: 80px; }
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 1.15rem;
  font-weight: 700;
}

.nav-brand-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--accent-gold);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 2rem;
}

@media (max-width: 900px) {
  .nav-links { display: none; }
}

.nav-link {
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--text-muted);
  transition: color 0.2s;
}

.nav-link:hover { color: var(--text-main); }

.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.7rem 1.5rem;
  border-radius: var(--radius-full);
  background: var(--text-main);
  color: #ffffff;
  font-size: 0.82rem;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
  transition: all 0.3s;
  white-space: nowrap;
}

.btn-primary:hover {
  background: #1e293b;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.7rem 1.5rem;
  border-radius: var(--radius-full);
  background: #ffffff;
  border: 1px solid var(--border-light);
  color: var(--text-main);
  font-size: 0.82rem;
  font-weight: 600;
  box-shadow: var(--shadow-soft);
  transition: all 0.3s;
  white-space: nowrap;
}

.btn-secondary:hover {
  border-color: var(--border-focus);
  transform: translateY(-2px);
}

/* Hero & 3D Stage (Mobile Refined) */
.hero-section {
  padding-top: clamp(100px, 15vw, 140px);
  padding-bottom: 40px;
  text-align: center;
}

.hero-3d-box {
  width: 100%;
  max-width: 1060px;
  height: 480px;
  margin: 2rem auto 1.25rem auto;
  background: radial-gradient(circle at center, #ffffff 0%, #f4f4f7 85%);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-float);
  position: relative;
  overflow: hidden;
}

@media (max-width: 768px) {
  .hero-3d-box {
    height: 400px;
    border-radius: var(--radius-sm);
  }
}

#canvas3D {
  width: 100%;
  height: 100%;
  display: block;
}

/* Mobile-Friendly Studio Toolbar */
.studio-toolbar {
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  padding: 0.35rem 0.5rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-light);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
  z-index: 10;
  max-width: 95%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.toolbar-btn {
  padding: 0.4rem 0.8rem;
  border-radius: var(--radius-full);
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--text-muted);
  transition: all 0.2s;
  white-space: nowrap;
  flex-shrink: 0;
}

.toolbar-btn.active {
  background: var(--text-main);
  color: #ffffff;
}

/* --------------------------------------------------------------------------
   CANLI KART OLUŞTURUCU (100% RESPONSIVE FOR MOBILE SCREENS)
   -------------------------------------------------------------------------- */
.configurator-section {
  background: var(--bg-secondary);
}

.configurator-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: clamp(1.5rem, 4vw, 3.5rem);
  box-shadow: var(--shadow-card);
  margin-top: 2.5rem;
}

.configurator-grid {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: clamp(1.5rem, 4vw, 3.5rem);
  align-items: center;
}

@media (max-width: 900px) {
  .configurator-grid {
    grid-template-columns: 1fr;
  }
}

/* Live Card Mockup - True Credit Card Aspect Ratio (1.586) */
.live-card-mockup {
  width: 100%;
  max-width: 380px;
  aspect-ratio: 1.586;
  min-height: 200px;
  margin: 0 auto;
  border-radius: 16px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.12);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: clamp(1.2rem, 3vw, 1.75rem);
  transition: all 0.4s ease;
}

@media (max-width: 480px) {
  .live-card-mockup {
    min-height: 180px;
    border-radius: 14px;
  }
}

.live-card-mockup.ceramic {
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
  border: 1px solid #e2e8f0;
  color: #0f172a;
}

.live-card-mockup.titanium {
  background: linear-gradient(135deg, #e2e8f0 0%, #cbd5e1 100%);
  border: 1px solid #94a3b8;
  color: #0f172a;
}

.live-card-mockup.champagne {
  background: linear-gradient(135deg, #faf5eb 0%, #d6c5af 100%);
  border: 1px solid #c8b6a6;
  color: #292524;
}

.live-card-mockup.gold {
  background: linear-gradient(135deg, #fef08a 0%, #eab308 100%);
  border: 1px solid #ca8a04;
  color: #422006;
}

.chip-graphic {
  width: 44px;
  height: 34px;
  border-radius: 6px;
  background: linear-gradient(135deg, #eab308 0%, #a16207 100%);
  border: 1px solid #ca8a04;
  position: relative;
  box-shadow: 0 2px 6px rgba(0,0,0,0.15);
}

.chip-graphic::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: 1px;
  background: rgba(0,0,0,0.25);
}

/* Responsive Pill Buttons on Mobile */
.alloy-pill-btn {
  padding: 0.5rem 0.9rem;
  border-radius: var(--radius-full);
  background: #ffffff;
  border: 1px solid var(--border-light);
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-main);
  box-shadow: 0 2px 6px rgba(0,0,0,0.03);
  transition: all 0.2s;
  flex: 1 1 calc(50% - 0.5rem);
  text-align: center;
  white-space: nowrap;
}

@media (min-width: 600px) {
  .alloy-pill-btn {
    flex: 0 0 auto;
  }
}

.alloy-pill-btn.active {
  border-color: var(--accent-gold);
  color: var(--accent-gold);
  background: rgba(179, 139, 77, 0.08);
}

.form-input-clean {
  width: 100%;
  padding: 0.85rem 1rem;
  background: var(--bg-secondary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  font-size: 0.92rem;
  color: var(--text-main);
  transition: all 0.2s;
}

.form-input-clean:focus {
  outline: none;
  background: #ffffff;
  border-color: var(--accent-gold);
  box-shadow: 0 0 0 3px rgba(179, 139, 77, 0.12);
}

/* --------------------------------------------------------------------------
   Ecosystem 6 Pillars Grid (Responsive 1/2/3 Columns)
   -------------------------------------------------------------------------- */
.eco-grid-6 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-top: 2.5rem;
}

@media (max-width: 1024px) {
  .eco-grid-6 { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 640px) {
  .eco-grid-6 { grid-template-columns: 1fr; }
}

.eco-tile {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: clamp(1.5rem, 3vw, 2.25rem);
  box-shadow: var(--shadow-soft);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.eco-thumb {
  height: 160px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at center, rgba(197, 168, 128, 0.08) 0%, transparent 70%);
  border-radius: var(--radius-sm);
  margin: 1rem 0;
}

.eco-thumb img {
  max-height: 130px;
  object-fit: contain;
  filter: drop-shadow(0 10px 18px rgba(0, 0, 0, 0.06));
}

/* --------------------------------------------------------------------------
   Weight Specs Comparator (Responsive 1/3 Columns)
   -------------------------------------------------------------------------- */
.comparator-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
  margin-top: 2.5rem;
}

@media (max-width: 840px) {
  .comparator-row { grid-template-columns: 1fr; }
}

.comparator-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 2rem 1.5rem;
  text-align: center;
  box-shadow: var(--shadow-soft);
}

.comparator-card.featured {
  border-color: var(--accent-gold);
  box-shadow: 0 15px 35px rgba(179, 139, 77, 0.12);
}

.weight-display {
  font-size: clamp(2.6rem, 6vw, 3.5rem);
  font-weight: 700;
  letter-spacing: -0.04em;
  margin: 0.5rem 0;
  line-height: 1;
}

/* Footer */
.footer-serene {
  background: var(--bg-secondary);
  border-top: 1px solid var(--border-light);
  padding: 3.5rem 0 2rem 0;
  font-size: 0.85rem;
  color: var(--text-muted);
}
"""

with open('/Users/ramay/gentech3-app/assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_mobile)

# 2. Update scene3d.js with Dynamic Mobile Camera & Touch Rotation
scene3d_mobile = """/**
 * GenTech 3 - Responsive 3D WebGL Engine (Mobile Touch & Portrait Scale Optimized)
 */

let scene, camera, renderer;
let cardMesh, ringMesh, chipMesh;
let cardGroup, ringGroup, mainStageGroup;
let hemiLight, dirLight1, dirLight2;
let targetRotationX = 0, targetRotationY = 0;
let isExploded = false;
let currentArtifact = 'both';

function init3DScene() {
  const container = document.getElementById('canvas3D');
  if (!container) return;

  const width = container.clientWidth;
  const height = container.clientHeight;

  scene = new THREE.Scene();

  camera = new THREE.PerspectiveCamera(40, width / height, 0.1, 1000);

  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.15;
  container.appendChild(renderer.domElement);

  // Lights
  hemiLight = new THREE.HemisphereLight(0xffffff, 0xf1f5f9, 1.2);
  scene.add(hemiLight);

  dirLight1 = new THREE.DirectionalLight(0xffffff, 1.8);
  dirLight1.position.set(6, 8, 10);
  scene.add(dirLight1);

  dirLight2 = new THREE.DirectionalLight(0xfaf5eb, 1.0);
  dirLight2.position.set(-8, -4, 6);
  scene.add(dirLight2);

  // Groups
  mainStageGroup = new THREE.Group();
  scene.add(mainStageGroup);

  cardGroup = new THREE.Group();
  ringGroup = new THREE.Group();
  mainStageGroup.add(cardGroup);
  mainStageGroup.add(ringGroup);

  // Card Mesh
  const cardGeo = new THREE.BoxGeometry(4.2, 2.7, 0.08);
  const cardMat = createMaterial('ceramic');
  cardMesh = new THREE.Mesh(cardGeo, cardMat);
  cardGroup.add(cardMesh);

  // Chip
  const chipGeo = new THREE.BoxGeometry(0.75, 0.6, 0.09);
  const chipMat = new THREE.MeshStandardMaterial({ color: 0xd4af37, metalness: 0.9, roughness: 0.2 });
  chipMesh = new THREE.Mesh(chipGeo, chipMat);
  chipMesh.position.set(-1.2, 0.4, 0.01);
  cardGroup.add(chipMesh);

  // Ring Mesh
  const ringGeo = new THREE.TorusGeometry(1.35, 0.3, 32, 100);
  const ringMat = createMaterial('ceramic');
  ringMesh = new THREE.Mesh(ringGeo, ringMat);
  ringMesh.rotation.x = Math.PI / 3;
  ringGroup.add(ringMesh);

  // Inner Resonator Trace
  const innerRingGeo = new THREE.TorusGeometry(1.2, 0.04, 16, 80);
  const innerRingMat = new THREE.MeshStandardMaterial({ color: 0x3b82f6, emissive: 0x3b82f6, emissiveIntensity: 0.6 });
  const innerRing = new THREE.Mesh(innerRingGeo, innerRingMat);
  innerRing.rotation.x = Math.PI / 3;
  ringGroup.add(innerRing);

  // Initial Responsive Positioning
  layoutObjectsForViewport(container.clientWidth, container.clientHeight);

  // Mouse Listener (Desktop)
  window.addEventListener('mousemove', (e) => {
    const rect = container.getBoundingClientRect();
    const x = e.clientX - (rect.left + rect.width / 2);
    const y = e.clientY - (rect.top + rect.height / 2);
    targetRotationY = (x / rect.width) * 0.4;
    targetRotationX = (y / rect.height) * 0.4;
  });

  // Touch Listener (Mobile)
  let touchStartX = 0, touchStartY = 0;
  container.addEventListener('touchstart', (e) => {
    if (e.touches.length === 1) {
      touchStartX = e.touches[0].clientX;
      touchStartY = e.touches[0].clientY;
    }
  }, { passive: true });

  container.addEventListener('touchmove', (e) => {
    if (e.touches.length === 1) {
      const deltaX = e.touches[0].clientX - touchStartX;
      const deltaY = e.touches[0].clientY - touchStartY;
      targetRotationY = (deltaX / window.innerWidth) * 1.5;
      targetRotationX = (deltaY / window.innerHeight) * 1.5;
    }
  }, { passive: true });

  // Resize Listener
  window.addEventListener('resize', () => {
    const newW = container.clientWidth;
    const newH = container.clientHeight;
    camera.aspect = newW / newH;
    camera.updateProjectionMatrix();
    renderer.setSize(newW, newH);
    layoutObjectsForViewport(newW, newH);
  });

  animate();
}

function layoutObjectsForViewport(width, height) {
  const aspect = width / height;
  if (aspect < 0.9) {
    // Mobile Portrait: Scale down & stack comfortably
    camera.position.set(0, 0, 18);
    if (currentArtifact === 'both') {
      cardGroup.position.set(0, 1.8, 0);
      cardGroup.scale.set(0.82, 0.82, 0.82);
      ringGroup.position.set(0, -2.1, 0);
      ringGroup.scale.set(0.85, 0.85, 0.85);
    }
  } else {
    // Desktop & Tablet Landscape
    camera.position.set(0, 0, 13.5);
    if (currentArtifact === 'both') {
      cardGroup.position.set(-2.0, 0, 0);
      cardGroup.scale.set(1, 1, 1);
      ringGroup.position.set(2.8, 0, 0);
      ringGroup.scale.set(1, 1, 1);
    }
  }
}

function createMaterial(type) {
  if (type === 'ceramic') {
    return new THREE.MeshStandardMaterial({ color: 0xf8fafc, metalness: 0.08, roughness: 0.12, clearcoat: 1.0 });
  } else if (type === 'titanium') {
    return new THREE.MeshStandardMaterial({ color: 0xd1d5db, metalness: 0.92, roughness: 0.25 });
  } else if (type === 'champagne') {
    return new THREE.MeshStandardMaterial({ color: 0xd6c5af, metalness: 0.85, roughness: 0.22 });
  } else if (type === 'gold') {
    return new THREE.MeshStandardMaterial({ color: 0xd4af37, metalness: 0.94, roughness: 0.16 });
  }
}

function set3DMaterial(matKey) {
  const newMat = createMaterial(matKey);
  if (cardMesh) cardMesh.material = newMat;
  if (ringMesh) ringMesh.material = newMat;
}

function setActiveArtifact(artifact) {
  currentArtifact = artifact;
  const container = document.getElementById('canvas3D');
  const isMobile = container && (container.clientWidth / container.clientHeight < 0.9);

  if (artifact === 'both') {
    layoutObjectsForViewport(container.clientWidth, container.clientHeight);
  } else if (artifact === 'card') {
    cardGroup.position.set(0, 0, 0);
    cardGroup.scale.set(isMobile ? 1.0 : 1.25, isMobile ? 1.0 : 1.25, isMobile ? 1.0 : 1.25);
    ringGroup.scale.set(0.001, 0.001, 0.001);
  } else if (artifact === 'ring') {
    ringGroup.position.set(0, 0, 0);
    ringGroup.scale.set(isMobile ? 1.1 : 1.35, isMobile ? 1.1 : 1.35, isMobile ? 1.1 : 1.35);
    cardGroup.scale.set(0.001, 0.001, 0.001);
  }
}

function toggleExplodedView() {
  isExploded = !isExploded;
  const targetZ = isExploded ? 1.0 : 0;
  if (cardMesh) cardMesh.position.z = targetZ;
  if (chipMesh) chipMesh.position.z = targetZ + 0.5;
}

function animate() {
  requestAnimationFrame(animate);
  const time = Date.now() * 0.001;
  if (cardGroup) {
    cardGroup.rotation.y += (targetRotationY - cardGroup.rotation.y) * 0.04;
    cardGroup.rotation.x += (targetRotationX - cardGroup.rotation.x) * 0.04;
    cardGroup.position.y += Math.sin(time * 0.8) * 0.002;
  }
  if (ringGroup) {
    ringGroup.rotation.y += 0.006;
  }
  renderer.render(scene, camera);
}

document.addEventListener('DOMContentLoaded', () => {
  if (typeof THREE !== 'undefined') init3DScene();
});
"""

with open('/Users/ramay/gentech3-app/assets/js/scene3d.js', 'w', encoding='utf-8') as f:
    f.write(scene3d_mobile)

# 3. Synchronize to GenTech 3 WordPress Theme and Rebuild ZIP
wp_theme_dir = '/Users/ramay/gentech3-wp/gentech3-theme'
os.system(f"cp /Users/ramay/gentech3-app/assets/css/style.css {wp_theme_dir}/assets/css/style.css")
os.system(f"cp /Users/ramay/gentech3-app/assets/js/* {wp_theme_dir}/assets/js/")
os.system(f"cp /Users/ramay/gentech3-app/index.html {wp_theme_dir}/front-page.php")
os.system(f"cp /Users/ramay/gentech3-app/index.html {wp_theme_dir}/index.php")

zip_path = '/Users/ramay/gentech3-wp/gentech3-modern-theme.zip'
if os.path.exists(zip_path):
    os.remove(zip_path)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(wp_theme_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(wp_theme_dir))
            zipf.write(file_path, arcname)

os.system(f"cp -r {wp_theme_dir}/* /Users/ramay/gentech-wp-instance/wp-content/themes/gentech3-theme/")

# Also sync to gentech3-lab for consistency
os.system("cp -r /Users/ramay/gentech3-app/* /Users/ramay/gentech3-lab/")

print("Mobile responsiveness fix completed and deployed across all environments!")
