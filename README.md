# Matsci MCQ and Subjective Test Generator

This project generates MCQ and Subjective tests using Python and Word documents.

---

## 🛠️ Steps to Execute

To generate the MCQ document:

```bash
python3 matsci_mcq.py
```

To generate the Subjective test document:

```bash
python3 subjective_test.py
```

---

## ✍️ How to Add/Update Questions

### For MCQs

Update the `mcq_data` list in `matsci_mcq.py` with entries in the following format:

```json
{
    "question": "Which of the following is a valid variable name in Java?",
    "options": ["2value", "value$", "int", "void"],
    "correct": 2,
    "solution": "Variable names cannot start with numbers or be keywords. 'value$' is valid."
}
```

- The `options` list must contain exactly 4 strings.
- The `correct` field should be an integer **starting from 1** (1 for the first option, 2 for second, etc.).
- The `solution` field explains why the selected answer is correct.

---

### For Subjective Questions

Update the question list in the `subjective_test.py` file like this:

```python
questions = [
    "Explain the difference between Java and Python.",
    "Write a Java program to print the first 10 even numbers.",
    ...
]
```

---

## 📄 Output

- Generates `.docx` files with questions formatted in tables.
- Each MCQ will include question text, options, correct answer indication, solution, and marks.

---

## 🧑‍💻 Requirements

- Python 3.x
- `python-docx` library

Install dependencies using:

```bash
pip install python-docx
```

---

Feel free to modify or extend the scripts to suit your curriculum!
