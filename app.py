from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai
import logging

# Initialize router
router = APIRouter()

# Setup logging
logging.basicConfig(level=logging.INFO)

# Request model
class ChatRequest(BaseModel):
    message: str

# Response model (optional for clarity)
class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Handles incoming chat messages and returns AI-generated response.
    """
    logging.info(f"Received message: {request.message}")

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.message}]
        )
        reply = completion.choices[0].message["content"]
        logging.info("Generated response successfully.")
        return {"response": reply}

    except Exception as e:
        logging.error(f"OpenAI error: {str(e)}")
        raise HTTPException(status_code=500, detail="AI response failed.")
        
