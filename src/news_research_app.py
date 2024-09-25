import streamlit as st
import time
from src.url_loader import URLLoader
from src.text_processor import TextProcessor
from src.embedding_manager import EmbeddingManager
from src.query_manager import QueryManager
from src.ner_processor import NERProcessor  # Import NERProcessor
from langchain import OpenAI

class NewsResearchApp:
    def __init__(self):
        self.llm = OpenAI(temperature=0.9, max_tokens=500)
        self.embedding_manager = EmbeddingManager()
        self.ner_processor = NERProcessor()  # Initialize NER processor

    def run(self):
        st.title("RockyBot: News Research Tool 📈")
        st.sidebar.title("News Article URLs")

        urls = self.get_urls()
        process_url_clicked = st.sidebar.button("Process URLs")
        
        # Step 1: Place the question bar at the top
        query = st.text_input("Question: ")
        
        if process_url_clicked:
            self.process_urls(urls)

        # NER output will now be in the sidebar
        if query:
            self.answer_query(query)

    def get_urls(self):
        """Gets URLs from the user."""
        urls = []
        for i in range(3):
            url = st.sidebar.text_input(f"URL {i+1}")
            urls.append(url)
        return urls

    def process_urls(self, urls):
        """Processes the URLs: loads data, splits text, creates embeddings, and applies NER."""
        main_placeholder = st.empty()
        main_placeholder.text("Data Loading...Started...✅✅✅")
        
        # Step 1: Load Data
        url_loader = URLLoader(urls)
        data = url_loader.load_data()

        # Combine all loaded text for NER processing
        combined_text = "\n".join([doc.page_content for doc in data])

        # Step 2: Split Text
        main_placeholder.text("Text Splitter...Started...✅✅✅")
        text_processor = TextProcessor()
        docs = text_processor.split_text(data)

        # Step 3: Create Embeddings and Save
        main_placeholder.text("Embedding Vector Started Building...✅✅✅")
        self.embedding_manager.create_and_save_embeddings(docs)
        time.sleep(2)

        # Step 4: Apply Named Entity Recognition (NER)
        main_placeholder.text("Applying Named Entity Recognition (NER)...")
        entities = self.ner_processor.extract_entities(combined_text)

        # Step 5: Display Extracted Celebrity Names (Filtered) in the sidebar
        st.sidebar.subheader("Extracted Celebrity Names")
        formatted_entities = self.ner_processor.format_entities(entities)
        for entity in formatted_entities:
            st.sidebar.write(f"Entity: {entity['entity']}, Word: {entity['word']}, Confidence: {entity['score']}")

        main_placeholder.text("Process Completed! 🎉")

    def answer_query(self, query):
        """Retrieves an answer to the user's query using the stored embeddings."""
        vectorstore = self.embedding_manager.load_embeddings()
        if vectorstore:
            query_manager = QueryManager(llm=self.llm, vectorstore=vectorstore)
            answer, sources = query_manager.query(query)

            st.header("Answer")
            st.write(answer)

            if sources:
                st.subheader("Sources:")
                for source in sources.split("\n"):
                    st.write(source)
        else:
            st.write("No embeddings found. Please process URLs first.")
