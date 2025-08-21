from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
import time
import json
from typing import Dict, List, Optional
import logging
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Serendipity AI Chat", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory session storage (use Redis or database in production)
chat_sessions: Dict[str, List[Dict]] = {}

# Configure OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatMessage(BaseModel):
    message: str
    session_id: str

class ChatResponse(BaseModel):
    response: str
    timestamp: float

@app.get("/")
async def root():
    """Serve the main chat interface"""
    return FileResponse("static/index.html")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": time.time()}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_message: ChatMessage):
    """Handle chat messages and return AI responses"""
    
    try:
        # Validate input
        if not chat_message.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        if len(chat_message.message) > 4000:
            raise HTTPException(status_code=400, detail="Message too long (max 4000 characters)")
        
        # Check if OpenAI API key is configured
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(
                status_code=500, 
                detail="OpenAI API key not configured. Please set the OPENAI_API_KEY environment variable."
            )
        
        # Get or create session
        session_id = chat_message.session_id
        if session_id not in chat_sessions:
            chat_sessions[session_id] = []
        
        # Add user message to session
        user_message = {
            "role": "user",
            "content": chat_message.message,
            "timestamp": time.time()
        }
        chat_sessions[session_id].append(user_message)
        
        # Keep only last 20 messages to manage context length
        if len(chat_sessions[session_id]) > 20:
            chat_sessions[session_id] = chat_sessions[session_id][-20:]
        
        # Prepare conversation history for OpenAI
        system_message = {
            "role": "system",
            "content": """You are Serendipity AI, a supportive and delightful AI companion. Your personality traits:

- **Supportive**: Always encourage and help users feel heard and understood
- **Curious**: Show genuine interest in what users share and ask thoughtful follow-up questions
- **Creative**: Offer unique perspectives and creative solutions
- **Empathetic**: Respond with emotional intelligence and understanding
- **Inspiring**: Help users discover new possibilities and see things from fresh angles
- **Conversational**: Keep responses natural, engaging, and appropriately sized for chat

Guidelines:
- Be warm, friendly, and authentic in your responses
- Provide helpful, accurate information while maintaining an encouraging tone
- Ask clarifying questions when helpful
- Share interesting insights or connections that might spark curiosity
- Keep responses conversational and not too lengthy (2-4 paragraphs max)
- Use emojis occasionally to add warmth but don't overuse them
- Remember you're having a chat conversation, not writing an essay

Your goal is to be a delightful companion that brings joy, support, and serendipitous discoveries to every interaction."""
        }
        
        # Build message history
        messages = [system_message]
        
        # Add recent conversation history (excluding system messages and timestamps)
        for msg in chat_sessions[session_id]:
            if msg["role"] in ["user", "assistant"]:
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
        
        # Call OpenAI API
        logger.info(f"Sending request to OpenAI for session {session_id}")
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.7,
            top_p=0.9,
            frequency_penalty=0.2,
            presence_penalty=0.2
        )
        
        ai_response = response.choices[0].message.content.strip()
        
        # Add AI response to session
        ai_message = {
            "role": "assistant",
            "content": ai_response,
            "timestamp": time.time()
        }
        chat_sessions[session_id].append(ai_message)
        
        logger.info(f"Successfully generated response for session {session_id}")
        
        return ChatResponse(
            response=ai_response,
            timestamp=time.time()
        )
        
    except openai.RateLimitError:
        logger.error("OpenAI rate limit exceeded")
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Please wait a moment and try again."
        )
    
    except openai.AuthenticationError:
        logger.error("OpenAI authentication failed")
        raise HTTPException(
            status_code=500,
            detail="OpenAI API authentication failed. Please check the API key."
        )
    
    except openai.APIError as e:
        logger.error(f"OpenAI API error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"AI service error: {str(e)}"
        )
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred. Please try again."
        )

@app.get("/sessions/{session_id}/history")
async def get_session_history(session_id: str):
    """Get chat history for a session"""
    if session_id not in chat_sessions:
        return {"messages": []}
    
    # Return messages without system messages
    messages = [
        msg for msg in chat_sessions[session_id] 
        if msg["role"] in ["user", "assistant"]
    ]
    
    return {"messages": messages}

@app.delete("/sessions/{session_id}")
async def clear_session(session_id: str):
    """Clear a chat session"""
    if session_id in chat_sessions:
        del chat_sessions[session_id]
        logger.info(f"Cleared session {session_id}")
    
    return {"message": "Session cleared successfully"}

@app.get("/sessions")
async def get_active_sessions():
    """Get list of active sessions (for admin purposes)"""
    return {
        "active_sessions": len(chat_sessions),
        "total_messages": sum(len(messages) for messages in chat_sessions.values())
    }

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8000))
    
    print("🤖 Starting Serendipity AI Chat Server...")
    print(f"📱 Server will be available at: http://localhost:{port}")
    print("🔑 Make sure to set your OPENAI_API_KEY environment variable!")
    
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
)
