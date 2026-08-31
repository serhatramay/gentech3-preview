/**
 * GenTech 3 - Ultra-Realistic 3D Atelier (Optimized Edition)
 * Dynamic Live 3D Configurator for:
 * 1. Samsung Galaxy Ring (Concave Titanium Smart Ring - Silver, Black, Gold)
 * 2. Sovereign Titanium Card (Stealth Black, Pale Titanium, 24K Gold, Hermes Ceramic)
 */

let scene, camera, renderer;
let cardMesh, ringMeshGroup;
let cardGroup, ringGroup, mainStageGroup;
let hemiLight, keyLight, fillLight, rimLightGold, rimLightHermes;
let targetRotationX = 0.18, targetRotationY = -0.22;
let currentArtifact = 'ring';

// Materials & Finishes
let ringTitaniumMat, ringInnerResinMat, ringPpgLedMat, ringPpgLight;
let currentRingFinish = 'silver';
let cardSideMat, cardFrontMat, cardFrameMat;
let currentCardFinish = 'stealth';
let cardTexturesCache = {};

let is3DInitialized = false;
let isSceneVisible = true;
let animFrameId = null;
let lastFrameTime = 0;
const targetFPS = 36; // 36 FPS is smooth and uses 50% less mobile CPU
const frameInterval = 1000 / targetFPS;

