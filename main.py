# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import route modules
from routes.chat import router as chat_router
# from routes.voice import router as voice_router
# from routes.image import router as image_router
# from routes.video import router as video_router

app = FastAPI(
    title="Serendipity AI",
    description="Creator-first workspace for memory, modularity, and momentum",
    version="7.0"
)

# CORS setup for frontend/API access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific domains if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(chat_router, prefix="/api/chat")
# app.include_router(voice_router, prefix="/api/voice")
# app.include_router(image_router, prefix="/api/image")
# app.include_router(video_router, prefix="/api/video")

@app.get("/")
def read_root():
    return {"message": "Welcome to Serendipity AI — v7.0 is live."}
    
