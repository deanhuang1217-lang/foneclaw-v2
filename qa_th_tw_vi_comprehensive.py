#!/usr/bin/env python3
"""
Comprehensive QA for FoneClaw th/tw/vi sites.
Visual QA + content optimization article QA checks.
"""
import re
import sys
import os
import json
from html.parser import HTMLParser

PAGES = [
    'index', 'features', 'download', 'community', 'resources',
    'tasker-alternative-voice-automation', 'xiaomi-ai-ecosystem-2026',
    'voice-control-visually-impaired', 'gemini-intelligence-supported-devices',
    'comp_vs_miclaw', 'wwdc-2026-ai-do-over-phone-agent',
    'agentic-ai-phone-explained', 'gemini-vs-foneclaw',
    'android-vs-ios-26-5-voice-control', 'voice-control-whatsapp',
    'gemini-intelligence-vs-siri', 'foneclaw-vs-apple-intelligence'
]

ARTICLE_SLUGS = [
    'tasker-alternative-voice-automation', 'xiaomi-ai-ecosystem-2026',
    'voice-control-visually-impaired', 'gemini-intelligence-supported-devices',
    'comp_vs_miclaw', 'wwdc-2026-ai-do-over-phone-agent',
    'agentic-ai-phone-explained', 'gemini-vs-foneclaw',
    'android-vs-ios-26-5-voice-control', 'voice-control-whatsapp',
    'gemini-intelligence-vs-siri', 'foneclaw-vs-apple-intelligence'
]

LANG_CONFIG = {
    'th': {'lang_attr': 'th', 'label': 'Thai'},
    'tw': {'lang_attr': 'zh-TW', 'label': 'Traditional Chinese'},
    'vi': {'lang_attr': 'vi', 'label': 'Vietnamese'},
}

