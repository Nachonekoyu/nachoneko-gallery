import os
import json

BASE_DIR = r'F:\猫图'

def get_image_files(folder_path):
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.ico')
    files = []
    for f in sorted(os.listdir(folder_path)):
        if f.lower().endswith(extensions):
            files.append(f)
    return files

def build_category_data():
    categories = {
        'main': {
            'recent': {
                'name': '近期作品',
                'path': os.path.join(BASE_DIR, '甘城主图', '主图', '近期'),
                'files': []
            },
            'daily': {
                'name': '日常插画',
                'path': os.path.join(BASE_DIR, '甘城主图', '日常'),
                'files': []
            },
            'sketch': {
                'name': '草图',
                'path': os.path.join(BASE_DIR, '甘城主图', '草图'),
                'files': []
            },
            'mousepad': {
                'name': '鼠标垫图',
                'path': os.path.join(BASE_DIR, '甘城主图', '鼠标垫图'),
                'files': []
            }
        },
        'emote': {
            'gura': {
                'name': 'Gawr Gura',
                'path': os.path.join(BASE_DIR, '相关表情', 'gura'),
                'files': []
            },
            'gura_q': {
                'name': 'Gura 特殊',
                'path': os.path.join(BASE_DIR, '相关表情', 'gura', '？'),
                'files': []
            },
            'nachoneko': {
                'name': 'Nachoneko',
                'path': os.path.join(BASE_DIR, '相关表情', 'nachoneko'),
                'files': []
            },
            'kana': {
                'name': 'Kana',
                'path': os.path.join(BASE_DIR, '相关表情', 'kana'),
                'files': []
            },
            'riru': {
                'name': 'Riru',
                'path': os.path.join(BASE_DIR, '相关表情', 'りる'),
                'files': []
            },
            'sui': {
                'name': 'Sui',
                'path': os.path.join(BASE_DIR, '相关表情', 'スイ（sui）'),
                'files': []
            },
            'naname': {
                'name': 'Naname',
                'path': os.path.join(BASE_DIR, '相关表情', 'naname'),
                'files': []
            },
            'twitch': {
                'name': 'Twitch',
                'path': os.path.join(BASE_DIR, '相关表情', 'Twitch'),
                'files': []
            },
            'other': {
                'name': '其他',
                'path': os.path.join(BASE_DIR, '相关表情', '其他'),
                'files': []
            }
        }
    }

    for section, cats in categories.items():
        for cat, data in cats.items():
            if os.path.exists(data['path']):
                data['files'] = get_image_files(data['path'])
            else:
                print(f"Warning: Path not found - {data['path']}")

    return categories

