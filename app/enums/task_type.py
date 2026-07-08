from enum import Enum

class TaskType(str, Enum): 
    REFERENCE_TO_VIDEO = "reference_to_video"
    SINGLE_SHOT_EXTENSION = "single_shot_extension"
    SHOT_SWITCHING_EXTENSION = "shot_switching_extension"
    TALKING_AVATAR = "talking_avatar"