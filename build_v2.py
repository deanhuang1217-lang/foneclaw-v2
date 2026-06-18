#!/usr/bin/env python3
"""FoneClaw Website v2 - Conversion-optimized copy"""
import pickle, os, json

base = '/home/administrator/clawfone-v2'
cache = pickle.load(open(os.path.join(base, '_build_cache.pkl'), 'rb'))
imgs = cache['imgs']
icon_b64 = cache['icon_b64']
logo = '<img src="favicon.png" alt="FoneClaw">'

def mi(name, alt=''):
    return f'<img src="data:image/jpeg;base64,{imgs[name]}" alt="{alt or name}" loading="lazy">'
def mf(name, alt=''):
    return '<figure class="fig">' + mi(name, alt) + '</figure>'

p = []

# ===== HEAD =====
p.append('<!DOCTYPE html>')
p.append('<html lang="en"><head>')
p.append('<meta charset="UTF-8">')
p.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
p.append('<title>FoneClaw - Your Phone, Your Voice, Zero Touch</title>')
p.append('<meta name="description" content="FoneClaw is a system-level AI agent that controls your Android phone entirely by voice. 50+ operations, cross-app automation, remote control. Free beta.">')
p.append('<meta name="robots" content="index, follow">')
p.append('<link rel="canonical" href="https://www.foneclaw.ai/">')
p.append('<meta property="og:type" content="website">')
p.append('<meta property="og:title" content="FoneClaw - Your Phone, Your Voice, Zero Touch">')
p.append('<meta property="og:description" content="Cant touch your phone? Dont want to? Shouldnt? Just speak. FoneClaw does the rest.">')
p.append('<meta property="og:url" content="https://www.foneclaw.ai/">')
p.append('<meta property="og:image" content="https://www.foneclaw.ai/og-image.png">')
p.append('<meta property="og:site_name" content="FoneClaw">')
p.append('<meta name="twitter:card" content="summary_large_image">')
p.append('<meta name="twitter:title" content="FoneClaw - Your Phone, Your Voice, Zero Touch">')
p.append('<meta name="twitter:description" content="Cant touch your phone? Just speak. FoneClaw does the rest.">')
p.append('<meta name="twitter:image" content="https://www.foneclaw.ai/og-image.png">')
p.append('<meta name="theme-color" content="#080c18">')
p.append('<link rel="icon" type="image/png" href="favicon.png">')
p.append('<link rel="apple-touch-icon" href="favicon.png">')
p.append('<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareApplication","name":"FoneClaw","applicationCategory":"UtilitiesApplication","operatingSystem":"Android","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}}</script>')
p.append('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"FoneClaw","url":"https://www.foneclaw.ai","logo":"https://www.foneclaw.ai/favicon.png"}</script>')

p.append('<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Is FoneClaw always listening to me?","acceptedAnswer":{"@type":"Answer","text":"No. It only activates on wake word or button press. No background recording."}},{"@type":"Question","name":"Is it safe to let an AI control my phone?","acceptedAnswer":{"@type":"Answer","text":"Built-in safety: voice PIN, App Whitelist, real-time status bar, say Stop anytime."}},{"@type":"Question","name":"How is this different from Siri?","acceptedAnswer":{"@type":"Answer","text":"Siri handles one command. FoneClaw chains multi-step tasks across apps and learns."}},{"@type":"Question","name":"Does it work on my phone?","acceptedAnswer":{"@type":"Answer","text":"Android 10+. Xiaomi optimized, Samsung/Pixel coming. iOS planned late 2026."}},{"@type":"Question","name":"How much does it cost?","acceptedAnswer":{"@type":"Answer","text":"Free for core commands. Pro $4.99/mo for automation. Beta users 50% off forever."}}]}</script>')
# CSS from file
with open(os.path.join(base, '_style.css')) as f:
    p.append(f.read())
translations = json.load(open(os.path.join(base, 'translations.json')))
print('[1/8] Head + CSS done')

# ===== NAV =====
p.append('<nav aria-label="Main navigation"><div class="nb">')
p.append(f'<span class="logo" onclick="G(0)">{logo}FoneClaw</span>')
p.append('<div class="nr"><a id="n0" onclick="G(0)">Home</a><a id="n1" onclick="G(1)">Features</a><a id="n2" onclick="G(2)">Resources</a><a id="n3" onclick="G(3)">Community</a>')
p.append('<div class="lang-dropdown" id="langDD"><button class="lang-btn" onclick="document.getElementById(\'langDD\').classList.toggle(\'open\')"><span id="currentFlag">\U0001f1fa\U0001f1f8</span> <span id="currentLang">EN</span> <span class="lang-arrow">\u25be</span></button><div class="lang-menu"><a onclick="setLang(\'en\')">\U0001f1fa\U0001f1f8 English</a><a onclick="setLang(\'zh\')">\U0001f1e8\U0001f1f3 \u4e2d\u6587</a><a onclick="setLang(\'ja\')">\U0001f1ef\U0001f1f5 \u65e5\u672c\u8a9e</a><a onclick="setLang(\'ko\')">\U0001f1f0\U0001f1f7 \ud55c\uad6d\uc5b4</a></div></div>')
p.append('</div></nav>')
print("[2/8] Nav done")

# ===== HOME PAGE =====
p.append('<main id="p0" class="pg on">')

# HERO
p.append('<section class="hero" style="background-image:url(data:image/jpeg;base64,' + imgs['hero_banner'] + ')"><div>')
p.append('<h1>Fone<span class="cn">Claw</span></h1>')
p.append('<p class="tag">Your Phone, Your Voice, Zero Touch</p>')
p.append('<p class="sub">An AI agent that actually controls your phone \u2014 not just answers questions. 50+ system operations, cross-app automation, learns your habits.</p>')
p.append('<p class="pain">\U0001f6ab Driving? Cooking? Holding a baby? Visually impaired? Your hands are free. Your phone is not.</p>')
p.append('<div class="btns"><a class="bp" onclick="G(1)">See How It Works \u2192</a><a class="bo">Free Beta \u2014 Join Waitlist</a></div>')
p.append('</div></section>')

