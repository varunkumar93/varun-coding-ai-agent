from modules.course_manager import ProgramizCourseManager

class UnifiedCourseManager:
    def __init__(self):
        self.programiz = ProgramizCourseManager()
        self.topic_map = {
            "Variables and Data Types": "variables-data-types",
            "Functions": "functions",
            "Loops": "loops",
            "Conditionals": "conditionals",
            "Python": "variables-data-types",  # fallback
            "C": "variables-data-types",       # fallback
            "Java": "java",                    # dynamic
            "JavaScript": "javascript"         # dynamic
        }

    def get_lesson_content(self, path, lesson):
        # ✅ Custom lessons for ML and Agentic AI
        if lesson == "Machine Learning":
            return """### 🤖 Machine Learning: Introduction
Machine Learning is the science of getting computers to learn from data.

**Topics Covered:**
- Supervised vs Unsupervised Learning
- Regression, Classification
- Neural Networks, Decision Trees

📘 Explore: [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)
"""
        elif lesson == "Agentic AI":
            return """### 🧠 Agentic AI: Foundations
Agentic AI refers to autonomous systems that plan, reason, and act.

**Topics Covered:**
- LangChain, CrewAI, AutoGen
- Planning, Memory, Tool Use
- Multi-agent collaboration

📘 Explore:
- [LangChain Docs](https://docs.langchain.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewAI)
"""

        # ✅ Dynamic lesson for mapped topics
        topic_slug = self.topic_map.get(lesson, lesson.lower().replace(" ", "-"))
        language = lesson if lesson in ["Java", "JavaScript", "Python"] else "Python"
        content = self.programiz.get_lesson_content(language, topic_slug)

        if not content:
            return f"""⚠️ Lesson content not found for **{lesson}**.

📘 Try another topic or check spelling.
📺 YouTube: [Learn {lesson}](https://www.youtube.com/results?search_query=learn+{lesson})
"""
        return content
