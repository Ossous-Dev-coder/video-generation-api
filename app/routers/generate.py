from fastapi import APIRouter, status

from app.schemas.Generate_request import GenerateRequest

router = APIRouter(tags=["Generate"])


@router.post("/api/generate", status_code=status.HTTP_201_CREATED)

def generate(request: GenerateRequest):
    
    return request.model_dump()