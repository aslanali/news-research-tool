from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain

class QueryManager:
    def __init__(self, llm, vectorstore):
        self.llm = llm
        self.vectorstore = vectorstore
    
    def query(self, question):
        """Queries the vector store and retrieves the answer."""
        chain = RetrievalQAWithSourcesChain.from_llm(llm=self.llm, retriever=self.vectorstore.as_retriever())
        result = chain.invoke({"question": question})
        return result["answer"], result.get("sources", "")
