import os

print("Building GenTech 3 — Serene Alabaster & Pure Ceramic (Light, Calm, Airy Edition)...")

# 1. Light, Serene & Airy CSS
css_content = """/* ==========================================================================
   GENTECH 3 - SERENE ALABASTER & PURE CERAMIC (LIGHT, CALM & AIRY EDITION)
   Aesthetic: Bang & Olufsen / Jony Ive Pure White / Vitra / Kinfolk FinTech
   Colors: Alabaster (#FBFBFC), Cashmere, Pale Champagne, Soft Sage, Slate
   ========================================================================== */

:root {
  --bg-primary: #fbfbfc;
  --bg-secondary: #f4f4f7;
  --bg-card: #ffffff;
  --bg-card-subtle: #fafafc;
  --bg-glass: rgba(255, 255, 255, 0.85);
  
  --text-main: #111827;
  --text-muted: #64748b;
  --text-dim: #94a3b8;
  
  --accent-champagne: #c5a880;
  --accent-gold: #b38b4d;
  --accent-sage: #477a66;
  --accent-blue: #3b82f6;
  
  --border-light: rgba(0, 0, 0, 0.06);
  --border-hover: rgba(179, 139, 77, 0.3);
  --border-focus: rgba(0, 0, 0, 0.15);
  
  --font-serif: 'Playfair Display', Georgia, serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  
  --radius-sm: 12px;
  --radius-md: 20px;
  --radius-lg: 32px;
  --radius-full: 9999px;
  
  --shadow-serene: 0 20px 40px -15px rgba(0, 0, 0, 0.05), 0 0 1px 1px rgba(0, 0, 0, 0.03);
  --shadow-float: 0 30px 60px -20px rgba(0, 0, 0, 0.08);
  --shadow-hover: 0 25px 50px -12px rgba(179, 139, 77, 0.12);
  
  --transition-calm: 0.5s cubic-bezier(0.16, 1, 0.3, 1);
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
  line-height: 1.7;
  overflow-x: hidden;
  position: relative;
}

/* Soft ambient lighting gradient */
body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: 
    radial-gradient(circle at 15% 15%, rgba(197, 168, 128, 0.06) 0%, transparent 50%),
    radial-gradient(circle at 85% 85%, rgba(71, 122, 102, 0.04) 0%, transparent 55%);
  pointer-events: none;
  z-index: 0;
}

h1, h2, h3, h4 {
  color: var(--text-main);
  font-weight: 600;
  letter-spacing: -0.025em;
  line-height: 1.15;
}

h1 { font-size: clamp(2.8rem, 5.5vw, 4.8rem); font-weight: 700; }
h2 { font-size: clamp(2.2rem, 3.8vw, 3.2rem); }
h3 { font-size: clamp(1.35rem, 2.2vw, 1.85rem); }

.serif-display {
  font-family: var(--font-serif);
  font-weight: 500;
  letter-spacing: -0.01em;
}

.champagne-gradient-text {
  background: linear-gradient(135deg, #111827 0%, #8d7b68 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

a { color: inherit; text-decoration: none; transition: all var(--transition-calm); }
button { cursor: pointer; border: none; background: none; font: inherit; color: inherit; }
img { max-width: 100%; height: auto; display: block; }

.container {
  width: 100%;
  max-width: 1280px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 2rem;
  padding-right: 2rem;
  position: relative;
  z-index: 1;
}

.section-spacing {
  padding-top: clamp(6rem, 10vw, 10rem);
  padding-bottom: clamp(6rem, 10vw, 10rem);
}

.calm-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 1.1rem;
  border-radius: var(--radius-full);
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  background: rgba(197, 168, 128, 0.12);
  color: var(--accent-gold);
  border: 1px solid rgba(197, 168, 128, 0.25);
  margin-bottom: 1.5rem;
}

/* --------------------------------------------------------------------------
   Serene Navigation
   -------------------------------------------------------------------------- */
.serene-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background: var(--bg-glass);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 1px solid var(--border-light);
  transition: all var(--transition-calm);
}

.serene-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 84px;
}

.serene-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.brand-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--accent-gold);
  box-shadow: 0 0 10px rgba(179, 139, 77, 0.4);
}

.brand-title {
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.serene-menu {
  display: flex;
  align-items: center;
  gap: 2.5rem;
}

@media (max-width: 960px) {
  .serene-menu { display: none; }
}

.serene-link {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text-muted);
  transition: color 0.3s;
}

.serene-link:hover, .serene-link.active {
  color: var(--text-main);
}

.btn-calm-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.8rem 1.8rem;
  border-radius: var(--radius-full);
  background: var(--text-main);
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 600;
  transition: all var(--transition-calm);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
}

.btn-calm-primary:hover {
  background: #2d3748;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
}

.btn-calm-ghost {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.8rem 1.8rem;
  border-radius: var(--radius-full);
  background: #ffffff;
  border: 1px solid var(--border-light);
  color: var(--text-main);
  font-size: 0.85rem;
  font-weight: 600;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
  transition: all var(--transition-calm);
}

.btn-calm-ghost:hover {
  border-color: var(--border-focus);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.06);
}

/* --------------------------------------------------------------------------
   Hero Section: Airy, Soft Studio
   -------------------------------------------------------------------------- */
.serene-hero {
  padding-top: 150px;
  padding-bottom: 70px;
  text-align: center;
}

.hero-subtext {
  font-size: clamp(1.1rem, 2vw, 1.35rem);
  color: var(--text-muted);
  max-width: 640px;
  margin: 1.25rem auto 2.5rem auto;
  line-height: 1.7;
}

.hero-3d-stage {
  width: 100%;
  max-width: 1040px;
  height: 500px;
  margin: 3.5rem auto 1.5rem auto;
  background: radial-gradient(circle at center, #ffffff 0%, #f4f4f7 85%);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-float);
  position: relative;
  overflow: hidden;
}

#canvas3D {
  width: 100%;
  height: 100%;
  display: block;
}

.stage-pill-controls {
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(16px);
  padding: 0.35rem 0.5rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-light);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
  z-index: 10;
}

.calm-tab-btn {
  padding: 0.45rem 1.1rem;
  border-radius: var(--radius-full);
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--text-muted);
  transition: all 0.3s;
}

.calm-tab-btn.active {
  background: var(--text-main);
  color: #ffffff;
}

/* --------------------------------------------------------------------------
   Serene Editorial Cards Grid
   -------------------------------------------------------------------------- */
.editorial-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 3.5rem;
}

@media (max-width: 1024px) {
  .editorial-grid { grid-template-columns: 1fr; }
}

.editorial-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 2.5rem 2rem;
  box-shadow: var(--shadow-serene);
  transition: all var(--transition-calm);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.editorial-card:hover {
  transform: translateY(-6px);
  border-color: var(--border-hover);
  box-shadow: var(--shadow-hover);
}

.card-media-box {
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at center, rgba(197, 168, 128, 0.08) 0%, transparent 70%);
  border-radius: var(--radius-sm);
  margin: 1.5rem 0;
  overflow: hidden;
}

.card-media-box img {
  max-height: 150px;
  object-fit: contain;
  filter: drop-shadow(0 15px 25px rgba(0, 0, 0, 0.08));
  transition: transform 0.6s var(--transition-calm);
}

.editorial-card:hover .card-media-box img {
  transform: scale(1.08);
}

.spec-chip {
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.3rem 0.75rem;
  border-radius: var(--radius-full);
  background: var(--bg-secondary);
  color: var(--text-muted);
  display: inline-block;
  margin-right: 0.4rem;
  margin-bottom: 0.4rem;
}

/* --------------------------------------------------------------------------
   Serene Weight & Gravitas Comparator
   -------------------------------------------------------------------------- */
.comparator-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
  margin-top: 3.5rem;
}

@media (max-width: 840px) {
  .comparator-row { grid-template-columns: 1fr; }
}

.comparator-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 2.5rem 2rem;
  text-align: center;
  box-shadow: var(--shadow-serene);
  transition: all 0.3s;
}

.comparator-card.featured {
  background: #ffffff;
  border-color: var(--accent-gold);
  box-shadow: 0 20px 45px rgba(179, 139, 77, 0.12);
}

.weight-display {
  font-size: 3.5rem;
  font-weight: 700;
  letter-spacing: -0.04em;
  margin: 0.75rem 0;
  line-height: 1;
}

/* --------------------------------------------------------------------------
   Serene Customization Studio
   -------------------------------------------------------------------------- */
.studio-light-box {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: clamp(2.5rem, 5vw, 4rem);
  box-shadow: var(--shadow-float);
}

.material-palette {
  display: flex;
  gap: 1rem;
  margin: 1.5rem 0;
}

.palette-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--text-muted);
  transition: all 0.2s;
}

.palette-circle {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
  border: 2px solid transparent;
  transition: all 0.2s;
}

.palette-btn.active .palette-circle {
  border-color: var(--text-main);
  transform: scale(1.15);
}

.palette-btn.active {
  color: var(--text-main);
  font-weight: 600;
}

.calm-input {
  width: 100%;
  padding: 1rem 1.25rem;
  background: var(--bg-secondary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  font-size: 1rem;
  color: var(--text-main);
  transition: border-color 0.3s;
}

.calm-input:focus {
  outline: none;
  background: #ffffff;
  border-color: var(--accent-gold);
  box-shadow: 0 0 0 3px rgba(179, 139, 77, 0.12);
}

/* --------------------------------------------------------------------------
   Footer
   -------------------------------------------------------------------------- */
.serene-footer {
  background: var(--bg-secondary);
  border-top: 1px solid var(--border-light);
  padding: 5rem 0 3rem 0;
  font-size: 0.88rem;
  color: var(--text-muted);
}
"""

