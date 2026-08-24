/**
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

  // Ring Titanium Finish Selector (Silver, Black, Gold)
  const ringFinishBtns = document.querySelectorAll('.ring-finish-btn');
  ringFinishBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      ringFinishBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const finish = btn.getAttribute('data-finish');
      if (typeof setRingTitaniumFinish === 'function') setRingTitaniumFinish(finish);
    });
  });

  // 3D Card Finish Selector (Stealth Black, Pale Titanium, Gold, Ceramic)
  const cardFinishBtns = document.querySelectorAll('.card-finish-btn');
  cardFinishBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      cardFinishBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cardFinish = btn.getAttribute('data-card-finish');
      if (typeof setCardTitaniumFinish === 'function') setCardTitaniumFinish(cardFinish);
    });
  });

  // Live Card Configurator (Section 2)
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
