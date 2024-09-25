import pickle
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

class EmbeddingManager:
    def __init__(self, file_path="models/faiss_store_openai.index"):
        self.file_path = file_path
        self.embeddings = OpenAIEmbeddings()
    
    def create_and_save_embeddings(self, docs):
        """Creates embeddings and saves them to a FAISS index."""
        # Ensure 'models' directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        
        vectorstore = FAISS.from_documents(docs, self.embeddings)
        
        # FAISS has a built-in save method for saving the index
        vectorstore.save_local(self.file_path)
    
    def load_embeddings(self):
        """Loads the FAISS index from the saved file."""
        if os.path.exists(self.file_path):
            return FAISS.load_local(self.file_path, self.embeddings,allow_dangerous_deserialization=True)
        return None


# class EmbeddingManager:
#     def __init__(self, file_path="models/faiss_store_openai.pkl"):
#         self.file_path = file_path
#         self.embeddings = OpenAIEmbeddings()
    
#     def create_and_save_embeddings(self, docs):
#         """Creates embeddings and saves them to a FAISS index."""
#         vectorstore = FAISS.from_documents(docs, self.embeddings)
#         print(os.getcwd())
#         with open(self.file_path, "wb") as f:
#             pickle.dump(vectorstore, f)
    
#     def load_embeddings(self):
#         """Loads the FAISS index from a pickle file."""
#         if os.path.exists(self.file_path):
#             with open(self.file_path, "rb") as f:
#                 return pickle.load(f)
#         return None
