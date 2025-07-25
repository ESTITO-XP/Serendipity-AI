from fastapi import FastAPI, HTTPException
import openai
import os
from pydantic import BaseModel, validator
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
MAX_HISTORY_LENGTH = 20  # Keep last 10 exchanges (20 messages)

class ChatRequest(BaseModel):
    message: str
    
    @validator('message')
    def message_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Message cannot be empty')
        if len(v) > 4000:
            raise ValueError('Message too long (max 4000 characters)')
        return v.strip()

@app.get("/")
def root():
    return {"message": "Welcome to Serendipity AI!"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Serendipity AI",
        "version": "0.1.0",
        "api_configured": bool(openai.api_key)
    }

@app.get("/about")
def about():
    return {
        "project": "Serendipity AI",
        "description": "Your supportive AI companion for delightful discoveries.",
        "status": "In progress",
        "open_source": True,
        "endpoints": [
            "/",
            "/health", 
            "/about",
            "/history",
            "/chat",
            "/clear-chat"
        ]
    }

@app.get("/history")
async def get_history():
    # Return history without system prompt
    user_history = [msg for msg in conversation_history if msg["role"] != "system"]
    return {"history": user_history, "count": len(user_history)}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        if not openai.api_key:
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        
        # Add user message to history
        conversation_history.append({"role": "user", "content": request.message})
        
        # Trim history if too long (keep system prompt + recent messages)
        if len(conversation_history) > MAX_HISTORY_LENGTH:
            conversation_history[1:] = conversation_history[-(MAX_HISTORY_LENGTH-1):]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=1000,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        # Add AI response to histor
