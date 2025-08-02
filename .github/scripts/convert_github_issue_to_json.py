# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

with open(sys.argv[1], 'r') as f:
    event = json.load(f)

issue = event["issue"]
title = issue["title"]
body = issue["body"]

# Simple parser to split question and options (you can improve this logic)
lines = body.strip().split("\n")
question = lines[0]
options = [line.strip("- ").strip() for line in lines[1:5]]
correct = int(lines[5].split(":")[1].strip())
solution = lines[6].split(":")[1].strip()

data = {
    "question": question,
    "options": options,
    "correct": correct,
    "solution": solution
}

out_path = Path("resources") / f"{title.lower().replace(' ', '_')}.json"
out_path.parent.mkdir(exist_ok=True)
with open(out_path, "w") as out:
    json.dump([data], out, indent=2)

print(f"Saved question to {out_path}")
