import json, os
base = os.path.dirname(__file__)
data_file = os.path.join(base, 'batch_workbuddy_data.json')
with open(data_file, 'r') as f:
    data = json.load(f)
BATCH = [(
    data[0]['slug'], data[0]['title'], data[0]['meta'], data[0]['category'], data[0]['rt'],
    [(s['subtitle'], s['body']) for s in data[0]['sections']]
)]
