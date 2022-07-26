from base64 import urlsafe_b64encode
from datetime import datetime

from jwt.algorithms.BaseAlgorithm import AlgorithmParentClass
from jwt.models import SignModels
from utils import base64_utils
from settings import TOKEN_TYP


class JWT(object):
    def __init__(self, token: bytes, *args, **kwargs):
        self.token = token
        self._header = None
        self._clear_header = None
        self._payload = None
        self._clear_payload = None
        self._signature = None
        if not kwargs.get('_not_init_token'):
            self._disassemble()

    def _disassemble(self):
        items = self.token.split(b'.')
        if len(items) != 3:
            raise ValueError('Cant disassemble jwt token')
        self._header, self._payload, self._signature = items

    def _clear(self):
        if self.header is None:
            raise ValueError('Cant perform header from base64, header is None')
        self._clear_header = base64_utils.dict_from_base64_urlsafe(self.header)
        if self.payload is None:
            raise ValueError('Cant perform payload from base64, payload is None')
        self._clear_payload = base64_utils.dict_from_base64_urlsafe(self.payload)

    def verify(self, key: bytes) -> bool:
        if not self.verify_sign(key):
            return False
        now_timestamp = datetime.now().timestamp()
        if self.clear_payload.get('nbf') is not None and (self.clear_payload.get('nbf') or 0) > now_timestamp:
            return False
        if self.clear_payload.get('exp') is None:
            return False
        if self.clear_payload.get('exp') < now_timestamp:
            return False
        return True

    def verify_sign(self, key: bytes) -> bool:
        if self.clear_header.get('typ') != TOKEN_TYP:
            return False
        alg = self.clear_header.get('alg')
        if alg is None:
            return False
        alg_class = AlgorithmParentClass.algorithm_enum_name_join(alg)
        return self.compile_signature(alg_class.func, b'.'.join((self.header, self.payload)), key) == self.signature

    def compile_signature(self, signature_func, signing_data: bytes, key: bytes) -> bytes:
        return signature_func(key, signing_data)

    @property
    def header(self):
        return self._header

    @property
    def clear_header(self):
        if self._clear_header is None:
            self._clear()
        return self._clear_header

    @property
    def payload(self):
        return self._payload

    @property
    def clear_payload(self):
        if self._clear_payload is None:
            self._clear()
        return self._clear_payload

    @property
    def signature(self):
        return self._signature

    @property
    def _joined_header_payload(self) -> bytes:
        return b'.'.join((self.header, self.payload))

    @classmethod
    def create(cls, *args, key: bytes = None, **kwargs):
        if key is None:
            raise ValueError('Key must be not None')
        if args:
            if len(args) != 1:
                raise ValueError('To many args for jwt token')
            data = args[0]
        elif not kwargs:
            raise ValueError('Need args or kwargs for creation jwt')
        else:
            data = SignModels.SignRequestModel(**kwargs)
        return cls._create(data, key)

    @classmethod
    def _create(cls, data: SignModels.SignRequestModel, key: bytes):
        jwt_obj = cls(b'', data, _not_init_token=True)
        jwt_obj._header = base64_utils.dict_to_base64_urlsafe(
            {
                'typ': TOKEN_TYP,
                'alg': data.alg.name
            })
        jwt_obj._payload = urlsafe_b64encode(
            data.json(include={'sub', 'aud', 'iat', 'exp', 'ltl', 'jti', 'nbf', 'body'}).encode())
        signature = jwt_obj.compile_signature(data.alg.func, jwt_obj._joined_header_payload, key)
        jwt_obj._signature = signature
        jwt_obj.token = jwt_obj._joined_header_payload + b'.' + jwt_obj.signature
        return jwt_obj

    def __str__(self):
        return self.token.decode()
