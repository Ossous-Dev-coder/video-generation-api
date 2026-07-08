import uuid

from datetime import datetime, timezone
from app.models.Job import Job
from app.schemas.Generate_request import GenerateRequest
from app.schemas.Generate_response import GenerateResponse
from app.enums.job_status import JobStatus
from app.schemas.Job_response import JobResponse


class JobService:

    _jobs: dict[str, Job] = {}

    @staticmethod
    def create_job(request: GenerateRequest) -> GenerateResponse:

        job = Job(
            job_id=str(uuid.uuid4()),
            task_type=request.task_type,
            prompt=request.prompt,
            duration=request.duration,
            resolution=request.resolution,
            seed=request.seed,
            status=JobStatus.QUEUED, ## Assuming the job is queued initially
            progress=0,
            estimated_time_seconds=300,
            created_at=datetime.now(timezone.utc),
            started_at=None,   ## Assuming the job hasn't started yet, still in the queue
            completed_at=None, ## Assuming the job hasn't completed yet, still in the queue
            output_url=None,   ## Assuming the output URL is not known yet, as the job hasn't completed
            error_message=None 
        )

        JobService._jobs[job.job_id] = job

        return GenerateResponse(
            job_id=job.job_id,
            status=job.status,
            estimated_time_seconds=job.estimated_time_seconds,
            created_at=job.created_at
        )
    
    @staticmethod
    def get_job(job_id: str) -> JobResponse | None:

        job = JobService._jobs.get(job_id)
    
        if job is None:
            return None
    
        return JobResponse(
            job_id=job.job_id,
            status=job.status,
            progress=job.progress,
            task_type=job.task_type,
            prompt=job.prompt,
            duration=job.duration,
            resolution=job.resolution,
            seed=job.seed,
            estimated_time_seconds=job.estimated_time_seconds,
            created_at=job.created_at,
            started_at=job.started_at,
            completed_at=job.completed_at,
            output_url=job.output_url,
            error_message=job.error_message
        )