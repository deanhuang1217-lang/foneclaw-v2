import requests, json

with open('/home/administrator/video-workflow/.env') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY'):
            api_key = line.strip().split('=', 1)[1]
            break

SYSTEM_PROMPT = """You are a senior SEO content writer for foneclaw.ai, a tech blog about AI agents and voice control on Android phones.

WRITING STYLE (CRITICAL):
1. Each section MUST be 250-400 words with 3-4 paragraphs (use \\n\\n between paragraphs)
2. Each paragraph should be 60-100 words
3. Use specific examples, scenarios, and data points
4. Write in second person "you" - address the reader directly
5. Use short sentences mixed with longer ones for rhythm
6. Include at least 1 specific number/statistic per section
7. Use "Based on our testing/experience/data" for E-E-A-T (at least 3 times total)
8. Reference real-world scenarios (driving, cooking, working, exercising)
9. Mention specific apps by name (WhatsApp, Spotify, Google Maps, etc.)
10. Alternate between "FoneClaw" and "the app/agent/tool" (max 1 FoneClaw per paragraph)

BANNED WORDS (NEVER use these):
utilize, furthermore, robust, seamlessly, incredibly, empower, leverage, cutting-edge, unparalleled, revolutionary, game-changer, navigate, landscape, intricate, foster, delve, tapestry, paramount, pivotal, enshroud, multifaceted, myriad, in conclusion, additionally, nuanced, absolutely, fundamentally

OUTPUT FORMAT:
Output ONLY valid Python BATCH code. No explanation, no markdown code blocks.

BATCH = [
    (
        "slug-with-hyphens",
        "Title with main keyword",
        "Meta description 120-160 chars with keyword",
        "Category",
        "X min",
        [
            ("Section 1 Title", "Body text 250-400 words.\\n\\nParagraph 2...\\n\\nParagraph 3..."),
            ("Frequently Asked Questions", "Q: Question?\\nA: Answer 40-60 words.\\n\\nQ: Question?\\nA: Answer."),
        ]
    ),
]

FAQ FORMAT:
- MUST use "Q: " and "A: " prefix (with colon and space)
- Each Q:A pair separated by \\n\\n
- NEVER use **bold** or numbered lists
- Answer should be 40-60 words with specific details

BRAND RULES:
- FoneClaw is independent startup, NOT Xiaomi
- MiMo is Xiaomi model, FoneClaw supports but does not own it
- First mention: "Xiaomi MiMo-V2.5-Pro", then can say "MiMo"
- Never say "FoneClaw MiMo" or imply ownership
- FAQ must include: "Is FoneClaw owned by Xiaomi?" -> "No. FoneClaw is an independent..."

PARAGRAPH STRUCTURE:
- Each section must have 3-4 paragraphs
- Use \\n\\n to separate paragraphs within a section
- Each paragraph should be 60-100 words"""

