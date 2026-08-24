import os

print("Building GenTech 3 Next-Gen FinTech Platform...")

# 1. Write audio.js
audio_js = """/**
 * GenTech 3 Audio Synthesis Engine (Web Audio API)
 * Synthesizes ultra-clean tactile, laser, and NFC payment chimes
 */
class AudioEngine {
  constructor() {
    this.ctx = null;
    this.enabled = true;
  }

  init() {
    if (!this.ctx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioContext();
    }
  }

  toggle() {
    this.enabled = !this.enabled;
    return this.enabled;
  }

  playClick() {
    if (!this.enabled) return;
    this.init();
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(800, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(300, this.ctx.currentTime + 0.04);
    gain.gain.setValueAtTime(0.12, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.04);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.04);
  }

  playNfcSuccess() {
    if (!this.enabled) return;
    this.init();
    const now = this.ctx.currentTime;
    
    // Tone 1 (1046 Hz - C6)
    const osc1 = this.ctx.createOscillator();
    const gain1 = this.ctx.createGain();
    osc1.type = 'sine';
    osc1.frequency.setValueAtTime(1046.5, now);
    gain1.gain.setValueAtTime(0.15, now);
    gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
    osc1.connect(gain1);
    gain1.connect(this.ctx.destination);
    osc1.start(now);
    osc1.stop(now + 0.12);

    // Tone 2 (1567 Hz - G6)
    const osc2 = this.ctx.createOscillator();
    const gain2 = this.ctx.createGain();
    osc2.type = 'sine';
    osc2.frequency.setValueAtTime(1567.98, now + 0.08);
    gain2.gain.setValueAtTime(0.18, now + 0.08);
    gain2.gain.exponentialRampToValueAtTime(0.001, now + 0.28);
    osc2.connect(gain2);
    gain2.connect(this.ctx.destination);
    osc2.start(now + 0.08);
    osc2.stop(now + 0.28);
  }

  playLaser() {
    if (!this.enabled) return;
    this.init();
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(2400, this.ctx.currentTime);
    osc.frequency.linearRampToValueAtTime(1200, this.ctx.currentTime + 0.1);
    gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.1);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.1);
  }
}

window.soundFx = new AudioEngine();
"""

with open('/Users/ramay/gentech3-app/assets/js/audio.js', 'w', encoding='utf-8') as f:
    f.write(audio_js)

