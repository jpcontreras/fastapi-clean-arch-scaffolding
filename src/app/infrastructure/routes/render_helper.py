from pydantic import BaseModel


class RenderSuccessFormat(BaseModel):
    success: bool = True
    message: str
    data: list


class RenderErrorFormat(BaseModel):
    success: bool = False
    code: str
    message: str
    description: str
