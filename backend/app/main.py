from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import files
from app.database import init_db

app = FastAPI()

app.include_router(files.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()