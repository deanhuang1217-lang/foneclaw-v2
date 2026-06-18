#!/usr/bin/env python3
"""
Translate English article body content to Chinese in zh/*.html files.
Uses Google Translate via deep-translator. Proper nouns are preserved naturally.
"""

import os
import re
import sys
import time
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag
from deep_translator import GoogleTranslator

ZH_DIR = Path("/home/administrator/clawfone-v2/zh")

FILES = [
    "tasker-alternative-voice-automation.html",
    "xiaomi-ai-ecosystem-2026.html",
    "voice-control-visually-impaired.html",
    "gemini-intelligence-supported-devices.html",
    "comp_vs_miclaw.html",
    "wwdc-2026-ai-do-over-phone-agent.html",
    "agentic-ai-phone-explained.html",
    "gemini-vs-foneclaw.html",
    "android-vs-ios-26-5-voice-control.html",
    "voice-control-whatsapp.html",
    "gemini-intelligence-vs-siri.html",
    "foneclaw-vs-apple-intelligence.html",
    "miclaw-vs-foneclaw.html",
    "foneclaw-vs-samsung-galaxy-ai.html",
    "foneclaw-vs-openally.html",
    "foneclaw-vs-minimax.html",
    "foneclaw-vs-all-in-one-ai-agent.html",
    "ai-phone-agent-harness.html",
    "best-voice-control-apps-2026.html",
    "top-10-ai-agent-models-2026.html",
    "voice-assistant-privacy-security.html",
    "ai-agent-vs-traditional-apps.html",
    "top-10-ai-agents-2026.html",
    "hands-free-cooking.html",
    "ai-terminal-war-agent-battlefield.html",
    "huawei-phone-agent.html",
    "miclaw-vs-openclaw.html",
]

translator = GoogleTranslator(source='en', target='zh-CN')
_translation_cache = {}
_call_count = 0


def translate_text(text, max_retries=3):
    """Translate English text to Chinese with caching and rate limiting."""
    global _call_count

    if not text or not text.strip():
        return text

    stripped = text.strip()

    # Skip if already mostly Chinese
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', stripped))
    if len(stripped) > 0 and chinese_chars / len(stripped) > 0.5:
        return text

    # Skip pure numbers/symbols
    if re.match(r'^[\d\s\.\,\%\+\-\(\)\[\]\{\}\/\:\;\!\?\'\"\$\€\£]+$', stripped):
        return text

    # Check cache
    if stripped in _translation_cache:
        return _translation_cache[stripped]

    # Rate limiting
    _call_count += 1
    if _call_count % 5 == 0:
        time.sleep(1.5)

    for attempt in range(max_retries):
        try:
            result = translator.translate(stripped)
            if result:
                _translation_cache[stripped] = result
                return result
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(3 * (attempt + 1))
            else:
                print(f"  WARN: translation failed for '{stripped[:60]}...': {e}")
                return text
    return text


def translate_mixed_content(element):
    """Translate elements with mixed text and inline tags (a, strong, em, etc.)."""
    if not element:
        return

    for child in list(element.children):
        if isinstance(child, NavigableString):
            text = str(child)
            if text.strip():
                translated = translate_text(text)
                child.replace_with(NavigableString(translated))
        elif isinstance(child, Tag):
            if child.name in ['script', 'style', 'svg', 'img', 'br']:
                continue
            # Recurse into child tags to translate their text nodes
            translate_mixed_content(child)


def translate_summary_box(soup):
    box = soup.find('div', class_='summary-box')
    if not box:
        return
    for li in box.find_all('li'):
        text = li.get_text(strip=True)
        if text:
            li.string = translate_text(text)
    print("  ✓ Summary box")


def translate_toc(soup):
    toc = soup.find('div', class_='toc')
    if not toc:
        return
    for a in toc.find_all('a'):
        text = a.get_text(strip=True)
        if text:
            a.string = translate_text(text)
    print("  ✓ Table of contents")


def translate_art_body(soup):
    body = soup.find('div', class_='art-body')
    if not body:
        return

    # Translate h2 headings
    for h2 in body.find_all('h2'):
        text_content = h2.get_text(strip=True)
        if text_content:
            anchor = h2.find('a', class_='anchor')
            if anchor:
                anchor.decompose()
                translated = translate_text(text_content)
                new_anchor = soup.new_tag('a', **{
                    'class': 'anchor',
                    'href': f'#{h2.get("id", "")}',
                    'aria-label': f'Link to {text_content}'
                })
                h2.clear()
                h2.append(new_anchor)
                h2.append(NavigableString(translated))
            else:
                h2.string = translate_text(text_content)

    # Translate h3 headings
    for h3 in body.find_all('h3'):
        text = h3.get_text(strip=True)
        if text:
            h3.string = translate_text(text)

    # Translate paragraphs with mixed content
    for p in body.find_all('p'):
        translate_mixed_content(p)

    # Translate list items
    for li in body.find_all('li'):
        translate_mixed_content(li)

    # Translate table cells
    for td in body.find_all('td'):
        text = td.get_text(strip=True)
        if text:
            td.string = translate_text(text)
    for th in body.find_all('th'):
        text = th.get_text(strip=True)
        if text:
            th.string = translate_text(text)

    # Translate blockquotes
    for bq in body.find_all('blockquote'):
        translate_mixed_content(bq)

    print("  ✓ Article body")


def translate_faq(soup):
    faq_section = soup.find('div', class_='art-faq')
    if not faq_section:
        return

    for item in faq_section.find_all('div', class_='faq-item'):
        q_div = item.find('div', class_='faq-q')
        if q_div:
            text = q_div.get_text(strip=True)
            if text:
                q_div.string = translate_text(text)

        a_inner = item.find('div', class_='faq-a-inner')
        if a_inner:
            translate_mixed_content(a_inner)

    print("  ✓ FAQ")


def translate_related(soup):
    section = soup.find('div', class_='related-section')
    if not section:
        return
    for card in section.find_all('a', class_='related-card'):
        title_div = card.find('div', class_='rc-title')
        if title_div:
            text = title_div.get_text(strip=True)
            if text:
                title_div.string = translate_text(text)
    print("  ✓ Related articles")


def translate_callout(soup):
    for callout in soup.find_all('div', class_='callout'):
        translate_mixed_content(callout)
    if soup.find('div', class_='callout'):
        print("  ✓ Callouts")


def translate_article(filepath):
    filename = filepath.name
    print(f"\n{'='*60}")
    print(f"Translating: {filename}")
    print(f"{'='*60}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    translate_summary_box(soup)
    translate_toc(soup)
    translate_art_body(soup)
    translate_faq(soup)
    translate_related(soup)
    translate_callout(soup)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"  ✓ Saved: {filename}")


def main():
    print("=" * 60)
    print("Chinese Article Translation Script")
    print(f"Translating {len(FILES)} articles")
    print("=" * 60)

    if len(sys.argv) > 1:
        files_to_translate = sys.argv[1:]
    else:
        files_to_translate = FILES

    success = 0
    fail = 0

    for filename in files_to_translate:
        filepath = ZH_DIR / filename
        if not filepath.exists():
            print(f"\n⚠ Not found: {filepath}")
            fail += 1
            continue
        try:
            translate_article(filepath)
            success += 1
        except Exception as e:
            print(f"\n✗ Error: {filename}: {e}")
            fail += 1
        time.sleep(2)

    print(f"\n{'='*60}")
    print(f"Done! Success: {success}, Failed: {fail}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
