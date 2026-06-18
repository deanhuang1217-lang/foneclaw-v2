#!/usr/bin/env python3
"""Generate 5 new FoneClaw articles via Gemini 3.5 Flash API."""

import requests
import json
import re
import time
import os

# Load API key
api_key = open('/home/administrator/video-workflow/.env').read().split('GEMINI_API_KEY=')[1].split('\n')[0].strip()
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={api_key}"

# System prompt (from template)
SYSTEM_PROMPT = """Write an SEO article for foneclaw.ai.

CRITICAL RULES:
1. FoneClaw is INDEPENDENT startup, NOT owned by Xiaomi
2. MiMo is Xiaomi's model - FoneClaw supports but does NOT own it
3. First mention of MiMo must include "Xiaomi" (e.g., "Xiaomi MiMo-V2.5-Pro")
4. Subsequent mentions can just say "MiMo"

E-E-A-T PLACEMENT (REQUIRED):
- First section must start with "Based on our testing/experience/data"
- At least 3 "Based on our testing/experience/data" references throughout
- At least 1 data reference (number + source)
- At least 1 test reference ("Based on our testing")

FAQ FORMAT (MUST follow):
Title MUST be "Frequently Asked Questions"
Q: Question here?
A: Answer here (40-60 words, specific and informative).
- At least 1 question must contain the main keyword
- Questions should be real search queries
- DO NOT use **bold** or numbered lists for FAQ

STYLE:
- Conversational tone, use "you" frequently
- Short sentences mixed with longer ones
- Second person ("you")
- Vary sentence openings
- Limit "FoneClaw" mentions: max 1 per paragraph, use "the app/agent/tool" alternately

PARAGRAPH STRUCTURE (CRITICAL - MUST follow):
- Each section MUST have 3-4 paragraphs (NOT 1 big block)
- Each paragraph: 3-5 sentences (60-100 words)
- Separate paragraphs with \\n\\n (double backslash-n) in Python string
- Structure per section (250-400 words total):
  * Paragraph 1: Hook/Problem (70-80 words)
  * Paragraph 2: Solution/Details (70-80 words)
  * Paragraph 3: Examples/Data (70-80 words)
  * Paragraph 4: Summary/Transition (15-20 words, optional)

BANNED WORDS (NEVER use):
utilize, furthermore, robust, seamlessly, incredibly, empower, leverage, cutting-edge, unparalleled, revolutionary, game-changer, navigate, landscape, intricate, foster, delve, tapestry, harness, paramount, pivotal, enshroud, multifaceted, myriad, in conclusion

BANNED SENTENCES:
"Here's the thing:", "But there's a catch", "Let me explain"
"Now you might be wondering", "The bottom line?", "Think about it this way"
"In conclusion", "To summarize"

INTERNAL LINK KEYWORDS (embed naturally in text, do NOT add <a> tags - the system auto-links them):
- Same keyword only link once (first occurrence)
- Same target article only link once
- Anchor text: 2-4 words, contains keyword
- Distribute evenly (don't concentrate in one paragraph)

OUTPUT FORMAT (Python BATCH code only, no explanation, no markdown):
BATCH = [
    (
        "slug-here",
        "Title Here",
        "Meta description 120-160 characters.",
        "Category",
        "X min",
        [
            ("Section Title 1", "Paragraph 1 hook and problem. 3-4 sentences here. Engage the reader. Set up the context.\\n\\nParagraph 2 solution and details. 3-4 sentences here. Explain the concept. Provide specifics.\\n\\nParagraph 3 examples and data. 3-4 sentences here. Real-world cases. Based on our testing.\\n\\nParagraph 4 short summary. Transition sentence."),
            ("Section Title 2", "Paragraph 1...\\n\\nParagraph 2...\\n\\nParagraph 3..."),
            # ... 6-7 sections, each with 3-4 paragraphs separated by \\n\\n
            ("Frequently Asked Questions", "Q: Question?\\nA: Answer 40-60 words.\\n\\nQ: Question?\\nA: Answer 40-60 words."),
        ]
    ),
]

IMPORTANT: Separate paragraphs with \\n\\n (double newline), NOT \\n (single newline)
- \\n\\n = paragraph break (correct)
- \\n = line break within paragraph (wrong for section body)

7-8 sections per article (6 content + 1 intro + 1 FAQ)
Total article length: 1500-3000 words
Each section 250-400 words
FAQ: 4-5 Q&A pairs, each 40-60 words
"""

