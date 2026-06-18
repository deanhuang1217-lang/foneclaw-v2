import os, subprocess

api_key = None
with open('/home/administrator/video-workflow/.env') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY'):
            api_key = line.split('=', 1)[1].strip()
            break

os.environ['GEMINI_API_KEY'] = api_key

prompt = "Premium subscription concept, golden crown above smartphone with AI brain, monthly payment symbol, blue and gold gradient, modern tech illustration, clean minimal design, 16:9 aspect ratio"

result = subprocess.run([
    'uv', 'run', os.path.expanduser('~/.hermes/skills/openclaw-imports/nano-banana-pro/scripts/generate_image.py'),
    '--prompt', prompt,
    '--filename', 'images/articles/apple-intelligence-pro-subscription-what-to-expect.jpg',
    '--resolution', '1K',
    '--aspect-ratio', '16:9'
], capture_output=True, text=True, timeout=120, cwd='/home/administrator/clawfone-v2')

print(result.stdout[:500])
print("Return code:", result.returncode)
