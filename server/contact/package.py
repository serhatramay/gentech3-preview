"""Build a secret-free upload archive for the isolated test domain only."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parent
assert (root / 'vendor/autoload.php').is_file(), 'Install locked dependencies first'
with ZipFile(root / 'contact-preview.zip', 'w', ZIP_DEFLATED) as bundle:
    bundle.write(root / 'public/contact.php', 'public_html/contact.php')
    for name in ['app.php', 'config.example.php']:
        bundle.write(root / name, 'gentech-form-private/' + name)
    for path in sorted((root / 'vendor').rglob('*')):
        if path.is_file():
            bundle.write(path, 'gentech-form-private/' + str(path.relative_to(root)))
print('Built contact-preview.zip; no config.php, credentials, production files or tests included.')
