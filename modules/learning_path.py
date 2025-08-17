class LearningPath:
    def recommend(self, progress):
        paths = {
            "Basics": ["Variables and Data Types", "Operators", "Input/Output"],
            "Control Flow": ["If-Else Statements", "Loops", "Switch Case"]
        }

        for path, lessons in paths.items():
            for lesson in lessons:
                if (path, lesson) not in progress:
                    return path, lesson
        return None, None
