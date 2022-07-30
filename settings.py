import os

from dotenv import load_dotenv

load_dotenv('configs/.env')

HASH_SECRET_KEY = os.environ.get('HMAC_SECRET_KEY', '').encode()
SERVER_HOST = os.environ.get('SERVER_HOST')
SERVER_PORT = int(os.environ.get('SERVER_PORT'))

TOKEN_TYP = 'jwt'
MAX_API_VERSION = '1.0.0'