# PAIN POINTS - emotional hook
p.append('<section class="pain-section"><div class="wrap"><div class="st"><h2>Real Problems. Real Solutions.</h2><p>Every day, millions of people struggle with the same phone frustrations</p></div>')
p.append('<div class="pain-grid">')
for icon, title, problem, solution in [
    ("\U0001f697", "Driving and need to reply to a text", "48 US states ban texting while driving. 3,000+ deaths/year from distracted driving.", "FoneClaw: Reply by voice. No screen touch. 100% legal."),
    ("\U0001f474", "Holding your baby and the phone rings", "One arm for baby, zero arms for phone.", "FoneClaw: Call husband, play white noise, check camera \u2014 all by voice."),
    ("\U0001f9d3", "Elderly parents keep calling for phone help", "50M+ US seniors struggle with smartphone complexity.", "FoneClaw: Set up their phone remotely via Telegram. They just speak."),
    ("\U0001f441\ufe0f", "Cannot see the screen but need your phone", "7M visually impaired Americans rely on complex accessibility gestures.", "FoneClaw: 100% voice control. Every function accessible. No gestures."),
    ("\U0001f373", "Cooking and need to check the recipe", "Hands covered in flour. Phone on the counter.", "FoneClaw: Read recipe step by step. Set timers. Play music. Hands-free."),
    ("\U0001f4bc", "A simple task takes 10 taps across 5 apps", "Book a flight: open app, search, compare, select, pay = 10 minutes.", "FoneClaw: One sentence. Done. 30 seconds."),
]:
    p.append(f'<div class="pain-card"><div class="icon">{icon}</div><h3>{title}</h3><p>{problem}</p><div class="solution">\u2705 {solution}</div></div>')
p.append('</div></div></section>')

# TRUST BAR
p.append('<section class="trust-section"><div class="wrap"><div class="trust-grid">')
for icon, title, desc in [
    ("\U0001f512", "You Are Always In Control", "Every sensitive action requires your confirmation. Say Stop anytime. Set spending limits. App whitelist."),
    ("\U0001f50a", "Not Listening Until You Ask", "Only activates on wake word or button press. No background recording. No silent data collection."),
    ("\U0001f4e6", "Your Data Stays On Device", "Voice profile, contacts, preferences \u2014 all stored locally. Cloud processing deletes instantly after use."),
    ("\U0001f4b0", "Free Core Forever", "Calls, messages, basic apps \u2014 always free. Pro $4.99/mo for advanced automation. Beta users 50% off forever."),
]:
    p.append(f'<div class="trust-item"><div class="t-icon">{icon}</div><h4>{title}</h4><p>{desc}</p></div>')
p.append('</div></div></section>')
print("[3/8] Home hero + pain + trust done")

# CORE CAPABILITIES - benefit-focused copy
p.append('<section class="sec"><div class="wrap"><div class="st"><h2>What FoneClaw Actually Does</h2><p>Not a chatbot. Not a voice assistant. A system-level AI agent that controls your phone.</p></div>')
for i,(n,title,desc,items) in enumerate([
    ('home_cap_voice','50+ Phone Operations By Voice','FoneClaw calls Android system APIs directly \u2014 not simulated taps. Make calls, send messages, adjust settings, control any app, manage files. Works at 3-5 meters with automatic noise cancellation. Wake rate and accuracy both above 95%.',['50+ system-level operations','Works at 3-5 meter range','Automatic noise cancellation','Wake word detection >95%']),
    ('home_cap_agent','One Sentence, Full Workflow','Say "Book the earliest flight from NYC to LA tomorrow" and FoneClaw searches, compares, books, pays, and sets a reminder \u2014 automatically. It understands intent, breaks tasks into steps, chains multiple apps, and handles errors.',['Intent accuracy >90%','Multi-step completion >80%','Conditional logic and branching','Automatic error recovery']),
    ('home_cap_remote','Control Your Phone From Anywhere','Your phone does not need to be in your hand. Connect via Telegram or WhatsApp and check battery, read messages, take photos, share location, or run any command \u2014 from any device, anywhere in the world. Under 3 seconds latency.',['Telegram Bot integration','WhatsApp support','Remote status queries','Remote photo and audio capture']),
    ('home_cap_evolve','Learns You. Gets Smarter.','FoneClaw remembers your morning alarm, your favorite DoorDash order, your commute route, your cooking music. It builds a preference model and optimizes execution over time. It even creates specialized sub-agents for your recurring tasks.',['File-level persistent memory','Learns user preferences','Optimizes execution strategies','Sub-agent spawning']),
]):
    li = ''.join('<li>' + x + '</li>' for x in items)
    bg = '' if i % 2 == 0 else 'background:#0b1020;'
    p.append(f'<div style="padding:50px 20px;{bg}"><div style="max-width:1000px;margin:0 auto" class="fg">{mf(n)}<div><h3>{title}</h3><p>{desc}</p><ul>{li}</ul></div></div></div>')
p.append('</div></section>')
print("[4/8] Capabilities done")

# USE CASES - three categories
p.append('<section class="se"><div class="wrap"><div class="st"><h2>Three Reasons You Need FoneClaw</h2><p>Cannot touch. Do not want to touch. Should not touch.</p></div>')

for cat_key, cat_title, cat_desc, cases in [
    ('cant_touch','\U0001f6ab Cannot Touch','Physically unable to touch the phone', [
        ('home_uc_blind','Visually Impaired','7M Americans. 100% voice control. 911 + automatic location sharing. No gestures needed.',[('All voice operations',''),('Call 911, send location','')]),
        ('home_uc_emergency','Emergency','"Call 911" \u2014 instant connection, auto speakerphone, GPS shared with emergency contacts. Works when phone is locked.',[('Call 911',''),('Send location to dad','')]),
        ('home_uc_baby','Holding a Baby','Baby in one arm. Phone ringing. FoneClaw: call husband, play white noise, check baby camera \u2014 both arms stay where they belong.',[('Call husband',''),('Play white noise','')]),
        ('home_uc_elderly','Elderly Parents','50M+ US seniors struggle with smartphones. FoneClaw replaces confusing gestures with natural voice. Family can configure remotely via Telegram.',[('Call my son',''),('BP is normal',''),('Text bigger','')]),
    ]),
    ('dont_want','\U0001f4a1 Do Not Want to Touch','More efficient without touching', [
        ('home_uc_multi','Multi-Step Tasks','"Find earliest flight NYC-LAX, book it, set reminder." One sentence replaces 10 taps. Agent engine handles the entire workflow.',[('Book NYC-LAX flight',''),('Where is my package?','')]),
        ('home_uc_run','Exercise','Running, cycling, lifting \u2014 hands busy, phone in armband. Change songs, check pace, answer calls. Works even with heavy breathing.',[('Next song',''),('Current pace?','')]),
    ]),
    ('shouldnt','\u26a0\ufe0f Should Not Touch','Safety or legal reasons', [
        ('home_uc_driving','Driving','Hands on wheel, eyes on road. 48 US states ban texting while driving. FoneClaw: reply by voice, navigate, make calls \u2014 100% legal.',[('Navigate to gas station',''),('Call wife, running late',''),('Reply iMessage: 10 min','')]),
        ('home_uc_cook','Cooking','Hands covered in flour? Just speak. Recipes, timers, music, smart home control \u2014 all without washing your hands.',[('How to make lasagna?',''),('Set timer 20 min',''),('Set AC to 72 degrees','')]),
    ]),
]:
    p.append(f'<div style="margin-bottom:40px"><h3 style="font-size:22px;font-weight:700;margin-bottom:6px;color:#00d4ff">{cat_title}</h3><p style="color:#8b949e;font-size:14px;margin-bottom:16px">{cat_desc}</p>')
    for n,title,desc,items in cases:
        li = ''.join(f'<li>{a}</li>' for a,_ in items)
        p.append(f'<article class="uc-card">{mi(n,title)}<div class="uc-body"><h3>{title}</h3><p>{desc}</p><ul>{li}</ul></div></article>')
    p.append('</div>')
