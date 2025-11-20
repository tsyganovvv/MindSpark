from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def health():
    return {"status": "OK", "service": "coach-api"}

@router.get("/detailed")
async def detailed_health():
    return {
        "status": "healthy",
        "service": "AI Coach API", 
        "version": "1.0.0"
    }