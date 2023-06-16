from pydantic import BaseModel
from fastapi import Response
from src.app.application.base_interactor import OutputSuccessContext, OutputErrorContext


class RenderSuccessFormat(BaseModel):
    success: bool = True
    message: str
    data: list


class RenderErrorFormat(BaseModel):
    success: bool = False
    code: str
    message: str
    description: str


def create_api_response(output_result: OutputSuccessContext | OutputErrorContext,
                        response: Response) -> RenderSuccessFormat | RenderErrorFormat:
    response.status_code = output_result.http_status
    if not output_result.success:
        return RenderErrorFormat(
            success=False,
            code=output_result.code,
            message=output_result.message,
            description=output_result.description
        )
    if output_result.success:
        return RenderSuccessFormat(
            success=True,
            data=output_result.data,
            message=output_result.message
        )
