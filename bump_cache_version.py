import os, re

base_dir = "/Users/ramay/gentech3-app"
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

for f in html_files:
    file_path = os.path.join(base_dir, f)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace ?v=XX.X with ?v=30.0
    content = re.sub(r'\?v=\d+\.\d+', '?v=30.0', content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Bumped cache version to ?v=30.0 across {len(html_files)} HTML files.")

