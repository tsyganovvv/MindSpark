from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .routers import chat, health, auth
from .database import engine
from .models.users import Base


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield

    await engine.dispose()


app = FastAPI(title="MindSparkAPI",
              description="API for MindSpark",
              version="1.0.0",
              lifespan=lifespan,
              )

#settings CORS
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/health", tags=["health"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/")
async def root():
    return {"message": "Coach AI API is running!"}

