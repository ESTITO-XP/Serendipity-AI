if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8000))
    
    uvicorn.run(
        "app:app",
        host="0.0.0.0",  # ← Make sure this is 0.0.0.0
        port=port,
        reload=False     # ← Turn off reload for production
    )
