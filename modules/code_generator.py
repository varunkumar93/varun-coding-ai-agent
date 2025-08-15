from modules.groq_agent import ask_groq

def generate_code(task: str, language: str = "Python") -> str:
    prompt = f"Write {language} code for this task:\n{task}"
    return ask_groq(prompt)
