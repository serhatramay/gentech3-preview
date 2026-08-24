/**
 * GenTech 3 - Ultra-Realistic 3D Atelier
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

// Generate High-Res 2048x1280 Titanium Card Texture with Dynamic Metal Alloy Finishes
function createCardTexture(finish = 'stealth') {
  const canvas = document.createElement('canvas');
  canvas.width = 2048;
  canvas.height = 1290;
  const ctx = canvas.getContext('2d');

  let textColor = '#ffffff';
  let subColor = '#94a3b8';
  let accentColor = '#eb651a';
  let borderStroke = 'rgba(255, 255, 255, 0.2)';
  let nfcColor = 'rgba(255, 255, 255, 0.45)';

  if (finish === 'stealth') {
    // 1. Stealth Dark Brushed Titanium
    const grad = ctx.createLinearGradient(0, 0, 2048, 1290);
    grad.addColorStop(0.0, '#22262f');
    grad.addColorStop(0.25, '#3b4352');
    grad.addColorStop(0.5, '#262b36');
    grad.addColorStop(0.75, '#475163');
    grad.addColorStop(1.0, '#1a1e26');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 2048, 1290);

    ctx.fillStyle = 'rgba(255, 255, 255, 0.035)';
    for (let i = 0; i < 1290; i += 3) {
      if (Math.random() > 0.4) ctx.fillRect(0, i, 2048, 1.5);
    }
  } else if (finish === 'titanium') {
    // 2. Pale Silver Natural Titanium
    const grad = ctx.createLinearGradient(0, 0, 2048, 1290);
    grad.addColorStop(0.0, '#c8d3e0');
    grad.addColorStop(0.3, '#f1f5f9');
    grad.addColorStop(0.6, '#94a3b8');
    grad.addColorStop(1.0, '#e2e8f0');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 2048, 1290);

    ctx.fillStyle = 'rgba(0, 0, 0, 0.04)';
    for (let i = 0; i < 1290; i += 3) {
      if (Math.random() > 0.4) ctx.fillRect(0, i, 2048, 1.5);
    }

    textColor = '#0f172a';
    subColor = '#475569';
    accentColor = '#b45309';
    borderStroke = 'rgba(15, 23, 42, 0.2)';
    nfcColor = 'rgba(15, 23, 42, 0.45)';
  } else if (finish === 'gold') {
    // 3. 24K Mirror Champagne Gold
    const grad = ctx.createLinearGradient(0, 0, 2048, 1290);
    grad.addColorStop(0.0, '#ca8a04');
    grad.addColorStop(0.25, '#fef08a');
    grad.addColorStop(0.5, '#eab308');
    grad.addColorStop(0.75, '#fef9c3');
    grad.addColorStop(1.0, '#a16207');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 2048, 1290);

    ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
    for (let i = 0; i < 1290; i += 3) {
      if (Math.random() > 0.4) ctx.fillRect(0, i, 2048, 1.5);
    }

    textColor = '#422006';
    subColor = '#713f12';
    accentColor = '#78350f';
    borderStroke = 'rgba(66, 32, 6, 0.25)';
    nfcColor = 'rgba(66, 32, 6, 0.45)';
  } else if (finish === 'ceramic') {
    // 4. Hermes Alabaster Ceramic
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
  ctx.roundRect(chipX, chipY, chipW, chipH, 24);
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
  ctx.letterSpacing = '8px';
  ctx.fillText('GENTECH', 1420, 240);

  ctx.fillStyle = accentColor;
  ctx.font = '600 36px "JetBrains Mono", monospace';
  ctx.letterSpacing = '4px';
  ctx.fillText('SOVEREIGN TITANIUM', 1340, 295);

  // Cardholder Details
  ctx.fillStyle = subColor;
  ctx.font = '600 32px "Plus Jakarta Sans", sans-serif';
  ctx.letterSpacing = '4px';
  ctx.fillText('CARDHOLDER / PRIVATE CLIENT', 220, 960);

  ctx.fillStyle = textColor;
  ctx.font = 'bold 64px "Plus Jakarta Sans", sans-serif';
  ctx.letterSpacing = '8px';
  ctx.fillText('ALEXANDER VANCE', 220, 1040);

  // Serial & CC EAL6+ Info
  ctx.fillStyle = subColor;
  ctx.font = '500 38px "JetBrains Mono", monospace';
  ctx.letterSpacing = '6px';
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
  return texture;
}

// Switch 3D Titanium Card Finish Live
function setCardTitaniumFinish(finish) {
  currentCardFinish = finish;
  if (!cardFrontMat || !cardSideMat) return;

  const newTex = createCardTexture(finish);
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
 * Build 100% Authentic Samsung Galaxy Ring 3D Architecture
 */
