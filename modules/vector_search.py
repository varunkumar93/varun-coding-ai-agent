from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

class VectorSearch:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.db = None

    def build_index(self, texts):
        docs = [Document(page_content=t) for t in texts]
        self.db = FAISS.from_documents(docs, self.embeddings)

    def search(self, query, k=3):
        if self.db:
            return self.db.similarity_search(query, k=k)
        return []
