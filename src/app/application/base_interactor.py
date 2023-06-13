from abc import ABC, abstractmethod

from src.app.domain.base_dto import BaseDto


class BaseInteractor(ABC):
    @abstractmethod
    def __init__(self):
        # Initialize common interactor attributes
        pass

    @abstractmethod
    def process(self, input_dto: BaseDto):
        # logic to process input data
        # You must implement this function in the child classes
        pass

    def run(self, input_dto: BaseDto):
        # Public method to execute the interactor
        input_dto.is_valid()
        return self.process(input_dto)
