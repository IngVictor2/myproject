from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: TaskPriority
    
class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    priority: TaskPriority 
    status: str 
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: TaskStatus
    priority: TaskPriority
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}