# FoneClaw Multilingual Core + Featured Articles QA Report

Date: 2026-06-20
Scope: 7 languages (EN/ZH/TW/JA/KO/ES/PT), 5 core pages per localized language, 12 selected articles per language.

## Final result

PASS.

- Strict multilingual content optimization/localization QA: FAIL=0, WARN=0
- Article language switcher matrix: 84 article pages checked, 588 expected language options checked, errors=0
- Static visual/responsive QA: issues=0
- Desktop browser DOM QA on zh/index.html: no horizontal overflow; hero images loaded; article card lazy-loading verified after scroll

## Commands run

```bash
python3 build_multi.py
for l in es pt ja ko zh tw; do
  python3 gen_${l}_articles.py
  python3 gen_${l}_resources.py
  python3 gen_${l}_community.py
done
python3 qa_multilingual_strict.py
python3 qa_language_matrix_7lang.py
```

Final command output:

```text
STRICT QA RESULTS: FAIL=0 WARN=0 TOTAL=0
MATRIX_CHECK pages=84 expected_options=588 errors=0
PASS
```

## What was fixed during QA

### Core pages

- Expanded localized meta descriptions to meet 120-160 character content optimization target.
- Fixed ZH/TW resources canonical path from English `/resources.html` to same-language canonical (`/zh/resources.html`, `/tw/resources.html`).
- Added JA/KO hardcoded feature category labels in `_features_page.py` so Features page no longer falls back to English category names.
- Shortened ES/PT homepage titles and descriptions to stay within title/meta limits.
- Rechecked product claims: no “forever free”; wording uses current/core feature availability.

### Featured articles

- Removed Chinese/TW terminology mismatches: replaced “智能体/代理/手機代理” with approved FoneClaw wording such as “助手/手机龙虾/龍蝦/手機龍蝦” depending on context.
- Added `.html` suffix to localized article body links where missing.
- Expanded under-length ZH articles to pass CJK content-length target while keeping product claims conservative.
- Added missing E-E-A-T signals in PT articles and regenerated PT pages.
- Added missing KO internal links in underlinked articles.
- Fixed KO risk wording (`무조건`).

### QA tooling

- Created `qa_multilingual_strict.py` for strict local checks:
  - title/meta length
  - canonical/hreflang completeness
  - JSON-LD syntax
  - localized banned terms
  - banned English content optimization words
  - FAQ rendered count
  - target-language E-E-A-T patterns
  - body length
  - body internal links
  - image/OG presence
- Created `qa_language_matrix_7lang.py` for 7-language article switcher matrix.
- Adjusted matrix QA to respect the known English slug override: localized `comp_vs_miclaw` maps to English `miclaw-vs-foneclaw.html`.

## Remaining non-blocking observation

Hero phone UI screenshots are still English screenshots on localized core pages. This is a visual/localization asset issue, not a generated HTML/content optimization failure. If we want perfect localized visual assets, the phone screenshot/GIF set should be recreated per language. I classify this as P1 visual localization debt, not a blocker for the current HTML/content optimization QA pass unless you require screenshots to be localized before publishing.

## Generated QA artifacts

- `/home/administrator/clawfone-v2/qa_multilingual_strict.py`
- `/home/administrator/clawfone-v2/qa_multilingual_strict_report.json`
- `/home/administrator/clawfone-v2/qa_language_matrix_7lang.py`
- `/home/administrator/clawfone-v2/QA_REPORT_2026-06-20_multilingual.md`
