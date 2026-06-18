import json, os
_dir = os.path.dirname(os.path.abspath('batch6'))
with open(os.path.join(_dir, "batch6_data.json"), encoding="utf-8") as _f:
    _data = json.load(_f)
BATCH = [(_d["id"], _d["title"], _d["desc"], _d["cat"], _d["rt"],
          [(s["subtitle"], s["body"]) for s in _d["sections"]],
          _d.get("share_text", "")) for _d in _data]
