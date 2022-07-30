from base64 import urlsafe_b64encode
import json
import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from utils import base64_utils


def test_dict_to_from_base64():
    testing_dicts = [
        {"some_value": 121,
         "another_value": "value"},
        {"dsdfdf": "dsfsdf",
         "body": {"some": 321},
         }
    ]
    for _t in testing_dicts:
        base64_data: bytes = base64_utils.dict_to_base64_urlsafe(_t)
        assert urlsafe_b64encode(json.dumps(_t).encode()) == base64_data
        assert _t == base64_utils.dict_from_base64_urlsafe(base64_data)
