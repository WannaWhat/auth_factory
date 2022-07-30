import requests
import json

BASE_URL = 'http://localhost:9091/'


def start():
    # sign = SignRequestModel(**{"alg": "hmac_sha256", "sub": "auth", "aud": "some site", "body": {'some': 234},
    #                            'exp': datetime.datetime.now() + timedelta(minutes=10),
    #                            'nbf': datetime.datetime.now()})
    sign_model = {"alg": "hmac_sha256", "sub": "auth", "aud": "some site", "body": {'some': 234}, "tlt": 600}
    response = requests.post(BASE_URL + 'api/v1/sign', data=json.dumps(sign_model))
    data = response.json()
    token = data['token']
    print(token)
    response = requests.post(BASE_URL + 'api/v1/verify_sign', data=json.dumps({'token': token}))
    print(response.content)
    response = requests.post(BASE_URL + 'api/v1/verify', data=json.dumps({'token': token}))
    print(response.content)

    response = requests.get(BASE_URL + 'api/algorithms')
    print(response.content)
