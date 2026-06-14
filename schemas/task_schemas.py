from datetime import datetime
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: str
    
class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    priority: str 
    status: str 
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str
    priority: str
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}