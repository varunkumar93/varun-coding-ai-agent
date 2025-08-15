# modules/groq_agent.py

import os
from groq import Groq

class GroqAgent:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    def query(self, prompt, model="llama3-8b-8192", temperature=0.7):
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
