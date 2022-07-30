import hmac
from base64 import urlsafe_b64encode
from hashlib import sha256

from jwt.algorithms.BaseAlgorithm import AlgorithmParentClass, AlgorithmTypesEnum


# Classes of supported algorithms
# Class for hmac_sha256
class HS256(AlgorithmParentClass):
    name = 'hmac_sha256'
    alg_type = AlgorithmTypesEnum.HASH_SUM
    func = (lambda key, value: urlsafe_b64encode(hmac.new(key, value, sha256).digest()))


# Class for sha256
class S256(AlgorithmParentClass):
    name = 'sha256'
    alg_type = AlgorithmTypesEnum.HASH_SUM
    func = (lambda key, value: urlsafe_b64encode(sha256(value + key).digest()))
