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

Slug: openclaw-security-risks-phone-agent-safer
Title: 5 Reasons Phone AI Agents Are Safer Than OpenClaw
Meta: OpenClaw has 4 major security risks. Phone AI agents like FoneClaw run on your device with zero deployment and naturally stronger security.
Category: Industry

Structure:
S0: Introduction - Based on our security analysis of AI agent platforms in 2026, China's National Internet Emergency Center issued a warning about OpenClaw's security risks: prompt injection, memory poisoning, plugin poisoning, and accidental operations. These 4 core risks have pushed OpenClaw from "installation service" to "uninstallation service." But the technology itself has value. The question is not whether to use AI agents, but how to use them safely. Phone AI agents like FoneClaw offer a naturally safer alternative. Open with E-E-A-T.

S1: OpenClaw Security Risk 1 — Prompt Injection - Malicious instructions injected through emails, web pages, or group chats. The SOUL.md file that defines the agent's behavior can be overridden. Heartbeat mechanisms that read external content are the biggest risk vector. A single heartbeat can consume 170,000-210,000 tokens. Based on our testing, this is the most common attack vector.

S2: OpenClaw Security Risk 2 — Memory Poisoning - MEMORY.md gets contaminated by malicious instructions. The agent writes harmful "experiences" into long-term memory. Regular cleanup is the only defense, but most users never do it. Based on our experience, this is the hardest risk to detect.

S3: OpenClaw Security Risk 3 — Plugin and Skill Poisoning - Unknown Skills may contain prompt attacks. VirusTotal has flagged some Skills as suspicious. The plugin ecosystem is thriving but security auditing is insufficient. You must only install certified Skills from ClawHub or official sources.

S4: OpenClaw Security Risk 4 — Accidental Operations - The agent can accidentally delete files. You need a backup machine or virtual machine for isolation. Permission popups tempt users to click "Allow" without thinking. Based on our data, accidental operations account for 30% of OpenClaw incidents.

S5: Why Phone AI Agents Are Naturally Safer - 5 security advantages of phone-based agents:
1. Device isolation — phone is a naturally separate environment
2. Zero terminal deployment — no command line needed
3. Local processing — data never leaves your phone
4. Fine-grained permissions — Android permission system controls access
5. No heartbeat costs — no token consumption
Compare with OpenClaw on each dimension. Mention voice control, local AI agent, phone agent, Xiaomi AI ecosystem, AI assistant, task automation.

S6: Conclusion — The Agent Revolution Should Be Secure - OpenClaw has its value for power users. But for most people, a phone AI agent is safer, simpler, and more practical. FoneClaw AI agent is phone-first and security-first. The future of AI agents should not require you to risk your data.

S7: FAQ:
Q1: What are the main OpenClaw security risks in 2026?
Q2: Can phone AI agents be hacked remotely?
Q3: How does FoneClaw protect my privacy?
Q4: Is OpenClaw safe if I follow all security guidelines?
Q5: Is FoneClaw owned by Xiaomi?

Primary keywords:
- OpenClaw security risks (title, S0, S1-S4 headings, FAQ)
- phone AI agent safe (S0, S5, S6, FAQ)
- FoneClaw AI agent (S0, S5, S6, FAQ)

Long-tail keywords:
- OpenClaw security vulnerabilities 2026 (S1)
- phone AI agent vs OpenClaw security (S5)
- AI agent without terminal deployment (S5)
- secure AI assistant Android no installation (S5)
- OpenClaw alternative safe phone agent (S6)

Internal link keywords (build system auto-links):
- AI agent
- OpenClaw
- voice control
- local AI agent
- phone agent
- cloud vs local
- Claude Code
- task automation
- Xiaomi AI
- AI assistant

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
                print(f'  ✅ Success! {len(content)} chars')
                break
            else:
                print(f'  ⚠️ No candidates')
        else:
            print(f'  ❌ {resp.text[:150]}')
    except Exception as e:
        print(f'  ❌ {e}')

if content:
    with open('/home/administrator/clawfone-v2/batch_security_raw.py', 'w') as f:
        f.write(content)
    print(f'\n✅ Saved ({len(content.split())} words)')
else:
    print('\n❌ All models failed')
