import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

config = {
    "llm": {
        "provider": "groq",
        "config": {
            "model": "llama-3.1-8b-instant",
            "api_key": GROQ_API_KEY   # ✅ use the variable, not the string
        }
    },
    "embedding_model": {
        "provider": "huggingface",
        "config": {
            "model": "sentence-transformers/all-MiniLM-L6-v2"
        }
    }
}
