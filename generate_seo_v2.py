#!/usr/bin/env python3
"""Generate SEO articles with keyword targeting using Gemini 3.1 Pro Preview."""
import json, os, sys, time
from urllib.request import Request, urlopen

GEMINI_KEY = open('/home/administrator/video-workflow/.env').read().split('GEMINI_API_KEY=')[1].split('\n')[0].strip()
API_URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"

SYSTEM_PROMPT = open('/home/administrator/clawfone-v2/seo_writing_spec.md').read()

SYSTEM_PROMPT += """

## CRITICAL OUTPUT FORMAT
Output ONLY valid Python — no markdown fences. Just the raw Python assignment.
Format: BATCH = [(article_id, title, description, category, read_time, [(subtitle, body), ...]), ...]

REMEMBER:
- Primary keyword MUST appear in: title(H1), first 100 words, at least 1 H2, FAQ, final paragraph
- Target keyword density: 1.0-1.8% of total word count
- Secondary keywords: each in a different H2 subtitle
- Every body paragraph should naturally reference at least one keyword
"""

def call_gemini(prompt):
    data = json.dumps({
        "model": "gemini-3.1-pro-preview",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 65536,
        "temperature": 0.7
    }).encode()
    req = Request(API_URL, data=data, headers={
        "Authorization": f"Bearer {GEMINI_KEY}", "Content-Type": "application/json"
    })
    for attempt in range(3):
        try:
            resp = urlopen(req, timeout=300)
            result = json.loads(resp.read())
            return result['choices'][0]['message']['content']
        except Exception as e:
            print(f"  Attempt {attempt+1} failed: {e}", file=sys.stderr)
            if attempt < 2: time.sleep(10)
    return None

def generate_batch(batch_name, prompt, output_file):
    print(f"\n{'='*60}\nGenerating {batch_name}...\n{'='*60}")
    content = call_gemini(prompt)
    if not content:
        print(f"FAILED: {batch_name}"); return False
    content = content.strip()
    if content.startswith("```"):
        content = content.split("\n", 1)[1]
    if content.endswith("```"):
        content = content.rsplit("```", 1)[0]
    content = content.strip()
    if not content.startswith("BATCH"):
        idx = content.find("BATCH")
        if idx >= 0: content = content[idx:]
        else: print(f"ERROR: No BATCH found"); return False
    outpath = f"/home/administrator/clawfone-v2/{output_file}"
    with open(outpath, "w") as f:
        f.write(content + "\n")
    try:
        exec(open(outpath).read())
        print(f"✅ {batch_name} saved and verified")
        return True
    except Exception as e:
        print(f"⚠️ Parse error: {e}")
        return False

# ============================================================
# BATCH 1: How-To Guides (4 articles)
# ============================================================
generate_batch("Batch 1", """
Write 4 SEO-optimized articles for FoneClaw (AI voice-controlled Android phone agent, US market).

CRITICAL KEYWORD RULES:
- Primary keyword MUST appear in the title (H1)
- Primary keyword MUST appear in the first 100 words of each article
- Primary keyword MUST appear in at least 1 H2 subtitle
- Primary keyword MUST appear in the FAQ section
- Primary keyword MUST appear in the final paragraph
- Target density: 1.0-1.8% (for 2000 words = 20-36 times)
- Secondary keywords: each should appear in a different H2 subtitle
- Use keyword variations naturally (e.g., "voice control" / "voice commands" / "voice-controlled")

---

ARTICLE 1: howto_voice_android
Title: "How to Control Android with Voice Commands"
Primary keyword: "voice control Android" (use ~20 times in various forms: "voice control on Android", "Android voice control", "voice-controlled Android", "control Android by voice")
Secondary keywords: ["voice commands Android", "hands-free phone control", "AI phone agent", "Android automation voice"]
Category: Setup, Read: 5 min
Description: Complete guide to setting up voice control on Android. Best commands for calls, messages, apps, and system settings.
Topics: Why voice control matters for Android users, Installation and setup, Voice calibration, Basic voice commands, Advanced multi-step commands, Pro tips

---

ARTICLE 2: howto_texts_handsfree
Title: "How to Send Texts Without Touching Your Phone"
Primary keyword: "send texts without touching phone" (use ~20 times: "text without touching", "hands-free texting", "text by voice", "touch-free messaging")
Secondary keywords: ["hands-free texting driving", "voice text messages", "iMessage voice control", "text while driving safely"]
Category: Tutorial, Read: 4 min
Topics: Why hands-free texting matters, Basic voice texting setup, Multi-app support, Reading messages aloud, Voice reply workflow, Driving mode

---

ARTICLE 3: howto_multistep
Title: "How to Automate Multi-Step Tasks with One Voice Command"
Primary keyword: "multi-step voice commands" (use ~20 times: "multi-step automation", "one voice command multiple tasks", "chain voice commands", "automate tasks voice")
Secondary keywords: ["cross-app automation", "voice workflow automation", "one sentence tasks", "multi-app voice control"]
Category: Advanced, Read: 8 min
Topics: What multi-step automation means, Booking travel by voice, Smart home routines, Food ordering, Complex workflow chaining, Success rates

---

ARTICLE 4: howto_elderly_setup
Title: "How to Set Up Voice Control for Elderly Parents"
Primary keyword: "voice control elderly parents" (use ~20 times: "elderly phone setup", "senior voice control", "phone for elderly parents", "voice-controlled phone seniors")
Secondary keywords: ["senior smartphone help", "elderly phone assistance", "family remote phone help", "easy phone for seniors"]
Category: Guide, Read: 5 min
Topics: The 50M+ seniors challenge, Installing on their phone, Family contacts setup, Elderly Mode, Medication reminders, Remote family assistance

Each article: 1500-2500 words, 7-8 sections, PAS opening, diverse Bucket Brigades (no repeats), FAQ section.
Output as BATCH = [(id, title, desc, cat, read_time, [(sub, body), ...]), ...]
""", "articles_batch1.py")

