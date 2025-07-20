from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Uncomment if using real AI responses with Transformers
# from transformers import pipeline
# ai_model = pipeline("text-generation", model="gpt2")  # or any other lightweight model

app = FastAPI(
    title="Serendipity AI",
    description="Your supportive AI companion for delightful discoveries.",
    version="0.1.0"
)

# -------------------------------
# Root Route
# -------------------------------
@app.get("/")
def root():
    return {"message": "Welcome to Serendipity AI!"}

# -------------------------------
# About Route
# -------------------------------
@app.get("/about")
def about():
    return {
        "project": "Serendipity AI",
        "description": "Your supportive AI companion for delightful discoveries.",
        "status": "In progress",
        "open_source": True
    }

# -------------------------------
# Contact Route
# -------------------------------
@app.get("/contact")
def contact():
    return {
        "email": "support@serendipity.ai",
        "twitter": "@SerendipityAI",
        "github": "https://github.com/serendipity-ai"
    }

# -------------------------------
# Features Route
# -------------------------------
@app.get("/features")
def features():
    return {
        "core_features": [
            "Conversational AI assistant",
            "Personalized recommendations",
            "Mood-based content suggestions"
        ],
        "coming_soon": [
            "Voice interactions",
            "Calendar sync",
            "Integration with smart devices"
        ]
    }

# -------------------------------
# Status Route
# -------------------------------
@app.get("/status")
def status():
    return {
        "status": "running",
        "uptime": "OK",
        "version": app.version
    }

# -------------------------------
# AI Respond Route
# -------------------------------
class Query(BaseModel):
    message: str

class AIResponse(BaseModel):
    response: str
    note: str

@app.post("/ai/respond", response_model=AIResponse)
def ai_respond(query: Query):
    # Placeholder response logic
    # Uncomment below to use real AI model
    # generated = ai_model(query.message, max_length=50, num_return_sequences=1)
    # response_text = generated[0]['generated_text']
    response_text = f"Echo: {query.message}"
    
    return {
        "response": response_text,
        "note": "AI response generation coming soon!"  # Change when AI is enabled
    }
