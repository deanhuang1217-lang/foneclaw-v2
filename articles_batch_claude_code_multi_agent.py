import json, os

base = os.path.dirname(__file__)
data_file = os.path.join(base, 'batch_claude_code_multi_agent_data.json')
with open(data_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

if isinstance(data, dict):
    data = [data]

BATCH = []
for article in data:
    BATCH.append((
        article['slug'],
        article['title'],
        article['meta'],
        article['category'],
        article['read_time'],
        [(s['subtitle'], s['body']) for s in article['sections']]
    ))
