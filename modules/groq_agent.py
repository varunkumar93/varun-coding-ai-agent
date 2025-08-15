import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def ask_groq(prompt, model="llama3-8b-8192"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
