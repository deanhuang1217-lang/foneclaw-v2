# content optimization Article Rewrite Task — Auto-Execution Instructions

## Overview
This file contains the complete workflow for rewriting 12 FoneClaw articles in any language following the content optimization article writing skill. A cronjob agent reads this file and executes the task autonomously.

## Workflow per Language

### Step 1: Create content optimization Plan
For the target language (ja/ko/zh/tw), create a JSON plan with these fields per article:
- slug, query (in target language), intent, title (≤49 chars), meta (120-160 chars)
- h2: 7-8 unique H2 headings (target language search intent)
- faq: 4-5 questions (target language)
- links: 5 internal link targets from the 12 slugs

### Step 2: Write Articles via delegate_task
Split 12 articles into 3 batches of 4. Each batch is a delegate_task with:
- Complete writing rules in the goal
- Target language specification
- The 4 slugs with their H2 plans
- All quality constraints

### Step 3: Validate Output
For each article, verify:
- Word count: 1000-2500 (body words)
- H2 count: 7-8
- E-E-A-T in first section (language-specific pattern)
- E-E-A-T total ≥ 3
- Title ≤ 49 chars
- Meta 120-160 chars
- Internal links ≥ 5 unique targets
- FAQ Q:/A: format, ≥ 4 questions
- No banned English words (word-boundary regex)
- No Chinese characters (for non-ZH/TW)
- JSON-LD valid

### Step 4: Write Source File
Write to `{lang}_article_rewrites.py` with proper Python dict format.

### Step 5: Rebuild
```bash
cd /home/administrator/clawfone-v2
python3 gen_{lang}_articles.py
python3 gen_{lang}_resources.py
python3 build_multi.py
```

### Step 6: Run content optimization QA Script
```bash
python3 /home/administrator/.hermes/skills/content optimization-content-writing/foneclaw-article-writing/scripts/seo_quality_check.py "{lang}/slug" "" ""
```
All 12 articles must pass (only "内链重复" is acceptable as known limitation).

### Step 7: Update Progress
Update `seo_rewrite_progress.json` with completion status.

## E-E-A-T Patterns by Language
- ja: '私たちのテストでは', 'our testing', 'our experience', '実際のテスト', '私たちの検証では'
- ko: '우리의 테스트에서', '우리의 경험에 따르면', 'our testing', '실제 테스트에서'
- zh: '根据我们的', '在我们的测试中', '我们的经验', '我们的分析', '我们测试了'
- tw: '根據我們的', '在我們的測試中', '我們的經驗', '我們的分析'

## FAQ Titles by Language
- ja: 'よくある質問'
- ko: '자주 묻는 질문'
- zh: '常见问题'
- tw: '常見問題'

## Writing Rules (MUST follow)
1. First section = Quick Answer + E-E-A-T signal in first sentence
2. 7 body H2 + 1 FAQ = 8 total sections
3. Each section body: 200-350 words, paragraphs separated by \n\n
4. FAQ: Q:/A: format, 5 questions per article
5. Internal links: ≥ 5 unique targets via <a href="/{lang}/{slug}.html">anchor</a>
6. Write in natural target language, NOT translation from English
7. FoneClaw facts: 16 categorías, 120+ actions, Android 9+, clear permissions, confirmation for sensitive actions, core features free
8. Do NOT mention: Google Play Store, install instructions
9. Banned words (word-boundary): utilize, furthermore, robust, seamlessly, navigate, landscape, game-changer, absolutely, fundamentally, additionally, delve, tapestry, multifaceted, nuanced, intricate, foster, realm, leverage, cutting-edge, unparalleled, revolutionary, empower, incredibly
10. No Chinese characters in JA/KO/ES/PT articles

## Article Data Format
```python
{lang.upper()}_ARTICLES = {
    'slug': {
        'title': 'Title ≤49 chars',
        'desc': 'Meta description 120-160 chars.',
        'cat': 'Category',
        'read_time': '9 min',
        'image': 'slug',
        'sections': [
            ('H2 Title', 'Body text with E-E-A-T...'),
            ...
            ('Perguntas frecuentes', 'Q: Question?\nA: Answer.\n\nQ: Question?\nA: Answer.'),
        ]
    },
    ...
}
```

## Error Handling
- If delegate_task returns articles with validation errors, retry once with corrections
- If rebuild fails, check syntax errors and fix source file
- If content optimization QA fails on a specific item, fix that item in source and rebuild
- Log all errors to seo_rewrite_progress.json
