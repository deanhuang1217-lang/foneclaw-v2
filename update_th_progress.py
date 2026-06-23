#!/usr/bin/env python3
from pathlib import Path
import json, datetime
p=Path('/home/administrator/clawfone-v2/multilingual_rollout_progress_20260620.json')
data=json.loads(p.read_text(encoding='utf-8'))
notes=[
 'Codex GPT-5.5 standalone build+QA completed TH localization: 5 core pages + 12 featured articles generated from source-backed Thai translations/generators.',
 'Updated source infrastructure: _th_translations.py, _i18n.py import/LANGUAGES, _components.py NAV_ITEMS_TH/LANG_OPTIONS/page_map/normalized_path/footer/syncLanguageSelectors, _social_share.py Thai labels, _features_page.py Thai stats/categories, _homepage.py Thai article cards/free label/category mapping, build_multi.py Thai core pages + sitemap hreflang order, assets/js/foneclaw-apk-cta.js Thai runtime labels.',
 'Created th_batch_1.py, th_batch_2.py, th_batch_3.py, th_article_rewrites.py, gen_th_articles.py, gen_th_resources.py, gen_th_community.py; rebuild order executed: python3 build_multi.py && python3 gen_th_articles.py && python3 gen_th_resources.py && python3 gen_th_community.py.',
 'Strict local QA PASS: th/index/features/download/resources/community plus 12 articles exist; lang=th; same-language canonical; complete hreflang en/zh/zh-TW/ja/ko/es/pt/ru/fr/de/ar/th/x-default; absolute language selector data-lang=th; sitemap.xml has TH URLs and href="" count 0.',
 'Article QA PASS: all 12 Thai articles have 907-1015 Thai token sequences, 18 H2 sections, 5 FAQ Q/A rendered, 5 unique Thai body internal links, 5 distinct Thai E-E-A-T signals with first-section signal, JSON-LD and OG image present, no Markdown residue, no CJK/Hebrew/Syriac/replacement-character contamination, and no English connector residue outside allowed brand/product names.',
 'Core Thai copy uses conservative product facts: FoneClaw is independent, Android AI assistant, 16 categories, 120+ supported actions, Android 9+, core features currently free; no overclaiming or free-forever language. Visual screenshot localization remains non-blocking debt as in prior rollouts.'
]
data.setdefault('status',{}).setdefault('th',{})['state']='complete'
data['status']['th']['notes']=notes
data['status']['th']['qa_completed_at']=datetime.datetime.now().isoformat(timespec='seconds')
data['status']['th']['qa_model']='openai-codex/gpt-5.5'
p.write_text(json.dumps(data,ensure_ascii=False,indent=4),encoding='utf-8')
print('updated th progress complete')
