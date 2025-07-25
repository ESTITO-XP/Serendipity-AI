from fastapi import FastAPI
import openai
import os
from pydantic import BaseModel

app = FastAPI(
    title="Serendipity AI",
    description="Your supportive AI companion for delightful discoveries.",
    version="0.1.0"
)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Welcome to Serendipity AI!"}

@app.get("/about")
def about():
    return {
        "project": "Serendipity AI",
        "description": "Your supportive AI companion for delightful discoveries.",
        "status": "In progress",
        "open_source": True
    }

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.message}]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
