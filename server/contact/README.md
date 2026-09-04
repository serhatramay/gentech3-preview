# Isolated contact-form preview

Endpoint: `https://forms-preview.gentech.ae/contact.php` (Markum, separate `gtformt` test account).
Production `gentech.ae` pages and mail routing are not changed by this service.

The test account requires PHP 8.2+ (PHP 8.3 selected), HTTPS and OpenSSL. Its free
Let's Encrypt certificate covers **only** `forms-preview.gentech.ae`.

## Build and test

```sh
php server/contact/test.php
python3 site/build.py --contact-endpoint https://forms-preview.gentech.ae/contact.php
python3 site/audit.py
```

The 33 PHP checks use a stub transport and do not send real email. A successful
GET challenge proves the endpoint is configured and running, not SMTP delivery.
Final acceptance requires a real form submission plus inbox/spam-folder verification.

Install locked dependencies with Composer (no plugins/scripts), then run
`python3 server/contact/package.py`. Extract the archive in the **test domain's**
directory, not the live site's directory. It creates `public_html/contact.php` and
a sibling `gentech-form-private` directory. Only the entry point is public.

Create `gentech-form-private/config.php` using `config.example.php` as the schema.
Set real credentials through the authenticated HTTPS panel, never in Git or
through plain FTP. Restrict private config/key/state permissions to the account.
The deployed config generates a 32-byte random signing key on first use and stores
it in its private sibling directory. Config, dependencies and archives are ignored
by Git; all `server/` source is excluded from GitHub Pages publication.

The SMTP sender is an authenticated `@gentech.ae` account, recipient is fixed to
`info@gentech.ae`, visitor address is Reply-To. Port 587 uses mandatory STARTTLS
with certificate verification; debugging does not expose SMTP errors to visitors.
No visitor auto-reply, attachments, arbitrary recipient or CRM integration exists.

Limits: 3 attempts/IP/15 minutes, 6/IP/day, 20 global/hour, 50 global/day.
The state file stores keyed hashes, references, timestamps and send outcomes,
not raw addresses, names or message bodies. Expired rows are pruned by subsequent
submissions. Normal hosting logs and the receiving mailbox are separate.

The signed token binds the requesting IP and expires in 30 minutes. Its minimum
age is 3 seconds. Origin checking is a browser restriction, not authentication or
a replacement for spam limits. SMTP attempts are persisted before sending;
unconfirmed outcomes are never automatically resent with the same token.

Rollback: build without `--contact-endpoint` to restore the explicit mailto-draft
fallback. Disable `enabled` in the private config to stop the test endpoint.
Do not deploy the test endpoint or enable production indexing without approval.

## Verification status

- Local backend assertions: 33 passed.
- Static site audit: 33 HTML routes passed.
- Composer audit: no known advisories reported at installation.
- HTTPS and GET challenge: HTTP 200, exact GitHub preview origin allowed.
- Actual SMTP delivery and mailbox receipt: pending user submission.
