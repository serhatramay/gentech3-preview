/**
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
