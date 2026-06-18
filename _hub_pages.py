"""Hub pages generation - uses full_page() for proper CSS/JS/components"""
import os, re, sys

def generate_hub_pages(base_dir):
    """Generate all hub pages using full_page()"""
    sys.path.insert(0, base_dir)
    from _components import full_page
    
    upload_dir = os.path.join(base_dir, '..', 'foneclaw-deploy', 'uploads', '2026-05-25_1750')
    
    # Hub configurations with tabs and featured content
    hubs = {
        'voice-control': {
            'title': 'Voice Control Android',
            'desc': '35 voice control tutorials covering WhatsApp, YouTube, TikTok, and 30+ apps. Learn hands-free phone control for driving, cooking, and accessibility.',
            'canonical': '/voice-control/index.html',
            'gradient': 'linear-gradient(135deg, #1E3A5F, #0F172A)',
            'hero_img': '/images/hub/hub-hero-voice-control.jpg',
            'stats': [{'num':'35','label':'Guides'},{'num':'12+','label':'Apps'},{'num':'9','label':'Use Cases'}],
            'cta_title': 'Ready to Go Hands-Free?',
            'cta_desc': 'Start controlling your Android phone with your voice today.',
            'tabs': [
                {'filter': 'all', 'label': 'All'},
                {'filter': 'apps', 'label': '📱 Apps'},
                {'filter': 'usecases', 'label': '🎯 Use Cases'},
                {'filter': 'safety', 'label': '🛡️ Safety'},
                {'filter': 'setup', 'label': '⚙️ Setup'},
            ],
            'featured': {
                'img': '/images/hub/hub-category-apps.jpg',
                'tag': 'Most Popular',
                'title': 'Voice Control for Your Apps',
                'desc': 'Control WhatsApp, YouTube, TikTok, and 30+ apps with simple voice commands. No touching required.',
                'link': '/voice-control-android.html'
            },
        },
        'comparisons': {
            'title': 'FoneClaw Comparisons',
            'sub_hubs': [
                {'slug': 'foneclaw-vs', 'title': 'FoneClaw vs', 'desc': '20 detailed head-to-head comparisons with competing AI assistants.', 'icon': '⚔️'},
                {'slug': 'tech-analysis', 'title': 'Tech Analysis', 'desc': '25 deep industry analyses of phone AI agent technology and trends.', 'icon': '📊'},
            ],
            'desc': '46 head-to-head comparisons: FoneClaw vs Siri, Alexa, Google Assistant, Samsung, Xiaomi, and more. See which AI phone agent wins in 2026.',
            'canonical': '/comparisons/index.html',
            'gradient': 'linear-gradient(135deg, #451A03, #0F172A)',
            'hero_img': '/images/hub/hub-hero-comparisons.jpg',
            'stats': [{'num':'46','label':'Guides'},{'num':'20+','label':'Competitors'},{'num':'2','label':'Categories'}],
            'cta_title': 'Ready to Compare?',
            'cta_desc': 'See how FoneClaw stacks up against the competition.',
            'tabs': [
                {'filter': 'all', 'label': 'All'},
                {'filter': 'fc-vs-x', 'label': '⚔️ FoneClaw vs'},
                {'filter': 'tech-analysis', 'label': '📊 Tech Analysis'},
            ],
            'featured': {
                'img': '/images/hub/hub-category-fc-vs-x.jpg',
                'tag': 'Head to Head',
                'title': 'FoneClaw vs Siri',
                'desc': 'Local AI agent vs Apple cloud-based assistant. See which voice control solution wins.',
                'link': '/foneclaw-vs-siri.html'
            },
        },
        'ai-agent': {
            'title': 'AI Agent Technology',
            'sub_hubs': [
                {'slug': 'gemini-intelligence', 'title': 'Gemini Intelligence', 'desc': '8 comprehensive guides to Gemini Intelligence features and capabilities.', 'icon': '✨'},
                {'slug': 'other', 'title': 'Other AI Agents', 'desc': '17 in-depth guides to AI agent architecture and phone automation.', 'icon': '🤖'},
            ],
            'desc': '25 deep dives into phone AI agent architecture, Gemini Intelligence features, and the future of mobile AI. Technical guides and industry analysis.',
            'canonical': '/ai-agent/index.html',
            'gradient': 'linear-gradient(135deg, #3B0764, #0F172A)',
            'hero_img': '/images/hub/hub-hero-ai-agent.jpg',
            'stats': [{'num':'25','label':'Guides'},{'num':'8','label':'Gemini Intel'},{'num':'17','label':'AI Agent'}],
            'cta_title': 'Ready to Go AI-Native?',
            'cta_desc': 'Start using AI agents on your phone today.',
            'tabs': [
                {'filter': 'all', 'label': 'All'},
                {'filter': 'gemini', 'label': '✨ Gemini Intelligence'},
                {'filter': 'agent', 'label': '🤖 AI Agent'},
            ],
            'featured': {
                'img': '/images/hub/hub-category-gemini.jpg',
                'tag': 'Deep Dive',
                'title': 'Gemini Intelligence Explained',
                'desc': 'Google AI ecosystem updates and announcements for phone AI agents.',
                'link': '/gemini-intelligence-complete-guide.html'
            },
        },
        'news': {
            'title': 'Industry News',
            'desc': '15 latest AI phone agent news from Apple, Google, Xiaomi, Samsung, and the AI ecosystem. Industry trends, product launches, and technology updates.',
            'canonical': '/news/index.html',
            'gradient': 'linear-gradient(135deg, #064E3B, #0F172A)',
            'hero_img': '/images/hub/hub-hero-news.jpg',
            'stats': [{'num':'15','label':'Articles'},{'num':'6','label':'Companies'},{'num':'2026','label':'Updated'}],
            'cta_title': 'Stay Updated',
            'cta_desc': 'Follow the latest developments in AI agent technology.',
            'tabs': [
                {'filter': 'all', 'label': 'All'},
                {'filter': 'companies', 'label': '🏢 Companies'},
                {'filter': 'products', 'label': '📱 Products'},
                {'filter': 'events', 'label': '📅 Events'},
                {'filter': 'industry', 'label': '📊 Industry'},
            ],
            'featured': {
                'img': '/images/hub/hub-card-news.jpg',
                'tag': 'Breaking',
                'title': 'AI Phone War 2026',
                'desc': 'OpenAI vs ByteDance vs Google. The battle for AI on your phone has begun.',
                'link': '/ai-phone-war-2026.html'
            },
        },
    }
    
    # Hub-specific category mappings
    HUB_CATEGORY_MAP = {
        'voice-control': {
            'Messaging': 'apps', 'Video': 'apps', 'Social': 'apps', 'Professional': 'apps',
            'Safety': 'safety', 'Home': 'usecases', 'Devices': 'usecases', 'Fitness': 'usecases',
            'Travel': 'usecases', 'Privacy': 'setup', 'Accessibility': 'setup', 'Guide': 'setup',
            'Ranking': 'setup', 'Advanced': 'setup', 'Productivity': 'usecases', 'AI': 'setup',
            'Business': 'usecases', 'Smart Home': 'usecases',
        },
        'comparisons': {
            # FoneClaw vs X (direct competitor comparisons)
            'Apple': 'fc-vs-x', 'Amazon': 'fc-vs-x', 'Google': 'fc-vs-x',
            'Samsung': 'fc-vs-x', 'Xiaomi': 'fc-vs-x', 'Tencent': 'fc-vs-x',
            'General': 'fc-vs-x', 'Creative': 'fc-vs-x', 'Phone Agent': 'fc-vs-x',
            'AI Model': 'fc-vs-x', 'AI Agent': 'fc-vs-x', 'AI Assistant': 'fc-vs-x',
            'Offline': 'fc-vs-x', 'Multi': 'fc-vs-x', 'Wearable': 'fc-vs-x',
            'Ranking': 'fc-vs-x', 'Guide': 'fc-vs-x',
            'Comparisons': 'fc-vs-x',  # 通用比较类文章
            # Tech Analysis (industry analysis & trends)
            'Trend': 'tech-analysis', 'Hardware': 'tech-analysis', 'Technical': 'tech-analysis',
            'Security': 'tech-analysis', 'Cost': 'tech-analysis', 'Search': 'tech-analysis',
            'Platform': 'tech-analysis', 'Landscape': 'tech-analysis',
            'Reliability': 'tech-analysis', 'Accessibility': 'tech-analysis',
        },
        'ai-agent': {
            # Gemini Intelligence sub-articles
            'Guide': 'gemini', 'Feature': 'gemini', 'Voice': 'gemini',
            'Productivity': 'gemini',
            # AI Agent sub-articles
            'Technical': 'agent', 'News': 'agent', 'Analysis': 'agent',
            'Trend': 'agent', 'Product': 'agent', 'Explainer': 'agent',
            'AI Agent Trends': 'news-trends',  # AI代理趋势文章
            'Industry and Trends': 'agent',
        },
        'news': {
            'Xiaomi': 'companies', 'Huawei': 'companies', 'Samsung': 'companies',
            'Microsoft': 'companies', 'Apple': 'companies',
            'Product': 'products', 'Hardware': 'products', 'Feature': 'products',
            'Event': 'events', 'War': 'events', 'Politics': 'events',
            'Marketing': 'industry', 'Security': 'industry',
            'Guide': 'industry', 'Analysis': 'industry', 'Trend': 'industry',
            'Industry': 'industry', 'Industry & Trends': 'industry', 'Industry and Trends': 'industry',  # 行业分析文章
        },
        # Sub-hub: Comparisons - FoneClaw vs
        'foneclaw-vs': {
            'Google': 'tech-giants', 'Apple': 'tech-giants', 'Samsung': 'tech-giants', 'Amazon': 'tech-giants',
            'AI Agent': 'ai-assistants', 'AI Model': 'ai-assistants', 'AI Assistant': 'ai-assistants',
            'Phone Agent': 'ai-assistants', 'Xiaomi': 'ai-assistants', 'Tencent': 'ai-assistants',
            'Wearable': 'other', 'Offline': 'other', 'Multi': 'other', 'General': 'other', 'Creative': 'other',
        },
        # Sub-hub: Comparisons - Tech Analysis
        'tech-analysis': {
            'Trend': 'trends', 'Ranking': 'trends', 'Landscape': 'trends', 'Guide': 'trends',
            'Technical': 'technical', 'Hardware': 'technical', 'Platform': 'technical', 'Search': 'technical',
            'Security': 'trust-cost', 'Cost': 'trust-cost', 'Reliability': 'trust-cost', 'Accessibility': 'trust-cost',
        },
        # Sub-hub: AI Agent - Gemini Intelligence
        'gemini-intelligence': {
            'Guide': 'guides', 'Voice': 'guides', 'Productivity': 'guides',
            'Feature': 'features', 'Analysis': 'features',
        },
        # Sub-hub: AI Agent - Other
        'other': {
            'Technical': 'technical', 'Product': 'technical', 'Explainer': 'technical',
            'News': 'news-trends', 'Trend': 'news-trends', 'Analysis': 'news-trends',
            'Guide': 'news-trends', 'Feature': 'news-trends', 'Industry and Trends': 'news-trends',
        },
    }

    def fix_card_categories(html, hub_slug=''):
        """Add data-category attributes to article cards based on their card-tag text"""
        def add_category(match):
            card_html = match.group(0)
            # Extract card-tag text
            tag_match = re.search(r'class="card-tag"[^>]*>([^<]+)<', card_html)
            if tag_match:
                tag_text = tag_match.group(1).strip()
                category_map = HUB_CATEGORY_MAP.get(hub_slug, {})
                category = category_map.get(tag_text, tag_text.lower().replace(' ', '-'))
                # Add data-category to the <a> tag
                card_html = re.sub(
                    r'class="article-card"(?:\s+data-category="[^"]*")?',
                    f'class="article-card" data-category="{category}"',
                    card_html
                )
            return card_html
        
        # Match each article card
        fixed = re.sub(
            r'<a href="[^"]+" class="article-card"[^>]*>[\s\S]*?</a>',
            add_category,
            html
        )
        return fixed

    def update_specific_cards(html):
        """Keep legacy hardcoded hub cards in sync with updated article titles/descriptions."""
        replacements = {
            'xiaomi-ai-ecosystem-2026': {
                'title': 'Xiaomi HyperOS AI Capabilities 2026',
                'desc': 'MiMo-V2.5, HyperAI, HyperConnect, and Xiaomi ecosystem features.',
                'time': '9 min',
            },
            'voice-control-visually-impaired': {
                'title': 'Voice Activated Phone for Blind Users',
                'desc': 'Android Voice Access, TalkBack, and FoneClaw for screen-free phone control.',
                'time': '9 min',
            },
            'miclaw-vs-foneclaw': {
                'title': 'Xiaomi MiClaw vs FoneClaw Phone Agent',
                'desc': 'Closed beta, HyperOS lock-in, MiMo support, WeChat access, and independent Android voice control.',
                'time': '7 min',
            },
            'wwdc-2026-ai-do-over-phone-agent': {
                'title': 'WWDC 2026 Siri AI and Apple Intelligence',
                'desc': 'Siri AI, Gemini-powered models, App Intents, and what Apple means for Android phone agents.',
                'time': '7 min',
            },
            'agentic-ai-phone-explained': {
                'title': 'Agentic AI Phone: MiClaw, Gemini, Siri AI',
                'desc': 'Compare Xiaomi MiClaw, Google Gemini Intelligence, Apple Siri AI, and FoneClaw Android phone agents.',
                'time': '8 min',
            },
            'gemini-vs-foneclaw': {
                'title': 'Gemini Intelligence vs FoneClaw',
                'desc': 'Android phone agent access, cross-app automation, device limits, and hands-free execution.',
                'time': '6 min',
            },
        }
        for slug_key, data in replacements.items():
            pattern = r'(<a href="/' + re.escape(slug_key) + r'\.html" class="article-card"[^>]*>[\s\S]*?<div class="card-title">)(.*?)(</div>[\s\S]*?<div class="card-desc">)(.*?)(</div>[\s\S]*?<div class="card-meta"><span>⏱️ )(.*?)(</span><span>Read →</span></div>[\s\S]*?</a>)'
            html = re.sub(
                pattern,
                lambda m: m.group(1) + data['title'] + m.group(3) + data['desc'] + m.group(5) + data['time'] + m.group(7),
                html,
                flags=re.DOTALL,
            )
        return html

    def fix_card_images(html):
        """Fix article card images to use individual article images instead of category images"""
        # Step 1: Fix broken <a> tags (missing closing >)
        # Pattern: <a href="..." class="article-card"\n  -> <a href="..." class="article-card">\n
        html = re.sub(
            r'<a href="([^"]+)" class="article-card"\n',
            r'<a href="\1" class="article-card">\n',
            html
        )
        
        # Step 2: Replace card-img backgrounds with article images
        def replace_card(match):
            full = match.group(0)
            href = match.group(1)
            slug = href.replace('/', '').replace('.html', '')
            article_img = f'/images/articles/{slug}.jpg'
            return re.sub(
                r"background:url\('[^']*'\) center/cover",
                f"background:url('{article_img}') center/cover",
                full
            )
        
        fixed = re.sub(
            r'<a href="([^"]+)" class="article-card">[\s\S]*?</a>',
            replace_card,
            html
        )
        return fixed
    
    for slug, config in hubs.items():
        # Read existing page to extract cards
        page_path = os.path.join(upload_dir, slug, 'index.html')
        if not os.path.exists(page_path):
            print(f"  ⚠️ Missing: {slug}")
            continue
        
        with open(page_path) as f:
            existing = f.read()
        
        # Extract cards from existing page and fix images
        cards_match = re.search(r'<div class="article-grid">(.*?)</div>\s*</section>', existing, re.DOTALL)
        cards = cards_match.group(1) if cards_match else ''
        cards = fix_card_images(cards)
        print(f"  Before fix_card_categories: {len(cards)} chars, {cards.count('data-category')} data-category attrs")
        cards = fix_card_categories(cards, slug)
        cards = update_specific_cards(cards)
        print(f"  After fix_card_categories: {len(cards)} chars, {cards.count('data-category')} data-category attrs")
        
        if slug == 'ai-agent' and 'gemini-intelligence-supported-devices.html' not in cards:
            cards += '''<a href="/gemini-intelligence-supported-devices.html" class="article-card" data-category="gemini">
      <div class="card-img" style="background:url('/images/articles/gemini-intelligence-supported-devices.jpg') center/cover"></div>
      <div class="card-body">
        <span class="card-tag">Guide</span>
        <div class="card-title">Gemini Intelligence Supported Devices List 2026</div>
        <div class="card-desc">Check Pixel, Samsung, Xiaomi, OnePlus, and Android compatibility for Gemini Intelligence.</div>
        <div class="card-meta"><span>⏱️ 10 min</span><span>Read →</span></div>
      </div>
    </a>'''
        agentic_card = '''<a href="/agentic-ai-phone-explained.html" class="article-card" data-category="agent">
      <div class="card-img" style="background:url('/images/articles/agentic-ai-phone-explained.jpg') center/cover"></div>
      <div class="card-body">
        <span class="card-tag">Industry and Trends</span>
        <div class="card-title">Agentic AI Phone: MiClaw, Gemini, Siri AI</div>
        <div class="card-desc">Compare Xiaomi MiClaw, Google Gemini Intelligence, Apple Siri AI, and FoneClaw Android phone agents.</div>
        <div class="card-meta"><span>⏱️ 8 min</span><span>Read →</span></div>
      </div>
    </a>'''
        if slug == 'ai-agent' and 'agentic-ai-phone-explained.html' not in cards:
            cards += agentic_card
        if slug == 'news' and 'agentic-ai-phone-explained.html' not in cards:
            cards += agentic_card.replace('data-category="agent"', 'data-category="industry"')
        tps_card = '''<a href="/1000-tps-llms-phone-agent-era.html" class="article-card" data-category="news-trends">
      <div class="card-img" style="background:url('/images/articles/1000-tps-llms-phone-agent-era.jpg') center/cover"></div>
      <div class="card-body">
        <span class="card-tag">AI Agent Trends</span>
        <div class="card-title">1000 TPS LLMs: Why Phone Agents Speed Up</div>
        <div class="card-desc">MiMo UltraSpeed, DFlash, TileRT, and what ultra-fast LLMs mean for phone agents.</div>
        <div class="card-meta"><span>⏱️ 8 min</span><span>Read →</span></div>
      </div>
    </a>'''
        if slug == 'ai-agent' and '1000-tps-llms-phone-agent-era.html' not in cards:
            cards += tps_card
        if slug == 'news' and '1000-tps-llms-phone-agent-era.html' not in cards:
            cards += tps_card.replace('data-category="news-trends"', 'data-category="industry"')
        jd_tencent_card = '''<a href="/jd-tencent-ai-agent-shopping-phone-agent.html" class="article-card" data-category="news-trends">
      <div class="card-img" style="background:url('/images/articles/jd-tencent-ai-agent-shopping-phone-agent.jpg') center/cover"></div>
      <div class="card-body">
        <span class="card-tag">AI Agent Trends</span>
        <div class="card-title">JD Tencent AI Agent: Shopping Agents Begin</div>
        <div class="card-desc">Why shopping agents need phone-level execution, safe approval, and real app control.</div>
        <div class="card-meta"><span>⏱️ 9 min</span><span>Read →</span></div>
      </div>
    </a>'''
        if slug == 'ai-agent' and 'jd-tencent-ai-agent-shopping-phone-agent.html' not in cards:
            cards += jd_tencent_card
        if slug == 'news' and 'jd-tencent-ai-agent-shopping-phone-agent.html' not in cards:
            cards += jd_tencent_card.replace('data-category="news-trends"', 'data-category="industry"')
        wechat_agent_card = '''<a href="/wechat-ai-agent-commandable-super-app.html" class="article-card" data-category="news-trends">
      <div class="card-img" style="background:url('/images/articles/wechat-ai-agent-commandable-super-app.jpg') center/cover"></div>
      <div class="card-body">
        <span class="card-tag">AI Agent Trends</span>
        <div class="card-title">WeChat AI Agent: Commandable Super App</div>
        <div class="card-desc">Where single-app agents end and system-level phone agents begin.</div>
        <div class="card-meta"><span>⏱️ 9 min</span><span>Read →</span></div>
      </div>
    </a>'''
        if slug == 'ai-agent' and 'wechat-ai-agent-commandable-super-app.html' not in cards:
            cards += wechat_agent_card
        if slug == 'news' and 'wechat-ai-agent-commandable-super-app.html' not in cards:
            cards += wechat_agent_card.replace('data-category="news-trends"', 'data-category="industry"')
        claude_code_card = '''<a href="/claude-code-multi-agent-system.html" class="article-card" data-category="news-trends">
      <div class="card-img" style="background:url('/images/articles/claude-code-multi-agent-system.jpg') center/cover"></div>
      <div class="card-body">
        <span class="card-tag">AI Agent Trends</span>
        <div class="card-title">Claude Code Multi-Agent System</div>
        <div class="card-desc">What AI coding agents teach phone agents about delegation, verification, and safe execution.</div>
        <div class="card-meta"><span>⏱️ 9 min</span><span>Read →</span></div>
      </div>
    </a>'''
        if slug == 'ai-agent' and 'claude-code-multi-agent-system.html' not in cards:
            cards += claude_code_card
        if slug == 'news' and 'claude-code-multi-agent-system.html' not in cards:
            cards += claude_code_card.replace('data-category="news-trends"', 'data-category="industry"')
        # Generate tabs HTML
        tabs_html = "\n".join([
            f'<button class="tab-btn{" active" if t["filter"]=="all" else ""}" data-filter="{t["filter"]}">{t["label"]}</button>'
            for t in config['tabs']
        ])
        
        # Featured content HTML
        feat = config.get('featured', {})
        featured_html = f"""
<section class="hub-featured">
  <a href="{feat['link']}" class="featured-card">
    <div class="featured-img" style="background-image:url('{feat['img']}')"></div>
    <div class="featured-content">
      <span class="featured-tag">{feat['tag']}</span>
      <h2>{feat['title']}</h2>
      <p>{feat['desc']}</p>
      <span class="bp" style="margin-top:16px;display:inline-block">Read Guide →</span>
    </div>
  </a>
</section>""" if feat else ''
        
        # Hub CSS - passed as extra_css to full_page()
        hub_css = f"""<style>
.hub-hero{{background:{config['gradient']};padding:80px 20px 60px;text-align:center;position:relative;overflow:hidden}}
.hub-hero::before{{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:url('{config['hero_img']}') center/cover;opacity:0.15}}
.hub-hero>*{{position:relative;z-index:1}}
.hub-hero h1{{font-size:clamp(32px,5vw,48px);font-weight:700;margin-bottom:12px;color:#f0f4f8}}
.hub-hero .subtitle{{color:#8b949e;font-size:18px;max-width:600px;margin:0 auto 24px}}
.hub-stats{{display:flex;justify-content:center;gap:48px;margin:32px 0}}
.hub-stat{{text-align:center}}.hub-stat .num{{font-size:2rem;font-weight:700;color:#00d4ff}}.hub-stat .label{{font-size:0.85rem;color:#8b949e;text-transform:uppercase;letter-spacing:1px}}
.hub-cta{{display:flex;gap:16px;justify-content:center;margin-top:24px}}
.hub-tabs{{display:flex;justify-content:center;gap:8px;padding:24px 20px;flex-wrap:wrap;border-bottom:1px solid #21262d;position:sticky;top:50px;background:#0d1117;z-index:100}}
.tab-btn{{padding:10px 20px;border-radius:20px;border:1px solid #30363d;background:transparent;color:#8b949e;cursor:pointer;font-size:0.9rem;transition:all 0.2s}}.tab-btn:hover{{border-color:#00d4ff;color:#00d4ff}}.tab-btn.active{{background:#00d4ff;border-color:#00d4ff;color:#080c18}}
.hub-featured{{max-width:1000px;margin:48px auto;padding:0 20px}}
.featured-card{{display:grid;grid-template-columns:1fr 1fr;gap:0;background:#161b22;border-radius:12px;overflow:hidden;border:1px solid #21262d;text-decoration:none;transition:all 0.3s}}.featured-card:hover{{border-color:#00d4ff;transform:translateY(-3px)}}
.featured-img{{background-size:cover;background-position:center;min-height:280px}}.featured-content{{padding:32px;display:flex;flex-direction:column;justify-content:center}}.featured-tag{{display:inline-block;background:rgba(0,212,255,0.1);color:#00d4ff;padding:4px 12px;border-radius:8px;font-size:0.75rem;font-weight:600;margin-bottom:12px;width:fit-content}}.featured-content h2{{font-size:1.5rem;margin-bottom:12px;color:#f0f4f8}}.featured-content p{{color:#8b949e;margin-bottom:20px;line-height:1.6}}
.hub-section{{max-width:1000px;margin:48px auto;padding:0 20px}}.hub-section h2{{font-size:1.5rem;margin-bottom:24px;color:#f0f4f8}}
.article-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px}}.article-card{{background:#161b22;border-radius:10px;border:1px solid #21262d;overflow:hidden;transition:all 0.3s;display:block;text-decoration:none}}.article-card:hover{{border-color:#00d4ff;transform:translateY(-3px)}}.card-img{{height:160px;background:#21262d;background-size:cover;background-position:center}}.card-body{{padding:16px}}.card-tag{{display:inline-block;background:rgba(63,185,80,0.1);color:#3fb950;padding:3px 8px;border-radius:6px;font-size:0.7rem;font-weight:600;margin-bottom:8px}}.card-title{{font-size:1rem;font-weight:600;margin-bottom:6px;color:#f0f4f8}}.card-desc{{color:#8b949e;font-size:0.85rem;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}}.card-meta{{display:flex;justify-content:space-between;color:#6e7681;font-size:0.75rem;margin-top:8px}}
.related-hubs{{max-width:1000px;margin:48px auto;padding:0 20px}}.related-hubs h2{{font-size:1.5rem;margin-bottom:24px;color:#f0f4f8}}
.hub-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}.hub-card{{background:#161b22;border-radius:10px;border:1px solid #21262d;padding:24px;text-align:center;transition:all 0.3s;display:block;text-decoration:none}}.hub-card:hover{{border-color:#00d4ff;transform:translateY(-3px)}}.hub-card i{{font-size:2rem;color:#00d4ff;margin-bottom:12px;display:block}}.hub-card h3{{font-size:1rem;margin-bottom:6px;color:#f0f4f8}}.hub-card p{{color:#8b949e;font-size:0.85rem;margin-bottom:12px}}.hub-card .link{{color:#00d4ff;font-weight:600;font-size:0.85rem}}
.cta-section{{background:#161b22;border-top:1px solid #21262d;padding:60px 20px;text-align:center;margin-top:48px}}.cta-section h2{{font-size:1.8rem;margin-bottom:10px;color:#f0f4f8}}.cta-section p{{color:#8b949e;margin-bottom:24px}}
@media(max-width:768px){{.hub-hero h1{{font-size:2rem}}.hub-stats{{flex-direction:column;gap:16px}}.featured-card{{grid-template-columns:1fr}}.article-grid{{grid-template-columns:1fr}}.hub-grid{{grid-template-columns:1fr}}.tab-btn{{padding:8px 14px;font-size:0.8rem}}}}
</style>"""
        
        stats_html = "\n".join([f'<div class="hub-stat"><div class="num">{s["num"]}</div><div class="label">{s["label"]}</div></div>' for s in config['stats']])
        
        # Generate sub-hubs HTML
        sub_hubs = config.get("sub_hubs", [])
        if sub_hubs:
            sub_hubs_items = ""
            for sh in sub_hubs:
                sub_hubs_items += f'<a href="/{slug}/{sh["slug"]}/index.html" class="hub-card"><i class="lucide-folder"></i><h3>{sh["icon"]} {sh["title"]}</h3><p>{sh["desc"]}</p><span class="link">Explore →</span></a>\n'
            sub_hubs_html = f'<section class="related-hubs"><h2>Sub-topics</h2><div class="hub-grid">{sub_hubs_items}</div></section>'
        else:
            sub_hubs_html = ""
        
        hub_body = f"""
<section class="hub-hero">
  <h1>{config['title']}</h1>
  <p class="subtitle">{config['desc'][:100]}</p>
  <div class="hub-stats">{stats_html}</div>
  <div class="hub-cta"><a href="#articles" class="bp">Explore Guides</a><a href="/download.html" class="bo">Get FoneClaw</a></div>
</section>
<nav class="hub-tabs">
{tabs_html}
</nav>
{featured_html}
{sub_hubs_html}
<section class="hub-section" id="articles"><h2>All Guides</h2><div class="article-grid">{cards}</div></section>
<section class="related-hubs"><h2>Explore More Topics</h2><div class="hub-grid">
<a href="/voice-control/index.html" class="hub-card"><i class="lucide-mic"></i><h3>Voice Control</h3><p>35 tutorials</p><span class="link">Explore →</span></a>
<a href="/comparisons/index.html" class="hub-card"><i class="lucide-swords"></i><h3>Comparisons</h3><p>46 analyses</p><span class="link">Explore →</span></a>
<a href="/ai-agent/index.html" class="hub-card"><i class="lucide-bot"></i><h3>AI Agent</h3><p>25 guides</p><span class="link">Explore →</span></a>
<a href="/news/index.html" class="hub-card"><i class="lucide-newspaper"></i><h3>Industry News</h3><p>15 articles</p><span class="link">Explore →</span></a>
</div></section>
<section class="cta-section"><h2>{config['cta_title']}</h2><p>{config['cta_desc']}</p><a href="/download.html" class="bp">Download FoneClaw Free</a></section>
<script>
document.querySelectorAll('.tab-btn').forEach(b=>{{b.addEventListener('click',()=>{{document.querySelectorAll('.tab-btn').forEach(x=>x.classList.remove('active'));b.classList.add('active');const f=b.dataset.filter;document.querySelectorAll('.article-card').forEach(c=>{{c.style.display=(f==='all'||c.dataset.category===f)?'':'none'}})}})}});
</script>"""
        
        # Use full_page() - CSS goes in <head>, body goes in <main>
        page_html = full_page(
            f"{config['title']} - FoneClaw",
            config['desc'],
            config['canonical'],
            3,  # Resources active
            hub_body,
            extra_css=hub_css,
            og_image=f"https://www.foneclaw.ai{config['hero_img']}"
        )
        
        # Write the file
        out_path = os.path.join(upload_dir, slug, 'index.html')
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(page_html)
        
        print(f"  ✅ Generated: {slug}/index.html ({len(page_html)//1024}KB)")

# Run
generate_hub_pages('/home/administrator/clawfone-v2')
print("\nAll hub pages regenerated with individual article images!")
