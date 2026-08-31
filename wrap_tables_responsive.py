import os, re

base_dir = "/Users/ramay/gentech3-app"
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

for f in html_files:
    file_path = os.path.join(base_dir, f)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Wrap table if not wrapped
    if '<table' in content and 'table-responsive' not in content:
        content = re.sub(r'(<table[^>]*>.*?</table>)', r'<div class="table-responsive">\1</div>', content, flags=re.DOTALL)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Wrapped tables in: {f}")

print("Responsive table wrapping completed.")
