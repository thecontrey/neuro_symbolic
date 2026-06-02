import json, sys
from pathlib import Path

def validate_jsonl(path):
    count = 0
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        json.loads(line)
        count += 1
    return count

if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(p, validate_jsonl(p), "records")