# Article definitions with related articles context
ARTICLES = [
    {
        "slug": "gemini-intelligence-form-filling",
        "title": "Gemini Intelligence Form Filling: Auto-Complete Forms",
        "meta": "Learn how Gemini Intelligence auto-fills forms on Android. Save time with smart suggestions, OCR scanning, and one-tap form completion.",
        "category": "Industry & Trends",
        "reading_time": "7 min",
        "internal_links": """
INTERNAL LINK KEYWORDS (embed naturally in text, do NOT add <a> tags):
- "Gemini Intelligence" -> /gemini-intelligence-complete-guide.html
- "Google AI" -> /gemini-intelligence-complete-guide.html
- "AI agent" -> /agentic-ai-phone-explained.html
- "Android AI" -> /gemini-intelligence-complete-guide.html
- "Gemini Intelligence features" -> /gemini-intelligence-features.html
- "task automation" -> /automate-multi-step-tasks.html
- "AI widgets" -> /gemini-intelligence-features.html
- "voice control" -> /voice-control-android.html
- "AI productivity" -> /gemini-intelligence-productivity.html
- "voice-to-text" -> /gemini-intelligence-voice-control.html
""",
        "sections": [
            "How Gemini Intelligence Transforms Form Filling on Android",
            "Smart Auto-Fill Technology: How It Works",
            "OCR Document Scanning for Instant Data Entry",
            "Cross-App Form Recognition and Memory",
            "Privacy and Security in Auto-Fill Features",
            "How FoneClaw Complements Auto-Fill Workflows",
            "Frequently Asked Questions"
        ]
    },
    {
        "slug": "gemini-intelligence-widgets",
        "title": "Gemini Intelligence Widgets: Custom Home Screen",
        "meta": "Customize your Android home screen with Gemini Intelligence widgets. Smart suggestions, task shortcuts, and AI-powered info displays.",
        "category": "Industry & Trends",
        "reading_time": "7 min",
        "internal_links": """
INTERNAL LINK KEYWORDS (embed naturally in text, do NOT add <a> tags):
- "Gemini Intelligence features" -> /gemini-intelligence-features.html
- "task automation" -> /automate-multi-step-tasks.html
- "AI widgets" -> /gemini-intelligence-features.html
- "Gemini Intelligence" -> /gemini-intelligence-complete-guide.html
- "Google AI" -> /gemini-intelligence-complete-guide.html
- "AI agent" -> /agentic-ai-phone-explained.html
- "voice control" -> /voice-control-android.html
- "AI productivity" -> /gemini-intelligence-productivity.html
- "voice-to-text" -> /gemini-intelligence-voice-control.html
- "Android AI" -> /gemini-intelligence-complete-guide.html
""",
        "sections": [
            "What Gemini Intelligence Widgets Offer Your Home Screen",
            "Contextual Widget Suggestions Based on Your Routine",
            "Custom Widget Layouts for Different Scenarios",
            "Smart Information Cards and Quick Actions",
            "Widget Integration with Third-Party Apps",
            "How FoneClaw Works Alongside Gemini Widgets",
            "Frequently Asked Questions"
        ]
    },
    {
        "slug": "gemini-intelligence-supported-devices",
        "title": "Gemini Intelligence Supported Devices List",
        "meta": "Full list of phones and tablets supporting Gemini Intelligence features. Check if your Android device qualifies for Google's AI agent.",
        "category": "Industry & Trends",
        "reading_time": "8 min",
        "internal_links": """
INTERNAL LINK KEYWORDS (embed naturally in text, do NOT add <a> tags):
- "Gemini Intelligence" -> /gemini-intelligence-complete-guide.html
- "Google AI" -> /gemini-intelligence-complete-guide.html
- "AI agent" -> /agentic-ai-phone-explained.html
- "Android AI" -> /gemini-intelligence-complete-guide.html
- "Gemini Intelligence features" -> /gemini-intelligence-features.html
- "task automation" -> /automate-multi-step-tasks.html
- "voice control" -> /voice-control-android.html
- "AI assistant comparison" -> /gemini-intelligence-vs-siri.html
- "AI productivity" -> /gemini-intelligence-productivity.html
- "phone automation" -> /agentic-ai-phone-explained.html
""",
        "sections": [
            "Which Devices Support Gemini Intelligence Features",
            "Minimum Hardware Requirements Explained",
            "Google Pixel Devices: Full Gemini Intelligence Support",
            "Samsung Galaxy: Gemini Intelligence Compatibility",
            "Other Android OEMs and Gemini Intelligence Rollout",
            "How FoneClaw Works on Devices Without Gemini Support",
            "Frequently Asked Questions"
        ]
    },
    {
        "slug": "tencent-phone-agent-cost",
        "title": "Tencent Phone Agent: Cost and Token Economics",
        "meta": "How much does Tencent's phone AI agent cost? Token pricing, API fees, and real-world usage economics explained for developers.",
        "category": "Industry & Trends",
        "reading_time": "8 min",
        "internal_links": """
INTERNAL LINK KEYWORDS (embed naturally in text, do NOT add <a> tags):
- "AI phone" -> /ai-phone-war-2026.html
- "agentic ai" -> /agentic-ai-phone-explained.html
- "AI agent" -> /ai-agent-phone-control.html
- "phone automation" -> /agentic-ai-phone-explained.html
- "voice automation" -> /voice-control-android.html
- "Android agent" -> /ai-agent-phone-control.html
- "Agentic Index" -> /top-10-ai-agent-models-2026.html
- "agent benchmark" -> /top-10-ai-agent-models-2026.html
- "AI agent model" -> /top-10-ai-agent-models-2026.html
- "autonomous agent" -> /agentic-ai-phone-explained.html
""",
        "sections": [
            "Understanding Tencent Phone Agent Pricing Structure",
            "Token Economics: How AI Agent Calls Are Priced",
            "Comparing Tencent Agent Costs to Google and Xiaomi",
            "Developer API Pricing and Tiers",
            "Real-World Usage Cost Scenarios",
            "How FoneClaw Offers a Cost-Effective Alternative",
            "Frequently Asked Questions"
        ]
    },
    {
        "slug": "xiaomi-phone-agent-summit",
        "title": "Xiaomi Phone Agent: Summit Highlights",
        "meta": "Key takeaways from Xiaomi's phone agent summit. MiClaw updates, new AI features, and what it means for Android users in 2026.",
        "category": "Industry & Trends",
        "reading_time": "8 min",
        "internal_links": """
INTERNAL LINK KEYWORDS (embed naturally in text, do NOT add <a> tags):
- "Xiaomi MiClaw" -> /xiaomi-miclaw-explained.html
- "MiClaw" -> /xiaomi-miclaw-explained.html
- "Xiaomi AI" -> /xiaomi-ai-ecosystem-2026.html
- "phone agent" -> /ai-agent-phone-control.html
- "Xiaomi Lobster Phone" -> /xiaomi-lobster-phone-ai-features.html
- "AI phone" -> /ai-phone-war-2026.html
- "agentic ai" -> /agentic-ai-phone-explained.html
- "phone automation" -> /agentic-ai-phone-explained.html
- "AI agent" -> /ai-agent-phone-control.html
- "voice automation" -> /voice-control-android.html
""",
        "sections": [
            "Xiaomi Phone Agent Summit: What Was Announced",
            "MiClaw Software Updates and New Capabilities",
            "Hardware Partnerships and Device Expansion",
            "Developer Tools and Agent Framework",
            "Market Positioning and Competition Outlook",
            "How FoneClaw Complements the Xiaomi Ecosystem",
            "Frequently Asked Questions"
        ]
    }
]


