"""Sub-hub pages generation - uses full_page() for consistent styling"""
import os, re, sys

def generate_subhub_pages(base_dir):
    """Generate all sub-hub pages using full_page()"""
    sys.path.insert(0, base_dir)
    from _components import full_page
    
    upload_dir = os.path.join(base_dir, '..', 'foneclaw-deploy', 'uploads', '2026-05-25_1750')
    
    subhubs = {
        'comparisons/foneclaw-vs': {
            'title': 'FoneClaw vs Siri, Alexa & Google',
            'desc': '20 head-to-head comparisons with major voice assistants.',
            'canonical': '/comparisons/foneclaw-vs/index.html',
            'gradient': 'linear-gradient(135deg, #7C2D12, #0F172A)',
            'hero_img': '/images/hub/hub-category-fc-vs-x.jpg',
            'stats': [{'num':'20','label':'Comparisons'},{'num':'12+','label':'Competitors'},{'num':'2026','label':'Updated'}],
            'tabs': [
                {'filter': 'all', 'label': 'All'},
                {'filter': 'tech-giants', 'label': '🏢 Tech Giants'},
                {'filter': 'ai-assistants', 'label': '🤖 AI Assistants'},
                {'filter': 'other', 'label': '📊 Other'},
            ],
            'categories': {
                'Google': 'tech-giants', 'Apple': 'tech-giants', 'Samsung': 'tech-giants', 'Amazon': 'tech-giants',
                'AI Agent': 'ai-assistants', 'AI Model': 'ai-assistants', 'AI Assistant': 'ai-assistants',
                'Phone Agent': 'ai-assistants', 'Xiaomi': 'ai-assistants', 'Tencent': 'ai-assistants',
                'Wearable': 'other', 'Offline': 'other', 'Multi': 'other', 'General': 'other', 'Creative': 'other',
            },
            'cta_title': 'Ready to Compare?',
            'cta_desc': 'See how FoneClaw stacks up against the competition.',
        },
        'comparisons/tech-analysis': {
            'title': 'AI Agent Technology Deep Dives',
            'desc': '25 in-depth technical analyses of AI agent architecture and trends.',
            'canonical': '/comparisons/tech-analysis/index.html',
            'gradient': 'linear-gradient(135deg, #1E3A5F, #0F172A)',
            'hero_img': '/images/hub/hub-category-tech-analysis.jpg',
            'stats': [{'num':'25','label':'Analyses'},{'num':'8','label':'Topics'},{'num':'2026','label':'Updated'}],
            'tabs': [
                {'filter': 'all', 'label': 'All'},
                {'filter': 'trends', 'label': '📈 Trends'},
                {'filter': 'technical', 'label': '⚙️ Technical'},
                {'filter': 'trust-cost', 'label': '🔒 Trust & Cost'},
            ],
            'categories': {
                'Trend': 'trends', 'Ranking': 'trends', 'Landscape': 'trends', 'Guide': 'trends',
                'Technical': 'technical', 'Hardware': 'technical', 'Platform': 'technical', 'Search': 'technical',
                'Security': 'trust-cost', 'Cost': 'trust-cost', 'Reliability': 'trust-cost', 'Accessibility': 'trust-cost',
            },
            'cta_title': 'Ready to Compare?',
            'cta_desc': 'See how FoneClaw stacks up against the competition.',
        },
        'ai-agent/gemini-intelligence': {
            'title': 'Gemini Intelligence Complete Guide',
            'desc': '8 guides covering Gemini Intelligence features, setup, and usage.',
            'canonical': '/ai-agent/gemini-intelligence/index.html',
            'gradient': 'linear-gradient(135deg, #4C1D95, #0F172A)',
            'hero_img': '/images/hub/hub-category-gemini.jpg',
            'stats': [{'num':'8','label':'Guides'},{'num':'5','label':'Features'},{'num':'10+','label':'Devices'}],
            'tabs': [
                {'filter': 'all', 'label': 'All'},
                {'filter': 'guides', 'label': '📖 Guides'},
                {'filter': 'features', 'label': '✨ Features'},
            ],
            'categories': {
                'Guide': 'guides', 'Voice': 'guides', 'Productivity': 'guides',
                'Feature': 'features', 'Analysis': 'features',
            },
            'cta_title': 'Ready to Try Gemini Intelligence?',
            'cta_desc': 'Start using AI agents on your phone today.',
        },
        'ai-agent/other': {
            'title': 'AI Agent Deep Dives',
            'desc': '17 articles on AI agent technology, architecture, and trends.',
            'canonical': '/ai-agent/other/index.html',
            'gradient': 'linear-gradient(135deg, #581C87, #0F172A)',
            'hero_img': '/images/hub/hub-category-agent.jpg',
            'stats': [{'num':'17','label':'Articles'},{'num':'6','label':'Topics'},{'num':'2026','label':'Updated'}],
            'tabs': [
                {'filter': 'all', 'label': 'All'},
                {'filter': 'technical', 'label': '⚙️ Technical'},
                {'filter': 'news-trends', 'label': '📰 News & Trends'},
            ],
            'categories': {
                'Technical': 'technical', 'Product': 'technical', 'Explainer': 'technical',
                'News': 'news-trends', 'Trend': 'news-trends', 'Analysis': 'news-trends',
                'Guide': 'news-trends', 'Feature': 'news-trends', 'AI Agent Trends': 'news-trends',
            },
            'cta_title': 'Ready to Go AI-Native?',
            'cta_desc': 'Start using AI agents on your phone today.',
        },
    }
    
    def extract_cards_from_hub(hub_slug, categories):
        """Extract articles from main hub page, filtered by category"""
        hub_path = os.path.join(upload_dir, f'{hub_slug}/index.html')
        if not os.path.exists(hub_path):
            return []
        
        with open(hub_path) as f:
            html = f.read()
        
        lines = html.split('\n')
        cards = []
        current_card = None
        
        for line in lines:
            if 'class="article-card"' in line and 'href=' in line:
                href = re.search(r'href="([^"]+)"', line)
                if href:
                    current_card = {'href': href.group(1), 'html': line}
            elif current_card and '</a>' in line:
                current_card['html'] += line
                cards.append(current_card)
                current_card = None
            elif current_card:
                current_card['html'] += line
        
        result = []
        for card in cards:
            tag = re.search(r'class="card-tag"[^>]*>([^<]+)<', card['html'])
            title = re.search(r'class="card-title"[^>]*>([^<]+)<', card['html'])
            desc = re.search(r'class="card-desc"[^>]*>([^<]+)<', card['html'])
            time = re.search(r'⏱️\s*(\d+\s*min)', card['html'])
            
            if title and tag:
                tag_text = tag.group(1).strip()
                # Check if this article belongs to this sub-hub
                if tag_text in categories:
                    result.append({
                        'href': card['href'],
                        'tag': tag_text,
                        'title': title.group(1).strip(),
                        'desc': desc.group(1).strip() if desc else '',
                        'time': time.group(1).strip() if time else '5 min',
                    })
        return result
    
    for slug, config in subhubs.items():
        # Read existing sub-hub page
        page_path = os.path.join(upload_dir, slug, 'index.html')
        if not os.path.exists(page_path):
            print(f"  Skip {slug}: not found")
            continue
        
        with open(page_path) as f:
            html = f.read()
        
        # Extract articles
        articles = extract_cards_from_hub(slug.split("/")[0], config["categories"])
        if not articles:
            print(f"  Skip {slug}: no articles found")
            continue
        
        if slug == 'ai-agent/gemini-intelligence' and not any(a.get('href') == '/gemini-intelligence-supported-devices.html' for a in articles):
            articles.append({
                'href': '/gemini-intelligence-supported-devices.html',
                'tag': 'Guide',
                'title': 'Gemini Intelligence Supported Devices List 2026',
                'desc': 'Check Pixel, Samsung, Xiaomi, OnePlus, and Android compatibility for Gemini Intelligence.',
                'time': '10 min',
                'category': 'guides',
            })
        if slug == 'ai-agent/other':
            forced_articles = [
                {
                    'href': '/jd-tencent-ai-agent-shopping-phone-agent.html',
                    'tag': 'AI Agent Trends',
                    'title': 'JD Tencent AI Agent: Shopping Agents Begin',
                    'desc': 'Why shopping agents need phone-level execution, safe approval, and real app control.',
                    'time': '9 min',
                },
                {
                    'href': '/wechat-ai-agent-commandable-super-app.html',
                    'tag': 'AI Agent Trends',
                    'title': 'WeChat AI Agent: Commandable Super App',
                    'desc': 'Where single-app agents end and system-level phone agents begin.',
                    'time': '9 min',
                },
            ]
            for forced in forced_articles:
                if not any(a.get('href') == forced['href'] for a in articles):
                    articles.append(forced)
        # Add data-category to articles
        for art in articles:
            art['category'] = config['categories'].get(art['tag'], 'other')
        
        # Build cards HTML
        cards_html = ""
        for art in articles:
            slug_name = art['href'].replace('/', '').replace('.html', '')
            thumb = f'/images/cards/{slug_name}.jpg'
            article_thumb = os.path.join(base_dir, 'images', 'articles', f'{slug_name}.jpg')
            if os.path.exists(article_thumb):
                thumb = f'/images/articles/{slug_name}.jpg'
            cards_html += f'''<a href="{art['href']}" class="article-card" data-category="{art['category']}">
      <div class="card-img" style="background:url('{thumb}') center/cover"></div>
      <div class="card-body">
        <span class="card-tag">{art['tag']}</span>
        <div class="card-title">{art['title']}</div>
        <div class="card-desc">{art['desc']}</div>
        <div class="card-meta"><span>⏱️ {art['time']}</span><span>Read →</span></div>
      </div>
    </a>'''
        
        # Generate tabs HTML
        tabs_html = "\n".join([
            f'<button class="tab-btn{" active" if t["filter"]=="all" else ""}" data-filter="{t["filter"]}">{t["label"]}</button>'
            for t in config['tabs']
        ])
        
        # Build hub body
        stats_html = "\n".join([f'<div class="hub-stat"><div class="num">{s["num"]}</div><div class="label">{s["label"]}</div></div>' for s in config['stats']])
        
        hub_body = f"""
<section class="hub-hero">
  <h1>{config['title']}</h1>
  <p class="subtitle">{config['desc']}</p>
  <div class="hub-stats">{stats_html}</div>
  <div class="hub-cta"><a href="#articles" class="bp">Explore Guides</a><a href="/download.html" class="bo">Get FoneClaw</a></div>
</section>
<nav class="hub-tabs">
{tabs_html}
</nav>
<section class="hub-section" id="articles"><h2>All Guides</h2><div class="article-grid">{cards_html}</div></section>
<section class="cta-section"><h2>{config['cta_title']}</h2><p>{config['cta_desc']}</p><a href="/download.html" class="bp">Download FoneClaw Free</a></section>
<script>
document.querySelectorAll('.tab-btn').forEach(b=>{{b.addEventListener('click',()=>{{document.querySelectorAll('.tab-btn').forEach(x=>x.classList.remove('active'));b.classList.add('active');const f=b.dataset.filter;document.querySelectorAll('.article-card').forEach(c=>{{c.style.display=(f==='all'||c.dataset.category===f)?'':'none'}})}})}});
</script>"""
        
        # Use full_page()
        # Hub CSS
        hub_css = """<style>
.hub-hero{background:''' + config['gradient'] + ''';padding:80px 20px 60px;text-align:center;position:relative;overflow:hidden}
.hub-hero::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:url(''' + config['hero_img'] + ''') center/cover;opacity:0.15}
.hub-hero>*{position:relative;z-index:1}
.hub-hero h1{font-size:clamp(32px,5vw,48px);font-weight:700;margin-bottom:12px;color:#f0f4f8}
.hub-hero .subtitle{color:#8b949e;font-size:18px;max-width:600px;margin:0 auto 24px}
.hub-stats{display:flex;justify-content:center;gap:48px;margin:32px 0}
.hub-stat{text-align:center}.hub-stat .num{font-size:2rem;font-weight:700;color:#00d4ff}.hub-stat .label{font-size:0.85rem;color:#8b949e;text-transform:uppercase;letter-spacing:1px}
.hub-cta{display:flex;gap:16px;justify-content:center;margin-top:24px}
.hub-tabs{display:flex;justify-content:center;gap:8px;padding:24px 20px;flex-wrap:wrap;border-bottom:1px solid #21262d;position:sticky;top:50px;background:#0d1117;z-index:100}
.tab-btn{padding:10px 20px;border-radius:20px;border:1px solid #30363d;background:transparent;color:#8b949e;cursor:pointer;font-size:0.9rem;transition:all 0.2s}.tab-btn:hover{border-color:#00d4ff;color:#00d4ff}.tab-btn.active{background:#00d4ff;border-color:#00d4ff;color:#080c18}
.hub-section{max-width:1000px;margin:48px auto;padding:0 20px}.hub-section h2{font-size:1.5rem;margin-bottom:24px;color:#f0f4f8}
.article-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px}.article-card{background:#161b22;border-radius:10px;border:1px solid #21262d;overflow:hidden;transition:all 0.3s;display:block;text-decoration:none}.article-card:hover{border-color:#00d4ff;transform:translateY(-3px)}.card-img{height:160px;background:#21262d;background-size:cover;background-position:center}.card-body{padding:16px}.card-tag{display:inline-block;background:rgba(63,185,80,0.1);color:#3fb950;padding:3px 8px;border-radius:6px;font-size:0.7rem;font-weight:600;margin-bottom:8px}.card-title{font-size:1rem;font-weight:600;margin-bottom:6px;color:#f0f4f8}.card-desc{color:#8b949e;font-size:0.85rem;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}.card-meta{display:flex;justify-content:space-between;color:#6e7681;font-size:0.75rem;margin-top:8px}
.cta-section{background:#161b22;border-top:1px solid #21262d;padding:60px 20px;text-align:center;margin-top:48px}.cta-section h2{font-size:1.8rem;margin-bottom:10px;color:#f0f4f8}.cta-section p{color:#8b949e;margin-bottom:24px}
@media(max-width:768px){.hub-hero h1{font-size:2rem}.hub-stats{flex-direction:column;gap:16px}.article-grid{grid-template-columns:1fr}.tab-btn{padding:8px 14px;font-size:0.8rem}}
</style>"""
        
        page_html = full_page(
            f"{config['title']} - FoneClaw",
            config['desc'],
            config['canonical'],
            3,
            hub_body,
            extra_css=hub_css,
            og_image=f"https://www.foneclaw.ai{config['hero_img']}"
        )
        
        # Write file
        out_path = os.path.join(upload_dir, slug, 'index.html')
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(page_html)
        
        print(f"  Generated: {slug}/index.html ({len(page_html)//1024}KB, {len(articles)} articles)")

# Run
print("\nAll sub-hub pages regenerated!")
