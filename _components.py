# Shared HTML components for all FoneClaw pages
# Used by build_multi.py and standalone page generators

import os

base = '/home/administrator/clawfone-v2'

with open(os.path.join(base, '_style.css')) as f:
    _CSS = f.read()

_CSS += """
#download-btn.available {
    background: linear-gradient(135deg,#3fb950,#2ea043);
    pointer-events: auto;
    opacity: 1;
    box-shadow: 0 4px 16px rgba(63,185,80,.3);
}
#download-btn.unavailable {
    background: #5a1d1d;
    pointer-events: none;
    opacity: 0.6;
}
"""


# Nav items: (index, label, href)
from _social_share import social_share

NAV_ITEMS = [
    (0, 'Home', '/'),
    (1, 'Features', '/features.html'),
    (2, 'Download', '/download.html'),
    (3, 'Resources', '/resources.html'),
    (4, 'Community', '/community.html'),
]

def head(title, description, canonical_path, extra_css='', og_image='https://www.foneclaw.ai/og-image.png', lang='en', hreflang_tags=''):
    favicon = '<link rel="icon" type="image/png" href="/favicon.png">'
    html_lang = 'zh-TW' if lang == 'tw' else lang
    dir_attr = ' dir="rtl"' if lang == 'ar' else ''
    return f'''<!DOCTYPE html>
<html lang="{html_lang}"{dir_attr}><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.foneclaw.ai{canonical_path}">
{hreflang_tags}
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://www.foneclaw.ai{canonical_path}">
<meta property="og:image" content="{og_image}">
<meta property="og:site_name" content="FoneClaw">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">
<meta name="theme-color" content="#080c18">
{favicon}
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/css/foneclaw-apk-cta.css">
<script defer src="/assets/js/foneclaw-apk-cta.js?v=20260622defr"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/_style.css">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0PHX8QGTBF"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-0PHX8QGTBF');</script>
<script>
// GA4 Event Tracking Utilities
function trackEvent(eventName, params){{gtag('event', eventName, params || {{}});}}
function trackShare(platform, articleSlug){{trackEvent('share',{{method:platform,content_type:'article',item_id:articleSlug}});}}
function trackScroll(depth, articleSlug){{trackEvent('scroll_depth',{{percent:depth,article:articleSlug}});}}
function trackOutbound(url, articleSlug){{trackEvent('outbound_click',{{link_url:url,article:articleSlug}});}}
function trackFAQ(question, articleSlug){{trackEvent('faq_expand',{{question:question,article:articleSlug}});}}
</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"FoneClaw","applicationCategory":"UtilitiesApplication","operatingSystem":"Android","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}</script>
{_CSS}
</style>
{extra_css}
</head><body>'''


NAV_ITEMS_ZH = [
    (0, '首页', '/'),
    (1, '功能', '/features.html'),
    (2, '下载', '/download.html'),
    (3, '资源', '/resources.html'),
    (4, '社区', '/community.html'),
]

NAV_ITEMS_TW = [
    (0, '首頁', '/'),
    (1, '功能', '/features.html'),
    (2, '下載', '/download.html'),
    (3, '資源', '/resources.html'),
    (4, '社群', '/community.html'),
]

NAV_ITEMS_JA = [
    (0, 'ホーム', '/'),
    (1, '機能', '/features.html'),
    (2, 'ダウンロード', '/download.html'),
    (3, 'リソース', '/resources.html'),
    (4, 'コミュニティ', '/community.html'),
]

NAV_ITEMS_KO = [
    (0, '홈', '/'),
    (1, '기능', '/features.html'),
    (2, '다운로드', '/download.html'),
    (3, '리소스', '/resources.html'),
    (4, '커뮤니티', '/community.html'),
]

NAV_ITEMS_ES = [
    (0, 'Inicio', '/'),
    (1, 'Funciones', '/features.html'),
    (2, 'Descargar', '/download.html'),
    (3, 'Recursos', '/resources.html'),
    (4, 'Comunidad', '/community.html'),
]

