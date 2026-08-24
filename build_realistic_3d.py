import os
import zipfile

print("Building photo-realistic 3D Card and High-Contrast Ring textures...")

# Photo-Realistic Three.js scene with Canvas Texture Generation
scene3d_masterpiece = """/**
 * GenTech 3 - Ultra-Realistic 3D Atelier
 * Generates dynamic high-res photorealistic textures for Titanium Card & Smart Ring
 */

let scene, camera, renderer;
let cardMesh, ringMesh;
let cardGroup, ringGroup, mainStageGroup;
let hemiLight, keyLight, fillLight, rimLightGold, rimLightBlue;
let targetRotationX = 0.1, targetRotationY = -0.15;
let currentArtifact = 'card';

// Generate High-Res 2048x1280 Titanium Card Texture
function createCardTexture() {
  const canvas = document.createElement('canvas');
  canvas.width = 2048;
  canvas.height = 1290;
  const ctx = canvas.getContext('2d');

  // 1. Brushed Titanium Base Gradient
  const grad = ctx.createLinearGradient(0, 0, 2048, 1290);
  grad.addColorStop(0.0, '#2a2f3a');
  grad.addColorStop(0.25, '#475163');
  grad.addColorStop(0.5, '#2d3340');
  grad.addColorStop(0.75, '#566175');
  grad.addColorStop(1.0, '#1f242e');
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, 2048, 1290);

  // Brushed Horizontal Texture Noise
  ctx.fillStyle = 'rgba(255, 255, 255, 0.03)';
  for (let i = 0; i < 1290; i += 3) {
    if (Math.random() > 0.4) {
      ctx.fillRect(0, i, 2048, 1.5);
    }
  }

  // Card Outer Chamfer Bevel Stroke
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
  ctx.lineWidth = 12;
  ctx.strokeRect(20, 20, 2008, 1250);

  // 2. Gold EMV Microchip Box with Intricate Circuit Paths
  const chipX = 220, chipY = 460, chipW = 280, chipH = 220;
  
  // Chip Base
  const chipGrad = ctx.createLinearGradient(chipX, chipY, chipX + chipW, chipY + chipH);
  chipGrad.addColorStop(0.0, '#e5c158');
  chipGrad.addColorStop(0.5, '#bf9526');
  chipGrad.addColorStop(1.0, '#ffd868');
  ctx.fillStyle = chipGrad;
  ctx.beginPath();
  ctx.roundRect(chipX, chipY, chipW, chipH, 24);
  ctx.fill();
  ctx.strokeStyle = '#85640e';
  ctx.lineWidth = 6;
  ctx.stroke();

  // Chip Micro-circuit Lines
  ctx.strokeStyle = 'rgba(0, 0, 0, 0.45)';
  ctx.lineWidth = 4;
  ctx.beginPath();
  // Horizontal split
  ctx.moveTo(chipX, chipY + 110); ctx.lineTo(chipX + chipW, chipY + 110);
  // Vertical splits
  ctx.moveTo(chipX + 85, chipY); ctx.lineTo(chipX + 85, chipY + chipH);
  ctx.moveTo(chipX + 195, chipY); ctx.lineTo(chipX + 195, chipY + chipH);
  // Center contact circle
  ctx.arc(chipX + 140, chipY + 110, 30, 0, Math.PI * 2);
  ctx.stroke();

  // 3. Contactless NFC Waves Icon
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.45)';
  ctx.lineWidth = 8;
  const nfcX = 580, nfcY = 570;
  for (let r = 25; r <= 75; r += 25) {
    ctx.beginPath();
    ctx.arc(nfcX, nfcY, r, -Math.PI * 0.35, Math.PI * 0.35);
    ctx.stroke();
  }

  // 4. Laser Engraved Brand Typography (GENTECH)
  ctx.fillStyle = '#ffffff';
  ctx.font = 'bold 84px "Plus Jakarta Sans", sans-serif';
  ctx.letterSpacing = '8px';
  ctx.fillText('GENTECH', 1420, 240);

  ctx.fillStyle = '#c5a880';
  ctx.font = '500 36px "JetBrains Mono", monospace';
  ctx.letterSpacing = '4px';
  ctx.fillText('SOVEREIGN TITANIUM', 1340, 295);

  // 5. Laser Engraved Cardholder Details
  ctx.fillStyle = 'rgba(255, 255, 255, 0.4)';
  ctx.font = '600 32px "Plus Jakarta Sans", sans-serif';
  ctx.letterSpacing = '4px';
  ctx.fillText('CARDHOLDER / PRIVATE CLIENT', 220, 960);

  ctx.fillStyle = '#f8fafc';
  ctx.font = 'bold 64px "Plus Jakarta Sans", sans-serif';
  ctx.letterSpacing = '8px';
  ctx.fillText('ALEXANDER VANCE', 220, 1040);

  // 6. Serial & CC EAL6+ Info
  ctx.fillStyle = '#94a3b8';
  ctx.font = '500 38px "JetBrains Mono", monospace';
  ctx.letterSpacing = '6px';
  ctx.fillText('GT-9482-2026 • CC EAL6+ SECURE ELEMENT', 220, 1140);

  // Holographic GenTech Security Crest Icon
  ctx.strokeStyle = '#c5a880';
  ctx.lineWidth = 6;
  ctx.strokeRect(1740, 960, 120, 120);
  ctx.fillStyle = '#c5a880';
  ctx.font = 'bold 36px "JetBrains Mono"';
  ctx.fillText('GT', 1775, 1035);

  const texture = new THREE.CanvasTexture(canvas);
  texture.needsUpdate = true;
  return texture;
}

// Generate Ring Texture (Bicolor Brushed Ceramic & Gold Inlay)
function createRingTexture() {
  const canvas = document.createElement('canvas');
  canvas.width = 1024;
  canvas.height = 256;
  const ctx = canvas.getContext('2d');

  // Dark obsidian ceramic gradient for rich contrast on light background
  const grad = ctx.createLinearGradient(0, 0, 1024, 256);
  grad.addColorStop(0.0, '#111827');
  grad.addColorStop(0.4, '#1f2937');
  grad.addColorStop(0.5, '#d4af37'); // Center 18K Gold Inlay Ridge
  grad.addColorStop(0.6, '#1f2937');
  grad.addColorStop(1.0, '#111827');
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, 1024, 256);

  // Gold laser markings
  ctx.fillStyle = '#fef08a';
  ctx.font = 'bold 24px "JetBrains Mono"';
  for (let x = 40; x < 1024; x += 240) {
    ctx.fillText('GENTECH APEX • NFC', x, 136);
  }

  const texture = new THREE.CanvasTexture(canvas);
  texture.needsUpdate = true;
  return texture;
}

function init3DScene() {
  const container = document.getElementById('canvas3D');
  if (!container) return;

  const width = container.clientWidth;
  const height = container.clientHeight;

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(38, width / height, 0.1, 1000);

  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.35;
  container.appendChild(renderer.domElement);

  // 1. Ambient & Hemisphere Light
  hemiLight = new THREE.HemisphereLight(0xffffff, 0xdbeafe, 1.2);
  scene.add(hemiLight);

  // 2. Crisp Key Studio Spotlight
  keyLight = new THREE.DirectionalLight(0xffffff, 2.8);
  keyLight.position.set(8, 10, 12);
  scene.add(keyLight);

  // 3. Warm Champagne Fill Light
  fillLight = new THREE.DirectionalLight(0xfef3c7, 1.6);
  fillLight.position.set(-10, -4, 8);
  scene.add(fillLight);

  // 4. Gold Rim Specular Highlight (Back Glint)
  rimLightGold = new THREE.DirectionalLight(0xd4af37, 2.2);
  rimLightGold.position.set(0, 8, -10);
  scene.add(rimLightGold);

  // 5. Stage Groups
  mainStageGroup = new THREE.Group();
  scene.add(mainStageGroup);

  cardGroup = new THREE.Group();
  ringGroup = new THREE.Group();
  mainStageGroup.add(cardGroup);
  mainStageGroup.add(ringGroup);

  // --- TITANIUM CARD MESH ---
  const cardTexture = createCardTexture();
  const cardGeo = new THREE.BoxGeometry(4.8, 3.03, 0.08);
  
  // Materials: Front has texture, back and sides have brushed titanium
  const sideMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.95, roughness: 0.2 });
  const frontMat = new THREE.MeshStandardMaterial({
    map: cardTexture,
    metalness: 0.88,
    roughness: 0.22,
    clearcoat: 0.6,
    clearcoatRoughness: 0.15
  });
  
  const cardMaterials = [sideMat, sideMat, sideMat, sideMat, frontMat, frontMat];
  cardMesh = new THREE.Mesh(cardGeo, cardMaterials);
  cardGroup.add(cardMesh);

  // Subtle 3D Card Edge Glint Frame
  const frameGeo = new THREE.BoxGeometry(4.82, 3.05, 0.07);
  const frameMat = new THREE.MeshStandardMaterial({ color: 0xd4af37, metalness: 0.98, roughness: 0.1 });
  const frameMesh = new THREE.Mesh(frameGeo, frameMat);
  cardGroup.add(frameMesh);

  // --- SMART RING MESH (High Contrast Obsidian & 18K Gold Inlay) ---
  const ringTexture = createRingTexture();
  const ringGeo = new THREE.TorusGeometry(1.45, 0.36, 48, 120);
  const ringMat = new THREE.MeshStandardMaterial({
    map: ringTexture,
    metalness: 0.92,
    roughness: 0.15,
    clearcoat: 1.0,
    clearcoatRoughness: 0.1
  });
  ringMesh = new THREE.Mesh(ringGeo, ringMat);
  ringMesh.rotation.x = Math.PI / 3;
  ringGroup.add(ringMesh);

  // Glowing Cyan RF Resonator Center Core
  const innerResGeo = new THREE.TorusGeometry(1.28, 0.05, 16, 80);
  const innerResMat = new THREE.MeshStandardMaterial({
    color: 0x06b6d4,
    emissive: 0x06b6d4,
    emissiveIntensity: 1.2
  });
  const innerRes = new THREE.Mesh(innerResGeo, innerResMat);
  innerRes.rotation.x = Math.PI / 3;
  ringGroup.add(innerRes);

  // Set default view to Card
  setActiveArtifact('card');

  // Mouse Listener
  window.addEventListener('mousemove', (e) => {
    const rect = container.getBoundingClientRect();
    const x = e.clientX - (rect.left + rect.width / 2);
    const y = e.clientY - (rect.top + rect.height / 2);
    targetRotationY = (x / rect.width) * 0.6;
    targetRotationX = (y / rect.height) * 0.5;
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
      targetRotationY = (deltaX / window.innerWidth) * 1.8;
      targetRotationX = (deltaY / window.innerHeight) * 1.8;
    }
  }, { passive: true });

  // Resize Listener
  window.addEventListener('resize', () => {
    const newW = container.clientWidth;
    const newH = container.clientHeight;
    camera.aspect = newW / newH;
    camera.updateProjectionMatrix();
    renderer.setSize(newW, newH);
    setActiveArtifact(currentArtifact);
  });

  animate();
}

function setActiveArtifact(artifact) {
  currentArtifact = artifact;
  const container = document.getElementById('canvas3D');
  const isMobile = container && (container.clientWidth / container.clientHeight < 0.9);

  if (artifact === 'card') {
    camera.position.set(0, 0, isMobile ? 12 : 10.5);
    cardGroup.position.set(0, 0, 0);
    cardGroup.scale.set(isMobile ? 1.0 : 1.22, isMobile ? 1.0 : 1.22, isMobile ? 1.0 : 1.22);

    ringGroup.position.set(0, 15, 0);
    ringGroup.scale.set(0.001, 0.001, 0.001);
  } else if (artifact === 'ring') {
    camera.position.set(0, 0, isMobile ? 11 : 9.5);
    ringGroup.position.set(0, 0, 0);
    ringGroup.scale.set(isMobile ? 1.15 : 1.35, isMobile ? 1.15 : 1.35, isMobile ? 1.15 : 1.35);

    cardGroup.position.set(0, -15, 0);
    cardGroup.scale.set(0.001, 0.001, 0.001);
  }
}

function animate() {
  requestAnimationFrame(animate);
  const time = Date.now() * 0.001;
  if (cardGroup && currentArtifact === 'card') {
    cardGroup.rotation.y += (targetRotationY - cardGroup.rotation.y) * 0.06;
    cardGroup.rotation.x += (targetRotationX - cardGroup.rotation.x) * 0.06;
    cardGroup.position.y = Math.sin(time * 0.7) * 0.07;
  }
  if (ringGroup && currentArtifact === 'ring') {
    ringGroup.rotation.y += 0.01;
    ringGroup.rotation.x += (targetRotationX - ringGroup.rotation.x) * 0.04;
    ringGroup.position.y = Math.cos(time * 0.7) * 0.07;
  }
  renderer.render(scene, camera);
}

document.addEventListener('DOMContentLoaded', () => {
  if (typeof THREE !== 'undefined') init3DScene();
});
"""

