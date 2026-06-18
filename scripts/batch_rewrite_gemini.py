#!/usr/bin/env python3
"""Batch rewrite articles using Gemini 3.1 Pro."""
import json
import os
import subprocess
import sys

os.chdir('/home/administrator/clawfone-v2')

# Get Gemini API key
env_file = '/home/administrator/video-workflow/.env'
api_key = None
with open(env_file) as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY='):
            api_key = line.strip().split('=', 1)[1]
            break

if not api_key:
    print("Error: GEMINI_API_KEY not found")
    sys.exit(1)

# Article definitions: (batch, slug, title, meta, category, topic_description)
articles = [
    ("batch9", "why-local-ai-agents-never-go-down",
     "Why Local AI Agents Like FoneClaw Never Go Down",
     "Local AI agents work offline and never crash. See why FoneClaw local processing beats cloud-dependent assistants.",
     "Comparison",
     "Compare local vs cloud AI agents. Local agents like FoneClaw process on-device, no internet needed, no server crashes. Cloud agents depend on servers."),

    ("batch9", "automate-instagram-with-voice",
     "How to Automate Instagram with Voice Commands",
     "Control Instagram hands-free with voice commands. Post, scroll, and message using FoneClaw voice control on Android.",
     "Use Case",
     "Voice control for Instagram: post photos, scroll feed, send DMs, like posts - all hands-free using FoneClaw on Android."),

    ("batch9", "android-vs-ios-26-5-voice-control",
     "Android vs iOS 26.5 Voice Control: Which Is Better?",
     "Compare Android voice control with iOS 26.5 features. See which platform handles hands-free phone tasks better.",
     "Comparison",
     "Compare Android (with FoneClaw) vs iOS 26.5 Siri voice control. Android wins on flexibility, iOS on polish."),

    ("batch9", "control-samsung-smart-tv-voice",
     "How to Control Samsung Smart TV with Voice Commands",
     "Control your Samsung Smart TV with voice commands using FoneClaw. Change channels, adjust volume, search content hands-free.",
     "Use Case",
     "Using FoneClaw to control Samsung Smart TV by voice: change channels, volume, input source, search apps."),

    ("batch9", "voice-control-wearables",
     "Voice Control for Wearables Beyond Your Phone",
     "Extend voice control to smartwatches and wearables. FoneClaw brings AI agent capabilities to wrist-mounted devices.",
     "Use Case",
     "Voice control on wearables: smartwatches, fitness bands. FoneClaw extends phone AI to wrist devices."),

    ("batch9", "small-businesses-use-ai-agents",
     "How Small Businesses Use AI Agents for Productivity",
     "Small businesses use AI agents to automate tasks. See how FoneClaw helps restaurants, shops, and services save time.",
     "Use Case",
     "Small business AI agent use cases: restaurants, retail, services. FoneClaw automates orders, inventory, customer messages."),

    ("batch9", "cerebras-future-ai-hardware",
     "Cerebras and the Future of AI Hardware",
     "Cerebras builds specialized AI chips for fast inference. See how hardware advances enable better on-device AI agents.",
     "Comparison",
     "Cerebras AI chip technology, on-device inference, hardware for AI agents. Enables faster local AI processing."),

    ("batch9", "trump-phone-mobile-ai",
     "Trump Phone and Mobile AI: What to Expect",
     "Trump Phone enters the AI phone race. Compare with FoneClaw approach to mobile AI and voice control.",
     "Comparison",
     "Trump Phone announcement, mobile AI trends, comparison with FoneClaw independent AI agent approach."),

    ("batch10", "top-10-ai-agent-models-2026",
     "Top 10 AI Agent Models 2026: Agentic Index Rankings",
     "Compare the top 10 AI agent models ranked by Agentic Index score. GPT-5.5, Claude Opus 4.7, Xiaomi MiMo-V2.5-Pro.",
     "Comparison",
     "Agentic Index top 10: GPT-5.5(74.1), Claude Opus 4.7(71.3), Xiaomi MiMo-V2.5-Pro(67.4), Grok 4.3, Qwen3.6, etc."),

    ("batch10b", "ai-phone-war-2026",
     "AI Phone War 2026: OpenAI vs ByteDance vs Google",
     "The AI phone war is here. OpenAI, ByteDance, Google, Samsung, and Xiaomi are racing to build agent-first smartphones.",
     "Comparison",
     "AI phone competition: OpenAI phone with Jony Ive, ByteDance Doubao phone, Google Pixel Gemini, Samsung Galaxy AI, Xiaomi MiMo."),

    ("batch6", "comp_vs_gemini",
     "Gemini vs FoneClaw: Android Voice Control",
     "Compare Google Gemini with FoneClaw for Android voice control. See which handles hands-free phone tasks better.",
     "Comparison",
     "Google Gemini vs FoneClaw for voice-controlled Android automation. Gemini is Google AI, FoneClaw is independent."),

    ("batch6", "comp_vs_miclaw",
     "MiClaw vs FoneClaw: Independent AI Agent vs Xiaomi",
     "Compare FoneClaw, an independent AI agent, with Xiaomi MiClaw for voice control on Android.",
     "Comparison",
     "Xiaomi MiClaw vs FoneClaw. MiClaw is Xiaomi's product, FoneClaw is independent. Both do voice control on Android."),

    ("batch7", "ai-agent-vs-traditional-apps",
     "AI Voice Agent vs Traditional Apps: Why Agents Win",
     "AI voice agents replace traditional apps. See why speaking commands beats tapping icons on your phone.",
     "Comparison",
     "AI agent vs traditional app approach. Voice control vs tap-based UI. FoneClaw as agent-first alternative."),

    ("batch7", "tasker-alternative-voice-automation",
     "Tasker Alternative: Voice Automation with FoneClaw",
     "Looking for a Tasker alternative? FoneClaw offers voice-controlled automation without complex scripting.",
     "Comparison",
     "Tasker automation vs FoneClaw voice control. Tasker needs scripting, FoneClaw uses natural language."),

    ("batch7", "voice-assistant-privacy-security",
     "Voice Assistant Privacy and Security: What You Need to Know",
     "Voice assistants collect data. See how FoneClaw local processing keeps your voice commands private and secure.",
     "Use Case",
     "Voice assistant privacy concerns, local vs cloud processing, FoneClaw on-device security."),

    ("batch7", "voice-control-dirty-hands",
     "Hands-Free Phone When Your Hands Are Dirty",
     "Cooking, gardening, or working? Use voice commands to control your phone without touching the screen.",
     "Use Case",
     "Hands-free phone use cases: cooking, cleaning, gardening, car repair. FoneClaw voice control for dirty hands."),

    ("batch8", "top-10-ai-agents-2026",
     "Top 10 AI Agents in 2026: Which One Works?",
     "Compare the top 10 AI agents available in 2026. See which ones actually work for daily phone automation.",
     "Comparison",
     "Top AI agents 2026: FoneClaw, Siri, Google Assistant, Alexa, Bixby, etc. Which handles real tasks best."),

    ("batch8", "hermes-agent-vs-openclaw-vs-foneclaw",
     "Hermes Agent vs OpenClaw vs FoneClaw: AI Agent Comparison",
     "Compare three AI agent platforms: Hermes Agent, OpenClaw, and FoneClaw. Features, pricing, and capabilities.",
     "Comparison",
     "Hermes Agent vs OpenClaw vs FoneClaw comparison. Three independent AI agent platforms with different approaches."),
]

