import os
import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
class MemoryAgent:
    def __init__(self, model="llama3-8b-8192"):
        self.memory = ConversationBufferMemory()
        self.chain = ConversationChain(
            llm=ChatGroq(
                model=model,
                api_key=st.secrets["GROQ_API_KEY"]
            ),
            memory=self.memory
        )

    def chat(self, user_input):
        return self.chain.run(user_input)