// Generate Optimized Titanium Card Texture on-demand with Dynamic Metal Alloy Finishes
function createCardTexture(finish = 'stealth') {
  if (cardTexturesCache[finish]) return cardTexturesCache[finish];

  const isMobile = typeof window !== 'undefined' && window.innerWidth < 768;
  const w = isMobile ? 1024 : 1400;
  const h = Math.round(w * (1290 / 2048));
  const scale = w / 2048;

  const canvas = document.createElement('canvas');
  canvas.width = w;
  canvas.height = h;
  const ctx = canvas.getContext('2d');
  ctx.scale(scale, scale);

  let textColor = '#ffffff';
  let subColor = '#94a3b8';
  let accentColor = '#eb651a';
  let borderStroke = 'rgba(255, 255, 255, 0.2)';
  let nfcColor = 'rgba(255, 255, 255, 0.45)';

  if (finish === 'stealth') {
    const grad = ctx.createLinearGradient(0, 0, 2048, 1290);
    grad.addColorStop(0.0, '#22262f');
    grad.addColorStop(0.25, '#3b4352');
    grad.addColorStop(0.5, '#262b36');
    grad.addColorStop(0.75, '#475163');
    grad.addColorStop(1.0, '#1a1e26');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 2048, 1290);

    ctx.fillStyle = 'rgba(255, 255, 255, 0.035)';
    for (let i = 0; i < 1290; i += 6) {
      ctx.fillRect(0, i, 2048, 2);
    }
  } else if (finish === 'titanium') {
    const grad = ctx.createLinearGradient(0, 0, 2048, 1290);
    grad.addColorStop(0.0, '#c8d3e0');
    grad.addColorStop(0.3, '#f1f5f9');
    grad.addColorStop(0.6, '#94a3b8');
    grad.addColorStop(1.0, '#e2e8f0');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 2048, 1290);

    ctx.fillStyle = 'rgba(0, 0, 0, 0.04)';
    for (let i = 0; i < 1290; i += 6) {
      ctx.fillRect(0, i, 2048, 2);
    }

    textColor = '#0f172a';
    subColor = '#475569';
    accentColor = '#b45309';
    borderStroke = 'rgba(15, 23, 42, 0.2)';
    nfcColor = 'rgba(15, 23, 42, 0.45)';
  } else if (finish === 'gold') {
    const grad = ctx.createLinearGradient(0, 0, 2048, 1290);
    grad.addColorStop(0.0, '#ca8a04');
    grad.addColorStop(0.25, '#fef08a');
    grad.addColorStop(0.5, '#eab308');
    grad.addColorStop(0.75, '#fef9c3');
    grad.addColorStop(1.0, '#a16207');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 2048, 1290);

    ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
    for (let i = 0; i < 1290; i += 6) {
      ctx.fillRect(0, i, 2048, 2);
    }

    textColor = '#422006';
    subColor = '#713f12';
    accentColor = '#78350f';
    borderStroke = 'rgba(66, 32, 6, 0.25)';
    nfcColor = 'rgba(66, 32, 6, 0.45)';
  } else if (finish === 'ceramic') {
    const grad = ctx.createLinearGradient(0, 0, 2048, 1290);
    grad.addColorStop(0.0, '#ffffff');
    grad.addColorStop(0.3, '#faf2eb');
    grad.addColorStop(0.7, '#fffaf5');
    grad.addColorStop(1.0, '#f5e4d6');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 2048, 1290);

    textColor = '#1a130e';
    subColor = '#6e6056';
    accentColor = '#eb651a';
    borderStroke = 'rgba(235, 101, 26, 0.3)';
    nfcColor = 'rgba(235, 101, 26, 0.5)';
  }

  // Card Outer Chamfer Bevel Stroke
  ctx.strokeStyle = borderStroke;
  ctx.lineWidth = 12;
  ctx.strokeRect(20, 20, 2008, 1250);

  // EMV Microchip Box
  const chipX = 220, chipY = 460, chipW = 280, chipH = 220;
  const chipGrad = ctx.createLinearGradient(chipX, chipY, chipX + chipW, chipY + chipH);
  chipGrad.addColorStop(0.0, '#e5c158');
  chipGrad.addColorStop(0.5, '#bf9526');
  chipGrad.addColorStop(1.0, '#ffd868');
  ctx.fillStyle = chipGrad;
  ctx.beginPath();
  if (ctx.roundRect) {
    ctx.roundRect(chipX, chipY, chipW, chipH, 24);
  } else {
    ctx.rect(chipX, chipY, chipW, chipH);
  }
  ctx.fill();
  ctx.strokeStyle = '#85640e';
  ctx.lineWidth = 6;
  ctx.stroke();

  // Chip Micro-circuit Lines
  ctx.strokeStyle = 'rgba(0, 0, 0, 0.45)';
  ctx.lineWidth = 4;
  ctx.beginPath();
  ctx.moveTo(chipX, chipY + 110); ctx.lineTo(chipX + chipW, chipY + 110);
  ctx.moveTo(chipX + 85, chipY); ctx.lineTo(chipX + 85, chipY + chipH);
  ctx.moveTo(chipX + 195, chipY); ctx.lineTo(chipX + 195, chipY + chipH);
  ctx.arc(chipX + 140, chipY + 110, 30, 0, Math.PI * 2);
  ctx.stroke();

  // Contactless NFC Waves Icon
  ctx.strokeStyle = nfcColor;
  ctx.lineWidth = 8;
  const nfcX = 580, nfcY = 570;
  for (let r = 25; r <= 75; r += 25) {
    ctx.beginPath();
    ctx.arc(nfcX, nfcY, r, -Math.PI * 0.35, Math.PI * 0.35);
    ctx.stroke();
  }

  // Laser Engraved Brand Typography (GENTECH)
  ctx.fillStyle = textColor;
  ctx.font = 'bold 84px "Plus Jakarta Sans", sans-serif';
  ctx.fillText('GENTECH', 1420, 240);

  ctx.fillStyle = accentColor;
  ctx.font = '600 36px "JetBrains Mono", monospace';
  ctx.fillText('SOVEREIGN TITANIUM', 1340, 295);

  // Cardholder Details
  ctx.fillStyle = subColor;
  ctx.font = '600 32px "Plus Jakarta Sans", sans-serif';
  ctx.fillText('CARDHOLDER / PRIVATE CLIENT', 220, 960);

  ctx.fillStyle = textColor;
  ctx.font = 'bold 64px "Plus Jakarta Sans", sans-serif';
  ctx.fillText('ALEXANDER VANCE', 220, 1040);

  // Serial & CC EAL6+ Info
  ctx.fillStyle = subColor;
  ctx.font = '500 38px "JetBrains Mono", monospace';
  ctx.fillText('GT-9482-2026 • CC EAL6+ SECURE ELEMENT', 220, 1140);

  // Holographic Crest Icon
  ctx.strokeStyle = accentColor;
  ctx.lineWidth = 6;
  ctx.strokeRect(1740, 960, 120, 120);
  ctx.fillStyle = accentColor;
  ctx.font = 'bold 36px "JetBrains Mono"';
  ctx.fillText('GT', 1775, 1035);

  const texture = new THREE.CanvasTexture(canvas);
  texture.needsUpdate = true;
  cardTexturesCache[finish] = texture;
  return texture;
}

