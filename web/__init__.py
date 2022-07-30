from fastapi import FastAPI

from web.models import MaxAllowedVersion, SupportedAlgorithms, VerifyToken
from web import api

app = FastAPI()
app.include_router(api.router)


@app.get('/')
def index():
    return {'code': 0}
