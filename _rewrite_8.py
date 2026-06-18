from urllib.request import Request, urlopen
import json, time, sys

GEMINI_KEY = open('/home/administrator/video-workflow/.env').read().split('GEMINI_API_KEY=')[1].split('\n')[0].strip()
API_URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
SPEC = open('/home/administrator/clawfone-v2/seo_writing_spec.md').read()

def call_gemini(system, prompt):
    data = json.dumps({"model": "gemini-3.1-pro-preview","messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],"max_tokens": 65536, "temperature": 0.7}).encode()
    req = Request(API_URL, data=data, headers={"Authorization": f"Bearer {GEMINI_KEY}", "Content-Type": "application/json"})
    for attempt in range(3):
        try:
            resp = urlopen(req, timeout=300)
            return json.loads(resp.read())['choices'][0]['message']['content']
        except Exception as e:
            print(f"  Retry {attempt+1}: {e}", flush=True)
            if attempt < 2: time.sleep(10)
    return None

system = SPEC + """

## CRITICAL OUTPUT FORMAT
Output ONLY valid Python assignment: BATCH = [(id, title, desc, cat, rt, [(sub, body), ...])]

## KEYWORD RULES (NON-NEGOTIABLE):
1. The title MUST EXACTLY match what is specified below
2. Primary keyword MUST appear in: first 100 words, at least 1 H2, FAQ, final paragraph
3. Target density: 1.0-1.8%
4. Secondary keywords each in different H2 subtitle
5. NO AI taste words
6. 7-8 sections, last section is FAQ with 4-5 Q&A pairs
"""

ARTICLES = [
    ('howto_texts_handsfree', 'How to Send Texts Without Touching Your Phone', 'send texts without touching phone', ['hands-free texting driving', 'voice text messages', 'imessage voice control', 'text while driving safely'], 'Step-by-step tutorial on sending iMessages, WhatsApp, and SMS using only your voice with FoneClaw AI agent.', 'Tutorial', '4 min', 'The dangers of manual texting while driving/cooking, Basic voice texting setup, Multi-app support, Reading messages aloud, Voice reply workflow, Driving mode auto-activation'),
    ('howto_multistep', 'How to Automate Multi-Step Tasks with One Voice Command', 'multi-step voice commands', ['cross-app automation', 'voice workflow automation', 'one sentence tasks', 'multi-app voice control'], 'Build powerful automations: book flights, manage smart home, order food all with a single sentence.', 'Advanced', '8 min', 'What multi-step automation means, Booking travel by voice, Smart home routines, Food ordering, Complex workflow chaining, Success rates'),
    ('uc_commuting', 'Voice Control for Commuters: Stay Connected Safely', 'voice control commuters', ['morning commute routine voice', 'driving commute voice', 'transit voice control', 'productive commute'], 'How millions of daily commuters use FoneClaw to stay connected while driving, biking, or on public transit hands-free.', 'Commuting', '7 min', '27-minute average commute, Morning commute routine, Stay connected while driving, Public transit with earbuds, Safety compliance, Real commuter scenarios'),
    ('uc_seniors', 'AI Phone for Seniors: Bridging the Digital Divide', 'ai phone seniors', ['senior digital divide', 'elderly phone help', 'voice-first seniors', 'senior phone independence'], 'How FoneClaw helps 50M+ US seniors use smartphones independently with voice-first interaction and family remote help.', 'Accessibility', '9 min', '50M+ seniors struggle, Voice-first design, Family remote assistance, Medication reminders, Emergency features, 3-day adoption speed'),
    ('uc_parenting', 'Parenting Hands-Free: Voice Control for New Parents', 'voice control new parents', ['new parent phone help', 'baby care voice', 'hands-free parent app', 'nursery voice control'], 'Stay connected while keeping your hands free for your baby. Calls, messages, music, and smart home all by voice.', 'Lifestyle', '5 min', 'Hands full with baby, Communication while holding baby, Baby care tools, Smart home for parents, Emergency preparedness, Self-care reminders'),
    ('uc_fitness', 'Voice-Controlled Fitness: Music, Tracking, Safety', 'voice control fitness', ['running music voice', 'workout tracking voice', 'fitness safety voice', 'exercise phone hands-free'], 'Music control, pace tracking, emergency calls, and hands-free photos during workouts.', 'Fitness', '6 min', 'Phone in armband hands busy, Music control mid-workout, Fitness tracking, Safety features, Social fitness, Cool-down and recovery'),
    ('comp_vs_siri', 'FoneClaw vs Siri: Which Voice Assistant is Better?', 'FoneClaw vs Siri', ['voice assistant comparison', 'siri limitations', 'ai agent vs assistant', 'siri alternative android'], 'System-level AI agent vs traditional voice assistant. Features, capabilities, cross-app control, and real-world performance.', 'Comparison', '7 min', 'Assistant vs agent, System access sandbox vs native, Multi-step tasks, Cross-app data passing, Remote control, Real-world verdict'),
    ('comp_vs_google', 'FoneClaw vs Google Assistant for Android', 'FoneClaw vs Google Assistant', ['android voice comparison', 'google assistant limitations', 'agent vs assistant android', 'google assistant replacement'], 'Agent-based approach vs cloud-first assistant. Cross-app tasks, privacy, on-device processing, and extensibility.', 'Comparison', '7 min', 'Architecture cloud-first vs device-first, Third-party app integration, Ad-hoc multi-step automation, Privacy model, Self-evolution learning, When to use which'),
]

import importlib.util
def load(f):
    s=importlib.util.spec_from_file_location('b',f)
    m=importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m.BATCH

# Load existing articles
for i in range(1,6):
    articles = load(f'/home/administrator/clawfone-v2/articles_batch{i}.py')

new_articles = {art[0]: None for art in ARTICLES}

for aid, title, primary, secondary, desc, cat, rt, topics in ARTICLES:
    prompt = f"""Write ONE article. CRITICAL: The title (H1) MUST be EXACTLY: "{title}"
Primary keyword: "{primary}" — use it 20+ times throughout
Secondary keywords: {secondary} — each in a different H2
Category: {cat}, Read time: {rt}
Description: {desc}
Topics: {topics}

Output: BATCH = [("{aid}", "{title}", "{desc}", "{cat}", "{rt}", [(subtitle, body_text), ...])]
Body text must be 250-400 words per section. 7-8 sections total. Last section is FAQ with 4-5 Q&A.
The title "{title}" must appear EXACTLY as written — do not modify it."""
    
    print(f"Generating {aid}...", end=" ", flush=True)
    content = call_gemini(system, prompt)
    if content:
        content = content.strip()
        if content.startswith("```"): content = content.split("\n", 1)[1]
        if content.endswith("```"): content = content.rsplit("```", 1)[0]
        content = content.strip()
        # Ensure BATCH prefix
        if not content.startswith("BATCH"):
            idx = content.find("BATCH")
            if idx >= 0: content = content[idx:]
        with open(f'/tmp/single_{aid}.py', 'w') as f:
            f.write(content + "\n")
        try:
            data = load(f'/tmp/single_{aid}.py')
            if data and len(data) > 0:
                new_articles[aid] = data[0]
                print("✅")
            else:
                print("❌ empty")
        except Exception as e:
            print(f"❌ {e}")
    else:
        print("❌ API failed")
    time.sleep(2)

# Merge into batch files
for batch_num in range(1, 6):
    fname = f'/home/administrator/clawfone-v2/articles_batch{batch_num}.py'
    articles = load(fname)
    merged = []
    for aid, title, desc, cat, rt, sections in articles:
        if aid in new_articles and new_articles[aid] is not None:
            merged.append(new_articles[aid])
            print(f"  {aid}: replaced with new version")
        else:
            merged.append((aid, title, desc, cat, rt, sections))
    with open(fname, 'w') as f:
        f.write(f"BATCH = {repr(merged)}\n")

print("\nAll 8 articles merged into batch files")
