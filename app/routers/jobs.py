from fastapi import APIRouter, HTTPException

from app.schemas.Job_response import JobResponse
from app.services.job_service import JobService

router = APIRouter(tags=["Jobs"])


@router.get("/api/jobs/{job_id}", response_model=JobResponse)

def get_job(job_id: str):

    job = JobService.get_job(job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found.")

    return job