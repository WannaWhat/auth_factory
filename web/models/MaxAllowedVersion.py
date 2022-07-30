from pydantic import BaseModel


class VersionResponseModel(BaseModel):
    code: int
    version: str