# 2. Write scene3d.js
scene3d_js = """/**
 * GenTech 3 Ultra 3D WebGL Engine
 * Synchronized Smart Payment Ring & Sovereign Titanium Card 3D Studio
 */

let scene, camera, renderer;
let cardMesh, ringMesh, chipMesh, antennaMesh;
let cardGroup, ringGroup, mainStageGroup;
let pointLight1, pointLight2, spotLight;
let currentMaterial = 'gold';
let isExploded = false;
let activeArtifact = 'both';
let targetRotationX = 0, targetRotationY = 0;

function init3DScene() {
  const container = document.getElementById('canvas3D');
  if (!container) return;

  const width = container.clientWidth;
  const height = container.clientHeight;

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
  camera.position.set(0, 0, 14);

  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.35;
  container.appendChild(renderer.domElement);

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
  scene.add(ambientLight);

  pointLight1 = new THREE.PointLight(0xf6e27a, 3.0, 50);
  pointLight1.position.set(8, 8, 10);
  scene.add(pointLight1);

  pointLight2 = new THREE.PointLight(0x00f0ff, 2.2, 50);
  pointLight2.position.set(-8, -6, 8);
  scene.add(pointLight2);

  spotLight = new THREE.SpotLight(0xffffff, 3.5);
  spotLight.position.set(0, 12, 12);
  spotLight.angle = Math.PI / 4;
  spotLight.penumbra = 0.6;
  scene.add(spotLight);

  // Stage Groups
  mainStageGroup = new THREE.Group();
  scene.add(mainStageGroup);

  cardGroup = new THREE.Group();
  ringGroup = new THREE.Group();
  mainStageGroup.add(cardGroup);
  mainStageGroup.add(ringGroup);

  cardGroup.position.set(-2.2, 0, 0);
  ringGroup.position.set(3.2, 0, 0);

  // Build Card
  const cardGeo = new THREE.BoxGeometry(4.2, 2.7, 0.08);
  const cardMat = createMaterial('gold');
  cardMesh = new THREE.Mesh(cardGeo, cardMat);
  cardGroup.add(cardMesh);

  // EMV Chip
  const chipGeo = new THREE.BoxGeometry(0.75, 0.6, 0.09);
  const chipMat = new THREE.MeshStandardMaterial({
    color: 0xe5c158,
    metalness: 0.95,
    roughness: 0.2,
    emissive: 0x332200
  });
  chipMesh = new THREE.Mesh(chipGeo, chipMat);
  chipMesh.position.set(-1.2, 0.4, 0.01);
  cardGroup.add(chipMesh);

  // NFC Wave
  const waveGeo = new THREE.RingGeometry(0.2, 0.24, 32);
  const waveMat = new THREE.MeshBasicMaterial({ color: 0xf6e27a, side: THREE.DoubleSide });
  antennaMesh = new THREE.Mesh(waveGeo, waveMat);
  antennaMesh.position.set(1.4, 0.7, 0.05);
  cardGroup.add(antennaMesh);

  // Build Ring
  const ringGeo = new THREE.TorusGeometry(1.5, 0.35, 30, 100);
  const ringMat = createMaterial('gold');
  ringMesh = new THREE.Mesh(ringGeo, ringMat);
  ringMesh.rotation.x = Math.PI / 3;
  ringGroup.add(ringMesh);

  // Inner Resonator
  const innerRingGeo = new THREE.TorusGeometry(1.28, 0.05, 16, 80);
  const innerRingMat = new THREE.MeshStandardMaterial({
    color: 0x00f0ff,
    emissive: 0x00f0ff,
    emissiveIntensity: 0.9
  });
  const innerRingMesh = new THREE.Mesh(innerRingGeo, innerRingMat);
  innerRingMesh.rotation.x = Math.PI / 3;
  ringGroup.add(innerRingMesh);

  // Mouse Listener
  window.addEventListener('mousemove', (e) => {
    const rect = container.getBoundingClientRect();
    const x = e.clientX - (rect.left + rect.width / 2);
    const y = e.clientY - (rect.top + rect.height / 2);
    targetRotationY = (x / rect.width) * 0.8;
    targetRotationX = (y / rect.height) * 0.8;
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
  if (type === 'gold') {
    return new THREE.MeshStandardMaterial({ color: 0xd4af37, metalness: 0.94, roughness: 0.14 });
  } else if (type === 'rosegold') {
    return new THREE.MeshStandardMaterial({ color: 0xe0a96d, metalness: 0.9, roughness: 0.16 });
  } else if (type === 'titanium') {
    return new THREE.MeshStandardMaterial({ color: 0xc5cbd3, metalness: 0.96, roughness: 0.22 });
  } else if (type === 'obsidian') {
    return new THREE.MeshStandardMaterial({ color: 0x0a0f18, metalness: 0.85, roughness: 0.2, emissive: 0x020509 });
  }
}

function set3DMaterial(matKey) {
  currentMaterial = matKey;
  const newMat = createMaterial(matKey);
  if (cardMesh) cardMesh.material = newMat;
  if (ringMesh) ringMesh.material = newMat;
  if (matKey === 'rosegold') pointLight1.color.setHex(0xe0a96d);
  else if (matKey === 'gold') pointLight1.color.setHex(0xf6e27a);
  else if (matKey === 'titanium') pointLight1.color.setHex(0xffffff);
  else if (matKey === 'obsidian') pointLight1.color.setHex(0x00f0ff);
}

function toggleExplodedView() {
  isExploded = !isExploded;
  const targetCardZ = isExploded ? 1.2 : 0;
  const targetChipZ = isExploded ? 0.8 : 0.01;
  const targetRingScale = isExploded ? 1.25 : 1.0;

  gsapTransition(cardMesh.position, 'z', targetCardZ);
  gsapTransition(chipMesh.position, 'z', targetChipZ);
  gsapTransition(ringMesh.scale, 'x', targetRingScale);
  gsapTransition(ringMesh.scale, 'y', targetRingScale);
  gsapTransition(ringMesh.scale, 'z', targetRingScale);
}

function gsapTransition(obj, prop, targetVal) {
  let startVal = obj[prop];
  let startTime = performance.now();
  let duration = 600;

  function step(time) {
    let progress = Math.min((time - startTime) / duration, 1);
    let ease = 1 - Math.pow(1 - progress, 3);
    obj[prop] = startVal + (targetVal - startVal) * ease;
    if (progress < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

function setActiveArtifact(artifact) {
  activeArtifact = artifact;
  if (artifact === 'both') {
    gsapTransition(cardGroup.position, 'x', -2.2);
    gsapTransition(cardGroup.scale, 'x', 1);
    gsapTransition(cardGroup.scale, 'y', 1);
    gsapTransition(cardGroup.scale, 'z', 1);

    gsapTransition(ringGroup.position, 'x', 3.2);
    gsapTransition(ringGroup.scale, 'x', 1);
    gsapTransition(ringGroup.scale, 'y', 1);
    gsapTransition(ringGroup.scale, 'z', 1);
  } else if (artifact === 'card') {
    gsapTransition(cardGroup.position, 'x', 0);
    gsapTransition(cardGroup.scale, 'x', 1.3);
    gsapTransition(cardGroup.scale, 'y', 1.3);
    gsapTransition(cardGroup.scale, 'z', 1.3);

    gsapTransition(ringGroup.scale, 'x', 0.001);
    gsapTransition(ringGroup.scale, 'y', 0.001);
    gsapTransition(ringGroup.scale, 'z', 0.001);
  } else if (artifact === 'ring') {
    gsapTransition(ringGroup.position, 'x', 0);
    gsapTransition(ringGroup.scale, 'x', 1.4);
    gsapTransition(ringGroup.scale, 'y', 1.4);
    gsapTransition(ringGroup.scale, 'z', 1.4);

    gsapTransition(cardGroup.scale, 'x', 0.001);
    gsapTransition(cardGroup.scale, 'y', 0.001);
    gsapTransition(cardGroup.scale, 'z', 0.001);
  }
}

function animate() {
  requestAnimationFrame(animate);
  const time = Date.now() * 0.0015;
  if (cardGroup) {
    cardGroup.rotation.y += (targetRotationY - cardGroup.rotation.y) * 0.05;
    cardGroup.rotation.x += (targetRotationX - cardGroup.rotation.x) * 0.05;
    cardGroup.position.y = Math.sin(time) * 0.15;
  }
  if (ringGroup) {
    ringGroup.rotation.y += 0.008;
    ringGroup.rotation.z = Math.cos(time * 0.8) * 0.1;
    ringGroup.position.y = Math.cos(time) * 0.15;
  }
  renderer.render(scene, camera);
}

document.addEventListener('DOMContentLoaded', () => {
  if (typeof THREE !== 'undefined') init3DScene();
});
"""