user_prompt = """Write an SEO article for foneclaw.ai:

Slug: gemini-spark-vs-foneclaw
Title: Gemini Spark vs FoneClaw: Which 24/7 AI Assistant Wins?
Meta: TechCrunch tested Google Gemini Spark. It cannot use Google Keep, sends data to the cloud, and needs its own toggle. FoneClaw offers a voice-first, local alternative.
Category: Comparisons

Structure:
S0: Introduction - Based on TechCrunch's hands-on review of Gemini Spark published May 30, 2026, Google's new 24/7 AI assistant is "a fairly useful implementation of consumer AI, but not one that deserves to have its own brand." The reviewer tested Spark on shopping savings, packing lists, newsletter summaries, weekend activities, and price tracking. While Spark performed reasonably well, its limitations reveal why phone-based AI agents like FoneClaw offer a compelling alternative. Open with E-E-A-T.

S1: What Is Gemini Spark? - Google's new 24/7 agentic assistant, introduced at Google I/O 2026. Runs on cloud virtual machines. CEO Sundar Pichai joked "yes, you can close your laptop" — comparing to OpenClaw which needs machines running. Integrates with Gmail, Calendar, Docs, Sheets, Slides. Positioned as "agentic AI for the rest of us." Based on our analysis of the AI assistant market, this is Google's play to capture the mainstream agent market.

S2: Spark's Strengths (From TechCrunch Testing) - 5 real test cases from TechCrunch:
1. Shopping savings: Found Walgreens deals and coupon stacking (one promo code was invalid though)
2. Packing list: Weather-based suggestions, reminded dogs weren't allowed
3. Newsletter summary: Weekly Top 5 articles from email (returned 4 instead of 5)
4. Weekend activities: Found local events including "Beaver Queen Pageant"
5. Price tracking: Set up biweekly price checks for eye cream
Overall: "surprisingly useful" but with small issues.

S3: Spark's 5 Limitations - The real problems TechCrunch identified:
1. Cannot use Google Keep — personal productivity oversight
2. No non-Google service integration (Resy, flight booking, etc.)
3. Cannot send texts
4. Independent brand adds cognitive burden — should just be a Gemini feature
5. Cloud-based — all data flows through Google's servers
These limitations highlight why phone-based agents matter.

S4: Head-to-Head Comparison Table - 7 dimensions comparison:
- Deployment: Spark = cloud VM, FoneClaw = on your phone
- Privacy: Spark = Google servers, FoneClaw = local processing
- App Support: Spark = Google apps only, FoneClaw = any Android app
- Activation: Spark = open Gemini app + toggle, FoneClaw = voice command
- Recurring Tasks: Both support, but Spark limited to Google ecosystem
- Brand: Spark = separate toggle, FoneClaw = phone-native
- Offline: Spark = no, FoneClaw = yes for local tasks

S5: Why Phone Agents Like FoneClaw Win - 4 advantages:
1. Local processing — data never leaves your phone
2. Voice-first — say a command, it happens, no app switching
3. Any app — not locked into Google ecosystem
4. Privacy — Android permission system gives you control
Based on our testing, voice control on Android has reached a level where it can replace app-based interactions for most daily tasks.

S6: Conclusion — Spark for Google Fans, FoneClaw for Everyone Else
- Spark is great if you live in Google's ecosystem
- FoneClaw is better if you want privacy, freedom, and voice-first
- The best AI assistant is the one that fits YOUR workflow

S7: FAQ:
Q1: What is Gemini Spark and how does it work?
Q2: Can Gemini Spark control apps outside Google?
Q3: How does FoneClaw compare to Gemini Spark for voice control?
Q4: Is Gemini Spark free or does it cost money?
Q5: Is FoneClaw owned by Xiaomi?

Primary keywords:
- Gemini Spark vs FoneClaw (title, S0, S4, S6, FAQ)
- Gemini Spark alternative (S0, S5, S6)
- 24/7 AI assistant phone (S0, S5, S6, FAQ)

Long-tail keywords:
- Google Gemini Spark vs phone AI agent comparison (S4)
- Gemini Spark limitations no Google Keep (S3)
- best AI assistant 2026 no cloud required (S5)
- Gemini Spark vs FoneClaw voice control (S5)
- 24/7 AI assistant alternative to Google Spark (S6)

Internal link keywords (build system auto-links):
- AI agent
- voice control
- phone agent
- task automation
- local AI agent
- cloud vs local
- Gemini Intelligence
- OpenClaw
- AI assistant
- Xiaomi AI

Include "Based on our testing/experience/data" citations (3+ times).
Each section must have 3-4 paragraphs separated by \\n\\n.
FAQ must use Q:/A: format with 5 questions.

Output BATCH Python code only."""

models_to_try = ['gemini-3.5-flash', 'gemini-3-flash']
content = None

for model in models_to_try:
    print(f'Trying {model}...')
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}'
    payload = {
        'contents': [{'parts': [{'text': f'{SYSTEM_PROMPT}\n\n{user_prompt}'}]}],
        'generationConfig': {'temperature': 0.7, 'maxOutputTokens': 16384}
    }
    try:
        resp = requests.post(url, json=payload, timeout=300)
        print(f'  Status: {resp.status_code}')
        if resp.status_code == 200:
            result = resp.json()
            if 'candidates' in result:
                content = result['candidates'][0]['content']['parts'][0]['text']
                content = content.replace('```python', '').replace('```', '').strip()
                print(f'  ✅ {len(content)} chars')
                break
            else:
                print(f'  ⚠️ No candidates')
        else:
            print(f'  ❌ {resp.text[:150]}')
    except Exception as e:
        print(f'  ❌ {e}')

if content:
    with open('/home/administrator/clawfone-v2/batch_spark_raw.py', 'w') as f:
        f.write(content)
    print(f'\n✅ Saved ({len(content.split())} words)')
else:
    print('\n❌ All models failed')