# ============================================================
# BATCH 2: Use Cases A (4 articles)
# ============================================================
generate_batch("Batch 2", """
Write 4 SEO-optimized articles for FoneClaw (AI voice-controlled Android phone agent, US market).

CRITICAL KEYWORD RULES:
- Primary keyword MUST appear in: title, first 100 words, at least 1 H2, FAQ, final paragraph
- Target density: 1.0-1.8%
- Secondary keywords each in different H2 subtitles
- Use natural variations

---

ARTICLE 1: howto_driving_voice
Title: "How to Use Voice Commands While Driving Safely"
Primary keyword: "voice commands while driving" (use ~20 times: "driving voice control", "hands-free driving", "voice commands driving", "driving mode voice")
Secondary keywords: ["hands-free driving safety", "car Bluetooth voice", "driving text voice", "legal hands-free phone"]
Category: Safety, Read: 4 min

ARTICLE 2: howto_smart_home
Title: "How to Control Smart Home Devices by Voice"
Primary keyword: "control smart home voice" (use ~20 times: "smart home voice control", "voice control devices", "smart home by voice", "voice-controlled home")
Secondary keywords: ["voice smart home automation", "smart home voice assistant", "control lights voice", "smart thermostat voice"]
Category: Smart Home, Read: 6 min

ARTICLE 3: uc_commuting
Title: "Voice Control for Commuters: Stay Connected Safely"
Primary keyword: "voice control commuters" (use ~20 times: "commute hands-free", "voice control commute", "commuter voice assistant", "hands-free commute")
Secondary keywords: ["morning commute routine voice", "driving commute voice", "transit voice control", "productive commute"]
Category: Commuting, Read: 7 min

ARTICLE 4: uc_seniors
Title: "AI Phone for Seniors: Bridging the Digital Divide"
Primary keyword: "AI phone seniors" (use ~20 times: "senior smartphone AI", "AI phone elderly", "smartphone for seniors", "senior-friendly phone AI")
Secondary keywords: ["senior digital divide", "elderly phone help", "voice-first seniors", "senior phone independence"]
Category: Accessibility, Read: 9 min

Each article: 1500-2500 words, 7-8 sections, PAS opening, diverse Bucket Brigades, FAQ section.
""", "articles_batch2.py")

# ============================================================
# BATCH 3: Lifestyle & Accessibility (4 articles)
# ============================================================
generate_batch("Batch 3", """
Write 4 SEO-optimized articles for FoneClaw (AI voice-controlled Android phone agent, US market).

CRITICAL KEYWORD RULES:
- Primary keyword MUST appear in: title, first 100 words, at least 1 H2, FAQ, final paragraph
- Target density: 1.0-1.8%
- Secondary keywords each in different H2 subtitles

---

ARTICLE 1: uc_cooking
Title: "Hands-Free Cooking: Voice Commands in the Kitchen"
Primary keyword: "hands-free cooking voice" (use ~20 times: "cooking voice commands", "kitchen hands-free", "voice control cooking", "cook without touching phone")
Secondary keywords: ["recipe voice control", "kitchen timer voice", "cooking music voice", "smart kitchen voice"]
Category: Lifestyle, Read: 5 min

ARTICLE 2: uc_emergency
Title: "Emergency Voice Commands: When Seconds Count"
Primary keyword: "emergency voice commands" (use ~20 times: "voice emergency call", "emergency hands-free", "call 911 voice", "SOS voice command")
Secondary keywords: ["call 911 hands-free", "emergency location share", "SOS message voice", "medical emergency phone"]
Category: Safety, Read: 6 min

ARTICLE 3: uc_productivity
Title: "Productivity Automation for Busy Professionals"
Primary keyword: "productivity voice automation" (use ~20 times: "voice productivity", "hands-free productivity", "voice automate tasks", "professional voice control")
Secondary keywords: ["voice calendar management", "email voice control", "voice task management", "save time voice automation"]
Category: Productivity, Read: 8 min

ARTICLE 4: uc_visual_impaired
Title: "Voice-First Phone for Visually Impaired Users"
Primary keyword: "voice phone visually impaired" (use ~20 times: "visually impaired phone", "blind voice control", "accessible phone voice", "vision disability phone")
Secondary keywords: ["accessibility voice control", "screen reader voice", "blind phone navigation", "accessible smartphone voice"]
Category: Accessibility, Read: 7 min

Each article: 1500-2500 words, 7-8 sections, PAS opening, diverse Bucket Brigades, FAQ section.
""", "articles_batch3.py")

