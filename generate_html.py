import os
import json

def get_image_files(base_dir):
    files = []
    for f in os.listdir(base_dir):
        full_path = os.path.join(base_dir, f)
        if os.path.isfile(full_path):
            ext = os.path.splitext(f)[1].lower()
            if ext in ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.ico'):
                files.append(f)
    files.sort()
    return files

def generate_main_gallery():
    categories = {
        "recent": {"name": "近期作品", "path": "images/main/recent"},
        "early": {"name": "早期作品", "path": "images/main/early"},
        "daily": {"name": "日常插画", "path": "images/main/daily"},
        "sketch": {"name": "草图", "path": "images/main/sketch"},
        "mousepad": {"name": "鼠标垫图", "path": "images/main/mousepad"},
        "merch": {"name": "周边展示", "path": "images/main/merch"},
        "corner": {"name": "阴暗角落", "path": "images/main/corner"}
    }
    
    for key in categories:
        cat = categories[key]
        cat["files"] = get_image_files(cat["path"])
        print(f"{key}: {len(cat['files'])} files")
    
    content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>甘城なつき - 主图画廊</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --primary-color: #A78BFA;
            --secondary-color: #F9A8D4;
            --accent-color: #67E8F9;
            --bg-dark: #FDF4FF;
            --bg-card: #FCE7F3;
            --text-primary: #4C1D95;
            --text-secondary: #7C3AED;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, var(--bg-dark) 0%, #F3E8FF 50%, #ECFEFF 100%);
            color: var(--text-primary);
            min-height: 100vh;
        }}

        header {{
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(167, 139, 250, 0.3);
            position: sticky;
            top: 0;
            z-index: 100;
        }}

        .header-content {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 1.5rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        h1 {{
            font-size: 2rem;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .nav-links {{
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }}

        .nav-links a {{
            color: var(--text-secondary);
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            transition: all 0.3s ease;
        }}

        .nav-links a:hover, .nav-links a.active {{
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
        }}

        main {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .hero-section {{
            text-align: center;
            padding: 3rem 2rem;
            background: linear-gradient(135deg, rgba(167, 139, 250, 0.15) 0%, rgba(249, 168, 212, 0.15) 100%);
            border-radius: 20px;
            margin-bottom: 3rem;
            border: 1px solid rgba(167, 139, 250, 0.3);
        }}

        .hero-section h2 {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .hero-section p {{
            font-size: 1.1rem;
            color: var(--text-secondary);
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.8;
        }}

        .gallery-section {{
            margin-bottom: 3rem;
        }}

        .gallery-section h3 {{
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            color: var(--primary-color);
        }}

        .category-tabs {{
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
        }}

        .category-tabs button {{
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 25px;
            background: white;
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.95rem;
            border: 1px solid rgba(167, 139, 250, 0.3);
        }}

        .category-tabs button:hover, .category-tabs button.active {{
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
            border-color: transparent;
        }}

        .images-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1rem;
        }}

        .image-item {{
            aspect-ratio: 1;
            border-radius: 10px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            background: linear-gradient(135deg, rgba(167, 139, 250, 0.2), rgba(249, 168, 212, 0.2));
        }}

        .image-item:hover {{
            transform: scale(1.05);
            box-shadow: 0 8px 30px rgba(167, 139, 250, 0.4);
        }}

        .image-item img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}

        .lightbox {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }}

        .lightbox.active {{
            display: flex;
        }}

        .lightbox-content {{
            max-width: 90%;
            max-height: 90%;
            object-fit: contain;
            border-radius: 10px;
        }}

        .lightbox-close {{
            position: absolute;
            top: 2rem;
            right: 2rem;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            transition: background 0.3s ease;
        }}

        .lightbox-close:hover {{
            background: rgba(255, 255, 255, 0.3);
        }}

        .lightbox-nav {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            transition: background 0.3s ease;
        }}

        .lightbox-nav:hover {{
            background: rgba(255, 255, 255, 0.3);
        }}

        .lightbox-prev {{
            left: 2rem;
        }}

        .lightbox-next {{
            right: 2rem;
        }}

        .pagination {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 1rem;
            margin-top: 2rem;
            padding: 1rem;
            background: white;
            border-radius: 15px;
            border: 1px solid rgba(167, 139, 250, 0.3);
        }}

        .pagination-btn {{
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 20px;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.95rem;
        }}

        .pagination-btn:hover:not(.disabled) {{
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(167, 139, 250, 0.4);
        }}

        .pagination-btn.disabled {{
            opacity: 0.5;
            cursor: not-allowed;
        }}

        .pagination-info {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            min-width: 100px;
            text-align: center;
        }}

        .scroll-top {{
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
        }}

        .scroll-top.active {{
            opacity: 1;
            visibility: visible;
        }}

        .footer {{
            text-align: center;
            padding: 2rem;
            border-top: 1px solid rgba(167, 139, 250, 0.3);
            margin-top: 3rem;
        }}

        .footer p {{
            color: var(--text-secondary);
            font-size: 0.95rem;
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <h1>甘城なつき</h1>
            <nav class="nav-links">
                <a href="index.html">首页</a>
                <a href="characters.html">角色介绍</a>
                <a href="main-gallery.html" class="active">主图画廊</a>
                <a href="emote-gallery.html">表情画廊</a>
            </nav>
        </div>
    </header>

    <main>
        <section class="hero-section">
            <h2>主图画廊</h2>
            <p>欣赏甘城なつき精心创作的主图插画作品，包括近期作品、早期作品、日常插画、草图、鼠标垫图、周边展示和阴暗角落等分类。</p>
        </section>

        <section class="gallery-section">
            <div class="category-tabs" id="main-tabs">
                <button data-category="recent">近期作品</button>
                <button data-category="early">早期作品</button>
                <button data-category="daily">日常插画</button>
                <button data-category="sketch">草图</button>
                <button data-category="mousepad">鼠标垫图</button>
                <button data-category="merch">周边展示</button>
                <button data-category="corner">阴暗角落</button>
            </div>
            <div class="images-grid" id="main-grid"></div>
        </section>
    </main>

    <button class="scroll-top" id="scroll-top">↑</button>

    <div class="lightbox" id="lightbox">
        <button class="lightbox-close" id="lightbox-close">×</button>
        <button class="lightbox-nav lightbox-prev" onclick="prevImage()">‹</button>
        <button class="lightbox-nav lightbox-next" onclick="nextImage()">›</button>
        <img src="" alt="" class="lightbox-content" id="lightbox-content">
    </div>

    <footer class="footer">
        <p>© 甘城なつき插画作品展示 | 仅供欣赏</p>
    </footer>

    <script>
        const mainCategories = {json.dumps(categories, ensure_ascii=False)};

        let currentImages = [];
        let currentIndex = 0;
        let mainPage = 1;
        const PAGE_SIZE = 20;

        function renderImages(gridId, category, config, page = 1) {{
            const grid = document.getElementById(gridId);
            const scrollTop = window.scrollY;
            const scrollLeft = window.scrollX;
            
            grid.innerHTML = '<div class="loading"></div>';

            setTimeout(() => {{
                grid.innerHTML = '';
                const start = (page - 1) * PAGE_SIZE;
                const end = start + PAGE_SIZE;
                const pageFiles = config.files.slice(start, end);
                const totalPages = Math.ceil(config.files.length / PAGE_SIZE);
                const urls = [];
                
                pageFiles.forEach(file => {{
                    const fullPath = config.path + '/' + encodeURI(file);
                    urls.push(fullPath);
                }});
                
                currentImages = urls.map((url, i) => ({{
                    url: url,
                    index: start + i
                }}));

                urls.forEach((url, index) => {{
                    const item = document.createElement('div');
                    item.className = 'image-item';
                    item.onclick = function() {{ openLightbox(url, index, urls); }};

                    const img = document.createElement('img');
                    img.src = url;
                    img.alt = pageFiles[index];
                    img.onerror = function() {{
                        this.parentElement.style.display = 'none';
                    }};
                    img.loading = 'lazy';

                    item.appendChild(img);
                    grid.appendChild(item);
                }});

                renderPagination(grid, gridId, page, totalPages, category, config);
                
                setTimeout(() => {{
                    window.scrollTo(scrollLeft, scrollTop);
                }}, 100);
            }}, 300);
        }}

        function renderPagination(grid, gridId, page, totalPages, category, config) {{
            const paginationId = gridId === 'main-grid' ? 'main-pagination' : 'emote-pagination';
            let pagination = document.getElementById(paginationId);
            if (!pagination) {{
                pagination = document.createElement('div');
                pagination.id = paginationId;
                pagination.className = 'pagination';
                grid.parentElement.appendChild(pagination);
            }}

            if (totalPages <= 1) {{
                pagination.innerHTML = '';
                return;
            }}

            pagination.innerHTML = '';

            const prevBtn = document.createElement('button');
            prevBtn.className = `pagination-btn ${{page === 1 ? 'disabled' : ''}}`;
            prevBtn.textContent = '上一页';
            prevBtn.addEventListener('click', function() {{
                if (page > 1) {{
                    changePage(gridId, page - 1, category, config);
                }}
            }});
            pagination.appendChild(prevBtn);

            const infoSpan = document.createElement('span');
            infoSpan.className = 'pagination-info';
            infoSpan.textContent = `第 ${{page}} / ${{totalPages}} 页`;
            pagination.appendChild(infoSpan);

            const nextBtn = document.createElement('button');
            nextBtn.className = `pagination-btn ${{page === totalPages ? 'disabled' : ''}}`;
            nextBtn.textContent = '下一页';
            nextBtn.addEventListener('click', function() {{
                if (page < totalPages) {{
                    changePage(gridId, page + 1, category, config);
                }}
            }});
            pagination.appendChild(nextBtn);
        }}

        function changePage(gridId, page, category, config) {{
            if (gridId === 'main-grid') {{
                mainPage = page;
            }} else {{
                emotePage = page;
            }}
            renderImages(gridId, category, config, page);
        }}

        function openLightbox(url, index, images) {{
            const lightbox = document.getElementById('lightbox');
            const content = document.getElementById('lightbox-content');
            content.src = url;
            currentImages = images;
            currentIndex = index;
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        }}

        function closeLightbox() {{
            const lightbox = document.getElementById('lightbox');
            lightbox.classList.remove('active');
            document.body.style.overflow = '';
        }}

        function prevImage() {{
            currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length;
            document.getElementById('lightbox-content').src = currentImages[currentIndex];
        }}

        function nextImage() {{
            currentIndex = (currentIndex + 1) % currentImages.length;
            document.getElementById('lightbox-content').src = currentImages[currentIndex];
        }}

        function initCategoryTabs(tabsId, gridId, categories) {{
            const tabs = document.getElementById(tabsId);
            const buttons = tabs.querySelectorAll('button');
            
            buttons.forEach(btn => {{
                btn.addEventListener('click', function() {{
                    buttons.forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                    
                    const category = this.dataset.category;
                    mainPage = 1;
                    renderImages(gridId, category, categories[category]);
                }});
            }});
            
            buttons[0].click();
        }}

        function initScrollTop() {{
            const scrollBtn = document.getElementById('scroll-top');
            window.addEventListener('scroll', function() {{
                if (window.scrollY > 300) {{
                    scrollBtn.classList.add('active');
                }} else {{
                    scrollBtn.classList.remove('active');
                }}
            }});
            scrollBtn.addEventListener('click', function() {{
                window.scrollTo({{ top: 0, behavior: 'smooth' }});
            }});
        }}

        document.getElementById('lightbox-close').addEventListener('click', closeLightbox);
        document.getElementById('lightbox').addEventListener('click', function(e) {{
            if (e.target === this) {{
                closeLightbox();
            }}
        }});

        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') {{
                closeLightbox();
            }} else if (e.key === 'ArrowLeft') {{
                prevImage();
            }} else if (e.key === 'ArrowRight') {{
                nextImage();
            }}
        }});

        initCategoryTabs('main-tabs', 'main-grid', mainCategories);
        initScrollTop();
    </script>
