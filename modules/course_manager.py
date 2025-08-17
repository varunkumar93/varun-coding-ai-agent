class ProgramizCourseManager:  # You can rename this to FreeCodeCampCourseManager if you prefer
    def get_lesson_content(self, language, topic_slug):
        if topic_slug == "variables-data-types":
            return """\
### 📘 Variables and Data Types (freeCodeCamp)
Variables store data. Data types define the kind of data.

**Examples:**
```python
x = 5       # Integer
name = "AI" # String
