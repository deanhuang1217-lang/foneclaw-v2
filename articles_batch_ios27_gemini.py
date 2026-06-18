# iOS 27 Siri Gemini Integration - Batch Loader
import json, os
base = os.path.dirname(__file__)
data_file = os.path.join(base, 'batch_ios27_gemini_data.json')
with open(data_file, 'r') as f:
    data = json.load(f)
BATCH = [(
    data['slug'], data['title'], data['desc'], data['cat'], data['rt'],
    [(s['subtitle'], s['body']) for s in data['sections']]
)]
