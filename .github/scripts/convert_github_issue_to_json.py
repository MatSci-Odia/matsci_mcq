import json
import os
import re
import sys

# Load GitHub issue JSON
with open("issue.json", "r") as f:
    issue = json.load(f)

body = issue.get("body", "")

# --- Extract title ---
title_match = re.search(r"### Test Title\s+([^\n]+)", body)
title_value = title_match.group(1).strip() if title_match else ""

# --- Extract file name ---
file_match = re.search(r"### File Name\s+([^\n]+)", body)
file_value = file_match.group(1).strip() if file_match else ""

# --- Extract MCQ JSON array ---
mcq_match = re.search(r"```json(.*?)```", body, re.DOTALL)
if not mcq_match:
    print("❌ MCQ JSON array not found in issue body.")
    exit(1)

try:
    mcq_data = json.loads(mcq_match.group(1).strip())
except json.JSONDecodeError as e:
    print("❌ Failed to parse MCQ JSON array:", e)
    exit(1)

# --- Final object ---
final_data = {
    "title": title_value,
    "file_name": file_value,
    "mcq_data": mcq_data
}

# Ensure folder exists
os.makedirs("resources", exist_ok=True)

# Save JSON
output_path = os.path.join("resources", file_value.replace(".docx", ".json"))
with open(output_path, "w") as out_file:
    json.dump(final_data, out_file, indent=2)

# Log to stderr for humans
print(f"✅ Saved MCQ test to {output_path}", file=sys.stderr)
print(output_path)
sys.stdout.flush()
