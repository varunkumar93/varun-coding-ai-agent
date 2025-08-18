class PromptLab:
    def __init__(self, groq_agent):
        self.agent = groq_agent

    def run_prompt(self, prompt, style="default"):
        if style == "verbose":
            prompt = f"Explain in detail: {prompt}"
        elif style == "minimal":
            prompt = f"Give a short answer: {prompt}"
        return self.agent.generate(prompt)

    def run(self, prompt, style="default"):
        # Unified entry point for agent orchestration
        return self.run_prompt(prompt, style)
