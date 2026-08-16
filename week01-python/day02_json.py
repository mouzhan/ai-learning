import json
from pathlib import Path

path = Path("data/sample.json")

with path.open("r",encoding="utf-8") as f:
    data = json.load(f)


print(data)
print("--------------------------------")
print(data["project"])
print("--------------------------------")
print(data["bugs"])