with open('/Users/ramay/gentech3-app/assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Update scene3d.js for Bright High-Key Ceramic Studio Lighting
scene3d_js = """/**
 * GenTech 3 Serene Studio 3D WebGL Engine
 * Pure White Ceramic, Champagne Gold & Brushed Titanium
 */

let scene, camera, renderer;
let cardMesh, ringMesh, chipMesh;
let cardGroup, ringGroup, mainStageGroup;
let light1, light2, hemiLight;
let targetRotationX = 0, targetRotationY = 0;
let isExploded = false;

function init3DScene() {
  const container = document.getElementById('canvas3D');
  if (!container) return;

  const width = container.clientWidth;
  const height = container.clientHeight;

  scene = new THREE.Scene();
  scene.background = null; // transparent to blend with CSS radial-gradient

  camera = new THREE.PerspectiveCamera(42, width / height, 0.1, 1000);
  camera.position.set(0, 0, 13.5);

  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.1;
  container.appendChild(renderer.domElement);

  // Soft High-Key Ambient & Studio Lights
  hemiLight = new THREE.HemisphereLight(0xffffff, 0xe2e8f0, 1.4);
  scene.add(hemiLight);

  light1 = new THREE.DirectionalLight(0xffffff, 1.8);
  light1.position.set(8, 12, 10);
  scene.add(light1);

  light2 = new THREE.DirectionalLight(0xfaf5eb, 1.2);
  light2.position.set(-8, -6, 6);
  scene.add(light2);

  // Stage Group
  mainStageGroup = new THREE.Group();
  scene.add(mainStageGroup);

  cardGroup = new THREE.Group();
  ringGroup = new THREE.Group();
  mainStageGroup.add(cardGroup);
  mainStageGroup.add(ringGroup);

  cardGroup.position.set(-2.0, 0, 0);
  ringGroup.position.set(2.8, 0, 0);

  // Build Ceramic / Titanium Card
  const cardGeo = new THREE.BoxGeometry(4.2, 2.7, 0.08);
  const cardMat = createMaterial('ceramic');
  cardMesh = new THREE.Mesh(cardGeo, cardMat);
  cardGroup.add(cardMesh);

  // Microchip
  const chipGeo = new THREE.BoxGeometry(0.75, 0.6, 0.09);
  const chipMat = new THREE.MeshStandardMaterial({
    color: 0xd4af37,
    metalness: 0.9,
    roughness: 0.2
  });
  chipMesh = new THREE.Mesh(chipGeo, chipMat);
  chipMesh.position.set(-1.2, 0.4, 0.01);
  cardGroup.add(chipMesh);

  // Build Ceramic Ring
  const ringGeo = new THREE.TorusGeometry(1.4, 0.32, 32, 100);
  const ringMat = createMaterial('ceramic');
  ringMesh = new THREE.Mesh(ringGeo, ringMat);
  ringMesh.rotation.x = Math.PI / 3;
  ringGroup.add(ringMesh);

  // Inner Resonator Trace
  const innerRingGeo = new THREE.TorusGeometry(1.24, 0.04, 16, 80);
  const innerRingMat = new THREE.MeshStandardMaterial({
    color: 0x3b82f6,
    emissive: 0x3b82f6,
    emissiveIntensity: 0.6
  });
  const innerRing = new THREE.Mesh(innerRingGeo, innerRingMat);
  innerRing.rotation.x = Math.PI / 3;
  ringGroup.add(innerRing);

  // Gentle Mouse listener
  window.addEventListener('mousemove', (e) => {
    const rect = container.getBoundingClientRect();
    const x = e.clientX - (rect.left + rect.width / 2);
    const y = e.clientY - (rect.top + rect.height / 2);
    targetRotationY = (x / rect.width) * 0.45;
    targetRotationX = (y / rect.height) * 0.45;
  });

  window.addEventListener('resize', () => {
    const newWidth = container.clientWidth;
    const newHeight = container.clientHeight;
    camera.aspect = newWidth / newHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(newWidth, newHeight);
  });

  animate();
}

function createMaterial(type) {
  if (type === 'ceramic') {
    return new THREE.MeshStandardMaterial({
      color: 0xf8fafc,
      metalness: 0.1,
      roughness: 0.15,
      clearcoat: 1.0,
      clearcoatRoughness: 0.1
    });
  } else if (type === 'champagne') {
    return new THREE.MeshStandardMaterial({
      color: 0xd6c5af,
      metalness: 0.85,
      roughness: 0.25
    });
  } else if (type === 'titanium') {
    return new THREE.MeshStandardMaterial({
      color: 0xd8dde3,
      metalness: 0.9,
      roughness: 0.28
    });
  } else if (type === 'gold') {
    return new THREE.MeshStandardMaterial({
      color: 0xd4af37,
      metalness: 0.92,
      roughness: 0.18
    });
  }
}

function set3DMaterial(matKey) {
  const newMat = createMaterial(matKey);
  if (cardMesh) cardMesh.material = newMat;
  if (ringMesh) ringMesh.material = newMat;
}

function setActiveArtifact(artifact) {
  if (artifact === 'both') {
    cardGroup.position.set(-2.0, 0, 0);
    cardGroup.scale.set(1, 1, 1);
    ringGroup.position.set(2.8, 0, 0);
    ringGroup.scale.set(1, 1, 1);
  } else if (artifact === 'card') {
    cardGroup.position.set(0, 0, 0);
    cardGroup.scale.set(1.25, 1.25, 1.25);
    ringGroup.scale.set(0.001, 0.001, 0.001);
  } else if (artifact === 'ring') {
    ringGroup.position.set(0, 0, 0);
    ringGroup.scale.set(1.35, 1.35, 1.35);
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
    cardGroup.position.y = Math.sin(time * 0.8) * 0.08;
  }
  
  if (ringGroup) {
    ringGroup.rotation.y += 0.005;
    ringGroup.position.y = Math.cos(time * 0.8) * 0.08;
  }
  
  renderer.render(scene, camera);
}

document.addEventListener('DOMContentLoaded', () => {
  if (typeof THREE !== 'undefined') init3DScene();
});
"""

with open('/Users/ramay/gentech3-app/assets/js/scene3d.js', 'w', encoding='utf-8') as f:
    f.write(scene3d_js)

# 3. Write HTML for Serene Alabaster Edition
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>GenTech | Serene Hardware & Autonomous FinTech Architecture</title>
    
    <!-- Google Fonts: Playfair Display + Plus Jakarta Sans + JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Three.js 3D WebGL Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <!-- Core Stylesheet -->
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<!-- Serene Sticky Navigation -->
<header class="serene-header">
    <div class="container">
        <nav class="serene-nav">
            <a href="index.html" class="serene-brand">
                <div class="brand-dot"></div>
                <div class="brand-title">GenTech</div>
            </a>

            <div class="serene-menu">
                <a href="#overview" class="serene-link">Overview</a>
                <a href="#ecosystem" class="serene-link">Ecosystem</a>
                <a href="#materials" class="serene-link">Materials & Weight</a>
                <a href="#transit" class="serene-link">Smart Cities</a>
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

<main id="overview">
    <!-- 1. Serene Hero Section -->
    <section class="serene-hero">
        <div class="container">
            <div class="calm-badge">✦ Dubai R&D Center • Pure Ceramic & Titanium</div>
            <h1 class="serif-display">
                Calm technology. <br>
                <span class="champagne-gradient-text">Substance in every touch.</span>
            </h1>
            <p class="hero-subtext">
                A serene synthesis of 28.5g solid titanium, battery-free zirconia ceramic smart rings, and sub-50ms municipal transit cards — engineered with whisper-quiet precision in Dubai.
            </p>

            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="#studio" class="btn-calm-primary">Personalize in Studio</a>
                <a href="#ecosystem" class="btn-calm-ghost">Explore Ecosystem</a>
            </div>

            <!-- Serene 3D Stage -->
            <div class="hero-3d-stage">
                <div id="canvas3D"></div>
                <div class="stage-pill-controls">
                    <button class="calm-tab-btn active artifact-toggle-btn" data-artifact="both">Both Artifacts</button>
                    <button class="calm-tab-btn artifact-toggle-btn" data-artifact="ring">Apex Ring</button>
                    <button class="calm-tab-btn artifact-toggle-btn" data-artifact="card">Sovereign Card</button>
                    <button class="calm-tab-btn" id="explodedViewBtn">Exploded View</button>
                </div>
            </div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">
                Move your cursor to gently rotate the 3D ceramic & titanium artifacts
            </div>
        </div>
    </section>

    <!-- 2. The Serene 6-Pillar Ecosystem Grid -->
    <section class="section-spacing" id="ecosystem" style="background: var(--bg-secondary);">
        <div class="container">
            <div style="text-align: center; max-width: 720px; margin: 0 auto 3rem auto;">
                <div class="calm-badge">Complete Hardware Suite</div>
                <h2 class="serif-display">Refined instruments of exchange.</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-top: 0.75rem;">
                    From bespoke private banking cards and smart jewelry to high-throughput metro ticketing and 5G multi-application SIMs.
                </p>
            </div>

            <div class="editorial-grid">
                <!-- 1. Apex Rings & Wearables -->
                <div class="editorial-card">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="spec-chip" style="background:rgba(71,122,102,0.1); color:var(--accent-sage);">Wearables</span>
                            <span style="font-size:0.8rem; color:var(--text-dim);">IP68 50m</span>
                        </div>
                        <div class="card-media-box">
                            <img src="assets/images/wearable.png" alt="Apex Rings and Wristbands">
                        </div>
                        <h3 class="serif-display">Apex Rings & Wristbands</h3>
                        <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.65; margin-top: 0.6rem;">
                            100% battery-free passive RF resonance. Crafted from biocompatible zirconia ceramic and medical silicone for resorts, fitness, and daily contactless payments.
                        </p>
                    </div>
                    <div style="margin-top: 1.5rem; border-top: 1px solid var(--border-light); padding-top: 1rem;">
                        <span class="spec-chip">0% Battery</span>
                        <span class="spec-chip">EMV Tokenized</span>
                    </div>
                </div>

                <!-- 2. Sovereign Metal Cards -->
                <div class="editorial-card">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="spec-chip" style="background:rgba(197,168,128,0.15); color:var(--accent-gold);">Tactile Luxury</span>
                            <span style="font-size:0.8rem; color:var(--accent-gold); font-weight:600;">28.5g</span>
                        </div>
                        <div class="card-media-box">
                            <img src="assets/images/portfolio-4.png" alt="Sovereign Metal Cards">
                        </div>
                        <h3 class="serif-display">Sovereign Metal & Ceramic</h3>
                        <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.65; margin-top: 0.6rem;">
                            Solid aerospace Grade-5 titanium and mirror-polished white ceramic cards machined with CNC precision for private wealth and high-tier banking.
                        </p>
                    </div>
                    <div style="margin-top: 1.5rem; border-top: 1px solid var(--border-light); padding-top: 1rem;">
                        <span class="spec-chip">28.5g Monolith</span>
                        <span class="spec-chip">CC EAL6+</span>
                    </div>
                </div>

                <!-- 3. Smart City Transit Cards -->
                <div class="editorial-card">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="spec-chip" style="background:rgba(59,130,246,0.1); color:var(--accent-blue);">Smart Cities</span>
                            <span style="font-size:0.8rem; color:var(--accent-blue); font-weight:600;">&lt;42ms</span>
                        </div>
                        <div class="card-media-box">
                            <img src="assets/images/transportcards.png" alt="Transport & City Transit Cards">
                        </div>
                        <h3 class="serif-display">Municipal City Transit Cards</h3>
                        <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.65; margin-top: 0.6rem;">
                            High-speed contactless fare collection for subways, bus fleets, and municipal multi-purpose cards with Calypso and MIFARE DESFire EV3 standards.
                        </p>
                    </div>
                    <div style="margin-top: 1.5rem; border-top: 1px solid var(--border-light); padding-top: 1rem;">
                        <span class="spec-chip">Calypso / MIFARE</span>
                        <span class="spec-chip">Bio-PVC</span>
                    </div>
                </div>

                <!-- 4. Super NFC 5G SIM -->
                <div class="editorial-card">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="spec-chip">5G Telecom</span>
                            <span style="font-size:0.8rem; color:var(--text-dim);">Super SIM</span>
                        </div>
                        <div class="card-media-box">
                            <img src="assets/images/supersim.png" alt="Super NFC 5G SIM">
                        </div>
                        <h3 class="serif-display">Super NFC 5G SIM Cards</h3>
                        <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.65; margin-top: 0.6rem;">
                            Unifies 5G telecommunications, banking payments, digital resident ID, and transit tokens into a single secure mobile chip element.
                        </p>
                    </div>
                    <div style="margin-top: 1.5rem; border-top: 1px solid var(--border-light); padding-top: 1rem;">
                        <span class="spec-chip">Multi-Applet</span>
                        <span class="spec-chip">GSMA 5G</span>
                    </div>
                </div>

                <!-- 5. Custom Chip Plates -->
                <div class="editorial-card">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="spec-chip">Artisan Chip</span>
                            <span style="font-size:0.8rem; color:var(--accent-gold);">Laser Etched</span>
                        </div>
                        <div class="card-media-box">
                            <img src="assets/images/customize-chip.png" alt="Custom Chip Modules">
                        </div>
                        <h3 class="serif-display">Bespoke Chip Modules</h3>
                        <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.65; margin-top: 0.6rem;">
                            Transform standard contact pads into high-prestige art with custom laser geometries, 24K gold flash plating, and micro-grooved satin finishes.
                        </p>
                    </div>
                    <div style="margin-top: 1.5rem; border-top: 1px solid var(--border-light); padding-top: 1rem;">
                        <span class="spec-chip">Custom Geometries</span>
                        <span class="spec-chip">24K Sputter</span>
                    </div>
                </div>

                <!-- 6. Banking Hardware & POS -->
                <div class="editorial-card">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="spec-chip">Issuance Hardware</span>
                            <span style="font-size:0.8rem; color:var(--text-dim);">POS / HSM</span>
                        </div>
                        <div class="card-media-box">
                            <img src="assets/images/pos.png" alt="Banking POS & Personalization Hardware">
                        </div>
                        <h3 class="serif-display">Personalization Hardware & POS</h3>
                        <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.65; margin-top: 0.6rem;">
                            Turnkey desktop card embossers, high-speed thermal printers, smart Android POS terminals, and cryptographic Hardware Security Modules.
                        </p>
                    </div>
                    <div style="margin-top: 1.5rem; border-top: 1px solid var(--border-light); padding-top: 1rem;">
                        <span class="spec-chip">PCI PTS 6.x</span>
                        <span class="spec-chip">Instant Issuance</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Tactile Weight & Material Comparison -->
    <section class="section-spacing" id="materials">
        <div class="container">
            <div style="text-align: center; max-width: 680px; margin: 0 auto 3rem auto;">
                <div class="calm-badge">Physical Weight Matters</div>
                <h2 class="serif-display">The unmistakable heft of quality.</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-top: 0.75rem;">
                    Feel the profound difference between disposable plastic and solid aerospace titanium.
                </p>
            </div>

            <div class="comparator-row">
                <div class="comparator-card">
                    <span style="font-size:0.8rem; font-weight:600; color:var(--text-dim); text-transform:uppercase;">Standard Commercial Card</span>
                    <div class="weight-display" style="color: #94a3b8;">5.0g</div>
                    <div style="font-size:0.9rem; font-weight:600; color:var(--text-muted); margin-bottom:1rem;">Conventional PVC</div>
                    <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6;">
                        Easily flexes and scratches within months of everyday use.
                    </p>
                </div>

                <div class="comparator-card">
                    <span style="font-size:0.8rem; font-weight:600; color:var(--text-dim); text-transform:uppercase;">Hybrid Veneer Card</span>
                    <div class="weight-display" style="color: #64748b;">16.0g</div>
                    <div style="font-size:0.9rem; font-weight:600; color:var(--text-muted); margin-bottom:1rem;">Steel Veneer + PVC Core</div>
                    <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6;">
                        Partial metal faceplate bonded over a standard plastic foundation.
                    </p>
                </div>

                <div class="comparator-card featured">
                    <span style="font-size:0.8rem; font-weight:700; color:var(--accent-gold); text-transform:uppercase;">GenTech Sovereign</span>
                    <div class="weight-display champagne-gradient-text">28.5g</div>
                    <div style="font-size:0.9rem; font-weight:600; color:var(--accent-gold); margin-bottom:1rem;">100% Solid Grade-5 Titanium</div>
                    <p style="font-size:0.85rem; color:var(--text-main); line-height:1.6;">
                        Milled from a single solid billet, 24K gold sputter, laser engraved, everlasting.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Bespoke Studio: Laser Engraving & Material Palette -->
    <section class="section-spacing" id="studio" style="background: var(--bg-secondary);">
        <div class="container">
            <div class="studio-light-box">
                <div style="text-align: center; max-width: 640px; margin: 0 auto 3rem auto;">
                    <div class="calm-badge">Bespoke Personalization</div>
                    <h2 class="serif-display">The Alabaster Studio</h2>
                    <p style="color: var(--text-muted); font-size: 1.05rem; margin-top: 0.5rem;">
                        Select your preferred palette and inscribe your institution's cardholder details with sub-micron laser precision.
                    </p>

                    <!-- Material Palette Selection -->
                    <div class="material-palette" style="justify-content: center;">
                        <button class="palette-btn active swatch-btn" data-material="ceramic">
                            <div class="palette-circle" style="background: #ffffff; border-color:#e2e8f0;"></div>
                            <span>Pure Ceramic</span>
                        </button>
                        <button class="palette-btn swatch-btn" data-material="champagne">
                            <div class="palette-circle" style="background: linear-gradient(135deg, #f7f1e5, #c8b6a6);"></div>
                            <span>Champagne</span>
                        </button>
                        <button class="palette-btn swatch-btn" data-material="titanium">
                            <div class="palette-circle" style="background: linear-gradient(135deg, #ffffff, #94a3b8);"></div>
                            <span>Pale Titanium</span>
                        </button>
                        <button class="palette-btn swatch-btn" data-material="gold">
                            <div class="palette-circle" style="background: linear-gradient(135deg, #f6e27a, #aa7c11);"></div>
                            <span>24K Gold</span>
                        </button>
                    </div>
                </div>

                <div style="max-width: 720px; margin: 0 auto;">
                    <div style="margin-bottom: 2rem;">
                        <label style="font-size:0.85rem; font-weight:600; color:var(--text-main); display:block; margin-bottom:0.5rem;">
                            Cardholder Name / Serial Number:
                        </label>
                        <input type="text" id="engravingTextInput" class="calm-input" placeholder="ALEXANDER VANCE" value="ALEXANDER VANCE" maxlength="28">
                    </div>

                    <div style="position: relative; height: 260px; background: #ffffff; border-radius: var(--radius-sm); border: 1px solid var(--border-light); display: flex; align-items: center; justify-content: center; overflow: hidden; box-shadow: var(--shadow-serene);">
                        <img src="assets/images/portfolio-4.png" alt="Card Preview" style="max-height: 190px; filter: drop-shadow(0 15px 30px rgba(0,0,0,0.1));">
                        <div id="liveEngravedText" style="position: absolute; bottom: 25px; right: 35px; font-family: var(--font-sans); font-size: 1.05rem; font-weight: 700; letter-spacing: 0.15em; color: #111827; text-transform: uppercase;">
                            ALEXANDER VANCE
                        </div>
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1.25rem; font-size: 0.82rem; color: var(--text-muted);">
                        <span>0.01mm Precision Fiber Laser</span>
                        <span style="color: var(--accent-gold); font-weight: 600;">Dubai Cleanroom Facility</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Quiet Enterprise Intake -->
    <section class="section-spacing" id="inquire" style="text-align: center;">
        <div class="container">
            <div class="calm-badge">Private Banking & FinTech Inquiries</div>
            <h2 class="serif-display">Commission your bank's fleet.</h2>
            <p class="hero-subtext">
                Speak directly with our Dubai engineering desk to request white-glove material sample boxes and custom pre-personalization configurations.
            </p>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="mailto:info@gentech.ae" class="btn-calm-primary">Initiate Confidential Consultation</a>
                <a href="tel:+971500000000" class="btn-calm-ghost">Direct Dubai Phone</a>
            </div>
        </div>
    </section>
</main>

<!-- Serene Footer -->
<footer class="serene-footer">
    <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-light); padding-bottom: 2.5rem; flex-wrap: wrap; gap: 1.5rem;">
            <div>
                <div style="font-size: 1.2rem; font-weight: 700; color: var(--text-main);">GenTech Global LLC</div>
                <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">
                    Ras Al Khaimah Economic Zone, Dubai, United Arab Emirates.
                </div>
            </div>
            <div style="display: flex; gap: 1.75rem; font-size: 0.82rem; font-weight: 600; color: var(--text-muted);">
                <span>EMVCo Certified</span>
                <span>PCI-DSS Level 1</span>
                <span>ISO 14443 Type A</span>
                <span>GSMA 5G</span>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 1.5rem; font-size: 0.82rem; color: var(--text-dim); flex-wrap: wrap; gap: 1rem;">
            <div>&copy; 2025-2026 GenTech Global LLC. All rights reserved.</div>
            <div>GenTech 3 • Serene Alabaster Edition</div>
        </div>
    </div>
</footer>

<!-- Scripts -->
<script src="assets/js/audio.js"></script>
<script src="assets/js/scene3d.js"></script>
<script src="assets/js/app.js"></script>
</body>
</html>
"""

with open('/Users/ramay/gentech3-app/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("GenTech 3 Serene Alabaster Edition created successfully!")
