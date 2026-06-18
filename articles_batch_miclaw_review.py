# batch_miclaw_review - Xiaomi MiClaw User Review Analysis
import json
import os

_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_dir, "batch_xiaomi_miclaw_user_review_data.json"), encoding="utf-8") as _f:
    _data = json.load(_f)

BATCH = [(
    _d["slug"],
    _d["title"],
    _d["meta"],
    _d["cat"],
    _d["rt"],
    [(s["subtitle"], s["body"]) for s in _d["sections"]]
) for _d in _data]
