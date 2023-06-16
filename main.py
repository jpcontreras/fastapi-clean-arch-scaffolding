from fastapi import FastAPI
from dotenv import load_dotenv
import os

from pyi18n import PyI18n

from src.app.infrastructure.routes.v1.health_checks import HealthRouter
from src.auth.infrastructure.routes.v1.auth_routes import AuthRouter
from src.basic_auth.infrastructure.routes.v1.basic_auth_routes import BasicAuthRouter

load_dotenv()

# Core Application Instance
app = FastAPI(
    title=os.getenv('APP_NAME'),
    version=os.getenv('API_VERSION'),
)

root_path = os.path.dirname(os.path.abspath(__file__))
# i18n: PyI18n = PyI18n(('es', 'en'), load_path=f"{root_path}/locales/")
# t: callable = i18n.gettext

app.include_router(HealthRouter)
app.include_router(AuthRouter)
app.include_router(BasicAuthRouter)
