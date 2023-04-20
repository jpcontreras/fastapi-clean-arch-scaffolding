import os

from flask import session, Flask
from fastapi import Request, HTTPException

flask_app = Flask(__name__)
flask_app.secret_key = os.getenv('SESSION_SECRET_KEY')


async def create_session(user_uid: str):
    session['uid'] = user_uid


async def current_session(request: Request):
    user_session = session.get('uid')
    if user_session is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user_session


async def destroy_session():
    session.clear()
