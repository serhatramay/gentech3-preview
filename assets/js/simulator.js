/**
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
