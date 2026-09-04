'use strict';
(() => {
  const form = document.getElementById('enquiryForm');
  if (!form?.dataset.endpoint) return;
  const result = document.getElementById('enquiryResult');
  const fields = document.getElementById('enquiryFields');
  const department = document.getElementById('department');
  const params = new URLSearchParams(location.search);
  if ([...department.options].some(o => o.value === params.get('dept'))) department.value = params.get('dept');
  if (params.get('design') && department.value === 'cards') document.getElementById('message').value = `I would like to discuss a sample.\n\n${params.get('design').slice(0, 500)}`;
  let attempt = null;
  let busy = false;
  const show = text => { result.textContent = text; result.hidden = false; };
  const call = async options => {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 25000);
    try {
      const response = await fetch(form.dataset.endpoint, {credentials:'omit', cache:'no-store', redirect:'error', ...options, signal:controller.signal});
      const data = await response.json();
      if (!response.ok || data.ok !== true) throw Object.assign(new Error('Submission failed'), {code:data.error});
      return data;
    } finally { clearTimeout(timer); }
  };
  form.addEventListener('input', () => { if (!busy) { attempt = null; result.hidden = true; } });
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (busy || !form.reportValidity()) return;
    busy = true;
    const values = Object.fromEntries(new FormData(form));
    values.consent = document.getElementById('consent').checked;
    fields.disabled = true;
    form.setAttribute('aria-busy', 'true');
    show('Sending your enquiry…');
    try {
      if (!attempt) {
        const challenge = await call({method:'GET'});
        if (typeof challenge.token !== 'string') throw new Error('Invalid response');
        attempt = {...values, token:challenge.token};
        await new Promise(resolve => setTimeout(resolve, 3200));
      }
      const data = await call({method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(attempt)});
      if (!/^GT-[A-F0-9]{32}$/.test(data.reference || '')) throw new Error('Invalid response');
      show(`Your enquiry was accepted by our mail server for info@gentech.ae. Reference: ${data.reference}. Our team can reply to the email address you provided.`);
      form.reset();
      attempt = null;
    } catch (error) {
      const messages = {rate_limit:'Too many submissions. Please try later or email info@gentech.ae directly.', invalid:'Please check your details and consent before trying again.', token:'The submission session expired. Edit a field and try again.', busy:'The service is busy. Please try again shortly.'};
      show(messages[error.code] || 'We could not confirm delivery. Your details are still here. You can retry the unchanged enquiry safely, or email info@gentech.ae directly.');
    } finally { busy = false; fields.disabled = false; form.removeAttribute('aria-busy'); }
  });
})();
