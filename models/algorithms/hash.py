import hmac
from base64 import urlsafe_b64encode
from hashlib import sha256

from models.algorithms.BaseAlgorithm import AlgorithmParentClass, AlgorithmTypesEnum


# classes of supported algorithms
class hs256(AlgorithmParentClass):
    name = 'hmac_sha256'
    alg_type = AlgorithmTypesEnum.HASH_SUM
    func = (lambda key, value: urlsafe_b64encode(hmac.new(key, value, sha256).digest()))


class s256(AlgorithmParentClass):
    name = 'sha256'
    alg_type = AlgorithmTypesEnum.HASH_SUM
    func = (lambda key, value: urlsafe_b64encode(sha256(value + key).digest()))
