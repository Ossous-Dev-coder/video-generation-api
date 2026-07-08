from enum import Enum

class InferenceSteps(str, Enum):
    FAST = 8
    HighQuality = 25
    SLOW = 50