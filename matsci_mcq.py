# -*- coding: utf-8 -*-
from docx import Document

# Create the document
doc = Document()
doc.add_heading("Class 11 Prog Fundamentals", level=1)

# Define the MCQs
mcq_data = [
    {
        "question": "Which of the following is a valid variable name in Java?",
        "options": ["2value", "value$", "int", "void"],
        "correct": 2,
        "solution": "Variable names cannot start with numbers or be keywords. 'value$' is valid."
    },
    {
        "question": "Which of these is a correct data type to store a decimal value?",
        "options": ["int", "float", "boolean", "char"],
        "correct": 2,
        "solution": "The 'float' data type is used to store decimal numbers in Java."
    },
    {
        "question": "What will be the output of: int a = 5; System.out.println(a == 5);",
        "options": ["true", "false", "5", "Compilation Error"],
        "correct": 1,
        "solution": "The '==' operator checks for equality. Since a equals 5, it prints 'true'."
    },
    {
        "question": "Which operator is used for logical AND in Java?",
        "options": ["&", "and", "&&", "||"],
        "correct": 3,
        "solution": "'&&' is the logical AND operator in Java."
    },
    {
        "question": "What is the result of 10 % 3 in Java?",
        "options": ["0", "1", "3", "10"],
        "correct": 2,
        "solution": "10 % 3 gives the remainder, which is 1."
    },
    {
        "question": "Which keyword is used for decision-making in Java?",
        "options": ["do", "if", "while", "switch"],
        "correct": 2,
        "solution": "'if' is used for decision-making in Java."
    },
    {
        "question": "What will be the output of: int x = 8; if (x > 5) System.out.print(\"Hi\");",
        "options": ["Hi", "Nothing", "Error", "5"],
        "correct": 1,
        "solution": "Since x > 5, the condition is true and 'Hi' is printed."
    },
    {
        "question": "Which statement ends a loop early in Java?",
        "options": ["exit", "continue", "stop", "break"],
        "correct": 4,
        "solution": "'break' is used to exit a loop prematurely."
    },
    {
        "question": "How many times will the loop run? for(int i = 1; i <= 3; i++)",
        "options": ["2", "3", "4", "Infinite"],
        "correct": 2,
        "solution": "The loop runs for i = 1, 2, 3 → Total 3 times."
    },
    {
        "question": "Which of the following is a valid use of 'while' loop?",
        "options": [
            "Repeat steps until user enters correct password",
            "Execute a menu at least once",
            "Print numbers from 1 to 10 if known",
            "None of the above"
        ],
        "correct": 1,
        "solution": "'while' is used when number of iterations is unknown."
    },
    {
        "question": "Which loop checks the condition after executing the loop body?",
        "options": ["for", "while", "do-while", "repeat"],
        "correct": 3,
        "solution": "'do-while' loop runs once before checking the condition."
    },
    {
        "question": "Which of the following is used to skip the current iteration in a loop?",
        "options": ["stop", "skip", "continue", "exit"],
        "correct": 3,
        "solution": "'continue' skips the current iteration and moves to the next."
    },
    {
        "question": "Which of these loops is best when number of iterations is known?",
        "options": ["for", "while", "do-while", "foreach"],
        "correct": 1,
        "solution": "'for' loop is best suited for known iteration count."
    },
    {
        "question": "Which is the correct syntax to declare an integer in Java?",
        "options": ["int = 5;", "int a = 5", "int a = 5;", "integer a = 5;"],
        "correct": 3,
        "solution": "Correct declaration: 'int a = 5;'"
    },
    {
        "question": "Which of the following is not a Java keyword?",
        "options": ["if", "else", "then", "switch"],
        "correct": 3,
        "solution": "'then' is not a keyword in Java."
    },
    {
        "question": "What will be the output of: int a = 5; int b = 10; System.out.println(a + b);",
        "options": ["15", "5", "10", "a + b"],
        "correct": 1,
        "solution": "5 + 10 = 15, so it prints 15."
    },
    {
        "question": "Which operator is used to assign a value in Java?",
        "options": ["==", ":=", "=", "+"],
        "correct": 3,
        "solution": "'=' is used for assignment in Java."
    },
    {
        "question": "What does 'i++' do in Java?",
        "options": ["Decreases i by 1", "Increases i by 1", "Prints i", "Sets i to 0"],
        "correct": 2,
        "solution": "'i++' increases the value of i by 1."
    },
    {
        "question": "Which loop will always execute at least once?",
        "options": ["for", "while", "do-while", "None"],
        "correct": 3,
        "solution": "'do-while' loop executes once before checking the condition."
    },
    {
        "question": "Which is a correct example of a for loop?",
        "options": [
            "for (i < 10; i++)",
            "for int i = 0 to 10",
            "for (int i = 0; i < 10; i++)",
            "loop(i=1;i<=10;i++)"
        ],
        "correct": 3,
        "solution": "The correct syntax: 'for (int i = 0; i < 10; i++)'"
    }
]



# Create table per question
for idx, mcq in enumerate(mcq_data, 1):
    table = doc.add_table(rows=8, cols=3)
    table.style = 'Table Grid'

    table.cell(0, 0).text = f"Question #{idx}"
    table.cell(0, 1).merge(table.cell(0, 2)).text = mcq["question"]

    table.cell(1, 0).text = "Type"
    table.cell(1, 1).merge(table.cell(1, 2)).text = "multiple_choice"

    for i in range(4):
        table.cell(2+i, 0).text = "Option"
        table.cell(2+i, 1).text = mcq["options"][i]
        table.cell(2+i, 2).text = "correct" if i == mcq["correct"] else "incorrect"

    table.cell(6, 0).text = "Solution"
    table.cell(6, 1).merge(table.cell(6, 2)).text = mcq["solution"]

    table.cell(7, 0).text = "Marks"
    table.cell(7, 1).text = "1"
    table.cell(7, 2).text = "0"

    doc.add_paragraph("")

# Save the file
doc.save("Class_11_Prog_Fundamentals.docx")
print("✅ Document created successfully: Class_11_Prog_Fundamentals.docx")
