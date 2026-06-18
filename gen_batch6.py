#!/usr/bin/env python3
"""Generate 5 new SEO articles using Gemini 3.1 Pro Preview"""
import os, json, sys
sys.path.insert(0, '/home/administrator/.hermes/hermes-agent')

# Load .env for API key
env_path = '/home/administrator/video-workflow/.env'
api_key = None
with open(env_path) as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY='):
            api_key = line.strip().split('=', 1)[1]
            break

if not api_key:
    print("ERROR: GEMINI_API_KEY not found")
    sys.exit(1)

# Read SEO spec
with open('/home/administrator/clawfone-v2/seo_writing_spec.md') as f:
    seo_spec = f.read()

# Article definitions
ARTICLES = [
    {
        "id": "comp_ai_vs_apps",
        "keyword": "AI agent vs traditional apps",
        "secondary": ["AI phone agent", "Android automation", "voice-controlled apps", "app replacement"],
        "title": "AI Agent vs Traditional Apps: The 2026 Phone Revolution",
        "category": "Industry",
        "angle": "How AI agents like FoneClaw are replacing traditional single-purpose apps. Cover: workflow automation, cross-app coordination, memory learning, reduced app switching. Reference real FoneClaw capabilities.",
    },
    {
        "id": "howto_dirty_hands",
        "keyword": "voice control dirty hands",
        "secondary": ["hands-free phone cooking", "voice commands gloves", "touch-free phone use", "dirty hands phone control"],
        "title": "Voice Control with Dirty Hands: The Complete Hands-Free Guide",
        "category": "Lifestyle",
        "angle": "Practical scenarios: cooking (raw chicken, dough), gardening, car repair, painting, gym. Cover specific commands for each scenario. Reference FoneClaw's noise cancellation and far-field mic.",
    },
    {
        "id": "comp_tasker_alt",
        "keyword": "Tasker alternative voice automation",
        "secondary": ["Android automation voice", "Tasker vs voice control", "automate phone voice commands", "Android task automation"],
        "title": "Tasker Alternative: Voice-Driven Android Automation in 2026",
        "category": "Comparison",
        "angle": "Compare Tasker's complex setup vs FoneClaw's voice-first approach. Cover: learning curve, multi-step workflows, no coding required, cross-app automation. Acknowledge Tasker's strengths but show FoneClaw's accessibility.",
    },
    {
        "id": "howto_privacy",
        "keyword": "voice assistant privacy security",
        "secondary": ["voice data protection", "phone AI privacy", "voice assistant data collection", "private voice control"],
        "title": "Voice Assistant Privacy and Security: What You Need to Know in 2026",
        "category": "Guide",
        "angle": "Deep dive into voice assistant privacy concerns: data collection, cloud processing, always-listening fears. Compare approaches (cloud vs local). Highlight FoneClaw's local-first processing as a privacy advantage.",
    },
    {
        "id": "comp_vs_gemini",
        "keyword": "Gemini vs FoneClaw voice control",
        "secondary": ["Gemini Android voice control", "Google Gemini phone assistant", "FoneClaw comparison", "AI voice assistant comparison"],
        "title": "Gemini vs FoneClaw: Which Voice Control Is Better for Android?",
        "category": "Comparison",
        "angle": "Compare Google Gemini's Android integration vs FoneClaw's system-level control. Cover: scope of control, automation depth, privacy, cross-app workflows, offline capability. Fair comparison acknowledging Gemini's strengths.",
    },
]

BATCH_TEMPLATE = '''
# Batch {batch_num}: New SEO Articles (2026-05-12)
BATCH = [
{articles}
]
'''

ARTICLE_TEMPLATE = """    ('{id}', '{title}', '{desc}', '{cat}', '{rt}', [
{sections}
    ]),
"""

