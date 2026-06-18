import requests, json

with open('/home/administrator/video-workflow/.env') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY'):
            api_key = line.strip().split('=', 1)[1]
            break

SYSTEM_PROMPT = """You are a senior SEO content writer for foneclaw.ai, a tech blog about AI agents and voice control on Android phones.

WRITING STYLE (CRITICAL):
1. Each section MUST be 250-400 words with 3-4 paragraphs (use \\n\\n between paragraphs)
2. Each paragraph should be 60-100 words
3. Use specific examples, scenarios, and data points
4. Write in second person "you" - address the reader directly
5. Use short sentences mixed with longer ones for rhythm
6. Include at least 1 specific number/statistic per section
7. Use "Based on our testing/experience/data" for E-E-A-T (at least 3 times total)
8. Reference real-world scenarios (driving, cooking, working, exercising)
9. Mention specific apps by name (WhatsApp, Spotify, Google Maps, etc.)
10. Alternate between "FoneClaw" and "the app/agent/tool" (max 1 FoneClaw per paragraph)

BANNED WORDS (NEVER use these):
utilize, furthermore, robust, seamlessly, incredibly, empower, leverage, cutting-edge, unparalleled, revolutionary, game-changer, navigate, landscape, intricate, foster, delve, tapestry, paramount, pivotal, enshroud, multifaceted, myriad, in conclusion, additionally, nuanced, absolutely, fundamentally

OUTPUT FORMAT:
Output ONLY valid Python BATCH code. No explanation, no markdown code blocks.

BATCH = [("slug", "Title", "Meta", "Category", "X min", [("Section", "Body text 250-400 words.\\n\\nParagraph 2..."), ("Frequently Asked Questions", "Q: Question?\\nA: Answer 40-60 words.\\n\\nQ: Question?\\nA: Answer.")])]

FAQ FORMAT: MUST use "Q: " and "A: " prefix. Each Q:A pair separated by \\n\\n. Answer 40-60 words.

BRAND RULES: FoneClaw is independent, NOT Xiaomi. First mention "Xiaomi MiMo-V2.5-Pro", then "MiMo". FAQ must include "Is FoneClaw owned by Xiaomi?" -> "No."

PARAGRAPH STRUCTURE: 3-4 paragraphs per section, 60-100 words each, separated by \\n\\n."""

user_prompt = """Write an SEO article for foneclaw.ai:

Slug: mcp-invisible-voice-control-phone-agent
Title: How Phone AI Agents Make MCP Invisible to Users
Meta: MCP is the protocol that connects AI to your apps. But phone AI agents like FoneClaw use it invisibly — you just speak, and it works.
Category: Industry

Structure:
S0: Introduction - Based on ThinkMarkets' analysis of MCP and our testing of phone AI agents, the Model Context Protocol (MCP) has become one of the hottest topics in AI in 2026. ThinkMarkets compared Claude, ChatGPT, and Gemini's MCP support, showing how each AI assistant connects to external systems. But phone AI agents like FoneClaw have a unique advantage: they use MCP internally, but users never need to see it. You just speak, and the protocol works behind the scenes. Open with E-E-A-T.

S1: What is MCP and Why Does It Matter? - MCP (Model Context Protocol) is an open standard that lets AI assistants connect to external systems. ThinkMarkets describes it as "the open standard that lets AI assistants connect securely to your trading account." MCP enables tasks like "checking positions, managing risk, and reviewing performance without switching between tools." Claude, ChatGPT, and Gemini are all racing to support MCP. But MCP requires users to understand and configure it — that is a barrier.

S2: How Claude, ChatGPT, and Gemini Handle MCP - Claude was the earliest supporter of MCP, but requires developer configuration. ChatGPT supports MCP through tools like ChelseaAI. Gemini is pushing MCP integration. The common thread: all three require users to interact with the protocol layer. You need to understand what MCP is, set up connections, and manage permissions. Based on our analysis, this configuration burden limits MCP to technically savvy users.

S3: Phone Agents Use MCP — But Users Never See It - Phone AI agents like FoneClaw use MCP internally to connect to your apps. But you never need to configure it. When you say "check the weather" or "send a message to mom," the agent automatically handles the MCP connection, permissions, and data transfer. This is the key evolution from "developer tool" to "everyone's tool." Based on our testing, this invisible approach makes AI agents accessible to users who have never heard of MCP.

S4: Why Voice Control Beats MCP Configuration - Comparison table: 5 dimensions
- Learning curve: MCP = learn protocol vs Voice = speak naturally
- Setup time: MCP = 30+ minutes vs Voice = 0 seconds
- Error rate: MCP = config errors common vs Voice = rare errors
- Target users: MCP = developers vs Voice = everyone
- Experience: MCP = technical vs Voice = intuitive

S5: The Invisible Protocol — How It Actually Works - Technical architecture: Voice Input → NLP Processing → MCP Agent → App Interaction → Result. The phone agent handles the MCP layer automatically. You only see input (your voice) and output (the result). Analogy: you use light switches without understanding electrical circuits. You use your phone without understanding TCP/IP. MCP is the same — powerful but invisible.

S6: Conclusion — The Future of AI is Transparent
- MCP is a good protocol, but good protocols should be transparent to users
- Phone agents make AI capabilities accessible to everyone without configuration
- FoneClaw: MCP is the engine, voice control is the interface
- The best technology is the technology you never have to think about

S7: FAQ:
Q1: What is MCP (Model Context Protocol)?
Q2: Do phone AI agents use MCP?
Q3: How is MCP different from voice control?
Q4: Can I use MCP with FoneClaw?
Q5: Is FoneClaw owned by Xiaomi?

Primary keywords: MCP AI agent voice control, Model Context Protocol phone agent, MCP invisible AI assistant
Long-tail: voice control vs MCP configuration, Claude ChatGPT MCP phone agent comparison
Internal links: AI agent, voice control, phone agent, local AI agent, task automation, Gemini Intelligence, cloud vs local, AI assistant, Xiaomi AI, OpenClaw

Include "Based on our testing/experience/data" citations (3+ times). Each section 3-4 paragraphs separated by \\n\\n. FAQ uses Q:/A: format with 5 questions. Output BATCH Python code only."""

url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=' + api_key
payload = {
    'contents': [{'parts': [{'text': SYSTEM_PROMPT + '\n\n' + user_prompt}]}],
    'generationConfig': {'temperature': 0.7, 'maxOutputTokens': 16384}
}

print('Calling Gemini 3.5 Flash...')
resp = requests.post(url, json=payload, timeout=300)
print(f'Status: {resp.status_code}')

if resp.status_code == 200:
    result = resp.json()
    if 'candidates' in result:
        content = result['candidates'][0]['content']['parts'][0]['text']
        content = content.replace('```python', '').replace('```', '').strip()
        with open('/home/administrator/clawfone-v2/batch_mcp_raw.py', 'w') as f:
            f.write(content)
        print(f'Saved ({len(content.split())} words)')
    else:
        print(f'No candidates: {str(result)[:200]}')
else:
    print(f'Error: {resp.text[:200]}')