def build_user_prompt(article):
    """Build user prompt for an article."""
    section_list = "\n".join([f"- S{i}: {s}" for i, s in enumerate(article['sections'])])
    return f"""Write an SEO article for foneclaw.ai.

Slug: {article['slug']}
Title: {article['title']} (≤60 characters)
Meta: {article['meta']} (120-160 characters)
Category: {article['category']}
Topic: {article['title']}

Structure (7-8 sections):
{section_list}

{article['internal_links']}

Write the article following ALL rules from the system prompt. Output ONLY the BATCH = [...] Python code, nothing else."""


def call_gemini(system_prompt, user_prompt):
    """Call Gemini API."""
    payload = {
        "contents": [{"parts": [{"text": f"{system_prompt}\n\n{user_prompt}"}]}],
        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 16384}
    }
    resp = requests.post(API_URL, json=payload, timeout=300)
    resp.raise_for_status()
    data = resp.json()
    text = data['candidates'][0]['content']['parts'][0]['text']
    return text


def extract_batch(text):
    """Extract BATCH = [...] from response."""
    # Remove markdown code blocks
    text = re.sub(r'```python\s*', '', text)
    text = re.sub(r'```\s*', '', text)
    
    # Find BATCH = [...]
    match = re.search(r'BATCH\s*=\s*\[', text)
    if match:
        start = match.start()
        # Find matching closing bracket
        bracket_count = 0
        for i in range(start + text[start:].find('['), len(text)):
            if text[i] == '[':
                bracket_count += 1
            elif text[i] == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    return text[start:i+1]
    return None


