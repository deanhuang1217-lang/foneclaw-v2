#!/usr/bin/env python3
"""Generate SEO articles using Gemini 3.1 Pro Preview API directly."""
import json, os, sys, time
from urllib.request import Request, urlopen

GEMINI_KEY = open('/home/administrator/video-workflow/.env').read().split('GEMINI_API_KEY=')[1].split('\n')[0].strip()
API_URL = f"https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"

SYSTEM_PROMPT = open('/home/administrator/clawfone-v2/seo_writing_spec.md').read()

SYSTEM_PROMPT += """

## CRITICAL OUTPUT FORMAT
Output ONLY valid Python — no markdown, no ``` fences. Just the raw Python assignment.
Format: BATCH = [(article_id, title, description, category, read_time, [(subtitle, body), ...]), ...]

Each body must be 250-400 words of REAL, helpful content. Total per article 2000-3000 words.
Last section must be FAQ: subtitle='Frequently Asked Questions', body contains 4-5 Q&A pairs.
Use PAS framework for opening section. Include Bucket Brigades in body sections.
Write for HUMANS — helpful, specific, engaging. No AI cliches.
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
        "Authorization": f"Bearer {GEMINI_KEY}",
        "Content-Type": "application/json"
    })
    
    for attempt in range(3):
        try:
            resp = urlopen(req, timeout=300)
            result = json.loads(resp.read())
            content = result['choices'][0]['message']['content']
            return content
        except Exception as e:
            print(f"  Attempt {attempt+1} failed: {e}", file=sys.stderr)
            if attempt < 2:
                time.sleep(5)
    return None

def generate_batch(batch_name, articles_desc, output_file):
    print(f"\n{'='*60}")
    print(f"Generating {batch_name}...")
    print(f"{'='*60}")
    
    content = call_gemini(articles_desc)
    if not content:
        print(f"FAILED: {batch_name}")
        return False
    
    # Clean up: remove markdown fences if present
    content = content.strip()
    if content.startswith("```"):
        content = content.split("\n", 1)[1]
    if content.endswith("```"):
        content = content.rsplit("```", 1)[0]
    content = content.strip()
    
    # Ensure it starts with BATCH =
    if not content.startswith("BATCH"):
        # Try to find BATCH assignment
        idx = content.find("BATCH")
        if idx >= 0:
            content = content[idx:]
        else:
            print(f"ERROR: No BATCH assignment found in output")
            print(f"First 500 chars: {content[:500]}")
            return False
    
    # Write to file
    outpath = f"/home/administrator/clawfone-v2/{output_file}"
    with open(outpath, "w") as f:
        f.write(content + "\n")
    
    # Verify it parses
    try:
        exec(open(outpath).read())
        print(f"✅ {batch_name} saved and verified: {outpath}")
        return True
    except Exception as e:
        print(f"⚠️ {batch_name} saved but parse error: {e}")
        print(f"Check manually: {outpath}")
        return False

# ============================================================
# BATCH 1: How-To Guides (4 articles)
# ============================================================
generate_batch("Batch 1 (How-To)", """
Write these 4 articles for FoneClaw (AI voice-controlled Android phone agent, US market):

1. howto_voice_android — "How to Control Android with Voice Commands"
   Desc: Complete guide to setting up voice control on Android. Best commands for calls, messages, apps, and system settings.
   Cat: Setup, Read: 5 min
   Topics: Why voice control matters on Android, Install and setup, Voice calibration, Basic commands (call/text/alarm), Advanced multi-step commands, Pro tips and tricks

2. howto_texts_handsfree — "How to Send Texts Without Touching Your Phone"
   Desc: Step-by-step tutorial on sending iMessages, WhatsApp, and SMS using only your voice with FoneClaw AI agent.
   Cat: Tutorial, Read: 4 min
   Topics: Why hands-free texting matters (driving/cooking/safety), Basic voice texting, Multi-app support (iMessage/WhatsApp/SMS), Reading messages aloud, Voice reply workflow, Driving mode auto-activation

3. howto_multistep — "How to Automate Multi-Step Tasks with One Voice Command"
   Desc: Build powerful automations: book flights, manage smart home, order food all with a single sentence.
   Cat: Advanced, Read: 8 min
   Topics: What multi-step automation means, Booking travel by voice, Smart home routines, Food ordering automation, Complex workflow chaining, Success rates and reliability

