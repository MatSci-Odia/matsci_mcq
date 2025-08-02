import json
import os
import re

with open("issue.json", "r") as f:
    issue = json.load(f)

title = issue["title"]
body = issue["body"]

def extract(field):
    match = re.search(f"{field}:(.*?)\n", body + "\n", re.DOTALL)
    return match.group(1).strip() if match else ""

question_type = extract("Type of Question")
question = extract("Question")
options = extract("Options").splitlines()
correct = extract("Correct Option Number")
solution = extract("Solution")
file_title = extract("Title (Filename)").replace(" ", "_").lower()

output = {
    "type": question_type,
    "question": question,
    "options": options if question_type == "MCQ" else [],
    "answer": int(correct) if correct.isdigit() else None,
    "solution": solution,
}

# Save to file
os.makedirs("resources", exist_ok=True)
with open(f"resources/{file_title}.json", "w") as out_file:
    json.dump(output, out_file, indent=2)

print(f"✅ Question saved to resources/{file_title}.json")
