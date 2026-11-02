import json
import urllib.request
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
print(f"Project root: {project_root}")
profile_path =  project_root /  "profile.txt"

profile_text = profile_path.read_text(encoding="utf-8")

profile_text_dumped = json.dumps({"text": profile_text}).encode("utf-8")

request = urllib.request.Request(
    "http://localhost:8000/profile/extract",
    data=profile_text_dumped,
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))

print(json.dumps(result, indent=4, ensure_ascii=False))


