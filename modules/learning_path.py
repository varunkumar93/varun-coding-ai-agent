class LearningPath:
    def __init__(self):
        self.paths = {
            "Beginner": ["Variables", "Loops", "Functions"],
            "Debug Master": ["Tracebacks", "Common Errors", "Fix Strategies"],
            "Groq Pro": ["Setup", "Prompting", "Streaming Responses"]
        }

    def recommend(self, progress):
        for path, lessons in self.paths.items():
            for lesson in lessons:
                if lesson not in progress.values():
                    return path, lesson
        return "All done!", None
