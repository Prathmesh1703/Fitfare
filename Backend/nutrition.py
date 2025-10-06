import os
from dotenv import load_dotenv
import google.generativeai as genai
from typing import Optional

# Load environment variables from .env
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a system instruction for NutriBot
SYSTEM_INSTRUCTION = (
    "You are NutriBot, an expert nutrition planner and diet assistant. "
    "Your goal is to provide accurate, evidence-based, and practical nutrition advice to users. "
    "Always consider the user's health, dietary restrictions, and fitness goals. "
    "Provide clear meal plans, snack suggestions, or diet tips based on the user's input. "
    "Avoid giving medical advice; always recommend consulting a healthcare professional for medical concerns. "
    "Include portions, calories, or nutrient information where possible. "
    "Make suggestions for various diets (vegetarian, vegan, keto, gluten-free) if specified by the user. "
    "Be friendly, concise, and encouraging. "
    "When unsure about specific health conditions, politely recommend the user consult a dietitian or doctor. "
    "Keep responses practical and easy to implement. "
    "Do not generate offensive, harmful, or unrealistic recommendations."
)

def chat_with_gemini(prompt: str, max_output_tokens: Optional[int] = 300) -> str:
    """
    Queries Google Gemini AI and returns a response.

    Args:
        prompt (str): The input question or user preferences.
        max_output_tokens (int, optional): Maximum number of tokens to generate.

    Returns:
        str: Response text from Gemini AI.
    """
    try:
        # Use Gemini GenerativeModel
        model = genai.GenerativeModel(
            "gemini-2.5-flash",
            system_instruction=SYSTEM_INSTRUCTION
        )

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error while querying Gemini: {str(e)}"
