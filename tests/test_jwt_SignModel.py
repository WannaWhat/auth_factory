import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from jwt.models.SignModels import SignRequestModel


# TODO: Write tests for SignRequestModel
# That test enter non-existent algorithm to SingRequestModel
def test_not_existent_algorithm():
    pass


# That expired time smaller than iat
def test_expired_time_smaller_than_iat():
    pass


# ltl time smaller than zero or zero
def test_ltl_smaller_than_zero():
    pass


