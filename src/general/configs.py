import json
from pathlib import Path

def load_config(path):
    path = Path(path)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
