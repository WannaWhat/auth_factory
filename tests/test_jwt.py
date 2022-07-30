import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from jwt.jwt import JWT


# Test verify_sign with normal key and bad key
def test_jwt_verify_sign():
    jwt_obj = JWT.create(alg='hmac_sha256', sub='some_sub_auth_exmp', aud='some_aud',
                  tlt=10, body={'user_id': 1321}, key=b'Key')
    assert jwt_obj.verify_sign(b'Key')
    assert not jwt_obj.verify(b'NotKey')


# TODO: Write all tests for jwt
# Test verify with not expired time and expired time
def test_jwt_verify_exp():
    pass


# Test verify with not before time
def test_jwt_verify_nbf():
    pass


# Test verify with not before time and expired time
def test_jwt_verify_nbf_exp():
    pass


# Test jwt payload in token
def test_jwt_payload_in_token():
    pass


# Test jwt verify signature with all hash algorithms
def test_jwt_hash_algorithms():
    pass


# Test jwt verify signature with all asymmetric algorithms
def test_jwt_asymmetric_algorithms():
    pass