p.append('</div></section>')
print("[5/8] Use Cases done")

# ARCHITECTURE
p.append('<section class="sec"><div class="wrap"><div class="st"><h2>Five-Layer Architecture</h2><p>From hearing your voice to executing your will</p></div>')
p.append('<div style="max-width:1000px;margin:0 auto" class="fg">' + mf('home_arch') + '<div class="g5" style="grid-template-columns:repeat(3,1fr);gap:8px">')
for n,t,s in [('01','Perception','Speech and intent'),('02','Planning','Task decomposition'),('03','Execution','System calls'),('04','Memory','User habits'),('05','Evolution','Self-learning')]:
    p.append(f'<div class="ac"><div class="n">{n}</div><h4>{t}</h4><p>{s}</p></div>')
p.append('</div></div></div></section>')

# HOW IT WORKS
p.append('<section class="se"><div class="wrap"><div class="st"><h2>How It Works</h2><p>One voice command. Full execution.</p></div>')
p.append('<div style="max-width:1000px;margin:0 auto;text-align:center">' + mf('home_workflow'))
p.append('<div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:24px">')
for n,t,d in [('01','You Say','Set alarm for 8am'),('02','Understand','AI: set alarm, 8am'),('03','Plan','Open clock, set time'),('04','Execute','Auto-call system'),('05','Respond','Done. Repeat?')]:
    p.append(f'<div style="background:rgba(14,20,38,0.9);border:1px solid rgba(0,200,255,0.08);border-radius:8px;padding:14px;text-align:center;flex:1;max-width:160px"><div style="font-size:18px;font-weight:800;color:#00d4ff;opacity:.2">{n}</div><h4 style="font-size:13px;font-weight:700">{t}</h4><p style="color:#8b949e;font-size:12px">{d}</p></div>')
p.append('</div></div></div></section>')

# COMPARISON
p.append('<section class="sec"><div class="wrap"><div class="st"><h2>FoneClaw vs Traditional Assistants</h2><p>Siri answers questions. FoneClaw does the work.</p></div><div style="overflow-x:auto"><table class="tb">')
for i,(a,b,c) in enumerate([('Feature','FoneClaw','Siri / Google'),('Core','System-level AI Agent','Voice command tool'),('System Access','Deep permissions, direct API','Limited app access'),('Execution','Auto-decompose, 50+ tools','Simple one-step commands'),('Cross-App','One sentence, multi-app workflow','Not supported'),('Remote Control','Telegram/WhatsApp from anywhere','Not supported'),('Learning','File-level memory, self-evolution','Fixed capabilities'),('Privacy','On-device first, cloud instant delete','All cloud processed')]):
    t='th' if i==0 else 'td'; clr=' style="color:#00d4ff"' if i>0 else ''
    p.append(f'<tr><{t}>{a}</{t}><{t}{clr}>{b}</{t}><{t}>{c}</{t}></tr>')
p.append('</table></div></div></section>')

# FAQ - address real concerns
p.append('<section class="se"><div class="wrap"><div class="st"><h2>Questions You Actually Have</h2></div><div style="max-width:700px;margin:0 auto">')
for q,a in [
    ('Is FoneClaw always listening to me?','No. It only activates when you say the wake word or press the floating button. It does NOT record or transmit anything in the background. Voice processing happens on your device first \u2014 cloud is used only for complex commands and deleted immediately after.'),
    ('Is it safe to let an AI control my phone?','Built-in safety: (1) Sensitive actions like payments require voice PIN confirmation. (2) App Whitelist \u2014 only apps you approve. (3) Real-time status bar shows every action. (4) Say "Stop" anytime to cancel. (5) Full execution history, all reversible.'),
    ('How is this different from Siri or Google Assistant?','Siri and Google handle one command at a time. FoneClaw is an AI Agent that chains multiple steps across apps. "Find earliest flight to LA, book it, set reminder" \u2014 Siri cannot do this. FoneClaw also has deep system access and learns your habits.'),
    ('Does it work on my phone?','Android 10+ phones. Currently optimized for Xiaomi, Samsung and Pixel coming soon. No special hardware needed \u2014 just install the app. iOS planned for late 2026.'),
    ('How much does it cost?','Free during beta. After launch: free tier for core commands (calls, messages, basic apps) and Pro ($4.99/mo) for multi-step automation, remote control, and unlimited app integrations. Beta users get permanent 50% discount.'),
    ('What if FoneClaw misunderstands me?','Every action is reversible. Low-risk tasks execute immediately. High-risk tasks (sending messages, purchases, deletions) require confirmation. Set a global confirmation level: Fast, Normal, or Safe.'),
    ('Will it drain my battery?','On-device processing is battery-optimized. Idle: less than 3%/day. Active use (20+ commands): 8-12%. Driving mode: about 15%. Disable always-on listening to save more.'),
    ('Can it make purchases or access my bank app?','By default, FoneClaw can browse but NOT complete purchases. Enable Shopping Mode with voice PIN for purchases. Banking apps are excluded by default \u2014 add to App Whitelist with a spending limit. We NEVER store payment information.'),
    ('Can I set it up for my elderly parents remotely?','Yes! Connect your Telegram to their FoneClaw: (1) Add contacts remotely, (2) Set medication reminders, (3) Check battery and connectivity, (4) Help troubleshoot, (5) Set Family Mode for safe contacts only. They do not need to configure anything.'),
    ('Can I use it in languages other than English?','Currently supports English (US, UK, AU) with 95%+ accuracy. Spanish, French, German, and Mandarin Chinese in beta. 10+ languages coming throughout 2026. Voice profile calibration helps with accent recognition.'),
]:
    p.append(f'<div class="fq" onclick="this.classList.toggle(\'on\')"><div class="fq-q">{q}</div><div class="fq-a">{a}</div></div>')
p.append('</div></div></section>')

