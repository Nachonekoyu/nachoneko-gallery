import os

def get_image_files(dir_path):
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.JPG', '.JPEG', '.PNG', '.GIF', '.WEBP')
    files = []
    if os.path.exists(dir_path):
        for f in os.listdir(dir_path):
            if f.lower().endswith(extensions):
                files.append(f)
    files.sort(key=lambda x: (x.split('.')[0], x))
    return files

early_files = get_image_files(os.path.join(os.path.dirname(__file__), 'images/main/early'))
files_str = '["' + '","'.join(early_files) + '"]'

with open(os.path.join(os.path.dirname(__file__), 'main-gallery.html'), 'r', encoding='utf-8') as f:
    content = f.read()

old_early = '"early": { "name": "早期作品", "path": "images/main/early", "files": ["早期图001.jpg"'
new_early = '"early": { "name": "早期作品", "path": "images/main/early", "files": ' + files_str

content = content.replace(old_early, new_early)

with open(os.path.join(os.path.dirname(__file__), 'main-gallery.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed early category with {len(early_files)} files")
