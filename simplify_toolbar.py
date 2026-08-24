import re
import os
import zipfile

print("Simplifying 3D toolbar to just Akıllı Yüzük and Titanyum Kart...")

# 1. Update index.html in gentech3-app
with open('/Users/ramay/gentech3-app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace toolbar
old_toolbar_pattern = r'<div class="studio-toolbar">.*?</div>'
new_toolbar = """<div class="studio-toolbar">
                    <button class="toolbar-btn active artifact-toggle-btn" data-artifact="ring">💍 Akıllı Yüzük</button>
                    <button class="toolbar-btn artifact-toggle-btn" data-artifact="card">💳 Titanyum Kart</button>
                </div>"""

html = re.sub(old_toolbar_pattern, new_toolbar, html, flags=re.DOTALL)

with open('/Users/ramay/gentech3-app/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update scene3d.js in gentech3-app for dedicated single-artifact focus
scene3d_code = """/**
 * GenTech 3 - Focused 3D Studio (Ring & Card Protagonists)
 */

let scene, camera, renderer;
let cardMesh, ringMesh, chipMesh;
let cardGroup, ringGroup, mainStageGroup;
let hemiLight, dirLight1, dirLight2;
let targetRotationX = 0, targetRotationY = 0;
let currentArtifact = 'ring'; // default to ring

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
  hemiLight = new THREE.HemisphereLight(0xffffff, 0xf1f5f9, 1.3);
  scene.add(hemiLight);

  dirLight1 = new THREE.DirectionalLight(0xffffff, 1.8);
  dirLight1.position.set(6, 8, 10);
  scene.add(dirLight1);

  dirLight2 = new THREE.DirectionalLight(0xfaf5eb, 1.0);
  dirLight2.position.set(-8, -4, 6);
  scene.add(dirLight2);

  // Stage Hierarchy
  mainStageGroup = new THREE.Group();
  scene.add(mainStageGroup);

  cardGroup = new THREE.Group();
  ringGroup = new THREE.Group();
  mainStageGroup.add(cardGroup);
  mainStageGroup.add(ringGroup);

  // Card Mesh
  const cardGeo = new THREE.BoxGeometry(4.4, 2.8, 0.08);
  const cardMat = createMaterial('titanium');
  cardMesh = new THREE.Mesh(cardGeo, cardMat);
  cardGroup.add(cardMesh);

  // Chip
  const chipGeo = new THREE.BoxGeometry(0.8, 0.65, 0.09);
  const chipMat = new THREE.MeshStandardMaterial({ color: 0xd4af37, metalness: 0.92, roughness: 0.18 });
  chipMesh = new THREE.Mesh(chipGeo, chipMat);
  chipMesh.position.set(-1.25, 0.45, 0.01);
  cardGroup.add(chipMesh);

  // Ring Mesh
  const ringGeo = new THREE.TorusGeometry(1.4, 0.32, 32, 100);
  const ringMat = createMaterial('ceramic');
  ringMesh = new THREE.Mesh(ringGeo, ringMat);
  ringMesh.rotation.x = Math.PI / 3;
  ringGroup.add(ringMesh);

  // Inner Resonator Trace
  const innerRingGeo = new THREE.TorusGeometry(1.24, 0.04, 16, 80);
  const innerRingMat = new THREE.MeshStandardMaterial({ color: 0x3b82f6, emissive: 0x3b82f6, emissiveIntensity: 0.6 });
  const innerRing = new THREE.Mesh(innerRingGeo, innerRingMat);
  innerRing.rotation.x = Math.PI / 3;
  ringGroup.add(innerRing);

  // Initialize focus on ring
  setActiveArtifact('ring');

  // Mouse Listener
  window.addEventListener('mousemove', (e) => {
    const rect = container.getBoundingClientRect();
    const x = e.clientX - (rect.left + rect.width / 2);
    const y = e.clientY - (rect.top + rect.height / 2);
    targetRotationY = (x / rect.width) * 0.45;
    targetRotationX = (y / rect.height) * 0.45;
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
    setActiveArtifact(currentArtifact);
  });

  animate();
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

  if (artifact === 'ring') {
    camera.position.set(0, 0, isMobile ? 12 : 11);
    ringGroup.position.set(0, 0, 0);
    ringGroup.scale.set(isMobile ? 1.2 : 1.35, isMobile ? 1.2 : 1.35, isMobile ? 1.2 : 1.35);

    cardGroup.position.set(0, -10, 0);
    cardGroup.scale.set(0.001, 0.001, 0.001);
  } else if (artifact === 'card') {
    camera.position.set(0, 0, isMobile ? 13.5 : 12);
    cardGroup.position.set(0, 0, 0);
    cardGroup.scale.set(isMobile ? 1.05 : 1.25, isMobile ? 1.05 : 1.25, isMobile ? 1.05 : 1.25);

    ringGroup.position.set(0, 10, 0);
    ringGroup.scale.set(0.001, 0.001, 0.001);
  }
}

function animate() {
  requestAnimationFrame(animate);
  const time = Date.now() * 0.001;
  if (cardGroup && currentArtifact === 'card') {
    cardGroup.rotation.y += (targetRotationY - cardGroup.rotation.y) * 0.05;
    cardGroup.rotation.x += (targetRotationX - cardGroup.rotation.x) * 0.05;
    cardGroup.position.y = Math.sin(time * 0.8) * 0.06;
  }
  if (ringGroup && currentArtifact === 'ring') {
    ringGroup.rotation.y += 0.008;
    ringGroup.position.y = Math.cos(time * 0.8) * 0.06;
  }
  renderer.render(scene, camera);
}

document.addEventListener('DOMContentLoaded', () => {
  if (typeof THREE !== 'undefined') init3DScene();
});
"""

with open('/Users/ramay/gentech3-app/assets/js/scene3d.js', 'w', encoding='utf-8') as f:
    f.write(scene3d_code)

# 3. Synchronize to WordPress Theme and Rebuild ZIP
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
os.system("cp -r /Users/ramay/gentech3-app/* /Users/ramay/gentech3-lab/")

print("Toolbar simplified to just 2 focused buttons (Akıllı Yüzük & Titanyum Kart)!")
