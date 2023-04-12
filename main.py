from fastapi import FastAPI
from dotenv import load_dotenv
import os
from src.app.infrastructure.routes.v1.health_checks import HealthRouter
from src.auth.infrastructure.routes.v1.auth_routes import AuthRouter

load_dotenv()

# Core Application Instance
app = FastAPI(
    title=os.getenv('APP_NAME'),
    version=os.getenv('API_VERSION'),
)


app.include_router(HealthRouter)
app.include_router(AuthRouter)
