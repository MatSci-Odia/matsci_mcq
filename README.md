# Matsci MCQ and Subjective Test Generator

This project generates MCQ and Subjective tests using Python and Word documents, and integrates with GitHub Actions to automate document generation, issue creation, and artifact uploading.

---

## 🛠️ Steps to Execute Locally (for Developers)

To generate the MCQ document:

```bash
python3 matsci_mcq.py resources/<file_name>
```

To generate the Subjective test document:

```bash
python3 subjective_test.py resources/<file_name>
```

---

## ✍️ How to Add/Update Questions (for Admin/Teachers)

### For MCQs

Update the JSON file in the `resources` directory (e.g., `resources/mcq_questions.json`) with entries in the following format:

```json
{
  "title": "Programming Basics - MCQ Test",
  "file_name": "programming_basics_mcq",
  "questions": [
    {
      "question": "Which of the following is a valid variable name in Java?",
      "options": ["2value", "value$", "int", "void"],
      "correct": 2,
      "solution": "Variable names cannot start with numbers or be keywords. 'value$' is valid."
    }
  ]
}
```

- The `options` list must contain exactly 4 strings.
- The `correct` field should be an integer **starting from 1**.
- The `solution` field explains the correct answer.

### For Subjective Questions

Update the file `resources/subjective_questions.txt` with one question per line. Example:

```json
{
  "heading": "Subjective Questions – Java (Variables, Data Types, Constants)",
  "output_filename": "Class11_Java_Subjective_Questions",
  "questions": [
    "Question 1: ....",
    "Question 2: ....."
  ]
}

```

---

## 🚀 How to Use from GitHub (for Admin/Teachers)

1. Go to the [Actions](https://github.com/MatSci-Odia/matsci_mcq/actions) tab in the repository.
2. Navigate to [Matsci Test Generator](https://github.com/MatSci-Odia/matsci_mcq/actions/workflows/python-app.yml)
2. Click on "Run Workflow".
3. Select `Use workflow from` -> `test`
3. Fill the form:
   - Choose the script: `MCQ` or `Subjective`
   - Select the resource file from `resources/<file_name>` directory
4. Click "Run workflow".

Once the workflow completes:
- If successful, a GitHub Issue will be created with a link to download the generated `.docx` file. View the [Issue here](https://github.com/MatSci-Odia/matsci_mcq/issues)
- File can be found under the "Artifacts" section or within the issue.

---

## 📄 Output

- Generates `.docx` files with questions formatted in tables.
- MCQs include question text, options, correct answer, and explanation.
- Subjective tests list all questions as paragraphs.

---

## 🧑‍💻 Requirements

- Python 3.x
- Required libraries: `python-docx`, `docx2pdf`, `flake8`

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

Feel free to modify or extend the scripts to suit your curriculum!
