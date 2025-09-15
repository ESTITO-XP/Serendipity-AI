from fastapi import APIRouter, Request
import openai
import os

router = APIRouter()
openai.api_key = os.getenv("OPENAI_API_KEY")

@router.post("/chat")
async def chat(request: Request):
    body = await request.json()
    message = body.get("message", "")
    session_id = body.get("session_id", "default")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        temperature=0.7
    )

    reply = response.choices[0].message["content"]

    return {
        "response": reply,
        "session_id": session_id,
        "version": os.getenv("APP_VERSION", "8.0")
    }
  