# System prompt for all articles
system_prompt = """You are an expert SEO article writer for foneclaw.ai, an independent AI agent platform for Android voice control.

CRITICAL RULES:
1. FoneClaw is an INDEPENDENT startup, NOT owned by Xiaomi
2. MiMo is Xiaomi's model - FoneClaw supports it but does NOT own it
3. Always say "Xiaomi MiMo-V2.5-Pro" when mentioning MiMo
4. Never imply FoneClaw belongs to Xiaomi

STYLE:
- Write in English
- Use second person "you"
- Short sentences, conversational tone
- Avoid AI-sounding phrases (no "furthermore", "robust", "seamlessly", "cutting-edge")
- Quality over word count (800-1500 words recommended)
- Include E-E-A-T reference (e.g., "Based on our testing...")

OUTPUT FORMAT (Python):
BATCH = [
    (
        "slug-here",
        "Title Here",
        "Meta description 120-160 characters.",
        "Category",
        "X min",
        [
            ("Section Title 1", "Body text..."),
            ("Section Title 2", "Body text..."),
            # 5-7 sections
            ("Frequently Asked Questions", "Q: Question?\\nA: Answer.\\n\\nQ: Question?\\nA: Answer."),
        ]
    ),
]

INTERNAL LINK KEYWORDS (embed naturally in text):
- "AI phone" -> ai-phone-war-2026
- "Agentic Index" -> top-10-ai-agent-models-2026
- "AI agents" -> top-10-ai-agents-2026
- "voice control" -> voice-control-android
- "senior" -> ai-phone-seniors
- "Google Assistant" -> foneclaw-vs-google-assistant
- "Xiaomi" -> miclaw-vs-foneclaw
"""

def call_gemini(prompt, max_tokens=8192):
    """Call Gemini API and return the response."""
    import urllib.request

    url = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gemini-3.1-pro-preview",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read())
            return result['choices'][0]['message']['content']
    except Exception as e:
        return f"ERROR: {e}"

# Process articles
print(f"开始用Gemini重写{len(articles)}篇文章...")
print("=" * 60)

results = {}
for i, (batch, slug, title, meta, category, topic) in enumerate(articles, 1):
    print(f"\n[{i}/{len(articles)}] 生成: {slug}")

    prompt = f"""Write an SEO article for foneclaw.ai:

Slug: {slug}
Title: {title}
Meta: {meta}
Category: {category}
Topic: {topic}

Requirements:
- 5-7 sections including FAQ
- Embed internal link keywords naturally
- FoneClaw is independent (not Xiaomi)
- MiMo is Xiaomi's model (not FoneClaw's)
- Quality over word count
- Conversational tone, no AI phrases

Output the complete BATCH Python code."""

    response = call_gemini(prompt)

    if response.startswith("ERROR"):
        print(f"  ❌ 失败: {response}")
        continue

    # Extract BATCH code from response
    if "BATCH = [" in response:
        start = response.index("BATCH = [")
        # Find the matching closing bracket
        bracket_count = 0
        end = start
        for j in range(start, len(response)):
            if response[j] == '[':
                bracket_count += 1
            elif response[j] == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    end = j + 1
                    break
        batch_code = response[start:end]
    else:
        batch_code = response

    results[batch] = results.get(batch, []) + [(batch_code, slug)]
    print(f"  ✅ 完成")

# Save results
print("\n" + "=" * 60)
print("保存结果...")

for batch, entries in results.items():
    output_file = f"articles_{batch}_gemini.py"
    with open(output_file, 'w') as f:
        f.write(f"# {batch} - Gemini version\n")
        f.write(f"# Generated: 2026-05-18\n\n")
        for code, slug in entries:
            f.write(f"# {slug}\n")
            f.write(code)
            f.write("\n\n")
    print(f"  ✅ {output_file}")

print("\n完成！")
