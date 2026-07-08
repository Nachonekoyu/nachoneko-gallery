import os
import json

def get_image_files(dir_path):
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.JPG', '.JPEG', '.PNG', '.GIF', '.WEBP')
    files = []
    if os.path.exists(dir_path):
        for f in os.listdir(dir_path):
            if f.lower().endswith(extensions):
                files.append(f)
    files.sort(key=lambda x: (x.split('.')[0], x))
    return files

main_categories = {
    "recent": {"name": "近期作品", "path": "images/main/recent"},
    "early": {"name": "早期作品", "path": "images/main/early"},
    "daily": {"name": "日常插画", "path": "images/main/daily"},
    "sketch": {"name": "草图", "path": "images/main/sketch"},
    "mousepad": {"name": "鼠标垫图", "path": "images/main/mousepad"},
    "merch": {"name": "周边展示", "path": "images/main/merch"},
    "corner": {"name": "阴暗角落", "path": "images/main/corner"}
}

for key, config in main_categories.items():
    dir_path = os.path.join(os.path.dirname(__file__), config["path"])
    files = get_image_files(dir_path)
    config["files"] = files
    print(f"{key}: {len(files)} files")

with open(os.path.join(os.path.dirname(__file__), 'main-gallery.html'), 'r', encoding='utf-8') as f:
    content = f.read()

old_pattern = "const mainCategories = \{[\s\S]*?\};"

new_categories = "const mainCategories = {\n"
for i, (key, config) in enumerate(main_categories.items()):
    files_str = '["' + '","'.join(config["files"]) + '"]'
    comma = "," if i < len(main_categories) - 1 else ""
    new_categories += f'    "{key}": {{ "name": "{config["name"]}", "path": "{config["path"]}", "files": {files_str} }}{comma}\n'
new_categories += "};"

content = content.replace(old_pattern, new_categories)

with open(os.path.join(os.path.dirname(__file__), 'main-gallery.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print("main-gallery.html updated successfully!")
