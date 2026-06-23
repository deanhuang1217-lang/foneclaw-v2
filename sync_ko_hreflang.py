#!/usr/bin/env python3
"""Post-build hreflang sync for Korean rollout.

Legacy EN/ZH/TW/JA article generators may not know about /ko/ pages.
Run this after build_multi.py and locale article generators.
"""
from pathlib import Path
BASE = Path('/home/administrator/clawfone-v2')
SLUGS = [
    'tasker-alternative-voice-automation','xiaomi-ai-ecosystem-2026','voice-control-visually-impaired','gemini-intelligence-supported-devices','comp_vs_miclaw','wwdc-2026-ai-do-over-phone-agent','agentic-ai-phone-explained','gemini-vs-foneclaw','android-vs-ios-26-5-voice-control','voice-control-whatsapp','gemini-intelligence-vs-siri','foneclaw-vs-apple-intelligence',
]
EN_FILES = {'comp_vs_miclaw':'miclaw-vs-foneclaw.html','voice-control-visually-impaired':'voice-control-visually-impaired.html','gemini-vs-foneclaw':'gemini-vs-foneclaw.html'}
def upsert(path: Path, slug: str):
    if not path.exists(): return False
    html = path.read_text(encoding='utf-8')
    ko_tag = f'<link rel="alternate" hreflang="ko" href="https://www.foneclaw.ai/ko/{slug}.html">'
    if ko_tag in html: return False
    marker = '<link rel="alternate" hreflang="x-default"'
    pos = html.find(marker)
    if pos != -1:
        html = html[:pos] + ko_tag + '\n' + html[pos:]
    else:
        html = html.replace('</head>', ko_tag + '\n</head>', 1)
    path.write_text(html, encoding='utf-8')
    return True
def main():
    changed=[]
    for slug in SLUGS:
        for p in [BASE/EN_FILES.get(slug, f'{slug}.html'), BASE/'zh'/f'{slug}.html', BASE/'tw'/f'{slug}.html', BASE/'ja'/f'{slug}.html']:
            if upsert(p, slug): changed.append(str(p.relative_to(BASE)))
    print(f'updated {len(changed)} files')
    for rel in changed: print(rel)
if __name__ == '__main__': main()
