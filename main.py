from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import openai
import os
import logging
from pydantic import BaseModel, validator
from dotenv import load_dotenv
from typing import List, Dict, Optional
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Serendipity AI",
    description="Your supportive AI companion for delightful discoveries.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Enhanced system prompt for AI personality
SYSTEM_PROMPT = {
    "role": "system", 
    "content": """You are Serendipity AI, a supportive and delightful AI companion designed to spark wonderful discoveries and meaningful conversations. 

Your personality traits:
- Warm, encouraging, and genuinely curious about the user's thoughts and experiences
- Insightful and thoughtful, helping users explore new ideas and perspectives
- Supportive during challenges while celebrating successes
- Creative and inspiring, often suggesting interesting connections or possibilities
- Always respectful of boundaries and user autonomy

Your communication style:
- Use a conversational, friendly tone
- Ask thoughtful follow-up questions when appropriate
- Offer multiple perspectives on topics
- Share relevant insights without being overwhelming
- Be concise but thorough when needed

Remember: You're here to be a delightful companion who helps users discover new ideas, work through problems, and explore their interests with enthusiasm and support."""
}

# Enhanced conversation storage (in production, use Redis or database)
class ConversationStore:
    def __init__(self):
        self.conversations: Dict[str, List[Dict]] = {}
        self.max_history = 20
    
    def get_conversation(self, session_id: str) -> List[Dict]:
        if session_id not in self.conversations:
            self.conversations[session_id] = [SYSTEM_PROMPT]
        return self.conversations[session_id]
    
    def add_message(self, session_id: str, message: Dict):
        conversation = self.get_conversation(session_id)
        conversation.append(message)
        
        # Trim history if too long (keep system prompt + recent messages)
        if len(conversation) > self.max_history:
            conversation[1:] = conversation[-(self.max_history-1):]
    
    def clear_conversation(self, session_id: str):
        self.conversations[session_id] = [SYSTEM_PROMPT]

store = ConversationStore()

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = "default"
    
    @validator('message')
    def message_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Message cannot be empty')
        if len(v) > 4000:
            raise ValueError('Message too long (max 4000 characters)')
        return v.strip()

class ChatResponse(BaseModel):
    response: str
    session_id: str
    timestamp: float

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main chat interface"""
    if os.path.exists("static/index.html"):
        with open("static/index.html", "r") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    return {"message": "Welcome to Serendipity AI! Visit /docs for API documentation."}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Serendipity AI",
        "version": "1.0.0",
        "api_configured": bool(openai.api_key),
        "timestamp": time.time()
    }

@app.get("/about")
def about():
    """Project information"""
    return {
        "project": "Serendipity AI",
        "description": "Your supportive AI companion for delightful discoveries.",
        "version": "1.0.0",
        "status": "Active Development",
        "open_source": True,
        "repository": "https://github.com/ESTITO-XP/Serendipity-AI",
        "features": [
            "Conversational AI with personality",
            "Session-based conversations", 
            "RESTful API",
            "Web interface",
            "Health monitoring"
        ],
        "endpoints": {
            "/": "Main chat interface",
            "/health": "Health check", 
            "/about": "Project information",
            "/chat": "Send chat message",
            "/history/{session_id}": "Get conversation history",
            "/clear-chat": "Clear conversation",
            "/docs": "API documentation"
        }
    }

@app.get("/history/{session_id}")
async def get_history(session_id: str):
    """Get conversation history for a session"""
    conversation = store.get_conversation(session_id)
    # Return history without system prompt
    user_history = [msg for msg in conversation if msg["role"] != "system"]
    return {
        "session_id": session_id,
        "history": user_history, 
        "count": len(user_history),
        "timestamp": time.time()
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Send a message to Serendipity AI"""
    try:
        if not openai.api_key:
            raise HTTPException(
                status_code=500, 
                detail="OpenAI API key not configured. Please set OPENAI_API_KEY environment variable."
            )
        
        # Get conversation for this session
        conversation = store.get_conversation(request.session_id)
        
        # Add user message to history
        store.add_message(request.session_id, {
            "role": "user", 
            "content": request.message,
            "timestamp": time.time()
        })
        
        # Prepare messages for OpenAI (without timestamps)
        messages_for_api = [
            {"role": msg["role"], "content": msg["content"]} 
            for msg in conversation
        ]
        
        logger.info(f"Sending request to OpenAI for session {request.session_id}")
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages_for_api,
            max_tokens=1500,
            temperature=0.8,
            presence_penalty=0.1,
            frequency_penalty=0.1
        )
        
        ai_response = response.choices[0].message.content.strip()
        
        # Add AI response to history
        store.add_message(request.session_id, {
            "role": "assistant", 
            "content": ai_response,
            "timestamp": time.time()
        })
        
        logger.info(f"Response generated for session {request.session_id}")
        
        return ChatResponse(
            response=ai_response,
            session_id=request.session_id,
            timestamp=time.time()
        )
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except openai.error.AuthenticationError:
        logger.error("OpenAI authentication failed")
        raise HTTPException(status_code=401, detail="Invalid OpenAI API key")
    except openai.error.RateLimitError:
        logger.error("OpenAI rate limit exceeded")
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Please try again later.")
    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API error: {str(e)}")
        raise HTTPException(status_code=502, detail=f"AI service error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/clear-chat")
async def clear_chat(session_id: str = "default"):
    """Clear conversation history for a session"""
    store.clear_conversation(session_id)
    logger.info(f"Conversation cleared for session {session_id}")
    return {
        "message": f"Conversation cleared for session {session_id}",
        "timestamp": time.time()
    }

@app.get("/sessions")
async def list_sessions():
    """List all active sessions"""
    return {
        "sessions": list(store.conversations.keys()),
        "count": len(store.conversations),
        "timestamp": time.time()
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
