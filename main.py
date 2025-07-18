from fastapi import FastAPI

app = FastAPI(
    title="Serendipity AI",
    description="Your supportive AI companion for delightful discoveries.",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to Serendipity AI!"}

@app.get("/about")
def about():
    return {
        "project": "Serendipity AI",
        "description": "Your supportive AI companion for delightful discoveries.",
        "status": "In progress",
        "open_source": True
    }
  