# BOTTOM CTA
p.append('<section style="padding:80px 0;text-align:center;background:linear-gradient(180deg,#080c18 0%,#0b1a3a 50%,#080c18 100%)">')
p.append('<div class="wrap"><h2 style="font-size:clamp(28px,5vw,42px);font-weight:800;margin-bottom:12px">Ready to Talk to Your Phone?</h2>')
p.append('<p style="color:#8b949e;font-size:17px;max-width:500px;margin:0 auto 28px">Join the beta. Free forever for core features. No credit card required.</p>')
p.append('<div class="btns"><a class="bp" onclick="G(1)">Explore Features \u2192</a><a class="bo">Join Beta Waitlist</a></div></div></section>')
p.append('</main>')
print("[6/8] Architecture + HowItWorks + Comparison + FAQ done")

# ===== FEATURES PAGE =====
p.append('<div id="p1" class="pg">')
p.append('<header style="position:relative;min-height:360px;display:flex;align-items:center;justify-content:center;text-align:center;background-image:url(data:image/jpeg;base64,' + imgs['features_banner'] + ');background-size:cover"><div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(8,12,24,0.5),rgba(8,12,24,0.85))"></div><div style="position:relative;z-index:1;padding:60px 20px"><h1 style="font-size:clamp(28px,5vw,44px);font-weight:800;margin-bottom:10px">Features</h1><p style="color:#8b949e;font-size:17px">Every capability, from core engine to real-world scenarios</p></div></header>')
for idx,(img_n,title,desc,metrics) in enumerate([
    ('feat_voice','Voice Interaction Engine','Streaming speech recognition, wake word, Barge-in interruption, noise cancellation, 3-5m far-field. Works in cars, kitchens, busy streets.', ['Wake >95%','Accurate >95%','<1s latency','3-5m range']),
    ('feat_agent','AI Agent Core Engine','Understands natural language intent. Auto-decomposes complex requests into executable sub-tasks. Conditional branching. Error recovery with retry and alternatives.', ['Intent >90%','Multi-step >80%','Conditional','Error recovery']),
    ('feat_system','System-Level Execution','Deep Android integration via Accessibility Service and native APIs. 50+ operations. Does not simulate taps \u2014 calls system APIs directly. Android 10+.', ['>98% success','<500ms','Native API','Android 10+']),
    ('feat_ui','UI Interface','Floating action button for instant access from any screen. Conversation history. Step-by-step permission setup. 60fps animations.', ['60fps smooth','30s setup','Guide >90%']),
    ('feat_driving','Driving / Riding','Auto driving mode activates on car Bluetooth or driving speed. Voice-only interface. Google Maps, calls, iMessage, food ordering \u2014 all hands-free and legal.', ['Driving >90%','BT >95%']),
    ('feat_multistep','Multi-Step Cross-App','"Check meetings, reschedule 3pm, order DoorDash for 12:30" \u2014 multi-app workflow from one sentence. 2-step success >85%, 3-step >70%.', ['2-step >85%','3-step >70%']),
    ('feat_elderly','Elderly Mode','For 50M+ US seniors. Extra-large text, simplified voice commands, family contact shortcuts, medication reminders. Family remote config via Telegram.', ['65+ first-use >70%','Error <1%']),
    ('feat_remote','Telegram/WhatsApp Remote','Control phone from anywhere. Battery, messages, photos, location, voice commands. Latency <3s. Perfect for helping elderly parents remotely.', ['<3s latency','>90% success']),
    ('feat_memory','Memory & Self-Evolution','Detailed user memory: preferences, routines, apps, contacts. Learns morning routine, commute, habits. Sub-agents for specialized recurring tasks.', ['Recognize >95%','Predict >70%']),
    ('feat_apps','Third-Party App Support','Native support for iMessage, Amazon, DoorDash, Google Maps, Spotify, Uber, and more. Each app integration supports 5+ distinct voice operations.', ['iMessage','Amazon','DoorDash','Google Maps']),
]):
    met = ''.join(f'<p style="color:#8b949e;font-size:14px">\u2705 {m}</p>' for m in metrics)
    bg = '' if idx%2==0 else 'background:#0b1020;'
    p.append(f'<section style="padding:60px 20px;{bg}"><div style="max-width:1000px;margin:0 auto" class="fg">{mf(img_n)}<div><h3>{title}</h3><p>{desc}</p><div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">{met}</div></div></div></section>')
p.append('</div>')

# ===== RESOURCES PAGE =====
p.append('<div id="p2" class="pg"><header style="position:relative;min-height:300px;display:flex;align-items:center;justify-content:center;text-align:center;background:linear-gradient(135deg,#080c18 0%,#0b1a3a 50%,#080c18 100%)"><div style="position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(0,212,255,0.08) 0%,transparent 70%)"></div><div style="position:relative;z-index:1;padding:60px 20px"><h1 style="font-size:clamp(28px,5vw,44px);font-weight:800;margin-bottom:10px">Resources</h1><p style="color:#8b949e;font-size:17px;max-width:500px;margin:0 auto">How-to guides, use cases, and comparisons</p></div></header>')

# How-To
p.append('<section class="sec" id="sec-howto"><div class="wrap"><div class="st"><h2>How-To Guides</h2></div><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px">')
for img_n,title,desc,cat,rt,aid in [
    ('howto_voice_android','Control Android with Voice','Complete setup guide for voice control on Android.','Setup','5 min','voice-android'),
    ('howto_texts_handsfree','Send Texts Without Touching Phone','iMessage, WhatsApp, SMS by voice only.','Tutorial','4 min','texts-handsfree'),
    ('howto_multistep','Automate Multi-Step Tasks','Book flights, manage smart home, order food with one sentence.','Advanced','8 min','multistep'),
    ('howto_elderly_setup','Voice Control for Elderly Parents','Large text, family contacts, simplified commands.','Guide','5 min','elderly-setup'),
    ('howto_driving_voice','Voice Commands While Driving','Driving mode, car Bluetooth, hands-free.','Safety','4 min','driving-voice'),
    ('howto_smart_home','Control Smart Home by Voice','Lights, thermostat, locks from your phone.','Smart Home','6 min','smart-home'),
]:
    p.append(f'<article class="rc" onclick="showArticle(\'{aid}\')"><img class="rc-img" src="data:image/jpeg;base64,{imgs[img_n]}" alt="{title}"><div class="rc-body"><div class="cat">{cat}</div><h3>{title}</h3><p>{desc}</p><div class="meta">{rt} read</div><div class="arrow">Read \u2192</div></div></article>')
p.append('</div></div></section>')

