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

BATCH = [("slug", "Title", "Meta", "Category", "X min", [("Section", "Body text 250-400 words.\\n\\nParagraph 2..."), ("Frequently Asked Questions", "Q: Question?\\nA: Answer 40-60 words.\\n\\nQ: Question?\\nA: Answer.")])]

FAQ FORMAT: MUST use "Q: " and "A: " prefix. Each Q:A pair separated by \\n\\n. Answer 40-60 words.

BRAND RULES: FoneClaw is independent, NOT Xiaomi. First mention "Xiaomi MiMo-V2.5-Pro", then "MiMo". FAQ must include "Is FoneClaw owned by Xiaomi?" -> "No."

PARAGRAPH STRUCTURE: 3-4 paragraphs per section, 60-100 words each, separated by \\n\\n."""

user_prompt = """Write an SEO article for foneclaw.ai:

Slug: personal-context-ai-agent-phone
Title: The Real AI Race Isn't About Models — It's About Personal Context
Meta: Everyone compares AI model size. But the real advantage is personal context. Phone AI agents like FoneClaw know you better than any cloud AI ever could.
Category: Industry

Structure:
S0: Introduction - Based on AppleMagazine's analysis and our testing of phone AI agents, the AI industry is obsessed with model size. But AppleMagazine made a critical observation: "Siri will not win by answering general questions better than every chatbot. It will win by using personal context safely." This shifts the entire AI race from who has the biggest model to who knows you best. Phone AI agents like FoneClaw have a natural advantage here because they run on your device, right next to your personal data. Open with E-E-A-T.

S1: The Model Size Myth - The AI industry measures everything in parameters, training tokens, and benchmark scores. ChatGPT can answer questions about quantum physics. Gemini can write poetry. But neither knows that you sent your boss a file last Tuesday, or that your daughter has a soccer game on Saturday. Model size matters for general knowledge, but personal context matters for personal productivity. Based on our data, users care more about an assistant that remembers their preferences than one that can quote Shakespeare.

S2: What Apple Learned About Personal Context - AppleMagazine argues that Siri's real advantage is system access: "It can interact with Apple apps, device settings, messages, reminders, calendars, music, contacts, and other personal areas in ways that a regular chatbot cannot." Apple promised a more personal Siri through Apple Intelligence, including better awareness of personal context and the ability to take action across apps. But those features have been delayed, making the gap more visible as competitors move quickly.

S3: Why Phone Agents Have the Personal Context Advantage - Phone AI agents take Apple's insight further. They run directly on your Android phone, which means they have instant access to your contacts, messages, call history, photos, calendar, and location — all without sending data to external servers. Based on our testing, this local access makes the agent respond faster and understand your habits better than any cloud-based assistant. The agent learns your daily patterns: when you wake up, what apps you use first, who you message most.

S4: How Personal Context Works in Practice - 5 real scenarios:
1. "Call mom and say I'll be late" — understands who "mom" is, how late, and what to say
2. "Send last week's meeting notes to Zhang San" — finds the notes, finds the contact, sends them
3. "Buy milk on the way home" — locates you, recommends a store on your route
4. "Organize today's photos into the travel album" — recognizes photos, categorizes, moves them
5. "Remind me to bring an umbrella tomorrow morning" — checks weather, sets reminder, links to calendar

S5: Cloud AI vs Phone Agent — The Personal Data Gap - Comparison table: 5 dimensions
- Data location: Cloud = remote servers vs Phone = your device
- Access speed: Cloud = network dependent vs Phone = instant
- Privacy: Cloud = data leaves device vs Phone = data stays local
- Personalization: Cloud = generic vs Phone = learns your habits
- Offline capability: Cloud = no vs Phone = yes for local tasks

S6: Conclusion — The Future Belongs to AI That Knows You
- Models will keep getting bigger and smarter
- But personal context is the real moat
- FoneClaw is phone-first, personal-context-first

S7: FAQ:
Q1: What is personal context in AI agents?
Q2: How does FoneClaw use my personal data?
Q3: Is personal context better than a larger AI model?
Q4: Can Siri use personal context like phone agents?
Q5: Is FoneClaw owned by Xiaomi?

Primary keywords: personal context AI agent, AI assistant personal data, phone agent knows you
Long-tail: why Siri needs personal context, local AI agent user data advantage, personal context voice control phone
Internal links: AI agent, voice control, phone agent, local AI agent, Apple Intelligence, Siri, AI assistant, Xiaomi AI, task automation, cloud vs local

Include "Based on our testing/experience/data" citations (3+ times). Each section 3-4 paragraphs separated by \\n\\n. FAQ uses Q:/A: format with 5 questions. Output BATCH Python code only."""

url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=' + api_key
payload = {
    'contents': [{'parts': [{'text': SYSTEM_PROMPT + '\n\n' + user_prompt}]}],
    'generationConfig': {'temperature': 0.7, 'maxOutputTokens': 16384}
}

print('Calling Gemini 3.5 Flash...')
resp = requests.post(url, json=payload, timeout=300)
print(f'Status: {resp.status_code}')

if resp.status_code == 200:
    result = resp.json()
    if 'candidates' in result:
        content = result['candidates'][0]['content']['parts'][0]['text']
        content = content.replace('```python', '').replace('```', '').strip()
        with open('/home/administrator/clawfone-v2/batch_context_raw.py', 'w') as f:
            f.write(content)
        print(f'Saved ({len(content.split())} words)')
    else:
        print(f'No candidates: {str(result)[:200]}')
else:
    print(f'Error: {resp.text[:200]}')
