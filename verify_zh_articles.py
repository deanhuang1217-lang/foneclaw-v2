import re
from zh_article_rewrites import zh_articles

EEAT_PHRASES = ['根据我们的测试', '在我们的经验中', '我们的分析显示']

for slug, sections in zh_articles.items():
    h2_count = len(sections)
    full_text = ''.join(body for _, body in sections)
    eeat_count = sum(1 for phrase in EEAT_PHRASES if phrase in full_text)
    faq_present = any(h2 == '常见问题' for h2, _ in sections)
    link_count = len(re.findall(r'<a href="/zh/[^"]+\.html">', full_text))
    char_count = len(re.sub(r'<[^>]+>', '', full_text))

    print(f"\n=== {slug} ===")
    print(f"  H2 count: {h2_count} {'✓' if h2_count >= 8 else '✗'}")
    print(f"  E-E-A-T count: {eeat_count} {'✓' if eeat_count >= 3 else '✗'}")
    print(f"  FAQ present: {faq_present} {'✓' if faq_present else '✗'}")
    print(f"  Internal links: {link_count} {'✓' if link_count >= 5 else '✗'}")
    print(f"  Chinese chars (approx): {char_count} {'✓' if 1500 <= char_count <= 2000 else 'WARN'}")
    for h2, body in sections:
        bc = len(re.sub(r'<[^>]+>', '', body))
        print(f"    {h2}: {bc} chars {'✓' if 150 <= bc <= 300 else 'WARN'}")
