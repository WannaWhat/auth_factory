from base64 import urlsafe_b64encode, urlsafe_b64decode
import json


def dict_to_base64_urlsafe(dict_value: dict) -> bytes:
    return urlsafe_b64encode(json.dumps(dict_value).encode())


def dict_from_base64_urlsafe(base_value: bytes) -> dict:
    return json.loads(urlsafe_b64decode(base_value))
