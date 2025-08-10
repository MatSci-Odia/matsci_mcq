import json
import os
import re
import sys

# Load GitHub issue JSON (assuming the file 'issue.json' exists)
with open("issue.json", "r") as f:
    issue = json.load(f)

body = issue.get("body", "")

# Extract the file name (after ### File Name)
file_name_match = re.search(r"### File Name\s+([^\n]+)", body)
if not file_name_match:
    print("❌ File name not found")
    sys.exit(1)
file_name = file_name_match.group(1).strip()

# Find all questions blocks by splitting on '### Question ' followed by a number
question_splits = re.split(r"### Question \d+\s*", body)[1:]  # first split is before Question 1, so skip it

mcq_data = []

for q_block in question_splits:
    # Extract question text (up to next ### Option 1)
    question_match = re.match(r"(.*?)\s+### Option 1\s+", q_block, re.DOTALL)
    if not question_match:
        print("❌ Question text not found or badly formatted.")
        sys.exit(1)
    question_text = question_match.group(1).strip()

    # Extract options
    options = []
    for i in range(1, 5):
        opt_match = re.search(rf"### Option {i}\s+(.*?)(?:\s+### Option {i+1}|### Correct Option|### Solution|$)", q_block, re.DOTALL)
        if opt_match:
            opt_text = opt_match.group(1).strip().replace("&nbsp;", " ").replace("\n", " ").strip()
            options.append(opt_text)
        else:
            options.append("")  # if missing option

    # Extract correct option number
    correct_match = re.search(r"### Correct Option\s+(\d+)", q_block)
    if not correct_match:
        print("❌ Correct option not found.")
        sys.exit(1)
    correct_option = int(correct_match.group(1))

    # Extract solution text
    solution_match = re.search(r"### Solution\s+(.*?)(?=### Question \d+|$)", q_block, re.DOTALL)
    if not solution_match:
        print("❌ Solution not found.")
        sys.exit(1)
    solution_text = solution_match.group(1).strip().replace("&nbsp;", " ").replace("\n", " ").strip()

    mcq_data.append({
        "question": question_text,
        "options": options,
        "correct": correct_option,
        "solution": solution_text
    })

# Prepare final JSON
final_json = {
    "file_name": file_name,
    "mcq_data": mcq_data
}

# Make sure output folder exists
os.makedirs("resources", exist_ok=True)

# Save JSON file with name based on file_name (replace .docx with .json)
json_filename = file_name.replace(".docx", ".json")
output_path = os.path.join("resources", json_filename)

with open(output_path, "w") as out_f:
    json.dump(final_json, out_f, indent=2)

print(f"✅ Saved parsed MCQ JSON to: {output_path}", file=sys.stderr)
print(output_path)  # For GitHub Actions output capture
sys.stdout.flush()
