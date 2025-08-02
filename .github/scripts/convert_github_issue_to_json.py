import json
import os

# Load GitHub issue JSON
with open("issue.json", "r") as f:
    issue = json.load(f)

title = issue.get("title", "")
body = issue.get("body", "")

# Function to extract values from the issue body using simple markers
def extract_marker(field):
    start_tag = f"{field}:"
    start_index = body.find(start_tag)
    if start_index == -1:
        return ""
    start_index += len(start_tag)
    end_index = body.find("\n", start_index)
    return body[start_index:end_index].strip()

# Alternatively, just extract JSON array using triple-backtick boundaries
import re
mcq_json_match = re.search(r"```json(.*?)```", body, re.DOTALL)
if not mcq_json_match:
    print("❌ MCQ JSON array not found in issue body.")
    exit(1)

try:
    mcq_data = json.loads(mcq_json_match.group(1).strip())
except json.JSONDecodeError as e:
    print("❌ Failed to parse MCQ JSON array:", e)
    exit(1)

# Extract filename and normalize
file_name_match = re.search(r"File Name:(.*?)\n", body)
file_name = file_name_match.group(1).strip() if file_name_match else "mcq_test.docx"

# Extract title (optional use, not needed for saving)
title_match = re.search(r"Test Title:(.*?)\n", body)
test_title = title_match.group(1).strip() if title_match else "MCQ Test"

# Write the MCQ JSON to a file
os.makedirs("resources", exist_ok=True)
output_path = os.path.join("resources", file_name.replace(".docx", ".json"))

with open(output_path, "w") as out_file:
    json.dump(mcq_data, out_file, indent=2)

print(f"✅ Saved MCQ test to {output_path}")
