from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import functions from separate files
from chatbot import get_gemini_response
from nutrition import chat_with_gemini

app = FastAPI()

# Enable CORS so frontend can talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Chatbot Endpoint ----------------
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = get_gemini_response(request.message)
    return ChatResponse(reply=reply)

# ---------------- Nutrition Endpoint ----------------
class NutritionRequest(BaseModel):
    goal: str
    dietary_preference: str
    calories: int
    meals: int
    restrictions: str = ""

@app.post("/api/nutrition")
async def generate_meal_plan(req: NutritionRequest):
    prompt = (
        f"Create a {req.goal.lower()} meal plan for {req.meals} meals per day, "
        f"{req.calories} calories, dietary preference: {req.dietary_preference}. "
    )
    if req.restrictions:
        prompt += f"Exclude: {req.restrictions}. "

    prompt += "Provide portions and calories for each meal."

    try:
        response_text = chat_with_gemini(prompt)
        return {"meal_plan": response_text}
    except Exception as e:
        return {"meal_plan": f"Error while querying Gemini: {str(e)}"}
