from fastapi import APIRouter

from src.app.infrastructure.settings import Settings

settings = Settings()

BasicAuthRouter = APIRouter(
    prefix='/v1/auth/basic', tags=['basic_auth']
)


@BasicAuthRouter.get("/signin")
async def basic_auth_signin():
    pass


@BasicAuthRouter.get("/login")
async def basic_auth_login():
    pass


@BasicAuthRouter.delete("/logout")
async def basic_auth_logout():
    pass
