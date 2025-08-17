# modules/groq_agent.py

import os
import time
from groq import Groq, RateLimitError

class GroqAgent:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    def query(self, prompt, model="llama3-8b-8192", temperature=0.7, retries=3):
        for attempt in range(retries):
            try:
                response = self.client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temperature
                )
                return response.choices[0].message.content
            except RateLimitError:
                wait_time = 2 * (attempt + 1)
                print(f"⚠️ Rate limit hit. Retrying in {wait_time}s...")
                time.sleep(wait_time)
        return "⚠️ Rate limit exceeded. Please wait and try again later."
