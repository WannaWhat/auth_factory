from dotenv import load_dotenv
import os

load_dotenv('configs/.env')

HASH_SECRET_KEY = os.environ.get('HMAC_SECRET_KEY').encode()
