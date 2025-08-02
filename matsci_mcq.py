# -*- coding: utf-8 -*-
import json
import sys
from docx import Document

# Read filename from command line or use default
if len(sys.argv) < 2:
    print("❌ Please provide a JSON file from the 'resources/' directory.")
    print("Usage: python3 matsci_mcq.py resources/prog_fundamentals.json")
    sys.exit(1)

json_path = sys.argv[1]

# Load JSON data
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

title = data.get("title", "MCQ Test")
file_name = data.get("file_name", "MCQ_Document.docx")
mcq_data = data.get("mcq_data", [])

# Create document
doc = Document()
doc.add_heading(title, level=1)

# Generate MCQs
for idx, mcq in enumerate(mcq_data, 1):
    table = doc.add_table(rows=8, cols=3)
    table.style = 'Table Grid'

    table.cell(0, 0).text = f"Question #{idx}"
    table.cell(0, 1).merge(table.cell(0, 2)).text = mcq["question"]

    table.cell(1, 0).text = "Type"
    table.cell(1, 1).merge(table.cell(1, 2)).text = "multiple_choice"

    for i in range(4):
        table.cell(2 + i, 0).text = "Option"
        table.cell(2 + i, 1).text = mcq["options"][i]
        table.cell(2 + i, 2).text = "correct" if i == mcq["correct"] else "incorrect"

    table.cell(6, 0).text = "Solution"
    table.cell(6, 1).merge(table.cell(6, 2)).text = mcq["solution"]

    table.cell(7, 0).text = "Marks"
    table.cell(7, 1).text = "1"
    table.cell(7, 2).text = "0"

    doc.add_paragraph("")

# Save file
doc.save(file_name)
print(f"✅ Document created successfully: {file_name}")
