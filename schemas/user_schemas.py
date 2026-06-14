from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: str
    full_name: str
    password: str

class UserReponse(BaseModel):
    id: int
    email: str
    full_name: str
    is_active: bool
    role: str
    created_at: datetime

class LoginRequest(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

    model_config = {"from_attributes": True}