with open('/Users/ramay/gentech3-app/assets/js/scene3d.js', 'w', encoding='utf-8') as f:
    f.write(scene3d_masterpiece)

# Update HTML to set Titanyum Kart as active default button in toolbar
with open('/Users/ramay/gentech3-app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<button class="toolbar-btn active artifact-toggle-btn" data-artifact="ring">💍 Akıllı Yüzük</button>\n                    <button class="toolbar-btn artifact-toggle-btn" data-artifact="card">💳 Titanyum Kart</button>',
    '<button class="toolbar-btn active artifact-toggle-btn" data-artifact="card">💳 Titanyum Kart</button>\n                    <button class="toolbar-btn artifact-toggle-btn" data-artifact="ring">💍 Akıllı Yüzük</button>'
)

with open('/Users/ramay/gentech3-app/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update app.js
app_js = """/**
 * GenTech 3 Master Controller
 */
document.addEventListener('DOMContentLoaded', () => {
  // Artifact Toggle (Card & Ring)
  const artifactBtns = document.querySelectorAll('.artifact-toggle-btn');
  artifactBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      artifactBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const art = btn.getAttribute('data-artifact');
      if (typeof setActiveArtifact === 'function') setActiveArtifact(art);
    });
  });

  // Live Card Configurator (Approved Design)
  const mockup = document.getElementById('liveCardMockup');
  const cardName = document.getElementById('mockupCardholder');
  const cardSerial = document.getElementById('mockupSerial');
  const nameInput = document.getElementById('configNameInput');
  const serialInput = document.getElementById('configSerialInput');
  const alloyBtns = document.querySelectorAll('.alloy-pill-btn');

  alloyBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      alloyBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const alloy = btn.getAttribute('data-alloy');
      if (mockup) {
        mockup.className = `live-card-mockup ${alloy}`;
      }
    });
  });

  nameInput?.addEventListener('input', (e) => {
    if (cardName) cardName.textContent = e.target.value.toUpperCase() || 'ALEXANDER VANCE';
  });

  serialInput?.addEventListener('input', (e) => {
    if (cardSerial) cardSerial.textContent = e.target.value || 'GT-9482-2026';
  });
});
"""

with open('/Users/ramay/gentech3-app/assets/js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

# Sync with WordPress Theme and Rebuild ZIP
wp_theme_dir = '/Users/ramay/gentech3-wp/gentech3-theme'
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
os.system("cp -r /Users/ramay/gentech3-app/* /Users/ramay/gentech3-lab/")

print("Realistic 3D Masterpiece with high-contrast Obsidian/Gold Ring and Apple-grade Titanium Card built!")
