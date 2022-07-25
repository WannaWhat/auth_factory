# from hashlib import sha256
# from datetime import datetime, timedelta
# from base64 import urlsafe_b64encode
# import hmac
# from uuid import uuid4
# import json
#
# SECRET_KEY = "Secret Key".encode()
#
# headers = {
#     "typ": "jwt",
#     "alg": "HS256"
# }
#
#
# payload = {
#     "iss": "auth_factory_121",
#     "sub": "user_auth",
#     "aud": "sml_api",
#     "exp": (datetime.now() + timedelta(minutes=5)).timestamp(),
#     "iat": datetime.now().timestamp(),
#     "nbf": (datetime.now() + timedelta(minutes=1)).timestamp(),  # Not before, token will be accepted after that time
#     "jti": uuid4().hex,
#     "body": {
#         "admin": True,
#         "user_id": 234213434,
#     }
# }
# segments = [headers, payload]
# segments = list(map(lambda x: json.dumps(x, separators=(",", ":")).encode(), segments))
# segments = list(map(lambda x: urlsafe_b64encode(x), segments))
# signing_value = b".".join(segments)
# signature = hmac.new(SECRET_KEY, signing_value, sha256).digest()
# segments.append(urlsafe_b64encode(signature))
# token = b".".join(segments)
# print(token.decode())


from models.request import sign
# from jwt import hwt