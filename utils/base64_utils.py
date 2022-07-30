import json
from base64 import urlsafe_b64encode, urlsafe_b64decode


def dict_to_base64_urlsafe(value: dict) -> bytes:
    return urlsafe_b64encode(json.dumps(value).encode())


def dict_from_base64_urlsafe(value: bytes) -> dict:
    return json.loads(urlsafe_b64decode(value))