# Use Cases
p.append('<section class="se" id="sec-usecases"><div class="wrap"><div class="st"><h2>Use Cases</h2></div><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px">')
for img_n,title,desc,cat,rt,aid in [
    ('uc_commuting','Voice for Commuters','Stay connected safely driving, biking, or on transit.','Commuting','7 min','commuting'),
    ('uc_seniors','AI Phone for Seniors','50M+ seniors use phones independently with voice.','Accessibility','9 min','seniors'),
    ('uc_cooking','Hands-Free Cooking','Recipes, timers, music while cooking.','Lifestyle','5 min','cooking'),
    ('uc_emergency','Emergency Voice Commands','911, location when you can\'t touch phone.','Safety','6 min','emergency'),
    ('uc_productivity','Productivity Automation','Save 30+ minutes daily.','Productivity','8 min','productivity'),
    ('uc_visual_impaired','Voice for Visually Impaired','Full control for 7M Americans.','Accessibility','7 min','visual-impaired'),
    ('uc_parenting','Parenting Hands-Free','Stay connected holding baby.','Lifestyle','5 min','parenting'),
    ('uc_fitness','Voice Fitness','Music, tracking during workouts.','Fitness','6 min','fitness'),
]:
    p.append(f'<article class="rc" onclick="showArticle(\'{aid}\')"><img class="rc-img" src="data:image/jpeg;base64,{imgs[img_n]}" alt="{title}"><div class="rc-body"><div class="cat">{cat}</div><h3>{title}</h3><p>{desc}</p><div class="meta">{rt} read</div><div class="arrow">Read \u2192</div></div></article>')
p.append('</div></div></section>')

# Comparisons
p.append('<section class="sec" id="sec-comparisons"><div class="wrap"><div class="st"><h2>Comparisons</h2></div><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px">')
for img_n,title,desc,cat,aid in [
    ('comp_vs_siri','FoneClaw vs Siri','AI agent vs traditional assistant.','Comparison','vs-siri'),
    ('comp_vs_google','vs Google Assistant','Device-first vs cloud-first.','Comparison','vs-google'),
    ('comp_vs_alexa','vs Alexa Mobile','Mobile vs home approach.','Comparison','vs-alexa'),
    ('comp_best_apps','Best Voice Apps 2026','Top solutions roundup.','Roundup','best-apps'),
    ('comp_ai_replacing','AI Agents Replacing Assistants','The shift from Siri to agents.','Industry','ai-replacing'),
]:
    p.append(f'<article class="rc" onclick="showArticle(\'{aid}\')"><img class="rc-img" src="data:image/jpeg;base64,{imgs[img_n]}" alt="{title}"><div class="rc-body"><div class="cat">{cat}</div><h3>{title}</h3><p>{desc}</p><div class="arrow">Read \u2192</div></div></article>')
p.append('</div></div></section></div>')

# ===== COMMUNITY PAGE =====
p.append('<div id="p3" class="pg"><header style="position:relative;min-height:300px;display:flex;align-items:center;justify-content:center;text-align:center;background:linear-gradient(135deg,#080c18 0%,#0b1a3a 50%,#080c18 100%)"><div style="position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(0,212,255,0.08) 0%,transparent 70%)"></div><div style="position:relative;z-index:1;padding:60px 20px"><h1 style="font-size:clamp(28px,5vw,44px);font-weight:800;margin-bottom:10px">Community</h1><p style="color:#8b949e;font-size:17px;max-width:500px;margin:0 auto">Join the movement shaping the future of phone AI</p></div></header>')
p.append('<section style="padding-top:40px"><div class="wrap"><div class="gc">')
for ic,t,d,b in [('\u2708\ufe0f','Telegram','Updates and beta access.','Join'),('\U0001f465','Facebook','Announcements and user stories.','Follow'),('\U0001f3ae','Discord','Real-time chat and dev discussion.','Join'),('\U0001f4ac','Feedback','Feature requests and bug reports.','Submit')]:
    p.append(f'<div class="cc"><div class="ci">{ic}</div><h3>{t}</h3><p>{d}</p><a class="bs">{b}</a></div>')
p.append('</div></div></section></div>')

# FOOTER
p.append(f'<footer><div class="wrap"><div class="ft-inner"><div class="ft-col"><div class="logo" style="margin-bottom:12px">{logo}FoneClaw</div><p style="color:#8b949e;font-size:14px">AI Agent for voice-controlled Android phones. Your phone, your voice, zero touch.</p></div>')
p.append('<div class="ft-col"><h4>Product</h4><a href="#" onclick="G(1);return false">Features</a><a href="#">Download</a></div>')
p.append('<div class="ft-col"><h4>Resources</h4><a href="#" onclick="G(2,\'sec-howto\');return false">How-To Guides</a><a href="#" onclick="G(2,\'sec-usecases\');return false">Use Cases</a><a href="#" onclick="G(2,\'sec-comparisons\');return false">Comparisons</a></div>')
p.append('<div class="ft-col"><h4>Company</h4><a href="#" onclick="G(3);return false">Community</a><a href="#">Contact</a><a href="#">Privacy Policy</a></div>')
p.append('</div><p style="text-align:center;margin-top:30px;color:#484f58;font-size:12px">&copy; 2026 FoneClaw. All rights reserved.</p></div></footer>')
p.append('<button class="back-to-top" id="backToTop" onclick="window.scrollTo({top:0,behavior:\'smooth\'})">\u2191</button>')
print("[7/8] Features + Resources + Community + Footer done")

# ===== ARTICLE OVERLAYS =====
def art(aid, cat, title, img_name, sects):
    t = '<div class="article-overlay" id="art-' + aid + '"><button class="close-btn" onclick="hideArticle()">&times;</button><div class="article-content">'
    t += '<span class="back-link" onclick="hideArticle()">&larr; Back</span><div class="cat">' + cat + '</div><h1>' + title + '</h1>'
    t += '<img class="art-hero" src="data:image/jpeg;base64,' + imgs[img_name] + '" alt="' + title + '">'
    for s,b in sects:
        t += '<h2>' + s + '</h2><p>' + b + '</p>'
    return t + '</div></div>'

