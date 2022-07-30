from typing import List

from pydantic import BaseModel


class SupportedAlgorithmsResponseModel(BaseModel):
    code: int
    algorithms: List[str]
