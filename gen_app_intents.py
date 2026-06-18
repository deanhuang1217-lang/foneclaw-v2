import os, json, requests

# 读取API Key
api_key = None
with open('/home/administrator/video-workflow/.env') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY'):
            api_key = line.split('=', 1)[1].strip()
            break

print(f"API Key loaded: {api_key[:8]}...")

# System Prompt
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

# 构建prompt
prompt = """Write an SEO article for foneclaw.ai:

Slug: app-intents-apps-machine-callable-ai-agents
Title: App Intents: Why Apps Must Be Machine-Callable
Meta: Apple App Intents lets AI agents call app functions directly. Learn why machine-callable apps are the future of AI agent integration on Android.
Category: Industry & Trends
Read time: 8 min

SECTIONS (7 sections including FAQ):

S0: Introduction
- Hook: Apple announced App Intents at WWDC, but the real story is bigger than Siri
- Core thesis: The next phase of AI is not about smarter models - it is about apps becoming callable by AI agents
- Mention Bank of America $380 Apple price target based on this thesis
- FoneClaw has been doing this since day one on Android
- E-E-A-T: "Based on our analysis of Apple developer framework..."

S1: What Are Apple App Intents?
- Explain App Intents as a developer framework
- It lets developers expose app functionality to Siri, Spotlight, Shortcuts
- Apps become "machine-callable" - AI can invoke specific actions
- Example: ordering food, booking rides, sending messages via voice
- Mention iOS 27 Siri integration
- Internal keyword: iOS 27 Siri

S2: Why Every App Must Become Machine-Callable
- The shift from "download and tap" to "ask and execute"
- Traditional apps require manual interaction - tap buttons, fill forms
- AI agents need apps to expose APIs/functions that can be called programmatically
- Bank of America predicts $200-600B in agent-mediated commerce by 2030
- Without machine-callable apps, AI agents are limited to their own built-in functions
- Internal keyword: traditional apps

S3: How FoneClaw Already Makes Apps Machine-Callable
- FoneClaw does not wait for Apple - it already controls apps via voice on Android
- Through voice control, FoneClaw can open apps, navigate menus, fill forms, send messages
- No developer opt-in needed - FoneClaw uses accessibility APIs and screen understanding
- This is the "Android advantage" - open platform vs Apple walled garden
- Internal keywords: voice control, phone control

S4: App Intents vs FoneClaw Approach - A Comparison
- Apple approach: developer opt-in via App Intents framework
- FoneClaw approach: system-level control via accessibility + screen understanding
- Apple needs developers to cooperate; FoneClaw works with any app immediately
- Privacy angle: FoneClaw processes locally, no cloud dependency
- Internal keyword: local AI agent

S5: The Future - When Every App Speaks AI
- Predictions: by 2028, major apps will expose AI-callable interfaces
- App Intents could become the "App Store of AI" - developers compete for AI agent calls
- FoneClaw vision: a world where any Android app can be controlled by voice
- Personal context makes this powerful - your agent knows your habits
- Internal keyword: personal context AI agent

S6: Frequently Asked Questions (5 questions)
Q: What are Apple App Intents?
A: App Intents is Apple framework that lets developers expose app actions to Siri and AI systems...

Q: How does FoneClaw make apps machine-callable without App Intents?
A: FoneClaw uses Android accessibility APIs and screen understanding...

Q: Do developers need to update their apps for FoneClaw?
A: No. FoneClaw works with existing apps through system-level controls...

Q: Is machine-callable apps a privacy risk?
A: FoneClaw processes everything locally on your device...

Q: Will App Intents come to Android?
A: Google has similar initiatives with Android App Actions...

INTERNAL LINK KEYWORDS (use naturally in text):
- agentic ai (S0)
- iOS 27 Siri (S1)
- traditional apps (S2)
- voice control (S3)
- phone control (S3)
- local AI agent (S4)
- personal context AI agent (S5)

Note: The build system will automatically create links when these keywords appear.
Do NOT manually add markdown links. Just use the keywords naturally.

OUTPUT: Python BATCH variable with string concatenation for long text. No triple quotes."""

# 调用Gemini API
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={api_key}"
payload = {
    "contents": [{"parts": [{"text": f"{SYSTEM_PROMPT}\n\n{prompt}"}]}],
    "generationConfig": {"temperature": 0.7, "maxOutputTokens": 16384}
}

print("Calling Gemini 3.5 Flash...")
response = requests.post(url, json=payload, timeout=180)
result = response.json()

if 'candidates' in result:
    content = result['candidates'][0]['content']['parts'][0]['text']
    save_path = '/home/administrator/clawfone-v2/batch_app_intents_raw.py'
    with open(save_path, 'w') as f:
        f.write(content)
    print(f"Article generated, saved to {save_path} ({len(content)} chars)")

    # 语法检查
    try:
        exec(compile(content, '<string>', 'exec'))
        print("Syntax check PASSED")
    except SyntaxError as e:
        print(f"Syntax error: {e}")
        print("--- RAW OUTPUT PREVIEW ---")
        print(content[:1000])
else:
    print(f"API error: {json.dumps(result, indent=2)[:500]}")
