from typing import Optional
from pydantic import BaseModel
from app.enums.job_status import JobStatus
from app.enums.task_type import TaskType


class WebhookRequest(BaseModel):

    job_id: str

    status: JobStatus

    task_type: TaskType

    output_url: Optional[str] = None

    error_message: Optional[str] = None