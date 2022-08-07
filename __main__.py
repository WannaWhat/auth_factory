import uvicorn

from settings import SERVER_HOST, SERVER_PORT
from web import app

if __name__ == '__main__':
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT)
