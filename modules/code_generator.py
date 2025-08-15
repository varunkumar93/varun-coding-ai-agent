from modules.groq_agent import GroqAgent

groq_agent = GroqAgent()

def generate_code(prompt):
    full_prompt = f"Write Python code for the following task:\n{prompt}"
    return groq_agent.query(full_prompt)
