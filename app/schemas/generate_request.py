from pydantic import BaseModel, model_validator
from typing import Optional

from app.enums.inference_steps import InferenceSteps
from app.enums.task_type import TaskType
from app.enums.resulations import Resolution


class GenerateRequest(BaseModel):

    task_type: TaskType
    prompt: str

    ref_imgs: Optional[list[str]] = None
    input_video: Optional[str] = None
    input_image: Optional[str] = None
    input_audio: Optional[str] = None

    duration: int = 5
    resolution: Resolution = Resolution.P720
    seed: int = 42
    num_inference_steps: InferenceSteps = InferenceSteps.HighQuality
    guidance_scale: float = 5.0
    guidance_scale_img: float = 3.0
    negative_prompt: str = ""
    offload: bool = False
    low_vram: bool = False



    @model_validator(mode="after")

    def validate_request(self):

        if not self.prompt or self.prompt.strip() == "":
            raise ValueError("Prompt cannot be empty.")

        if self.task_type == TaskType.REFERENCE_TO_VIDEO:

            self.validate_reference_to_video()

        elif self.task_type == TaskType.SINGLE_SHOT_EXTENSION:

            self.validate_single_shot_extension()

        elif self.task_type == TaskType.SHOT_SWITCHING_EXTENSION:

            self.validate_shot_switching_extension()

        elif self.task_type == TaskType.TALKING_AVATAR:

            self.validate_talking_avatar()

        return self
    
    def validate_reference_to_video(self) :
        if not self.ref_imgs:
            raise ValueError("ref_imgs is required for REFERENCE_TO_VIDEO")

        if len(self.ref_imgs) > 4:
            raise ValueError("A maximum of 4 reference images is allowed")

        if self.duration < 1 or self.duration > 5:
            raise ValueError("duration must be between 1 and 5 for REFERENCE_TO_VIDEO")

    def validate_single_shot_extension(self):

        if not self.input_video:
            raise ValueError("input_video is required for SINGLE_SHOT_EXTENSION")

        if self.duration < 5 or self.duration > 30:
            raise ValueError("duration must be between 5 and 30 for SINGLE_SHOT_EXTENSION")

    def validate_shot_switching_extension(self):
        if not self.input_video:
            raise ValueError("input_video is required for SHOT_SWITCHING_EXTENSION")

        if self.duration < 1 or self.duration > 5:
            raise ValueError("duration must be between 1 and 5 for SHOT_SWITCHING_EXTENSION")

    def validate_talking_avatar(self):

        if not self.input_image:
            raise ValueError("input_image is required for TALKING_AVATAR")

        if not self.input_audio:
            raise ValueError("input_audio is required for TALKING_AVATAR")

        if self.duration < 1 or self.duration > 200:
            raise ValueError("duration must be between 1 and 200 for TALKING_AVATAR")













