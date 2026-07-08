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

emote_categories = {
    "gura": {"name": "Gawr Gura", "path": "images/emote/gura"},
    "gura_q": {"name": "Gura Q版", "path": "images/emote/gura_q"},
    "komugi": {"name": "小粥", "path": "images/emote/komugi"},
    "kai": {"name": "怪诶", "path": "images/emote/kai"},
    "hazuki": {"name": "猫羽雫", "path": "images/emote/hazuki"},
    "mari": {"name": "茉莉", "path": "images/emote/mari"},
    "akami": {"name": "赤见", "path": "images/emote/akami"},
    "nachoneko": {"name": "Nachoneko", "path": "images/emote/nachoneko"},
    "kana": {"name": "Kana", "path": "images/emote/kana"},
    "riru": {"name": "Riru", "path": "images/emote/riru"},
    "sui": {"name": "Sui", "path": "images/emote/sui"},
    "naname": {"name": "Naname", "path": "images/emote/naname"},
    "twitch": {"name": "Twitch", "path": "images/emote/twitch"},
    "other": {"name": "其他", "path": "images/emote/other"}
}

for key, config in emote_categories.items():
    dir_path = os.path.join(os.path.dirname(__file__), config["path"])
    files = get_image_files(dir_path)
    config["files"] = files
    print(f"{key}: {len(files)} files")

with open(os.path.join(os.path.dirname(__file__), 'emote-gallery.html'), 'r', encoding='utf-8') as f:
    content = f.read()

old_pattern = "const emoteCategories = \{[\s\S]*?\};"

new_categories = "const emoteCategories = {\n"
for i, (key, config) in enumerate(emote_categories.items()):
    files_str = '["' + '","'.join(config["files"]) + '"]'
    comma = "," if i < len(emote_categories) - 1 else ""
    new_categories += f'    "{key}": {{ "name": "{config["name"]}", "path": "{config["path"]}", "files": {files_str} }}{comma}\n'
new_categories += "};"

content = content.replace(old_pattern, new_categories)

with open(os.path.join(os.path.dirname(__file__), 'emote-gallery.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print("emote-gallery.html updated successfully!")
