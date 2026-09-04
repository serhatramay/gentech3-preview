# Gentech Group static site

`python3 site/build.py` builds all public HTML pages, legacy redirects, sitemap and preview robots rules. Shared facts live in `site/content.py`; page composition is in `site/build.py`; product studio and network illustration live in `site/templates/`.

`python3 site/audit.py` validates links, anchors, SEO, approved facts, prohibited claims and the required homepage/platform order.

The default build is **preview-only and noindex**. GitHub Pages publishes `main` at https://serhatramay.github.io/gentech3-preview/. No production transfer is performed by this builder. After separate approval, a production release needs an explicitly reviewed `--production` build and the independently controlled live deployment workflow. Do not push a production-indexed build to the public preview.

The enquiry tool is a browser-local email composer, not an HTTP form backend. It does not send mail, store a CRM record, or issue acknowledgements. A verified backend, spam controls, routing and an authorised test recipient are required before replacing it with a submitted form.

Outstanding source requirements: approved Mustafa Sertkaya portrait; contract signature-page confirmation if an exact signatory claim is desired; product-specific certificates before any certification claim is restored. No photograph, certificate, ownership relationship or exclusive mandate has been invented.
