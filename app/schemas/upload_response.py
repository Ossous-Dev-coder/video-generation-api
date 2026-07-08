from pydantic import BaseModel

class UploadResponse(BaseModel):
    upload_url: str

    public_url: str

    expires_in_seconds: int

    