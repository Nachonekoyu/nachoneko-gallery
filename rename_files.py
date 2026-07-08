import os
import shutil

def rename_files_in_dir(base_dir, category_name):
    files = []
    for f in os.listdir(base_dir):
        full_path = os.path.join(base_dir, f)
        if os.path.isfile(full_path):
            ext = os.path.splitext(f)[1].lower()
            if ext in ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.ico'):
                files.append(f)
    
    files.sort(key=lambda x: (x.split('.')[0], x))
    
    new_files = []
    for i, f in enumerate(files, 1):
        ext = os.path.splitext(f)[1]
        new_name = f"{category_name}{i:03d}{ext}"
        old_path = os.path.join(base_dir, f)
        new_path = os.path.join(base_dir, new_name)
        os.rename(old_path, new_path)
        new_files.append(new_name)
        print(f"Renamed: {f} -> {new_name}")
    
    return new_files

main_categories = {
    "recent": "images/main/recent",
    "early": "images/main/early",
    "daily": "images/main/daily",
    "sketch": "images/main/sketch",
    "mousepad": "images/main/mousepad",
    "merch": "images/main/merch",
    "corner": "images/main/corner"
}

emote_categories = {
    "gura": "images/emote/gura",
    "gura_q": "images/emote/gura_q",
    "komugi": "images/emote/komugi",
    "kai": "images/emote/kai",
    "hazuki": "images/emote/hazuki",
    "mari": "images/emote/mari",
    "akami": "images/emote/akami",
    "nachoneko": "images/emote/nachoneko",
    "kana": "images/emote/kana",
    "riru": "images/emote/riru",
    "sui": "images/emote/sui",
    "naname": "images/emote/naname",
    "twitch": "images/emote/twitch",
    "other": "images/emote/other"
}

new_main = {}
for key, path in main_categories.items():
    full_path = os.path.join(os.path.dirname(__file__), path)
    if os.path.exists(full_path):
        print(f"\nRenaming files in {path}...")
        new_main[key] = rename_files_in_dir(full_path, key)

new_emote = {}
for key, path in emote_categories.items():
    full_path = os.path.join(os.path.dirname(__file__), path)
    if os.path.exists(full_path):
        print(f"\nRenaming files in {path}...")
        new_emote[key] = rename_files_in_dir(full_path, key)

print("\nDone! Now updating HTML files...")

import re

main_content = {
    "recent": {"name": "近期作品", "path": "images/main/recent", "files": new_main["recent"]},
    "early": {"name": "早期作品", "path": "images/main/early", "files": new_main["early"]},
    "daily": {"name": "日常插画", "path": "images/main/daily", "files": new_main["daily"]},
    "sketch": {"name": "草图", "path": "images/main/sketch", "files": new_main["sketch"]},
    "mousepad": {"name": "鼠标垫图", "path": "images/main/mousepad", "files": new_main["mousepad"]},
    "merch": {"name": "周边展示", "path": "images/main/merch", "files": new_main["merch"]},
    "corner": {"name": "阴暗角落", "path": "images/main/corner", "files": new_main["corner"]}
}

new_main_categories = "const mainCategories = {\n"
for i, (key, config) in enumerate(main_content.items()):
    files_str = '["' + '","'.join(config["files"]) + '"]'
    comma = "," if i < len(main_content) - 1 else ""
    new_main_categories += f'    "{key}": {{ "name": "{config["name"]}", "path": "{config["path"]}", "files": {files_str} }}{comma}\n'
new_main_categories += "};"

with open(os.path.join(os.path.dirname(__file__), 'main-gallery.html'), 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'const mainCategories = \{[\s\S]*?\};', new_main_categories, content)
with open(os.path.join(os.path.dirname(__file__), 'main-gallery.html'), 'w', encoding='utf-8') as f:
    f.write(content)

emote_content = {
    "gura": {"name": "Gawr Gura", "path": "images/emote/gura", "files": new_emote["gura"]},
    "gura_q": {"name": "Gura Q版", "path": "images/emote/gura_q", "files": new_emote["gura_q"]},
    "komugi": {"name": "小粥", "path": "images/emote/komugi", "files": new_emote["komugi"]},
    "kai": {"name": "怪诶", "path": "images/emote/kai", "files": new_emote["kai"]},
    "hazuki": {"name": "猫羽雫", "path": "images/emote/hazuki", "files": new_emote["hazuki"]},
    "mari": {"name": "茉莉", "path": "images/emote/mari", "files": new_emote["mari"]},
    "akami": {"name": "赤见", "path": "images/emote/akami", "files": new_emote["akami"]},
    "nachoneko": {"name": "Nachoneko", "path": "images/emote/nachoneko", "files": new_emote["nachoneko"]},
    "kana": {"name": "Kana", "path": "images/emote/kana", "files": new_emote["kana"]},
    "riru": {"name": "Riru", "path": "images/emote/riru", "files": new_emote["riru"]},
    "sui": {"name": "Sui", "path": "images/emote/sui", "files": new_emote["sui"]},
    "naname": {"name": "Naname", "path": "images/emote/naname", "files": new_emote["naname"]},
    "twitch": {"name": "Twitch", "path": "images/emote/twitch", "files": new_emote["twitch"]},
    "other": {"name": "其他", "path": "images/emote/other", "files": new_emote["other"]}
}

new_emote_categories = "const emoteCategories = {\n"
for i, (key, config) in enumerate(emote_content.items()):
    files_str = '["' + '","'.join(config["files"]) + '"]'
    comma = "," if i < len(emote_content) - 1 else ""
    new_emote_categories += f'    "{key}": {{ "name": "{config["name"]}", "path": "{config["path"]}", "files": {files_str} }}{comma}\n'
new_emote_categories += "};"

with open(os.path.join(os.path.dirname(__file__), 'emote-gallery.html'), 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'const emoteCategories = \{[\s\S]*?\};', new_emote_categories, content)
with open(os.path.join(os.path.dirname(__file__), 'emote-gallery.html'), 'w', encoding='utf-8') as f:
    f.write(content)

character_image_map = {
    "gura": new_emote["gura"][3] if len(new_emote["gura"]) > 3 else new_emote["gura"][0],
    "komugi": new_emote["komugi"][0],
    "kai": new_emote["kai"][0],
    "hazuki": new_emote["hazuki"][0],
    "mari": new_emote["mari"][0],
    "akami": new_emote["akami"][0],
    "nachoneko": new_emote["nachoneko"][0],
    "kana": new_emote["kana"][0],
    "riru": new_emote["riru"][0],
    "sui": new_emote["sui"][0],
    "naname": new_emote["naname"][0]
}

with open(os.path.join(os.path.dirname(__file__), 'characters.html'), 'r', encoding='utf-8') as f:
    content = f.read()

for char_id, new_image in character_image_map.items():
    old_pattern = f'images/emote/{char_id}/[^"]+'
    new_path = f'images/emote/{char_id}/{new_image}'
    content = re.sub(old_pattern, new_path, content)

with open(os.path.join(os.path.dirname(__file__), 'characters.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print("\nAll files renamed and HTML updated!")
