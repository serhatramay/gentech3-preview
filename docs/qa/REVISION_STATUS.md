# 24-point revision — preview acceptance record

Scope: GitHub Pages preview only. No production transfer, FTP connection or live release.

## Applied

1–3. Holding positioning, exact hero title and introduction; capital, technology, infrastructure and operations lead.

4–9. Conceptual Toronto / Ras Al Khaimah / Johannesburg network; required ten-section homepage order; Develop / Finance / Integrate / Operate model; six platforms in the requested order; card and wearable studio moved to Cards & Secure Payment Products; replacement group metrics.

10–13. Program concession language, commuter/active-user claims, exaggerated corporate wording and sovereign terminology removed from published page copy. 65 million is described as potential population reach.

14–17. Exact Canada and South Africa entity names and conservative operating roles; existing contractual program under the agreement with SANTACO acting through TaxiChoice; architecture distinguished from deployed operations. No unverified parent ownership, direct signatory or exclusive-executor claim.

18–19. Unsupported certification, own-factory and performance claims removed. Product-specific evidence is required before reinstating any such assertion. Card role stated as design, customisation, personalisation, production management and supply.

20. Chairman name, title, descriptor and English/Turkish program wording revised. The initials placeholder is removed. **Approved professional portrait still required; no image of another person or synthetic likeness substituted.**

21. All three supplied addresses and exact corporate names used in shared source data. Old addresses, placeholder telephone numbers, unverified hours and maps removed. info@gentech.ae retained.

22. False CRM-success claim removed. Browser-local email composer validates required fields, email format and consent, carries the enquiry topic into the subject, and supports card sample details. It explicitly says nothing has been submitted or logged. Withdrawing consent or changing fields invalidates the prepared draft. **Server-side sending, real department routing, acknowledgements, CRM logging, spam protection and actual delivery are not implemented or verified; an approved backend and authorised test recipient are required.**

23. Shared navigation and compact footer; Business Platforms replaces Solutions; no flag emojis; standardised group identity. Warm neutral/orange design retained with stronger holding hierarchy.

24. All 33 HTML URLs have shared pages or explicit legacy redirects. Offline audit covers internal URLs/anchors, SEO, IDs, corporate facts, prohibited language and section order. Browser audit covers desktop/tablet/mobile and image/overflow/error checks. Preview is noindex with production canonicals. Production acceptance remains open pending the missing inputs below.

## Verification evidence — 5 September 2026

- `python3 site/audit.py`: PASS, all 33 HTML URLs and internal link/anchor checks.
- `python3 site/browser_audit.py`: PASS, 99 route/viewport checks at 1440×1000, 768×1024 and 390×844. No JavaScript page errors, horizontal overflow, broken images, blank pages or error overlays.
- Both loaded JavaScript files pass `node --check`.
- axe-core 4.12.1: zero reported WCAG A/AA violations on the homepage, contact page and card studio after contrast/ARIA fixes. Logo, SVG and gradient-background text require manual contrast review; inspected visually. This is not a claim of full accessibility certification.
- Card/wearable switch, material selection and card-name/reference personalisation verified. Sample request preserves material, design name and reference and selects the cards enquiry topic.
- Empty required fields and missing consent do not generate a draft. A completed preview-only enquiry creates a correctly encoded `mailto:info@gentech.ae` link and readable copy fallback; zero fetch/XHR submissions. Withdrawing consent removes the link and clears the draft. No email application was opened and no test message was sent.
- Mobile navigation opens, exposes ordered platform links and closes its dropdown/menu with Escape. Reduced-motion mode tested.
- Simulated absence of WebGL: fallback enabled, no 3D canvas, static product image available, no uncaught page error.
- Screenshots and detailed route results are stored locally under `docs/qa/` and excluded from Pages output.

## External evidence still required

- Approved Mustafa Sertkaya portrait.
- Form/backend/CRM details and approval for a real test message; no mail was sent during this revision.
- Contract signature page before an exact direct-signatory claim can be approved. The current copy deliberately makes no such entity-level claim.
- Product-specific certificates before any certification assertion is restored.
- Review the revised Chairman message and privacy/terms content before production publication.

## Security boundary

GitHub Pages configuration excludes local build tools, deployment scripts/notes, QA files and superseded JavaScript from the published site. Existing deployment notes contain access material: excluding them from the website does **not** remove the material from repository history. Credentials need owner-controlled rotation. No credential values are reproduced in this report.
