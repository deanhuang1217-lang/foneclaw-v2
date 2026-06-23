#!/usr/bin/env python3
from pathlib import Path
from bs4 import BeautifulSoup
import re, json
ROOT=Path(__file__).resolve().parent
LANGS=['en','zh','tw','ja','ko','es','pt']
DIR={'en':'','zh':'zh','tw':'tw','ja':'ja','ko':'ko','es':'es','pt':'pt'}
SLUGS=[
 'tasker-alternative-voice-automation','xiaomi-ai-ecosystem-2026','voice-control-visually-impaired','gemini-intelligence-supported-devices','comp_vs_miclaw','wwdc-2026-ai-do-over-phone-agent','agentic-ai-phone-explained','gemini-vs-foneclaw','android-vs-ios-26-5-voice-control','voice-control-whatsapp','gemini-intelligence-vs-siri','foneclaw-vs-apple-intelligence']
EN_SLUG_OVERRIDE={'comp_vs_miclaw':'miclaw-vs-foneclaw'}
errors=[]
def local_path(lang, slug):
    real_slug = EN_SLUG_OVERRIDE.get(slug, slug) if lang == 'en' else slug
    return ROOT/(DIR[lang])/(real_slug+'.html') if DIR[lang] else ROOT/(real_slug+'.html')
def expected_url(lang, slug):
    real_slug = EN_SLUG_OVERRIDE.get(slug, slug) if lang == 'en' else slug
    return f'https://www.foneclaw.ai/{DIR[lang]+"/" if DIR[lang] else ""}{real_slug}.html'
for slug in SLUGS:
  for lang in LANGS:
    p=local_path(lang, slug)
    if not p.exists():
      errors.append({'type':'missing_page','lang':lang,'slug':slug,'path':str(p.relative_to(ROOT))}); continue
    soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    sels=soup.select('select.lang-sel')
    if not sels:
      errors.append({'type':'missing_selector','lang':lang,'slug':slug}); continue
    opts={o.get_text(strip=True):o.get('value','') for o in sels[0].select('option')}
    values=list(opts.values())
    for target in LANGS:
      exp=expected_url(target, slug)
      if exp not in values:
        errors.append({'type':'bad_or_missing_option','src_lang':lang,'target_lang':target,'slug':slug,'expected':exp,'values':values})
      if not local_path(target, slug).exists():
        errors.append({'type':'target_missing','src_lang':lang,'target_lang':target,'slug':slug})
    selected=[o.get('value','') for o in sels[0].select('option') if o.has_attr('selected')]
    exp_self=expected_url(lang, slug)
    if selected and selected[0]!=exp_self:
      errors.append({'type':'selected_wrong','src_lang':lang,'slug':slug,'selected':selected[0],'expected':exp_self})
print(f'MATRIX_CHECK pages={len(SLUGS)*len(LANGS)} expected_options={len(SLUGS)*len(LANGS)*len(LANGS)} errors={len(errors)}')
if errors:
  print(json.dumps(errors[:80], ensure_ascii=False, indent=2))
  raise SystemExit(1)
print('PASS')