// Switch 3D Titanium Card Finish Live
function setCardTitaniumFinish(finish) {
  currentCardFinish = finish;
  if (!cardFrontMat || !cardSideMat) return;

  const newTex = createCardTexture(finish);
  cardFrontMat.color.setHex(0xffffff);
  cardFrontMat.map = newTex;
  cardFrontMat.needsUpdate = true;

  if (finish === 'stealth') {
    cardSideMat.color.setHex(0x94a3b8);
    cardSideMat.metalness = 0.95;
    cardSideMat.roughness = 0.2;
    if (cardFrameMat) cardFrameMat.color.setHex(0xeb651a);
  } else if (finish === 'titanium') {
    cardSideMat.color.setHex(0xd0d8e2);
    cardSideMat.metalness = 0.95;
    cardSideMat.roughness = 0.15;
    if (cardFrameMat) cardFrameMat.color.setHex(0x94a3b8);
  } else if (finish === 'gold') {
    cardSideMat.color.setHex(0xca8a04);
    cardSideMat.metalness = 0.98;
    cardSideMat.roughness = 0.1;
    if (cardFrameMat) cardFrameMat.color.setHex(0xffd700);
  } else if (finish === 'ceramic') {
    cardSideMat.color.setHex(0xffffff);
    cardSideMat.metalness = 0.2;
    cardSideMat.roughness = 0.05;
    if (cardFrameMat) cardFrameMat.color.setHex(0xeb651a);
  }
}

/**
 * Build Lightweight authentic Galaxy Ring
 */
