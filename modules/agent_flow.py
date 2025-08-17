class AgentFlow:
    def __init__(self, assistant, generator):
        self.assistant = assistant
        self.generator = generator

    def explain_then_debug(self, code):
        explanation = self.assistant.explain_code(code)
        debugged = self.assistant.debug_code(code)
        return explanation, debugged

    def generate_then_explain(self, prompt):
        code = self.generator.generate_code(prompt)
        explanation = self.assistant.explain_code(code)
        return code, explanation
