class QuizEngine:
    def get_quiz(self, topic):
        return {
            "question": "What does `len()` do?",
            "options": ["Returns length", "Returns type", "Returns value"],
            "answer": "Returns length"
        }

    def check_answer(self, user_answer, correct_answer):
        return user_answer == correct_answer