function buildGalaxyRing() {
  const ringRoot = new THREE.Group();

  const rEdge = 1.62;
  const rCenter = 1.50;
  const rInner = 1.34;
  const height = 1.12;

  // 1. OUTER CONCAVE TITANIUM CYLINDER (48 segments for high performance)
  const outerGeo = new THREE.CylinderGeometry(rEdge, rEdge, height, 48, 16, true);
  const pos = outerGeo.attributes.position;
  
  for (let i = 0; i < pos.count; i++) {
    const x = pos.getX(i);
    const y = pos.getY(i);
    const z = pos.getZ(i);
    
    const normY = y / (height / 2);
    const dipFactor = Math.cos(normY * Math.PI * 0.5);
    const rCurrent = rEdge - dipFactor * (rEdge - rCenter);
    
    const angle = Math.atan2(z, x);
    pos.setXYZ(i, Math.cos(angle) * rCurrent, y, Math.sin(angle) * rCurrent);
  }
  outerGeo.computeVertexNormals();

  ringTitaniumMat = new THREE.MeshStandardMaterial({
    color: 0xd8dde6,
    metalness: 0.95,
    roughness: 0.22
  });

  const outerShellMesh = new THREE.Mesh(outerGeo, ringTitaniumMat);
  ringRoot.add(outerShellMesh);

  // 2. INNER BIO-RESIN LINER
  const innerGeo = new THREE.CylinderGeometry(rInner, rInner, height - 0.02, 48, 1, true);
  ringInnerResinMat = new THREE.MeshStandardMaterial({
    color: 0x14171d,
    metalness: 0.35,
    roughness: 0.18,
    side: THREE.BackSide
  });
  const innerLinerMesh = new THREE.Mesh(innerGeo, ringInnerResinMat);
  ringRoot.add(innerLinerMesh);

  // 3. TOP & BOTTOM RIMS
  const topRimGeo = new THREE.RingGeometry(rInner, rEdge, 48);
  const topRimMesh = new THREE.Mesh(topRimGeo, ringTitaniumMat);
  topRimMesh.position.y = height / 2;
  topRimMesh.rotation.x = -Math.PI / 2;
  ringRoot.add(topRimMesh);

  const bottomRimGeo = new THREE.RingGeometry(rInner, rEdge, 48);
  const bottomRimMesh = new THREE.Mesh(bottomRimGeo, ringTitaniumMat);
  bottomRimMesh.position.y = -height / 2;
  bottomRimMesh.rotation.x = Math.PI / 2;
  ringRoot.add(bottomRimMesh);

  // 4. SENSOR HUB
  const sensorHub = new THREE.Group();

  const ppgPodGeo = new THREE.BoxGeometry(0.20, 0.42, 0.07);
  const podMat = new THREE.MeshStandardMaterial({ color: 0x0c0e12, metalness: 0.2, roughness: 0.1 });
  const ppgPod = new THREE.Mesh(ppgPodGeo, podMat);
  ppgPod.position.set(0, 0, rInner - 0.025);
  sensorHub.add(ppgPod);

  const ppgLedGeo = new THREE.CylinderGeometry(0.04, 0.04, 0.025, 12);
  ringPpgLedMat = new THREE.MeshStandardMaterial({
    color: 0x00ff88,
    emissive: 0x00ff66,
    emissiveIntensity: 1.5,
    metalness: 0.1,
    roughness: 0.1
  });
  const ppgLed = new THREE.Mesh(ppgLedGeo, ringPpgLedMat);
  ppgLed.rotation.x = Math.PI / 2;
  ppgLed.position.set(0, 0.09, rInner - 0.055);
  sensorHub.add(ppgLed);

  ringPpgLight = new THREE.PointLight(0x00ff88, 1.0, 1.5);
  ringPpgLight.position.set(0, 0.09, rInner - 0.08);
  sensorHub.add(ringPpgLight);

  // Notch
  const notchGeo = new THREE.BoxGeometry(0.035, 0.12, 0.05);
  const notchMat = new THREE.MeshStandardMaterial({ color: 0x64748b, metalness: 0.8, roughness: 0.3 });
  const notch = new THREE.Mesh(notchGeo, notchMat);
  notch.position.set(0, -height / 2 + 0.01, rEdge - 0.01);
  ringRoot.add(notch);

  ringRoot.add(sensorHub);
  ringRoot.rotation.x = Math.PI * 0.28;
  ringRoot.rotation.z = Math.PI * 0.06;

  return ringRoot;
}

// Switch Samsung Galaxy Ring Titanium Finishes
function setRingTitaniumFinish(finish) {
  currentRingFinish = finish;
  if (!ringTitaniumMat) return;

  if (finish === 'silver') {
    ringTitaniumMat.color.setHex(0xd8dde6);
    ringTitaniumMat.metalness = 0.95;
    ringTitaniumMat.roughness = 0.22;
  } else if (finish === 'black') {
    ringTitaniumMat.color.setHex(0x1a1d22);
    ringTitaniumMat.metalness = 0.88;
    ringTitaniumMat.roughness = 0.30;
  } else if (finish === 'gold') {
    ringTitaniumMat.color.setHex(0xd8b88a);
    ringTitaniumMat.metalness = 0.92;
    ringTitaniumMat.roughness = 0.20;
  }
}

