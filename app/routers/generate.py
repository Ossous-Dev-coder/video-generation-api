from fastapi import APIRouter, status

from app.schemas.Generate_request import GenerateRequest
from app.schemas.Generate_response import GenerateResponse
from app.services.Job_service import JobService

router = APIRouter(tags=["Generate"])
    
@router.post("/api/generate", response_model=GenerateResponse,status_code=status.HTTP_201_CREATED)
def generate(request: GenerateRequest):
    return JobService.create_job(request)