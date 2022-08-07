from fastapi import APIRouter


from jwt.algorithms.BaseAlgorithm import AlgorithmParentClass
from settings import MAX_API_VERSION
from web.api.v1 import sign_verif
from web.models import MaxAllowedVersion, SupportedAlgorithms

# Blueprint route
router = APIRouter(
    prefix='/api',
    responses={404: {'code': 404, 'message': 'Not found'}}
)
router.include_router(sign_verif.router)


# /api/version
@router.get('/version', response_model=MaxAllowedVersion.VersionResponseModel, status_code=200)
def version():
    return {
        'code': 0,
        'version': MAX_API_VERSION,
    }


# /api/algorithms
@router.get('/algorithms', response_model=SupportedAlgorithms.SupportedAlgorithmsResponseModel)
def supported_algorithms():
    return {
        'code': 0,
        'algorithms': AlgorithmParentClass.supported_algorithms,
    }
