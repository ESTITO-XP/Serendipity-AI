from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import router  # app.py v3 handles routing
import logging

# Initialize FastAPI app
app = FastAPI(
    title="Serendipity AI",
    description="Creator-first workspace powered by FastAPI + OpenAI",
    version="12.0.0"
)

# Setup logging
logging.basicConfig(level=logging.INFO)
logging.info("SAI v12.0 booting up...")

# CORS middleware (open for dev, tighten for prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include chat routes from app.py
app.include_router(router)

# Health check endpoint
@app.get("/health")
def health_check() -> dict:
    """
    Returns status of the API.
    """
    return {"status": "ok", "version": "12.0.0"}

# Entry point for local dev
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
    
