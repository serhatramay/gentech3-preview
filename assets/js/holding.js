'use strict';
(() => {
  const nav = document.querySelector('.g-nav');
  const toggle = document.querySelector('.g-menu-toggle');
  const closeMenu = () => { nav?.classList.remove('g-open'); toggle?.setAttribute('aria-expanded', 'false'); };
  toggle?.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('g-open', open);
  });
  document.querySelectorAll('.g-nav details').forEach(detail => {
    detail.addEventListener('toggle', () => {
      if (detail.open) document.querySelectorAll('.g-nav details').forEach(other => { if (other !== detail) other.open = false; });
    });
  });
  document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    const open = document.querySelector('.g-nav details[open]');
    if (open) { open.open = false; open.querySelector('summary').focus(); }
    else if (toggle?.getAttribute('aria-expanded') === 'true') { closeMenu(); toggle.focus(); }
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.g-header')) { closeMenu(); document.querySelectorAll('.g-nav details').forEach(d => { d.open = false; }); }
  });
  nav?.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
  window.matchMedia('(min-width:1001px)').addEventListener('change', closeMenu);

  const select = (buttons, selected) => buttons.forEach(b => { b.classList.toggle('active', b === selected); b.setAttribute('aria-pressed', String(b === selected)); });
  const artifactButtons = [...document.querySelectorAll('[data-artifact]')];
  artifactButtons.forEach(button => button.addEventListener('click', () => {
    const artifact = button.dataset.artifact;
    select(artifactButtons, button);
    document.getElementById('ringShowcaseStage').classList.toggle('hidden', artifact !== 'ring');
    document.getElementById('ringFinishSelector').classList.toggle('hidden', artifact !== 'ring');
    document.getElementById('cardFinishSelector').classList.toggle('hidden', artifact !== 'card');
    if (typeof setActiveArtifact === 'function') setActiveArtifact(artifact);
  }));
  const ringButtons = [...document.querySelectorAll('[data-finish]')];
  ringButtons.forEach(button => button.addEventListener('click', () => {
    select(ringButtons, button);
    const image = document.getElementById('ringHeroImg');
    image.src = `assets/images/smart_ring_${button.dataset.finish}.webp`;
    image.alt = `Illustrative exploded wearable design in a ${button.dataset.finish} finish`;
  }));
  const cardButtons = [...document.querySelectorAll('[data-card-finish]')];
  cardButtons.forEach(button => button.addEventListener('click', () => {
    select(cardButtons, button);
    if (typeof setCardTitaniumFinish === 'function') setCardTitaniumFinish(button.dataset.cardFinish);
  }));
  const stage = document.getElementById('ringShowcaseStage');
  const ring = document.getElementById('ringInteractiveWrapper');
  if (stage && !window.matchMedia('(prefers-reduced-motion:reduce)').matches) {
    stage.addEventListener('pointermove', event => {
      if (event.pointerType !== 'mouse') return;
      const rect = stage.getBoundingClientRect();
      ring.style.transform = `rotateX(${-(event.clientY-rect.top-rect.height/2)/35}deg) rotateY(${(event.clientX-rect.left-rect.width/2)/35}deg)`;
    });
    stage.addEventListener('pointerleave', () => { ring.style.transform = ''; });
  }
  const name = document.getElementById('cardName');
  const reference = document.getElementById('cardReference');
  const design = document.getElementById('designCard');
  let material = 'titanium';
  const updateDesign = () => {
    if (!design) return;
    document.getElementById('designName').textContent = (name.value.trim() || 'YOUR NAME').toUpperCase();
    document.getElementById('designReference').textContent = reference.value.trim() || 'GT-2026-001';
    const params = new URLSearchParams({dept:'cards', design:`Material: ${material}; Name: ${name.value.trim() || 'Not specified'}; Reference: ${reference.value.trim() || 'GT-2026-001'}`});
    document.getElementById('sampleRequest').href = `contact.html?${params}`;
  };
  name?.addEventListener('input', updateDesign);
  reference?.addEventListener('input', updateDesign);
  document.querySelectorAll('[data-material]').forEach(button => button.addEventListener('click', () => {
    material = button.dataset.material;
    design.dataset.material = material;
    document.querySelectorAll('[data-material]').forEach(b => { b.classList.toggle('selected', b === button); b.setAttribute('aria-pressed', String(b === button)); });
    updateDesign();
  }));

  const form = document.getElementById('enquiryForm');
  if (form) {
    const params = new URLSearchParams(location.search);
    const department = document.getElementById('department');
    if ([...department.options].some(o => o.value === params.get('dept'))) department.value = params.get('dept');
    const detail = params.get('design');
    if (detail && department.value === 'cards') document.getElementById('message').value = `I would like to discuss a sample.\n\n${detail.slice(0,500)}`;
    const result = document.getElementById('enquiryResult');
    // A changed field invalidates the previously prepared draft, including withdrawn consent.
    form.addEventListener('input', () => { result.hidden = true; document.getElementById('emailDraft').removeAttribute('href'); document.getElementById('draftText').value = ''; });
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const fields = new FormData(form);
      const topic = department.options[department.selectedIndex].text;
      const subject = `Gentech enquiry — ${topic}`;
      const body = `Name: ${fields.get('name')}\nEmail: ${fields.get('email')}\nCompany: ${fields.get('company') || 'Not provided'}\nTopic: ${topic}\n\n${fields.get('message')}\n\nThe sender has read the website privacy notice and agrees to a response to this enquiry.`;
      document.getElementById('emailDraft').href = `mailto:info@gentech.ae?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      document.getElementById('draftText').value = `To: info@gentech.ae\nSubject: ${subject}\n\n${body}`;
      result.hidden = false;
      result.scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion:reduce)').matches ? 'instant' : 'smooth',block:'nearest'});
    });
  }
})();
