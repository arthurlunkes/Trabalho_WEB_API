from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.config.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}