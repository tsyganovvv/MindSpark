import aiohttp
import jwt
from fastapi import APIRouter, Body

from ..services.outh_google import generate_google_oauth_redirect_uri
from ..config import settings

router = APIRouter()

@router.get("/google/url")
def get_google_oauth_redirect_uri():
    uri = generate_google_oauth_redirect_uri()
    return {"url": uri}


@router.post("/google/callback")
async def handle_code(code: str = Body(..., embed=True)):
    try:
        google_token_url = settings.GOOGLE_TOKEN_URL
        
        async with aiohttp.ClientSession() as session, session.post(
            url=google_token_url,
            data={
                "client_id": settings.OAUTH_GOOGLE_CLIENT_ID,
                "client_secret": settings.OAUTH_GOOGLE_CLIENT_SECRET,
                "grant_type": "authorization_code",
                "redirect_uri": "http://localhost:5173/auth/google",
                "code": code,
            },
            ssl=False,
        ) as response:
            token_data = await response.json()
            
            if "error" in token_data:
                return {
                    "error": token_data.get("error_description", token_data["error"])
                }
            
            id_token_jwt = token_data.get("id_token")
            
            if not id_token_jwt:
                return {"error": "No id_token received from Google"}
            
            try:
                decoded = jwt.decode(
                    id_token_jwt, 
                    options={"verify_signature": False}
                )
                
                user_email = decoded.get("email")
                user_name = decoded.get("name", "No name")
                
                return {
                    "email": user_email,
                    "name": user_name
                }
                
            except Exception as e:
                return {"error": f"Failed to decode token: {str(e)}"}
                
    except Exception as e:
        return {"error": f"Internal server error: {str(e)}"}

