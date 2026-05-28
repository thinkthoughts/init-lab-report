import json
from pathlib import Path

def save_markdown_report(path, title, lines):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    content = [f"# {title}\n"]
    content.extend([f"- {line}\n" for line in lines])

    path.write_text("".join(content), encoding="utf-8")

def save_json_result(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8"
    )
