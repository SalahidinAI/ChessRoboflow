from fastapi import FastAPI
import uvicorn
from routers import predict, router
from database import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


chess_app = FastAPI()
chess_app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(chess_app, host='127.0.0.1', port=8000)

