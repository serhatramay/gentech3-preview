import re

# Update build_all_gentech_group.py to support extra_scripts in get_footer
with open("/Users/ramay/gentech3-app/build_all_gentech_group.py", "r", encoding="utf-8") as f:
    code = f.read()

old_footer_func = '''def get_footer():
    return """
<!-- Corporate Footer -->'''

new_footer_func = '''def get_footer(extra_scripts=""):
    return f"""
<!-- Corporate Footer -->'''

code = code.replace(old_footer_func, new_footer_func)

old_footer_end = '''<!-- Core Scripts -->
<script src="assets/js/app.js?v=21.0"></script>
</body>
</html>
"""'''

new_footer_end = '''<!-- Core Scripts -->
{extra_scripts}
<script src="assets/js/app.js?v=21.0"></script>
</body>
</html>
"""'''

code = code.replace(old_footer_end, new_footer_end)

with open("/Users/ramay/gentech3-app/build_all_gentech_group.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_all_gentech_group.py with extra_scripts support.")

# Now update generate_pages_master.py to pass Three.js and scene3d.js to index.html and solutions-cards.html
with open("/Users/ramay/gentech3-app/generate_pages_master.py", "r", encoding="utf-8") as f:
    gen_code = f.read()

gen_code = gen_code.replace(
    'write_file("index.html", header + body + get_footer())',
    'three_scripts = \'<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\\n<script src="assets/js/scene3d.js?v=21.0"></script>\'\n    write_file("index.html", header + body + get_footer(three_scripts))'
)

with open("/Users/ramay/gentech3-app/generate_pages_master.py", "w", encoding="utf-8") as f:
    f.write(gen_code)

print("Updated generate_pages_master.py with Three.js injection for index.html.")

