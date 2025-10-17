from fastapi import APIRouter, Request
from pydantic import BaseModel

chat_router = APIRouter()

class ChatInput(BaseModel):
    message: str

@chat_router.post("/")
async def chat(input: ChatInput):
    user_message = input.message
    # Placeholder response logic
    return {"response": f"Echo: {user_message}"}
    
