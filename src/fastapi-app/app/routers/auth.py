import aiohttp

from fastapi import APIRouter, Body
from fastapi.responses import RedirectResponse

from ..services.outh_google import generate_google_oauth_redirect_uri
from ..config import settings

router = APIRouter()

@router.get("/google/url")
def get_google_oauth_redirect_uri():
    uri = generate_google_oauth_redirect_uri()
    return RedirectResponse(url=uri, status_code=302)


@router.post("/google/callback")
async def handle_code(
    code: str = Body(..., embed=True),
):
    google_token_url = settings.GOOGLE_TOKEN_URL
    
    async with aiohttp.ClientSession() as session, session.post(
        url=google_token_url,
        data={
            "client_id":settings.OAUTH_GOOGLE_CLIENT_ID,
            "client_secret":settings.OAUTH_GOOGLE_CLIENT_SECRET,
            "grant_type":"authorization_code",
            "redirect_uri":"http://localhost:80/auth/google",
            "code":code,
        },
        ssl=False,
    ) as response:
        res = await response.json()
        print(res)