NAV_ITEMS_PT = [
    (0, 'Início', '/'),
    (1, 'Recursos', '/features.html'),
    (2, 'Baixar', '/download.html'),
    (3, 'Guias', '/resources.html'),
    (4, 'Comunidade', '/community.html'),
]

NAV_ITEMS_RU = [
    (0, 'Главная', '/'),
    (1, 'Функции', '/features.html'),
    (2, 'Скачать', '/download.html'),
    (3, 'Ресурсы', '/resources.html'),
    (4, 'Сообщество', '/community.html'),
]

NAV_ITEMS_FR = [
    (0, 'Accueil', '/'),
    (1, 'Fonctionnalités', '/features.html'),
    (2, 'Télécharger', '/download.html'),
    (3, 'Ressources', '/resources.html'),
    (4, 'Communauté', '/community.html'),
]

NAV_ITEMS_DE = [
    (0, 'Startseite', '/'),
    (1, 'Funktionen', '/features.html'),
    (2, 'Download', '/download.html'),
    (3, 'Ressourcen', '/resources.html'),
    (4, 'Community', '/community.html'),
]

NAV_ITEMS_AR = [
    (0, 'الرئيسية', '/'),
    (1, 'الميزات', '/features.html'),
    (2, 'التنزيل', '/download.html'),
    (3, 'الموارد', '/resources.html'),
    (4, 'المجتمع', '/community.html'),
]

NAV_ITEMS_TH = [
    (0, 'หน้าแรก', '/'),
    (1, 'ฟีเจอร์', '/features.html'),
    (2, 'ดาวน์โหลด', '/download.html'),
    (3, 'แหล่งความรู้', '/resources.html'),
    (4, 'ชุมชน', '/community.html'),
]

NAV_ITEMS_VI = [
    (0, 'Trang chủ', '/'),
    (1, 'Tính năng', '/features.html'),
    (2, 'Tải xuống', '/download.html'),
    (3, 'Tài nguyên', '/resources.html'),
    (4, 'Cộng đồng', '/community.html'),
]

NAV_ITEMS_ID = [
    (0, 'Beranda', '/'),
    (1, 'Fitur', '/features.html'),
    (2, 'Unduh', '/download.html'),
    (3, 'Sumber Daya', '/resources.html'),
    (4, 'Komunitas', '/community.html'),
]

LANG_DIR = {'en': '', 'zh': 'zh', 'tw': 'tw', 'ja': 'ja', 'ko': 'ko', 'es': 'es', 'pt': 'pt', 'ru': 'ru', 'fr': 'fr', 'de': 'de', 'ar': 'ar', 'th': 'th', 'vi': 'vi', 'id': 'id'}
LANG_OPTIONS = [('en', 'English'), ('zh', '简体中文'), ('tw', '繁體中文'), ('ja', '日本語'), ('ko', '한국어'), ('es', 'Español'), ('pt', 'Português'), ('ru', 'Русский'), ('fr', 'Français'), ('de', 'Deutsch'), ('ar', 'العربية'), ('th', 'ไทย'), ('vi', 'Tiếng Việt'), ('id', 'Bahasa Indonesia')]

def lang_prefix(lang='en'):
    d = LANG_DIR.get(lang, '')
    return f'/{d}' if d else ''

