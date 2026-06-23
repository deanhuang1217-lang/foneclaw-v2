#!/usr/bin/env python3
"""Validate Korean content optimization articles against all requirements."""
import re, sys
sys.path.insert(0, '.')
from ko_articles import articles

# Banned words
BANNED = ['utilize', 'furthermore', 'robust', 'seamlessly', 'navigate', 'landscape',
          'game-changer', 'absolutely', 'fundamentally', 'additionally', 'delve',
          'tapestry', 'multifaceted', 'nuanced', 'intricate', 'foster', 'realm',
          'leverage', 'cutting-edge', 'unparalleled', 'revolutionary', 'empower',
          'incredibly']

# E-E-A-T signals
EEAT_SIGNALS = ['우리의 테스트에서', '우리의 경험에 따르면', '실제 테스트에서', '우리의 분석에 따르면']

# Chinese character pattern (CJK Unified Ideographs)
CHINESE_RE = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf]')

all_ok = True

for slug, data in articles.items():
    print(f"\n{'='*60}")
    print(f"Validating: {slug}")
    print(f"{'='*60}")
    
    # 1. Title <= 49 chars
    title = data['title']
    tlen = len(title)
    ok = tlen <= 49
    print(f"  Title ({tlen} chars, need <=49): {'OK' if ok else 'FAIL'} - {title}")
    if not ok: all_ok = False
    
    # 2. Meta description 120-160 chars
    desc = data['desc']
    dlen = len(desc)
    ok = 120 <= dlen <= 160
    print(f"  Desc ({dlen} chars, need 120-160): {'OK' if ok else 'FAIL'} - {desc}")
    if not ok: all_ok = False
    
    # 3. 8 sections (7 body + 1 FAQ)
    sections = data['sections']
    n_sections = len(sections)
    ok = n_sections == 8
    print(f"  Sections ({n_sections}, need 8): {'OK' if ok else 'FAIL'}")
    if not ok: all_ok = False
    
    # 4. Last section is FAQ
    last_title = sections[-1][0]
    ok = last_title == '자주 묻는 질문'
    print(f"  FAQ title: {'OK' if ok else 'FAIL'} - '{last_title}'")
    if not ok: all_ok = False
    
    # 5. Body word count (1500-2500, not counting FAQ)
    body_text = '\n\n'.join([s[1] for s in sections[:-1]])
    # Count Korean "words" - split by whitespace and count non-empty tokens
    words = [w for w in body_text.split() if w.strip()]
    wcount = len(words)
    ok = 1500 <= wcount <= 2500
    print(f"  Body words ({wcount}, need 1500-2500): {'OK' if ok else 'FAIL'}")
    if not ok: all_ok = False
    
    # 6. E-E-A-T in first section >= 3 total
    first_body = sections[0][1]
    full_body = body_text
    eeat_in_first = sum(1 for s in EEAT_SIGNALS if s in first_body)
    eeat_total = sum(1 for s in EEAT_SIGNALS if s in full_body)
    ok1 = eeat_in_first >= 1
    ok2 = eeat_total >= 3
    print(f"  E-E-A-T in first section ({eeat_in_first}, need >=1): {'OK' if ok1 else 'FAIL'}")
    print(f"  E-E-A-T total ({eeat_total}, need >=3): {'OK' if ok2 else 'FAIL'}")
    if not ok1 or not ok2: all_ok = False
    
    # 7. Internal links >= 5 unique targets
    links = re.findall(r'href="/ko/([^"]+)\.html"', body_text)
    unique_links = set(links)
    ok = len(unique_links) >= 5
    print(f"  Unique internal links ({len(unique_links)}, need >=5): {'OK' if ok else 'FAIL'} - {unique_links}")
    if not ok: all_ok = False
    
    # 8. No Chinese characters
    chinese_found = CHINESE_RE.findall(body_text + '\n' + sections[-1][1])
    ok = len(chinese_found) == 0
    print(f"  No Chinese chars: {'OK' if ok else 'FAIL'} - found: {chinese_found[:10]}")
    if not ok: all_ok = False
    
    # 9. No banned words
    all_text = (data['title'] + ' ' + data['desc'] + ' ' + body_text + ' ' + sections[-1][1]).lower()
    found_banned = [w for w in BANNED if w.lower() in all_text]
    ok = len(found_banned) == 0
    print(f"  No banned words: {'OK' if ok else 'FAIL'} - found: {found_banned}")
    if not ok: all_ok = False
    
    # 10. FAQ format (Q:/A: pattern)
    faq_text = sections[-1][1]
    qa_pairs = re.findall(r'Q: .+\nA: .+', faq_text)
    ok = len(qa_pairs) >= 5
    print(f"  FAQ Q&A pairs ({len(qa_pairs)}, need 5): {'OK' if ok else 'FAIL'}")
    if not ok: all_ok = False
    
    # 11. No Google Play mention
    gp_found = 'Google Play' in data['title'] + data['desc'] + body_text + faq_text
    ok = not gp_found
    print(f"  No Google Play: {'OK' if ok else 'FAIL'}")
    if not ok: all_ok = False

print(f"\n{'='*60}")
print(f"OVERALL: {'ALL PASSED' if all_ok else 'SOME CHECKS FAILED'}")
print(f"{'='*60}")
