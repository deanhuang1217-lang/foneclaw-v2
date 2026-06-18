import requests, json, os

# Read API Key
with open('/home/administrator/video-workflow/.env') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY'):
            api_key = line.strip().split('=', 1)[1]
            break

SYSTEM_PROMPT = """You are an SEO writer. Output ONLY Python BATCH code. No explanation, no thinking, no markdown. Just the code.

BATCH format:
BATCH = [("slug", "Title", "Meta 120-160 chars", "Category", "X min", [("Section Title", "Body 250-400 words with \\n\\n paragraphs"), ...])]

Rules:
- 8 sections total (7 content + 1 FAQ)
- Each section 3-4 paragraphs, 60-100 words each, separated by \\n\\n
- FAQ uses Q:/A: format, 5 questions
- No banned words: utilize, furthermore, robust, seamlessly, incredibly, empower, leverage, cutting-edge, unparalleled, revolutionary, game-changer, navigate, landscape, intricate, foster, delve, tapestry, paramount, pivotal, enshroud, multifaceted, myriad, additionally, nuanced, absolutely, fundamentally
- Use "Based on our testing/experience" for E-E-A-T (3+ times)
- Write in second person "you"
- Mention FoneClaw max 1 time per paragraph
- FAQ must include "Is FoneClaw owned by Xiaomi?" -> "No. FoneClaw is an independent startup, not affiliated with Xiaomi."
- First mention of Xiaomi: "Xiaomi MiMo-V2.5-Pro", then can say "MiMo"

OUTPUT: Only valid Python BATCH code. No explanation."""

user_prompt = """Write BATCH code for foneclaw.ai:

Slug: apple-local-ai-validates-phone-agent
Title: Apple's Local AI Push Validates What Phone Agents Already Do
Meta: Apple TV 4K gets A17 Pro for local AI. HomePod mini still needs cloud. Phone agents like FoneClaw had local AI from day one.
Category: Industry

Sections:
S0: Intro - Based on 9to5Mac's report and our testing of phone AI agents, Apple is finally rolling out local AI to Apple TV 4K with the A17 Pro chip this fall. But HomePod mini with its S9 chip cannot run AI locally and must rely on cloud streaming. Meanwhile, phone AI agents like FoneClaw have been running AI locally on Android devices from the start. Apple's push into local AI validates the approach phone agents have always taken.

S1: What Apple Announced - Apple TV 4K will upgrade from A15 to A17 Pro chip. HomePod mini will upgrade from S5 to S9 chip. Both launching this fall alongside iOS 27 and next-gen Siri. Apple delayed these releases because they wanted to tie hardware to Apple Intelligence features. Now with Google Gemini partnership and Private Cloud Compute, Apple finally has its AI rollout in order.

S2: A17 Pro Enables Local AI on Apple TV - The A17 Pro chip gives Apple TV 4K enough power to run Apple's AI models locally. This means faster responses, better privacy, and no internet dependency. But Apple TV is a stationary device plugged into your TV. You cannot carry it with you. Phone agents run the same local AI on a device you already carry everywhere.

S3: HomePod mini's Cloud Problem - The S9 chip in HomePod mini cannot run AI models locally. All Apple Intelligence features must stream through the cloud. This means latency, privacy concerns, and dependency on internet connection. Phone agents avoid this entirely by running on your phone's processor.

S4: Why Phone Agents Had Local AI First - Phone agents like FoneClaw have always run locally on your Android device. No cloud dependency, no latency, no privacy concerns. Based on our testing, local processing on a phone responds in under 50 milliseconds. Apple is just now bringing this capability to Apple TV, while phone agents have had it for years.

S5: The Privacy Advantage - Local AI means your data never leaves your device. Cloud AI means your data goes to remote servers. Apple's own research shows they care about privacy, yet HomePod mini still sends data to the cloud. Phone agents give you the privacy Apple promises but cannot always deliver.

S6: What This Means for Users - Apple's move proves local AI is the future. Phone agents are already there. The best AI assistant is one that works on your device, respects your privacy, and responds instantly. FoneClaw delivers this today.

S7: FAQ:
Q1: What is local AI and why does it matter?
Q2: Can Apple TV run AI without internet?
Q3: Why can't HomePod mini run AI locally?
Q4: How does FoneClaw compare to Apple TV for local AI?
Q5: Is FoneClaw owned by Xiaomi?

Primary: Apple TV local AI phone agent, HomePod mini cloud AI vs phone agent, Apple Intelligence local processing phone
Long-tail: Apple TV A17 Pro local AI, HomePod mini cloud dependent AI, phone agent vs Apple TV AI
Internal: AI agent, local AI agent, cloud vs local, voice control, phone agent, task automation, Xiaomi AI, AI assistant, OpenClaw, Gemini Intelligence

Include "Based on our testing/experience" 3+ times. Each section 3-4 paragraphs separated by \\n\\n. FAQ Q:/A: format. Output BATCH Python code only."""

url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={api_key}'
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
        batch_start = content.find('BATCH')
        if batch_start > 0:
            content = content[batch_start:]
        with open('/home/administrator/clawfone-v2/batch_apple_local_raw.py', 'w') as f:
            f.write(content)
        print(f'Saved ({len(content.split())} words)')
    else:
        print(f'No candidates: {str(result)[:200]}')
else:
    print(f'Error: {resp.text[:200]}')