def nav(active_page=-1, lang='en', canonical_path=''):
    logo = '<img src="/favicon.png" alt="FoneClaw">'
    prefix = lang_prefix(lang)
    links = ''
    items = NAV_ITEMS_PT if lang == 'pt' else (NAV_ITEMS_ES if lang == 'es' else (NAV_ITEMS_KO if lang == 'ko' else (NAV_ITEMS_JA if lang == 'ja' else (NAV_ITEMS_TW if lang == 'tw' else (NAV_ITEMS_ZH if lang == 'zh' else NAV_ITEMS)))))
    if lang == 'ru':
        items = NAV_ITEMS_RU
    elif lang == 'fr':
        items = NAV_ITEMS_FR
    elif lang == 'de':
        items = NAV_ITEMS_DE
    elif lang == 'ar':
        items = NAV_ITEMS_AR
    elif lang == 'th':
        items = NAV_ITEMS_TH
    elif lang == 'vi':
        items = NAV_ITEMS_VI
    elif lang == 'id':
        items = NAV_ITEMS_ID
    for idx, label, href in items:
        cls = ' class="on"' if idx == active_page else ''
        links += f'<a{cls} href="{prefix}{href}">{label}</a>'
    # Language dropdown selector — use full absolute URLs to avoid CDN caching issues
    page_map = {
        'en': {'index': 'https://www.foneclaw.ai/index.html', 'features': 'https://www.foneclaw.ai/features.html', 'download': 'https://www.foneclaw.ai/download.html', 'resources': 'https://www.foneclaw.ai/resources.html', 'community': 'https://www.foneclaw.ai/community.html'},
        'zh': {'index': 'https://www.foneclaw.ai/zh/index.html', 'features': 'https://www.foneclaw.ai/zh/features.html', 'download': 'https://www.foneclaw.ai/zh/download.html', 'resources': 'https://www.foneclaw.ai/zh/resources.html', 'community': 'https://www.foneclaw.ai/zh/community.html'},
        'tw': {'index': 'https://www.foneclaw.ai/tw/index.html', 'features': 'https://www.foneclaw.ai/tw/features.html', 'download': 'https://www.foneclaw.ai/tw/download.html', 'resources': 'https://www.foneclaw.ai/tw/resources.html', 'community': 'https://www.foneclaw.ai/tw/community.html'},
        'ja': {'index': 'https://www.foneclaw.ai/ja/index.html', 'features': 'https://www.foneclaw.ai/ja/features.html', 'download': 'https://www.foneclaw.ai/ja/download.html', 'resources': 'https://www.foneclaw.ai/ja/resources.html', 'community': 'https://www.foneclaw.ai/ja/community.html'},
        'ko': {'index': 'https://www.foneclaw.ai/ko/index.html', 'features': 'https://www.foneclaw.ai/ko/features.html', 'download': 'https://www.foneclaw.ai/ko/download.html', 'resources': 'https://www.foneclaw.ai/ko/resources.html', 'community': 'https://www.foneclaw.ai/ko/community.html'},
        'es': {'index': 'https://www.foneclaw.ai/es/index.html', 'features': 'https://www.foneclaw.ai/es/features.html', 'download': 'https://www.foneclaw.ai/es/download.html', 'resources': 'https://www.foneclaw.ai/es/resources.html', 'community': 'https://www.foneclaw.ai/es/community.html'},
        'pt': {'index': 'https://www.foneclaw.ai/pt/index.html', 'features': 'https://www.foneclaw.ai/pt/features.html', 'download': 'https://www.foneclaw.ai/pt/download.html', 'resources': 'https://www.foneclaw.ai/pt/resources.html', 'community': 'https://www.foneclaw.ai/pt/community.html'},
        'ru': {'index': 'https://www.foneclaw.ai/ru/index.html', 'features': 'https://www.foneclaw.ai/ru/features.html', 'download': 'https://www.foneclaw.ai/ru/download.html', 'resources': 'https://www.foneclaw.ai/ru/resources.html', 'community': 'https://www.foneclaw.ai/ru/community.html'},
        'fr': {'index': 'https://www.foneclaw.ai/fr/index.html', 'features': 'https://www.foneclaw.ai/fr/features.html', 'download': 'https://www.foneclaw.ai/fr/download.html', 'resources': 'https://www.foneclaw.ai/fr/resources.html', 'community': 'https://www.foneclaw.ai/fr/community.html'},
        'de': {'index': 'https://www.foneclaw.ai/de/index.html', 'features': 'https://www.foneclaw.ai/de/features.html', 'download': 'https://www.foneclaw.ai/de/download.html', 'resources': 'https://www.foneclaw.ai/de/resources.html', 'community': 'https://www.foneclaw.ai/de/community.html'},
        'ar': {'index': 'https://www.foneclaw.ai/ar/index.html', 'features': 'https://www.foneclaw.ai/ar/features.html', 'download': 'https://www.foneclaw.ai/ar/download.html', 'resources': 'https://www.foneclaw.ai/ar/resources.html', 'community': 'https://www.foneclaw.ai/ar/community.html'},
        'th': {'index': 'https://www.foneclaw.ai/th/index.html', 'features': 'https://www.foneclaw.ai/th/features.html', 'download': 'https://www.foneclaw.ai/th/download.html', 'resources': 'https://www.foneclaw.ai/th/resources.html', 'community': 'https://www.foneclaw.ai/th/community.html'},
        'vi': {'index': 'https://www.foneclaw.ai/vi/index.html', 'features': 'https://www.foneclaw.ai/vi/features.html', 'download': 'https://www.foneclaw.ai/vi/download.html', 'resources': 'https://www.foneclaw.ai/vi/resources.html', 'community': 'https://www.foneclaw.ai/vi/community.html'},
        'id': {'index': 'https://www.foneclaw.ai/id/index.html', 'features': 'https://www.foneclaw.ai/id/features.html', 'download': 'https://www.foneclaw.ai/id/download.html', 'resources': 'https://www.foneclaw.ai/id/resources.html', 'community': 'https://www.foneclaw.ai/id/community.html'},
    }
    # Determine language-switch target from canonical_path first.
    # Article pages pass active_page=3 to highlight Resources, but their switcher
    # must still point to the corresponding article, not /resources.html.
    import os
    core_by_path = {
        '': 'index', '/': 'index', '/index.html': 'index',
        '/features.html': 'features', '/download.html': 'download',
        '/resources.html': 'resources', '/community.html': 'community',
    }
    normalized_path = canonical_path or ''
    if normalized_path.startswith('/ko/'):
        normalized_path = '/' + normalized_path.split('/ko/', 1)[1]
    elif normalized_path.startswith('/ja/'):
        normalized_path = '/' + normalized_path.split('/ja/', 1)[1]
    elif normalized_path.startswith('/zh/'):
        normalized_path = '/' + normalized_path.split('/zh/', 1)[1]
    elif normalized_path.startswith('/tw/'):
        normalized_path = '/' + normalized_path.split('/tw/', 1)[1]
    elif normalized_path.startswith('/ru/'):
        normalized_path = '/' + normalized_path.split('/ru/', 1)[1]
    elif normalized_path.startswith('/es/'):
        normalized_path = '/' + normalized_path.split('/es/', 1)[1]
    elif normalized_path.startswith('/pt/'):
        normalized_path = '/' + normalized_path.split('/pt/', 1)[1]
    elif normalized_path.startswith('/fr/'):
        normalized_path = '/' + normalized_path.split('/fr/', 1)[1]
    elif normalized_path.startswith('/de/'):
        normalized_path = '/' + normalized_path.split('/de/', 1)[1]
    elif normalized_path.startswith('/ar/'):
        normalized_path = '/' + normalized_path.split('/ar/', 1)[1]
    elif normalized_path.startswith('/th/'):
        normalized_path = '/' + normalized_path.split('/th/', 1)[1]
    elif normalized_path.startswith('/vi/'):
        normalized_path = '/' + normalized_path.split('/vi/', 1)[1]
    elif normalized_path.startswith('/id/'):
        normalized_path = '/' + normalized_path.split('/id/', 1)[1]
    current_page = core_by_path.get(normalized_path)
    lang_options = []
    for code, label in LANG_OPTIONS:
        if current_page and current_page in page_map.get(code, {}):
            url = page_map[code][current_page]
        else:
            # For article pages or unknown pages, construct URL from current path.
            # Some legacy English URLs use a different filename than localized article pages.
            current_filename = os.path.basename(canonical_path) if canonical_path else 'index.html'
            if not current_filename.endswith('.html'):
                current_filename = 'index.html'
            localized_filename = {
                'miclaw-vs-foneclaw.html': 'comp_vs_miclaw.html',
            }.get(current_filename, current_filename)
            english_filename = {
                'comp_vs_miclaw.html': 'miclaw-vs-foneclaw.html',
            }.get(current_filename, current_filename)
            target_filename = english_filename if code == 'en' else localized_filename
            if code != 'en' and code != lang:
                try:
                    candidate = os.path.join(os.path.dirname(__file__), code, target_filename)
                    if not os.path.exists(candidate):
                        continue
                except Exception:
                    pass
            url = f'https://www.foneclaw.ai/{code}/{target_filename}' if code != 'en' else f'https://www.foneclaw.ai/{target_filename}'
        sel = ' selected' if code == lang else ''
        lang_options.append(f'<option value="{url}"{sel}>{label}</option>')
    lang_switcher = f'<select class="lang-sel" data-lang="{lang}" onchange="window.location.href=this.value">{chr(10).join(lang_options)}</select>'
    logo_href = f'{prefix}/'
    return f'<nav class="top-nav" aria-label="Main navigation"><div class="nb"><a class="logo" href="{logo_href}">{logo}FoneClaw</a><button class="hamburger" onclick="this.nextElementSibling.classList.toggle(\'open\')" aria-label="Menu">\u2630</button><div class="nr">{links}{lang_switcher}</div></div></nav>'