def generate_article(art_def):
    """Generate a single article using Gemini API"""
    import requests
    
    prompt = f"""You are an expert SEO content writer for FoneClaw, an AI voice-controlled Android phone agent.

## SEO WRITING SPECIFICATION
{seo_spec}

## ARTICLE TASK
Write ONE article with these EXACT specifications:

**Article ID**: {art_def['id']}
**Title (use EXACTLY this, do NOT modify)**: {art_def['title']}
**Category**: {art_def['category']}
**Primary Keyword**: {art_def['keyword']}
**Secondary Keywords**: {', '.join(art_def['secondary'])}
**Content Angle**: {art_def['angle']}

## 2026 SEO RULES (MANDATORY)
1. First 200 words must directly answer the primary query
2. Include at least ONE unique insight not found in competitor content
3. Use definitive, quotable statements (for GEO/LLM extraction)
4. Reference specific FoneClaw capabilities with numbers (50+ commands, <500ms latency, etc.)
5. FAQ section: 4-5 Q&A pairs in "Q: ... A: ..." format, each 40-60 words

## OUTPUT FORMAT
Output a Python list of tuples. Each tuple is (subtitle, body_text).
- 7-8 sections total: 1 intro + 5-6 body + 1 FAQ
- Each body_text: 250-400 words
- Total article: 1500-2500 words
- Use second person ("you")
- Conversational but authoritative tone
- Include 1-2 Bucket Brigades total (not per section)

## BANNED WORDS (DO NOT USE)
incredibly, seamlessly, absolutely, fundamentally, revolutionary, game-changer, empower, leverage, cutting-edge, unparalleled, delve, utilize, robust, furthermore, moreover, additionally, innovative

## BANNED PHRASES
"Here's the thing:", "But there's a catch", "Let me explain", "Now you might be wondering", "The bottom line?", "Think about it this way", "We have all been there", "Imagine your/this/that", "in this article", "changes this dynamic entirely"

Output ONLY the Python list of tuples, nothing else. Start with [ and end with ].
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gemini-3.1-pro-preview",
        "max_tokens": 65536,
        "temperature": 0.7,
        "messages": [
            {"role": "system", "content": "You are an expert SEO content writer. Output only Python code, no explanations."},
            {"role": "user", "content": prompt}
        ]
    }
    
    print(f"Generating: {art_def['id']}...", flush=True)
    resp = requests.post(url, headers=headers, json=data, timeout=300)
    resp.raise_for_status()
    result = resp.json()
    content = result['choices'][0]['message']['content']
    
    # Extract Python code from response
    if '```python' in content:
        content = content.split('```python')[1].split('```')[0]
    elif '```' in content:
        content = content.split('```')[1].split('```')[0]
    
    return content.strip()

def main():
    all_articles = []
    
    for i, art_def in enumerate(ARTICLES):
        print(f"\n[{i+1}/5] Generating: {art_def['title']}")
        try:
            sections_code = generate_article(art_def)
            
            # Generate description (first 150 chars of angle)
            desc = art_def['angle'][:150]
            if len(art_def['angle']) > 150:
                desc = desc.rsplit(' ', 1)[0] + '...'
            
            # Estimate read time
            word_count = len(sections_code.split()) // 5  # rough estimate
            rt = f"{max(3, word_count // 300 * 5)} min"
            
            article_code = ARTICLE_TEMPLATE.format(
                id=art_def['id'],
                title=art_def['title'],
                desc=desc.replace("'", "\\'"),
                cat=art_def['category'],
                rt=rt,
                sections=sections_code
            )
            all_articles.append(article_code)
            print(f"  ✓ Generated ({len(sections_code)} chars)")
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
            # Generate a placeholder
            all_articles.append(f"    # ERROR generating {art_def['id']}: {e}\n")
    
    # Write batch file
    batch_content = BATCH_TEMPLATE.format(
        batch_num=6,
        articles='\n'.join(all_articles)
    )
    
    output_path = '/home/administrator/clawfone-v2/articles_batch6.py'
    with open(output_path, 'w') as f:
        f.write(batch_content)
    
    print(f"\n✓ Saved to {output_path}")
    print(f"  Total articles: {len(all_articles)}")

if __name__ == '__main__':
    main()
