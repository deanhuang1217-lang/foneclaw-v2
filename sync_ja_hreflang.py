#!/usr/bin/env python3
"""Post-build i18n hreflang sync for first Japanese rollout.

The legacy English/ZH/TW article generators each write their own hreflang tags.
After adding /ja/ pages, run this script after all article generators and build_multi.py
so the 12 paired EN/ZH/TW pages advertise the Japanese variant too.
"""
from pathlib import Path

BASE = Path('/home/administrator/clawfone-v2')
SLUGS = [
    'tasker-alternative-voice-automation',
    'xiaomi-ai-ecosystem-2026',
    'voice-control-visually-impaired',
    'gemini-intelligence-supported-devices',
    'comp_vs_miclaw',
    'wwdc-2026-ai-do-over-phone-agent',
    'agentic-ai-phone-explained',
    'gemini-vs-foneclaw',
    'android-vs-ios-26-5-voice-control',
    'voice-control-whatsapp',
    'gemini-intelligence-vs-siri',
    'foneclaw-vs-apple-intelligence',
]
# English source URL exceptions for legacy article slugs.
EN_FILES = {
    'comp_vs_miclaw': 'miclaw-vs-foneclaw.html',
    'voice-control-visually-impaired': 'voice-control-visually-impaired.html',
    'gemini-vs-foneclaw': 'gemini-vs-foneclaw.html',
}


def upsert(path: Path, slug: str):
    if not path.exists():
        return False
    html = path.read_text(encoding='utf-8')
    ja_href = f'https://www.foneclaw.ai/ja/{slug}.html'
    ja_tag = f'<link rel="alternate" hreflang="ja" href="{ja_href}">'
    if ja_tag in html:
        return False
    # Place before x-default if present; otherwise before </head>.
    marker = '<link rel="alternate" hreflang="x-default"'
    pos = html.find(marker)
    if pos != -1:
        html = html[:pos] + ja_tag + '\n' + html[pos:]
    else:
        html = html.replace('</head>', ja_tag + '\n</head>', 1)
    path.write_text(html, encoding='utf-8')
    return True


def main():
    changed = []
    for slug in SLUGS:
        candidates = [
            BASE / EN_FILES.get(slug, f'{slug}.html'),
            BASE / 'zh' / f'{slug}.html',
            BASE / 'tw' / f'{slug}.html',
        ]
        for p in candidates:
            if upsert(p, slug):
                changed.append(str(p.relative_to(BASE)))
    print(f'updated {len(changed)} files')
    for rel in changed:
        print(rel)


if __name__ == '__main__':
    main()
