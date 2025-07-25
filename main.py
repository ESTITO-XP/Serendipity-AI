from fastapi import FastAPI
import openai
import os
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Serendipity AI",
    description="Your supportive AI companion for delightful discoveries.",
    version="0.1.0"
)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# System prompt for AI personality
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are Serendipity AI, a supportive and delightful AI companion. You're always available to help, provide insightful conversations, and create delightful discoveries. Be friendly, encouraging, and curious. Help users explore new ideas and perspectives."
}

# Store conversation history (in production, use a database)
conversation_history = [SYSTEM_PROMPT]

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
    conversation_history = [SYSTEM_PROMPT]
    return {"message": "Conversation cleared"}
