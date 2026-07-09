from fastapi import APIRouter, Header, HTTPException, status

from app.schemas.webhook_request import WebhookRequest
from app.services.job_service import JobService

router = APIRouter(tags=["Webhook"])

WEBHOOK_SECRET = "wh_test_secret"


@router.post("/api/webhook/job_complete")
def job_complete(request: WebhookRequest,x_webhook_secret: str = Header(...)):

    if x_webhook_secret != WEBHOOK_SECRET:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid webhook secret.")

    updated = JobService.complete_job(request)

    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job not found.")

    return {
        "message": "Webhook processed successfully."
    }