articles_data = [
    ('voice-android','Setup','How to Control Android with Voice','howto_voice_android',[('Why Voice Control','Voice transforms phone interaction when driving, cooking, or hands are full. FoneClaw provides system-level control over 50+ operations.'),('Install and Permissions','Download from Play Store. Setup wizard guides through Accessibility Service permissions with clear animations. Takes about 30 seconds.'),('Voice Profile','Calibrates to your voice in 30 seconds. Accuracy improves from 90% to 95%+. Custom wake word available.'),('Basic Commands','Start simple: Call Mom, Text John, Set alarm 7am, Open Spotify. Instant execution with audio confirmation.'),('Advanced Commands','Try: Check calendar tomorrow, Navigate to Starbucks and text wife, Order my usual from DoorDash. The agent engine handles complexity.'),('Pro Tips','Use Barge-in to interrupt. Chain commands. Enable driving mode for car Bluetooth. Set up family contacts for quick calling.')]),
    ('texts-handsfree','Tutorial','Send Texts Without Touching Phone','howto_texts_handsfree',[('Safe Messaging','Millions text while driving or cooking. FoneClaw makes it safe: just speak. Supports iMessage, WhatsApp, SMS, Telegram.'),('Basic Commands','Send text to Mom saying dinner at 7. FoneClaw auto-selects the right app based on contact preferences.'),('Multi-App Support','Text Sarah on WhatsApp uses WhatsApp. iMessage Dad uses iMessage. AI remembers which app you use for each contact.'),('Reading Aloud','Read my latest messages reads them aloud, handling group chats and timestamps. Perfect when you cannot look at the screen.'),('Voice Reply','Say Reply and dictate. FoneClaw reads back for confirmation. Change that to edits before sending. 10 seconds total.'),('Driving Mode','Auto-activates at driving speeds. All messages read aloud and replies are voice-only. Set auto-replies: Driving, will reply soon.')]),
    ('multistep','Advanced','Automate Multi-Step Tasks','howto_multistep',[('Multi-Step Power','Real-world tasks involve multiple apps. Booking a flight requires searching, comparing, booking, and setting reminders. FoneClaw handles all from one sentence.'),('Book a Trip','Find earliest flight NYC-LAX tomorrow, book with saved card, set reminder. FoneClaw: search, compare, select, book, remind.'),('Smart Home Routine','Good night: lock front door, set thermostat 68, turn off all lights, set alarm for 7am, enable Do Not Disturb.'),('Order Food','Order my usual from DoorDash for 12:30. Remembers favorite orders, places order, confirms total.'),('Complex Workflows','Chain any commands: Check meetings, cancel 3pm, order lunch. Conditional: If 3pm meeting, remind 15min before.'),('Success Rates','Two-step tasks succeed over 85% of the time. Three-step tasks succeed over 70%. The AI learns from failures and improves.')]),
    ('elderly-setup','Guide','Voice Control for Elderly Parents','howto_elderly_setup',[('The Challenge','Over 50 million US seniors own smartphones but struggle with small screens, complex gestures, and confusing interfaces.'),('Install on Their Phone','Visit your parent and install FoneClaw. The app uses large text and clear voice prompts. Every step includes audio instructions.'),('Configure Family Contacts','Set up 5 most important contacts with simple voice shortcuts: Call my son, Call the doctor. Add remotely via Telegram.'),('Enable Simplified Mode','Turn on Elderly Mode: extra-large text 24px minimum, simplified command vocabulary, always-on voice feedback, confirmation before every action.'),('Medication Reminders','Create voice-activated medication reminders. FoneClaw can remind at specific times and log acknowledgment. Check remotely.'),('Remote Family Assistance','Connect your Telegram to their FoneClaw. Check battery, read recent messages, help navigate, troubleshoot all from your phone.')]),
    ('driving-voice','Safety','Voice Commands While Driving','howto_driving_voice',[('Why Voice Matters','Distracted driving causes over 3,000 deaths per year in the US. Texting while driving is illegal in 48 states.'),('Setting Up Driving Mode','Auto-detects driving via car Bluetooth connection or GPS speed. Switches to voice-only mode with no screen interaction needed.'),('Essential Driving Commands','Navigate to nearest gas station opens Maps. Call my wife dials hands-free. Reply to last message sends a voice-typed reply.'),('Car Bluetooth Integration','Pair phone with car Bluetooth. FoneClaw uses car speakers for audio and car microphone for voice input. Steering wheel volume works.'),('Legal Compliance','Driving mode prevents screen-based interactions. All actions are voice-only. Automatically sends I am driving replies to incoming messages.'),('Emergency While Driving','If you witness an accident or have a medical emergency: Call 911 connects immediately. Send my location to emergency contacts shares GPS.')]),
    ('smart-home','Smart Home','Control Smart Home by Voice','howto_smart_home',[('The Connected Home','Modern homes have dozens of smart devices. FoneClaw unifies all of them under one voice interface instead of opening 5 different apps.'),('Supported Devices','Works with Philips Hue, Nest, Ring, August Lock, TP-Link, Samsung SmartThings, and any device controllable through Google Home or Alexa.'),('Basic Commands','Turn off the living room lights. Set thermostat to 72 degrees. Lock the front door. Execute in under 2 seconds with audio confirmation.'),('Creating Routines','Movie time dims lights to 20%, sets thermostat to 70, turns on TV, closes blinds. Leaving home locks all doors, turns off all lights, arms security.'),('Voice vs App Control','Voice is faster for quick actions: 2 seconds vs opening app, finding device, tapping. For complex setups like scenes and schedules, the app interface is better.'),('Privacy and Security','Smart home commands are processed locally when possible. Camera feeds are not stored in the cloud. Lock commands require voice verification.')]),
    ('commuting','Commuting','Voice for Commuters','uc_commuting',[('The Commuter Dilemma','The average American spends 27 minutes commuting each way. That is nearly an hour daily where your phone is in your pocket and your eyes are on the road.'),('Morning Commute Routine','Start my commute: read calendar, check traffic, play morning podcast, text spouse your ETA. All automatically when you connect to car Bluetooth.'),('Stay Connected While Driving','Reply to messages, join conference calls, check emails read aloud, manage schedule all without touching your phone. Noise cancellation works with road noise.'),('Public Transit Use','On buses and trains, use earbuds for private voice control. Whisper mode detects quiet speech for crowded environments.'),('Safety Compliance','Driving mode auto-activates when it detects car Bluetooth or driving speeds. Prevents accidental screen touches. All interactions are voice-only.'),('Real User Scenario','What is on my schedule today reads calendar. Reply to team Slack sends message. Play commute playlist starts music. All while keeping both hands on the wheel.')]),
    ('seniors','Accessibility','AI Phone for Seniors','uc_seniors',[('The Digital Divide','Over 50 million Americans are 65 or older. Many own smartphones but struggle with small text, complex gestures, and confusing app interfaces.'),('Voice-First Design','Everything in FoneClaw can be done by voice. No tiny buttons, no swipe gestures, no hidden menus. Call my son works every time.'),('Family Remote Assistance','Adult children can connect their Telegram to parent FoneClaw. Check battery, help with settings, add contacts, troubleshoot all remotely.'),('Medication and Health','Set daily medication reminders that speak aloud: Time for your blood pressure pill. Log acknowledgment and notify family if missed.'),('Emergency Features','One-voice emergency: Call 911 connects instantly. I fell, send help triggers SOS to all emergency contacts with GPS location.'),('Adoption Speed','Beta testers report elderly users adopt FoneClaw within 3 days, compared to weeks for traditional smartphone training.')]),
    ('cooking','Lifestyle','Hands-Free Cooking','uc_cooking',[('The Kitchen Challenge','Cooking requires both hands. You are chopping, stirring, measuring and your phone is covered in flour. FoneClaw lets you control entirely by voice.'),('Recipe Assistance','How do I make lasagna reads the recipe step by step. What is the next step advances. How long do I bake this answers immediately.'),('Multiple Timers','Set multiple timers simultaneously: 20-minute timer for pasta, 45-minute timer for bread. Each has a distinct sound. How much time left checks remaining.'),('Smart Kitchen Control','Set the oven to 375 degrees. Turn on the kitchen lights. Set the thermostat to 72. Control smart appliances without leaving the counter.'),('Entertainment While Cooking','Play my cooking playlist on Spotify. Play the latest episode. Call Mom and ask about her stuffing recipe. Stay entertained while hands are busy.'),('Hands-Free Shopping','Run out of an ingredient? Add eggs to my shopping list. Order groceries from Amazon Fresh. What is a substitute for buttermilk?')]),
    ('emergency','Safety','Emergency Voice Commands','uc_emergency',[('When Every Second Matters','In a medical emergency, car accident, or dangerous situation, you may not be able to touch your phone. FoneClaw responds to voice commands instantly.'),('Calling 911','Call 911 connects to emergency services immediately. FoneClaw automatically enables speakerphone and shares your GPS location with the dispatcher.'),('Location Sharing','Send my location to Dad shares precise GPS coordinates via text message. Share my location with all emergency contacts broadcasts to everyone.'),('SOS Messages','I need help, send SOS sends a pre-written emergency message to all designated contacts with your current location, time, and battery level.'),('Medical Information','What is my blood type or I am allergic to penicillin store medical information that FoneClaw can relay to first responders.'),('After an Emergency','FoneClaw logs all emergency actions with timestamps. A long-press of the volume button can trigger a silent SOS if you cannot speak.')]),
    ('productivity','Productivity','Productivity Automation','uc_productivity',[('The Productivity Problem','The average professional switches between 9 apps per task and checks their phone 96 times per day. FoneClaw eliminates most of this friction.'),('Calendar Management','What meetings do I have today reads your schedule. Cancel the 3pm meeting and email the attendees. Schedule a lunch with Sarah for Thursday at noon.'),('Email and Messages','Read my latest emails reads subject lines and senders. Reply to the email from John, say I approve the proposal. Process your inbox while walking.'),('Travel Booking','Find a flight from SFO to JFK next Tuesday morning. Book a hotel near Times Square for 2 nights. What is my gate number?'),('Task Management','Add buy groceries to my to-do list. What tasks are due today? Mark the quarterly report as complete. Integrates with Todoist, Apple Reminders, Google Tasks.'),('Time Savings','Beta users report saving 30+ minutes daily on phone interactions. The biggest gains come from hands-free email processing and automated morning routines.')]),
    ('visual-impaired','Accessibility','Voice for Visually Impaired','uc_visual_impaired',[('The Accessibility Gap','Over 7 million Americans have severe visual impairment. Standard smartphone accessibility requires complex gesture patterns that many users find difficult.'),('Complete Voice Control','Every phone function is accessible by voice: making calls, sending messages, browsing web, using apps, adjusting settings, managing files. No gestures required.'),('Screen Reader Integration','FoneClaw works alongside existing screen readers. It can describe what is on screen, read text aloud, and navigate interfaces by voice.'),('Navigation Assistance','Where am I shares your location. Navigate to the nearest pharmacy opens turn-by-turn directions with audio guidance. Read the street sign uses camera to identify text.'),('Social Connection','Read my WhatsApp messages. Reply to the group chat. Call my sister on video. Stay socially connected without visual barriers.'),('Emergency and Safety','Call 911 works instantly. Send my location to emergency contacts shares GPS coordinates. I am lost, help me navigate home activates navigation.')]),
    ('parenting','Lifestyle','Parenting Hands-Free','uc_parenting',[('The New Parent Reality','New parents have their hands full literally. Holding a baby, preparing bottles, changing diapers there is rarely a free hand for the phone.'),('Communication While Holding Baby','Call my husband. Reply to Mom, say we are doing great. Read my latest messages. Stay connected without putting down your baby.'),('Baby Care Tools','Set a feeding timer. When did I last change the diaper? Play white noise. What is the temperature in the nursery? Track baby care routines by voice.'),('Smart Home for Parents','Dim the nursery lights. Turn on the baby monitor camera. Set the thermostat to 72 degrees. Control smart home without leaving the rocking chair.'),('Emergency Preparedness','Call the pediatrician. What are the symptoms of fever in newborns? Find the nearest urgent care. Quick access when you are panicked and holding a crying baby.'),('Staying Sane','Play my relaxation playlist. Call my best friend. Remind me to take a nap at 2pm. Self-care matters too during the most demanding time of your lives.')]),
    ('fitness','Fitness','Voice-Controlled Fitness','uc_fitness',[('The Hands-Free Workout','When you are running, cycling, or lifting weights, your hands are busy and your phone is in an armband. FoneClaw lets you control everything by voice.'),('Music Control','Next song. Play my running playlist. Volume up. Play something faster. Control Spotify, Apple Music without stopping your workout.'),('Fitness Tracking','What is my current pace? How far have I run? What is my heart rate? Check your workout stats hands-free. Start a new running workout activates tracking.'),('Safety Features','Call 911 if you are injured. Share my location with my running partner. Find the nearest hospital. Works even with heavy breathing and wind noise.'),('Social Fitness','Text my running buddy, say I am 5 minutes away. Post my run to Strava. Call my trainer. Stay connected without interrupting your workout.'),('Workout Recovery','Play my cool-down playlist. Remind me to stretch in 10 minutes. Order a protein shake from DoorDash. Transition from workout to recovery by voice.')]),
    ('vs-siri','Comparison','FoneClaw vs Siri','comp_vs_siri',[('Fundamental Difference','Siri is a voice assistant that answers questions and handles simple commands. FoneClaw is an AI agent that understands intent, executes multi-step tasks, and learns from experience.'),('System Access','Siri operates within Apple sandbox with limited app access. FoneClaw has deep Android system permissions and calls native APIs directly.'),('Multi-Step Tasks','Siri handles one command at a time. Set a timer works. But Find a flight, book it, and remind me does not. FoneClaw decomposes complex requests automatically.'),('Cross-App Capability','Siri cannot pass data between apps. FoneClaw: Check my calendar and text my wife the meeting time requires reading Calendar and writing to Messages.'),('Remote Control','Siri requires the phone to be nearby. FoneClaw can be controlled remotely via Telegram or WhatsApp from any device, anywhere in the world.'),('Verdict','For simple voice commands on iPhone, Siri works fine. For complex phone automation on Android, FoneClaw is in a completely different category.')]),
    ('vs-google','Comparison','FoneClaw vs Google Assistant','comp_vs_google',[('Architecture Difference','Google Assistant is cloud-first: your voice sent to Google servers. FoneClaw is device-first: core processing on your phone. Faster response and better privacy.'),('Task Execution','Google Assistant controls Google apps well but struggles with third-party. FoneClaw has deep integration with 20+ popular apps and growing.'),('Multi-Step Automation','Google Assistant requires Routines to be pre-configured. FoneClaw handles ad-hoc multi-step tasks with no pre-configuration needed.'),('Privacy Model','Google Assistant sends all voice data to cloud. FoneClaw processes locally by default and deletes cloud data instantly after use.'),('Self-Evolution','Google Assistant has fixed capabilities. FoneClaw learns your preferences, routines, and habits. Gets smarter with every interaction.'),('Verdict','Google Assistant is excellent for search and Google ecosystem. FoneClaw excels at cross-app automation, privacy, and personalization.')]),
    ('vs-alexa','Comparison','FoneClaw vs Alexa Mobile','comp_vs_alexa',[('Mobile vs Home','Alexa was designed for smart speakers. Its mobile app is an afterthought. FoneClaw was built mobile-first for the phone in your pocket.'),('Phone Control','Alexa can control smart home but has very limited phone control. It cannot send iMessages, manage calendar, or operate system settings. FoneClaw controls 50+ operations.'),('On-the-Go Usage','Alexa requires internet for everything. FoneClaw handles many operations offline: setting alarms, creating reminders, basic phone operations all work without internet.'),('Third-Party Apps','Alexa has Skills but they are web-based and limited. FoneClaw has native app integrations that actually control the apps on your phone.'),('Driving Scenario','Alexa navigate to nearest gas station requires Alexa Auto hardware. FoneClaw works immediately with Google Maps on your phone. No extra hardware.'),('Verdict','Alexa is great for smart home control via speakers. For mobile phone control, FoneClaw is purpose-built and far more capable.')]),
    ('best-apps','Roundup','Best Voice Control Apps 2026','comp_best_apps',[('The Landscape','Voice control on Android has evolved from simple commands to full AI agents. Here are the top solutions ranked by capability and real-world performance.'),('#1 FoneClaw','The most capable option. System-level AI agent with 50+ operations, multi-step automation, cross-app tasks, remote control, self-evolution. Free beta.'),('#2 Google Assistant','Default choice for basic commands. Excellent Google ecosystem integration. Limitations: no multi-step automation, limited third-party, cloud-dependent.'),('#3 Samsung Bixby','Good Samsung ecosystem integration. Can control Samsung apps and settings. Limitations: Samsung-only, limited third-party, inconsistent accuracy.'),('#4 Amazon Alexa Mobile','Best smart home integration. Controls Alexa-compatible devices. Limitations: poor phone control, requires internet, designed for home use.'),('How to Choose','Basic commands: Google Assistant. Smart home: Alexa. Full phone automation and accessibility: FoneClaw is the clear winner.')]),
    ('ai-replacing','Industry','AI Agents Replacing Assistants','comp_ai_replacing',[('The Evolution','Phone AI went through three generations: simple commands 2011-2018, conversational assistants 2018-2024, autonomous agents 2024 onward.'),('Why Assistants Are Not Enough','Traditional assistants handle one command at a time. Real-world tasks are complex: booking travel involves 5+ apps and 10+ steps.'),('The Agent Advantage','AI agents like FoneClaw understand intent, decompose tasks, manage state across steps, handle errors, and learn from experience.'),('What This Means for Users','Users can finally control phones the way they think: in complete tasks. Plan my business trip instead of 15 manual steps.'),('What This Means for Developers','App developers need to prepare for agent-driven interaction. Apps with clear APIs and structured data will be preferred by AI agents.'),('The Road Ahead','By 2028, analysts predict 60% of smartphone interactions will be agent-driven. The tap-and-swipe era is giving way to speak-and-trust.')]),
]