4. howto_elderly_setup — "How to Set Up Voice Control for Elderly Parents"
   Desc: Configure FoneClaw for seniors: large text, family contacts, simplified commands, and remote family assistance.
   Cat: Guide, Read: 5 min
   Topics: The 50M+ US seniors challenge, Installing on their phone, Configuring family contacts, Elderly Mode setup, Medication reminders, Remote family assistance via Telegram

Each article: 2000-3000 words, 7-8 sections, PAS opening, Bucket Brigades, FAQ section.
Output as BATCH = [(id, title, desc, cat, read_time, [(sub, body), ...]), ...]
""", "articles_batch1.py")

# ============================================================
# BATCH 2: Use Cases (4 articles)
# ============================================================
generate_batch("Batch 2 (Use Cases A)", """
Write these 4 articles for FoneClaw (AI voice-controlled Android phone agent, US market):

1. howto_driving_voice — "How to Use Voice Commands While Driving Safely"
   Desc: Set up driving mode, connect car Bluetooth, and use hands-free navigation, calls, and messages legally and safely.
   Cat: Safety, Read: 4 min
   Topics: 3000+ deaths/year from distracted driving, Setting up driving mode, Essential driving commands, Car Bluetooth integration, Legal compliance in 48 states, Emergency while driving

2. howto_smart_home — "How to Control Smart Home Devices by Voice"
   Desc: Connect FoneClaw to your smart home: lights, thermostat, locks, cameras all controllable from your phone by voice.
   Cat: Smart Home, Read: 6 min
   Topics: The fragmented smart home problem, Supported devices (Hue/Nest/Ring/SmartThings), Basic voice commands, Creating routines, Voice vs app comparison, Privacy and security

3. uc_commuting — "Voice Control for Commuters: Stay Connected Safely"
   Desc: How millions of daily commuters use FoneClaw to stay connected while driving, biking, or on public transit hands-free.
   Cat: Commuting, Read: 7 min
   Topics: 27-minute average commute, Morning commute routine, Stay connected while driving, Public transit with earbuds, Safety compliance, Real commuter scenarios

4. uc_seniors — "AI Phone for Seniors: Bridging the Digital Divide"
   Desc: How FoneClaw helps 50M+ US seniors use smartphones independently with voice-first interaction and family remote help.
   Cat: Accessibility, Read: 9 min
   Topics: 50M+ seniors struggle with smartphones, Voice-first design philosophy, Family remote assistance, Medication and health reminders, Emergency features, 3-day adoption speed

Each article: 2000-3000 words, 7-8 sections, PAS opening, Bucket Brigades, FAQ section.
""", "articles_batch2.py")

# ============================================================
# BATCH 3: Lifestyle & Accessibility (4 articles)
# ============================================================
generate_batch("Batch 3 (Lifestyle)", """
Write these 4 articles for FoneClaw (AI voice-controlled Android phone agent, US market):

1. uc_cooking — "Hands-Free Cooking: Voice Commands in the Kitchen"
   Desc: Recipes, timers, music, calls, smart home control all while your hands are covered in flour.
   Cat: Lifestyle, Read: 5 min
   Topics: Both hands busy + flour on phone, Recipe step-by-step assistance, Multiple simultaneous timers, Smart kitchen appliance control, Entertainment while cooking, Hands-free shopping list

2. uc_emergency — "Emergency Voice Commands: When Seconds Count"
   Desc: How FoneClaw enables 911 calls, location sharing, and SOS messages when you physically cannot touch your phone.
   Cat: Safety, Read: 6 min
   Topics: When you can't touch your phone, Calling 911 with auto-speakerphone, GPS location sharing, SOS broadcast messages, Medical info relay to responders, Silent SOS via volume button

3. uc_productivity — "Productivity Automation for Busy Professionals"
   Desc: From scheduling to travel booking to delivery tracking save 30+ minutes daily with voice automation.
   Cat: Productivity, Read: 8 min
   Topics: 9 apps per task / 96 phone checks per day, Calendar management by voice, Email processing hands-free, Travel booking automation, Task management, 30+ minutes daily savings