def validate_article(raw_text, slug):
    """Validate article quality."""
    issues = []
    
    # Check banned words
    banned = ['utilize', 'furthermore', 'robust', 'seamlessly', 'incredibly', 'empower', 'leverage',
              'cutting-edge', 'unparalleled', 'revolutionary', 'game-changer', 'navigate', 'landscape',
              'intricate', 'foster', 'delve', 'tapestry', 'harness', 'paramount', 'pivotal',
              'enshroud', 'multifaceted', 'myriad', 'in conclusion']
    
    text_lower = raw_text.lower()
    found_banned = [w for w in banned if w.lower() in text_lower]
    if found_banned:
        issues.append(f"BANNED WORDS FOUND: {found_banned}")
    
    # Check E-E-A-T
    eeat_patterns = ['based on our testing', 'based on our experience', 'based on our data', 
                     'based on our analysis', 'according to our', 'our testing shows']
    eeat_count = sum(text_lower.count(p) for p in eeat_patterns)
    if eeat_count < 3:
        issues.append(f"E-E-A-T count: {eeat_count} (need ≥3)")
    
    # Check FAQ
    if 'frequently asked questions' not in text_lower:
        issues.append("Missing 'Frequently Asked Questions' section")
    
    # Count Q: and A:
    q_count = len(re.findall(r'Q:', raw_text))
    a_count = len(re.findall(r'A:', raw_text))
    if q_count < 4:
        issues.append(f"FAQ: only {q_count} questions (need 4-5)")
    if a_count < 4:
        issues.append(f"FAQ: only {a_count} answers (need 4-5)")
    
    # Word count
    words = len(raw_text.split())
    if words < 1500:
        issues.append(f"Word count: {words} (need 1500-3000)")
    elif words > 3000:
        issues.append(f"Word count: {words} (over 3000)")
    
    return {
        'banned_words': found_banned,
        'eeat_count': eeat_count,
        'faq_questions': q_count,
        'faq_answers': a_count,
        'word_count': words,
        'issues': issues,
        'pass': len(issues) == 0
    }


def parse_batch_code(batch_code):
    """Parse BATCH code into data structure."""
    # Execute the batch code safely
    local_vars = {}
    exec(batch_code, {}, local_vars)
    return local_vars.get('BATCH', [])


def main():
    raw_outputs = {}
    all_articles = []
    
    for i, article in enumerate(ARTICLES):
        slug = article['slug']
        print(f"\n{'='*60}")
        print(f"[{i+1}/5] Generating: {slug}")
        print(f"{'='*60}")
        
        user_prompt = build_user_prompt(article)
        
        # Call Gemini
        print("  Calling Gemini API...")
        try:
            raw_text = call_gemini(SYSTEM_PROMPT, user_prompt)
            raw_outputs[slug] = raw_text
            print(f"  Got {len(raw_text)} chars response")
        except Exception as e:
            print(f"  ERROR: {e}")
            raw_outputs[slug] = f"ERROR: {e}"
            continue
        
        # Validate
        print("  Validating...")
        validation = validate_article(raw_text, slug)
        print(f"  Banned words: {len(validation['banned_words'])}")
        print(f"  E-E-A-T count: {validation['eeat_count']}")
        print(f"  FAQ questions: {validation['faq_questions']}")
        print(f"  Word count: {validation['word_count']}")
        
        if validation['issues']:
            print(f"  ⚠️  Issues: {validation['issues']}")
        else:
            print(f"  ✅ Validation PASSED")
        
        # Extract and parse batch code
        batch_code = extract_batch(raw_text)
        if batch_code:
            try:
                batch_data = parse_batch_code(batch_code)
                if batch_data:
                    item = batch_data[0]
                    all_articles.append({
                        'slug': item[0],
                        'title': item[1],
                        'meta': item[2],
                        'category': item[3],
                        'reading_time': item[4],
                        'sections': [{'subtitle': s[0], 'body': s[1]} for s in item[5]]
                    })
                    print(f"  ✅ Parsed successfully")
                else:
                    print(f"  ⚠️  Empty batch data")
            except Exception as e:
                print(f"  ⚠️  Parse error: {e}")
        else:
            print(f"  ⚠️  Could not extract BATCH code")
        
        # Wait between API calls
        if i < len(ARTICLES) - 1:
            print("  Waiting 5s before next call...")
            time.sleep(5)
    
    # Save raw outputs
    print(f"\n{'='*60}")
    print("Saving raw outputs...")
    raw_path = '/home/administrator/clawfone-v2/batch_new_articles_raw.py'
    with open(raw_path, 'w', encoding='utf-8') as f:
        f.write("# Raw Gemini outputs for 5 new articles\n")
        f.write(f"# Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for slug, raw in raw_outputs.items():
            f.write(f"# ===== {slug} =====\n")
            f.write(raw)
            f.write(f"\n\n")
    print(f"  Saved to {raw_path}")
    
    # Save JSON data
    json_path = '/home/administrator/clawfone-v2/batch_new_articles_data.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(all_articles, f, indent=2, ensure_ascii=False)
    print(f"  Saved {len(all_articles)} articles to {json_path}")
    
    # Print summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for a in all_articles:
        word_count = sum(len(s['body'].split()) for s in a['sections'])
        print(f"  {a['slug']}: {len(a['sections'])} sections, ~{word_count} words")
    
    return raw_outputs, all_articles


if __name__ == '__main__':
    raw_outputs, all_articles = main()
