from abc import ABC
from pydantic import BaseModel


class BaseDto(BaseModel, ABC):
    pass
