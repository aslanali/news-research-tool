# News Research Tool 📈
A Streamlit-based tool for researching news articles, extracting named entities (NER), and querying information using embeddings.

## Features
- Process a news article URL and extract Named Entities (people, organizations, etc.).
- Store embeddings in FAISS for efficient retrieval.
- Query the embeddings for specific questions related to the news content.

## Installation
To get started, clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/news_research_tool.git
cd news_research_tool
pip install -r requirements.txt
```

## Setup
Create a .env file in the project root to store your OpenAI API key:
```bash
OPENAI_API_KEY=<your_openai_api_key_here>
```

## Running the App
```bash
streamlit run app.py
```

## Folder Structure:

### Root Directory 
* **src/:** Contains the core logic of the app.
* **models/:** Stores embeddings (FAISS index).
* **requirements.txt:** Python dependencies.
* **app.py:** This is the entry point of your Streamlit app. It imports the core logic from the src/ directory and runs the app when the command streamlit run app.py is executed.
* **README.md:** Documentation for the project.


## Usage

1. **Enter a news article URL:** Paste the URL of the news article you want to analyze.
2. **Process the URL:** The tool will automatically extract named entities from the article.
3. **Ask questions:** Start asking questions about the content of the news.
