from typing import Union

from pydantic import BaseModel, validator


# Token validation verify class
class VerifyRequestSignature(BaseModel):
    token: Union[str, bytes]

    # Token format validator
    @validator('token')
    def token_validator(cls, v: Union[str, bytes], values, **kwargs) -> str:
        if type(v) is str:
            v = v.encode()
        if len(v.split(b'.')) != 3:
            raise ValueError('Token not in token format')
        return v


# Token validation response model
class VerifyResponseModel(BaseModel):
    code: int
    token: str
    status: bool

    # Token format validator
    @validator('token')
    def token_validator(cls, v: str, values, **kwargs) -> str:
        if len(v.split('.')) != 3:
            raise ValueError('Token not in token format')
        return v