function init3DScene() {
  const container = document.getElementById('canvas3D');
  if (!container || !window.THREE) return;

  const width = container.clientWidth || 600;
  const height = container.clientHeight || 500;

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(38, width / height, 0.1, 1000);

  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.35;
  container.innerHTML = '';
  container.appendChild(renderer.domElement);

  // Lights
  hemiLight = new THREE.HemisphereLight(0xffffff, 0xfceee3, 1.35);
  scene.add(hemiLight);

  keyLight = new THREE.DirectionalLight(0xffffff, 2.5);
  keyLight.position.set(8, 10, 12);
  scene.add(keyLight);

  fillLight = new THREE.DirectionalLight(0xffedd5, 1.4);
  fillLight.position.set(-10, -4, 8);
  scene.add(fillLight);

  rimLightGold = new THREE.DirectionalLight(0xd4af37, 2.0);
  rimLightGold.position.set(0, 8, -10);
  scene.add(rimLightGold);

  // Groups
  mainStageGroup = new THREE.Group();
  scene.add(mainStageGroup);

  cardGroup = new THREE.Group();
  ringGroup = new THREE.Group();
  mainStageGroup.add(cardGroup);
  mainStageGroup.add(ringGroup);

  // Card Mesh (Lazy texture loaded when switched)
  const cardGeo = new THREE.BoxGeometry(4.8, 3.03, 0.08);
  cardSideMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.95, roughness: 0.2 });
  cardFrontMat = new THREE.MeshStandardMaterial({
    color: 0xffffff,
    metalness: 0.88,
    roughness: 0.22,
    clearcoat: 0.6,
    clearcoatRoughness: 0.15
  });
  cardFrontMat.map = createCardTexture('stealth');
  
  const cardMaterials = [cardSideMat, cardSideMat, cardSideMat, cardSideMat, cardFrontMat, cardFrontMat];
  cardMesh = new THREE.Mesh(cardGeo, cardMaterials);
  cardGroup.add(cardMesh);

  const frameGeo = new THREE.BoxGeometry(4.82, 3.05, 0.07);
  cardFrameMat = new THREE.MeshStandardMaterial({ color: 0xeb651a, metalness: 0.95, roughness: 0.15 });
  const frameMesh = new THREE.Mesh(frameGeo, cardFrameMat);
  cardGroup.add(frameMesh);

  // Ring Mesh
  ringMeshGroup = buildGalaxyRing();
  ringGroup.add(ringMeshGroup);

  setActiveArtifact('ring');

  // Listeners
  window.addEventListener('mousemove', (e) => {
    const rect = container.getBoundingClientRect();
    const x = e.clientX - (rect.left + rect.width / 2);
    const y = e.clientY - (rect.top + rect.height / 2);
    targetRotationY = (x / rect.width) * 0.65;
    targetRotationX = (y / rect.height) * 0.55;
  }, { passive: true });

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

  window.addEventListener('resize', () => {
    const newW = container.clientWidth;
    const newH = container.clientHeight;
    if (camera && renderer && newW && newH) {
      camera.aspect = newW / newH;
      camera.updateProjectionMatrix();
      renderer.setSize(newW, newH);
      setActiveArtifact(currentArtifact);
    }
  }, { passive: true });

  start3DAnimation();
}

function setActiveArtifact(artifact) {
  currentArtifact = artifact;
  const container = document.getElementById('canvas3D');
  const isMobile = container && (container.clientWidth / container.clientHeight < 0.9);
  const ringFinishBar = document.getElementById('ringFinishSelector');
  const cardFinishBar = document.getElementById('cardFinishSelector');

  if (artifact === 'card') {
    if (cardFrontMat) {
      cardFrontMat.color.setHex(0xffffff);
      cardFrontMat.map = createCardTexture(currentCardFinish || 'stealth');
      cardFrontMat.needsUpdate = true;
    }

    if (camera) camera.position.set(0, 0, isMobile ? 12 : 10.5);
    if (cardGroup) {
      cardGroup.position.set(0, 0, 0);
      cardGroup.scale.set(isMobile ? 1.0 : 1.22, isMobile ? 1.0 : 1.22, isMobile ? 1.0 : 1.22);
    }
    if (ringGroup) {
      ringGroup.position.set(0, 15, 0);
      ringGroup.scale.set(0.001, 0.001, 0.001);
    }

    if (ringFinishBar) ringFinishBar.style.display = 'none';
    if (cardFinishBar) cardFinishBar.style.display = 'flex';
  } else if (artifact === 'ring') {
    if (camera) camera.position.set(0, 0, isMobile ? 11 : 9.5);
    if (ringGroup) {
      ringGroup.position.set(0, 0, 0);
      ringGroup.scale.set(isMobile ? 1.25 : 1.45, isMobile ? 1.25 : 1.45, isMobile ? 1.25 : 1.45);
    }
    if (cardGroup) {
      cardGroup.position.set(0, -15, 0);
      cardGroup.scale.set(0.001, 0.001, 0.001);
    }

    if (ringFinishBar) ringFinishBar.style.display = 'flex';
    if (cardFinishBar) cardFinishBar.style.display = 'none';
  }
}

