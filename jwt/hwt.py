import hmac
from settings import HASH_SECRET_KEY
from hashlib import sha256
from base64 import urlsafe_b64encode


class BaseAlgorithm(object):
    alg = None
    hmac = False


class SupportedAlgorithms(object):
    class hs256(BaseAlgorithm):
        alg = sha256
        hmac = True

    class s256(BaseAlgorithm):
        alg = sha256
        hmac = False


class HWT(object):
    def __init__(self, secret_key: bytes):
        self._secret_key = secret_key

    def sign(self, message: bytes, alg) -> bytes:
        if not issubclass(alg, BaseAlgorithm):
            raise ValueError('Alg argument must be subclass from BaseAlgorithm')
        if alg.hmac:
            signature = hmac.new(self._secret_key, message, alg.alg).digest()
        else:
            signature = sha256(message + self._secret_key).digest()
        signature = urlsafe_b64encode(signature)
        return signature

    def verify(self, message: bytes, alg, signature: bytes) -> bool:
        return signature == self.sign(message, alg)


hwt = HWT(secret_key=HASH_SECRET_KEY)
# print(hwt.sign(b'Some', SupportedAlgorithms.hs256))
# print(hwt.verify(b'Some', SupportedAlgorithms.hs256, hwt.sign(b'Some', SupportedAlgorithms.hs256)))
#

