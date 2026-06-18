# Xiaomi Phone Agent Summit - Batch Loader
import json
import os

base = os.path.dirname(__file__)
data_file = os.path.join(base, 'batch_xiaomi_summit_data.json')

with open(data_file, 'r') as f:
    data = json.load(f)

BATCH = [(
    data['slug'],
    data['title'],
    data['desc'],
    data['cat'],
    data['rt'],
    [(s['subtitle'], s['body']) for s in data['sections']]
)]
