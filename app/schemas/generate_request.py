from pydantic import BaseModel
from typing import Optional
from app.enums.task_type import TaskType
from pydantic import model_validator


class GenerateRequest(BaseModel):

    task_type: TaskType
    prompt: str
    
    ref_imgs: Optional[list[str]] = None
    duration: Optional[int] = 5
    resolution: Optional[str] = "720P"
    seed: Optional[int] = 42
    num_inference_steps: Optional[int] = 25
    guidance_scale: Optional[float] = 5.0
    guidance_scale_img: Optional[float] = 3.0
    negative_prompt: Optional[str] = ""
    offload: Optional[bool] = False
    low_vram: Optional[bool] = False
    input_video: Optional[str] = None
    input_image: Optional[str] = None
    input_audio: Optional[str] = None

