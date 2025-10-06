import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction=(
        "You are Fitfare, an AI fitness assistant. "
        "You give evidence-based fitness, workout, and nutrition advice. "
        "Your tone is friendly, motivational, and encouraging. "
        "Avoid making medical diagnoses. "
        "Keep answers concise but actionable."
    )
)

def get_gemini_response(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text
