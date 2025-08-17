from modules.course_manager import ProgramizCourseManager

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
        if lesson == "Machine Learning":
            return """
### 🤖 Machine Learning: Introduction
Machine Learning is the science of getting computers to learn from data.

**Topics Covered:**
- Supervised vs Unsupervised Learning
- Regression, Classification
- Neural Networks, Decision Trees

📘 Explore [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)
"""
        elif lesson == "Agentic AI":
            return """
### 🧠 Agentic AI: Foundations
Agentic AI refers to autonomous systems that plan, reason, and act.

**Topics Covered:**
- LangChain, CrewAI, AutoGen
- Planning, Memory, Tool Use
- Multi-agent collaboration

📘 Explore [LangChain Docs](https://docs.langchain.com) or [CrewAI GitHub](https://github.com/joaomdmoura/crewAI)
"""
        else:
            topic_slug = self.topic_map.get(lesson, lesson.lower().replace(" ", "-"))
            return self.programiz.get_lesson_content("Python", topic_slug)
