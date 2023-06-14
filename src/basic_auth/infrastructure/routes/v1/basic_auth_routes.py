from fastapi import APIRouter, Depends
from src.app.infrastructure.settings import Settings
from src.basic_auth.application.create_basic_user_interactor import CreateBasicUserInteractor
from src.basic_auth.domain.basic_auth_user_dto import BasicAuthUserDto
from src.basic_auth.infrastructure.basic_auth_depends import create_basic_user_depends

settings = Settings()

BasicAuthRouter = APIRouter(
    prefix='/v1/auth/basic', tags=['basic_auth']
)


@BasicAuthRouter.post("/signup")
def basic_auth_signup(basic_user_dto: BasicAuthUserDto,
                      create_basic_user: CreateBasicUserInteractor = Depends(create_basic_user_depends)):
    return create_basic_user.run(basic_user_dto)


@BasicAuthRouter.get("/login")
async def basic_auth_login():
    pass


@BasicAuthRouter.delete("/logout")
async def basic_auth_logout():
    pass
