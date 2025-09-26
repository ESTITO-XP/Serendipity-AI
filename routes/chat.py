# routes/chat.py

from fastapi import APIRouter, Request
from pydantic import BaseModel
from utils.memory import get_context, update_context
from utils.response import generate_reply

router = APIRouter()

class ChatInput(BaseModel):
    user_id: str
    message: str

@router.post("/chat")
async def chat_endpoint(payload: ChatInput, request: Request):
    # Retrieve context for user
    context = get_context(payload.user_id)

    # Generate AI response
    reply = generate_reply(payload.message, context)

    # Update memory/context
    update_context(payload.user_id, payload.message, reply)

    return {"reply": reply}
    
