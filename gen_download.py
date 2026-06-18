#!/usr/bin/env python3
"""Generate download.html for FoneClaw"""
import pickle, os

base = '/home/administrator/clawfone-v2'
cache = pickle.load(open(os.path.join(base, '_build_cache.pkl'), 'rb'))
icon_b64 = cache['icon_b64']
imgs = cache['imgs']

with open(os.path.join(base, '_style.css')) as f:
    CSS = f.read()

# Reuse build_multi helpers
exec(open(os.path.join(base, 'build_multi.py')).read().split('# ===== URL MAP =====')[0])

html = []
html.append(head('Download FoneClaw - AI Voice Agent for Android',
    'Download FoneClaw, the AI agent that controls your Android phone by voice. Free for core features.',
    '/download.html'))
html.append(nav(-1))
html.append('<main>')

# Hero section
html.append('''
<section style="padding:120px 0 60px;text-align:center;background:linear-gradient(180deg,#080c18 0%,#0b1a3a 50%,#080c18 100%)">
<div class="wrap">
<h1 style="font-size:clamp(32px,5vw,48px);font-weight:700;margin-bottom:16px;color:#f0f4f8">
<span style="color:#00d4ff">Download</span> FoneClaw
</h1>
<p style="color:#8b949e;font-size:18px;max-width:520px;margin:0 auto 40px;line-height:1.7">
Free forever for core features.<br>No credit card required.
</p>
</div>
</section>
''')

# Download cards
html.append('''
<section style="padding:0 0 80px">
<div class="wrap" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;max-width:800px;margin:0 auto">

<!-- Android Card -->
<div style="background:#0d1117;border:1px solid #1a2332;border-radius:16px;padding:40px 28px;text-align:center;position:relative;overflow:hidden">
<div style="font-size:48px;margin-bottom:16px">🤖</div>
<h2 style="font-size:22px;margin-bottom:8px;color:#f0f4f8">Android</h2>
<p style="color:#8b949e;font-size:14px;margin-bottom:24px;line-height:1.6">
System-level AI agent for Android 10+. Voice control, cross-app automation, memory learning.
</p>
<div style="background:rgba(255,255,255,.04);border:1px dashed #21262d;border-radius:12px;padding:24px;margin-bottom:20px">
<p style="color:#6e7681;font-size:13px;margin-bottom:4px">Coming Soon</p>
<p style="color:#484f58;font-size:12px">APK Download • Google Play</p>
</div>
<a href="/early-access.html" style="display:inline-block;width:100%;padding:14px;background:linear-gradient(135deg,#3fb950,#2ea043);color:#080c18;font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:15px;border-radius:10px;text-decoration:none;box-shadow:0 4px 16px rgba(63,185,80,.3)">Get Early Access</a>
</div>

<!-- System Requirements -->
<div style="background:#0d1117;border:1px solid #1a2332;border-radius:16px;padding:40px 28px;text-align:center">
<div style="font-size:48px;margin-bottom:16px">⚙️</div>
<h2 style="font-size:22px;margin-bottom:8px;color:#f0f4f8">System Requirements</h2>
<p style="color:#8b949e;font-size:14px;margin-bottom:24px;line-height:1.6">
Make sure your device meets these requirements before downloading.
</p>
<div style="text-align:left;padding:0 8px">
<div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid #1a2332">
<span style="color:#3fb950">✓</span><span style="color:#c9d1d9;font-size:14px">Android 10.0 or higher</span>
</div>
<div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid #1a2332">
<span style="color:#3fb950">✓</span><span style="color:#c9d1d9;font-size:14px">3GB RAM minimum</span>
</div>
<div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid #1a2332">
<span style="color:#3fb950">✓</span><span style="color:#c9d1d9;font-size:14px">100MB storage space</span>
</div>
<div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid #1a2332">
<span style="color:#3fb950">✓</span><span style="color:#c9d1d9;font-size:14px">Microphone permission</span>
</div>
<div style="display:flex;align-items:center;gap:10px;padding:10px 0">
<span style="color:#3fb950">✓</span><span style="color:#c9d1d9;font-size:14px">Accessibility Service access</span>
</div>
</div>
</div>

</div>
</section>
''')

# FAQ section
html.append('''
<section style="padding:60px 0 80px;background:linear-gradient(180deg,#080c18 0%,#0b1a3a 50%,#080c18 100%)">
<div class="wrap" style="max-width:680px">
<h2 style="font-size:24px;text-align:center;margin-bottom:32px;color:#f0f4f8">Frequently Asked Questions</h2>
''')

faqs = [
    ('Is FoneClaw really free?', 'Yes. Core features are free forever. We may offer a Pro plan with advanced features in the future, but the core voice agent, basic automation, and system controls will always be free.'),
    ('Does it work on all Android phones?', 'FoneClaw requires Android 10 or higher with at least 3GB of RAM. It works on most modern Android devices including Samsung, Google Pixel, OnePlus, and Xiaomi phones.'),
    ('Is my data safe?', 'Absolutely. FoneClaw processes everything locally on your device. Your voice commands, contacts, and personal data never leave your phone unless you explicitly enable cloud sync.'),
    ('When will it be available?', 'We are launching soon! Sign up for early access to be notified as soon as FoneClaw is ready for download.'),
]

for q, a in faqs:
    html.append(f'''
    <details style="margin-bottom:12px;background:#0d1117;border:1px solid #1a2332;border-radius:10px;padding:0;overflow:hidden">
    <summary style="padding:16px 20px;cursor:pointer;font-family:'Space Grotesk',sans-serif;font-weight:600;color:#f0f4f8;font-size:15px;list-style:none;display:flex;justify-content:space-between;align-items:center">
    {q}<span style="color:#6e7681;font-size:18px">+</span>
    </summary>
    <div style="padding:0 20px 16px;color:#8b949e;font-size:14px;line-height:1.7">{a}</div>
    </details>
    ''')

html.append('</div></section>')

# CTA
html.append('''
<section style="padding:60px 0;text-align:center">
<div class="wrap">
<h2 style="font-size:clamp(22px,3vw,30px);margin-bottom:12px;color:#f0f4f8">Ready to go hands-free?</h2>
<p style="color:#8b949e;font-size:16px;margin-bottom:28px">Join the waitlist and be the first to try FoneClaw.</p>
<a href="/early-access.html" style="display:inline-block;padding:14px 36px;background:linear-gradient(135deg,#3fb950,#2ea043);color:#080c18;font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:16px;border-radius:10px;text-decoration:none;box-shadow:0 4px 16px rgba(63,185,80,.3)">Get Early Access</a>
</div>
</section>
''')

html.append('</main>')
html.append(footer())
html.append(js('{}'))
html.append('</body></html>')

with open(os.path.join(base, 'download.html'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(html))
print(f"download.html: {len(''.join(html))//1024}KB")
