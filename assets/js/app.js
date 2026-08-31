/**
 * GenTech 3 Master Controller
 * Handles 3D toggles, live configurator, category filtering, and technical modal dialogs
 */

document.addEventListener('DOMContentLoaded', () => {

  // Mobile Hamburger Menu Toggle
  const mobileToggle = document.getElementById('mobileMenuToggle');
  const mobileDrawer = document.getElementById('mobileNavDrawer');
  const mobileClose = document.getElementById('mobileNavClose');

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      mobileDrawer.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  }

  if (mobileClose && mobileDrawer) {
    mobileClose.addEventListener('click', () => {
      mobileDrawer.classList.remove('open');
      document.body.style.overflow = '';
    });
  }

  // 1. 3D Artifact Toggle (Ring & Card)
  const artifactBtns = document.querySelectorAll('.artifact-toggle-btn');
  const ringFinishSelector = document.getElementById('ringFinishSelector');
  const cardFinishSelector = document.getElementById('cardFinishSelector');

  artifactBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      artifactBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const art = btn.getAttribute('data-artifact');
      
      if (art === 'ring') {
        if (ringFinishSelector) ringFinishSelector.classList.remove('hidden');
        if (cardFinishSelector) cardFinishSelector.classList.add('hidden');
      } else {
        if (ringFinishSelector) ringFinishSelector.classList.add('hidden');
        if (cardFinishSelector) cardFinishSelector.classList.remove('hidden');
      }
      
      if (typeof setActiveArtifact === 'function') setActiveArtifact(art);
    });
  });

  // 2. Ring Titanium Finish Selector (Silver, Black, Gold)
  const ringFinishBtns = document.querySelectorAll('.ring-finish-btn');
  ringFinishBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      ringFinishBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const finish = btn.getAttribute('data-finish');
      if (typeof setRingTitaniumFinish === 'function') setRingTitaniumFinish(finish);
    });
  });

  // 3. 3D Card Finish Selector (Stealth Black, Pale Titanium, Gold, Ceramic)
  const cardFinishBtns = document.querySelectorAll('.card-finish-btn');
  cardFinishBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      cardFinishBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cardFinish = btn.getAttribute('data-card-finish');
      if (typeof setCardTitaniumFinish === 'function') setCardTitaniumFinish(cardFinish);
    });
  });

  // 4. Live Card Configurator (Section 6)
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

  // 5. Product Category Filter Tabs
  const filterBtns = document.querySelectorAll('.filter-btn');
  const productCards = document.querySelectorAll('.product-item-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.getAttribute('data-filter');

      productCards.forEach(card => {
        const cat = card.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // 6. Service Technical Specs Modal System
  const modalBackdrop = document.getElementById('modalBackdrop');
  const modalContent = document.getElementById('modalContent');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const detailModalBtns = document.querySelectorAll('.btn-detail-modal');

  const serviceSpecsData = {
    'modal-service-emv': {
      title: 'Smart & EMV Cards Technical Specification',
      tag: 'Core Banking Standard',
      desc: 'PVC (Polyvinyl Chloride) is the most widely used card printing material globally for bank cards (credit/debit), government ID, and transit cards. GenTech provides standard PVC alongside certified eco-friendly alternatives to meet sustainability demands.',
      details: `
        <table class="modal-specs-table">
          <tr><th>Material Substrates</th><td>Standard PVC, Recycled PVC (rPVC), Bioplastic (PLA from corn/sugarcane), Ocean Plastic, Polycarbonate (PC)</td></tr>
          <tr><th>Layer Structure</th><td>Laminated multi-layer core with transparent protective overlays</td></tr>
          <tr><th>Network Certification</th><td>Visa, Mastercard, Discover, UnionPay</td></tr>
          <tr><th>Security Elements</th><td>CC EAL6+ Certified Cryptographic Secure Element</td></tr>
          <tr><th>Shell Foil Technology</th><td>3D noble grain surface, multi-color iridescent reflective shell foils</td></tr>
          <tr><th>ISO Standards</th><td>ISO/IEC 7810, ISO/IEC 7811, ISO/IEC 7813, CQM Reliability Tested</td></tr>
        </table>
        <p><strong>Shell Foil Decorative Technology:</strong> Shell Foil is composed of specially arranged PVC elements creating a vibrant, three-dimensional, shell-like reflective aesthetic suitable for high-tier financial cards and gift portfolios.</p>
      `
    },
    'modal-service-metal': {
      title: 'Metal & Titanium Cards Specification',
      tag: 'Sovereign Wealth Luxury',
      desc: 'Metal bank cards offer an unmistakable tactile heft and prestige compared to standard plastic. Engineered from solid Grade-5 titanium or stainless steel for private wealth management.',
      details: `
        <table class="modal-specs-table">
          <tr><th>Weight Range</th><td>16.0g (Hybrid Metal) to 28.5g (100% Solid Titanium Monolith)</td></tr>
          <tr><th>Finishing Options</th><td>Stealth PVD Matte Black, Brushed Titanium, 24K Mirror Gold Plating, Mirror Edge Chamfer</td></tr>
          <tr><th>Dual Interface Antenna</th><td>Patented RF booster antenna through solid metal substrate</td></tr>
          <tr><th>Personalization</th><td>High-precision fiber laser engraving, tactile mechanical stamping</td></tr>
          <tr><th>Durability</th><td>Corrosion proof, scratch resistant PVD, zero delamination guarantee</td></tr>
        </table>
      `
    },
    'modal-service-ceramic': {
      title: 'Ceramic Smart Cards Specification',
      tag: 'High-Tech Engineering Ceramics',
      desc: 'Produced from high-performance engineering ceramics such as high-purity Alumina (Al2O3) and Zirconia (ZrO2), delivering unparalleled scratch resistance and diamond-grade luster.',
      details: `
        <table class="modal-specs-table">
          <tr><th>Ceramic Grade</th><td>Tetragonal Zirconia Polycrystal (TZP) & High-Purity Alumina</td></tr>
          <tr><th>Hardness</th><td>Mohs Hardness 8.5+ (diamond-grade scratch immunity)</td></tr>
          <tr><th>Surface Luster</th><td>Deep mirror gloss or silky satin matte finish</td></tr>
          <tr><th>RF Properties</th><td>100% electromagnetic transparent (optimal NFC field efficiency)</td></tr>
          <tr><th>Hypoallergenic</th><td>Biocompatible, skin-friendly, completely chemically inert</td></tr>
        </table>
      `
    },
    'modal-service-chip': {
      title: 'Bespoke Chip Modules Specification',
      tag: 'Micro-Electronic Customization',
      desc: 'We customize chip module contact surfaces with proprietary bank logos, cultural crests, or bespoke geometric contact traces, elevating the visual identity of the card.',
      details: `
        <table class="modal-specs-table">
          <tr><th>Plating Metallurgy</th><td>24K Flash Gold, Palladium, Rose Gold, Ruthenium Black</td></tr>
          <tr><th>Laser Patterning</th><td>Custom micro-laser contact etchings (emblems, logos, geometric art)</td></tr>
          <tr><th>Chip Security</th><td>CC EAL6+ Certified crypto-coprocessor with RSA/ECC accelerators</td></tr>
          <tr><th>Interfaces</th><td>Contact (ISO/IEC 7816) & Dual Interface Contactless (ISO/IEC 14443)</td></tr>
        </table>
      `
    },
    'modal-service-wearable': {
      title: 'Wearable Payment Devices Specification',
      tag: 'Biometric & NFC Mobility',
      desc: 'GENTECH Global designs and manufactures wearable payment devices integrating certified EMV chips into rings, wristbands, and key fobs for seamless tap-and-go transactions.',
      details: `
        <table class="modal-specs-table">
          <tr><th>Form Factors</th><td>Concave Titanium Smart Rings, Ceramic Smart Rings, Silicone/Ceramic Wristbands, Fobs</td></tr>
          <tr><th>Payment Power</th><td>Zero-battery passive NFC operation (infinite standby power)</td></tr>
          <tr><th>Health Telemetry</th><td>BioActive optical PPG sensors (heart rate, SpO2, sleep stages) in smart rings</td></tr>
          <tr><th>Water Resistance</th><td>5ATM & IP68 rated (swimming and shower safe)</td></tr>
          <tr><th>Security Tokenization</th><td>Tokenized EMV credentials approved by Visa and Mastercard</td></tr>
        </table>
      `
    },
    'modal-service-transport': {
      title: 'Transport & City Cards Specification',
      tag: 'Smart Mobility & Transit',
      desc: 'Contactless smart transit cards engineered for high-throughput public transportation networks, including subways, metros, buses, trams, ferries, and smart city infrastructure.',
      details: `
        <table class="modal-specs-table">
          <tr><th>Gate Latency</th><td>Sub-50ms ultra-fast transaction time for zero turnstile bottleneck</td></tr>
          <tr><th>Ticketing Standards</th><td>Account-Based Ticketing (ABT), Calypso, MIFARE Plus / DESFire</td></tr>
          <tr><th>Open Loop Transit</th><td>Direct contactless EMV bank card acceptance at transit turnstiles</td></tr>
          <tr><th>Multi-Modal Tokens</th><td>Unified subway, bus, parking, bike sharing, and civic identification</td></tr>
        </table>
      `
    },
    'modal-service-telecom': {
      title: 'Telecommunications & 5G SIM Specification',
      tag: 'Cellular & Super NFC Architecture',
      desc: 'Intelligent cards used in 5G networks to authenticate subscribers, manage network profiles, and protect user data, along with Super NFC SIM modules.',
      details: `
        <table class="modal-specs-table">
          <tr><th>SIM Generations</th><td>GSM SIM, 4G LTE SIM, 5G Standalone & Non-Standalone (SA/NSA)</td></tr>
          <tr><th>Super NFC SIM</th><td>Unifies 5G cellular, bank cards, electronic ID, and subway tickets into one chip</td></tr>
          <tr><th>OTA Protocol</th><td>Remote Over-the-Air application provisioning and credential updates</td></tr>
          <tr><th>Security OS</th><td>Multi-tenant Secure OS supporting GSMA and ISO/IEC 14443 Type A/B</td></tr>
          <tr><th>IoT Cards</th><td>Specialized IoT number segments with private APN and fleet telemetry</td></tr>
        </table>
      `
    },
    'modal-service-hardware': {
      title: 'Banking & Payment Hardware Specification',
      tag: 'Point-of-Sale Fleet & Audio Verification',
      desc: 'Commercial hardware infrastructure enabling merchants and financial institutions to accept card, mobile, and dynamic QR transactions securely.',
      details: `
        <table class="modal-specs-table">
          <tr><th>POS Form Factors</th><td>Countertop POS (Ethernet), mPOS (Bluetooth/4G/5G), Smart Android Touchscreen POS</td></tr>
          <tr><th>QR Code Sound Box Z20</th><td>2.4-inch LCD screen, 4G/WiFi connectivity, high-decibel audio confirmation broadcast</td></tr>
          <tr><th>Cloud Printers</th><td>Wireless internet thermal printing without host PC connection</td></tr>
          <tr><th>Certifications</th><td>PCI-PTS 6.x, EMV L1/L2 Contact & Contactless, CE, FCC</td></tr>
        </table>
      `
    },
    'modal-service-integration': {
      title: 'Card & Chip Integration & Personalization',
      tag: 'Certified Facility Operations',
      desc: 'Complete end-to-end control from antenna embedding and chip packaging to laser engraving, color personalization, and secure cryptographic key injection.',
      details: `
        <table class="modal-specs-table">
          <tr><th>Prelam Manufacturing</th><td>High-precision ultrasonic wire embedding and chip module lamination</td></tr>
          <tr><th>Personalization Tech</th><td>High-speed UV drop-on-demand printing, thermal retransfer, fiber laser engraving</td></tr>
          <tr><th>HSM Key Management</th><td>FIPS 140-2 Level 3 Hardware Security Modules for cryptographic key derivation</td></tr>
          <tr><th>Packaging & Fulfillment</th><td>Tamper-evident secure packaging with custom luxury bank presentation boxes</td></tr>
        </table>
      `
    }
  };

  detailModalBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const modalKey = btn.getAttribute('data-modal');
      const data = serviceSpecsData[modalKey];
      if (data && modalContent) {
        modalContent.innerHTML = `
          <div style="font-size:0.75rem; font-weight:700; color:var(--accent-hermes); text-transform:uppercase; margin-bottom:0.4rem;">${data.tag}</div>
          <h3 class="serif-title">${data.title}</h3>
          <p>${data.desc}</p>
          ${data.details}
          <div style="margin-top: 1.75rem; text-align: center;">
            <a href="#contact" class="btn-primary modal-inquire-btn" style="padding: 0.7rem 1.8rem;">
              <span>Inquire Fleet Specifications</span>
            </a>
          </div>
        `;
        if (modalBackdrop) modalBackdrop.classList.add('open');

        // Attach listener to new modal inquire button
        const inqBtn = modalContent.querySelector('.modal-inquire-btn');
        inqBtn?.addEventListener('click', () => {
          if (modalBackdrop) modalBackdrop.classList.remove('open');
        });
      }
    });
  });

  modalCloseBtn?.addEventListener('click', () => {
    if (modalBackdrop) modalBackdrop.classList.remove('open');
  });

  modalBackdrop?.addEventListener('click', (e) => {
    if (e.target === modalBackdrop) {
      modalBackdrop.classList.remove('open');
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalBackdrop?.classList.contains('open')) {
      modalBackdrop.classList.remove('open');
    }
  });
});