with open('/Users/ramay/gentech3-app/assets/js/scene3d.js', 'w', encoding='utf-8') as f:
    f.write(scene3d_js)

# 3. Write simulator.js (Interactive NFC Tap Gate Handshake Simulator)
simulator_js = """/**
 * GenTech 3 Interactive NFC Transit & POS Handshake Simulator
 */
document.addEventListener('DOMContentLoaded', () => {
  const tapButtons = document.querySelectorAll('.sim-tap-btn');
  const terminalScreen = document.getElementById('terminalLogScreen');
  const statusLed = document.getElementById('terminalStatusLed');
  const gateStatus = document.getElementById('gateStatusBadge');

  if (!terminalScreen) return;

  function runHandshake(deviceType) {
    window.soundFx?.playClick();
    
    // Clear and start handshake log
    terminalScreen.innerHTML = `
      <div style="color: #64748b;">[00:00:001] ⚡ RF Carrier Detected: 13.56 MHz (ISO 14443 Type A)</div>
      <div style="color: #38bdf8;">[00:00:012] 🔍 Polling Target: ${deviceType.toUpperCase()}</div>
    `;
    statusLed.style.background = '#f59e0b';
    statusLed.style.boxShadow = '0 0 15px #f59e0b';
    gateStatus.innerHTML = 'AUTHENTICATING...';
    gateStatus.style.color = '#f59e0b';

    setTimeout(() => {
      terminalScreen.innerHTML += `
        <div style="color: #c084fc;">[00:00:028] 🛡️ SELECT PPSE (2PAY.SYS.DDF01) -> AID: A0000000031010</div>
        <div style="color: #94a3b8;">[00:00:035] 🔑 GPO Request: Dynamic Crypto Nonce Transmitted</div>
      `;
    }, 180);

    setTimeout(() => {
      window.soundFx?.playNfcSuccess();
      terminalScreen.innerHTML += `
        <div style="color: #10b981; font-weight: bold;">[00:00:042] ✓ ARQC Cryptogram Verified: 0x90 0x00</div>
        <div style="color: #34d399;">[00:00:048] 🟢 LATENCY: 42ms | GATE UNLOCKED | PASSENGER CLEARED</div>
      `;
      statusLed.style.background = '#10b981';
      statusLed.style.boxShadow = '0 0 20px #10b981';
      gateStatus.innerHTML = '✓ CLEARED (42ms)';
      gateStatus.style.color = '#10b981';
    }, 400);
  }

  tapButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const dev = btn.getAttribute('data-device');
      runHandshake(dev);
    });
  });
});
"""

