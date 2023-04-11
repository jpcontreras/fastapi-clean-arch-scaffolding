from fastapi import APIRouter

HealthRouter = APIRouter(
    prefix='/v1/health', tags=['health']
)


@HealthRouter.get("/")
async def health():
    return {'message': 'Service is Up!'}
