from enum import Enum

class InferenceSteps(int, Enum):
    FAST = 8
    HighQuality = 25
    SLOW = 50