def check_page(lang, slug, base_dir):
    filepath = os.path.join(base_dir, lang, f'{slug}.html')
    if not os.path.exists(filepath):
        return {'slug': slug, 'error': 'FILE NOT FOUND'}
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    issues = []
    details = {}
    config = LANG_CONFIG[lang]
    
    # 1. lang attribute
    lang_match = re.search(r'<html\s+lang="([^"]*)"', html)
    actual_lang = lang_match.group(1) if lang_match else 'MISSING'
    expected_lang = config['lang_attr']
    lang_ok = actual_lang.lower() == expected_lang.lower()
    if not lang_ok:
        issues.append(f"lang attr: expected '{expected_lang}', got '{actual_lang}'")
    details['lang_attr'] = actual_lang
    
    # 2. hreflang links count
    hreflangs = re.findall(r'<link\s+rel="alternate"\s+hreflang="([^"]*)"', html)
    hreflang_count = len(hreflangs)
    hreflang_ok = hreflang_count >= 14  # should have ~15
    if not hreflang_ok:
        issues.append(f"hreflang: {hreflang_count} (expected ~15)")
    details['hreflang_count'] = hreflang_count
    details['hreflangs'] = hreflangs
    
    # 3. Language switcher options
    option_count = len(re.findall(r'<option\s', html))
    details['language_switcher_options'] = option_count
    if option_count < 12:
        issues.append(f"Language switcher: {option_count} options (expected ~14)")
    
    # 4. Canonical URL
    canonical = re.search(r'<link\s+rel="canonical"\s+href="([^"]*)"', html)
    details['canonical'] = canonical.group(1) if canonical else 'MISSING'
    if not canonical:
        issues.append("Canonical: MISSING")
    
    # 5. Meta description
    meta_desc = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html)
    if meta_desc:
        desc = meta_desc.group(1)
        desc_len = len(desc)
        details['meta_desc_length'] = desc_len
        details['meta_desc'] = desc[:100] + '...'
        # Check 80-180 range for visual QA (broader than content optimization script's 120-160)
        if not (80 <= desc_len <= 180):
            issues.append(f"Meta desc length: {desc_len} (target 80-180)")
    else:
        issues.append("Meta description: MISSING")
        details['meta_desc_length'] = 0
    
    # 6. Title
    title = re.search(r'<title>([^<]+)</title>', html)
    if title:
        title_text = title.group(1)
        details['title'] = title_text[:80]
        details['title_length'] = len(title_text)
        if len(title_text) > 70:
            issues.append(f"Title too long: {len(title_text)} chars (target ≤60)")
    else:
        issues.append("Title: MISSING")
    
    # 7. H1 count
    h1_tags = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
    h1_count = len(h1_tags)
    details['h1_count'] = h1_count
    if h1_count != 1:
        issues.append(f"H1 count: {h1_count} (expected 1)")
    
    # 8. Footer hub links check
    footer_match = re.search(r'<footer[^>]*>(.*?)</footer>', html, re.DOTALL | re.IGNORECASE)
    if footer_match:
        footer = footer_match.group(1)
        hub_links_in_footer = re.findall(r'href="[^"]*hub[^"]*"', footer, re.IGNORECASE)
        if hub_links_in_footer:
            issues.append(f"Footer has {len(hub_links_in_footer)} hub links (should be 0)")
            details['footer_hub_links'] = len(hub_links_in_footer)
        else:
            details['footer_hub_links'] = 0
    else:
        details['footer_hub_links'] = 'no footer found'
    
    # 9. APK CTA - check for download button text in local language
    # Look for common CTA patterns
    cta_patterns = {
        'th': ['ดาวน์โหลด', 'โหลด', 'ติดตั้ง'],
        'tw': ['下載', '免費下載', '立即下載'],
        'vi': ['tải về', 'tải xuống', 'tải miễn phí']
    }
    cta_found = False
    for pat in cta_patterns[lang]:
        if pat.lower() in html.lower():
            cta_found = True
            break
    if not cta_found and slug in ['index', 'download', 'features']:
        issues.append(f"APK CTA: No local language CTA found")
    details['apk_cta_found'] = cta_found
    
    # 10. console.log check
    console_logs = re.findall(r'console\.log\(', html)
    details['console_log_count'] = len(console_logs)
    if console_logs:
        issues.append(f"console.log found: {len(console_logs)} occurrences")
    
    # 11. Empty href check
    empty_hrefs = re.findall(r'href=""', html)
    details['empty_href_count'] = len(empty_hrefs)
    if empty_hrefs:
        issues.append(f"Empty href: {len(empty_hrefs)} found")
    
    # 12. Overflow check (basic - look for overflow-x styles)
    details['has_overflow_scroll'] = 'overflow-x: scroll' in html or 'overflow-x: auto' in html
    
    # Article-specific checks
    is_article = slug not in ['index', 'features', 'download', 'community', 'resources']
    if is_article:
        # H2 count
        h2_tags = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL | re.IGNORECASE)
        h2_count = len(h2_tags)
        details['h2_count'] = h2_count
        if h2_count < 5:
            issues.append(f"H2 count: {h2_count} (expected ≥5)")
        
        # FAQ count
        faq_questions = re.findall(r'class="faq-q"', html)
        details['faq_question_count'] = len(faq_questions)
        if len(faq_questions) < 4:
            issues.append(f"FAQ questions: {len(faq_questions)} (expected ≥4)")
        
        # Internal links (article links only)
        all_links = re.findall(r'href="/([^"]*\.html)"', html)
        nav_slugs = ['author', 'index', 'features', 'community', 'download', 'early-access', 'privacy', 'resources']
        article_links = [l for l in all_links if not any(n in l for n in nav_slugs)]
        unique_links = list(set(article_links))
        details['internal_links_count'] = len(unique_links)
        if len(unique_links) < 3:
            issues.append(f"Internal links: {len(unique_links)} (expected ≥3)")
        
        # Related articles count
        related_match = re.findall(r'class="related-item"', html)
        if not related_match:
            related_match = re.findall(r'class="[^"]*related[^"]*card[^"]*"', html)
        details['related_count'] = len(related_match)
        if len(related_match) < 3:
            issues.append(f"Related articles: {len(related_match)} (expected 3)")
    
    # Community-specific
    if slug == 'community':
        cards = re.findall(r'class="[^"]*card[^"]*"', html)
        details['community_cards'] = len(cards)
    
    # Resources-specific
    if slug == 'resources':
        article_cards = re.findall(r'class="[^"]*article-card[^"]*"', html)
        if not article_cards:
            article_cards = re.findall(r'class="[^"]*card[^"]*article[^"]*"', html)
        details['resource_article_cards'] = len(article_cards)
    
    return {
        'slug': slug,
        'issues': issues,
        'issue_count': len(issues),
        'details': details,
        'pass': len(issues) == 0
    }


def run_qa(lang, base_dir):
    results = []
    for slug in PAGES:
        result = check_page(lang, slug, base_dir)
        results.append(result)
    return results


def print_report(lang, results):
    config = LANG_CONFIG[lang]
    print(f"\n{'='*70}")
    print(f"  VISUAL QA REPORT - {config['label'].upper()} ({lang})")
    print(f"{'='*70}")
    
    total_issues = 0
    pages_pass = 0
    pages_fail = 0
    
    for r in results:
        if 'error' in r:
            print(f"\n  ❌ {r['slug']}: {r['error']}")
            pages_fail += 1
            continue
        
        status = "✅" if r['pass'] else "❌"
        if r['pass']:
            pages_pass += 1
        else:
            pages_fail += 1
            total_issues += r['issue_count']
        
        print(f"\n  {status} {r['slug']} ({r['issue_count']} issues)")
        for issue in r['issues']:
            print(f"      - {issue}")
    
    print(f"\n{'='*70}")
    print(f"  SUMMARY: {pages_pass}/{len(results)} pages passed, {total_issues} total issues")
    print(f"{'='*70}")
    
    return {'lang': lang, 'pages_pass': pages_pass, 'pages_fail': pages_fail, 'total_issues': total_issues, 'results': results}


if __name__ == '__main__':
    base_dir = '/home/administrator/clawfone-v2'
    all_reports = {}
    
    for lang in ['th', 'tw', 'vi']:
        results = run_qa(lang, base_dir)
        report = print_report(lang, results)
        all_reports[lang] = report
    
    # Save JSON reports
    output_path = os.path.join(base_dir, 'qa_visual_report_th_tw_vi.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_reports, f, ensure_ascii=False, indent=2)
    print(f"\nJSON report saved to: {output_path}")
