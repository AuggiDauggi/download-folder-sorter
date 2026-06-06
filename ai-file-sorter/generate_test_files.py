from pathlib import Path

DOWNLOADS = Path("downloads")
DOWNLOADS.mkdir(exist_ok=True)

files = {
    "assignment.txt": """
Machine Learning Assignment 3

Implement a neural network classifier and compare it to logistic regression.
""",

    "lecture_notes.md": """
# Artificial Intelligence

Today's lecture covered A* search, heuristics, and pathfinding algorithms.
""",

    "budget.txt": """
Monthly Budget

Rent: 1200
Food: 350
Savings: 500
Utilities: 100
""",

    "invoice.txt": """
Invoice #1042

Amount Due: $249.99
Payment Due: June 15
""",

    "meeting_notes.txt": """
Project Meeting Notes

Discussed sprint planning, deadlines, and client requirements.
""",

    "diary.txt": """
Today I went hiking with friends and had a great time.
""",

    "app.py": """
def hello():
    print("Hello World")

hello()
""",

    "website.html": """
<html>
<head><title>My Website</title></head>
<body>
<h1>Hello World</h1>
</body>
</html>
""",

    "research.txt": """
Large language models are capable of reasoning over complex datasets
and generating structured outputs.
""",

    "recipe.txt": """
Chocolate Cake Recipe

2 cups flour
1 cup sugar
3 eggs
""",
}

for filename, content in files.items():
    with open(DOWNLOADS / filename, "w", encoding="utf-8") as f:
        f.write(content)

# Create some empty binary-like files
(DOWNLOADS / "vacation_photo.jpg").touch()
(DOWNLOADS / "screenshot.png").touch()
(DOWNLOADS / "archive.zip").touch()
(DOWNLOADS / "presentation.pptx").touch()

print(f"Created {len(files) + 4} test files.")
