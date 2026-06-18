import json, os
base = os.path.dirname(__file__)
with open(os.path.join(base, 'batch_foneclaw_vs_nebula_ai_data.json'), 'r') as f:
    data = json.load(f)
BATCH = [(data['slug'], data['title'], data['desc'], data['cat'], data['rt'], [(s['subtitle'], s['body']) for s in data['sections']])]
