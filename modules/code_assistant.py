from modules.groq_agent import GroqAgent

groq_agent = GroqAgent()

def explain_code(code):
    prompt = f"Explain the following code:\n{code}"
    return groq_agent.query(prompt)

def debug_code(code):
    prompt = f"Find and fix bugs in the following code:\n{code}"
    return groq_agent.query(prompt)
