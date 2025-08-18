from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq

class GroqAgent:
    def __init__(self):
        self.llm = ChatGroq(model="llama-3.3-70b-versatile")
        self.prompt = PromptTemplate.from_template("Answer this: {input}")
        self.chain = self.prompt | self.llm

    def generate(self, prompt_text):
        return self.chain.invoke({"input": prompt_text})
