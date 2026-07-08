from datetime import datetime

from pydantic import BaseModel


class GenerateResponse(BaseModel):
    job_id: str
    status: str
    estimated_time_seconds: int
    created_at: datetime