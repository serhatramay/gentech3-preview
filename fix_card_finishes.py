import re

# 1. Update scene3d.js
scene3d_path = "/Users/ramay/gentech3-app/assets/js/scene3d.js"
with open(scene3d_path, "r", encoding="utf-8") as f:
    js = f.read()

# Fix init3DScene cardFrontMat color
old_mat_init = """  cardFrontMat = new THREE.MeshStandardMaterial({
    color: 0x22262f,
    metalness: 0.88,
    roughness: 0.22,
    clearcoat: 0.6,
    clearcoatRoughness: 0.15
  });"""

new_mat_init = """  cardFrontMat = new THREE.MeshStandardMaterial({
    color: 0xffffff,
    metalness: 0.88,
    roughness: 0.22,
    clearcoat: 0.6,
    clearcoatRoughness: 0.15
  });
  cardFrontMat.map = createCardTexture('stealth');"""

js = js.replace(old_mat_init, new_mat_init)

# Fix setCardTitaniumFinish
old_finish_func = """function setCardTitaniumFinish(finish) {
  currentCardFinish = finish;
  if (!cardFrontMat || !cardSideMat) return;

  const newTex = createCardTexture(finish);
  cardFrontMat.map = newTex;
  cardFrontMat.needsUpdate = true;"""

new_finish_func = """function setCardTitaniumFinish(finish) {
  currentCardFinish = finish;
  if (!cardFrontMat || !cardSideMat) return;

  const newTex = createCardTexture(finish);
  cardFrontMat.color.setHex(0xffffff);
  cardFrontMat.map = newTex;
  cardFrontMat.needsUpdate = true;"""

js = js.replace(old_finish_func, new_finish_func)

# Fix setActiveArtifact
old_active_artifact = """    if (cardFrontMat && !cardFrontMat.map) {
      cardFrontMat.map = createCardTexture(currentCardFinish || 'stealth');
      cardFrontMat.needsUpdate = true;
    }"""

new_active_artifact = """    if (cardFrontMat) {
      cardFrontMat.color.setHex(0xffffff);
      cardFrontMat.map = createCardTexture(currentCardFinish || 'stealth');
      cardFrontMat.needsUpdate = true;
    }"""

js = js.replace(old_active_artifact, new_active_artifact)

with open(scene3d_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Updated scene3d.js with pure-white base color and dynamic canvas texture mapping.")

# 2. Update generate_pages_master.py to use exactly 3 card finish buttons (removing ceramic)
master_path = "/Users/ramay/gentech3-app/generate_pages_master.py"
with open(master_path, "r", encoding="utf-8") as f:
    master_code = f.read()

# Remove ceramic button from cardFinishSelector
master_code = master_code.replace(
    '<button class="finish-pill-btn card-finish-btn" data-card-finish="ceramic" aria-label="Hermes Ceramic finish">Ceramic</button>',
    ''
)
master_code = master_code.replace(
    '<button class="finish-pill-btn card-finish-btn" data-card-finish="ceramic">Ceramic</button>',
    ''
)

with open(master_path, "w", encoding="utf-8") as f:
    f.write(master_code)

print("Updated generate_pages_master.py (3 card finishes).")

