from pydantic import BaseModel
from typing import Optional
from app.enums.task_type import TaskType
from pydantic import model_validator


class GenerateRequest(BaseModel):

    task_type: TaskType
    ref_imgs: Optional[list[str]] = None
    prompt: str
    
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

    @model_validator(mode="after")
    def validate_task_type(self):

        if self.task_type == TaskType.REFERENCE_TO_VIDEO:
            if not self.ref_imgs:
                raise ValueError("ref_imgs is required for REFERENCE_TO_VIDEO task type")
            
        elif self.task_type == TaskType.SINGLE_SHOT_EXTENSION:
            if not self.input_video:
                raise ValueError("input_video is required for SINGLE_SHOT_EXTENSION task type")
            
        elif self.task_type == TaskType.SHOT_SWITCHING_EXTENSION:
            if not self.input_video:
                raise ValueError("input_video is required for SHOT_SWITCHING_EXTENSION task type")
            
        elif self.task_type == TaskType.TALKING_AVATAR:
            if not self.input_audio or not self.input_image:
                raise ValueError("input_audio and input_image are required for TALKING_AVATAR task type")
            
        return self