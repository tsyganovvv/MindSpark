from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.neural_service import neuro_service
from typing import Dict

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    user_id: str = "test_user"


class ChatResponse(BaseModel):
    response: str
    user_id: str


@router.post("/message", response_model=ChatResponse)
async def send_message(request: ChatRequest):
    try:
        response = await neuro_service.generate_response(request.message)
        return ChatResponse(response=response,
                            user_id=request.user_id
                            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/test")
async def test_chat() -> Dict[str, str]:
    return {"message": "chat router is working"}

