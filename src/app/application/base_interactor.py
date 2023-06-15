from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel
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
        pass

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
        # Public method to execute the interactor
        self.validate(input_dto)
        return self.process(input_dto)
