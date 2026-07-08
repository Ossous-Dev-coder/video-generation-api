from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.enums.task_type import TaskType
from app.enums.job_status import JobStatus


class JobResponse(BaseModel):
    job_id: str

    status: JobStatus

    progress: int

    task_type: TaskType

    prompt: str

    duration: int

    resolution: str

    seed: int

    estimated_time_seconds: int

    created_at: datetime

    started_at: Optional[datetime] = None

    completed_at: Optional[datetime] = None

    output_url: Optional[str] = None

    error_message: Optional[str] = None