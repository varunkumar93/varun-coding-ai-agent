import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import Groq

class MemoryAgent:
    def __init__(self, model="llama3-8b-8192"):
        self.memory = ConversationBufferMemory()
        self.chain = ConversationChain(
            llm=Groq(
                model=model,
                api_key=os.getenv("GROQ_API_KEY")
            ),
            memory=self.memory
        )

    def chat(self, user_input):
        return self.chain.run(user_input)