def generate_html(categories):
    html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>甘城なつき - 插画作品展示</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary-color: #8B5CF6;
            --secondary-color: #F472B6;
            --accent-color: #06B6D4;
            --bg-dark: #0F172A;
            --bg-card: #1E293B;
            --text-primary: #F8FAFC;
            --text-secondary: #94A3B8;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, var(--bg-dark) 0%, #1E1B4B 100%);
            color: var(--text-primary);
            min-height: 100vh;
        }

        header {
            background: rgba(30, 41, 59, 0.8);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(139, 92, 246, 0.2);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .header-content {
            max-width: 1400px;
            margin: 0 auto;
            padding: 1.5rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        h1 {
            font-size: 2rem;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .nav-links {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .nav-links a {
            color: var(--text-secondary);
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            transition: all 0.3s ease;
        }

        .nav-links a:hover, .nav-links a.active {
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
        }

        main {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }

        .hero-section {
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(244, 114, 182, 0.1) 100%);
            border-radius: 20px;
            margin-bottom: 3rem;
            border: 1px solid rgba(139, 92, 246, 0.2);
        }

        .hero-section h2 {
            font-size: 3rem;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero-section p {
            font-size: 1.2rem;
            color: var(--text-secondary);
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.8;
        }

        .about-section {
            background: var(--bg-card);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 3rem;
            border: 1px solid rgba(139, 92, 246, 0.2);
        }

        .about-section h3 {
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            color: var(--secondary-color);
        }

        .about-section p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: var(--text-secondary);
            margin-bottom: 1rem;
        }

        .characters-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            margin-bottom: 3rem;
        }

        .character-card {
            background: var(--bg-card);
            border-radius: 15px;
            overflow: hidden;
            border: 1px solid rgba(139, 92, 246, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .character-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 40px rgba(139, 92, 246, 0.3);
        }

        .character-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        }

        .character-card .card-content {
            padding: 1.5rem;
        }

        .character-card h4 {
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
            color: var(--primary-color);
        }

        .character-card p {
            font-size: 0.95rem;
            color: var(--text-secondary);
            line-height: 1.6;
        }

        .gallery-section {
            margin-bottom: 3rem;
        }

        .gallery-section h3 {
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            color: var(--secondary-color);
        }

        .category-tabs {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
        }

        .category-tabs button {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 25px;
            background: var(--bg-card);
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.95rem;
            border: 1px solid rgba(139, 92, 246, 0.2);
        }

        .category-tabs button:hover, .category-tabs button.active {
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
            border-color: transparent;
        }

        .images-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1rem;
        }

        .image-item {
            aspect-ratio: 1;
            border-radius: 10px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(244, 114, 182, 0.2));
        }

        .image-item:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 30px rgba(139, 92, 246, 0.4);
        }

        .image-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .lightbox {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.9);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }

        .lightbox.active {
            display: flex;
        }

        .lightbox-content {
            max-width: 90%;
            max-height: 90%;
            object-fit: contain;
            border-radius: 10px;
        }

        .lightbox-close {
            position: absolute;
            top: 2rem;
            right: 2rem;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        .lightbox-close:hover {
            background: rgba(255, 255, 255, 0.2);
        }

        .lightbox-nav {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        .lightbox-nav:hover {
            background: rgba(255, 255, 255, 0.2);
        }

        .lightbox-prev {
            left: 2rem;
        }

        .lightbox-next {
            right: 2rem;
        }

        .loading {
            width: 50px;
            height: 50px;
            border: 3px solid rgba(139, 92, 246, 0.3);
            border-top-color: var(--primary-color);
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 2rem auto;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .scroll-top {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            border: none;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 100;
        }

        .scroll-top.active {
            opacity: 1;
            visibility: visible;
        }

        footer {
            background: var(--bg-card);
            border-top: 1px solid rgba(139, 92, 246, 0.2);
            padding: 2rem;
            text-align: center;
            color: var(--text-secondary);
        }

        @media (max-width: 768px) {
            h1 {
                font-size: 1.5rem;
            }

            .hero-section h2 {
                font-size: 2rem;
            }

            .hero-section p {
                font-size: 1rem;
            }

            .images-grid {
                grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            }

            .nav-links {
                display: none;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <h1>甘城なつき</h1>
            <nav class="nav-links">
                <a href="#about">关于作者</a>
                <a href="#characters">角色介绍</a>
                <a href="#main-gallery">主图</a>
                <a href="#emotes">表情</a>
            </nav>
        </div>
    </header>

    <main>
        <section class="hero-section">
            <h2>甘城なつき</h2>
            <p>アマシロナツキ — 知名插画师，以设计 VTuber 角色而闻名，代表作品包括 Hololive EN 成员 Gawr Gura、Ninomae Ina'nis 等角色形象。其独特的艺术风格和可爱的角色设计深受粉丝喜爱。</p>
        </section>

        <section id="about" class="about-section">
            <h3>关于作者</h3>
            <p><strong>甘城なつき（Amashiro Natsuki）</strong> 是一位日本插画师，活跃于社交媒体和插画平台。她以创作可爱的虚拟主播（VTuber）角色设计而广为人知，尤其在 Hololive English 一期生中，她设计的角色形象极具辨识度。</p>
            <p>甘城なつき的艺术风格以柔和的色彩、圆润的线条和生动的表情为特点，擅长捕捉角色的个性魅力。她的作品不仅限于角色设计，还包括日常插画、同人创作等多种形式。</p>
            <p>除了 Hololive 的角色外，甘城なつき还创作了许多原创角色，如猫耳少女 Nachoneko（なちょねこ），展现了她丰富的想象力和创作才华。</p>
        </section>

        <section id="characters" class="characters-section">
            <h3 style="font-size: 1.8rem; margin-bottom: 1.5rem; color: #F472B6;">主要角色介绍</h3>
            <div class="characters-grid">
                <div class="character-card">
                    <img src="file:///F:/猫图/相关表情/gura/gura04.jpg" alt="Gawr Gura">
                    <div class="card-content">
                        <h4>Gawr Gura（がうる・がうら）</h4>
                        <p>Hololive EN 一期生成员，鲨鱼娘形象。以可爱的外表和活泼的性格受到广泛喜爱，是 Hololive 中人气最高的虚拟主播之一。</p>
                    </div>
                </div>
                <div class="character-card">
                    <img src="file:///F:/猫图/相关表情/nachoneko/nachoneko-001.jpg" alt="Nachoneko">
                    <div class="card-content">
                        <h4>Nachoneko（なちょねこ）</h4>
                        <p>甘城なつき的原创角色，一只可爱的猫耳少女。作为作者的看板娘，经常出现在各种插画作品中。</p>
                    </div>
                </div>
                <div class="character-card">
                    <img src="file:///F:/猫图/相关表情/kana/kana01.PNG" alt="Kana">
                    <div class="card-content">
                        <h4>Kana（かな）</h4>
                        <p>甘城なつき创作的另一个原创角色，以其独特的发型和可爱的表情受到粉丝喜爱。</p>
                    </div>
                </div>
                <div class="character-card">
                    <img src="file:///F:/猫图/相关表情/りる/りる01.png" alt="Riru">
                    <div class="card-content">
                        <h4>Riru（りる）</h4>
                        <p>甘城なつき设计的角色之一，以其独特的造型和可爱的形象吸引了众多粉丝。</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="main-gallery" class="gallery-section">
            <h3>主图画廊</h3>
            <div class="category-tabs">
"""

    for cat, data in categories['main'].items():
        active = 'class="active"' if cat == 'recent' else ''
        html += f'                <button {active} data-category="{cat}">{data["name"]}</button>\n'

    html += """            </div>
            <div class="images-grid" id="main-grid">
                <div class="loading"></div>
            </div>
        </section>

        <section id="emotes" class="gallery-section">
            <h3>表情画廊</h3>
            <div class="category-tabs">
"""

    for cat, data in categories['emote'].items():
        active = 'class="active"' if cat == 'gura' else ''
        html += f'                <button {active} data-category="{cat}">{data["name"]}</button>\n'

    html += """            </div>
            <div class="images-grid" id="emote-grid">
                <div class="loading"></div>
            </div>
        </section>
    </main>

    <footer>
        <p>© 2026 甘城なつき作品展示 | 所有图片版权归原作者所有</p>
    </footer>

    <div class="lightbox" id="lightbox">
        <button class="lightbox-close" id="lightbox-close">×</button>
        <button class="lightbox-nav lightbox-prev" id="lightbox-prev">‹</button>
        <img class="lightbox-content" id="lightbox-content" src="" alt="">
        <button class="lightbox-nav lightbox-next" id="lightbox-next">›</button>
    </div>

    <button class="scroll-top" id="scroll-top">↑</button>

    <script>
        const mainCategories = """ + json.dumps(categories['main'], ensure_ascii=False) + """;
        const emoteCategories = """ + json.dumps(categories['emote'], ensure_ascii=False) + """;

        let currentImages = [];
        let currentIndex = 0;

        function renderImages(gridId, category, config) {
            const grid = document.getElementById(gridId);
            grid.innerHTML = '<div class="loading"></div>';

            setTimeout(() => {
                grid.innerHTML = '';
                const urls = [];
                config.files.forEach(file => {
                    const path = config.path.replace(/\\\\/g, '/');
                    urls.push('file:///' + path + '/' + file);
                });
                currentImages = urls;

                urls.forEach((url, index) => {
                    const item = document.createElement('div');
                    item.className = 'image-item';
                    item.onclick = () => openLightbox(url, index, urls);

                    const img = document.createElement('img');
                    img.src = url;
                    img.alt = file;
                    img.onerror = function() {
                        this.parentElement.style.display = 'none';
                    };
                    img.loading = 'lazy';

                    item.appendChild(img);
                    grid.appendChild(item);
                });
            }, 500);
        }

        function initCategoryTabs(tabContainerSelector, gridId, categories) {
            const buttons = document.querySelectorAll(tabContainerSelector + ' button');
            buttons.forEach(btn => {
                btn.addEventListener('click', () => {
                    buttons.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    const category = btn.dataset.category;
                    renderImages(gridId, category, categories[category]);
                });
            });
        }

        function openLightbox(url, index, images) {
            const lightbox = document.getElementById('lightbox');
            const content = document.getElementById('lightbox-content');
            content.src = url;
            currentImages = images;
            currentIndex = index;
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeLightbox() {
            const lightbox = document.getElementById('lightbox');
            lightbox.classList.remove('active');
            document.body.style.overflow = '';
        }

        function prevImage() {
            currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length;
            document.getElementById('lightbox-content').src = currentImages[currentIndex];
        }

        function nextImage() {
            currentIndex = (currentIndex + 1) % currentImages.length;
            document.getElementById('lightbox-content').src = currentImages[currentIndex];
        }

        function initScrollTop() {
            const scrollBtn = document.getElementById('scroll-top');
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    scrollBtn.classList.add('active');
                } else {
                    scrollBtn.classList.remove('active');
                }
            });
            scrollBtn.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }

        document.getElementById('lightbox-close').addEventListener('click', closeLightbox);
        document.getElementById('lightbox-prev').addEventListener('click', prevImage);
        document.getElementById('lightbox-next').addEventListener('click', nextImage);

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowLeft') prevImage();
            if (e.key === 'ArrowRight') nextImage();
        });

        initCategoryTabs('.gallery-section:nth-of-type(1) .category-tabs', 'main-grid', mainCategories);
        initCategoryTabs('.gallery-section:nth-of-type(2) .category-tabs', 'emote-grid', emoteCategories);

        renderImages('main-grid', 'recent', mainCategories['recent']);
        renderImages('emote-grid', 'gura', emoteCategories['gura']);

        initScrollTop();
    </script>
</body>
</html>"""

    return html

def main():
    categories = build_category_data()
    html = generate_html(categories)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('HTML generated successfully!')

if __name__ == '__main__':
    main()
