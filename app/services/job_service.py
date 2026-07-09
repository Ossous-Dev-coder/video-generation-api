import uuid
import time
from datetime import datetime, timezone
from app.models.Job import Job
from app.schemas.generate_request import GenerateRequest
from app.schemas.generate_response import GenerateResponse
from app.enums.job_status import JobStatus
from app.schemas.job_response import JobResponse
from app.schemas.webhook_request import WebhookRequest


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
    def process_job(job_id: str): ## Simulating the processing of a job.

        job = JobService._jobs.get(job_id)

        if job is None:
            return

        time.sleep(10)

        job.status = JobStatus.RUNNING
        job.started_at = datetime.now(timezone.utc)

        job.progress = 25

        time.sleep(5)

        job.progress = 50

        time.sleep(5)

        job.progress = 75

        time.sleep(5)

        job.progress = 100
        job.status = JobStatus.COMPLETED
        job.completed_at = datetime.now(timezone.utc)

        job.output_url = (f"https://bucket.s3.amazonaws.com/output/{job.job_id}.mp4")
    
    @staticmethod
    def complete_job(request: WebhookRequest):

        job = JobService._jobs.get(request.job_id)
    
        if job is None:
            return False
    
        job.status = request.status
    
        job.completed_at = datetime.now(timezone.utc)
    
        if request.status == JobStatus.COMPLETED:
        
            job.progress = 100
    
            job.output_url = request.output_url
    
        elif request.status == JobStatus.FAILED:
        
            job.error_message = request.error_message
    
        return True

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