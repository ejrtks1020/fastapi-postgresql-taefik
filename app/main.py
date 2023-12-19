from fastapi import FastAPI
from common.database import User, database
from contextlib import asynccontextmanager
import uvicorn
from common.logger import Logger



logger = Logger.getLogger(__name__)



@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("startup")
    if not database.is_connected:
        await database.connect()
    await User.objects.get_or_create(email="test@test.com")

    yield 

    logger.info("shutdown")
    if database.is_connected:
        await database.disconnect()

app = FastAPI(
    title="FastAPI, Docker, and Traefik",
    lifespan=lifespan
)

@app.get("/")
async def read_root():
    return await User.objects.all()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)