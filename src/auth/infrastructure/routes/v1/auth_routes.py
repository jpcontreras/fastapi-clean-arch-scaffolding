from fastapi import APIRouter, Request, Depends
from fastapi_sso.sso.facebook import FacebookSSO
from fastapi.responses import RedirectResponse
from src.app.infrastructure.settings import Settings
from src.auth.application.facebook_user_authenticator import FacebookUserAuthenticator
from src.auth.application.generate_user_token import GenerateUserToken
from src.auth.infrastructure.auth_depends import create_facebook_user_authenticator_depends

settings = Settings()

AuthRouter = APIRouter(
    prefix='/v1/auth', tags=['auth']
)

sso = FacebookSSO(
    client_id=settings.FB_CLIENT_ID,
    client_secret=settings.FB_CLIENT_SECRET,
    redirect_uri=settings.FB_REDIRECT_URI,
)


@AuthRouter.get("/facebook/login")
async def facebook_login(return_url: str):
    return await sso.get_login_redirect(state=return_url)


@AuthRouter.get("/facebook/callback")
async def auth_callback(request: Request,
                        fb_authenticator: FacebookUserAuthenticator = Depends(create_facebook_user_authenticator_depends),
                        generate_token: GenerateUserToken = Depends()):
    user = await sso.verify_and_process(request)
    auth_user = fb_authenticator.run(user)
    token = generate_token.run(auth_user)
    return RedirectResponse(url=sso.state, headers={"Authorization": f"Bearer {token}"})


@AuthRouter.delete("/logout")
async def logout():
    pass
