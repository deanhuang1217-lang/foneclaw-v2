import requests, json

# Read API Key
with open('/home/administrator/video-workflow/.env') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY'):
            api_key = line.strip().split('=', 1)[1]
            break

# System Prompt
SYSTEM_PROMPT = """You are a senior SEO content writer for foneclaw.ai, a tech blog about AI agents and voice control on Android phones.

WRITING STYLE (CRITICAL - follow these rules exactly):
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
            ("Section 2 Title", "Body text 250-400 words."),
            ("Frequently Asked Questions", "Q: Question?\\nA: Answer 40-60 words.\\n\\nQ: Question?\\nA: Answer."),
        ]
    ),
]

FAQ FORMAT (CRITICAL):
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

PARAGRAPH STRUCTURE (CRITICAL):
- Each section must have 3-4 paragraphs
- Use \\n\\n to separate paragraphs within a section
- Each paragraph should be 60-100 words"""

# User Prompt
user_prompt = """Write an SEO article for foneclaw.ai:

Slug: cloud-vs-local-ai-agent-2026
Title: Cloud AI Agent vs Local Phone Agent: Two Routes Shaping 2026
Meta: Cloud agents like MuleRun need zero setup. Local agents like FoneClaw run on your phone. We compare the two AI agent routes dominating 2026.
Category: Industry

Structure:
S0: Introduction - The AI agent market is splitting into two distinct routes in 2026. Open with E-E-A-T: "Based on our analysis of the AI agent market in 2026...". Mention that global AI agent paid users are only around 1 million. Introduce cloud vs local divergence. Mention FoneClaw as a local phone agent.

S1: The OpenClaw Craze and Its Aftermath - OpenClaw (lobster) craze recap: WeChat index surged from 2.53M to 165M then dropped 75%. OpenClaw showed people that agents and chatbots are different things, but the barrier was too high (needed virtual machines/Mac Minis). Engineering issues: "updated itself into breaking multiple times". The craze left behind educated potential users.

S2: The Cloud Route — Alibaba MuleRun - Alibaba Cloud's MuleRun (Mule Run) product. Created by Chen Yusen (youngest VP at Alibaba Cloud, born post-90s). Positioned as "AI Workforce". Serves 43 countries. 34% of users spend $200+/month. Deep user retention is "almost zero churn". Core selling point: zero deployment, no downloads needed. Enterprise cases: World Aquatics, Latin American data center operator.

S3: The Local Route — Phone-Based AI Agents - Local phone agent route. FoneClaw, Xiaomi MiClaw, etc. Advantages: privacy (data stays on phone), low latency (local processing), offline capability, always-on. Phone is the most personal device, agents running on phone is most natural. Reference voice control and task automation scenarios.

S4: Cloud vs Local — Head-to-Head Comparison - Comparison table. Dimensions: deployment barrier, data privacy, offline capability, processing power, cost, use cases. Cloud suits enterprise-scale tasks. Local suits personal privacy and daily phone operations. "phone agent" concept.

S5: The Market Is Still Wide Open - Market data: out of 7 billion people globally, about 1 billion have used ChatGPT, tens of millions pay. But only about 1 million have used agent products, with ~1M paying. Extremely low penetration. "It's hard to find competitors" — customers buy immediately when they see good products. Reference AI agent spending data.

S6: What This Means for Users - FoneClaw positioning: phone-first, cloud-optional. Future: hybrid architecture. Agents will have "personality". User choice matters.

S7: FAQ - 5 questions:
Q1: What is the difference between a cloud AI agent and a local AI agent?
Q2: Is Alibaba MuleRun available for individual users?
Q3: Can FoneClaw work without internet?
Q4: Which is more secure — cloud or local AI agent?
Q5: Is FoneClaw owned by Xiaomi?

Primary keywords to use naturally:
- cloud AI agent vs local AI agent (in title, first paragraph, S4, FAQ Q1, conclusion)
- AI agent 2026 (in title/intro, S5, conclusion)
- FoneClaw AI agent (in S0, S3, S6, FAQ)

Long-tail keywords to embed naturally:
- cloud AI agent vs phone agent comparison (S4)
- Alibaba MuleRun AI agent review (S2)
- best AI agent no installation required (S2)
- local AI agent vs cloud agent pros cons (S4)
- AI agent market size enterprise 2026 (S5)

Internal link keywords to use naturally in the text (build system auto-links these):
- AI agent
- OpenClaw
- voice control
- task automation
- AI assistant
- Gemini Intelligence
- Xiaomi AI
- phone agent
- AI agent spending
- local processing

Include "Based on our testing/experience/data" citations (3+ times).
Each section must have 3-4 paragraphs separated by \\n\\n.
FAQ must use Q:/A: format with 5 questions.

Output BATCH Python code only."""

# Call API - try gemini-3.1-pro first, fallback
models_to_try = ['gemini-3.1-pro', 'gemini-3.5-flash', 'gemini-3-flash']
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
                print(f'  ✅ Success! Content length: {len(content)} chars')
                break
            else:
                print(f'  ⚠️ No candidates: {str(result)[:200]}')
        else:
            print(f'  ❌ Error: {resp.text[:200]}')
    except Exception as e:
        print(f'  ❌ Exception: {e}')

if content:
    with open('/home/administrator/clawfone-v2/batch_cloud_local_raw.py', 'w') as f:
        f.write(content)
    word_count = len(content.split())
    print(f'\n✅ Saved to batch_cloud_local_raw.py ({word_count} words)')
else:
    print('\n❌ All models failed')
