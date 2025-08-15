from modules.groq_agent import GroqAgent

class CodeAssistant:
    def __init__(self):
        self.agent = GroqAgent()

    def explain_code(self, code):
        prompt = f"Explain the following code:\n{code}"
        return self.agent.query(prompt)

    def debug_code(self, code):
        prompt = f"Find and fix bugs in the following code:\n{code}"
        return self.agent.query(prompt)