function buildGalaxyRing() {
  const ringRoot = new THREE.Group();

  const rEdge = 1.62;   // Outer flared rim radius
  const rCenter = 1.50; // Inward concave dip radius (Galaxy Ring signature)
  const rInner = 1.34;  // Inner finger band radius
  const height = 1.12;  // Band height/width

  // 1. OUTER CONCAVE TITANIUM CYLINDER
  const outerGeo = new THREE.CylinderGeometry(rEdge, rEdge, height, 96, 32, true);
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

  // Grade 5 Titanium Shell Material
  ringTitaniumMat = new THREE.MeshStandardMaterial({
    color: 0xd8dde6, // Titanium Silver default
    metalness: 0.95,
    roughness: 0.22,
    envMapIntensity: 1.6
  });

  const outerShellMesh = new THREE.Mesh(outerGeo, ringTitaniumMat);
  ringRoot.add(outerShellMesh);

  // 2. INNER TRANSLUCENT BIO-RESIN LINER
  const innerGeo = new THREE.CylinderGeometry(rInner, rInner, height - 0.02, 96, 1, true);
  ringInnerResinMat = new THREE.MeshStandardMaterial({
    color: 0x14171d,
    metalness: 0.35,
    roughness: 0.18,
    side: THREE.BackSide
  });
  const innerLinerMesh = new THREE.Mesh(innerGeo, ringInnerResinMat);
  ringRoot.add(innerLinerMesh);

  // 3. TOP & BOTTOM BEVELED RIM RINGS
  const topRimGeo = new THREE.RingGeometry(rInner, rEdge, 96);
  const topRimMesh = new THREE.Mesh(topRimGeo, ringTitaniumMat);
  topRimMesh.position.y = height / 2;
  topRimMesh.rotation.x = -Math.PI / 2;
  ringRoot.add(topRimMesh);

  const bottomRimGeo = new THREE.RingGeometry(rInner, rEdge, 96);
  const bottomRimMesh = new THREE.Mesh(bottomRimGeo, ringTitaniumMat);
  bottomRimMesh.position.y = -height / 2;
  bottomRimMesh.rotation.x = Math.PI / 2;
  ringRoot.add(bottomRimMesh);

  // 4. SAMSUNG BIOACTIVE SENSOR HUB: 3 Raised Inner Sensor Modules
  const sensorHub = new THREE.Group();

  // A. Center Sensor Module: BioActive Optical PPG Hub (Angle = 0°)
  const ppgPodGeo = new THREE.BoxGeometry(0.20, 0.42, 0.07);
  const podMat = new THREE.MeshStandardMaterial({
    color: 0x0c0e12,
    metalness: 0.2,
    roughness: 0.1
  });
  const ppgPod = new THREE.Mesh(ppgPodGeo, podMat);
  ppgPod.position.set(0, 0, rInner - 0.025);
  sensorHub.add(ppgPod);

  // Green Optical PPG Emitter Diode (Pulsing Bioluminescent LED)
  const ppgLedGeo = new THREE.CylinderGeometry(0.04, 0.04, 0.025, 16);
  ringPpgLedMat = new THREE.MeshStandardMaterial({
    color: 0x00ff88,
    emissive: 0x00ff66,
    emissiveIntensity: 1.8,
    metalness: 0.1,
    roughness: 0.1
  });
  const ppgLed = new THREE.Mesh(ppgLedGeo, ringPpgLedMat);
  ppgLed.rotation.x = Math.PI / 2;
  ppgLed.position.set(0, 0.09, rInner - 0.055);
  sensorHub.add(ppgLed);

  // Infrared / Red Optical Sensor Lens
  const irLensGeo = new THREE.CylinderGeometry(0.04, 0.04, 0.025, 16);
  const irLensMat = new THREE.MeshStandardMaterial({
    color: 0x330000,
    emissive: 0x880000,
    emissiveIntensity: 0.6,
    metalness: 0.2,
    roughness: 0.1
  });
  const irLens = new THREE.Mesh(irLensGeo, irLensMat);
  irLens.rotation.x = Math.PI / 2;
  irLens.position.set(0, -0.09, rInner - 0.055);
  sensorHub.add(irLens);

  // Point Light for Heartbeat Glow
  ringPpgLight = new THREE.PointLight(0x00ff88, 1.2, 1.6);
  ringPpgLight.position.set(0, 0.09, rInner - 0.08);
  sensorHub.add(ringPpgLight);

  // B. Sensor 2: Skin Temperature Sensor Disc (Angle = +42°)
  const angle2 = Math.PI * 0.23;
  const tempSensorGeo = new THREE.CylinderGeometry(0.075, 0.075, 0.05, 24);
  const tempSensorMat = new THREE.MeshStandardMaterial({
    color: 0xd0d8e2,
    metalness: 0.95,
    roughness: 0.12
  });
  const tempSensor = new THREE.Mesh(tempSensorGeo, tempSensorMat);
  tempSensor.rotation.x = Math.PI / 2;
  tempSensor.position.set(Math.sin(angle2) * (rInner - 0.02), 0, Math.cos(angle2) * (rInner - 0.02));
  tempSensor.rotation.y = angle2;
  sensorHub.add(tempSensor);

  // C. Sensor 3: 3D Motion / Sleep Tracking Hub (Angle = -42°)
  const angle3 = -Math.PI * 0.23;
  const motionPodGeo = new THREE.BoxGeometry(0.16, 0.32, 0.06);
  const motionPod = new THREE.Mesh(motionPodGeo, podMat);
  motionPod.position.set(Math.sin(angle3) * (rInner - 0.02), 0, Math.cos(angle3) * (rInner - 0.02));
  motionPod.rotation.y = angle3;
  sensorHub.add(motionPod);

  // D. Dual 24K Gold Magnetic Pogo Charging Pins (Angle = +80°)
  const pinAngle = Math.PI * 0.44;
  const pinGeo = new THREE.CylinderGeometry(0.024, 0.024, 0.04, 16);
  const pinMat = new THREE.MeshStandardMaterial({
    color: 0xffd700,
    metalness: 0.98,
    roughness: 0.1
  });

  const pin1 = new THREE.Mesh(pinGeo, pinMat);
  pin1.rotation.x = Math.PI / 2;
  pin1.position.set(Math.sin(pinAngle) * (rInner - 0.015), 0.11, Math.cos(pinAngle) * (rInner - 0.015));
  pin1.rotation.y = pinAngle;
  sensorHub.add(pin1);

  const pin2 = new THREE.Mesh(pinGeo, pinMat);
  pin2.rotation.x = Math.PI / 2;
  pin2.position.set(Math.sin(pinAngle) * (rInner - 0.015), -0.11, Math.cos(pinAngle) * (rInner - 0.015));
  pin2.rotation.y = pinAngle;
  sensorHub.add(pin2);

  // 5. Orientation Alignment Notch (Bottom Outer Lip)
  const notchGeo = new THREE.BoxGeometry(0.035, 0.12, 0.05);
  const notchMat = new THREE.MeshStandardMaterial({
    color: 0x64748b,
    metalness: 0.8,
    roughness: 0.3
  });
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

  // 1. Ambient & Warm Light
  hemiLight = new THREE.HemisphereLight(0xffffff, 0xfceee3, 1.35);
  scene.add(hemiLight);

  // 2. Key Light
  keyLight = new THREE.DirectionalLight(0xffffff, 2.9);
  keyLight.position.set(8, 10, 12);
  scene.add(keyLight);

  // 3. Fill Light
  fillLight = new THREE.DirectionalLight(0xffedd5, 1.6);
  fillLight.position.set(-10, -4, 8);
  scene.add(fillLight);

  // 4. Gold & Hermes Rim Glints
  rimLightGold = new THREE.DirectionalLight(0xd4af37, 2.2);
  rimLightGold.position.set(0, 8, -10);
  scene.add(rimLightGold);

  rimLightHermes = new THREE.DirectionalLight(0xeb651a, 1.4);
  rimLightHermes.position.set(-8, 6, -8);
  scene.add(rimLightHermes);

  // 5. Stage Groups
  mainStageGroup = new THREE.Group();
  scene.add(mainStageGroup);

  cardGroup = new THREE.Group();
  ringGroup = new THREE.Group();
  mainStageGroup.add(cardGroup);
  mainStageGroup.add(ringGroup);

  // --- TITANIUM CARD MESH ---
  const cardTexture = createCardTexture('stealth');
  const cardGeo = new THREE.BoxGeometry(4.8, 3.03, 0.08);
  
  cardSideMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.95, roughness: 0.2 });
  cardFrontMat = new THREE.MeshStandardMaterial({
    map: cardTexture,
    metalness: 0.88,
    roughness: 0.22,
    clearcoat: 0.6,
    clearcoatRoughness: 0.15
  });
  
  const cardMaterials = [cardSideMat, cardSideMat, cardSideMat, cardSideMat, cardFrontMat, cardFrontMat];
  cardMesh = new THREE.Mesh(cardGeo, cardMaterials);
  cardGroup.add(cardMesh);

  const frameGeo = new THREE.BoxGeometry(4.82, 3.05, 0.07);
  cardFrameMat = new THREE.MeshStandardMaterial({ color: 0xeb651a, metalness: 0.95, roughness: 0.15 });
  const frameMesh = new THREE.Mesh(frameGeo, cardFrameMat);
  cardGroup.add(frameMesh);

  // --- SAMSUNG GALAXY RING MESH GROUP ---
  ringMeshGroup = buildGalaxyRing();
  ringGroup.add(ringMeshGroup);

  // Set default active view to Galaxy Smart Ring
  setActiveArtifact('ring');

  // Mouse / Pointer Listener
  window.addEventListener('mousemove', (e) => {
    const rect = container.getBoundingClientRect();
    const x = e.clientX - (rect.left + rect.width / 2);
    const y = e.clientY - (rect.top + rect.height / 2);
    targetRotationY = (x / rect.width) * 0.65;
    targetRotationX = (y / rect.height) * 0.55;
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
  const ringFinishBar = document.getElementById('ringFinishSelector');
  const cardFinishBar = document.getElementById('cardFinishSelector');

  if (artifact === 'card') {
    camera.position.set(0, 0, isMobile ? 12 : 10.5);
    cardGroup.position.set(0, 0, 0);
    cardGroup.scale.set(isMobile ? 1.0 : 1.22, isMobile ? 1.0 : 1.22, isMobile ? 1.0 : 1.22);

    ringGroup.position.set(0, 15, 0);
    ringGroup.scale.set(0.001, 0.001, 0.001);

    if (ringFinishBar) ringFinishBar.style.display = 'none';
    if (cardFinishBar) cardFinishBar.style.display = 'flex';
  } else if (artifact === 'ring') {
    camera.position.set(0, 0, isMobile ? 11 : 9.5);
    ringGroup.position.set(0, 0, 0);
    ringGroup.scale.set(isMobile ? 1.25 : 1.45, isMobile ? 1.25 : 1.45, isMobile ? 1.25 : 1.45);

    cardGroup.position.set(0, -15, 0);
    cardGroup.scale.set(0.001, 0.001, 0.001);

    if (ringFinishBar) ringFinishBar.style.display = 'flex';
    if (cardFinishBar) cardFinishBar.style.display = 'none';
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
    ringGroup.rotation.y += 0.009;
    ringGroup.rotation.x += (targetRotationX * 0.5 - ringGroup.rotation.x) * 0.04;
    ringGroup.position.y = Math.cos(time * 0.7) * 0.06;

    // Rhythmic optical PPG sensor heartbeat pulse
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

document.addEventListener('DOMContentLoaded', () => {
  if (typeof THREE !== 'undefined') init3DScene();
});