# ============================================================
# BATCH 4: Lifestyle & Comparisons (4 articles)
# ============================================================
generate_batch("Batch 4", """
Write 4 SEO-optimized articles for FoneClaw (AI voice-controlled Android phone agent, US market).

CRITICAL KEYWORD RULES:
- Primary keyword MUST appear in: title, first 100 words, at least 1 H2, FAQ, final paragraph
- Target density: 1.0-1.8%
- Secondary keywords each in different H2 subtitles

---

ARTICLE 1: uc_parenting
Title: "Parenting Hands-Free: Voice Control for New Parents"
Primary keyword: "voice control new parents" (use ~20 times: "parenting hands-free", "new parent phone", "baby hands-free phone", "parent voice control")
Secondary keywords: ["new parent phone help", "baby care voice", "hands-free parent app", "nursery voice control"]
Category: Lifestyle, Read: 5 min

ARTICLE 2: uc_fitness
Title: "Voice-Controlled Fitness: Music, Tracking, Safety"
Primary keyword: "voice control fitness" (use ~20 times: "workout voice commands", "fitness voice control", "exercise hands-free", "gym voice assistant")
Secondary keywords: ["running music voice", "workout tracking voice", "fitness safety voice", "exercise phone hands-free"]
Category: Fitness, Read: 6 min

ARTICLE 3: comp_vs_siri
Title: "FoneClaw vs Siri: Which Voice Assistant is Better?"
Primary keyword: "FoneClaw vs Siri" (use ~20 times: "FoneClaw Siri comparison", "Siri alternative", "better than Siri", "Siri vs AI agent")
Secondary keywords: ["voice assistant comparison", "Siri limitations", "AI agent vs assistant", "Siri alternative Android"]
Category: Comparison, Read: 7 min

ARTICLE 4: comp_vs_google
Title: "FoneClaw vs Google Assistant for Android"
Primary keyword: "FoneClaw vs Google Assistant" (use ~20 times: "Google Assistant alternative", "FoneClaw Google comparison", "better than Google Assistant", "Google Assistant vs AI agent")
Secondary keywords: ["Android voice comparison", "Google Assistant limitations", "agent vs assistant Android", "Google Assistant replacement"]
Category: Comparison, Read: 7 min

Each article: 1500-2500 words, 7-8 sections, PAS opening, diverse Bucket Brigades, FAQ section.
""", "articles_batch4.py")

# ============================================================
# BATCH 5: Comparisons & Industry (3 articles)
# ============================================================
generate_batch("Batch 5", """
Write 3 SEO-optimized articles for FoneClaw (AI voice-controlled Android phone agent, US market).

CRITICAL KEYWORD RULES:
- Primary keyword MUST appear in: title, first 100 words, at least 1 H2, FAQ, final paragraph
- Target density: 1.0-1.8%
- Secondary keywords each in different H2 subtitles

---

ARTICLE 1: comp_vs_alexa
Title: "FoneClaw vs Alexa on Mobile: Voice Control Showdown"
Primary keyword: "FoneClaw vs Alexa" (use ~20 times: "Alexa mobile alternative", "FoneClaw Alexa comparison", "Alexa vs AI agent phone", "better than Alexa mobile")
Secondary keywords: ["mobile voice control comparison", "Alexa phone limitations", "voice control showdown", "Alexa alternative Android"]
Category: Comparison, Read: 6 min

ARTICLE 2: comp_best_apps
Title: "Best Voice Control Apps for Android in 2026"
Primary keyword: "best voice control apps Android" (use ~20 times: "top voice apps Android", "voice control app comparison", "Android voice apps 2026", "best voice assistant Android")
Secondary keywords: ["voice control app review", "Android voice control ranking", "voice app comparison 2026", "top voice assistants Android"]
Category: Roundup, Read: 8 min

ARTICLE 3: comp_ai_replacing
Title: "How AI Phone Agents Are Replacing Traditional Assistants"
Primary keyword: "AI phone agents replacing assistants" (use ~20 times: "AI replacing voice assistants", "phone agent evolution", "autonomous phone AI", "AI agent vs traditional assistant")
Secondary keywords: ["future of voice control", "AI agent technology", "voice assistant evolution", "autonomous phone control"]
Category: Industry, Read: 7 min

Each article: 1500-2500 words, 7-8 sections, PAS opening, diverse Bucket Brigades, FAQ section.
""", "articles_batch5.py")

print("\n" + "="*60)
print("ALL BATCHES COMPLETE")
print("="*60)
