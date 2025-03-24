import os
import google.generativeai as genai
import pathlib
from dotenv import load_dotenv

print("Starting script")

# Load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("API key not found")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# PATH=os.getenv("PATH")
FILE_PATH = pathlib.Path("C:/Users/thari/.config/assignment/derogatory_words.txt")

if FILE_PATH.exists():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f.readlines()]
else:
    print("File not found. Check the path!")

def load_inappropriate_words():
    """Load inappropriate words from a local file."""
    try:
        with open(FILE_PATH, "r") as f:
            return [line.strip().lower() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Warning: {FILE_PATH} not found. Skipping content filtering.")
        return []

def filter_content(response):
    """Block responses containing inappropriate words."""
    inappropriate_words = load_inappropriate_words()
    
    # If any bad word is in the response, block it entirely
    if any(word in response.lower() for word in inappropriate_words):
        return "Content flagged as inappropriate."
    
    return response 

def ask_gemini(query):
    """Send a query to Google Gemini API and get a response."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(query)
        return filter_content(response.text)  # Apply filtering before returning
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_input = input("Enter your question: ")
    print("AI Response:", ask_gemini(user_input))
