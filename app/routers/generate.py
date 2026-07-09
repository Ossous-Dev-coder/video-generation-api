import uuid
from fastapi import APIRouter, status
from app.schemas.Generate_request import GenerateRequest
from app.schemas.Generate_response import GenerateResponse
from app.schemas.Upload_response import UploadResponse
from app.schemas.Upload_response import UploadResponse
from app.services.job_service import JobService
from fastapi import BackgroundTasks

router = APIRouter(tags=["Generate"])

@router.post("/api/generate", response_model=GenerateResponse,status_code=status.HTTP_201_CREATED)

def generate(request: GenerateRequest, background_tasks: BackgroundTasks):
    response = JobService.create_job(request)

    ## Comment out this to try out the webhook functionality.
    background_tasks.add_task(JobService.process_job, response.job_id)

    return response


@router.get("/api/generate/signed-upload-url",response_model=UploadResponse)
def get_signed_upload_url():

    file_name = f"{uuid.uuid4()}.png" ## Generate a unique file name

    public_url = (f"https://bucket.s3.amazonaws.com/uploads/user_123/{file_name}")

    upload_url = (public_url+ "?AWSAccessKeyId=mock" + "&Signature=mock_signature")

    return UploadResponse(
        upload_url=upload_url,
        public_url=public_url,
        expires_in_seconds=3600
    )