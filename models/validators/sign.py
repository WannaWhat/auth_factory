from datetime import datetime, timedelta
from typing import Optional, Union, Dict
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, validator

# from models.algorithms.BaseAlgorithm import AlgorithmParentClass
from models.algorithms.hash import *

# Initial __new__ class. At this point enum is created
AlgorithmParentClass()


# Token validation class
class SignRequestModel(BaseModel):
    alg: AlgorithmParentClass.algorithms_enum  # Algorithm for calculate token signature
    sub: str = Field(max_length=32)  # Subject
    aud: str = Field(max_length=32)  # Auditor who will verify token
    iat: Union[datetime] = Field(default_factory=datetime.now)  # Token creation time
    exp: Optional[datetime] = None  # Token expired time
    nbf: Optional[datetime] = None  # Not before token will not validated before some time
    jti: Union[UUID] = Field(default_factory=uuid4)  # Token unique id
    tlt: Optional[int] = None  # Token Life Time custom claim

    body: Optional[Dict] = None  # Token body (information claim) custom claim

    # Algorithm validation class
    # From algorithm text name -> algorithm class with algorithm function
    @validator('alg')
    def alg_join_table_validator(cls, v, values, **kwargs) -> Optional[AlgorithmParentClass]:
        algorithm_class_obj = AlgorithmParentClass.algorithm_enum_value_join(v)
        if algorithm_class_obj is None:
            raise ValueError('alg is not compiled in SupportedAlgorithms class')
        return algorithm_class_obj

    # Validate that expire time greater than token created time
    @validator('exp')
    def exp_greater_then_iat_validator(cls, v, values, **kwargs):
        if v is not None and values.get('iat') is not None:
            if v.timestamp() < values['iat'].timestamp():
                raise ValueError('exp claim must be greater than iat claim')
        return v

    # Validate that token life time or token expire time exists
    # If token life time is None make token life time from expire time
    @validator('tlt', always=True)
    def time_identification_validator(cls, v, values, **kwargs):
        if v is not None and values.get('exp') is not None:
            raise ValueError('tlt and exp claims cant be setted together')
        if v is not None:
            if v < 0:
                raise ValueError('tlt must be greater or equal than 0')
            values['exp'] = values['iat'] + timedelta(seconds=v)
            return v
        elif values.get('exp') is None:
            raise ValueError('tlt or exp claims must be not None')
        else:
            return int(values['exp'].timestamp() - values['iat'].timestamp())


# try:
#     jwt_request = SignRequestModel(alg='s256', sub='auth', aud='some site', body={"some": 234}, tlt=600)
#     print(jwt_request.alg.func(b'1', b'dsf'))
# except ValidationError as e:
#     print(e.errors())
# except Exception as e:
#     print(e)
