import os, subprocess

# 读取API Key
api_key = None
with open('/home/administrator/video-workflow/.env') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY'):
            api_key = line.split('=', 1)[1].strip()
            break

os.environ['GEMINI_API_KEY'] = api_key

# 生成首图
prompt = "Modern smartphone with app icons floating and connecting to an AI brain symbol, digital neural network lines, blue and purple gradient, tech futuristic style, clean minimal design, 16:9 aspect ratio"

result = subprocess.run([
    'uv', 'run', os.path.expanduser('~/.hermes/skills/openclaw-imports/nano-banana-pro/scripts/generate_image.py'),
    '--prompt', prompt,
    '--filename', 'images/articles/app-intents-apps-machine-callable-ai-agents.jpg',
    '--resolution', '1K',
    '--aspect-ratio', '16:9'
], capture_output=True, text=True, timeout=120, cwd='/home/administrator/clawfone-v2')

print("STDOUT:", result.stdout[:500])
print("STDERR:", result.stderr[:500])
print("Return code:", result.returncode)
