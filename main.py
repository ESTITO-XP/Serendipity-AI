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

# Store conversation history (in production, use a database)
conversation_history = []

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
        # Add user message to history
        conversation_history.append({"role": "user", "content": request.message})
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        
        ai_response = response.choices[0].message.content
        
        # Add AI response to history
        conversation_history.append({"role": "assistant", "content": ai_response})
        
        return {"response": ai_response}
    except Exception as e:
        return {"error": str(e)}

@app.post("/clear-chat")
async def clear_chat():
    global conversation_history
    conversation_history = []
    return {"message": "Conversation cleared"}
