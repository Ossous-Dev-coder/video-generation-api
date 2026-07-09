from fastapi import FastAPI
from app.routers.generate import router
from app.routers.jobs import router as jobs_router
from app.routers.webhook import router as webhook_router
from app.exceptions.handlers import register_exception_handlers

app = FastAPI()

app.include_router(router)
app.include_router(jobs_router)
app.include_router(webhook_router)

register_exception_handlers(app)