def footer(lang='en'):
    logo = '<img src="/favicon.png" alt="FoneClaw">'
    if lang == 'tw':
        slogan = 'FoneClaw 是能幫你實際操作 Android 手機的 AI 助手，不只是語音助理。'
        ft_product = '產品'
        ft_topics = '主題'
        ft_company = '公司'
        ft_features = '功能'
        ft_download = '下載'
        ft_vc = '語音控制'
        ft_comp = '產品比較'
        ft_ai = 'AI Agent'
        ft_news = '產業新聞'
        ft_resources = '全部資源'
        ft_community = '社群'
        ft_privacy = '隱私權政策'
        ft_copy = '保留所有權利。'
    elif lang == 'pt':
        slogan = 'FoneClaw é o assistente de IA para Android que realmente controla seu telefone — não apenas responde perguntas.'
        ft_product = 'Produto'
        ft_topics = 'Temas'
        ft_company = 'Empresa'
        ft_features = 'Recursos'
        ft_download = 'Baixar'
        ft_vc = 'Controle por voz'
        ft_comp = 'Comparativos'
        ft_ai = 'Agente de IA'
        ft_news = 'Notícias do setor'
        ft_resources = 'Todos os guias'
        ft_community = 'Comunidade'
        ft_privacy = 'Privacidade'
        ft_copy = 'Todos os direitos reservados.'
    elif lang == 'es':
        slogan = 'FoneClaw es el asistente de IA para Android que controla tu teléfono de verdad, no solo responde preguntas.'
        ft_product = 'Producto'
        ft_topics = 'Temas'
        ft_company = 'Compañía'
        ft_features = 'Funciones'
        ft_download = 'Descargar'
        ft_vc = 'Control por voz'
        ft_comp = 'Comparativas'
        ft_ai = 'Agente de IA'
        ft_news = 'Noticias del sector'
        ft_resources = 'Todos los recursos'
        ft_community = 'Comunidad'
        ft_privacy = 'Privacidad'
        ft_copy = 'Todos los derechos reservados.'
    elif lang == 'ko':
        slogan = 'FoneClaw는 질문에 답하는 데서 끝나지 않고 Android 스마트폰을 실제로 조작하는 AI 어시스턴트입니다.'
        ft_product = '제품'
        ft_topics = '주제'
        ft_company = '회사'
        ft_features = '기능'
        ft_download = '다운로드'
        ft_vc = '음성 조작'
        ft_comp = '비교'
        ft_ai = 'AI 에이전트'
        ft_news = '업계 뉴스'
        ft_resources = '모든 리소스'
        ft_community = '커뮤니티'
        ft_privacy = '개인정보 처리방침'
        ft_copy = '모든 권리 보유.'
    elif lang == 'ja':
        slogan = 'FoneClaw は、質問に答えるだけでなく、Android スマートフォンを実際に操作する AI アシスタントです。'
        ft_product = '製品'
        ft_topics = 'トピック'
        ft_company = '会社'
        ft_features = '機能'
        ft_download = 'ダウンロード'
        ft_vc = '音声操作'
        ft_comp = '比較'
        ft_ai = 'AIエージェント'
        ft_news = '業界ニュース'
        ft_resources = 'すべてのリソース'
        ft_community = 'コミュニティ'
        ft_privacy = 'プライバシーポリシー'
        ft_copy = '無断転載を禁じます。'
    elif lang == 'zh':
        slogan = 'FoneClaw 是能帮你实际操作 Android 手机的 AI 助手，不仅仅是语音助手。'
        ft_product = '产品'
        ft_topics = '主题'
        ft_company = '公司'
        ft_features = '功能'
        ft_download = '下载'
        ft_vc = '语音控制'
        ft_comp = '产品对比'
        ft_ai = 'AI Agent'
        ft_news = '行业资讯'
        ft_resources = '全部资源'
        ft_community = '社区'
        ft_privacy = '隐私政策'
        ft_copy = '保留所有权利。'
    elif lang == 'ru':
        slogan = 'FoneClaw — это AI-агент для Android, который реально управляет вашим телефоном, а не просто отвечает на вопросы.'
        ft_product = 'Продукт'
        ft_topics = 'Темы'
        ft_company = 'Компания'
        ft_features = 'Функции'
        ft_download = 'Скачать'
        ft_vc = 'Голосовое управление'
        ft_comp = 'Сравнения'
        ft_ai = 'AI-агент'
        ft_news = 'Новости индустрии'
        ft_resources = 'Все ресурсы'
        ft_community = 'Сообщество'
        ft_privacy = 'Политика конфиденциальности'
        ft_copy = 'Все права защищены.'
    elif lang == 'fr':
        slogan = 'FoneClaw est l\'agent IA pour Android qui contrôle réellement votre téléphone — pas juste un assistant qui répond à des questions.'
        ft_product = 'Produit'
        ft_topics = 'Sujets'
        ft_company = 'Entreprise'
        ft_features = 'Fonctionnalités'
        ft_download = 'Télécharger'
        ft_vc = 'Commande vocale'
        ft_comp = 'Comparaisons'
        ft_ai = 'Agent IA'
        ft_news = 'Actualités'
        ft_resources = 'Toutes les ressources'
        ft_community = 'Communauté'
        ft_privacy = 'Politique de confidentialité'
        ft_copy = 'Tous droits réservés.'
    elif lang == 'de':
        slogan = 'FoneClaw ist der KI-Agent für Android, der Ihr Telefon wirklich steuert — nicht nur Fragen beantwortet.'
        ft_product = 'Produkt'
        ft_topics = 'Themen'
        ft_company = 'Unternehmen'
        ft_features = 'Funktionen'
        ft_download = 'Download'
        ft_vc = 'Sprachsteuerung'
        ft_comp = 'Vergleiche'
        ft_ai = 'KI-Agent'
        ft_news = 'Branchennews'
        ft_resources = 'Alle Ressourcen'
        ft_community = 'Community'
        ft_privacy = 'Datenschutz'
        ft_copy = 'Alle Rechte vorbehalten.'
    elif lang == 'vi':
        slogan = 'FoneClaw là trợ lý AI cho Android có thể thực sự điều khiển điện thoại, không chỉ trả lời câu hỏi.'
        ft_product = 'Sản phẩm'
        ft_topics = 'Chủ đề'
        ft_company = 'Công ty'
        ft_features = 'Tính năng'
        ft_download = 'Tải xuống'
        ft_vc = 'Điều khiển giọng nói'
        ft_comp = 'So sánh'
        ft_ai = 'AI trên điện thoại'
        ft_news = 'Tin tức'
        ft_resources = 'Tất cả tài nguyên'
        ft_community = 'Cộng đồng'
        ft_privacy = 'Chính sách riêng tư'
        ft_copy = 'Đã đăng ký bản quyền.'
    elif lang == 'th':
        slogan = 'FoneClaw คือผู้ช่วย AI สำหรับ Android ที่ลงมือควบคุมมือถือจริง ไม่ใช่แค่ตอบคำถาม'
        ft_product = 'ผลิตภัณฑ์'
        ft_topics = 'หัวข้อ'
        ft_company = 'บริษัท'
        ft_features = 'ฟีเจอร์'
        ft_download = 'ดาวน์โหลด'
        ft_vc = 'การสั่งงานด้วยเสียง'
        ft_comp = 'เปรียบเทียบ'
        ft_ai = 'AI บนมือถือ'
        ft_news = 'ข่าวสาร'
        ft_resources = 'แหล่งความรู้ทั้งหมด'
        ft_community = 'ชุมชน'
        ft_privacy = 'นโยบายความเป็นส่วนตัว'
        ft_copy = 'สงวนลิขสิทธิ์'
    elif lang == 'ar':
        slogan = 'FoneClaw هو وكيل الذكاء الاصطناعي لأندرويد الذي يتحكم فعليًا في هاتفك — وليس مجرد مساعد يجيب على الأسئلة.'
        ft_product = 'المنتج'
        ft_topics = 'المواضيع'
        ft_company = 'الشركة'
        ft_features = 'الميزات'
        ft_download = 'التنزيل'
        ft_vc = 'التحكم الصوتي'
        ft_comp = 'المقارنات'
        ft_ai = 'وكيل الذكاء الاصطناعي'
        ft_news = 'أخبار الصناعة'
        ft_resources = 'جميع الموارد'
        ft_community = 'المجتمع'
        ft_privacy = 'سياسة الخصوصية'
        ft_copy = 'جميع الحقوق محفوظة.'
    elif lang == 'id':
        slogan = 'FoneClaw adalah agen AI untuk Android yang benar-benar mengendalikan ponsel Anda — bukan sekadar menjawab pertanyaan.'
        ft_product = 'Produk'
        ft_topics = 'Topik'
        ft_company = 'Perusahaan'
        ft_features = 'Fitur'
        ft_download = 'Unduh'
        ft_vc = 'Kontrol Suara'
        ft_comp = 'Perbandingan'
        ft_ai = 'Agen AI'
        ft_news = 'Berita Industri'
        ft_resources = 'Semua Sumber Daya'
        ft_community = 'Komunitas'
        ft_privacy = 'Kebijakan Privasi'
        ft_copy = 'Hak cipta dilindungi.'
    else:
        slogan = 'FoneClaw is the Android AI agent that actually controls your phone — not just answers questions.'
        ft_product = 'Product'
        ft_topics = 'Topics'
        ft_company = 'Company'
        ft_features = 'Features'
        ft_download = 'Download'
        ft_vc = 'Voice Control'
        ft_comp = 'Comparisons'
        ft_ai = 'AI Agent'
        ft_news = 'Industry News'
        ft_resources = 'All Resources'
        ft_community = 'Community'
        ft_privacy = 'Privacy Policy'
        ft_copy = 'All rights reserved.'
    prefix = lang_prefix(lang)
    if lang in ('zh', 'tw', 'ja', 'ko', 'es', 'pt', 'ru', 'fr', 'de', 'ar', 'id', 'th', 'vi'):
        topics_links = f'<a href="{prefix}/resources.html">{ft_resources}</a>'
    else:
        topics_links = f'<a href="/voice-control/index.html">{ft_vc}</a><a href="/comparisons/index.html">{ft_comp}</a><a href="/ai-agent/index.html">{ft_ai}</a><a href="/news/index.html">{ft_news}</a><a href="{prefix}/resources.html">{ft_resources}</a>'
    return f'''<footer aria-label="Footer"><div class="wrap"><div class="ft-inner">
<div class="ft-col"><div class="logo" style="margin-bottom:12px">{logo}FoneClaw</div><p style="color:#8b949e;font-size:14px">{slogan}</p></div>
<div class="ft-col"><div class="ft-heading">{ft_product}</div><a href="{prefix}/features.html">{ft_features}</a><a href="{prefix}/download.html">{ft_download}</a></div>
<div class="ft-col"><div class="ft-heading">{ft_topics}</div>{topics_links}</div>
<div class="ft-col"><div class="ft-heading">{ft_company}</div><a href="{prefix}/community.html">{ft_community}</a><a href="/privacy.html">{ft_privacy}</a></div>
</div><p style="text-align:center;margin-top:30px;color:#484f58;font-size:12px">&copy; 2026 FoneClaw. {ft_copy}</p></div></footer>
<button class="back-to-top" id="backToTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>
</button>'''

