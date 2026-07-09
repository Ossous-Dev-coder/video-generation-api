from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=400,
            content={
                "error": "validation_error",
                "message": str(exc)
            }
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):

        error = {
            400: "validation_error",
            401: "unauthorized",
            402: "insufficient_credits",
            404: "not_found",
            500: "internal_server_error"
        }.get(exc.status_code, "error")

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": error,
                "message": exc.detail
            }
        )
    
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "error": "internal_server_error",
                "message": "An unexpected error occurred."
            }
    )













