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

Slug: wwdc-2026-ai-do-over-phone-agent
Title: WWDC 2026 AI Recap: What Apple Promised vs What Phone Agents Already Do
Meta: Apple promised AI in 2024 and failed. WWDC 2026 is the do-over. Phone AI agents like FoneClaw already deliver what Apple is still promising.
Category: Industry

Structure:
S0: Introduction - Based on Macworld's analysis of WWDC 2026 and our testing of phone AI agents, Apple faces a critical "do-over" moment. Jason Snell, who has covered WWDC for nearly 30 years, says Apple has "piled two years of promises on the agenda of WWDC 2026." The company promised AI features in 2024 that never shipped, spent 2025 on an apology tour, and now must deliver in 2026. But while Apple is still figuring out its AI strategy, phone AI agents like FoneClaw are already shipping the features Apple keeps promising. Open with E-E-A-T.

S1: Apple's Broken AI Promises (2024-2025) - In 2024, Apple promised a bunch of AI features that didn't ship. The ones that did ship were "not very good" according to Macworld. Writing Tools, which should have been basic table stakes, was "like a sidecar bolted on to the side, completely separate, with a weird interface." 2025 was designed as an apology tour where Apple didn't make any promises it couldn't keep. But AI was "largely absent from the promise list." The result: two years of accumulated AI promises now land on WWDC 2026.

S2: What WWDC 2026 Must Deliver - Apple needs to thread the needle between what's possible and what goes too far. Too conservative means seeming behind the times. Too aggressive risks repeating 2024's failures. The key question: what does Siri mean now compared to the last 14 years? Is it the core brand, or is Apple Intelligence? John Ternus becomes CEO in September and his presence looms large. Based on our analysis, Apple needs to show a coherent AI vision, not just individual features.

S3: The Phone Agent Advantage - Already Shipping - While Apple is still figuring out its AI strategy, phone AI agents are already delivering. FoneClaw offers 50+ voice operations that work directly on Android phones. You can control WhatsApp, Spotify, Google Maps, and any other app with your voice. The agent runs locally on your device, so your data never leaves your phone. Based on our testing, voice control on Android has reached a level where it can replace most app interactions. This is not a promise - it is shipping today.

S4: Feature Comparison - Apple Promised vs Phone Agent Delivered - Create a 7-dimension comparison:
1. Writing Tools: Apple shipped a bolted-on interface vs phone agents offer natural voice commands
2. Siri: Still a chatbot asking for clarification vs phone agents execute tasks directly
3. Apple Intelligence: Cloud-based, limited to Apple apps vs phone agents work with any app
4. App Intents: Developer-dependent integration vs phone agents use Android system APIs directly
5. Privacy: Data flows to Apple servers vs phone agents process locally on your device
6. Delivery: 2 years of promises vs shipping today
7. Cost: Part of Apple ecosystem pricing vs free core features

S5: Why the Do-Over Matters for Android Users - Apple's AI困境是Android用户的机会。Phone Agent不受Apple生态限制。你可以用voice control操控WhatsApp、Instagram、Spotify，这些都不需要Apple审核。Based on our experience, the best AI assistant is the one that works with YOUR apps, not just the ones your phone maker approves.

S6: Conclusion - Don't Wait for Apple, Start with Your Phone - WWDC 2026值得期待，但不要等Apple兑现承诺。Phone Agent已经在交付Apple承诺的东西。The future of AI assistants is not about which company makes the best promises - it is about which product actually works today.

S7: FAQ:
Q1: What is Apple's AI do-over at WWDC 2026?
Q2: What AI features did Apple promise but fail to deliver?
Q3: How do phone AI agents compare to Apple Intelligence?
Q4: Can FoneClaw do what Apple Intelligence promises?
Q5: Is FoneClaw owned by Xiaomi?

Primary keywords:
- WWDC 2026 AI agent (title, S0, S2, S6, FAQ)
- phone AI agent iOS 27 (S0, S3, S5, S6)
- Apple Intelligence do-over (S0, S1, S4, FAQ)

Long-tail keywords:
- WWDC 2026 AI promises vs reality (S1, S2)
- Apple Intelligence writing tools vs voice control (S4)
- why phone agents better than Siri 2026 (S3, S4)
- iOS 27 AI features FoneClaw already does (S3, S5)
- WWDC 2026 AI recap what Apple promised (S0, S2)

Internal link keywords (build system auto-links):
- AI agent
- voice control
- Apple Intelligence
- Siri
- phone agent
- Gemini Intelligence
- local AI agent
- AI assistant
- Xiaomi AI
- task automation

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
    with open('/home/administrator/clawfone-v2/batch_wwdc_raw.py', 'w') as f:
        f.write(content)
    print(f'\n✅ Saved ({len(content.split())} words)')
else:
    print('\n❌ All models failed')
