import requests, json

# Read API Key
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

Slug: ai-agent-from-lab-to-pocket
Title: From Lab to Pocket: How AI Agents Are Reaching Everyone
Meta: Anthropic research shows coding agents are transforming science. Phone AI agents bring that same power to your Android device in 2026.
Category: Industry

Structure:
S0: Introduction - Based on Anthropic's new survey of 1,260 social scientists, AI coding agents are transforming how we study the economy and society. But this technology is not staying in research labs. The same agent capabilities that automate research tasks are now migrating to your pocket through phone AI agents. Open with E-E-A-T: "Based on Anthropic's new survey of 1,260 social scientists fielded in early 2026..." Mention that AI agent automation phone is the next frontier.

S1: What the Anthropic Survey Found - Anthropic surveyed 1,260 quantitative social scientists in Feb-March 2026. 81% have tried AI chatbots for research, but only 20% regularly use coding agents like Claude Code. Claude Code dominates with 86% market share among coding agent users, Codex at 31%. Economics has 39% adoption, political science 25%, but public health only 6%, education 4%. The Claude Code AI agent adoption rate 2026 shows massive growth potential.

S2: How AI Agents Automate Research Tasks - Coding agents automate "irreducibly human steps" in empirical research. They take a research idea and dataset, write and run analysis code, interpret output, and iterate autonomously. 97% of coding agent users use them to generate analysis code. The workflow: research idea -> dataset -> code -> analysis -> interpretation -> iteration. This is how AI agents automate research tasks at scale.

S3: The Adoption Gap — And Why It Matters - Male-named researchers adopt coding agents at 2x the rate of female-named researchers. Doctoral students and postdocs: 25%+ adoption. Tenured professors: less than half that. Top 25 universities: 40% more likely to use agents. This is a local AI agent vs cloud issue too — cloud-based tools require subscriptions and internet access, creating barriers.

S4: From Desktop to Phone — The Democratization of AI Agents - Core argument: Phone AI agents democratize access. Zero deployment, no virtual machines, no programming background needed. FoneClaw's voice control lets anyone use natural language to control their phone. While coding agents need Claude Code or Codex on a desktop, phone agents like FoneClaw run directly on your Android device. Xiaomi AI ecosystem also entering this space. This is AI agent accessibility phone at its best.

S5: What This Means for the AI Agent Market in 2026 - The agent market is still early. Global paid agent users only around 1 million. But the trajectory from academic research to daily life is clear. AI agent spending is growing as more people discover these tools.

S6: Conclusion — The Agent Revolution Is Personal - Coding agents proved AI can do real work. Phone AI agents bring that power to everyone. FoneClaw AI agent is phone-first, making the agent revolution personal and accessible.

S7: FAQ:
Q1: What did Anthropic's survey find about AI coding agents?
Q2: How many researchers use Claude Code for social science research?
Q3: Can phone AI agents do what coding agents do?
Q4: How does FoneClaw compare to Claude Code for AI agent tasks?
Q5: Is FoneClaw owned by Xiaomi?

Primary keywords:
- AI agent automation phone (title, S0, S4, conclusion)
- AI agent 2026 (S0, S5, FAQ)
- FoneClaw AI agent (S0, S4, S6, FAQ)

Long-tail keywords:
- Claude Code AI agent adoption rate 2026 (S1)
- AI agent from lab to pocket (S0, S4)
- how AI agents automate research tasks (S2)
- AI agent accessibility phone (S4)
- Anthropic coding agents social sciences (S1)

Internal link keywords (build system auto-links):
- AI agent
- Claude Code
- phone agent
- voice control
- local AI agent
- AI agent spending
- cloud vs local
- task automation
- Xiaomi AI
- AI assistant

Include "Based on our testing/experience/data" citations (3+ times).
Each section must have 3-4 paragraphs separated by \\n\\n.
FAQ must use Q:/A: format with 5 questions.

Output BATCH Python code only."""

# Call API
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
                print(f'  ✅ Success! Content length: {len(content)} chars')
                break
            else:
                print(f'  ⚠️ No candidates: {str(result)[:200]}')
        else:
            print(f'  ❌ Error: {resp.text[:200]}')
    except Exception as e:
        print(f'  ❌ Exception: {e}')

if content:
    with open('/home/administrator/clawfone-v2/batch_lab_to_pocket_raw.py', 'w') as f:
        f.write(content)
    word_count = len(content.split())
    print(f'\n✅ Saved ({word_count} words)')
else:
    print('\n❌ All models failed')
