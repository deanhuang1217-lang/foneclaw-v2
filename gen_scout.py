import os, json, requests

api_key = None
with open('/home/administrator/video-workflow/.env') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY'):
            api_key = line.split('=', 1)[1].strip()
            break

print(f"API Key loaded: {api_key[:8]}...")

SYSTEM_PROMPT = """You are a senior SEO content writer for foneclaw.ai, a local AI agent app for Android phones.

RULES:
1. Write in English, professional but accessible tone
2. Every section must have 3-4 paragraphs, each 60-100 words
3. Include "Based on our analysis/testing/experience" citations (E-E-A-T) at least 3 times, INCLUDING the first paragraph
4. Use "you" and "your" frequently to address the reader
5. NO banned words: utilize, furthermore, robust, seamlessly, navigate, landscape, game-changer, absolutely, fundamentally, additionally, delve, tapestry, multifaceted, nuanced, intricate, foster, realm, leverage, cutting-edge, unparalleled, revolutionary, empower, incredibly
6. NO markdown tables or pipe characters in body text
7. DO NOT use triple quotes anywhere in output. Use string concatenation with + for long text.
8. FAQ must use Q:/A: format with 5 questions
9. Title must be <= 45 characters (system appends " - FoneClaw")
10. Meta description must be 120-160 characters, NO internal quotes

OUTPUT FORMAT: Python BATCH variable only. No explanation."""

prompt = """Write an SEO article for foneclaw.ai:

Slug: microsoft-scout-openclaw-ai-agent
Title: Microsoft Scout: OpenClaw Goes Enterprise
Meta: Microsoft built Scout, an AI agent based on OpenClaw. We explore why Microsoft chose OpenClaw and what it means for FoneClaw users in the OpenClaw ecosystem.
Category: Industry & Trends
Read time: 8 min

SECTIONS (7 sections including FAQ):

S0: Introduction
- Hook: At Build 2026, Microsoft unveiled Scout, a new AI agent built on OpenClaw technology
- This is huge: Microsoft chose an open-source project as the foundation for its enterprise AI agent
- FoneClaw is part of the same OpenClaw ecosystem
- E-E-A-T: "Based on our analysis of Microsoft Build 2026 announcements..."
- The OpenClaw ecosystem just went mainstream

S1: What Is Microsoft Scout?
- Microsoft Scout is a new AI agent from Microsoft
- Built on OpenClaw, the open-source AI agent framework
- Designed for enterprise use cases: workflow automation, data analysis, code assistance
- Part of Microsoft's Copilot super app strategy
- Not just a chatbot — it can take actions across Microsoft 365 and Windows
- Internal keyword: OpenClaw

S2: Why Microsoft Chose OpenClaw
- OpenClaw is an open-source project for building AI agents
- Microsoft could have built from scratch, but chose OpenClaw for speed and flexibility
- The OpenClaw community has already solved key problems: tool integration, memory management, security
- Microsoft gets a proven framework, OpenClaw gets enterprise validation
- This proves open-source AI agents are production-ready
- Internal keyword: OpenClaw security

S3: The OpenClaw Ecosystem Explained
- OpenClaw is not just one product — it is an ecosystem
- Hermes Agent, FoneClaw, and now Microsoft Scout are all built on OpenClaw
- Each targets different platforms: desktop, mobile, enterprise
- The core framework handles AI model integration, tool calling, and memory
- FoneClaw brings this to Android phones with voice control
- Internal keyword: local AI agent

S4: What This Means for FoneClaw
- Microsoft validating OpenClaw is a win for the entire ecosystem
- FoneClaw users benefit from improvements Microsoft contributes back
- Enterprise adoption drives more developer tools and integrations
- The OpenClaw standard becomes stronger with every major company that adopts it
- FoneClaw remains the mobile-first option in this growing ecosystem
- Internal keyword: AI agent adoption

S5: The Future of AI Agents
- Microsoft Scout represents the enterprise AI agent trend
- FoneClaw represents the personal AI agent trend
- Both are built on the same OpenClaw foundation
- The AI agent battlefield is expanding from phones to desktops to enterprise
- The winners will be platforms that balance power with privacy
- Internal keyword: AI terminal

S6: Frequently Asked Questions (5 questions)
Q: What is Microsoft Scout?
A: Microsoft Scout is a new AI agent built on the open-source OpenClaw framework. It was announced at Microsoft Build 2026 and is designed for enterprise workflow automation...

Q: How is Microsoft Scout different from Copilot?
A: Microsoft Scout is a standalone AI agent that can take actions across applications, while Copilot is a general AI assistant integrated into Microsoft 365 apps...

Q: Is FoneClaw related to Microsoft Scout?
A: Both FoneClaw and Microsoft Scout are built on the OpenClaw framework. They share the same core technology but target different platforms — FoneClaw for mobile, Scout for enterprise...

Q: Is OpenClaw secure for enterprise use?
A: Yes. OpenClaw has enterprise-grade security features including tool permission controls, memory isolation, and audit logging...

Q: Will FoneClaw get features from Microsoft Scout?
A: As part of the OpenClaw ecosystem, improvements to the core framework benefit all OpenClaw-based products, including FoneClaw...

INTERNAL LINK KEYWORDS (use naturally in text):
- Microsoft Build 2026 (S0)
- OpenClaw (S1)
- OpenClaw security (S2)
- local AI agent (S3)
- AI agent adoption (S4)
- AI terminal (S5)

Note: The build system will automatically create links when these keywords appear.
Do NOT manually add markdown links. Just use the keywords naturally.

OUTPUT: Python BATCH variable with string concatenation for long text. No triple quotes."""

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=*** = {
    "contents": [{"parts": [{"text": f"{SYSTEM_PROMPT}\n\n{prompt}"}]}],
    "generationConfig": {"temperature": 0.7, "maxOutputTokens": 16384}
}

print("Calling Gemini 3.5 Flash...")
response = requests.post(url, json=payload, timeout=180)
result = response.json()

if 'candidates' in result:
    content = result['candidates'][0]['content']['parts'][0]['text']
    save_path = '/home/administrator/clawfone-v2/batch_scout_raw.py'
    with open(save_path, 'w') as f:
        f.write(content)
    print(f"Article generated, saved to {save_path} ({len(content)} chars)")

    try:
        exec(compile(content, '<string>', 'exec'))
        print("Syntax check PASSED")
    except SyntaxError as e:
        print(f"Syntax error: {e}")
        print("--- RAW OUTPUT PREVIEW ---")
        print(content[:1000])
else:
    print(f"API error: {json.dumps(result, indent=2)[:500]}")
