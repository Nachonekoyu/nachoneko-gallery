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

recent_files = get_image_files(os.path.join(os.path.dirname(__file__), 'images/main/recent'))
files_str = '["' + '","'.join(recent_files) + '"]'

with open(os.path.join(os.path.dirname(__file__), 'main-gallery.html'), 'r', encoding='utf-8') as f:
    content = f.read()

old_recent = '"recent": { "name": "近期作品", "path": "images/main/recent", "files": ["176.jpg"'
new_recent = '"recent": { "name": "近期作品", "path": "images/main/recent", "files": ' + files_str

content = content.replace(old_recent, new_recent)

with open(os.path.join(os.path.dirname(__file__), 'main-gallery.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed recent category with {len(recent_files)} files")
