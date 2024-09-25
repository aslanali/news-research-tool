from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextProcessor:
    def __init__(self, chunk_size=1000):
        self.chunk_size = chunk_size
    
    def split_text(self, documents):
        """Splits documents into chunks."""
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=self.chunk_size
        )
        return text_splitter.split_documents(documents)
