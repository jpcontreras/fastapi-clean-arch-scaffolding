from abc import ABC, abstractmethod


class InteractorBase(ABC):
    @abstractmethod
    def __init__(self):
        # Initialize common interactor attributes
        pass

    @abstractmethod
    def validate_input_dto(self, input_dto):
        # Logic to validate input data
        # Manage error in case of invalid input data
        # You must implement this function in the child classes
        pass

    @abstractmethod
    def process(self, input_dto):
        # logic to process input data
        # You must implement this function in the child classes
        pass

    def run(self, input_dto):
        # Public method to execute the interactor
        self.validate_input_dto(input_dto)
        return self.process(input_dto)