</body>
</html>'''
    
    with open('main-gallery.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("main-gallery.html generated successfully")

def generate_emote_gallery():
    categories = {
        "gura": {"name": "Gura", "path": "images/emote/gura"},
        "gura_q": {"name": "Gura Q版", "path": "images/emote/gura_q"},
        "komugi": {"name": "小麦", "path": "images/emote/komugi"},
        "kai": {"name": "小海", "path": "images/emote/kai"},
        "hazuki": {"name": "叶月", "path": "images/emote/hazuki"},
        "mari": {"name": "麻里", "path": "images/emote/mari"},
        "akami": {"name": "茜", "path": "images/emote/akami"},
        "nachoneko": {"name": "茄子猫", "path": "images/emote/nachoneko"},
        "kana": {"name": "香奈", "path": "images/emote/kana"},
        "riru": {"name": "璃瑠", "path": "images/emote/riru"},
        "sui": {"name": "翠", "path": "images/emote/sui"},
        "naname": {"name": "斜め", "path": "images/emote/naname"},
        "twitch": {"name": "Twitch", "path": "images/emote/twitch"},
        "other": {"name": "其他", "path": "images/emote/other"}
    }
    
    for key in categories:
        cat = categories[key]
        cat["files"] = get_image_files(cat["path"])
        print(f"{key}: {len(cat['files'])} files")
    
    content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>甘城なつき - 表情画廊</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --primary-color: #A78BFA;
            --secondary-color: #F9A8D4;
            --accent-color: #67E8F9;
            --bg-dark: #FDF4FF;
            --bg-card: #FCE7F3;
            --text-primary: #4C1D95;
            --text-secondary: #7C3AED;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, var(--bg-dark) 0%, #F3E8FF 50%, #ECFEFF 100%);
            color: var(--text-primary);
            min-height: 100vh;
        }}

        header {{
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(167, 139, 250, 0.3);
            position: sticky;
            top: 0;
            z-index: 100;
        }}

        .header-content {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 1.5rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        h1 {{
            font-size: 2rem;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .nav-links {{
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }}

        .nav-links a {{
            color: var(--text-secondary);
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            transition: all 0.3s ease;
        }}

        .nav-links a:hover, .nav-links a.active {{
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
        }}

        main {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .hero-section {{
            text-align: center;
            padding: 3rem 2rem;
            background: linear-gradient(135deg, rgba(167, 139, 250, 0.15) 0%, rgba(249, 168, 212, 0.15) 100%);
            border-radius: 20px;
            margin-bottom: 3rem;
            border: 1px solid rgba(167, 139, 250, 0.3);
        }}

        .hero-section h2 {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .hero-section p {{
            font-size: 1.1rem;
            color: var(--text-secondary);
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.8;
        }}

        .gallery-section {{
            margin-bottom: 3rem;
        }}

        .gallery-section h3 {{
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            color: var(--primary-color);
        }}

        .category-tabs {{
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
        }}

        .category-tabs button {{
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 25px;
            background: white;
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.95rem;
            border: 1px solid rgba(167, 139, 250, 0.3);
        }}

        .category-tabs button:hover, .category-tabs button.active {{
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
            border-color: transparent;
        }}

        .images-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 1rem;
        }}

        .image-item {{
            aspect-ratio: 1;
            border-radius: 10px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            background: linear-gradient(135deg, rgba(167, 139, 250, 0.2), rgba(249, 168, 212, 0.2));
        }}

        .image-item:hover {{
            transform: scale(1.05);
            box-shadow: 0 8px 30px rgba(167, 139, 250, 0.4);
        }}

        .image-item img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}

        .lightbox {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }}

        .lightbox.active {{
            display: flex;
        }}

        .lightbox-content {{
            max-width: 90%;
            max-height: 90%;
            object-fit: contain;
            border-radius: 10px;
        }}

        .lightbox-close {{
            position: absolute;
            top: 2rem;
            right: 2rem;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            transition: background 0.3s ease;
        }}

        .lightbox-close:hover {{
            background: rgba(255, 255, 255, 0.3);
        }}

        .lightbox-nav {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            transition: background 0.3s ease;
        }}

        .lightbox-nav:hover {{
            background: rgba(255, 255, 255, 0.3);
        }}

        .lightbox-prev {{
            left: 2rem;
        }}

        .lightbox-next {{
            right: 2rem;
        }}

        .pagination {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 1rem;
            margin-top: 2rem;
            padding: 1rem;
            background: white;
            border-radius: 15px;
            border: 1px solid rgba(167, 139, 250, 0.3);
        }}

        .pagination-btn {{
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 20px;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.95rem;
        }}

        .pagination-btn:hover:not(.disabled) {{
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(167, 139, 250, 0.4);
        }}

        .pagination-btn.disabled {{
            opacity: 0.5;
            cursor: not-allowed;
        }}

        .pagination-info {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            min-width: 100px;
            text-align: center;
        }}

        .scroll-top {{
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
        }}

        .scroll-top.active {{
            opacity: 1;
            visibility: visible;
        }}

        .footer {{
            text-align: center;
            padding: 2rem;
            border-top: 1px solid rgba(167, 139, 250, 0.3);
            margin-top: 3rem;
        }}

        .footer p {{
            color: var(--text-secondary);
            font-size: 0.95rem;
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <h1>甘城なつき</h1>
            <nav class="nav-links">
                <a href="index.html">首页</a>
                <a href="characters.html">角色介绍</a>
                <a href="main-gallery.html">主图画廊</a>
                <a href="emote-gallery.html" class="active">表情画廊</a>
            </nav>
        </div>
    </header>

    <main>
        <section class="hero-section">
            <h2>表情画廊</h2>
            <p>欣赏甘城なつき创作的各种表情插画作品，包括Gura、小麦、小海、叶月、麻里、茜、茄子猫、香奈、璃瑠、翠、斜め、Twitch等角色表情。</p>
        </section>

        <section class="gallery-section">
            <div class="category-tabs" id="emote-tabs">
                <button data-category="gura">Gura</button>
                <button data-category="gura_q">Gura Q版</button>
                <button data-category="komugi">小麦</button>
                <button data-category="kai">小海</button>
                <button data-category="hazuki">叶月</button>
                <button data-category="mari">麻里</button>
                <button data-category="akami">茜</button>
                <button data-category="nachoneko">茄子猫</button>
                <button data-category="kana">香奈</button>
                <button data-category="riru">璃瑠</button>
                <button data-category="sui">翠</button>
                <button data-category="naname">斜め</button>
                <button data-category="twitch">Twitch</button>
                <button data-category="other">其他</button>
            </div>
            <div class="images-grid" id="emote-grid"></div>
        </section>
    </main>

    <button class="scroll-top" id="scroll-top">↑</button>

    <div class="lightbox" id="lightbox">
        <button class="lightbox-close" id="lightbox-close">×</button>
        <button class="lightbox-nav lightbox-prev" onclick="prevImage()">‹</button>
        <button class="lightbox-nav lightbox-next" onclick="nextImage()">›</button>
        <img src="" alt="" class="lightbox-content" id="lightbox-content">
    </div>

    <footer class="footer">
        <p>© 甘城なつき插画作品展示 | 仅供欣赏</p>
    </footer>

    <script>
        const emoteCategories = {json.dumps(categories, ensure_ascii=False)};

        let currentImages = [];
        let currentIndex = 0;
        let emotePage = 1;
        const PAGE_SIZE = 20;

        function renderImages(gridId, category, config, page = 1) {{
            const grid = document.getElementById(gridId);
            const scrollTop = window.scrollY;
            const scrollLeft = window.scrollX;
            
            grid.innerHTML = '<div class="loading"></div>';

            setTimeout(() => {{
                grid.innerHTML = '';
                const start = (page - 1) * PAGE_SIZE;
                const end = start + PAGE_SIZE;
                const pageFiles = config.files.slice(start, end);
                const totalPages = Math.ceil(config.files.length / PAGE_SIZE);
                const urls = [];
                
                pageFiles.forEach(file => {{
                    const fullPath = config.path + '/' + encodeURI(file);
                    urls.push(fullPath);
                }});
                
                currentImages = urls.map((url, i) => ({{
                    url: url,
                    index: start + i
                }}));

                urls.forEach((url, index) => {{
                    const item = document.createElement('div');
                    item.className = 'image-item';
                    item.onclick = function() {{ openLightbox(url, index, urls); }};

                    const img = document.createElement('img');
                    img.src = url;
                    img.alt = pageFiles[index];
                    img.onerror = function() {{
                        this.parentElement.style.display = 'none';
                    }};
                    img.loading = 'lazy';

                    item.appendChild(img);
                    grid.appendChild(item);
                }});

                renderPagination(grid, gridId, page, totalPages, category, config);
                
                setTimeout(() => {{
                    window.scrollTo(scrollLeft, scrollTop);
                }}, 100);
            }}, 300);
        }}

        function renderPagination(grid, gridId, page, totalPages, category, config) {{
            const paginationId = gridId === 'main-grid' ? 'main-pagination' : 'emote-pagination';
            let pagination = document.getElementById(paginationId);
            if (!pagination) {{
                pagination = document.createElement('div');
                pagination.id = paginationId;
                pagination.className = 'pagination';
                grid.parentElement.appendChild(pagination);
            }}

            if (totalPages <= 1) {{
                pagination.innerHTML = '';
                return;
            }}

            pagination.innerHTML = '';

            const prevBtn = document.createElement('button');
            prevBtn.className = `pagination-btn ${{page === 1 ? 'disabled' : ''}}`;
            prevBtn.textContent = '上一页';
            prevBtn.addEventListener('click', function() {{
                if (page > 1) {{
                    changePage(gridId, page - 1, category, config);
                }}
            }});
            pagination.appendChild(prevBtn);

            const infoSpan = document.createElement('span');
            infoSpan.className = 'pagination-info';
            infoSpan.textContent = `第 ${{page}} / ${{totalPages}} 页`;
            pagination.appendChild(infoSpan);

            const nextBtn = document.createElement('button');
            nextBtn.className = `pagination-btn ${{page === totalPages ? 'disabled' : ''}}`;
            nextBtn.textContent = '下一页';
            nextBtn.addEventListener('click', function() {{
                if (page < totalPages) {{
                    changePage(gridId, page + 1, category, config);
                }}
            }});
            pagination.appendChild(nextBtn);
        }}

        function changePage(gridId, page, category, config) {{
            if (gridId === 'main-grid') {{
                mainPage = page;
            }} else {{
                emotePage = page;
            }}
            renderImages(gridId, category, config, page);
        }}

        function openLightbox(url, index, images) {{
            const lightbox = document.getElementById('lightbox');
            const content = document.getElementById('lightbox-content');
            content.src = url;
            currentImages = images;
            currentIndex = index;
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        }}

        function closeLightbox() {{
            const lightbox = document.getElementById('lightbox');
            lightbox.classList.remove('active');
            document.body.style.overflow = '';
        }}

        function prevImage() {{
            currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length;
            document.getElementById('lightbox-content').src = currentImages[currentIndex];
        }}

        function nextImage() {{
            currentIndex = (currentIndex + 1) % currentImages.length;
            document.getElementById('lightbox-content').src = currentImages[currentIndex];
        }}

        function initCategoryTabs(tabsId, gridId, categories) {{
            const tabs = document.getElementById(tabsId);
            const buttons = tabs.querySelectorAll('button');
            
            buttons.forEach(btn => {{
                btn.addEventListener('click', function() {{
                    buttons.forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                    
                    const category = this.dataset.category;
                    emotePage = 1;
                    renderImages(gridId, category, categories[category]);
                }});
            }});
            
            buttons[0].click();
        }}

        function initScrollTop() {{
            const scrollBtn = document.getElementById('scroll-top');
            window.addEventListener('scroll', function() {{
                if (window.scrollY > 300) {{
                    scrollBtn.classList.add('active');
                }} else {{
                    scrollBtn.classList.remove('active');
                }}
            }});
            scrollBtn.addEventListener('click', function() {{
                window.scrollTo({{ top: 0, behavior: 'smooth' }});
            }});
        }}

        document.getElementById('lightbox-close').addEventListener('click', closeLightbox);
        document.getElementById('lightbox').addEventListener('click', function(e) {{
            if (e.target === this) {{
                closeLightbox();
            }}
        }});

        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') {{
                closeLightbox();
            }} else if (e.key === 'ArrowLeft') {{
                prevImage();
            }} else if (e.key === 'ArrowRight') {{
                nextImage();
            }}
        }});

        initCategoryTabs('emote-tabs', 'emote-grid', emoteCategories);
        initScrollTop();
    </script>
</body>
</html>'''
    
    with open('emote-gallery.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("emote-gallery.html generated successfully")

if __name__ == '__main__':
    generate_main_gallery()
    generate_emote_gallery()
    print("All HTML files generated!")
