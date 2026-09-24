import os
from dotenv import load_dotenv
import google.generativeai as genai
from database import students_db

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_chatbot(query: str) -> str:
    context = f"Here is the current student database records: {students_db}"
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"{context}\n\nUser Question: {query}\nAnswer accurately based only on the student records provided above:"
    
    response = model.generate_content(prompt)
    return response.text