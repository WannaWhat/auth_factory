from fastapi import APIRouter

from jwt import jwt
from jwt.models import SignModels
from settings import HASH_SECRET_KEY
from web.models import VerifyToken

# Blueprint route
router = APIRouter(
    prefix='/v1',
    responses={404: {'code': 404, 'message': 'Not found'}},
)


# /api/v1/sign
@router.post('/sign', status_code=200, response_model=SignModels.SignResponseModel)
def api_sign(request_data: SignModels.SignRequestModel):
    jwt_obj = jwt.JWT.create(request_data, key=HASH_SECRET_KEY)
    return {
        'code': 0,
        'token': jwt_obj.token,
    }


# /api/v1/verify
@router.post('/verify', status_code=200, response_model=VerifyToken.VerifyResponseModel)
def api_verify(request_data: VerifyToken.VerifyRequestSignature):
    jwt_obj = jwt.JWT(request_data.token)
    return {
        'code': 0,
        'token': jwt_obj.token,
        'status': jwt_obj.verify(HASH_SECRET_KEY),
    }


# /api/v1/verify_sign
@router.post('/verify_sign', status_code=200, response_model=VerifyToken.VerifyResponseModel)
def api_verify_sign(request_data: VerifyToken.VerifyRequestSignature):
    jwt_obj = jwt.JWT(request_data.token)

    return {
        'code': 0,
        'token': jwt_obj.token,
        'status': jwt_obj.verify_sign(HASH_SECRET_KEY),
    }