function start3DAnimation() {
  if (!animFrameId) {
    animFrameId = requestAnimationFrame(animate);
  }
}

function stop3DAnimation() {
  if (animFrameId) {
    cancelAnimationFrame(animFrameId);
    animFrameId = null;
  }
}

function animate(now) {
  animFrameId = requestAnimationFrame(animate);

  if (!isSceneVisible || !renderer || !scene || !camera) return;

  // Frame limiter for mobile efficiency
  if (now && now - lastFrameTime < frameInterval) return;
  lastFrameTime = now || 0;

  const time = (now || Date.now()) * 0.001;

  if (cardGroup && currentArtifact === 'card') {
    cardGroup.rotation.y += (targetRotationY - cardGroup.rotation.y) * 0.06;
    cardGroup.rotation.x += (targetRotationX - cardGroup.rotation.x) * 0.06;
    cardGroup.position.y = Math.sin(time * 0.7) * 0.07;
  }

  if (ringGroup && currentArtifact === 'ring') {
    ringGroup.rotation.y += 0.009;
    ringGroup.rotation.x += (targetRotationX * 0.5 - ringGroup.rotation.x) * 0.04;
    ringGroup.position.y = Math.cos(time * 0.7) * 0.06;

    const heartPulse = (Math.sin(time * 4.8) + 1) * 0.5;
    if (ringPpgLedMat) {
      ringPpgLedMat.emissiveIntensity = 1.0 + heartPulse * 1.6;
    }
    if (ringPpgLight) {
      ringPpgLight.intensity = 0.6 + heartPulse * 1.0;
    }
  }

  renderer.render(scene, camera);
}

// Scheduled Non-Blocking 3D Engine Setup
function schedule3DInit() {
  const container = document.getElementById('canvas3D');
  if (!container || is3DInitialized) return;

  const runInit = () => {
    if (is3DInitialized) return;
    is3DInitialized = true;
    if (typeof THREE !== 'undefined') {
      init3DScene();
    } else {
      let retries = 0;
      const checkThree = setInterval(() => {
        if (typeof THREE !== 'undefined') {
          clearInterval(checkThree);
          init3DScene();
        } else if (++retries > 25) {
          clearInterval(checkThree);
        }
      }, 100);
    }
  };

  // IntersectionObserver to pause rendering when offscreen
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        isSceneVisible = entry.isIntersecting;
        if (entry.isIntersecting) {
          start3DAnimation();
        } else {
          stop3DAnimation();
        }
      });
    }, { threshold: 0.05 });
    observer.observe(container);
  }

  // Defer 3D load until browser has finished first paint & idle
  if ('requestIdleCallback' in window) {
    requestIdleCallback(() => {
      setTimeout(runInit, 300);
    }, { timeout: 1500 });
  } else {
    setTimeout(runInit, 500);
  }

  // Also initialize immediately on user interaction
  const triggerInstantly = () => {
    window.removeEventListener('scroll', triggerInstantly);
    window.removeEventListener('touchstart', triggerInstantly);
    window.removeEventListener('click', triggerInstantly);
    runInit();
  };
  window.addEventListener('scroll', triggerInstantly, { passive: true, once: true });
  window.addEventListener('touchstart', triggerInstantly, { passive: true, once: true });
  window.addEventListener('click', triggerInstantly, { passive: true, once: true });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', schedule3DInit);
} else {
  schedule3DInit();
}
