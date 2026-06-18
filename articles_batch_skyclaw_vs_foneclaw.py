import json, os
base = os.path.dirname(__file__)
with open(os.path.join(base, 'batch_skyclaw_vs_foneclaw_data.json'), 'r') as f:
    data = json.load(f)
BATCH = [(data['slug'], data['title'], data['desc'], data['cat'], data['rt'], [(s['subtitle'], s['body']) for s in data['sections']])]
