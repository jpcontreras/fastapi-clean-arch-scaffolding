from dotenv import load_dotenv
from fastapi import APIRouter, Request, Depends
from fastapi_sso.sso.facebook import FacebookSSO
import os

from sqlalchemy.orm import Session

from src.app.infrastructure.db.postgresql_connect import get_db
from src.auth.application.facebook_user_authenticator import FacebookUserAuthenticator
from src.auth.infrastructure.auth_flask_session import current_session, destroy_session
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


# Dependency
def create_facebook_user_authenticator_depends(db_session: Session = Depends(get_db)):
    return FacebookUserAuthenticator(PostgresAuthRepository(db_session))


@AuthRouter.get("/facebook/login")
async def facebook_login():
    return await sso.get_login_redirect()


@AuthRouter.get("/facebook/callback")
async def auth_callback(request: Request,
                        interactor: FacebookUserAuthenticator = Depends(create_facebook_user_authenticator_depends)):
    user = await sso.verify_and_process(request)
    interactor.run(user)
    return user


@AuthRouter.delete("/logout")
async def logout():
    destroy_session()
