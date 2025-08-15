from modules.groq_agent import ask_groq

def explain_code(code: str) -> str:
    prompt = f"Explain this code:\n{code}"
    return ask_groq(prompt)

def debug_code(code: str) -> str:
    prompt = f"Find bugs in this code:\n{code}"
    return ask_groq(prompt)

def optimize_code(code: str) -> str:
    prompt = f"Suggest optimizations for this code:\n{code}"
    return ask_groq(prompt)
