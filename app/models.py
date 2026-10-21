from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum

# Enums for Input validation
class TaskType(str, Enum):
    SCRIPT_ANALYSIS = "script_analysis"
    REWRITE = "rewrite"
    AVATAR_DELIVERY = "avatar_delivery"
    AUTOMATION = "automation"

class Role(str, Enum):
    NEWS = "news"
    STORYTELLER = "storyteller"
    INFLUENCER = "influencer"
    EDUCATOR = "educator"
    NEUTRAL = "neutral"

class Platform(str, Enum):
    YOUTUBE = "youtube"
    SHORTS = "shorts"
    REELS = "reels"
    PODCAST = "podcast"
    PRESENTATION = "presentation"

class Tone(str, Enum):
    SERIOUS = "serious"
    ENERGETIC = "energetic"
    CALM = "calm"
    DRAMATIC = "dramatic"

class Goal(str, Enum):
    ENGAGEMENT = "engagement"
    CLARITY = "clarity"
    CONVERSION = "conversion"
    AUTOMATION = "automation"

# Input Object
class InputObject(BaseModel):
    task_type: TaskType
    script: Optional[str] = None
    role: Role
    platform: Platform
    audience: str
    tone: Tone
    goal: Goal

# Output Components
class Analysis(BaseModel):
    issues: List[str]
    opportunities: List[str]

class OptimizedScript(BaseModel):
    primary_version: str
    alternate_version: Optional[str] = None
    audio_url: Optional[str] = None

class DeliveryGuidance(BaseModel):
    tone: str
    pace: str
    expressions: str
    emphasis_points: List[str]
    gesture_frequency: float = 0.5  # 0.0 to 1.0
    gesture_types: List[str] = []   # e.g., ["open_palm", "point"]

class ActionStep(BaseModel):
    step: int
    action: str
    tool_required: bool

# Output Object
class OutputObject(BaseModel):
    analysis: Analysis
    optimized_script: OptimizedScript
    delivery_guidance: DeliveryGuidance
    action_plan: List[ActionStep]
