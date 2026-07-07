from fastapi import FastAPI
from app.routers.Generate import router

app = FastAPI()

app.include_router(router)