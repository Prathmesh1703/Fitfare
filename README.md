Fitfare: AI-Powered Fitness & Nutrition Platform

Fitfare is a full-stack web application designed to help users manage their fitness, nutrition, and device connections effectively. It includes a nutrition planner, chatbot assistant, gym peak hour analytics, and a connected device dashboard. The application leverages FastAPI for the backend and Tailwind CSS for a modern frontend UI.

Features

Nutrition Planner: Generate meal plans based on goals, dietary preferences, calories, and restrictions.

AI Chatbot: Interact with Fitfare for fitness and nutrition advice in real-time.

Gym Peak Hour Analytics: Visualize gym usage patterns and identify peak hours.

Connected Device Dashboard: Manage and monitor connected fitness devices.

Responsive UI: Sidebar navigation for easy access to all modules.

Folder Structure
Fitfare/
│
├── Backend/
│   ├── main.py          # Main FastAPI application combining nutrition and chatbot APIs
│   ├── chatbot.py       # Gemini chatbot logic
│   └── nutrition.py     # Nutrition AI logic
│
├── Frontend/
│   ├── index.html                # Main template with sidebar navigation
│   ├── nutritionplanner.html     # Nutrition planner UI
│   ├── chatbot.html              # Chatbot UI
│   ├── dashboard.html            # Connected device dashboard
│   ├── connecteddevice.html      # Connected device page
│   ├── peakdata.html             # Gym peak hour analytics page
│   └── synthetic_gym_multi.csv   # CSV data for gym analytics

Installation & Setup
1. Backend Setup

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install fastapi uvicorn pydantic
# Add any other dependencies like your Gemini API client if required


Run the backend server:

cd Backend
uvicorn main:app --reload


Backend APIs will run at: http://127.0.0.1:8000

2. Frontend Setup

Open the Frontend folder.

You can open index.html directly in a browser (for local testing).

Ensure that the frontend fetch URLs match your backend (default http://127.0.0.1:8000).

For CSV-based analytics (peakdata.html), make sure synthetic_gym_multi.csv is in the same folder as the HTML file.

Usage

Open the app in a browser by opening index.html.

Use the sidebar to navigate between:

Chatbot – Ask fitness or nutrition questions.

Nutrition Planner – Generate meal plans.

Gym Analytics – View peak hours using your CSV data.

Connected Devices – Monitor or connect your fitness devices.

The UI displays structured, markdown-formatted responses from the AI.

Technologies Used

Backend: FastAPI, Python, Gemini AI (for chatbot & nutrition)

Frontend: HTML, Tailwind CSS, Plotly.js (charts), PapaParse (CSV parsing)

Data: CSV (synthetic_gym_multi.csv) for gym analytics

Notes

Ensure CORS is enabled in FastAPI so the frontend can communicate with the backend.

The chatbot and nutrition planner output is rendered with Markdown for better readability.

This setup is intended for local testing/development. For production, replace allow_origins=["*"] with your frontend domain in FastAPI.

Author

Prathamesh Bharsakale