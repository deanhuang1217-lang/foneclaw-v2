import requests, json

with open('/home/administrator/video-workflow/.env') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY'):
            api_key = line.strip().split('=', 1)[1]
            break

SYSTEM_PROMPT = """You are an SEO writer. Output ONLY Python BATCH code. No explanation, no thinking, no markdown. Just the code.

BATCH format:
BATCH = [("slug", "Title", "Meta 120-160 chars", "Category", "X min", [("Section Title", "Body 250-400 words with \\n\\n paragraphs"), ...])]

Rules:
- 8 sections total (7 content + 1 FAQ)
- Each section 3-4 paragraphs, 60-100 words each, separated by \\n\\n
- FAQ uses Q:/A: format, 5 questions
- No banned words: utilize, furthermore, robust, seamlessly, incredibly, empower, leverage, cutting-edge, unparalleled, revolutionary, game-changer, navigate, landscape, intricate, foster, delve, tapestry, paramount, pivotal, enshroud, multifaceted, myriad, additionally, nuanced, absolutely, fundamentally
- Use "Based on our testing/experience" for E-E-A-T (3+ times)
- Write in second person "you"
- Mention FoneClaw max 1 time per paragraph"""

user_prompt = """Write BATCH code for foneclaw.ai:

Slug: mcp-invisible-voice-control-phone-agent
Title: How Phone AI Agents Make MCP Invisible to Users
Meta: MCP connects AI to apps. Phone AI agents like FoneClaw use it invisibly — you just speak, and it works.
Category: Industry

Sections:
S0: Intro - Based on ThinkMarkets analysis of MCP and our testing, MCP (Model Context Protocol) is the hottest AI topic in 2026. Claude, ChatGPT, Gemini all support it. But phone agents use MCP invisibly. Open with E-E-A-T.

S1: What is MCP - Open standard for AI to connect to external systems. Enables checking positions, managing risk. ThinkMarkets calls it "the open standard for secure AI-trading connections."

S2: Claude ChatGPT Gemini MCP support - Claude earliest but needs config. ChatGPT via ChelseaAI. Gemini pushing integration. All require users to interact with protocol layer.

S3: Phone agents use MCP invisibly - FoneClaw uses MCP internally but users never configure it. Say "check weather" and agent handles MCP automatically. Key evolution from developer tool to everyone's tool.

S4: Voice vs MCP config - Comparison table: learning curve, setup time, error rate, target users, experience. Voice wins on all dimensions.

S5: How it works - Voice → NLP → MCP Agent → App → Result. Like using light switch without understanding circuits.

S6: Conclusion - MCP is good but should be transparent. Phone agents make AI accessible. FoneClaw: MCP is engine, voice is interface.

S7: FAQ - What is MCP? Do phone agents use MCP? How is MCP different from voice control? Can I use MCP with FoneClaw? Is FoneClaw owned by Xiaomi?

Primary: MCP AI agent voice control, Model Context Protocol phone agent, MCP invisible AI assistant
Internal: AI agent, voice control, phone agent, local AI agent, task automation, Gemini Intelligence, cloud vs local, AI assistant, Xiaomi AI, OpenClaw

Output BATCH Python code only. No explanation."""

url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={api_key}'
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
        # Remove any thinking/reasoning text before BATCH
        batch_start = content.find('BATCH')
        if batch_start > 0:
            content = content[batch_start:]
        with open('/home/administrator/clawfone-v2/batch_mcp_raw.py', 'w') as f:
            f.write(content)
        print(f'Saved ({len(content.split())} words)')
    else:
        print(f'No candidates: {str(result)[:200]}')
else:
    print(f'Error: {resp.text[:200]}')