with open('/Users/ramay/gentech3-app/assets/js/simulator.js', 'w', encoding='utf-8') as f:
    f.write(simulator_js)

# 4. Write portal.js (Interactive Bank Client Dashboard)
portal_js = """/**
 * GenTech 3 B2B Bank Client Portal & Issuance Tracker
 */
document.addEventListener('DOMContentLoaded', () => {
  const bankButtons = document.querySelectorAll('.bank-select-btn');
  const institutionName = document.getElementById('portalBankName');
  const batchOrderNumber = document.getElementById('portalBatchNumber');
  const activeVolume = document.getElementById('portalActiveVolume');

  const bankData = {
    enbd: { name: 'Emirates NBD • Private Wealth', batch: 'PO-GT-9482', volume: '50,000 Cards (24K Gold)', progress: '84%' },
    fab: { name: 'First Abu Dhabi Bank (FAB)', batch: 'PO-GT-9921', volume: '100,000 Transit Smart Cards', progress: '92%' },
    sc: { name: 'Standard Chartered UAE', batch: 'PO-GT-8840', volume: '25,000 Apex Smart Rings', progress: '65%' },
    revolut: { name: 'Revolut Middle East Hub', batch: 'PO-GT-7719', volume: '150,000 Super NFC 5G SIMs', progress: '98%' }
  };

  bankButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      window.soundFx?.playClick();
      bankButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const bankKey = btn.getAttribute('data-bank');
      const data = bankData[bankKey];
      if (data) {
        if (institutionName) institutionName.textContent = data.name;
        if (batchOrderNumber) batchOrderNumber.textContent = data.batch;
        if (activeVolume) activeVolume.textContent = data.volume;
      }
    });
  });
});
"""

with open('/Users/ramay/gentech3-app/assets/js/portal.js', 'w', encoding='utf-8') as f:
    f.write(portal_js)

# 5. Write app.js
app_js = """/**
 * GenTech 3 Master Controller
 */
document.addEventListener('DOMContentLoaded', () => {
  // Live Dubai Clock
  function updateDubaiClock() {
    const el = document.getElementById('liveDubaiTime');
    if (!el) return;
    const now = new Date();
    const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
    const dubaiTime = new Date(utc + (3600000 * 4));
    const hours = String(dubaiTime.getHours()).padStart(2, '0');
    const minutes = String(dubaiTime.getMinutes()).padStart(2, '0');
    const seconds = String(dubaiTime.getSeconds()).padStart(2, '0');
    el.textContent = `${hours}:${minutes}:${seconds} GST (Dubai)`;
  }
  updateDubaiClock();
  setInterval(updateDubaiClock, 1000);

  // Sound Toggle Button
  const soundBtn = document.getElementById('soundToggleBtn');
  soundBtn?.addEventListener('click', () => {
    const isMuted = !window.soundFx.toggle();
    soundBtn.innerHTML = isMuted ? '🔇 Sound: OFF' : '🔊 Sound: ON';
    soundBtn.style.color = isMuted ? '#64748b' : '#f59e0b';
  });

  // Artifact Buttons
  const artifactBtns = document.querySelectorAll('.artifact-toggle-btn');
  artifactBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      window.soundFx?.playClick();
      artifactBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const art = btn.getAttribute('data-artifact');
      if (typeof setActiveArtifact === 'function') setActiveArtifact(art);
    });
  });

  // Exploded View Button
  const explodedBtn = document.getElementById('explodedViewBtn');
  explodedBtn?.addEventListener('click', () => {
    window.soundFx?.playClick();
    explodedBtn.classList.toggle('active');
    if (typeof toggleExplodedView === 'function') toggleExplodedView();
  });

  // Swatches
  const swatchBtns = document.querySelectorAll('.swatch-btn');
  swatchBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      window.soundFx?.playClick();
      swatchBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const mat = btn.getAttribute('data-material');
      if (typeof set3DMaterial === 'function') set3DMaterial(mat);
    });
  });

  // Laser Engraving Text
  const input = document.getElementById('engravingTextInput');
  const textDisplay = document.getElementById('liveEngravedText');
  const laserBeam = document.querySelector('.laser-beam');

  input?.addEventListener('input', (e) => {
    const val = e.target.value.toUpperCase() || 'ALEXANDER VANCE';
    if (textDisplay) textDisplay.textContent = val;
    window.soundFx?.playLaser();

    laserBeam?.classList.add('firing');
    clearTimeout(window.laserTimeout);
    window.laserTimeout = setTimeout(() => {
      laserBeam?.classList.remove('firing');
    }, 600);
  });
});
"""

with open('/Users/ramay/gentech3-app/assets/js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("JavaScript modules created!")
