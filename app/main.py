from fastapi import FastAPI
from app.routers.Generate import router
from app.routers.Jobs import router as jobs_router

app = FastAPI()

app.include_router(router)
app.include_router(jobs_router)