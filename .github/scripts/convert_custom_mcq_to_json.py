import sys
import json
import re

def parse_issue_markdown(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]

    data = {
        "file_name": None,
        "mcq_data": []  # changed key name here
    }

    current_question = {}
    current_field = None

    header_pattern = re.compile(r"^###\s+(.*)$")

    for line in lines:
        if not line:
            continue

        m = header_pattern.match(line)
        if m:
            header = m.group(1).strip()

            if header.startswith("Question "):
                if current_question:
                    data["mcq_data"].append(current_question)
                current_question = {
                    "question": "",
                    "options": ["", "", "", ""],
                    "correct": None,
                    "solution": ""
                }
                current_field = "question"
            elif header == "File Name":
                current_field = "file_name"
            elif header.startswith("Option "):
                option_number = int(header.split()[1])
                if 1 <= option_number <= 4:
                    current_field = f"option_{option_number}"
                else:
                    current_field = None
            elif header == "Correct Option":
                current_field = "correct"
            elif header == "Solution":
                current_field = "solution"
            else:
                current_field = None
            continue

        # Value assignment based on current field
        if current_field == "file_name":
            data["file_name"] = line
        elif current_field == "question":
            current_question["question"] = (current_question["question"] + " " + line).strip()
        elif current_field and current_field.startswith("option_"):
            idx = int(current_field.split("_")[1]) - 1
            current_question["options"][idx] = (current_question["options"][idx] + " " + line).strip()
        elif current_field == "correct":
            try:
                val = int(line)
                if 1 <= val <= 4:
                    current_question["correct"] = val
            except ValueError:
                pass
        elif current_field == "solution":
            current_question["solution"] = (current_question["solution"] + " " + line).strip()

    # Append last question if valid
    if current_question:
        data["mcq_data"].append(current_question)

    # Filter out incomplete questions
    data["mcq_data"] = [q for q in data["mcq_data"] if q["question"] and q["correct"] is not None]

    return data

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_github_issue_to_json.py <issue_body_file.md>")
        sys.exit(1)

    filename = sys.argv[1]
    parsed = parse_issue_markdown(filename)

    json_file_name = "questions.json"
    if parsed["file_name"]:
        json_file_name = parsed["file_name"]
        if json_file_name.lower().endswith(".docx"):
            json_file_name = json_file_name[:-5] + ".json"
        else:
            json_file_name = json_file_name + ".json"

    with open(json_file_name, "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=2, ensure_ascii=False)

    print(json_file_name)

if __name__ == "__main__":
    main()
