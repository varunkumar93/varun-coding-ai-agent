class UnifiedCourseManager:
    def __init__(self):
        self.programiz = ProgramizCourseManager()
        self.topic_map = {
            "Variables and Data Types": "variables-data-types",
            "Operators": "operators",
            "Input/Output": "taking-input",
            "Loops": "loops",
            "Functions": "functions",
            "Python": "variables-data-types",  # fallback
            "C": "variables-data-types",
            "Java": "variables-data-types",
            "JavaScript": "variables-data-types"
        }

    def get_lesson_content(self, path, lesson):
        if lesson in ["Machine Learning", "Agentic AI"]:
            # return curated content
            ...
        else:
            topic_slug = self.topic_map.get(lesson, lesson.lower().replace(" ", "-"))
            return self.programiz.get_lesson_content("Python", topic_slug)
