from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

class MemoryAgent:
    def __init__(self, model="gpt-3.5-turbo"):
        self.memory = ConversationBufferMemory()
        self.chain = ConversationChain(llm=OpenAI(model_name=model), memory=self.memory)

    def chat(self, user_input):
        return self.chain.run(user_input)
