from settings import HASH_SECRET_KEY
from jwt.models import SignModels
from jwt import jwt
from web.models import VerifyToken

from fastapi import APIRouter

# Blueprint route
router = APIRouter(
    prefix='/v1',
    responses={404: {"code": 404, "message": "Not found"}}
)


# /api/v1/sign
@router.post('/sign', status_code=200)
def api_sign(data: SignModels.SignRequestModel):
    jwt_obj = jwt.JWT.create(data, key=HASH_SECRET_KEY)
    return {
        'code': 0,
        'token': jwt_obj.token
    }


# /api/v1/verify
@router.post('/verify', status_code=200)
def api_verify(data: VerifyToken.VerifyRequestSignature):
    jwt_obj = jwt.JWT(data.token)
    response = {'code': 0,
                'token': jwt_obj.token}
    if jwt_obj.verify(HASH_SECRET_KEY):
        response['status'] = True
    else:
        response['status'] = False
    return response


# /api/v1/verify_sign
@router.post('/verify_sign', status_code=200)
def api_verify_sign(data: VerifyToken.VerifyRequestSignature):
    jwt_obj = jwt.JWT(data.token)

    response = {'code': 0,
                'token': jwt_obj.token}
    if jwt_obj.verify_sign(HASH_SECRET_KEY):
        response['status'] = True
    else:
        response['status'] = False
    return VerifyToken.VerifyResponseModel(**response)
