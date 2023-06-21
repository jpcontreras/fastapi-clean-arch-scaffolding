from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel
from starlette import status
from src.app.domain.base_dto import BaseDto
from src.basic_auth.domain.basic_auth_user_dto import BasicAuthUserDto


class OutputSuccessContext(BaseModel):
    success: bool = True
    http_status: int
    data: List[BasicAuthUserDto]
    message: str


class OutputErrorContext(BaseModel):
    success: bool = False
    http_status: int
    code: str
    message: str
    description: str


class BaseInteractor(ABC):
    @abstractmethod
    def __init__(self):
        # Initialize common interactor attributes
        self.translate = None

    @abstractmethod
    def process(self, input_dto: BaseDto) -> OutputSuccessContext | OutputErrorContext:
        # logic to process input data
        # You must implement this function in the child classes
        pass

    @abstractmethod
    def validate(self, input_dto: BaseDto):
        # logic to validate input data
        # You must implement this function in the child classes
        pass

    def run(self, input_dto: BaseDto) -> OutputSuccessContext | OutputErrorContext:
        try:
            # Public method to execute the interactor
            self.validate(input_dto)
            return self.process(input_dto)
        except Exception as e:
            # TODO: Log error integration with Sentry or similar
            return OutputErrorContext(
                http_status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                code=self.translate.text('api.errors.unknown_error.code'),
                message=self.translate.text('api.errors.unknown_error.message'),
                description=self.translate.text('api.errors.unknown_error.description')
            )