for aid,cat,title,img_name,sects in articles_data:
    p.append(art(aid,cat,title,img_name,sects))

# ===== JAVASCRIPT =====
trans_json = json.dumps(translations, ensure_ascii=False)
p.append('<script>var T=' + trans_json + ';')
p.append('var CL=localStorage.getItem("foneclaw_lang")||"en";')
p.append('var flags={"en":"\U0001f1fa\U0001f1f8","zh":"\U0001f1e8\U0001f1f3","ja":"\U0001f1ef\U0001f1f5","ko":"\U0001f1f0\U0001f1f7"};')
p.append('var labels={"en":"EN","zh":"\u4e2d\u6587","ja":"\u65e5\u672c\u8a9e","ko":"\ud55c\uad6d\uc5b4"};')
p.append('function setLang(l){CL=l;localStorage.setItem("foneclaw_lang",l);document.getElementById("langDD").classList.remove("open");applyLang();}')
p.append('function applyLang(){document.querySelectorAll("[data-i18n]").forEach(function(el){var k=el.getAttribute("data-i18n");if(T[k]&&T[k][CL])el.textContent=T[k][CL];});document.getElementById("currentFlag").textContent=flags[CL]||"\U0001f1fa\U0001f1f8";document.getElementById("currentLang").textContent=labels[CL]||"EN";}')
p.append('function G(n,sec){hideArticle();for(var i=0;i<4;i++){var p=document.getElementById("p"+i);if(p)p.classList.toggle("on",i===n);var na=document.getElementById("n"+i);if(na)na.classList.toggle("on",i===n);}if(sec){var el=document.getElementById(sec);if(el){setTimeout(function(){var y=el.getBoundingClientRect().top+window.pageYOffset-60;window.scrollTo({top:y,behavior:"smooth"});},200);}}else{window.scrollTo(0,0);}}')
p.append("function TL(){L=(L===\"zh\")?\"en\":\"zh\";document.getElementById(\"lgBtn\").textContent=(L===\"zh\")?\"EN\":\"\\u4e2d\\u6587\";}")
p.append("function showArticle(id){var el=document.getElementById('art-'+id);if(el){el.classList.add('show');document.body.style.overflow='hidden';window.scrollTo(0,0);}}")
p.append("function hideArticle(){document.querySelectorAll('.article-overlay').forEach(function(e){e.classList.remove('show');});document.body.style.overflow='';}")
p.append("document.addEventListener('keydown',function(e){if(e.key==='Escape')hideArticle();});")
p.append("window.addEventListener('scroll',function(){var btn=document.getElementById('backToTop');if(btn){btn.classList.toggle('show',window.scrollY>400);}});")
p.append("applyLang();")
p.append('</script></body></html>')

print("[8/8] Articles + JS done")

# ===== OUTPUT =====
html = '\n'.join(p)
outpath = os.path.join(base, 'index.html')
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"\nGenerated: {outpath}")
print(f"Size: {len(html)} bytes ({len(html)//1024}KB)")
print(f"Chunks: {len(p)}")
print(f"data-i18n markers: {html.count('data-i18n=')}")
print(f"Article overlays: {html.count('class=\"article-overlay\"')}")
