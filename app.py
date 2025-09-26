# app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import route modules
from routes.chat import router as chat_router
# from routes.voice import router as voice_router
# from routes.image import router as image_router
# from routes.video import router as video_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Serendipity AI",
        description="Creator-first workspace for memory, modularity, and momentum",
        version="7.0"
    )

    # CORS setup
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Replace with specific domains if needed
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routes
    app.include_router(chat_router, prefix="/api/chat")
    # app.include_router(voice_router, prefix="/api/voice")
    # app.include_router(image_router, prefix="/api/image")
    # app.include_router(video_router, prefix="/api/video")

    return app

app = create_app()