4. uc_visual_impaired — "Voice-First Phone for Visually Impaired Users"
   Desc: Full phone control through voice for 7M visually impaired Americans, replacing complex accessibility gestures.
   Cat: Accessibility, Read: 7 min
   Topics: 7M visually impaired Americans, Complete voice control of all functions, Screen reader integration, Navigation assistance, Social connection without visual barriers, Emergency and safety

Each article: 2000-3000 words, 7-8 sections, PAS opening, Bucket Brigades, FAQ section.
""", "articles_batch3.py")

# ============================================================
# BATCH 4: Lifestyle & Comparisons (4 articles)
# ============================================================
generate_batch("Batch 4 (Comparisons A)", """
Write these 4 articles for FoneClaw (AI voice-controlled Android phone agent, US market):

1. uc_parenting — "Parenting Hands-Free: Voice Control for New Parents"
   Desc: Stay connected while keeping your hands free for your baby. Calls, messages, music, and smart home all by voice.
   Cat: Lifestyle, Read: 5 min
   Topics: Hands full with baby/bottles/diapers, Communication while holding baby, Baby care tools (feeding timer/white noise), Smart home for parents, Emergency preparedness, Self-care reminders

2. uc_fitness — "Voice-Controlled Fitness: Music, Tracking, Safety"
   Desc: Music control, pace tracking, emergency calls, and hands-free photos during workouts.
   Cat: Fitness, Read: 6 min
   Topics: Phone in armband, hands busy, Music control mid-workout, Fitness tracking hands-free, Safety features (911/location), Social fitness (text buddy/Strava), Cool-down and recovery

3. comp_vs_siri — "FoneClaw vs Siri: Which Voice Assistant is Better?"
   Desc: System-level AI agent vs traditional voice assistant. Features, capabilities, cross-app control, and real-world performance.
   Cat: Comparison, Read: 7 min
   Topics: Fundamental difference (assistant vs agent), System access (sandbox vs native), Multi-step task capability, Cross-app data passing, Remote control, Real-world verdict

4. comp_vs_google — "FoneClaw vs Google Assistant for Android"
   Desc: Agent-based approach vs cloud-first assistant. Cross-app tasks, privacy, on-device processing, and extensibility.
   Cat: Comparison, Read: 7 min
   Topics: Architecture (cloud-first vs device-first), Third-party app integration, Ad-hoc multi-step automation, Privacy model (cloud vs local), Self-evolution learning, When to use which

Each article: 2000-3000 words, 7-8 sections, PAS opening, Bucket Brigades, FAQ section.
""", "articles_batch4.py")

# ============================================================
# BATCH 5: Comparisons & Industry (3 articles)
# ============================================================
generate_batch("Batch 5 (Comparisons B)", """
Write these 3 articles for FoneClaw (AI voice-controlled Android phone agent, US market):

1. comp_vs_alexa — "FoneClaw vs Alexa on Mobile: Voice Control Showdown"
   Desc: Two approaches to mobile voice control. Which handles real-world driving, cooking, and accessibility scenarios better?
   Cat: Comparison, Read: 6 min
   Topics: Mobile-first vs speaker-first design, Phone control depth, Offline capability, Native app integrations, Driving scenario comparison, Clear verdict

2. comp_best_apps — "Best Voice Control Apps for Android in 2026"
   Desc: Comprehensive roundup of top voice control solutions. Features, pricing, privacy, and recommendations.
   Cat: Roundup, Read: 8 min
   Topics: Voice control landscape in 2026, #1 FoneClaw (system-level agent), #2 Google Assistant (ecosystem), #3 Samsung Bixby (Samsung-only), #4 Amazon Alexa (smart home), How to choose

3. comp_ai_replacing — "How AI Phone Agents Are Replacing Traditional Assistants"
   Desc: The shift from Siri/Alexa to autonomous AI agents. What it means for users and developers.
   Cat: Industry, Read: 7 min
   Topics: Three generations of phone AI, Why single-command assistants are not enough, The agent advantage (intent/decompose/learn), What this means for users, What this means for developers, The road ahead (2028 predictions)

Each article: 2000-3000 words, 7-8 sections, PAS opening, Bucket Brigades, FAQ section.
""", "articles_batch5.py")

print("\n" + "="*60)
print("ALL BATCHES COMPLETE")
print("="*60)
