import urllib.parse

from ..config import settings

def generate_google_oauth_redirect_uri():
    base_uri = "https://accounts.google.com/o/oauth2/v2/auth"
    query_params = {
        "redirect_uri":"http://localhost:5173/auth/google",
        "client_id":f"{settings.OAUTH_GOOGLE_CLIENT_ID}",
        "response_type":"code",
        "scope":" ".join([
            "openid",
            "profile",
            "email",
        ]),
        #state: ...
    }
    query_string = urllib.parse.urlencode(query_params, quote_via=urllib.parse.quote)
    return f"{base_uri}?{query_string}"