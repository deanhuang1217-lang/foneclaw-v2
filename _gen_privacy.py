#!/usr/bin/env python3
"""Generate privacy policy page for FoneClaw."""
import os

base = '/home/administrator/clawfone-v2'

# Read existing build helpers
exec(open(os.path.join(base, 'build_multi.py')).read().split('# ----- ARTICLE PAGES -----')[0])

html = []
html.append(head('Privacy Policy - FoneClaw', 'FoneClaw privacy policy. How we collect, use, and protect your data. Your voice data stays on device.', '/privacy.html'))
html.append(nav(-1))
html.append('<div class="reading-progress" id="readProgress"></div>')
html.append('<main><div class="art-wrap">')

# Breadcrumb
html.append('<div class="breadcrumb"><a href="/">Home</a><span class="sep">\u203a</span><span>Privacy Policy</span></div>')

# Header
html.append('<header class="art-header">')
html.append('<div class="cat">Legal</div>')
html.append('<div class="meta-row"><span>\U0001f4c5 May 9, 2026</span><span>\u23f1\ufe0f 5 min read</span></div>')
html.append('<h1>Privacy Policy</h1>')
html.append('<p class="art-desc">How FoneClaw collects, uses, and protects your personal information.</p>')
html.append('</header>')

# Content
sections = [
    ('Information We Collect', 'FoneClaw collects minimal data necessary to provide voice-controlled phone automation. This includes: voice commands processed locally on your device, app usage patterns stored only on your device for learning preferences, and optional cloud processing data that is encrypted and deleted immediately after use. We do not collect browsing history, contacts, or message content.'),
    ('How We Use Your Information', 'Your data is used solely to provide and improve FoneClaw services. Voice commands are processed to execute phone operations. Usage patterns help FoneClaw learn your preferences and improve accuracy over time. All learning data is stored locally on your device. Cloud-processed data is used only for real-time command execution and is never stored permanently.'),
    ('Data Storage and Security', 'FoneClaw stores user preferences, voice profiles, and learning data locally on your device using Android secure storage. Cloud processing uses end-to-end encryption. Data transmitted to cloud servers is deleted immediately after processing. We use industry-standard TLS 1.3 encryption for all data in transit. No data is sold to third parties.'),
    ('Voice Data Privacy', 'Your voice recordings are processed locally by default. Wake word detection runs entirely on-device. Cloud voice processing (when enabled) encrypts audio before transmission and deletes it immediately after transcription. We never store voice recordings. Voice profiles used for speaker identification are stored only on your device.'),
    ('Third-Party App Integration', 'FoneClaw integrates with third-party apps (iMessage, Amazon, DoorDash, Google Maps, Spotify, Uber) through Android Accessibility Service. FoneClaw does not share your data with these apps beyond what is necessary to execute your commands. Each app integration follows that app\'s own privacy policy for the data it receives.'),
    ('Remote Control via Telegram/WhatsApp', 'When you connect FoneClaw to Telegram or WhatsApp for remote control, message data is processed through those platforms\' own encryption. FoneClaw does not store Telegram or WhatsApp message history. Remote commands are processed in real-time and not logged.'),
    ('Children\'s Privacy', 'FoneClaw is not intended for children under 13. We do not knowingly collect personal information from children. If you believe a child has provided us with personal information, please contact us immediately and we will delete it.'),
    ('Your Rights', 'You have the right to: access all data FoneClaw stores about you (all stored locally on your device), delete all stored data through the app settings, opt out of cloud processing at any time, export your preferences and learning data. Since data is stored locally, you have full control over your information.'),
    ('Changes to This Policy', 'We may update this privacy policy from time to time. We will notify you of any changes through the FoneClaw app. Continued use of FoneClaw after changes constitutes acceptance of the updated policy.'),
    ('Contact Us', 'If you have questions about this privacy policy or FoneClaw\'s data practices, please contact us through our community channels at foneclaw.ai/community or via email at privacy@foneclaw.ai.'),
]

html.append('<div class="art-body">')
for sub, body in sections:
    slug = sub.lower().replace(' ', '-').replace("'", '')
    html.append(f'<h2 id="{slug}"><a class="anchor" href="#{slug}" aria-label="Link to {sub}"></a>{sub}</h2>')
    html.append(f'<p>{body}</p>')
html.append('</div>')

html.append('</div></main>')
html.append(footer())
html.append(js({}))
html.append('</body></html>')

with open(os.path.join(base, 'privacy.html'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(html))
print("privacy.html created")
