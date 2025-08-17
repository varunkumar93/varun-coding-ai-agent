class LearningPath:
    def recommend(self, progress):
        if "Basics" not in progress:
            return "Basics", "Variables and Data Types"
        elif "Control Flow" not in progress:
            return "Control Flow", "If-Else Statements"
        else:
            return None, None
