from langchain.document_loaders import UnstructuredURLLoader

class URLLoader:
    def __init__(self, urls):
        self.urls = urls
    
    def load_data(self):
        """Loads data from provided URLs."""
        loader = UnstructuredURLLoader(urls=self.urls)
        return loader.load()
