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

Slug: apple-intelligence-pro-subscription-what-to-expect
Title: Apple Intelligence Pro: Is $15/Month Worth It
Meta: Bank of America predicts 50-75 million Apple Intelligence Pro subscribers at $15/month. We analyze the value and compare with free alternatives like FoneClaw.
Category: Industry & Trends
Read time: 8 min

SECTIONS (7 sections including FAQ):

S0: Introduction
- Hook: Bank of America predicts Apple will launch a $15/month AI subscription called Apple Intelligence Pro
- 50-75 million subscribers generating $9-14 billion in annual revenue
- Core question: Is a monthly AI subscription worth it when free alternatives exist?
- Mention FoneClaw as a free local alternative
- E-E-A-T: "Based on our analysis of Bank of America research report..."

S1: What Is Apple Intelligence Pro?
- Apple planned subscription tier for AI features
- Built on top of Apple Intelligence (on-device + cloud processing)
- Features: advanced Siri, priority access to new AI models, enhanced cloud processing
- Part of Apple strategy to monetize AI beyond hardware sales
- Mention iOS 27 Siri integration
- Internal keyword: iOS 27 Siri

S2: The $15/Month Breakdown
- $15/month = $180/year per user
- Bank of America base case: 50-75 million subscribers = $9-14 billion revenue
- Bull case: 100-125 million subscribers = $18-23 billion
- This is pure recurring revenue for Apple
- Compare to other AI subscriptions: ChatGPT Plus ($20), Claude Pro ($20)
- Internal keyword: AI agent spending

S3: What You Get for $15/Month
- Priority access to latest AI models
- Enhanced cloud processing for complex tasks
- Advanced Siri capabilities (agentic features)
- More cloud storage for AI data
- But: still limited to Apple ecosystem
- Comparison with FoneClaw vs Apple Intelligence features
- Internal keyword: FoneClaw vs Apple Intelligence

S4: Why Free Alternatives Exist
- FoneClaw provides AI agent capabilities at zero cost
- Local processing means no subscription fees
- No token costs because everything runs on your device
- Open Android platform vs closed Apple ecosystem
- You get voice control, app automation, personal context without paying
- Internal keyword: local AI agent

S5: Is It Worth the Price?
- For Apple-only users: potentially worth it if you rely heavily on Siri
- For Android users: FoneClaw offers similar capabilities for free
- The real cost is not just money — its data privacy
- Local AI agents keep your data on device
- Cloud subscriptions send your data to remote servers
- Internal keyword: local AI agent trust

S6: Frequently Asked Questions (5 questions)
Q: What is Apple Intelligence Pro?
A: Apple Intelligence Pro is a planned subscription service that gives users access to advanced AI features on their iPhone...

Q: How much does Apple Intelligence Pro cost?
A: Based on Bank of America analysis, the subscription is expected to cost $15 per month...

Q: Is there a free alternative to Apple Intelligence Pro?
A: Yes. FoneClaw provides AI agent capabilities on Android phones at no cost...

Q: What is the difference between Apple Intelligence and Apple Intelligence Pro?
A: Apple Intelligence is the free tier with basic AI features. Apple Intelligence Pro adds advanced cloud processing...

Q: Will Apple Intelligence Pro be worth the monthly fee?
A: It depends on your usage. If you heavily rely on Siri and Apple ecosystem, the advanced features may justify the cost...

INTERNAL LINK KEYWORDS (use naturally in text):
- AI agent token cost (S0)
- iOS 27 Siri (S1)
- AI agent spending (S2)
- FoneClaw vs Apple Intelligence (S3)
- local AI agent (S4)
- local AI agent trust (S5)
- personal context AI agent (S5)

Note: The build system will automatically create links when these keywords appear.
Do NOT manually add markdown links. Just use the keywords naturally.

OUTPUT: Python BATCH variable with string concatenation for long text. No triple quotes."""

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
    save_path = '/home/administrator/clawfone-v2/batch_ai_pro_raw.py'
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
