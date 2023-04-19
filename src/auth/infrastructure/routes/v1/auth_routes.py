from dotenv import load_dotenv
from fastapi import APIRouter, Request, Depends
from fastapi_sso.sso.facebook import FacebookSSO
import os

from src.auth.application.facebook_user_authenticator import FacebookUserAuthenticator
from src.auth.domain.auth_repository import AuthRepository
from src.auth.infrastructure.postgres_auth_repository import PostgresAuthRepository

load_dotenv()

AuthRouter = APIRouter(
    prefix='/v1/auth', tags=['auth']
)

sso = FacebookSSO(
    client_id=os.getenv('FB_CLIENT_ID'),
    client_secret=os.getenv('FB_CLIENT_SECRET'),
    redirect_uri="http://localhost:8000/v1/auth/facebook/callback",
)

repository: AuthRepository = PostgresAuthRepository()
authenticator: FacebookUserAuthenticator = FacebookUserAuthenticator(repository)

@AuthRouter.get("/facebook/login")
async def facebook_login():
    return await sso.get_login_redirect()

@AuthRouter.get("/facebook/callback")
async def auth_callback(request: Request, interactor: FacebookUserAuthenticator = Depends()):
    user = await sso.verify_and_process(request)
    interactor.run(user)
    return user