def js(trans_json='{}'):
    return f"""<script>
function showArticle(id){{var el=document.getElementById("art-"+id);if(el){{el.classList.add("show");document.body.style.overflow="hidden";window.scrollTo(0,0);}}}}
function hideArticle(){{document.querySelectorAll(".article-overlay").forEach(function(e){{e.classList.remove("show");}});document.body.style.overflow="";}}
document.addEventListener("keydown",function(e){{if(e.key==="Escape")hideArticle();}});
window.addEventListener("scroll",function(){{var b=document.getElementById("backToTop");if(b){{if(window.scrollY>400){{b.style.opacity="1";b.style.visibility="visible";}}else{{b.style.opacity="0";b.style.visibility="hidden";}}}}}});
function syncLanguageSelectors(){{
  document.querySelectorAll(".lang-sel").forEach(function(sel){{
    var expected=sel.getAttribute("data-lang") || document.documentElement.lang || "en";
    var opts=Array.prototype.slice.call(sel.options);
    var match=opts.find(function(o){{return o.selected && o.value.indexOf("/"+expected+"/")>-1;}});
    if(expected==="en"){{match=opts.find(function(o){{return o.value.indexOf("/zh/")===-1&&o.value.indexOf("/tw/")===-1&&o.value.indexOf("/ja/")===-1&&o.value.indexOf("/ko/")===-1&&o.value.indexOf("/es/")===-1&&o.value.indexOf("/pt/")===-1&&o.value.indexOf("/ru/")===-1&&o.value.indexOf("/fr/")===-1&&o.value.indexOf("/de/")===-1&&o.value.indexOf("/ar/")===-1&&o.value.indexOf("/th/")===-1&&o.value.indexOf("/vi/")===-1&&o.value.indexOf("/id/")===-1;}});}}
    else {{match=opts.find(function(o){{return o.value.indexOf("/"+expected+"/")>-1;}});}}
    if(match) sel.value=match.value;
  }});
}}
document.addEventListener("DOMContentLoaded",syncLanguageSelectors);
window.addEventListener("pageshow",syncLanguageSelectors);
</script>
"""


def full_page(title, description, canonical_path, active_page, body_html, extra_css='', og_image='https://www.foneclaw.ai/og-image.png', lang='en', hreflang_tags=''):
    """Generate a complete page with head, nav, content, footer, back-to-top, js."""
    html = []
    html.append(head(title, description, canonical_path, extra_css, og_image, lang, hreflang_tags))
    html.append(nav(active_page, lang, canonical_path))
    html.append('<main>')
    html.append(body_html)
    html.append('</main>')
    html.append(footer(lang))
    html.append(social_share(lang=lang))
    html.append(js())
    html.append('</body></html>')
    return '\n'.join(html)
