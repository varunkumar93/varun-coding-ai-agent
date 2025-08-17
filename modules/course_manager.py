class ProgramizCourseManager:
    def get_lesson_content(self, language, topic_slug):
        if topic_slug == "variables-data-types":
            return """### 📘 Variables and Data Types (freeCodeCamp)
Variables store data. Data types define the kind of data.

**Examples:**
    x = 5        # Integer
    name = "AI"  # String

📺 Watch: Learn Python Full Course
https://www.youtube.com/watch?v=rfscVS0vtbw

📘 Read: freeCodeCamp Python Guide
https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/
"""
        elif topic_slug == "functions":
            return """### 🧠 Functions in Python (freeCodeCamp)
Functions are reusable blocks of code.

**Example:**
    def greet(name):
        return f"Hello, {name}!"

📺 Watch: Python Functions Tutorial
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1h10m
"""
        elif topic_slug == "loops":
            return """### 🔁 Loops in Python (freeCodeCamp)
Loops let you repeat actions.

**Example:**
    for i in range(5):
        print(i)

📺 Watch: Python Loops Tutorial
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1h20m
"""
        elif topic_slug == "conditionals":
            return """### ⚖️ Conditionals in Python (freeCodeCamp)
Conditionals let you make decisions.

**Example:**
    if x > 0:
        print("Positive")
    else:
        print("Non-positive")

📺 Watch: Python Conditionals
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1h30m
"""
        return None
