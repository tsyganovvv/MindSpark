from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import chat, health

app = FastAPI(title="Coach AI API", version="1.0.0")

#settings CORS
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/v1/chat", tags=["chat"])
app.include_router(health.router, prefix="/api/v1/health", tags=["health"])


@app.get("/")
async def root():
    return {"message": "Coach AI API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

