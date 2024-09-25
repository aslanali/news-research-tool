from src.news_research_app import NewsResearchApp
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Main execution
if __name__ == "__main__":
    app = NewsResearchApp()
    app.run()
