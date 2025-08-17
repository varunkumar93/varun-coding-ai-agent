from langchain.chains import RetrievalQA
from langchain.llms import OpenAI  # or Groq if you’ve wrapped it
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

class RetrievalAgent:
    def __init__(self, model="gpt-3.5-turbo"):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.db = None
        self.qa_chain = None
        self.llm = OpenAI(model_name=model)

    def build_index(self, texts):
        docs = [Document(page_content=t) for t in texts]
        self.db = FAISS.from_documents(docs, self.embeddings)
        self.qa_chain = RetrievalQA.from_chain_type(llm=self.llm, retriever=self.db.as_retriever())

    def ask(self, query):
        if self.qa_chain:
            return self.qa_chain.run(query)
        return "No index available."
