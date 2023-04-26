from fastapi import APIRouter, Request, Depends
from fastapi_sso.sso.facebook import FacebookSSO
from sqlalchemy.orm import Session
from src.app.infrastructure.db.postgresql_connect import get_db
from src.app.infrastructure.settings import Settings
from src.auth.application.facebook_user_authenticator import FacebookUserAuthenticator
from src.auth.application.generate_token import GenerateToken
from src.auth.infrastructure.postgres_auth_repository import PostgresAuthRepository

settings = Settings()

AuthRouter = APIRouter(
    prefix='/v1/auth', tags=['auth']
)

sso = FacebookSSO(
    client_id=settings.FB_CLIENT_ID,
    client_secret=settings.FB_CLIENT_SECRET,
    redirect_uri=settings.FB_REDIRECT_URI,
)


# Dependency
def create_facebook_user_authenticator_depends(db_session: Session = Depends(get_db)):
    return FacebookUserAuthenticator(PostgresAuthRepository(db_session))


@AuthRouter.get("/facebook/login")
async def facebook_login():
    return await sso.get_login_redirect()


@AuthRouter.get("/facebook/callback")
async def auth_callback(request: Request,
                        fb_authenticator: FacebookUserAuthenticator = Depends(create_facebook_user_authenticator_depends),
                        generate_token: GenerateToken = Depends()):
    user = await sso.verify_and_process(request)
    auth_user = fb_authenticator.run(user)
    return generate_token.run(auth_user)


@AuthRouter.delete("/logout")
async def logout():
    pass
